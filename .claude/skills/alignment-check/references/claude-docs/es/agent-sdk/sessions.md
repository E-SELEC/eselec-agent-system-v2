---
source_url: https://code.claude.com/docs/es/agent-sdk/sessions
fetched_url: https://code.claude.com/docs/es/agent-sdk/sessions.md
category: SDK de Agente
status: 200
scraped_at: 2026-05-15T14:28:32+00:00
sha256_16: f2d77cf1ab4dbbde
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Trabajar con sesiones

> Cómo las sesiones persisten el historial de conversación del agente, y cuándo usar continue, resume y fork para volver a una ejecución anterior.

Una sesión es el historial de conversación que el SDK acumula mientras su agente trabaja. Contiene su prompt, cada llamada a herramienta que hizo el agente, cada resultado de herramienta y cada respuesta. El SDK la escribe en disco automáticamente para que pueda volver a ella más tarde.

Volver a una sesión significa que el agente tiene contexto completo de antes: archivos que ya leyó, análisis que ya realizó, decisiones que ya tomó. Puede hacer una pregunta de seguimiento, recuperarse de una interrupción o ramificarse para probar un enfoque diferente.

<Note>
  Las sesiones persisten la **conversación**, no el sistema de archivos. Para capturar y revertir cambios de archivos que hizo el agente, use [file checkpointing](/es/agent-sdk/file-checkpointing).
</Note>

Esta guía cubre cómo elegir el enfoque correcto para su aplicación, las interfaces del SDK que rastrean sesiones automáticamente, cómo capturar IDs de sesión y usar `resume` y `fork` manualmente, y qué debe saber sobre reanudar sesiones entre hosts.

## Elegir un enfoque

Cuánto manejo de sesiones necesita depende de la forma de su aplicación. La gestión de sesiones entra en juego cuando envía múltiples prompts que deben compartir contexto. Dentro de una única llamada `query()`, el agente ya toma tantos turnos como necesita, y los prompts de permiso y `AskUserQuestion` se [manejan en bucle](/es/agent-sdk/user-input) (no terminan la llamada).

