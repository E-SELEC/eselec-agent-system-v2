---
source_url: https://code.claude.com/docs/es/agent-sdk/hooks
fetched_url: https://code.claude.com/docs/es/agent-sdk/hooks.md
category: SDK de Agente
status: 200
scraped_at: 2026-05-15T14:28:35+00:00
sha256_16: 8f69dc53d4ec4aa2
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Interceptar y controlar el comportamiento del agente con hooks

> Interceptar y personalizar el comportamiento del agente en puntos clave de ejecución con hooks

Los hooks son funciones de devolución de llamada que ejecutan su código en respuesta a eventos del agente, como una herramienta siendo llamada, una sesión iniciándose, o la ejecución deteniéndose. Con hooks, puede:

* **Bloquear operaciones peligrosas** antes de que se ejecuten, como comandos de shell destructivos o acceso a archivos no autorizado
* **Registrar y auditar** cada llamada de herramienta para cumplimiento, depuración o análisis
* **Transformar entradas y salidas** para desinfectar datos, inyectar credenciales o redirigir rutas de archivos
* **Requerir aprobación humana** para acciones sensibles como escrituras en bases de datos o llamadas a API
* **Rastrear el ciclo de vida de la sesión** para gestionar estado, limpiar recursos o enviar notificaciones

Esta guía cubre cómo funcionan los hooks, cómo configurarlos, y proporciona ejemplos para patrones comunes como bloquear herramientas, modificar entradas y reenviar notificaciones.

## Cómo funcionan los hooks

