---
source_url: https://code.claude.com/docs/es/debug-your-config
fetched_url: https://code.claude.com/docs/es/debug-your-config.md
category: Crear con Claude Code, agentes y automatizacion
status: 200
scraped_at: 2026-05-15T14:27:50+00:00
sha256_16: 31fabb2b1e221d82
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Depura tu configuración

> Diagnostica por qué CLAUDE.md, configuración, hooks, servidores MCP o skills no están surtiendo efecto. Usa /context, /doctor, /hooks y /mcp para ver qué se cargó realmente.

Cuando Claude ignora una instrucción o una característica que configuró no aparece, la causa suele ser que el archivo no se cargó, se cargó desde una ubicación diferente a la que esperaba, u otro archivo la anuló. Esta guía muestra cómo inspeccionar qué cargó realmente Claude Code para que pueda reducir cuál se aplica.

Para problemas de instalación, autenticación y conectividad, consulte [Troubleshooting installation and login](/es/troubleshoot-install) en su lugar.

## Ver qué se cargó en el contexto

El comando `/context` muestra todo lo que ocupa la ventana de contexto para la sesión actual, desglosado por categoría: indicación del sistema, archivos de memoria, skills, herramientas MCP y mensajes de conversación. Ejecútelo primero para confirmar si su `CLAUDE.md`, reglas o descripciones de skills están presentes en absoluto.

Para obtener detalles sobre una categoría específica, continúe con el comando dedicado:

| Comando          | Muestra                                                                                                                                         |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| `/memory`        | Qué archivos `CLAUDE.md` y rules se cargaron, más entradas de memoria automática                                                                |
| `/skills`        | Skills disponibles de fuentes de proyecto, usuario y plugin                                                                                     |
| `/agents`        | Subagentes configurados y sus configuraciones                                                                                                   |
| `/hooks`         | Configuraciones de hook activas                                                                                                                 |
| `/mcp`           | Servidores MCP conectados y su estado                                                                                                           |
| `/permissions`   | Reglas de permitir y denegar resueltas actualmente en vigor                                                                                     |
| `/doctor`        | Diagnósticos de configuración: claves inválidas, errores de esquema, salud de instalación                                                       |
| `/debug [issue]` | Habilita el registro de depuración para la sesión e indica a Claude que diagnostique usando la salida del registro y las rutas de configuración |
| `/status`        | Fuentes de configuración activas, incluido si la configuración administrada está en vigor                                                       |