| Lo que está construyendo                                            | Qué usar                                                                                                                                                                      |
| :------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tarea de una sola vez: prompt único, sin seguimiento                | Nada extra. Una llamada `query()` lo maneja.                                                                                                                                  |
| Chat multi-turno en un proceso                                      | [`ClaudeSDKClient` (Python) o `continue: true` (TypeScript)](#automatic-session-management). El SDK rastrea la sesión para usted sin manejo de ID.                            |
| Continuar donde lo dejó después de un reinicio de proceso           | `continue_conversation=True` (Python) / `continue: true` (TypeScript). Reanuda la sesión más reciente en el directorio, sin ID necesario.                                     |
| Reanudar una sesión pasada específica (no la más reciente)          | Capture el ID de sesión y páselo a `resume`.                                                                                                                                  |
| Probar un enfoque alternativo sin perder el original                | Bifurque la sesión.                                                                                                                                                           |
| Tarea sin estado, no quiere nada escrito en disco (solo TypeScript) | Establezca [`persistSession: false`](/es/agent-sdk/typescript#options). La sesión existe solo en memoria durante la duración de la llamada. Python siempre persiste en disco. |

### Continue, resume y fork

Continue, resume y fork son campos de opción que establece en `query()` ([`ClaudeAgentOptions`](/es/agent-sdk/python#claudeagentoptions) en Python, [`Options`](/es/agent-sdk/typescript#options) en TypeScript).

**Continue** y **resume** ambos retoman una sesión existente y la amplían. La diferencia es cómo encuentran esa sesión:

* **Continue** encuentra la sesión más reciente en el directorio actual. No rastrea nada. Funciona bien cuando su aplicación ejecuta una conversación a la vez.
* **Resume** toma un ID de sesión específico. Rastrea el ID. Requerido cuando tiene múltiples sesiones (por ejemplo, una por usuario en una aplicación multiusuario) o desea volver a una que no sea la más reciente.

**Fork** es diferente: crea una nueva sesión que comienza con una copia del historial del original. El original permanece sin cambios. Use fork para probar una dirección diferente mientras mantiene la opción de volver atrás.

## Gestión automática de sesiones

Ambos SDKs ofrecen una interfaz que rastrea el estado de la sesión para usted entre llamadas, por lo que no pasa IDs alrededor manualmente. Use estos para conversaciones multi-turno dentro de un único proceso.

### Python: `ClaudeSDKClient`

[`ClaudeSDKClient`](/es/agent-sdk/python#claudesdkclient) maneja IDs de sesión internamente. Cada llamada a `client.query()` continúa automáticamente la misma sesión. Llame a [`client.receive_response()`](/es/agent-sdk/python#claudesdkclient) para iterar sobre los mensajes de la consulta actual. El cliente debe usarse como un gestor de contexto asincrónico.

Este ejemplo ejecuta dos consultas contra el mismo `client`. La primera le pide al agente que analice un módulo; la segunda le pide que refactorice ese módulo. Debido a que ambas llamadas van a través de la misma instancia de cliente, la segunda consulta tiene contexto completo de la primera sin ningún `resume` explícito o ID de sesión:

```python Python theme={null}
import asyncio
from claude_agent_sdk import (
    ClaudeSDKClient,
    ClaudeAgentOptions,
    AssistantMessage,
    ResultMessage,
    TextBlock,
)


def print_response(message):
    """Print only the human-readable parts of a message."""
    if isinstance(message, AssistantMessage):
        for block in message.content:
            if isinstance(block, TextBlock):
                print(block.text)
    elif isinstance(message, ResultMessage):
        cost = (
            f"${message.total_cost_usd:.4f}"
            if message.total_cost_usd is not None
            else "N/A"
        )
        print(f"[done: {message.subtype}, cost: {cost}]")


async def main():
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Edit", "Glob", "Grep"],
    )

    async with ClaudeSDKClient(options=options) as client:
        # First query: client captures the session ID internally
        await client.query("Analyze the auth module")
        async for message in client.receive_response():
            print_response(message)

        # Second query: automatically continues the same session
        await client.query("Now refactor it to use JWT")
        async for message in client.receive_response():
            print_response(message)


asyncio.run(main())
```

Vea la [referencia del SDK de Python](/es/agent-sdk/python#choosing-between-query-and-claudesdkclient) para detalles sobre cuándo usar `ClaudeSDKClient` versus la función `query()` independiente.

### TypeScript: `continue: true`

El SDK de TypeScript estable (la función `query()` utilizada en toda esta documentación, a veces llamada V1) no tiene un objeto cliente que mantenga sesión como el `ClaudeSDKClient` de Python. En su lugar, pase `continue: true` en cada llamada `query()` posterior y el SDK retoma la sesión más reciente en el directorio actual. No se requiere seguimiento de ID.

Este ejemplo hace dos llamadas `query()` separadas. La primera crea una sesión nueva; la segunda establece `continue: true`, que le dice al SDK que encuentre y reanude la sesión más reciente en disco. El agente tiene contexto completo de la primera llamada:

```typescript TypeScript theme={null}
import { query } from "@anthropic-ai/claude-agent-sdk";

// First query: creates a new session
for await (const message of query({
  prompt: "Analyze the auth module",
  options: { allowedTools: ["Read", "Glob", "Grep"] }
})) {
  if (message.type === "result" && message.subtype === "success") {
    console.log(message.result);
  }
}

// Second query: continue: true resumes the most recent session
for await (const message of query({
  prompt: "Now refactor it to use JWT",
  options: {
    continue: true,
    allowedTools: ["Read", "Edit", "Write", "Glob", "Grep"]
  }
})) {
  if (message.type === "result" && message.subtype === "success") {
    console.log(message.result);
  }
}
```

<Note>
  La [API de sesión V2](/es/agent-sdk/typescript-v2-preview) experimental, que proporcionaba `createSession()` con un patrón `send` / `stream`, está deprecada. Use la función V1 `query()` y las opciones de sesión descritas en esta página en su lugar.
</Note>

## Usar opciones de sesión con `query()`

### Capturar el ID de sesión

Resume y fork requieren un ID de sesión. Léalo del campo `session_id` en el mensaje de resultado ([`ResultMessage`](/es/agent-sdk/python#resultmessage) en Python, [`SDKResultMessage`](/es/agent-sdk/typescript#sdkresultmessage) en TypeScript), que está presente en cada resultado independientemente del éxito o error. En TypeScript, el ID también está disponible antes como un campo directo en el `SystemMessage` de inicio; en Python está anidado dentro de `SystemMessage.data`.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage


  async def main():
      session_id = None

      async for message in query(
          prompt="Analyze the auth module and suggest improvements",
          options=ClaudeAgentOptions(
              allowed_tools=["Read", "Glob", "Grep"],
          ),
      ):
          if isinstance(message, ResultMessage):
              session_id = message.session_id
              if message.subtype == "success":
                  print(message.result)

      print(f"Session ID: {session_id}")
      return session_id


  session_id = asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  let sessionId: string | undefined;

  for await (const message of query({
    prompt: "Analyze the auth module and suggest improvements",
    options: { allowedTools: ["Read", "Glob", "Grep"] }
  })) {
    if (message.type === "result") {
      sessionId = message.session_id;
      if (message.subtype === "success") {
        console.log(message.result);
      }
    }
  }

  console.log(`Session ID: ${sessionId}`);
  ```
</CodeGroup>

### Reanudar por ID

Pase un ID de sesión a `resume` para volver a esa sesión específica. El agente retoma con contexto completo de donde la sesión se quedó. Las razones comunes para reanudar son:

* **Seguimiento en una tarea completada.** El agente ya analizó algo; ahora quiere que actúe sobre ese análisis sin releer archivos.
* **Recuperarse de un límite.** La primera ejecución terminó con `error_max_turns` o `error_max_budget_usd` (vea [Manejar el resultado](/es/agent-sdk/agent-loop#handle-the-result)); reanude con un límite más alto.
* **Reiniciar su proceso.** Capturó el ID antes del apagado y desea restaurar la conversación.

Este ejemplo reanuda la sesión de [Capturar el ID de sesión](#capture-the-session-id) con un prompt de seguimiento. Debido a que está reanudando, el agente ya tiene el análisis anterior en contexto:

<CodeGroup>
  ```python Python theme={null}
  # Earlier session analyzed the code; now build on that analysis
  async for message in query(
      prompt="Now implement the refactoring you suggested",
      options=ClaudeAgentOptions(
          resume=session_id,
          allowed_tools=["Read", "Edit", "Write", "Glob", "Grep"],
      ),
  ):
      if isinstance(message, ResultMessage) and message.subtype == "success":
          print(message.result)
  ```

  ```typescript TypeScript theme={null}
  // Earlier session analyzed the code; now build on that analysis
  for await (const message of query({
    prompt: "Now implement the refactoring you suggested",
    options: {
      resume: sessionId,
      allowedTools: ["Read", "Edit", "Write", "Glob", "Grep"]
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```
</CodeGroup>

<Tip>
  Si una llamada `resume` devuelve una sesión nueva en lugar del historial esperado, la causa más común es un `cwd` no coincidente. Las sesiones se almacenan bajo `~/.claude/projects/<encoded-cwd>/*.jsonl`, donde `<encoded-cwd>` es el directorio de trabajo absoluto con cada carácter no alfanumérico reemplazado por `-` (entonces `/Users/me/proj` se convierte en `-Users-me-proj`). Si su llamada resume se ejecuta desde un directorio diferente, el SDK busca en el lugar incorrecto. El archivo de sesión también necesita existir en la máquina actual.
</Tip>

Para reanudar sesiones entre máquinas o en entornos sin servidor, refleje transcripciones en almacenamiento compartido con un adaptador [`SessionStore`](/es/agent-sdk/session-storage).

### Bifurcar para explorar alternativas

Bifurcar crea una nueva sesión que comienza con una copia del historial del original pero diverge desde ese punto. La bifurcación obtiene su propio ID de sesión; el ID y el historial del original permanecen sin cambios. Termina con dos sesiones independientes que puede reanudar por separado.

<Note>
  Bifurcar ramifica el historial de conversación, no el sistema de archivos. Si un agente bifurcado edita archivos, esos cambios son reales y visibles para cualquier sesión que trabaje en el mismo directorio. Para ramificar y revertir cambios de archivos, use [file checkpointing](/es/agent-sdk/file-checkpointing).
</Note>

Este ejemplo se basa en [Capturar el ID de sesión](#capture-the-session-id): ya ha analizado un módulo de autenticación en `session_id` y desea explorar OAuth2 sin perder el hilo enfocado en JWT. El primer bloque bifurca la sesión y captura el ID de la bifurcación (`forked_id`); el segundo bloque reanuda el `session_id` original para continuar por el camino JWT. Ahora tiene dos IDs de sesión apuntando a dos historiales separados:

<CodeGroup>
  ```python Python theme={null}
  # Fork: branch from session_id into a new session
  forked_id = None
  async for message in query(
      prompt="Instead of JWT, implement OAuth2 for the auth module",
      options=ClaudeAgentOptions(
          resume=session_id,
          fork_session=True,
      ),
  ):
      if isinstance(message, ResultMessage):
          forked_id = message.session_id  # The fork's ID, distinct from session_id
          if message.subtype == "success":
              print(message.result)

  print(f"Forked session: {forked_id}")

  # Original session is untouched; resuming it continues the JWT thread
  async for message in query(
      prompt="Continue with the JWT approach",
      options=ClaudeAgentOptions(resume=session_id),
  ):
      if isinstance(message, ResultMessage) and message.subtype == "success":
          print(message.result)
  ```

  ```typescript TypeScript theme={null}
  // Fork: branch from sessionId into a new session
  let forkedId: string | undefined;

  for await (const message of query({
    prompt: "Instead of JWT, implement OAuth2 for the auth module",
    options: {
      resume: sessionId,
      forkSession: true
    }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      forkedId = message.session_id; // The fork's ID, distinct from sessionId
    }
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }

  console.log(`Forked session: ${forkedId}`);

  // Original session is untouched; resuming it continues the JWT thread
  for await (const message of query({
    prompt: "Continue with the JWT approach",
    options: { resume: sessionId }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```
</CodeGroup>

## Reanudar entre hosts

Los archivos de sesión son locales a la máquina que los creó. Para reanudar una sesión en un host diferente (trabajadores de CI, contenedores efímeros, sin servidor), tiene dos opciones:

* **Mover el archivo de sesión.** Persista `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl` de la primera ejecución y restáurelo a la misma ruta en el nuevo host antes de llamar a `resume`. El `cwd` debe coincidir.
* **No confíe en la reanudación de sesión.** Capture los resultados que necesita (salida de análisis, decisiones, diffs de archivos) como estado de aplicación y páselos al prompt de una sesión nueva. Esto a menudo es más robusto que enviar archivos de transcripción.

Ambos SDKs exponen funciones para enumerar sesiones en disco y leer sus mensajes: [`listSessions()`](/es/agent-sdk/typescript#listsessions) y [`getSessionMessages()`](/es/agent-sdk/typescript#getsessionmessages) en TypeScript, [`list_sessions()`](/es/agent-sdk/python#list_sessions) y [`get_session_messages()`](/es/agent-sdk/python#get_session_messages) en Python. Úselos para construir selectores de sesión personalizados, lógica de limpieza o visores de transcripción.

Ambos SDKs también exponen funciones para buscar y mutar sesiones individuales: [`get_session_info()`](/es/agent-sdk/python#get_session_info), [`rename_session()`](/es/agent-sdk/python#rename_session) y [`tag_session()`](/es/agent-sdk/python#tag_session) en Python, y [`getSessionInfo()`](/es/agent-sdk/typescript#getsessioninfo), [`renameSession()`](/es/agent-sdk/typescript#renamesession) y [`tagSession()`](/es/agent-sdk/typescript#tagsession) en TypeScript. Úselos para organizar sesiones por etiqueta o darles títulos legibles por humanos.

## Recursos relacionados

* [Cómo funciona el bucle del agente](/es/agent-sdk/agent-loop): Comprenda turnos, mensajes y acumulación de contexto dentro de una sesión
* [File checkpointing](/es/agent-sdk/file-checkpointing): Rastrear y revertir cambios de archivos entre sesiones
* [Python `ClaudeAgentOptions`](/es/agent-sdk/python#claudeagentoptions): Referencia completa de opciones de sesión para Python
* [TypeScript `Options`](/es/agent-sdk/typescript#options): Referencia completa de opciones de sesión para TypeScript