<Steps>
  <Step title="Se dispara un evento">
    Algo sucede durante la ejecución del agente y el SDK dispara un evento: una herramienta está a punto de ser llamada (`PreToolUse`), una herramienta devolvió un resultado (`PostToolUse`), un subagente se inició o se detuvo, el agente está inactivo, o la ejecución finalizó. Vea la [lista completa de eventos](#available-hooks).
  </Step>

  <Step title="El SDK recopila hooks registrados">
    El SDK verifica si hay hooks registrados para ese tipo de evento. Esto incluye hooks de devolución de llamada que pasa en `options.hooks` y hooks de comandos de shell de archivos de configuración cuando la entrada [`settingSources`](/es/agent-sdk/typescript#settingSources) o [`setting_sources`](/es/agent-sdk/python#settingSources) correspondiente está habilitada, lo cual lo está para las opciones predeterminadas de `query()`.
  </Step>

  <Step title="Los matchers filtran qué hooks se ejecutan">
    Si un hook tiene un patrón [`matcher`](#matchers) (como `"Write|Edit"`), el SDK lo prueba contra el objetivo del evento (por ejemplo, el nombre de la herramienta). Los hooks sin un matcher se ejecutan para cada evento de ese tipo.
  </Step>

  <Step title="Se ejecutan las funciones de devolución de llamada">
    Cada hook coincidente recibe su [función de devolución de llamada](#callback-functions) con información sobre lo que está sucediendo: el nombre de la herramienta, sus argumentos, el ID de sesión y otros detalles específicos del evento.
  </Step>

  <Step title="Su devolución de llamada devuelve una decisión">
    Después de realizar cualquier operación (registro, llamadas a API, validación), su devolución de llamada devuelve un [objeto de salida](#outputs) que le dice al agente qué hacer: permitir la operación, bloquearla, modificar la entrada o inyectar contexto en la conversación.
  </Step>
</Steps>

El siguiente ejemplo reúne estos pasos. Registra un hook `PreToolUse` (paso 1) con un matcher `"Write|Edit"` (paso 3) para que la devolución de llamada solo se dispare para herramientas de escritura de archivos. Cuando se activa, la devolución de llamada recibe la entrada de la herramienta (paso 4), verifica si la ruta del archivo apunta a un archivo `.env`, y devuelve `permissionDecision: "deny"` para bloquear la operación (paso 5):

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import (
      AssistantMessage,
      ClaudeSDKClient,
      ClaudeAgentOptions,
      HookMatcher,
      ResultMessage,
  )


  # Define a hook callback that receives tool call details
  async def protect_env_files(input_data, tool_use_id, context):
      # Extract the file path from the tool's input arguments
      file_path = input_data["tool_input"].get("file_path", "")
      file_name = file_path.split("/")[-1]

      # Block the operation if targeting a .env file
      if file_name == ".env":
          return {
              "hookSpecificOutput": {
                  "hookEventName": input_data["hook_event_name"],
                  "permissionDecision": "deny",
                  "permissionDecisionReason": "Cannot modify .env files",
              }
          }

      # Return empty object to allow the operation
      return {}


  async def main():
      options = ClaudeAgentOptions(
          hooks={
              # Register the hook for PreToolUse events
              # The matcher filters to only Write and Edit tool calls
              "PreToolUse": [HookMatcher(matcher="Write|Edit", hooks=[protect_env_files])]
          }
      )

      async with ClaudeSDKClient(options=options) as client:
          await client.query("Update the database configuration")
          async for message in client.receive_response():
              # Filter for assistant and result messages
              if isinstance(message, (AssistantMessage, ResultMessage)):
                  print(message)


  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import { query, HookCallback, PreToolUseHookInput } from "@anthropic-ai/claude-agent-sdk";

  // Define a hook callback with the HookCallback type
  const protectEnvFiles: HookCallback = async (input, toolUseID, { signal }) => {
    // Cast input to the specific hook type for type safety
    const preInput = input as PreToolUseHookInput;

    // Cast tool_input to access its properties (typed as unknown in the SDK)
    const toolInput = preInput.tool_input as Record<string, unknown>;
    const filePath = toolInput?.file_path as string;
    const fileName = filePath?.split("/").pop();

    // Block the operation if targeting a .env file
    if (fileName === ".env") {
      return {
        hookSpecificOutput: {
          hookEventName: preInput.hook_event_name,
          permissionDecision: "deny",
          permissionDecisionReason: "Cannot modify .env files"
        }
      };
    }

    // Return empty object to allow the operation
    return {};
  };

  for await (const message of query({
    prompt: "Update the database configuration",
    options: {
      hooks: {
        // Register the hook for PreToolUse events
        // The matcher filters to only Write and Edit tool calls
        PreToolUse: [{ matcher: "Write|Edit", hooks: [protectEnvFiles] }]
      }
    }
  })) {
    // Filter for assistant and result messages
    if (message.type === "assistant" || message.type === "result") {
      console.log(message);
    }
  }
  ```
</CodeGroup>

## Hooks disponibles

El SDK proporciona hooks para diferentes etapas de la ejecución del agente. Algunos hooks están disponibles en ambos SDK, mientras que otros son solo para TypeScript.

| Evento de Hook       | SDK de Python | SDK de TypeScript | Qué lo dispara                                                                                                     | Caso de uso de ejemplo                                          |
| -------------------- | ------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| `PreToolUse`         | Sí            | Sí                | Solicitud de llamada de herramienta (puede bloquear o modificar)                                                   | Bloquear comandos de shell peligrosos                           |
| `PostToolUse`        | Sí            | Sí                | Resultado de ejecución de herramienta                                                                              | Registrar todos los cambios de archivo en pista de auditoría    |
| `PostToolUseFailure` | Sí            | Sí                | Fallo de ejecución de herramienta                                                                                  | Manejar o registrar errores de herramienta                      |
| `PostToolBatch`      | No            | Sí                | Un lote completo de llamadas de herramienta se resuelve, una vez por lote antes de la siguiente llamada del modelo | Inyectar convenciones una vez para todo el lote                 |
| `UserPromptSubmit`   | Sí            | Sí                | Envío de solicitud del usuario                                                                                     | Inyectar contexto adicional en solicitudes                      |
| `Stop`               | Sí            | Sí                | Detención de ejecución del agente                                                                                  | Guardar estado de sesión antes de salir                         |
| `SubagentStart`      | Sí            | Sí                | Inicialización de subagente                                                                                        | Rastrear generación de tareas paralelas                         |
| `SubagentStop`       | Sí            | Sí                | Finalización de subagente                                                                                          | Agregar resultados de tareas paralelas                          |
| `PreCompact`         | Sí            | Sí                | Solicitud de compactación de conversación                                                                          | Archivar transcripción completa antes de resumir                |
| `PermissionRequest`  | Sí            | Sí                | Se mostraría diálogo de permiso                                                                                    | Manejo de permisos personalizado                                |
| `SessionStart`       | No            | Sí                | Inicialización de sesión                                                                                           | Inicializar registro y telemetría                               |
| `SessionEnd`         | No            | Sí                | Terminación de sesión                                                                                              | Limpiar recursos temporales                                     |
| `Notification`       | Sí            | Sí                | Mensajes de estado del agente                                                                                      | Enviar actualizaciones de estado del agente a Slack o PagerDuty |
| `Setup`              | No            | Sí                | Configuración/mantenimiento de sesión                                                                              | Ejecutar tareas de inicialización                               |
| `TeammateIdle`       | No            | Sí                | El compañero se vuelve inactivo                                                                                    | Reasignar trabajo o notificar                                   |
| `TaskCompleted`      | No            | Sí                | Tarea de fondo se completa                                                                                         | Agregar resultados de tareas paralelas                          |
| `ConfigChange`       | No            | Sí                | Archivo de configuración cambia                                                                                    | Recargar configuración dinámicamente                            |
| `WorktreeCreate`     | No            | Sí                | Git worktree creado                                                                                                | Rastrear espacios de trabajo aislados                           |
| `WorktreeRemove`     | No            | Sí                | Git worktree eliminado                                                                                             | Limpiar recursos de espacio de trabajo                          |

## Configurar hooks

Para configurar un hook, páselo en el campo `hooks` de sus opciones de agente (`ClaudeAgentOptions` en Python, el objeto `options` en TypeScript):

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      hooks={"PreToolUse": [HookMatcher(matcher="Bash", hooks=[my_callback])]}
  )

  async with ClaudeSDKClient(options=options) as client:
      await client.query("Your prompt")
      async for message in client.receive_response():
          print(message)
  ```

  ```typescript TypeScript theme={null}
  for await (const message of query({
    prompt: "Your prompt",
    options: {
      hooks: {
        PreToolUse: [{ matcher: "Bash", hooks: [myCallback] }]
      }
    }
  })) {
    console.log(message);
  }
  ```
</CodeGroup>

La opción `hooks` es un diccionario (Python) u objeto (TypeScript) donde:

* **Las claves** son [nombres de eventos de hook](#available-hooks) (por ejemplo, `'PreToolUse'`, `'PostToolUse'`, `'Stop'`)
* **Los valores** son matrices de [matchers](#matchers), cada una conteniendo un patrón de filtro opcional y sus [funciones de devolución de llamada](#callback-functions)

### Matchers

Use matchers para filtrar cuándo se disparan sus devoluciones de llamada. El campo `matcher` es una cadena regex que coincide con un valor diferente dependiendo del tipo de evento de hook. Por ejemplo, los hooks basados en herramientas coinciden con el nombre de la herramienta, mientras que los hooks `Notification` coinciden con el tipo de notificación. Vea la [referencia de hooks de Claude Code](/es/hooks#matcher-patterns) para la lista completa de valores de matcher para cada tipo de evento.

| Opción    | Tipo             | Predeterminado | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------- | ---------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `matcher` | `string`         | `undefined`    | Patrón regex coincidido contra el campo de filtro del evento. Para hooks de herramientas, este es el nombre de la herramienta. Las herramientas integradas incluyen `Bash`, `Read`, `Write`, `Edit`, `Glob`, `Grep`, `WebFetch`, `Agent` y otros (vea [Tipos de entrada de herramienta](/es/agent-sdk/typescript#tool-input-types) para la lista completa). Las herramientas MCP usan el patrón `mcp__<server>__<action>`. |
| `hooks`   | `HookCallback[]` | -              | Requerido. Matriz de funciones de devolución de llamada a ejecutar cuando el patrón coincide                                                                                                                                                                                                                                                                                                                               |
| `timeout` | `number`         | `60`           | Tiempo de espera en segundos                                                                                                                                                                                                                                                                                                                                                                                               |

Use el patrón `matcher` para dirigirse a herramientas específicas siempre que sea posible. Un matcher con `'Bash'` solo se ejecuta para comandos Bash, mientras que omitir el patrón ejecuta sus devoluciones de llamada para cada ocurrencia del evento. Tenga en cuenta que para hooks basados en herramientas, los matchers solo filtran por **nombre de herramienta**, no por rutas de archivo u otros argumentos. Para filtrar por ruta de archivo, verifique `tool_input.file_path` dentro de su devolución de llamada.

<Tip>
  **Descubriendo nombres de herramientas:** Vea [Tipos de entrada de herramienta](/es/agent-sdk/typescript#tool-input-types) para la lista completa de nombres de herramientas integradas, o agregue un hook sin un matcher para registrar todas las llamadas de herramienta que su sesión realiza.

  **Nomenclatura de herramientas MCP:** Las herramientas MCP siempre comienzan con `mcp__` seguido del nombre del servidor y la acción: `mcp__<server>__<action>`. Por ejemplo, si configura un servidor llamado `playwright`, sus herramientas se nombrarán `mcp__playwright__browser_screenshot`, `mcp__playwright__browser_click`, etc. El nombre del servidor proviene de la clave que usa en la configuración `mcpServers`.
</Tip>

### Funciones de devolución de llamada

#### Entradas

Cada devolución de llamada de hook recibe tres argumentos:

* **Datos de entrada:** un objeto tipado que contiene detalles del evento. Cada tipo de hook tiene su propia forma de entrada (por ejemplo, `PreToolUseHookInput` incluye `tool_name` y `tool_input`, mientras que `NotificationHookInput` incluye `message`). Vea las definiciones de tipo completas en las referencias del SDK de [TypeScript](/es/agent-sdk/typescript#hookinput) y [Python](/es/agent-sdk/python#hookinput).
  * Todas las entradas de hook comparten `session_id`, `cwd` y `hook_event_name`.
  * `agent_id` y `agent_type` se rellenan cuando el hook se dispara dentro de un subagente. En TypeScript, estos están en la entrada de hook base y disponibles para todos los tipos de hook. En Python, están solo en `PreToolUse`, `PostToolUse` y `PostToolUseFailure`.
* **ID de uso de herramienta** (`str | None` / `string | undefined`): correlaciona eventos `PreToolUse` y `PostToolUse` para la misma llamada de herramienta.
* **Contexto:** en TypeScript, contiene una propiedad `signal` (`AbortSignal`) para cancelación. En Python, este argumento está reservado para uso futuro.

#### Salidas

Su devolución de llamada devuelve un objeto con dos categorías de campos:

* **Campos de nivel superior** funcionan igual en cada evento: `systemMessage` muestra un mensaje al usuario, y `continue` (`continue_` en Python) determina si el agente sigue ejecutándose después de este hook.
* **`hookSpecificOutput`** controla la operación actual. Los campos dentro dependen del tipo de evento de hook. Para hooks `PreToolUse`, aquí es donde establece `permissionDecision` (`"allow"`, `"deny"`, `"ask"` o `"defer"`), `permissionDecisionReason` e `updatedInput`. Devolver `"defer"` finaliza la consulta para que pueda [reanudarla más tarde](/es/hooks#defer-a-tool-call-for-later). Para hooks `PostToolUse`, puede establecer `additionalContext` para agregar información al resultado de la herramienta, o `updatedToolOutput` para reemplazar completamente la salida de la herramienta antes de que Claude la vea.

Devuelva `{}` para permitir la operación sin cambios. Los hooks de devolución de llamada del SDK usan el mismo formato de salida JSON que [hooks de comandos de shell de Claude Code](/es/hooks#json-output), que documenta cada campo y opción específica del evento. Para las definiciones de tipo del SDK, vea las referencias del SDK de [TypeScript](/es/agent-sdk/typescript#synchookjsonoutput) y [Python](/es/agent-sdk/python#synchookjsonoutput).

<Note>
  Cuando se aplican múltiples hooks o reglas de permiso, **deny** tiene prioridad sobre **defer**, que tiene prioridad sobre **ask**, que tiene prioridad sobre **allow**. Si algún hook devuelve `deny`, la operación se bloquea independientemente de otros hooks.
</Note>

#### Salida asincrónica

De forma predeterminada, el agente espera a que su hook devuelva antes de continuar. Si su hook realiza un efecto secundario (registro, envío de webhook) y no necesita influir en el comportamiento del agente, puede devolver una salida asincrónica en su lugar. Esto le dice al agente que continúe inmediatamente sin esperar a que el hook termine:

<CodeGroup>
  ```python Python theme={null}
  async def async_hook(input_data, tool_use_id, context):
      # Start a background task, then return immediately
      asyncio.create_task(send_to_logging_service(input_data))
      return {"async_": True, "asyncTimeout": 30000}
  ```

  ```typescript TypeScript theme={null}
  const asyncHook: HookCallback = async (input, toolUseID, { signal }) => {
    // Start a background task, then return immediately
    sendToLoggingService(input).catch(console.error);
    return { async: true, asyncTimeout: 30000 };
  };
  ```
</CodeGroup>

| Campo          | Tipo     | Descripción                                                                                                              |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| `async`        | `true`   | Señala modo asincrónico. El agente continúa sin esperar. En Python, use `async_` para evitar la palabra clave reservada. |
| `asyncTimeout` | `number` | Tiempo de espera opcional en milisegundos para la operación de fondo                                                     |

<Note>
  Las salidas asincrónicas no pueden bloquear, modificar o inyectar contexto en la operación ya que el agente ya ha avanzado. Úselas solo para efectos secundarios como registro, métricas o notificaciones.
</Note>

## Ejemplos

### Modificar entrada de herramienta

Este ejemplo intercepta llamadas de herramienta Write y reescribe el argumento `file_path` para anteponer `/sandbox`, redirigiendo todas las escrituras de archivo a un directorio aislado. La devolución de llamada devuelve `updatedInput` con la ruta modificada y `permissionDecision: 'allow'` para aprobar automáticamente la operación reescrita:

<CodeGroup>
  ```python Python theme={null}
  async def redirect_to_sandbox(input_data, tool_use_id, context):
      if input_data["hook_event_name"] != "PreToolUse":
          return {}

      if input_data["tool_name"] == "Write":
          original_path = input_data["tool_input"].get("file_path", "")
          return {
              "hookSpecificOutput": {
                  "hookEventName": input_data["hook_event_name"],
                  "permissionDecision": "allow",
                  "updatedInput": {
                      **input_data["tool_input"],
                      "file_path": f"/sandbox{original_path}",
                  },
              }
          }
      return {}
  ```

  ```typescript TypeScript theme={null}
  const redirectToSandbox: HookCallback = async (input, toolUseID, { signal }) => {
    if (input.hook_event_name !== "PreToolUse") return {};

    const preInput = input as PreToolUseHookInput;
    const toolInput = preInput.tool_input as Record<string, unknown>;
    if (preInput.tool_name === "Write") {
      const originalPath = toolInput.file_path as string;
      return {
        hookSpecificOutput: {
          hookEventName: preInput.hook_event_name,
          permissionDecision: "allow",
          updatedInput: {
            ...toolInput,
            file_path: `/sandbox${originalPath}`
          }
        }
      };
    }
    return {};
  };
  ```
</CodeGroup>

<Note>
  Cuando use `updatedInput`, también debe incluir `permissionDecision: 'allow'` para aprobar automáticamente la entrada modificada o `permissionDecision: 'ask'` para mostrársela al usuario. Con `'defer'`, `updatedInput` se ignora. Siempre devuelva un nuevo objeto en lugar de mutar el `tool_input` original.
</Note>

### Agregar contexto y bloquear una herramienta

Este ejemplo bloquea escrituras en el directorio `/etc` y explica por qué tanto al modelo como al usuario:

* `permissionDecision: 'deny'` detiene la llamada de herramienta.
* `permissionDecisionReason` le dice al modelo por qué, para que evite reintentar.
* `systemMessage` muestra al usuario qué sucedió.

<CodeGroup>
  ```python Python theme={null}
  async def block_etc_writes(input_data, tool_use_id, context):
      file_path = input_data["tool_input"].get("file_path", "")

      if file_path.startswith("/etc"):
          return {
              # Top-level field: message shown to the user
              "systemMessage": "Remember: system directories like /etc are protected.",
              # hookSpecificOutput: block the operation
              "hookSpecificOutput": {
                  "hookEventName": input_data["hook_event_name"],
                  "permissionDecision": "deny",
                  "permissionDecisionReason": "Writing to /etc is not allowed",
              },
          }
      return {}
  ```

  ```typescript TypeScript theme={null}
  const blockEtcWrites: HookCallback = async (input, toolUseID, { signal }) => {
    const preInput = input as PreToolUseHookInput;
    const toolInput = preInput.tool_input as Record<string, unknown>;
    const filePath = toolInput?.file_path as string;

    if (filePath?.startsWith("/etc")) {
      return {
        // Top-level field: message shown to the user
        systemMessage: "Remember: system directories like /etc are protected.",
        // hookSpecificOutput: block the operation
        hookSpecificOutput: {
          hookEventName: preInput.hook_event_name,
          permissionDecision: "deny",
          permissionDecisionReason: "Writing to /etc is not allowed"
        }
      };
    }
    return {};
  };
  ```
</CodeGroup>

### Aprobar automáticamente herramientas específicas

De forma predeterminada, el agente puede solicitar permiso antes de usar ciertas herramientas. Este ejemplo aprueba automáticamente herramientas del sistema de archivos de solo lectura (Read, Glob, Grep) devolviendo `permissionDecision: 'allow'`, permitiéndoles ejecutarse sin confirmación del usuario mientras deja todas las otras herramientas sujetas a verificaciones de permiso normales:

<CodeGroup>
  ```python Python theme={null}
  async def auto_approve_read_only(input_data, tool_use_id, context):
      if input_data["hook_event_name"] != "PreToolUse":
          return {}

      read_only_tools = ["Read", "Glob", "Grep"]
      if input_data["tool_name"] in read_only_tools:
          return {
              "hookSpecificOutput": {
                  "hookEventName": input_data["hook_event_name"],
                  "permissionDecision": "allow",
                  "permissionDecisionReason": "Read-only tool auto-approved",
              }
          }
      return {}
  ```

  ```typescript TypeScript theme={null}
  const autoApproveReadOnly: HookCallback = async (input, toolUseID, { signal }) => {
    if (input.hook_event_name !== "PreToolUse") return {};

    const preInput = input as PreToolUseHookInput;
    const readOnlyTools = ["Read", "Glob", "Grep"];
    if (readOnlyTools.includes(preInput.tool_name)) {
      return {
        hookSpecificOutput: {
          hookEventName: preInput.hook_event_name,
          permissionDecision: "allow",
          permissionDecisionReason: "Read-only tool auto-approved"
        }
      };
    }
    return {};
  };
  ```
</CodeGroup>

### Registrar múltiples hooks

Cuando se dispara un evento, todos los hooks coincidentes se ejecutan en paralelo. Para decisiones de permiso, el resultado más restrictivo gana: un único `deny` bloquea la llamada de herramienta independientemente de lo que devuelvan los otros hooks. Debido a que el orden de finalización es no determinista, escriba cada hook para actuar de forma independiente en lugar de depender de que otro hook se haya ejecutado primero.

El ejemplo a continuación registra tres verificaciones independientes para cada llamada de herramienta:

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      hooks={
          "PreToolUse": [
              HookMatcher(hooks=[authorization_check]),
              HookMatcher(hooks=[input_validator]),
              HookMatcher(hooks=[audit_logger]),
          ]
      }
  )
  ```

  ```typescript TypeScript theme={null}
  const options = {
    hooks: {
      PreToolUse: [
        { hooks: [authorizationCheck] },
        { hooks: [inputValidator] },
        { hooks: [auditLogger] }
      ]
    }
  };
  ```
</CodeGroup>

### Filtrar con matchers regex

Use patrones regex para coincidir con múltiples herramientas. Este ejemplo registra tres matchers con diferentes alcances: el primero dispara `file_security_hook` solo para herramientas de modificación de archivos, el segundo dispara `mcp_audit_hook` para cualquier herramienta MCP (herramientas cuyos nombres comienzan con `mcp__`), y el tercero dispara `global_logger` para cada llamada de herramienta independientemente del nombre:

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      hooks={
          "PreToolUse": [
              # Match file modification tools
              HookMatcher(matcher="Write|Edit|Delete", hooks=[file_security_hook]),
              # Match all MCP tools
              HookMatcher(matcher="^mcp__", hooks=[mcp_audit_hook]),
              # Match everything (no matcher)
              HookMatcher(hooks=[global_logger]),
          ]
      }
  )
  ```

  ```typescript TypeScript theme={null}
  const options = {
    hooks: {
      PreToolUse: [
        // Match file modification tools
        { matcher: "Write|Edit|Delete", hooks: [fileSecurityHook] },

        // Match all MCP tools
        { matcher: "^mcp__", hooks: [mcpAuditHook] },

        // Match everything (no matcher)
        { hooks: [globalLogger] }
      ]
    }
  };
  ```
</CodeGroup>

### Rastrear actividad de subagente

Use hooks `SubagentStop` para monitorear cuándo los subagentes terminan su trabajo. Vea el tipo de entrada completo en las referencias del SDK de [TypeScript](/es/agent-sdk/typescript#hookinput) y [Python](/es/agent-sdk/python#hookinput). Este ejemplo registra un resumen cada vez que un subagente se completa:

<CodeGroup>
  ```python Python theme={null}
  async def subagent_tracker(input_data, tool_use_id, context):
      # Log subagent details when it finishes
      print(f"[SUBAGENT] Completed: {input_data['agent_id']}")
      print(f"  Transcript: {input_data['agent_transcript_path']}")
      print(f"  Tool use ID: {tool_use_id}")
      print(f"  Stop hook active: {input_data.get('stop_hook_active')}")
      return {}


  options = ClaudeAgentOptions(
      hooks={"SubagentStop": [HookMatcher(hooks=[subagent_tracker])]}
  )
  ```

  ```typescript TypeScript theme={null}
  import { HookCallback, SubagentStopHookInput } from "@anthropic-ai/claude-agent-sdk";

  const subagentTracker: HookCallback = async (input, toolUseID, { signal }) => {
    // Cast to SubagentStopHookInput to access subagent-specific fields
    const subInput = input as SubagentStopHookInput;

    // Log subagent details when it finishes
    console.log(`[SUBAGENT] Completed: ${subInput.agent_id}`);
    console.log(`  Transcript: ${subInput.agent_transcript_path}`);
    console.log(`  Tool use ID: ${toolUseID}`);
    console.log(`  Stop hook active: ${subInput.stop_hook_active}`);
    return {};
  };

  const options = {
    hooks: {
      SubagentStop: [{ hooks: [subagentTracker] }]
    }
  };
  ```
</CodeGroup>

### Realizar solicitudes HTTP desde hooks

Los hooks pueden realizar operaciones asincrónicas como solicitudes HTTP. Capture errores dentro de su hook en lugar de dejarlos propagarse, ya que una excepción no manejada puede interrumpir el agente.

Este ejemplo envía un webhook después de que cada herramienta se completa, registrando qué herramienta se ejecutó y cuándo. El hook captura errores para que un webhook fallido no interrumpa el agente:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import json
  import urllib.request
  from datetime import datetime


  def _send_webhook(tool_name):
      """Synchronous helper that POSTs tool usage data to an external webhook."""
      data = json.dumps(
          {
              "tool": tool_name,
              "timestamp": datetime.now().isoformat(),
          }
      ).encode()
      req = urllib.request.Request(
          "https://api.example.com/webhook",
          data=data,
          headers={"Content-Type": "application/json"},
          method="POST",
      )
      urllib.request.urlopen(req)


  async def webhook_notifier(input_data, tool_use_id, context):
      # Only fire after a tool completes (PostToolUse), not before
      if input_data["hook_event_name"] != "PostToolUse":
          return {}

      try:
          # Run the blocking HTTP call in a thread to avoid blocking the event loop
          await asyncio.to_thread(_send_webhook, input_data["tool_name"])
      except Exception as e:
          # Log the error but don't raise. A failed webhook shouldn't stop the agent
          print(f"Webhook request failed: {e}")

      return {}
  ```

  ```typescript TypeScript theme={null}
  import { query, HookCallback, PostToolUseHookInput } from "@anthropic-ai/claude-agent-sdk";

  const webhookNotifier: HookCallback = async (input, toolUseID, { signal }) => {
    // Only fire after a tool completes (PostToolUse), not before
    if (input.hook_event_name !== "PostToolUse") return {};

    try {
      await fetch("https://api.example.com/webhook", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          tool: (input as PostToolUseHookInput).tool_name,
          timestamp: new Date().toISOString()
        }),
        // Pass signal so the request cancels if the hook times out
        signal
      });
    } catch (error) {
      // Handle cancellation separately from other errors
      if (error instanceof Error && error.name === "AbortError") {
        console.log("Webhook request cancelled");
      }
      // Don't re-throw. A failed webhook shouldn't stop the agent
    }

    return {};
  };

  // Register as a PostToolUse hook
  for await (const message of query({
    prompt: "Refactor the auth module",
    options: {
      hooks: {
        PostToolUse: [{ hooks: [webhookNotifier] }]
      }
    }
  })) {
    console.log(message);
  }
  ```
</CodeGroup>

### Reenviar notificaciones a Slack

Use hooks `Notification` para recibir notificaciones del sistema del agente y reenviarlas a servicios externos. Las notificaciones se disparan para tipos de evento específicos: `permission_prompt` (Claude necesita permiso), `idle_prompt` (Claude está esperando entrada), `auth_success` (autenticación completada), `elicitation_dialog` (Claude está solicitando al usuario), `elicitation_response` (el usuario respondió a una elicitación), y `elicitation_complete` (una elicitación se cerró). Cada notificación incluye un campo `message` con una descripción legible por humanos y opcionalmente un `title`.

Este ejemplo reenvía cada notificación a un canal de Slack. Requiere una [URL de webhook entrante de Slack](https://api.slack.com/messaging/webhooks), que crea agregando una aplicación a su espacio de trabajo de Slack y habilitando webhooks entrantes:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import json
  import urllib.request

  from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, HookMatcher


  def _send_slack_notification(message):
      """Synchronous helper that sends a message to Slack via incoming webhook."""
      data = json.dumps({"text": f"Agent status: {message}"}).encode()
      req = urllib.request.Request(
          "https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
          data=data,
          headers={"Content-Type": "application/json"},
          method="POST",
      )
      urllib.request.urlopen(req)


  async def notification_handler(input_data, tool_use_id, context):
      try:
          # Run the blocking HTTP call in a thread to avoid blocking the event loop
          await asyncio.to_thread(_send_slack_notification, input_data.get("message", ""))
      except Exception as e:
          print(f"Failed to send notification: {e}")

      # Return empty object. Notification hooks don't modify agent behavior
      return {}


  async def main():
      options = ClaudeAgentOptions(
          hooks={
              # Register the hook for Notification events (no matcher needed)
              "Notification": [HookMatcher(hooks=[notification_handler])],
          },
      )

      async with ClaudeSDKClient(options=options) as client:
          await client.query("Analyze this codebase")
          async for message in client.receive_response():
              print(message)


  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import { query, HookCallback, NotificationHookInput } from "@anthropic-ai/claude-agent-sdk";

  // Define a hook callback that sends notifications to Slack
  const notificationHandler: HookCallback = async (input, toolUseID, { signal }) => {
    // Cast to NotificationHookInput to access the message field
    const notification = input as NotificationHookInput;

    try {
      // POST the notification message to a Slack incoming webhook
      await fetch("https://hooks.slack.com/services/YOUR/WEBHOOK/URL", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: `Agent status: ${notification.message}`
        }),
        // Pass signal so the request cancels if the hook times out
        signal
      });
    } catch (error) {
      if (error instanceof Error && error.name === "AbortError") {
        console.log("Notification cancelled");
      } else {
        console.error("Failed to send notification:", error);
      }
    }

    // Return empty object. Notification hooks don't modify agent behavior
    return {};
  };

  // Register the hook for Notification events (no matcher needed)
  for await (const message of query({
    prompt: "Analyze this codebase",
    options: {
      hooks: {
        Notification: [{ hooks: [notificationHandler] }]
      }
    }
  })) {
    console.log(message);
  }
  ```
</CodeGroup>

## Solucionar problemas comunes

### Hook no se dispara

* Verifique que el nombre del evento de hook sea correcto y sensible a mayúsculas (`PreToolUse`, no `preToolUse`)
* Verifique que su patrón de matcher coincida exactamente con el nombre de la herramienta
* Asegúrese de que el hook esté bajo el tipo de evento correcto en `options.hooks`
* Para hooks que no son de herramientas como `Stop` y `SubagentStop`, los matchers coinciden contra campos diferentes (vea [patrones de matcher](/es/hooks#matcher-patterns))
* Los hooks pueden no dispararse cuando el agente alcanza el límite [`max_turns`](/es/agent-sdk/python#claudeagentoptions) porque la sesión termina antes de que los hooks puedan ejecutarse

### Matcher no filtra como se esperaba

Los matchers solo coinciden con **nombres de herramientas**, no con rutas de archivo u otros argumentos. Para filtrar por ruta de archivo, verifique `tool_input.file_path` dentro de su hook:

```typescript theme={null}
const myHook: HookCallback = async (input, toolUseID, { signal }) => {
  const preInput = input as PreToolUseHookInput;
  const toolInput = preInput.tool_input as Record<string, unknown>;
  const filePath = toolInput?.file_path as string;
  if (!filePath?.endsWith(".md")) return {}; // Skip non-markdown files
  // Process markdown files...
  return {};
};
```

### Tiempo de espera del hook

* Aumente el valor `timeout` en la configuración `HookMatcher`
* Use el `AbortSignal` del tercer argumento de devolución de llamada para manejar la cancelación correctamente en TypeScript

### Herramienta bloqueada inesperadamente

* Verifique todos los hooks `PreToolUse` para devoluciones de `permissionDecision: 'deny'`
* Agregue registro a sus hooks para ver qué `permissionDecisionReason` están devolviendo
* Verifique que los patrones de matcher no sean demasiado amplios (un matcher vacío coincide con todas las herramientas)

### Entrada modificada no aplicada

* Asegúrese de que `updatedInput` esté dentro de `hookSpecificOutput`, no en el nivel superior:

  ```typescript theme={null}
  return {
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "allow",
      updatedInput: { command: "new command" }
    }
  };
  ```

* También debe devolver `permissionDecision: 'allow'` u `'ask'` para que la modificación de entrada surta efecto

* Incluya `hookEventName` en `hookSpecificOutput` para identificar para qué tipo de hook es la salida

### Hooks de sesión no disponibles en Python

`SessionStart` y `SessionEnd` pueden registrarse como hooks de devolución de llamada del SDK en TypeScript, pero no están disponibles en el SDK de Python (`HookEvent` los omite). En Python, solo están disponibles como [hooks de comandos de shell](/es/hooks#hook-events) definidos en archivos de configuración (por ejemplo, `.claude/settings.json`). Para cargar hooks de comandos de shell desde su aplicación SDK, incluya la fuente de configuración apropiada con [`setting_sources`](/es/agent-sdk/python#settingsource) o [`settingSources`](/es/agent-sdk/typescript#settingsource):

<CodeGroup>
  ```python Python theme={null}
  options = ClaudeAgentOptions(
      setting_sources=["project"],  # Loads .claude/settings.json including hooks
  )
  ```

  ```typescript TypeScript theme={null}
  const options = {
    settingSources: ["project"] // Loads .claude/settings.json including hooks
  };
  ```
</CodeGroup>

Para ejecutar lógica de inicialización como una devolución de llamada del SDK de Python en su lugar, use el primer mensaje de `client.receive_response()` como su disparador.

### Solicitudes de permiso de subagente multiplicándose

Al generar múltiples subagentes, cada uno puede solicitar permisos por separado. Los subagentes no heredan automáticamente los permisos del agente padre. Para evitar solicitudes repetidas, use hooks `PreToolUse` para aprobar automáticamente herramientas específicas, o configure reglas de permiso que se apliquen a sesiones de subagente.

### Bucles recursivos de hook con subagentes

Un hook `UserPromptSubmit` que genera subagentes puede crear bucles infinitos si esos subagentes disparan el mismo hook. Para prevenir esto:

* Verifique un indicador de subagente en la entrada del hook antes de generar
* Use una variable compartida o estado de sesión para rastrear si ya está dentro de un subagente
* Alcance los hooks para ejecutarse solo para la sesión del agente de nivel superior

### systemMessage no aparece en la salida

El campo `systemMessage` muestra un mensaje al usuario, no al modelo. Por defecto, el SDK no expone la salida de hooks en el flujo de mensajes, por lo que el mensaje puede no aparecer a menos que establezca `includeHookEvents` (`include_hook_events` en Python). Para pasar contexto al modelo en su lugar, devuelva [`additionalContext`](/es/hooks#add-context-for-claude).

Si necesita exponer decisiones de hook a su aplicación de manera confiable, regístrelas por separado o use un canal de salida dedicado.

## Recursos relacionados

* [Referencia de hooks de Claude Code](/es/hooks): esquemas completos de entrada/salida JSON, documentación de eventos y patrones de matcher
* [Guía de hooks de Claude Code](/es/hooks-guide): ejemplos de hooks de comandos de shell y tutoriales
* [Referencia del SDK de TypeScript](/es/agent-sdk/typescript): tipos de hook, definiciones de entrada/salida y opciones de configuración
* [Referencia del SDK de Python](/es/agent-sdk/python): tipos de hook, definiciones de entrada/salida y opciones de configuración
* [Permisos](/es/agent-sdk/permissions): controlar qué puede hacer su agente
* [Herramientas personalizadas](/es/agent-sdk/custom-tools): crear herramientas para extender las capacidades del agente
