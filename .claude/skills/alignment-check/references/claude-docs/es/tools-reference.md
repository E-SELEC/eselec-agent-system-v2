---
source_url: https://code.claude.com/docs/es/tools-reference
fetched_url: https://code.claude.com/docs/es/tools-reference.md
category: Referencia
status: 200
scraped_at: 2026-05-15T14:28:19+00:00
sha256_16: 827a06f5fad9835d
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Referencia de herramientas

> Referencia completa de las herramientas que Claude Code puede utilizar, incluidos los requisitos de permisos y el comportamiento por herramienta.

Claude Code tiene acceso a un conjunto de herramientas integradas que le ayudan a entender y modificar su base de código. Los nombres de herramientas son las cadenas exactas que utiliza en [reglas de permisos](/es/permissions#tool-specific-permission-rules), [listas de herramientas de subagents](/es/sub-agents) y [coincidencias de hooks](/es/hooks). Para desactivar una herramienta completamente, agregue su nombre al array `deny` en su [configuración de permisos](/es/permissions#tool-specific-permission-rules).

Para agregar herramientas personalizadas, conecte un [servidor MCP](/es/mcp). Para extender Claude con flujos de trabajo basados en prompts reutilizables, escriba una [skill](/es/skills), que se ejecuta a través de la herramienta `Skill` existente en lugar de agregar una nueva entrada de herramienta.

| Herramienta            | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Permiso requerido |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------- |
| `Agent`                | Genera un [subagent](/es/sub-agents) con su propia ventana de contexto para manejar una tarea. Consulte [comportamiento de la herramienta Agent](#agent-tool-behavior)                                                                                                                                                                                                                                                                                                                           | No                |
| `AskUserQuestion`      | Hace preguntas de opción múltiple para recopilar requisitos o aclarar ambigüedades                                                                                                                                                                                                                                                                                                                                                                                                               | No                |
| `Bash`                 | Ejecuta comandos de shell en su entorno. Consulte [comportamiento de la herramienta Bash](#bash-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                   | Sí                |
| `CronCreate`           | Programa una solicitud recurrente o única dentro de la sesión actual. Las tareas tienen alcance de sesión y se restauran en `--resume` o `--continue` si no han expirado. Consulte [tareas programadas](/es/scheduled-tasks)                                                                                                                                                                                                                                                                     | No                |
| `CronDelete`           | Cancela una tarea programada por ID                                                                                                                                                                                                                                                                                                                                                                                                                                                              | No                |
| `CronList`             | Lista todas las tareas programadas en la sesión                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No                |
| `Edit`                 | Realiza ediciones dirigidas a archivos específicos. Consulte [comportamiento de la herramienta Edit](#edit-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                        | Sí                |
| `EnterPlanMode`        | Cambia a Plan Mode para diseñar un enfoque antes de codificar                                                                                                                                                                                                                                                                                                                                                                                                                                    | No                |
| `EnterWorktree`        | Crea un [git worktree](/es/worktrees) aislado y cambia a él. Pase un `path` para cambiar a un worktree existente del repositorio actual en lugar de crear uno nuevo. No disponible para subagents                                                                                                                                                                                                                                                                                                | No                |
| `ExitPlanMode`         | Presenta un plan para aprobación y sale de Plan Mode                                                                                                                                                                                                                                                                                                                                                                                                                                             | Sí                |
| `ExitWorktree`         | Sale de una sesión de worktree y regresa al directorio original. No disponible para subagents                                                                                                                                                                                                                                                                                                                                                                                                    | No                |
| `Glob`                 | Encuentra archivos basados en coincidencia de patrones. Consulte [comportamiento de la herramienta Glob](#glob-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                    | No                |
| `Grep`                 | Busca patrones en el contenido de archivos. Consulte [comportamiento de la herramienta Grep](#grep-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                | No                |
| `ListMcpResourcesTool` | Lista recursos expuestos por [servidores MCP](/es/mcp) conectados                                                                                                                                                                                                                                                                                                                                                                                                                                | No                |
| `LSP`                  | Inteligencia de código a través de servidores de lenguaje: saltar a definiciones, encontrar referencias, reportar errores de tipo y advertencias. Consulte [comportamiento de la herramienta LSP](#lsp-tool-behavior)                                                                                                                                                                                                                                                                            | No                |
| `Monitor`              | Ejecuta un comando en segundo plano y devuelve cada línea de salida a Claude, para que pueda reaccionar a entradas de registro, cambios de archivos, o estado sondeado a mitad de la conversación. Consulte [herramienta Monitor](#monitor-tool)                                                                                                                                                                                                                                                 | Sí                |
| `NotebookEdit`         | Modifica celdas de cuadernos Jupyter. Consulte [comportamiento de la herramienta NotebookEdit](#notebookedit-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                      | Sí                |
| `PowerShell`           | Ejecuta comandos de PowerShell de forma nativa. Consulte [herramienta PowerShell](#powershell-tool) para disponibilidad                                                                                                                                                                                                                                                                                                                                                                          | Sí                |
| `PushNotification`     | Envía una notificación de escritorio, y una notificación push en el teléfono cuando [Remote Control](/es/remote-control) está conectado, para que una tarea de larga duración o [tarea programada](/es/scheduled-tasks) pueda alcanzarlo cuando se aleje. {/* plan-availability: feature=push-notifications providers=anthropic */}La entrega push se ejecuta a través de infraestructura alojada por Anthropic, que no es accesible desde Amazon Bedrock, Google Vertex AI, o Microsoft Foundry | No                |
| `Read`                 | Lee el contenido de archivos. Consulte [comportamiento de la herramienta Read](#read-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                              | No                |
| `ReadMcpResourceTool`  | Lee un recurso MCP específico por URI                                                                                                                                                                                                                                                                                                                                                                                                                                                            | No                |
| `RemoteTrigger`        | Crea, actualiza, ejecuta y lista [Routines](/es/routines) en claude.ai. Respalda el comando `/schedule`. {/* plan-availability: feature=routines plans=pro,max,team,enterprise providers=anthropic */}Las Routines viven en claude.ai y requieren un plan Pro, Max, Team o Enterprise, por lo que esta herramienta no es accesible desde Amazon Bedrock, Google Vertex AI, o Microsoft Foundry                                                                                                   | No                |
| `SendMessage`          | Envía un mensaje a un miembro del [equipo de agentes](/es/agent-teams), o [reanuda un subagent](/es/sub-agents#resume-subagents) por su ID de agente. Los subagents detenidos se reanudan automáticamente en segundo plano. Solo disponible cuando `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` está establecido                                                                                                                                                                                     | No                |
| `ShareOnboardingGuide` | {/* plan-availability: feature=onboarding-guide-share plans=pro,max,team,enterprise providers=anthropic */}Carga `ONBOARDING.md` y devuelve un enlace de compartición que los compañeros de equipo pueden abrir en Claude Code. Se llama desde `/team-onboarding` después de que se escribe la guía. Disponible para suscriptores de claude.ai en planes Pro, Max, Team y Enterprise                                                                                                             | Sí                |
| `Skill`                | Ejecuta una [skill](/es/skills#control-who-invokes-a-skill) dentro de la conversación principal                                                                                                                                                                                                                                                                                                                                                                                                  | Sí                |
| `TaskCreate`           | Crea una nueva tarea en la lista de tareas                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No                |
| `TaskGet`              | Recupera detalles completos para una tarea específica                                                                                                                                                                                                                                                                                                                                                                                                                                            | No                |
| `TaskList`             | Lista todas las tareas con su estado actual                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No                |
| `TaskOutput`           | (Obsoleto) Recupera la salida de una tarea de fondo. Prefiera `Read` en la ruta del archivo de salida de la tarea                                                                                                                                                                                                                                                                                                                                                                                | No                |
| `TaskStop`             | Mata una tarea de fondo en ejecución por ID                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No                |
| `TaskUpdate`           | Actualiza el estado de la tarea, dependencias, detalles, o elimina tareas                                                                                                                                                                                                                                                                                                                                                                                                                        | No                |
| `TeamCreate`           | Crea un [equipo de agentes](/es/agent-teams) con múltiples compañeros de equipo. Solo disponible cuando `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` está establecido                                                                                                                                                                                                                                                                                                                                | No                |
| `TeamDelete`           | Disuelve un equipo de agentes y limpia los procesos de compañeros de equipo. Solo disponible cuando `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` está establecido                                                                                                                                                                                                                                                                                                                                    | No                |
| `TodoWrite`            | Gestiona la lista de verificación de tareas de la sesión. Disponible en modo no interactivo y el [Agent SDK](/es/headless); las sesiones interactivas utilizan TaskCreate, TaskGet, TaskList y TaskUpdate en su lugar                                                                                                                                                                                                                                                                            | No                |
| `ToolSearch`           | Busca y carga herramientas diferidas cuando [búsqueda de herramientas](/es/mcp#scale-with-mcp-tool-search) está habilitada                                                                                                                                                                                                                                                                                                                                                                       | No                |
| `WebFetch`             | Obtiene contenido de una URL especificada. Consulte [comportamiento de la herramienta WebFetch](#webfetch-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                         | Sí                |
| `WebSearch`            | Realiza búsquedas web. Consulte [comportamiento de la herramienta WebSearch](#websearch-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                           | Sí                |
| `Write`                | Crea o sobrescribe archivos. Consulte [comportamiento de la herramienta Write](#write-tool-behavior)                                                                                                                                                                                                                                                                                                                                                                                             | Sí                |

## Configurar herramientas con reglas de permisos y hooks

En su mayor parte, Claude decide cuándo usar estas herramientas y no necesita nombrarlas usted mismo cuando interactúa con Claude. Hace referencia a los nombres de herramientas directamente cuando define permisos y otra configuración:

* en [`permissions.allow` y `permissions.deny`](/es/settings#available-settings) en la configuración, y la interfaz `/permissions`
* en los [indicadores CLI](/es/cli-reference) `--allowedTools` y `--disallowedTools`
* en las opciones [`allowedTools` y `disallowedTools`](/es/agent-sdk/permissions#allow-and-deny-rules) del Agent SDK
* en el [frontmatter](/es/sub-agents#supported-frontmatter-fields) `tools` o `disallowedTools` de un subagent
* en el [frontmatter](/es/skills#frontmatter-reference) `allowed-tools` de una skill
* en la condición [`if`](/es/hooks-guide#filter-by-tool-name-and-arguments-with-the-if-field) de un hook

Todos estos aceptan el mismo formato de regla, `ToolName(specifier)`. El especificador depende de la herramienta, y varias herramientas comparten un formato:

| Formato de regla               | Se aplica a               | Detalles                                                                     |
| :----------------------------- | :------------------------ | :--------------------------------------------------------------------------- |
| `Bash(npm run *)`              | Bash, Monitor             | [Coincidencia de patrón de comando](/es/permissions#bash)                    |
| `PowerShell(Get-ChildItem *)`  | PowerShell                | [Coincidencia de patrón de comando](/es/permissions#powershell)              |
| `Read(~/secrets/**)`           | Read, Grep, Glob, LSP     | [Coincidencia de patrón de ruta](/es/permissions#read-and-edit)              |
| `Edit(/src/**)`                | Edit, Write, NotebookEdit | [Coincidencia de patrón de ruta](/es/permissions#read-and-edit)              |
| `Skill(deploy *)`              | Skill                     | [Coincidencia de nombre de skill](/es/skills#restrict-claude's-skill-access) |
| `Agent(Explore)`               | Agent                     | [Coincidencia de tipo de subagent](/es/permissions#agent-subagents)          |
| `WebFetch(domain:example.com)` | WebFetch                  | [Coincidencia de dominio](/es/permissions#webfetch)                          |
| `WebSearch`                    | WebSearch                 | Sin especificador; permitir o denegar la herramienta en su totalidad         |

Las herramientas no listadas aquí, como `ExitPlanMode` o `ShareOnboardingGuide`, aceptan solo el nombre de herramienta desnudo sin especificador.

Una regla de permiso `Edit(...)` también otorga acceso de lectura a la misma ruta, por lo que no necesita una regla `Read(...)` coincidente.

Los campos `matcher` de Hook utilizan nombres de herramientas desnudos, no el formato de regla entre paréntesis. Consulte [patrones de coincidencia](/es/hooks#matcher-patterns) para las reglas de coincidencia. Para los nombres de campo que cada herramienta pasa a `tool_input` en hooks, consulte la [referencia de entrada PreToolUse](/es/hooks#pretooluse-input).

## Comportamiento de la herramienta Agent

La herramienta Agent genera un subagent en una ventana de contexto separada. El subagent trabaja a través de su tarea de forma autónoma, luego devuelve un único resultado de texto a la conversación principal. El principal no ve las llamadas de herramientas intermedias o salidas del subagent, solo ese resultado final. Para limitar cuántos turnos ejecuta un subagent, establezca `maxTurns` en la [definición del subagent](/es/sub-agents#supported-frontmatter-fields).

La misma herramienta Agent también lanza [subagents bifurcados](/es/sub-agents#fork-the-current-conversation) cuando el modo de bifurcación está habilitado. Una bifurcación hereda la conversación principal completa en lugar de comenzar de nuevo, siempre se ejecuta en segundo plano, y aún muestra solicitudes de permisos en su terminal. El resto de esta sección describe subagents nombrados.

Qué herramientas puede usar un subagent nombrado depende de los campos `tools` y `disallowedTools` en la [definición del subagent](/es/sub-agents):

* **Ningún campo establecido**: el subagent hereda todas las herramientas disponibles para el principal.
* **Solo `tools`**: el subagent obtiene solo las herramientas listadas.
* **Solo `disallowedTools`**: el subagent obtiene todas las herramientas principales excepto las listadas.
* **Ambos establecidos**: `disallowedTools` tiene precedencia. Una herramienta listada en ambos se elimina.

Lanzar el subagent no solicita permiso en sí mismo. Las propias llamadas de herramientas del subagent se verifican contra sus reglas de permisos mientras se ejecuta:

* **Subagents en primer plano** muestran los mismos solicitudes de permisos que vería en la conversación principal, en el momento en que ocurre cada llamada de herramienta.
* **Subagents en segundo plano** no muestran solicitudes. Se ejecutan con los permisos ya otorgados en la sesión y deniegan automáticamente cualquier llamada de herramienta que de otro modo solicitaría. Después de una denegación, el subagent continúa sin esa herramienta.

Para limitar lo que un subagent puede alcanzar en primer lugar, reduzca su campo `tools`, deje Bash fuera de la lista, o establezca reglas de denegación en su configuración, como se describe en [Controlar capacidades de subagent](/es/sub-agents#control-subagent-capabilities). Para más información sobre cómo elegir entre primer plano y segundo plano, consulte [Ejecutar subagents en primer plano o segundo plano](/es/sub-agents#run-subagents-in-foreground-or-background).

## Comportamiento de la herramienta Bash

La herramienta Bash ejecuta cada comando en un proceso separado con el siguiente comportamiento de persistencia:

* Cuando Claude ejecuta `cd` en la sesión principal, el nuevo directorio de trabajo se mantiene en comandos Bash posteriores siempre que permanezca dentro del directorio del proyecto o un [directorio de trabajo adicional](/es/permissions#working-directories) que agregó con `--add-dir`, `/add-dir`, o `additionalDirectories` en la configuración. Las sesiones de subagents nunca mantienen cambios de directorio de trabajo.
  * Si `cd` cae fuera de esos directorios, Claude Code se reinicia al directorio del proyecto y añade `Shell cwd was reset to <dir>` al resultado de la herramienta.
  * Para desactivar este mantenimiento para que cada comando Bash comience en el directorio del proyecto, establezca `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1`.
* Las variables de entorno no persisten. Un `export` en un comando no estará disponible en el siguiente.

Active su entorno virtualenv o conda antes de lanzar Claude Code. Para hacer que las variables de entorno persistan entre comandos Bash, establezca [`CLAUDE_ENV_FILE`](/es/env-vars) en un script de shell antes de lanzar Claude Code, o use un [hook SessionStart](/es/hooks#persist-environment-variables) para poblarlo dinámicamente.

Dos límites acotan cada comando:

* **Tiempo de espera**: dos minutos por defecto. Claude puede solicitar hasta 10 minutos por comando con el parámetro `timeout`. Anule el valor predeterminado y el techo con [`BASH_DEFAULT_TIMEOUT_MS` y `BASH_MAX_TIMEOUT_MS`](/es/env-vars).
* **Longitud de salida**: 30.000 caracteres por defecto. Cuando un comando produce más que eso, Claude Code guarda la salida completa en un archivo en el directorio de sesión y le da a Claude la ruta del archivo más una vista previa corta desde el inicio. Claude lee o busca ese archivo cuando necesita el resto. Aumente el límite con [`BASH_MAX_OUTPUT_LENGTH`](/es/env-vars), hasta un techo duro de 150.000 caracteres.

Para procesos de larga duración como servidores de desarrollo o compilaciones de vigilancia, Claude puede establecer `run_in_background: true` para iniciar el comando como una tarea de fondo y continuar trabajando mientras se ejecuta. Liste y detenga tareas de fondo con `/tasks`.

## Comportamiento de la herramienta Edit

La herramienta Edit realiza reemplazo exacto de cadenas. Toma un `old_string` y un `new_string` y reemplaza el primero con el segundo. No utiliza expresiones regulares o coincidencia difusa.

Tres verificaciones deben pasar para que se aplique una edición:

* **Lectura antes de edición**: Claude debe haber leído el archivo en la conversación actual, y el archivo no debe haber cambiado en el disco desde esa lectura. Esta verificación se ejecuta primero, antes de cualquier coincidencia de cadena.
* **Coincidencia**: `old_string` debe aparecer en el archivo exactamente como está escrito. Una sola diferencia de carácter de espacio en blanco o indentación es suficiente para fallar.
* **Unicidad**: `old_string` debe aparecer exactamente una vez. Cuando aparece más de una vez, Claude proporciona una cadena más larga con suficiente contexto circundante para fijar una ocurrencia, o establece `replace_all: true` para reemplazarlas todas.

Ver un archivo con Bash también satisface el requisito de lectura antes de edición cuando el comando es `cat path/to/file` o `sed -n 'X,Yp' path/to/file` en un único archivo sin tuberías o redirecciones. Otros comandos Bash como `head`, `tail`, o salida canalizada no cuentan, y Claude debe usar Read antes de editar en esos casos.

Esto afecta solo la elegibilidad de edición, no los permisos. Las [reglas de denegación de Read y Edit](/es/permissions#tool-specific-permission-rules) también se aplican a comandos de archivo que Claude Code reconoce en Bash, como `cat`, `head`, `tail`, y `sed`, pero no a subprocesos arbitrarios que leen o escriben archivos indirectamente, como un script de Python o Node que abre archivos por sí mismo. Para la aplicación a nivel del sistema operativo que cubre todos los procesos, [habilite el sandbox](/es/sandboxing).

## Comportamiento de la herramienta Glob

La herramienta Glob encuentra archivos por patrón de nombre. Admite sintaxis glob estándar incluyendo `**` para coincidencia de directorio recursivo:

* `**/*.js` coincide con todos los archivos `.js` a cualquier profundidad
* `src/**/*.ts` coincide con todos los archivos `.ts` bajo `src/`
* `*.{json,yaml}` coincide con archivos `.json` y `.yaml` en el directorio actual

Los resultados se ordenan por tiempo de modificación y se limitan a 100 archivos. Si se alcanza el límite, Claude ve una bandera de truncamiento en el resultado y puede estrechar el patrón.

Glob no respeta `.gitignore` por defecto, por lo que encuentra archivos ignorados por git junto con los rastreados. Esto difiere de [Grep](#grep-tool-behavior), que omite archivos ignorados por git. Para hacer que Glob respete `.gitignore`, establezca `CLAUDE_CODE_GLOB_NO_IGNORE=false` antes de lanzar Claude Code.

## Comportamiento de la herramienta Grep

La herramienta Grep busca patrones en el contenido de archivos. Donde [Glob](#glob-tool-behavior) encuentra archivos por nombre, Grep encuentra líneas dentro de ellos.

Grep se basa en [ripgrep](https://github.com/BurntSushi/ripgrep) y utiliza la sintaxis regex de ripgrep, no grep de POSIX. Los patrones que incluyen metacaracteres regex necesitan escape. Por ejemplo, encontrar `interface{}` en código Go requiere el patrón `interface\{\}`.

Tres modos de salida controlan lo que regresa:

* `files_with_matches`: solo rutas de archivo, sin contenido de línea. Este es el predeterminado.
* `content`: líneas coincidentes con número de archivo y línea.
* `count`: recuento de coincidencias por archivo.

Claude puede limitar resultados por archivo con el parámetro `glob`, como `**/*.tsx`, o por lenguaje con el parámetro `type`, como `py` o `rust`. Por defecto, los patrones coinciden dentro de una sola línea. Claude puede establecer `multiline: true` para coincidir entre límites de línea.

Grep respeta `.gitignore`, por lo que los archivos ignorados por git se omiten. Para buscar un archivo ignorado por git, Claude pasa su ruta directamente.

## Comportamiento de la herramienta LSP

La herramienta LSP proporciona a Claude inteligencia de código desde un servidor de lenguaje en ejecución. Después de cada edición de archivo, reporta automáticamente errores de tipo y advertencias para que Claude pueda corregir problemas sin un paso de compilación separado. Claude también puede llamarlo directamente para navegar por el código:

* Saltar a la definición de un símbolo
* Encontrar todas las referencias a un símbolo
* Obtener información de tipo en una posición
* Listar símbolos en un archivo o espacio de trabajo
* Encontrar implementaciones de una interfaz
* Rastrear jerarquías de llamadas

La herramienta está inactiva hasta que instale un [plugin de inteligencia de código](/es/discover-plugins#code-intelligence) para su lenguaje. El plugin agrupa la configuración del servidor de lenguaje, e instala el binario del servidor por separado.

## Herramienta Monitor

<Note>
  La herramienta Monitor requiere Claude Code v2.1.98 o posterior.
</Note>

La herramienta Monitor permite que Claude observe algo en segundo plano y reaccione cuando cambia, sin pausar la conversación. Pida a Claude que:

* Siga un archivo de registro y marque errores a medida que aparecen
* Sondee una PR o trabajo de CI y reporte cuando su estado cambia
* Observe un directorio para cambios de archivos
* Rastrear la salida de cualquier script de larga duración que señale

Claude escribe un pequeño script para la observación, lo ejecuta en segundo plano, y recibe cada línea de salida a medida que llega. Continúa trabajando en la misma sesión y Claude interviene cuando llega un evento. Detenga un monitor pidiendo a Claude que lo cancele o terminando la sesión.

Monitor utiliza las mismas [reglas de permisos que Bash](/es/permissions#tool-specific-permission-rules), por lo que los patrones `allow` y `deny` que tiene establecidos para Bash se aplican aquí también. No está disponible en Amazon Bedrock, Google Vertex AI, o Microsoft Foundry. Tampoco está disponible cuando `DISABLE_TELEMETRY` o `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` está establecido.

Los plugins pueden declarar monitores que se inician automáticamente cuando el plugin está activo, en lugar de pedirle a Claude que los inicie. Consulte [monitores de plugins](/es/plugins-reference#monitors).

## Comportamiento de la herramienta NotebookEdit

NotebookEdit modifica un cuaderno Jupyter una celda a la vez, dirigiéndose a celdas por su `cell_id`. No realiza reemplazo de cadenas en todo el cuaderno de la manera que [Edit](#edit-tool-behavior) lo hace en archivos simples.

Tres modos de edición controlan lo que sucede con la celda objetivo:

* `replace`: sobrescribe la fuente de la celda. Este es el predeterminado.
* `insert`: agrega una nueva celda después de la objetivo. Sin `cell_id`, la nueva celda va al inicio del cuaderno. Requiere `cell_type` establecido a `code` o `markdown`.
* `delete`: elimina la celda objetivo.

Las reglas de permisos utilizan el formato de ruta `Edit(...)`. Una regla como `Edit(notebooks/**)` cubre llamadas de NotebookEdit en archivos en ese directorio.

## Herramienta PowerShell

La herramienta PowerShell permite que Claude ejecute comandos de PowerShell de forma nativa. En Windows, esto significa que los comandos se ejecutan en PowerShell en lugar de enrutarse a través de Git Bash. En Windows sin Git Bash, la herramienta se habilita automáticamente. En Windows con Git Bash instalado, la herramienta se está implementando progresivamente. En Linux, macOS y WSL, la herramienta es opcional.

### Habilitar la herramienta PowerShell

Establezca `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` en su entorno o en `settings.json`:

```json theme={null}
{
  "env": {
    "CLAUDE_CODE_USE_POWERSHELL_TOOL": "1"
  }
}
```

En Windows, establezca la variable a `0` para optar por no participar en la implementación. En Linux, macOS y WSL, la herramienta requiere PowerShell 7 o posterior: instale `pwsh` y asegúrese de que esté en su `PATH`.

En Windows, Claude Code detecta automáticamente `pwsh.exe` para PowerShell 7+ con una alternativa a `powershell.exe` para PowerShell 5.1. Cuando la herramienta está habilitada, Claude trata PowerShell como el shell principal. La herramienta Bash permanece disponible para scripts POSIX cuando Git Bash está instalado.

### Selección de shell en configuración, hooks y skills

Tres configuraciones adicionales controlan dónde se usa PowerShell:

* `"defaultShell": "powershell"` en [`settings.json`](/es/settings#available-settings): enruta comandos interactivos `!` a través de PowerShell. Requiere que la herramienta PowerShell esté habilitada.
* `"shell": "powershell"` en [hooks de comando](/es/hooks#command-hook-fields) individuales: ejecuta ese hook en PowerShell. Los hooks generan PowerShell directamente, por lo que esto funciona independientemente de `CLAUDE_CODE_USE_POWERSHELL_TOOL`.
* `shell: powershell` en [frontmatter de skill](/es/skills#frontmatter-reference): ejecuta bloques `` !`command` `` en PowerShell. Requiere que la herramienta PowerShell esté habilitada.

El mismo comportamiento de reinicio del directorio de trabajo de la sesión principal descrito en la sección de la herramienta Bash se aplica a los comandos de PowerShell, incluida la variable de entorno `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR`.

### Limitaciones de vista previa

La herramienta PowerShell tiene las siguientes limitaciones conocidas durante la vista previa:

* Los perfiles de PowerShell no se cargan
* En Windows, el sandboxing no es compatible

## Comportamiento de la herramienta Read

La herramienta Read toma una ruta de archivo y devuelve el contenido con números de línea. Claude recibe instrucciones de siempre pasar rutas absolutas.

Por defecto, Read devuelve el archivo desde el inicio. Los archivos sobre un umbral de tamaño devuelven un error en lugar de contenido parcial, lo que solicita a Claude que reintente con `offset` y `limit` para leer un rango específico.

Read maneja varios tipos de archivo más allá del texto simple:

* **Imágenes**: PNG, JPG y otros formatos de imagen se devuelven como contenido visual que Claude puede ver, no como bytes sin procesar. Claude Code redimensiona y recomprime imágenes grandes para ajustarse a los límites de tamaño de imagen del modelo antes de enviarlas, por lo que Claude puede ver una versión reducida de una captura de pantalla grande. Si Claude pierde detalle a nivel de píxel fino en una imagen grande, pídale que primero recorte la región de interés, por ejemplo con ImageMagick a través de Bash.
* **PDFs**: Claude lee archivos `.pdf` cortos completos. Para PDFs más largos que 10 páginas, lee en rangos con un parámetro `pages`, como `"1-5"`, hasta 20 páginas a la vez.
* **Cuadernos Jupyter**: los archivos `.ipynb` devuelven todas las celdas con sus salidas, incluyendo código, markdown y visualizaciones.

Read solo lee archivos, no directorios. Claude utiliza `ls` a través de la herramienta Bash para listar contenidos de directorio.

## Comportamiento de la herramienta WebFetch

WebFetch toma una URL y un prompt describiendo qué extraer. Obtiene la página, convierte la respuesta a Markdown cuando el servidor devuelve HTML, y ejecuta el prompt contra el contenido usando un modelo pequeño y rápido. Para la mayoría de obtenciones, Claude recibe la respuesta de ese modelo, no la página sin procesar. El paso de conversión no es configurable.

Esto hace que WebFetch sea con pérdida por diseño. El prompt de extracción determina lo que llega a Claude, por lo que un resultado que dice que una página no menciona algo puede solo significar que el prompt no preguntó por ello. Pida a Claude que obtenga de nuevo con un prompt más específico, o use `curl` a través de Bash para la página sin procesar.

Algunos comportamientos dan forma a la respuesta que Claude recibe:

* Las URLs HTTP se actualizan automáticamente a HTTPS.
* Las páginas grandes se truncan a un límite de caracteres fijo antes del procesamiento.
* Las respuestas se almacenan en caché durante 15 minutos, por lo que las obtenciones repetidas de la misma URL regresan rápidamente.
* Cuando una URL se redirige a un host diferente, WebFetch devuelve un resultado de texto que nombra la URL original y el destino de redirección en lugar de seguirlo. Claude luego obtiene la nueva URL con una segunda llamada de WebFetch.

En los modos de permiso predeterminado y `acceptEdits`, WebFetch solicita la primera vez que alcanza un nuevo dominio. Para permitir un dominio por adelantado sin una solicitud, agregue una regla de permiso como `WebFetch(domain:example.com)`. Los modos de permiso `auto` y `bypassPermissions` [permission modes](/es/permissions#permission-modes) omiten la solicitud completamente.

WebFetch establece un encabezado `User-Agent` que comienza con `Claude-User`, y un encabezado `Accept` que prefiere Markdown sobre HTML para que los servidores que admiten negociación de contenido puedan devolver Markdown directamente. Las [reglas de red de Sandbox](/es/sandboxing) se configuran por separado, por lo que un dominio que desea que un proceso en sandbox alcance aún necesita una regla de permiso de sandbox explícita.

## Comportamiento de la herramienta WebSearch

WebSearch ejecuta una consulta contra el backend de [búsqueda web](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) de Anthropic y devuelve títulos y URLs de resultados. No obtiene las páginas de resultados. Para leer una página que Claude encuentra en resultados de búsqueda, continúa con [WebFetch](#webfetch-tool-behavior).

La herramienta puede emitir hasta ocho búsquedas de backend por llamada, refinando la búsqueda internamente antes de devolver resultados. Claude puede limitar resultados con `allowed_domains` para incluir solo ciertos hosts, o `blocked_domains` para excluirlos. Las dos listas no se pueden combinar en una sola llamada.

El backend de búsqueda no es configurable. Para buscar con un proveedor diferente, agregue un [servidor MCP](/es/mcp) que exponga una herramienta de búsqueda.

Las reglas de permisos de WebSearch no toman especificador. Una entrada `WebSearch` desnuda en `allow` o `deny` es la única forma.

<Note>
  WebSearch está disponible en la API de Claude y Microsoft Foundry. En Google Cloud Vertex AI funciona con modelos Claude 4, incluyendo Opus, Sonnet y Haiku. Amazon Bedrock no expone la herramienta de búsqueda web del lado del servidor.
</Note>

## Comportamiento de la herramienta Write

La herramienta Write crea un nuevo archivo o sobrescribe uno existente con el contenido completo proporcionado. No añade ni fusiona.

Si la ruta objetivo ya existe, Claude debe haber leído ese archivo al menos una vez en la conversación actual antes de sobrescribirlo. Una Write a un archivo existente no leído falla con un error. Esta restricción no se aplica a archivos nuevos.

Ver el archivo con Bash `cat` o `sed -n` también satisface este requisito, como se describe en [comportamiento de la herramienta Edit](#edit-tool-behavior).

Para cambios parciales a un archivo existente, Claude utiliza Edit en lugar de Write.

## Verificar qué herramientas están disponibles

Su conjunto exacto de herramientas depende de su proveedor, plataforma y configuración. Para verificar qué está cargado en una sesión en ejecución, pregúntele a Claude directamente:

```text theme={null}
¿Qué herramientas tienes disponibles?
```

Claude proporciona un resumen conversacional. Para nombres exactos de herramientas MCP, ejecute `/mcp`.

## Véase también

* [Servidores MCP](/es/mcp): agregue herramientas personalizadas conectando servidores externos
* [Permisos](/es/permissions): sistema de permisos, sintaxis de reglas y patrones específicos de herramientas
* [Subagents](/es/sub-agents): configure el acceso a herramientas para subagents
* [Hooks](/es/hooks-guide): ejecute comandos personalizados antes o después de la ejecución de herramientas
