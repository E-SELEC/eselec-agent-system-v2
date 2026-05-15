---
source_url: https://code.claude.com/docs/es/agent-sdk/permissions
fetched_url: https://code.claude.com/docs/es/agent-sdk/permissions.md
category: SDK de Agente
status: 200
scraped_at: 2026-05-15T14:28:33+00:00
sha256_16: 47e9e5379fc908cd
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configurar permisos

> Controle cómo su agente utiliza herramientas con modos de permiso, hooks y reglas declarativas de permitir/denegar.

El SDK del Agente Claude proporciona controles de permisos para gestionar cómo Claude utiliza las herramientas. Utilice modos de permiso y reglas para definir qué está permitido automáticamente, y la devolución de llamada [`canUseTool`](/es/agent-sdk/user-input) para manejar todo lo demás en tiempo de ejecución.

<Note>
  Esta página cubre modos de permiso y reglas. Para crear flujos de aprobación interactivos donde los usuarios aprueban o deniegan solicitudes de herramientas en tiempo de ejecución, consulte [Manejar aprobaciones e entrada del usuario](/es/agent-sdk/user-input).
</Note>

## Cómo se evalúan los permisos

Cuando Claude solicita una herramienta, el SDK verifica los permisos en este orden:

<Steps>
  <Step title="Hooks">
    Ejecute [hooks](/es/agent-sdk/hooks) primero. Un hook puede denegar la llamada directamente o pasarla. Un hook que devuelve `allow` no omite las reglas de denegar y preguntar a continuación; esas se evalúan independientemente del resultado del hook.
  </Step>

  <Step title="Reglas de denegar">
    Verifique las reglas `deny` (de `disallowed_tools` y [settings.json](/es/settings#permission-settings)). Si una regla de denegar coincide, la herramienta se bloquea, incluso en modo `bypassPermissions`.
  </Step>

  <Step title="Modo de permiso">
    Aplique el [modo de permiso](#permission-modes) activo. `bypassPermissions` aprueba todo lo que llega a este paso. `acceptEdits` aprueba operaciones de archivo. Otros modos se descartan.
  </Step>

  <Step title="Reglas de permitir">
    Verifique las reglas `allow` (de `allowed_tools` y settings.json). Si una regla coincide, la herramienta se aprueba.
  </Step>

  <Step title="Devolución de llamada canUseTool">
    Si no se resuelve por ninguno de los anteriores, llame a su devolución de llamada [`canUseTool`](/es/agent-sdk/user-input) para una decisión. En modo `dontAsk`, este paso se omite y la herramienta se deniega.
  </Step>
</Steps>

<img src="https://mintcdn.com/claude-code/FEspvVUyRuaWjm0s/images/agent-sdk/permissions-flow.svg?fit=max&auto=format&n=FEspvVUyRuaWjm0s&q=85&s=a1759b0cf4541281a9fdd8f5348228e8" alt="Diagrama de flujo de evaluación de permisos" width="920" height="260" data-path="images/agent-sdk/permissions-flow.svg" />

Esta página se enfoca en **reglas de permitir y denegar** y **modos de permiso**. Para los otros pasos:

* **Hooks:** ejecute código personalizado para permitir, denegar o modificar solicitudes de herramientas. Consulte [Controlar la ejecución con hooks](/es/agent-sdk/hooks).
* **Devolución de llamada canUseTool:** solicite aprobación a los usuarios en tiempo de ejecución. Consulte [Manejar aprobaciones e entrada del usuario](/es/agent-sdk/user-input).

## Reglas de permitir y denegar

`allowed_tools` y `disallowed_tools` (TypeScript: `allowedTools` / `disallowedTools`) agregan entradas a las listas de reglas de permitir y denegar en el flujo de evaluación anterior. Controlan si una llamada de herramienta se aprueba, no si la herramienta está disponible para Claude.

| Opción                           | Efecto                                                                                                                                       |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| `allowed_tools=["Read", "Grep"]` | `Read` y `Grep` se aprueban automáticamente. Las herramientas no listadas aquí aún existen y se descartan al modo de permiso y `canUseTool`. |
| `disallowed_tools=["Bash"]`      | `Bash` siempre se deniega. Las reglas de denegar se verifican primero y se mantienen en cada modo de permiso, incluido `bypassPermissions`.  |

Para un agente bloqueado, empareje `allowedTools` con `permissionMode: "dontAsk"`. Las herramientas listadas se aprueban; cualquier otra cosa se deniega directamente en lugar de solicitar:

```typescript theme={null}
const options = {
  allowedTools: ["Read", "Glob", "Grep"],
  permissionMode: "dontAsk"
};
```

<Warning>
  **`allowed_tools` no restringe `bypassPermissions`.** `allowed_tools` solo pre-aprueba las herramientas que lista. Las herramientas no listadas no coinciden con ninguna regla de permitir y se descartan al modo de permiso, donde `bypassPermissions` las aprueba. Establecer `allowed_tools=["Read"]` junto con `permission_mode="bypassPermissions"` aún aprueba cada herramienta, incluidas `Bash`, `Write` y `Edit`. Si necesita `bypassPermissions` pero desea que herramientas específicas se bloqueen, use `disallowed_tools`.
</Warning>

También puede configurar reglas de permitir, denegar y preguntar de forma declarativa en `.claude/settings.json`. Estas reglas se leen cuando la fuente de configuración `project` está habilitada, que lo está para las opciones predeterminadas de `query()`. Si establece `setting_sources` (TypeScript: `settingSources`) explícitamente, incluya `"project"` para que se apliquen. Consulte [Configuración de permisos](/es/settings#permission-settings) para la sintaxis de reglas.

## Modos de permiso

Los modos de permiso proporcionan control global sobre cómo Claude utiliza las herramientas. Puede establecer el modo de permiso al llamar a `query()` o cambiarlo dinámicamente durante sesiones de transmisión.

### Modos disponibles

El SDK admite estos modos de permiso:

| Modo                     | Descripción                                | Comportamiento de herramientas                                                                                                                                           |
| :----------------------- | :----------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default`                | Comportamiento de permiso estándar         | Sin aprobaciones automáticas; las herramientas no coincidentes activan su devolución de llamada `canUseTool`                                                             |
| `dontAsk`                | Denegar en lugar de solicitar              | Cualquier cosa no pre-aprobada por `allowed_tools` o reglas se deniega; `canUseTool` nunca se llama                                                                      |
| `acceptEdits`            | Auto-aceptar ediciones de archivo          | Las ediciones de archivo y [operaciones del sistema de archivos](#accept-edits-mode-acceptedits) (`mkdir`, `rm`, `mv`, etc.) se aprueban automáticamente                 |
| `bypassPermissions`      | Omitir todas las verificaciones de permiso | Todas las herramientas se ejecutan sin solicitudes de permiso (usar con cuidado)                                                                                         |
| `plan`                   | Modo de planificación                      | Las herramientas de solo lectura se ejecutan; Claude analiza y planifica sin editar sus archivos fuente                                                                  |
| `auto` (solo TypeScript) | Aprobaciones clasificadas por modelo       | Un clasificador de modelo aprueba o deniega cada llamada de herramienta. Consulte [Modo Auto](/es/permission-modes#eliminate-prompts-with-auto-mode) para disponibilidad |

<Warning>
  **Herencia de subagentos:** Cuando el padre usa `bypassPermissions`, `acceptEdits` o `auto`, todos los subagentos heredan ese modo y no se puede anular por subagentos. Los subagentos pueden tener diferentes indicaciones del sistema y comportamiento menos restringido que su agente principal, por lo que heredar `bypassPermissions` les otorga acceso completo y autónomo al sistema sin solicitudes de aprobación.
</Warning>

### Establecer modo de permiso

Puede establecer el modo de permiso una vez al iniciar una consulta, o cambiarlo dinámicamente mientras la sesión está activa.

<Tabs>
  <Tab title="En tiempo de consulta">
    Pase `permission_mode` (Python) o `permissionMode` (TypeScript) al crear una consulta. Este modo se aplica para toda la sesión a menos que se cambie dinámicamente.

    <CodeGroup>
      ```python Python theme={null}
      import asyncio
      from claude_agent_sdk import query, ClaudeAgentOptions


      async def main():
          async for message in query(
              prompt="Help me refactor this code",
              options=ClaudeAgentOptions(
                  permission_mode="default",  # Set the mode here
              ),
          ):
              if hasattr(message, "result"):
                  print(message.result)


      asyncio.run(main())
      ```

      ```typescript TypeScript theme={null}
      import { query } from "@anthropic-ai/claude-agent-sdk";

      async function main() {
        for await (const message of query({
          prompt: "Help me refactor this code",
          options: {
            permissionMode: "default" // Set the mode here
          }
        })) {
          if ("result" in message) {
            console.log(message.result);
          }
        }
      }

      main();
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Durante la transmisión">
    Llame a `set_permission_mode()` (Python) o `setPermissionMode()` (TypeScript) para cambiar el modo a mitad de sesión. El nuevo modo entra en vigor inmediatamente para todas las solicitudes de herramientas posteriores. Esto le permite comenzar restrictivo y flexibilizar los permisos a medida que aumenta la confianza, por ejemplo, cambiar a `acceptEdits` después de revisar el enfoque inicial de Claude.

    <CodeGroup>
      ```python Python theme={null}
      import asyncio
      from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions


      async def main():
          async with ClaudeSDKClient(
              options=ClaudeAgentOptions(
                  permission_mode="default",  # Start in default mode
              )
          ) as client:
              await client.query("Help me refactor this code")

              # Change mode dynamically mid-session
              await client.set_permission_mode("acceptEdits")

              # Process messages with the new permission mode
              async for message in client.receive_response():
                  if hasattr(message, "result"):
                      print(message.result)


      asyncio.run(main())
      ```

      ```typescript TypeScript theme={null}
      import { query } from "@anthropic-ai/claude-agent-sdk";

      async function main() {
        const q = query({
          prompt: "Help me refactor this code",
          options: {
            permissionMode: "default" // Start in default mode
          }
        });

        // Change mode dynamically mid-session
        await q.setPermissionMode("acceptEdits");

        // Process messages with the new permission mode
        for await (const message of q) {
          if ("result" in message) {
            console.log(message.result);
          }
        }
      }

      main();
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Detalles del modo

#### Modo de aceptar ediciones (`acceptEdits`)

Auto-aprueba operaciones de archivo para que Claude pueda editar código sin solicitar. Otras herramientas (como comandos Bash que no son operaciones del sistema de archivos) aún requieren permisos normales.

**Operaciones auto-aprobadas:**

* Ediciones de archivo (herramientas Edit, Write)
* Comandos del sistema de archivos: `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed`

Ambos se aplican solo a rutas dentro del directorio de trabajo o `additionalDirectories`. Las rutas fuera de ese alcance y las escrituras en rutas protegidas aún solicitan.

**Usar cuando:** confía en las ediciones de Claude y desea una iteración más rápida, como durante la creación de prototipos o cuando trabaja en un directorio aislado.

#### Modo no preguntar (`dontAsk`)

Convierte cualquier solicitud de permiso en una denegación. Las herramientas pre-aprobadas por `allowed_tools`, reglas de permitir de `settings.json` o un hook se ejecutan normalmente. Todo lo demás se deniega sin llamar a `canUseTool`.

**Usar cuando:** desea una superficie de herramienta fija y explícita para un agente sin interfaz y prefiere una denegación dura sobre la dependencia silenciosa de que `canUseTool` esté ausente.

#### Modo de omitir permisos (`bypassPermissions`)

Auto-aprueba todos los usos de herramientas sin solicitudes. Los hooks aún se ejecutan y pueden bloquear operaciones si es necesario.

<Warning>
  Usar con extrema precaución. Claude tiene acceso completo al sistema en este modo. Solo use en entornos controlados donde confía en todas las operaciones posibles.

  `allowed_tools` no restringe este modo. Cada herramienta se aprueba, no solo las que listó. Las reglas de denegar (`disallowed_tools`), reglas explícitas de `ask` y hooks se evalúan antes de la verificación del modo y aún pueden bloquear una herramienta.
</Warning>

#### Modo de planificación (`plan`)

Restringe Claude a herramientas de solo lectura. Claude puede leer archivos y ejecutar comandos de shell de solo lectura para explorar la base de código pero no edita sus archivos fuente. Claude puede usar `AskUserQuestion` para aclarar requisitos antes de finalizar el plan. Consulte [Manejar aprobaciones e entrada del usuario](/es/agent-sdk/user-input#handle-clarifying-questions) para manejar estas solicitudes.

**Usar cuando:** desea que Claude proponga cambios sin ejecutarlos, como durante la revisión de código o cuando necesita aprobar cambios antes de que se realicen.

## Recursos relacionados

Para los otros pasos en el flujo de evaluación de permisos:

* [Manejar aprobaciones e entrada del usuario](/es/agent-sdk/user-input): solicitudes de aprobación interactivas y preguntas aclaratorias
* [Guía de hooks](/es/agent-sdk/hooks): ejecute código personalizado en puntos clave del ciclo de vida del agente
* [Reglas de permisos](/es/settings#permission-settings): reglas declarativas de permitir/denegar en `settings.json`