Si falta un archivo de memoria en `/memory`, verifique su ubicación contra [cómo se cargan los archivos CLAUDE.md](/es/memory#how-claude-md-files-load). Los archivos `CLAUDE.md` del subdirectorio se cargan bajo demanda cuando Claude lee un archivo en ese directorio con la herramienta Read, no al inicio de la sesión.

Si `/memory` confirma que el archivo se cargó pero Claude aún no sigue una instrucción particular, el problema probablemente sea cómo se escribe la instrucción en lugar de si se cargó. CLAUDE.md funciona bien para el tipo de orientación que daría a un nuevo compañero de equipo, como convenciones de proyecto, comandos de compilación y dónde pertenecen los archivos.

La adherencia disminuye cuando una instrucción es lo suficientemente vaga como para interpretarse de múltiples formas, cuando dos archivos dan direcciones conflictivas, o cuando el archivo ha crecido lo suficiente como para que las reglas individuales reciban menos atención. [Escribir instrucciones efectivas](/es/memory#write-effective-instructions) cubre los patrones de especificidad, tamaño y estructura que mantienen la adherencia alta.

<Note>
  CLAUDE.md y los permisos resuelven problemas diferentes. CLAUDE.md le dice a Claude cómo funciona su proyecto para que tome buenas decisiones. [Permisos](/es/permissions) y [hooks](/es/hooks) aplican límites independientemente de lo que Claude decida. Use CLAUDE.md para "lo hacemos de esta manera aquí". Use permisos o hooks para límites de seguridad y cualquier cosa que nunca deba suceder, donde necesita una garantía en lugar de orientación.
</Note>

## Verificar configuración resuelta

La configuración se fusiona en ámbitos administrados, de usuario, de proyecto y locales. La configuración administrada siempre gana cuando está presente. Entre el resto, el ámbito más cercano anula el más amplio en el orden local, luego proyecto, luego usuario. Algunos ajustes también se pueden establecer mediante banderas de línea de comandos o [variables de entorno](/es/env-vars), que actúan como otra capa de anulación. Cuando una configuración no parece aplicarse, el valor que estableció generalmente se anula por otro ámbito o una variable de entorno.

Ejecute `/doctor` para validar sus archivos de configuración y mostrar claves inválidas o errores de esquema. Cuando `/doctor` informa de problemas, presione `f` para enviar el informe de diagnóstico a Claude y dejar que lo guíe a través de las correcciones.

Ejecute `/status` para ver qué fuentes de configuración están activas, incluido si la configuración administrada está en vigor. Para entender qué ámbito gana para una clave determinada, consulte [Cómo interactúan los ámbitos](/es/settings#how-scopes-interact).

## Verificar servidores MCP

Ejecute `/mcp` para ver cada servidor configurado, su estado de conexión y si lo ha aprobado para el proyecto actual. Un servidor puede estar definido correctamente pero aún no proporcionar herramientas por algunas razones comunes:

* Los servidores con ámbito de proyecto en `.mcp.json` requieren una aprobación única. Si se descartó el mensaje, el servidor permanece deshabilitado hasta que lo apruebe desde `/mcp`.
* Un servidor que no se inicia se muestra como fallido en `/mcp`. Las rutas de archivo relativas en `command` o `args` son una causa frecuente, ya que se resuelven contra el directorio desde el que lanzó Claude Code en lugar de la ubicación de `.mcp.json`.
* Un servidor que se muestra como conectado pero enumera cero herramientas se ha iniciado correctamente pero no devuelve una lista de herramientas. Seleccione **Reconnect** desde `/mcp`. Si el recuento permanece en cero, ejecute `claude --debug mcp` para ver la salida stderr del servidor.

Para ubicaciones de configuración y reglas de ámbito, consulte [MCP](/es/mcp).

## Verificar hooks

Ejecute `/hooks` para enumerar cada hook registrado para la sesión actual, agrupado por evento. Si un hook que definió no aparece, no se está leyendo: los hooks van bajo la clave `"hooks"` en un archivo de configuración, no en un archivo independiente.

Si el hook aparece pero no se dispara, el matcher es la causa habitual. El campo `matcher` es una cadena única que usa `|` para coincidir con múltiples nombres de herramientas, por ejemplo `"Edit|Write"`. Un nombre de herramienta mal escrito falla silenciosamente porque el matcher nunca coincide. Un valor de matriz es un error de esquema: Claude Code muestra un aviso de error de configuración, `/doctor` informa del error de validación y la entrada del hook se descarta para que no aparezca en `/hooks`.

Las ediciones en `settings.json` surten efecto en la sesión en ejecución después de un breve retraso de estabilidad de archivo. No necesita reiniciar. Si `/hooks` aún muestra la definición anterior unos segundos después de guardar, ejecute `/hooks` nuevamente para actualizar la vista.

Si `/hooks` muestra el hook pero aún no se dispara, el siguiente paso es ver la evaluación del hook en vivo. Inicie una sesión con `claude --debug hooks` y active la llamada de herramienta. El registro de depuración registra cada evento, qué matchers se verificaron y el código de salida y la salida del hook. Consulte [Depurar hooks](/es/hooks#debug-hooks) para el formato del registro y [solución de problemas de hooks](/es/hooks-guide#limitations-and-troubleshooting) para patrones de fallo comunes.

## Probar contra una configuración limpia

Si las comprobaciones dirigidas no aíslan la causa, o su configuración está en un estado desconocido, compare contra una sesión que no carga nada de su configuración habitual. Apunte [`CLAUDE_CONFIG_DIR`](/es/env-vars) a un directorio vacío para omitir todo bajo `~/.claude`, e inicie desde un directorio que no tenga carpeta `.claude`, `.mcp.json` o `CLAUDE.md` para que la configuración del proyecto también se omita.

```bash theme={null}
cd /tmp && CLAUDE_CONFIG_DIR=/tmp/claude-clean claude
```

La sesión limpia no tiene configuración de usuario o proyecto, hooks, servidores MCP, plugins o memoria.

* La configuración administrada aún se aplica si su organización la implementa, ya que vive en una ruta del sistema fuera de `~/.claude`
* En Linux y Windows, se le pedirá que inicie sesión nuevamente porque las credenciales se almacenan en el directorio de configuración
* En macOS, las credenciales están en el Keychain y se transfieren a la sesión limpia

Si el problema desaparece aquí, la causa está en algún lugar de sus archivos reales `~/.claude` o `.claude` del proyecto. Reintrodúzcalos uno a la vez, copiando archivos en el directorio temporal o iniciando desde su proyecto, para encontrar cuál es. Si persiste en la sesión limpia, la causa está fuera de su configuración de usuario y proyecto. Ejecute `/status` para verificar si la configuración administrada está en vigor, busque [variables de entorno](/es/env-vars) que afecten a Claude Code, luego consulte [Solución de problemas](/es/troubleshooting).

## Verificar causas comunes

La mayoría de las sorpresas de configuración se remontan a un pequeño conjunto de reglas de ubicación y sintaxis. Verifique estos antes de asumir un error:

| Síntoma                                                                          | Causa                                                                                                                      | Solución                                                                                                                                                                                                                      |
| :------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hook nunca se dispara                                                            | `matcher` es una matriz JSON en lugar de una cadena                                                                        | Use una cadena única con `\|` para coincidir con múltiples herramientas, por ejemplo `"Edit\|Write"`. Consulte [patrones de matcher](/es/hooks#matcher-patterns).                                                             |
| Hook nunca se dispara                                                            | El valor `matcher` está en minúsculas, por ejemplo `"bash"`                                                                | La coincidencia distingue mayúsculas de minúsculas. Los nombres de herramientas están capitalizados: `Bash`, `Edit`, `Write`, `Read`.                                                                                         |
| Hook nunca se dispara                                                            | Los hooks están en un archivo `.claude/hooks.json` independiente                                                           | No hay archivo de hooks independiente. Defina hooks bajo la clave `"hooks"` en `settings.json`. Consulte [configuración de hook](/es/hooks).                                                                                  |
| Los permisos, hooks o env establecidos globalmente se ignoran                    | La configuración se agregó a `~/.claude.json`                                                                              | `~/.claude.json` contiene el estado de la aplicación y los cambios de interfaz de usuario. `permissions`, `hooks` y `env` pertenecen a `~/.claude/settings.json`. Estos son dos archivos diferentes.                          |
| Un valor `settings.json` parece ignorado                                         | La misma clave se establece en `settings.local.json`                                                                       | `settings.local.json` anula `settings.json`, y ambos anulan `~/.claude/settings.json`. Consulte [precedencia de configuración](/es/settings#how-scopes-interact).                                                             |
| Skill no aparece en `/skills`                                                    | El archivo de skill está en `.claude/skills/name.md` en lugar de en una carpeta                                            | Use una carpeta con `SKILL.md` dentro: `.claude/skills/name/SKILL.md`.                                                                                                                                                        |
| Skill aparece en `/skills` pero Claude nunca lo invoca                           | Skill tiene `disable-model-invocation: true` en su frontmatter, o su descripción no coincide con cómo formula la solicitud | Verifique la insignia en `/skills`: una etiqueta "user-only" significa que Claude no lo activará por su cuenta. Consulte [invocación de skill](/es/skills).                                                                   |
| Las instrucciones de `CLAUDE.md` del subdirectorio parecen ignoradas             | Los archivos del subdirectorio se cargan bajo demanda, no al inicio de la sesión                                           | Se cargan cuando Claude lee un archivo en ese directorio con la herramienta Read, no al lanzar y no al escribir o crear archivos allí. Consulte [cómo se cargan los archivos CLAUDE.md](/es/memory#how-claude-md-files-load). |
| El subagente ignora las instrucciones de `CLAUDE.md`                             | Los subagentes no siempre heredan la memoria del proyecto                                                                  | Coloque las reglas críticas en el cuerpo del archivo del agente, que se convierte en el indicador del sistema del subagente. Consulte [configuración de subagente](/es/sub-agents).                                           |
| La lógica de limpieza nunca se ejecuta al final de la sesión                     | No hay hook `SessionEnd` configurado                                                                                       | Agregue un hook `SessionEnd` en `settings.json`. Consulte la [lista de eventos de hook](/es/hooks#hook-events).                                                                                                               |
| Los servidores MCP en `.mcp.json` nunca se cargan                                | El archivo está bajo `.claude/` o usa el formato de configuración de Claude Desktop                                        | La configuración de MCP del proyecto va en la raíz del repositorio como `.mcp.json`, no dentro de `.claude/`. Consulte [configuración de MCP](/es/mcp).                                                                       |
| Los servidores MCP agregados bajo `mcpServers` en `settings.json` nunca aparecen | `settings.json` no lee una clave `mcpServers`                                                                              | Defina servidores de proyecto en `.mcp.json` en la raíz del repositorio, o ejecute `claude mcp add --scope user` para servidores con ámbito de usuario. Consulte [configuración de MCP](/es/mcp).                             |
| El servidor MCP del proyecto agregado pero no aparece                            | Se descartó el mensaje de aprobación única                                                                                 | Los servidores con ámbito de proyecto requieren aprobación. Ejecute `/mcp` para ver el estado y aprobar.                                                                                                                      |
| El servidor MCP no se inicia desde algunos directorios                           | `command` o `args` usa una ruta de archivo relativa                                                                        | Use rutas absolutas para scripts locales. Los ejecutables en su `PATH` como `npx` o `uvx` funcionan tal cual.                                                                                                                 |
| El servidor MCP se inicia sin las variables de entorno esperadas                 | Las variables están en `settings.json` `env`, que no se propaga a procesos secundarios de MCP                              | Establezca `env` por servidor dentro de `.mcp.json` en su lugar.                                                                                                                                                              |
| La regla de denegación `Bash(rm *)` no bloquea `/bin/rm` o `find -delete`        | Las reglas de prefijo coinciden con la cadena de comando literal, no con el ejecutable subyacente                          | Agregue patrones explícitos para cada variante, o use un [hook PreToolUse](/es/hooks-guide) o el [sandbox](/es/sandboxing) para una garantía dura.                                                                            |

## Recursos relacionados

Para una referencia completa en cada superficie de configuración, consulte la página dedicada:

* **[Referencia del directorio `.claude`](/es/claude-directory)**: cada ubicación de archivo de configuración y qué lo lee
* **[Configuración](/es/settings)**: orden de precedencia y la lista completa de claves
* **[Referencia de hooks](/es/hooks)**: nombres de eventos, cargas útiles y formato de salida `--debug hooks`
* **[MCP](/es/mcp)**: configuración del servidor, aprobación y salida `/mcp`
* **[Solucionar problemas de instalación e inicio de sesión](/es/troubleshoot-install)**: `comando no encontrado`, PATH y problemas de autenticación
* **[Solución de problemas](/es/troubleshooting)**: rendimiento, bloqueos y problemas de búsqueda
