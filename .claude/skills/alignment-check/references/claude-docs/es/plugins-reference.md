---
source_url: https://code.claude.com/docs/es/plugins-reference
fetched_url: https://code.claude.com/docs/es/plugins-reference.md
category: Referencia
status: 200
scraped_at: 2026-05-15T14:28:22+00:00
sha256_16: 605f4cad5cf93858
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Referencia de plugins

> Referencia técnica completa para el sistema de plugins de Claude Code, incluyendo esquemas, comandos CLI y especificaciones de componentes.

<Tip>
  ¿Buscas instalar plugins? Consulta [Descubrir e instalar plugins](/es/discover-plugins). Para crear plugins, consulta [Plugins](/es/plugins). Para distribuir plugins, consulta [Marketplaces de plugins](/es/plugin-marketplaces).
</Tip>

Esta referencia proporciona especificaciones técnicas completas para el sistema de plugins de Claude Code, incluyendo esquemas de componentes, comandos CLI y herramientas de desarrollo.

Un **plugin** es un directorio independiente de componentes que extiende Claude Code con funcionalidad personalizada. Los componentes del plugin incluyen skills, agents, hooks, servidores MCP, servidores LSP y monitores.

## Referencia de componentes de plugins

### Skills

Los plugins añaden skills a Claude Code, creando atajos `/name` que usted o Claude pueden invocar.

**Ubicación**: Directorio `skills/` o `commands/` en la raíz del plugin

**Formato de archivo**: Los skills son directorios con `SKILL.md`; los comandos son archivos markdown simples

**Estructura de skill**:

```text theme={null}
skills/
├── pdf-processor/
│   ├── SKILL.md
│   ├── reference.md (opcional)
│   └── scripts/ (opcional)
└── code-reviewer/
    └── SKILL.md
```

**Comportamiento de integración**:

* Los skills y comandos se descubren automáticamente cuando se instala el plugin
* Claude puede invocarlos automáticamente según el contexto de la tarea
* Los skills pueden incluir archivos de apoyo junto a SKILL.md

Para obtener detalles completos, consulte [Skills](/es/skills).

### Agents

Los plugins pueden proporcionar subagents especializados para tareas específicas que Claude puede invocar automáticamente cuando sea apropiado.

**Ubicación**: Directorio `agents/` en la raíz del plugin

**Formato de archivo**: Archivos markdown que describen las capacidades del agent

**Estructura del agent**:

```markdown theme={null}
---
name: agent-name
description: En qué se especializa este agent y cuándo Claude debe invocarlo
model: sonnet
effort: medium
maxTurns: 20
disallowedTools: Write, Edit
---

Prompt del sistema detallado para el agent describiendo su rol, experiencia y comportamiento.
```

Los agents del plugin soportan campos frontmatter `name`, `description`, `model`, `effort`, `maxTurns`, `tools`, `disallowedTools`, `skills`, `memory`, `background` e `isolation`. El único valor válido de `isolation` es `"worktree"`. Por razones de seguridad, `hooks`, `mcpServers` y `permissionMode` no se soportan para agents distribuidos con plugins.

**Puntos de integración**:

* Los agents aparecen en la interfaz `/agents`
* Claude puede invocar agents automáticamente según el contexto de la tarea
* Los agents pueden ser invocados manualmente por los usuarios
* Los agents del plugin funcionan junto con los agents integrados de Claude

Para obtener detalles completos, consulte [Subagents](/es/sub-agents).

### Hooks

Los plugins pueden proporcionar manejadores de eventos que responden automáticamente a eventos de Claude Code.

**Ubicación**: `hooks/hooks.json` en la raíz del plugin, o en línea en plugin.json

**Formato**: Configuración JSON con coincidencias de eventos y acciones

**Configuración de hook**:

```json theme={null}
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/format-code.sh"
          }
        ]
      }
    ]
  }
}
```

Los hooks del plugin responden a los mismos eventos del ciclo de vida que los [hooks definidos por el usuario](/es/hooks):

| Event                 | When it fires                                                                                                                                          |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SessionStart`        | When a session begins or resumes                                                                                                                       |
| `Setup`               | When you start Claude Code with `--init-only`, or with `--init` or `--maintenance` in `-p` mode. For one-time preparation in CI or scripts             |
| `UserPromptSubmit`    | When you submit a prompt, before Claude processes it                                                                                                   |
| `UserPromptExpansion` | When a user-typed command expands into a prompt, before it reaches Claude. Can block the expansion                                                     |
| `PreToolUse`          | Before a tool call executes. Can block it                                                                                                              |
| `PermissionRequest`   | When a permission dialog appears                                                                                                                       |
| `PermissionDenied`    | When a tool call is denied by the auto mode classifier. Return `{retry: true}` to tell the model it may retry the denied tool call                     |
| `PostToolUse`         | After a tool call succeeds                                                                                                                             |
| `PostToolUseFailure`  | After a tool call fails                                                                                                                                |
| `PostToolBatch`       | After a full batch of parallel tool calls resolves, before the next model call                                                                         |
| `Notification`        | When Claude Code sends a notification                                                                                                                  |
| `SubagentStart`       | When a subagent is spawned                                                                                                                             |
| `SubagentStop`        | When a subagent finishes                                                                                                                               |
| `TaskCreated`         | When a task is being created via `TaskCreate`                                                                                                          |
| `TaskCompleted`       | When a task is being marked as completed                                                                                                               |
| `Stop`                | When Claude finishes responding                                                                                                                        |
| `StopFailure`         | When the turn ends due to an API error. Output and exit code are ignored                                                                               |
| `TeammateIdle`        | When an [agent team](/en/agent-teams) teammate is about to go idle                                                                                     |
| `InstructionsLoaded`  | When a CLAUDE.md or `.claude/rules/*.md` file is loaded into context. Fires at session start and when files are lazily loaded during a session         |
| `ConfigChange`        | When a configuration file changes during a session                                                                                                     |
| `CwdChanged`          | When the working directory changes, for example when Claude executes a `cd` command. Useful for reactive environment management with tools like direnv |
| `FileChanged`         | When a watched file changes on disk. The `matcher` field specifies which filenames to watch                                                            |
| `WorktreeCreate`      | When a worktree is being created via `--worktree` or `isolation: "worktree"`. Replaces default git behavior                                            |
| `WorktreeRemove`      | When a worktree is being removed, either at session exit or when a subagent finishes                                                                   |
| `PreCompact`          | Before context compaction                                                                                                                              |
| `PostCompact`         | After context compaction completes                                                                                                                     |
| `Elicitation`         | When an MCP server requests user input during a tool call                                                                                              |
| `ElicitationResult`   | After a user responds to an MCP elicitation, before the response is sent back to the server                                                            |
| `SessionEnd`          | When a session terminates                                                                                                                              |

**Tipos de hook**:

* `command`: ejecutar comandos de shell o scripts
* `http`: enviar el JSON del evento como una solicitud POST a una URL
* `mcp_tool`: llamar a una herramienta en un [servidor MCP](/es/mcp) configurado
* `prompt`: evaluar un prompt con un LLM (usa el marcador de posición `$ARGUMENTS` para el contexto)
* `agent`: ejecutar un verificador agentic con herramientas para tareas de verificación complejas

### MCP servers

Los plugins pueden agrupar servidores Model Context Protocol (MCP) para conectar Claude Code con herramientas y servicios externos.

**Ubicación**: `.mcp.json` en la raíz del plugin, o en línea en plugin.json

**Formato**: Configuración estándar del servidor MCP

**Configuración del servidor MCP**:

```json theme={null}
{
  "mcpServers": {
    "plugin-database": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": {
        "DB_PATH": "${CLAUDE_PLUGIN_ROOT}/data"
      }
    },
    "plugin-api-client": {
      "command": "npx",
      "args": ["@company/mcp-server", "--plugin-mode"],
      "cwd": "${CLAUDE_PLUGIN_ROOT}"
    }
  }
}
```

**Comportamiento de integración**:

* Los servidores MCP del plugin se inician automáticamente cuando se habilita el plugin
* Los servidores aparecen como herramientas MCP estándar en el kit de herramientas de Claude
* Las capacidades del servidor se integran sin problemas con las herramientas existentes de Claude
* Los servidores del plugin se pueden configurar independientemente de los servidores MCP del usuario

### LSP servers

<Tip>
  ¿Buscas usar plugins LSP? Instálalos desde el marketplace oficial: busca "lsp" en la pestaña Discover de `/plugin`. Esta sección documenta cómo crear plugins LSP para lenguajes no cubiertos por el marketplace oficial.
</Tip>

Los plugins pueden proporcionar servidores [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) (LSP) para dar a Claude inteligencia de código en tiempo real mientras trabaja en su base de código.

La integración de LSP proporciona:

* **Diagnósticos instantáneos**: Claude ve errores y advertencias inmediatamente después de cada edición
* **Navegación de código**: ir a definición, encontrar referencias e información al pasar el ratón
* **Conciencia del lenguaje**: información de tipo y documentación para símbolos de código

**Ubicación**: `.lsp.json` en la raíz del plugin, o en línea en `plugin.json`

**Formato**: Configuración JSON que asigna nombres de servidores de lenguaje a sus configuraciones

**Formato del archivo `.lsp.json`**:

```json theme={null}
{
  "go": {
    "command": "gopls",
    "args": ["serve"],
    "extensionToLanguage": {
      ".go": "go"
    }
  }
}
```

**En línea en `plugin.json`**:

```json theme={null}
{
  "name": "my-plugin",
  "lspServers": {
    "go": {
      "command": "gopls",
      "args": ["serve"],
      "extensionToLanguage": {
        ".go": "go"
      }
    }
  }
}
```

**Campos requeridos:**

| Campo                 | Descripción                                                 |
| :-------------------- | :---------------------------------------------------------- |
| `command`             | El binario LSP a ejecutar (debe estar en PATH)              |
| `extensionToLanguage` | Asigna extensiones de archivo a identificadores de lenguaje |

**Campos opcionales:**

| Campo                   | Descripción                                                         |
| :---------------------- | :------------------------------------------------------------------ |
| `args`                  | Argumentos de línea de comandos para el servidor LSP                |
| `transport`             | Transporte de comunicación: `stdio` (predeterminado) o `socket`     |
| `env`                   | Variables de entorno a establecer al iniciar el servidor            |
| `initializationOptions` | Opciones pasadas al servidor durante la inicialización              |
| `settings`              | Configuración pasada a través de `workspace/didChangeConfiguration` |
| `workspaceFolder`       | Ruta de carpeta de espacio de trabajo para el servidor              |
| `startupTimeout`        | Tiempo máximo para esperar el inicio del servidor (milisegundos)    |
| `shutdownTimeout`       | Tiempo máximo para esperar el apagado elegante (milisegundos)       |
| `restartOnCrash`        | Si se debe reiniciar automáticamente el servidor si se bloquea      |
| `maxRestarts`           | Número máximo de intentos de reinicio antes de rendirse             |

<Warning>
  **Debe instalar el binario del servidor de lenguaje por separado.** Los plugins LSP configuran cómo Claude Code se conecta a un servidor de lenguaje, pero no incluyen el servidor en sí. Si ve `Executable not found in $PATH` en la pestaña Errors de `/plugin`, instale el binario requerido para su lenguaje.
</Warning>

**Plugins LSP disponibles:**

| Plugin              | Servidor de lenguaje       | Comando de instalación                                                                       |
| :------------------ | :------------------------- | :------------------------------------------------------------------------------------------- |
| `pyright-lsp`       | Pyright (Python)           | `pip install pyright` o `npm install -g pyright`                                             |
| `typescript-lsp`    | TypeScript Language Server | `npm install -g typescript-language-server typescript`                                       |
| `rust-analyzer-lsp` | rust-analyzer              | [Ver instalación de rust-analyzer](https://rust-analyzer.github.io/manual.html#installation) |

Instale el servidor de lenguaje primero, luego instale el plugin desde el marketplace.

### Monitors

Los plugins pueden declarar monitores de fondo que Claude Code inicia automáticamente cuando el plugin está activo. Cada monitor ejecuta un comando de shell durante la vida útil de la sesión y entrega cada línea de stdout a Claude como una notificación, para que Claude pueda reaccionar a entradas de registro, cambios de estado o eventos sondeados sin que se le pida que inicie la vigilancia por sí mismo.

Los monitores del plugin utilizan el mismo mecanismo que la [herramienta Monitor](/es/tools-reference#monitor-tool) y comparten sus restricciones de disponibilidad. Se ejecutan solo en sesiones CLI interactivas, se ejecutan sin sandbox al mismo nivel de confianza que los [hooks](#hooks), y se omiten en hosts donde la herramienta Monitor no está disponible.

<Note>
  Los monitores del plugin requieren Claude Code v2.1.105 o posterior.
</Note>

**Ubicación**: `monitors/monitors.json` en la raíz del plugin, o en línea en `plugin.json`

**Formato**: Array JSON de entradas de monitor

El siguiente `monitors/monitors.json` vigila un endpoint de estado de implementación y un registro de errores local:

```json theme={null}
[
  {
    "name": "deploy-status",
    "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/poll-deploy.sh ${user_config.api_endpoint}",
    "description": "Cambios de estado de implementación"
  },
  {
    "name": "error-log",
    "command": "tail -F ./logs/error.log",
    "description": "Registro de errores de la aplicación",
    "when": "on-skill-invoke:debug"
  }
]
```

Para declarar monitores en línea, establezca `experimental.monitors` en `plugin.json` en el mismo array. Para cargar desde una ruta no predeterminada, establezca `experimental.monitors` en una cadena de ruta relativa como `"./config/monitors.json"`. Los monitores son un [componente experimental](#experimental-components).

**Campos requeridos:**

| Campo         | Descripción                                                                                                                      |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------- |
| `name`        | Identificador único dentro del plugin. Previene procesos duplicados cuando el plugin se recarga o se invoca una skill nuevamente |
| `command`     | Comando de shell ejecutado como un proceso de fondo persistente en el directorio de trabajo de la sesión                         |
| `description` | Resumen breve de lo que se está vigilando. Se muestra en el panel de tareas y en resúmenes de notificaciones                     |

**Campos opcionales:**

| Campo  | Descripción                                                                                                                                                                                                                                        |
| :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `when` | Controla cuándo se inicia el monitor. `"always"` lo inicia al inicio de la sesión y en la recarga del plugin, y es el predeterminado. `"on-skill-invoke:<skill-name>"` lo inicia la primera vez que se distribuye la skill nombrada en este plugin |

El valor `command` soporta las mismas [sustituciones de variables](#environment-variables) que las configuraciones de servidores MCP y LSP: `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`, `${CLAUDE_PROJECT_DIR}`, `${user_config.*}` y cualquier `${ENV_VAR}` del entorno. Prefije el comando con `cd "${CLAUDE_PLUGIN_ROOT}" && ` si el script necesita ejecutarse desde el directorio del plugin.

Deshabilitar un plugin a mitad de sesión no detiene los monitores que ya se están ejecutando. Se detienen cuando termina la sesión.

### Themes

Los plugins pueden distribuir temas de color que aparecen en `/theme` junto con los presets integrados y los temas locales del usuario. Un tema es un archivo JSON en `themes/` con un preset `base` y un mapa disperso `overrides` de tokens de color. Los temas son un [componente experimental](#experimental-components).

```json theme={null}
{
  "name": "Dracula",
  "base": "dark",
  "overrides": {
    "claude": "#bd93f9",
    "error": "#ff5555",
    "success": "#50fa7b"
  }
}
```

Seleccionar un tema de plugin persiste `custom:<plugin-name>:<slug>` en la configuración del usuario. Los temas de plugin son de solo lectura; presionar `Ctrl+E` en uno en `/theme` lo copia en `~/.claude/themes/` para que el usuario pueda editar la copia.

***

## Alcances de instalación de plugins

Cuando instalas un plugin, eliges un **alcance** que determina dónde está disponible el plugin y quién más puede usarlo:

| Alcance   | Archivo de configuración                                  | Caso de uso                                                            |
| :-------- | :-------------------------------------------------------- | :--------------------------------------------------------------------- |
| `user`    | `~/.claude/settings.json`                                 | Plugins personales disponibles en todos los proyectos (predeterminado) |
| `project` | `.claude/settings.json`                                   | Plugins de equipo compartidos a través del control de versiones        |
| `local`   | `.claude/settings.local.json`                             | Plugins específicos del proyecto, ignorados por git                    |
| `managed` | [Configuración administrada](/es/settings#settings-files) | Plugins administrados (solo lectura, solo actualizar)                  |

Los plugins utilizan el mismo sistema de alcance que otras configuraciones de Claude Code. Para instrucciones de instalación y banderas de alcance, consulta [Instalar plugins](/es/discover-plugins#install-plugins). Para una explicación completa de los alcances, consulta [Alcances de configuración](/es/settings#configuration-scopes).

***

## Esquema del manifiesto del plugin

El archivo `.claude-plugin/plugin.json` define los metadatos y la configuración de tu plugin. Esta sección documenta todos los campos y opciones soportados.

El manifiesto es opcional. Si se omite, Claude Code descubre automáticamente componentes en [ubicaciones predeterminadas](#file-locations-reference) y deriva el nombre del plugin del nombre del directorio. Usa un manifiesto cuando necesites proporcionar metadatos o rutas de componentes personalizadas.

### Esquema completo

```json theme={null}
{
  "name": "plugin-name",
  "version": "1.2.0",
  "description": "Brief plugin description",
  "author": {
    "name": "Author Name",
    "email": "author@example.com",
    "url": "https://github.com/author"
  },
  "homepage": "https://docs.example.com/plugin",
  "repository": "https://github.com/author/plugin",
  "license": "MIT",
  "keywords": ["keyword1", "keyword2"],
  "skills": "./custom/skills/",
  "commands": ["./custom/commands/special.md"],
  "agents": ["./custom/agents/reviewer.md"],
  "hooks": "./config/hooks.json",
  "mcpServers": "./mcp-config.json",
  "outputStyles": "./styles/",
  "lspServers": "./.lsp.json",
  "experimental": {
    "themes": "./themes/",
    "monitors": "./monitors.json"
  },
  "dependencies": [
    "helper-lib",
    { "name": "secrets-vault", "version": "~2.1.0" }
  ]
}
```

### Campos requeridos

Si incluyes un manifiesto, `name` es el único campo requerido.

| Campo  | Tipo   | Descripción                                    | Ejemplo              |
| :----- | :----- | :--------------------------------------------- | :------------------- |
| `name` | string | Identificador único (kebab-case, sin espacios) | `"deployment-tools"` |

Este nombre se utiliza para espacios de nombres de componentes. Por ejemplo, en la interfaz de usuario, el agent `agent-creator` para el plugin con nombre `plugin-dev` aparecerá como `plugin-dev:agent-creator`.

### Campos de metadatos

| Campo         | Tipo   | Descripción                                                                                                                                                                                                                                                                                                                                                                                                          | Ejemplo                                                           |
| :------------ | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------- |
| `$schema`     | string | URL del esquema JSON para autocompletado y validación del editor. Claude Code ignora este campo en el momento de la carga.                                                                                                                                                                                                                                                                                           | `"https://json.schemastore.org/claude-code-plugin-manifest.json"` |
| `version`     | string | Opcional. Versión semántica. Establecer esto fija el plugin a esa cadena de versión, por lo que los usuarios solo reciben actualizaciones cuando la incrementas. Si se omite, Claude Code recurre al SHA del commit de git, por lo que cada commit se trata como una nueva versión. Si también se establece en la entrada del marketplace, `plugin.json` gana. Consulta [Gestión de versiones](#version-management). | `"2.1.0"`                                                         |
| `description` | string | Explicación breve del propósito del plugin                                                                                                                                                                                                                                                                                                                                                                           | `"Deployment automation tools"`                                   |
| `author`      | object | Información del autor                                                                                                                                                                                                                                                                                                                                                                                                | `{"name": "Dev Team", "email": "dev@company.com"}`                |
| `homepage`    | string | URL de documentación                                                                                                                                                                                                                                                                                                                                                                                                 | `"https://docs.example.com"`                                      |
| `repository`  | string | URL del código fuente                                                                                                                                                                                                                                                                                                                                                                                                | `"https://github.com/user/plugin"`                                |
| `license`     | string | Identificador de licencia                                                                                                                                                                                                                                                                                                                                                                                            | `"MIT"`, `"Apache-2.0"`                                           |
| `keywords`    | array  | Etiquetas de descubrimiento                                                                                                                                                                                                                                                                                                                                                                                          | `["deployment", "ci-cd"]`                                         |

### Campos de ruta de componentes

| Campo                   | Tipo                  | Descripción                                                                                                                                                                       | Ejemplo                                              |
| :---------------------- | :-------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------- |
| `skills`                | string\|array         | Directorios de skills personalizados que contienen `<name>/SKILL.md` (además del predeterminado `skills/`)                                                                        | `"./custom/skills/"`                                 |
| `commands`              | string\|array         | Archivos de skill planos `.md` o directorios personalizados (reemplaza el predeterminado `commands/`)                                                                             | `"./custom/cmd.md"` o `["./cmd1.md"]`                |
| `agents`                | string\|array         | Archivos de agent personalizados (reemplaza el predeterminado `agents/`)                                                                                                          | `"./custom/agents/reviewer.md"`                      |
| `hooks`                 | string\|array\|object | Rutas de configuración de hooks o configuración en línea                                                                                                                          | `"./my-extra-hooks.json"`                            |
| `mcpServers`            | string\|array\|object | Rutas de configuración de MCP o configuración en línea                                                                                                                            | `"./my-extra-mcp-config.json"`                       |
| `outputStyles`          | string\|array         | Archivos/directorios de estilos de salida personalizados (reemplaza el predeterminado `output-styles/`)                                                                           | `"./styles/"`                                        |
| `lspServers`            | string\|array\|object | Configuraciones de [Language Server Protocol](https://microsoft.github.io/language-server-protocol/) para inteligencia de código (ir a definición, encontrar referencias, etc.)   | `"./.lsp.json"`                                      |
| `experimental.themes`   | string\|array         | Archivos/directorios de temas de color (reemplaza el predeterminado `themes/`). Consulta [Themes](#themes)                                                                        | `"./themes/"`                                        |
| `experimental.monitors` | string\|array         | Configuraciones de [Monitor](/es/tools-reference#monitor-tool) de fondo que se inician automáticamente cuando el plugin está activo. Consulta [Monitors](#monitors)               | `"./monitors.json"`                                  |
| `userConfig`            | object                | Valores configurables por el usuario solicitados al habilitar. Consulta [Configuración del usuario](#user-configuration)                                                          | Ver abajo                                            |
| `channels`              | array                 | Declaraciones de canales para inyección de mensajes (estilo Telegram, Slack, Discord). Consulta [Channels](#channels)                                                             | Ver abajo                                            |
| `dependencies`          | array                 | Otros plugins que requiere este plugin, opcionalmente con restricciones de versión semántica. Consulta [Restringir versiones de dependencias de plugins](/es/plugin-dependencies) | `[{ "name": "secrets-vault", "version": "~2.1.0" }]` |

### Componentes experimentales

Los componentes bajo la clave `experimental`, `themes` y `monitors`, tienen un esquema de manifiesto que puede cambiar entre versiones mientras se estabilizan. Dónde los declares es una migración separada: el nivel superior aún funciona, `claude plugin validate` advierte, y una versión futura requerirá `experimental.*`.

### Configuración del usuario

El campo `userConfig` declara valores que Claude Code solicita al usuario cuando se habilita el plugin. Usa esto en lugar de requerir que los usuarios editen manualmente `settings.json`.

```json theme={null}
{
  "userConfig": {
    "api_endpoint": {
      "type": "string",
      "title": "API endpoint",
      "description": "Tu endpoint de API del equipo"
    },
    "api_token": {
      "type": "string",
      "title": "API token",
      "description": "Token de autenticación de API",
      "sensitive": true
    }
  }
}
```

Las claves deben ser identificadores válidos. Cada opción soporta estos campos:

| Campo         | Requerido | Descripción                                                                                                 |
| :------------ | :-------- | :---------------------------------------------------------------------------------------------------------- |
| `type`        | Sí        | Uno de `string`, `number`, `boolean`, `directory`, o `file`                                                 |
| `title`       | Sí        | Etiqueta mostrada en el diálogo de configuración                                                            |
| `description` | Sí        | Texto de ayuda mostrado debajo del campo                                                                    |
| `sensitive`   | No        | Si es `true`, enmascara la entrada y almacena el valor en almacenamiento seguro en lugar de `settings.json` |
| `required`    | No        | Si es `true`, la validación falla cuando el campo está vacío                                                |
| `default`     | No        | Valor utilizado cuando el usuario no proporciona nada                                                       |
| `multiple`    | No        | Para tipo `string`, permite un array de cadenas                                                             |
| `min` / `max` | No        | Límites para tipo `number`                                                                                  |

Cada valor está disponible para sustitución como `${user_config.KEY}` en configuraciones de servidores MCP y LSP, comandos de hooks y comandos de monitores. Los valores no sensibles también pueden sustituirse en contenido de skills y agents. Todos los valores se exportan a subprocesos del plugin como variables de entorno `CLAUDE_PLUGIN_OPTION_<KEY>`.

Los valores no sensibles se almacenan en `settings.json` bajo `pluginConfigs[<plugin-id>].options`. Los valores sensibles van al llavero del sistema (o `~/.claude/.credentials.json` donde el llavero no está disponible). El almacenamiento en llavero se comparte con tokens OAuth y tiene un límite total aproximado de 2 KB, así que mantén los valores sensibles pequeños.

### Canales

El campo `channels` permite que un plugin declare uno o más canales de mensajes que inyecten contenido en la conversación. Cada canal se vincula a un servidor MCP que proporciona el plugin.

```json theme={null}
{
  "channels": [
    {
      "server": "telegram",
      "userConfig": {
        "bot_token": {
          "type": "string",
          "title": "Bot token",
          "description": "Token del bot de Telegram",
          "sensitive": true
        },
        "owner_id": {
          "type": "string",
          "title": "Owner ID",
          "description": "Tu ID de usuario de Telegram"
        }
      }
    }
  ]
}
```

El campo `server` es requerido y debe coincidir con una clave en los `mcpServers` del plugin. El `userConfig` opcional por canal usa el mismo esquema que el campo de nivel superior, permitiendo que el plugin solicite tokens de bot o IDs de propietario cuando se habilita el plugin.

### Reglas de comportamiento de rutas

Si una ruta personalizada reemplaza o extiende el directorio predeterminado del plugin depende del campo:

* **Reemplaza el predeterminado**: `commands`, `agents`, `outputStyles`, `experimental.themes`, `experimental.monitors`. Por ejemplo, cuando el manifiesto especifica `commands`, el directorio predeterminado `commands/` no se escanea. Para mantener el predeterminado y añadir más, enuméralo explícitamente: `"commands": ["./commands/", "./extras/"]`
* **Se añade al predeterminado**: `skills`. El directorio predeterminado `skills/` siempre se escanea, y los directorios enumerados en `skills` se cargan junto a él
* **Reglas de fusión propias**: [hooks](#hooks), [MCP servers](#mcp-servers) y [LSP servers](#lsp-servers). Consulta cada sección para ver cómo se combinan múltiples fuentes

Cuando un plugin tiene tanto una carpeta predeterminada como la clave de manifiesto coincidente, Claude Code v2.1.140 y posterior marca la carpeta ignorada en `/doctor`, `claude plugin list` y la vista de detalles `/plugin`. El plugin aún se carga usando las rutas del manifiesto. No se muestra advertencia cuando la clave del manifiesto apunta a la carpeta predeterminada, por ejemplo `"commands": ["./commands/deploy.md"]`, porque la carpeta se aborda explícitamente en ese caso.

Para todos los campos de ruta:

* Todas las rutas deben ser relativas a la raíz del plugin y comenzar con `./`
* Los componentes de rutas personalizadas utilizan las mismas reglas de nomenclatura y espacios de nombres
* Se pueden especificar múltiples rutas como arrays
* Cuando una ruta de skill apunta a un directorio que contiene un `SKILL.md` directamente, por ejemplo `"skills": ["./"]` apuntando a la raíz del plugin, el campo frontmatter `name` en `SKILL.md` determina el nombre de invocación de la skill. Esto proporciona un nombre estable independientemente del directorio de instalación. Si `name` no se establece en el frontmatter, el nombre base del directorio se usa como alternativa.

**Ejemplos de rutas**:

```json theme={null}
{
  "commands": [
    "./specialized/deploy.md",
    "./utilities/batch-process.md"
  ],
  "agents": [
    "./custom-agents/reviewer.md",
    "./custom-agents/tester.md"
  ]
}
```

### Variables de entorno

Claude Code proporciona tres variables para hacer referencia a rutas. Todas se sustituyen en línea en cualquier lugar donde aparezcan en contenido de skills, contenido de agents, comandos de hooks, comandos de monitores y configuraciones de servidores MCP o LSP. Todas también se exportan como variables de entorno a procesos de hooks y subprocesos de servidores MCP o LSP.

**`${CLAUDE_PLUGIN_ROOT}`**: la ruta absoluta al directorio de instalación de tu plugin. Úsala para hacer referencia a scripts, binarios y archivos de configuración incluidos con el plugin. En comandos de hooks, usa [forma exec](/es/hooks#exec-form-and-shell-form) con `args` para que la ruta se pase como un argumento sin comillas. En hooks de forma shell y comandos de monitores, envuélvelo en comillas dobles, como en `"${CLAUDE_PLUGIN_ROOT}"`. Esta ruta cambia cuando se actualiza el plugin. El directorio de la versión anterior permanece en el disco durante aproximadamente siete días después de una actualización antes de la limpieza, pero trátalo como efímero y no escribas estado aquí.

Cuando un plugin se actualiza a mitad de sesión, los comandos de hooks, monitores, servidores MCP y servidores LSP siguen usando la ruta de la versión anterior. Ejecuta `/reload-plugins` para cambiar hooks, servidores MCP y servidores LSP a la nueva ruta; los monitores requieren un reinicio de sesión.

**`${CLAUDE_PLUGIN_DATA}`**: un directorio persistente para el estado del plugin que sobrevive a las actualizaciones. Úsalo para dependencias instaladas como `node_modules` o entornos virtuales de Python, código generado, cachés y cualquier otro archivo que deba persistir entre versiones del plugin. El directorio se crea automáticamente la primera vez que se hace referencia a esta variable.

**`${CLAUDE_PROJECT_DIR}`**: la raíz del proyecto. Este es el mismo directorio que los hooks reciben en su variable `CLAUDE_PROJECT_DIR`. Úsalo para hacer referencia a scripts o archivos de configuración locales del proyecto. Envuélvelo en comillas para manejar rutas con espacios, por ejemplo `"${CLAUDE_PROJECT_DIR}/scripts/server.sh"`. Los servidores MCP también pueden llamar a la solicitud MCP `roots/list`, que devuelve el directorio desde el que se lanzó Claude Code.

```json theme={null}
{
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/process.sh"
          }
        ]
      }
    ]
  }
}
```

#### Directorio de datos persistente

El directorio `${CLAUDE_PLUGIN_DATA}` se resuelve a `~/.claude/plugins/data/{id}/`, donde `{id}` es el identificador del plugin con caracteres fuera de `a-z`, `A-Z`, `0-9`, `_` y `-` reemplazados por `-`. Para un plugin instalado como `formatter@my-marketplace`, el directorio es `~/.claude/plugins/data/formatter-my-marketplace/`.

Un uso común es instalar dependencias de lenguaje una vez y reutilizarlas en sesiones y actualizaciones de plugins. Porque el directorio de datos sobrevive a cualquier versión única del plugin, una verificación de existencia de directorio solo no puede detectar cuándo una actualización cambia el manifiesto de dependencias del plugin. El patrón recomendado compara el manifiesto incluido contra una copia en el directorio de datos y reinstala cuando difieren.

Este hook `SessionStart` instala `node_modules` en la primera ejecución y nuevamente siempre que una actualización del plugin incluya un `package.json` cambiado:

```json theme={null}
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "diff -q \"${CLAUDE_PLUGIN_ROOT}/package.json\" \"${CLAUDE_PLUGIN_DATA}/package.json\" >/dev/null 2>&1 || (cd \"${CLAUDE_PLUGIN_DATA}\" && cp \"${CLAUDE_PLUGIN_ROOT}/package.json\" . && npm install) || rm -f \"${CLAUDE_PLUGIN_DATA}/package.json\""
          }
        ]
      }
    ]
  }
}
```

El `diff` sale con código distinto de cero cuando la copia almacenada falta o difiere de la incluida, cubriendo tanto la primera ejecución como las actualizaciones que cambian dependencias. Si `npm install` falla, el `rm` final elimina el manifiesto copiado para que la siguiente sesión reintente.

Los scripts incluidos en `${CLAUDE_PLUGIN_ROOT}` pueden ejecutarse contra los `node_modules` persistidos:

```json theme={null}
{
  "mcpServers": {
    "routines": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/server.js"],
      "env": {
        "NODE_PATH": "${CLAUDE_PLUGIN_DATA}/node_modules"
      }
    }
  }
}
```

El directorio de datos se elimina automáticamente cuando desinstales el plugin del último alcance donde está instalado. La interfaz `/plugin` muestra el tamaño del directorio y solicita confirmación antes de eliminar. La CLI elimina por defecto; pasa [`--keep-data`](#plugin-uninstall) para preservarlo.

***

## Almacenamiento en caché de plugins y resolución de archivos

Los plugins se especifican de una de dos formas:

* A través de `claude --plugin-dir` o `claude --plugin-url`, durante la duración de una sesión.
* A través de un marketplace, instalado para sesiones futuras.

Por razones de seguridad y verificación, Claude Code copia plugins del *marketplace* a la **caché de plugins** local del usuario (`~/.claude/plugins/cache`) en lugar de usarlos en su lugar. Entender este comportamiento es importante al desarrollar plugins que hacen referencia a archivos externos.

Cada versión instalada es un directorio separado en la caché. Cuando actualiza o desinstala un plugin, el directorio de versión anterior se marca como huérfano y se elimina automáticamente 7 días después. El período de gracia permite que las sesiones de Claude Code concurrentes que ya cargaron la versión anterior sigan ejecutándose sin errores.

Las herramientas Glob y Grep de Claude omiten directorios de versión huérfanos durante búsquedas, por lo que los resultados de archivos no incluyen código de plugin obsoleto.

### Limitaciones de traversal de rutas

Los plugins instalados no pueden hacer referencia a archivos fuera de su directorio. Las rutas que traversan fuera de la raíz del plugin (como `../shared-utils`) no funcionarán después de la instalación porque esos archivos externos no se copian a la caché.

### Compartir archivos dentro de un marketplace con enlaces simbólicos

Si su plugin necesita compartir archivos con otras partes del mismo marketplace, puede crear enlaces simbólicos dentro de su directorio de plugin. La forma en que se maneja un enlace simbólico cuando el plugin se copia en la caché depende de dónde se resuelva su destino:

* **Dentro del directorio propio del plugin:** el enlace simbólico se preserva como un enlace simbólico relativo en la caché, por lo que sigue resolviendo al destino copiado en tiempo de ejecución.
* **En otro lugar dentro del mismo marketplace:** el enlace simbólico se desreferencia. El contenido del destino se copia en la caché en su lugar. Esto permite que el directorio `skills/` de un meta-plugin se vincule a skills definidas por otros plugins en el marketplace.
* **Fuera del marketplace:** el enlace simbólico se omite por seguridad. Esto evita que los plugins extraigan archivos arbitrarios del host, como rutas del sistema, en la caché.

Para plugins instalados con `--plugin-dir` o desde una ruta local, solo se preservan los enlaces simbólicos que se resuelven dentro del directorio propio del plugin. Todos los demás se omiten.

El siguiente comando crea un enlace desde dentro de un plugin del marketplace a una skill compartida definida por un plugin hermano. En Windows, use `mklink /D` desde un símbolo del sistema elevado o habilite el Modo de desarrollador:

```bash theme={null}
ln -s ../../shared-plugin/skills/foo ./skills/foo
```

Esto proporciona flexibilidad mientras se mantienen los beneficios de seguridad del sistema de almacenamiento en caché.

***

## Estructura del directorio del plugin

### Diseño estándar del plugin

Un plugin completo sigue esta estructura:

```text theme={null}
enterprise-plugin/
├── .claude-plugin/           # Directorio de metadatos (opcional)
│   └── plugin.json             # manifiesto del plugin
├── skills/                   # Skills
│   ├── code-reviewer/
│   │   └── SKILL.md
│   └── pdf-processor/
│       ├── SKILL.md
│       └── scripts/
├── commands/                 # Skills como archivos .md planos
│   ├── status.md
│   └── logs.md
├── agents/                   # Definiciones de subagent
│   ├── security-reviewer.md
│   ├── performance-tester.md
│   └── compliance-checker.md
├── output-styles/            # Definiciones de estilo de salida
│   └── terse.md
├── themes/                   # Definiciones de tema de color
│   └── dracula.json
├── monitors/                 # Configuraciones de monitor de fondo
│   └── monitors.json
├── hooks/                    # Configuraciones de hooks
│   ├── hooks.json           # Configuración principal de hooks
│   └── security-hooks.json  # Hooks adicionales
├── bin/                      # Ejecutables del plugin añadidos a PATH
│   └── my-tool               # Invocable como comando desnudo en herramienta Bash
├── settings.json            # Configuración predeterminada para el plugin
├── .mcp.json                # Definiciones del servidor MCP
├── .lsp.json                # Configuraciones del servidor LSP
├── scripts/                 # Scripts de hooks y utilidades
│   ├── security-scan.sh
│   ├── format-code.py
│   └── deploy.js
├── LICENSE                  # Archivo de licencia
└── CHANGELOG.md             # Historial de versiones
```

<Warning>
  El directorio `.claude-plugin/` contiene el archivo `plugin.json`. Todos los otros directorios (commands/, agents/, skills/, output-styles/, themes/, monitors/, hooks/) deben estar en la raíz del plugin, no dentro de `.claude-plugin/`.
</Warning>

Un archivo `CLAUDE.md` en la raíz del plugin no se carga como contexto del proyecto. Los plugins contribuyen contexto a través de skills, agents y hooks en lugar de CLAUDE.md. Para enviar instrucciones que se carguen en el contexto de Claude, colóquelas en un [skill](#skills).

### Referencia de ubicaciones de archivos

| Componente            | Ubicación predeterminada     | Propósito                                                                                                                                                                                            |
| :-------------------- | :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Manifiesto**        | `.claude-plugin/plugin.json` | Metadatos y configuración del plugin (opcional)                                                                                                                                                      |
| **Skills**            | `skills/`                    | Skills con estructura `<name>/SKILL.md`                                                                                                                                                              |
| **Comandos**          | `commands/`                  | Skills como archivos Markdown planos. Usa `skills/` para nuevos plugins                                                                                                                              |
| **Agents**            | `agents/`                    | Archivos Markdown de Subagent                                                                                                                                                                        |
| **Estilos de salida** | `output-styles/`             | Definiciones de estilo de salida                                                                                                                                                                     |
| **Temas**             | `themes/`                    | Definiciones de tema de color                                                                                                                                                                        |
| **Hooks**             | `hooks/hooks.json`           | Configuración de hooks                                                                                                                                                                               |
| **Servidores MCP**    | `.mcp.json`                  | Definiciones del servidor MCP                                                                                                                                                                        |
| **Servidores LSP**    | `.lsp.json`                  | Configuraciones del servidor de lenguaje                                                                                                                                                             |
| **Monitores**         | `monitors/monitors.json`     | Configuraciones de monitor de fondo                                                                                                                                                                  |
| **Ejecutables**       | `bin/`                       | Ejecutables añadidos al `PATH` de la herramienta Bash. Los archivos aquí son invocables como comandos desnudos en cualquier llamada de herramienta Bash mientras el plugin está habilitado           |
| **Configuración**     | `settings.json`              | Configuración predeterminada aplicada cuando se habilita el plugin. Actualmente solo se soportan las claves [`agent`](/es/sub-agents) y [`subagentStatusLine`](/es/statusline#subagent-status-lines) |

***

## Referencia de comandos CLI

Claude Code proporciona comandos CLI para la gestión de plugins no interactiva, útil para scripting y automatización.

### plugin install

Instala un plugin desde los marketplaces disponibles.

```bash theme={null}
claude plugin install <plugin> [options]
```

**Argumentos:**

* `<plugin>`: Nombre del plugin o `plugin-name@marketplace-name` para un marketplace específico

**Opciones:**

| Opción                | Descripción                                          | Predeterminado |
| :-------------------- | :--------------------------------------------------- | :------------- |
| `-s, --scope <scope>` | Alcance de instalación: `user`, `project`, o `local` | `user`         |
| `-h, --help`          | Mostrar ayuda para el comando                        |                |

El alcance determina qué archivo de configuración se añade el plugin instalado. Por ejemplo, `--scope project` escribe en `enabledPlugins` en .claude/settings.json, haciendo que el plugin esté disponible para todos los que clonan el repositorio del proyecto.

**Ejemplos:**

```bash theme={null}
# Instalar en alcance de usuario (predeterminado)
claude plugin install formatter@my-marketplace

# Instalar en alcance de proyecto (compartido con el equipo)
claude plugin install formatter@my-marketplace --scope project

# Instalar en alcance local (ignorado por git)
claude plugin install formatter@my-marketplace --scope local
```

### plugin uninstall

Elimina un plugin instalado.

```bash theme={null}
claude plugin uninstall <plugin> [options]
```

**Argumentos:**

* `<plugin>`: Nombre del plugin o `plugin-name@marketplace-name`

**Opciones:**

| Opción                | Descripción                                                                                                                          | Predeterminado |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------- | :------------- |
| `-s, --scope <scope>` | Desinstalar del alcance: `user`, `project`, o `local`                                                                                | `user`         |
| `--keep-data`         | Preservar el directorio de datos persistente del plugin                                                                              |                |
| `--prune`             | También eliminar las dependencias instaladas automáticamente que ningún otro plugin requiere. Consulta [plugin prune](#plugin-prune) |                |
| `-y, --yes`           | Omitir la solicitud de confirmación de `--prune`. Requerido cuando stdin no es un TTY                                                |                |
| `-h, --help`          | Mostrar ayuda para el comando                                                                                                        |                |

**Alias:** `remove`, `rm`

Por defecto, desinstalar del último alcance restante también elimina el directorio `${CLAUDE_PLUGIN_DATA}` del plugin. Usa `--keep-data` para preservarlo, por ejemplo cuando reinstales después de probar una nueva versión.

### plugin prune

Elimina las dependencias de plugins instaladas automáticamente que ya no son requeridas por ningún plugin instalado. Las dependencias que Claude Code incluyó para satisfacer el campo [`dependencies`](/es/plugin-dependencies) de otro plugin se eliminan; los plugins que instalaste directamente nunca se tocan.

```bash theme={null}
claude plugin prune [options]
```

**Opciones:**

| Opción                | Descripción                                                              | Predeterminado |
| :-------------------- | :----------------------------------------------------------------------- | :------------- |
| `-s, --scope <scope>` | Limpiar en alcance: `user`, `project`, o `local`                         | `user`         |
| `--dry-run`           | Listar lo que se eliminaría sin eliminar nada                            |                |
| `-y, --yes`           | Omitir la solicitud de confirmación. Requerido cuando stdin no es un TTY |                |
| `-h, --help`          | Mostrar ayuda para el comando                                            |                |

**Alias:** `autoremove`

El comando lista las dependencias huérfanas y solicita confirmación antes de eliminarlas. Para eliminar un plugin y limpiar sus dependencias en un paso, ejecuta `claude plugin uninstall <plugin> --prune`.

<Note>
  `claude plugin prune` requiere Claude Code v2.1.121 o posterior.
</Note>

### plugin enable

Habilita un plugin deshabilitado.

```bash theme={null}
claude plugin enable <plugin> [options]
```

**Argumentos:**

* `<plugin>`: Nombre del plugin o `plugin-name@marketplace-name`

**Opciones:**

| Opción                | Descripción                                       | Predeterminado |
| :-------------------- | :------------------------------------------------ | :------------- |
| `-s, --scope <scope>` | Alcance a habilitar: `user`, `project`, o `local` | `user`         |
| `-h, --help`          | Mostrar ayuda para el comando                     |                |

### plugin disable

Deshabilita un plugin sin desinstalarlo.

```bash theme={null}
claude plugin disable <plugin> [options]
```

**Argumentos:**

* `<plugin>`: Nombre del plugin o `plugin-name@marketplace-name`

**Opciones:**

| Opción                | Descripción                                          | Predeterminado |
| :-------------------- | :--------------------------------------------------- | :------------- |
| `-s, --scope <scope>` | Alcance a deshabilitar: `user`, `project`, o `local` | `user`         |
| `-h, --help`          | Mostrar ayuda para el comando                        |                |

### plugin update

Actualiza un plugin a la versión más reciente.

```bash theme={null}
claude plugin update <plugin> [options]
```

**Argumentos:**

* `<plugin>`: Nombre del plugin o `plugin-name@marketplace-name`

**Opciones:**

| Opción                | Descripción                                                   | Predeterminado |
| :-------------------- | :------------------------------------------------------------ | :------------- |
| `-s, --scope <scope>` | Alcance a actualizar: `user`, `project`, `local`, o `managed` | `user`         |
| `-h, --help`          | Mostrar ayuda para el comando                                 |                |

***

### plugin list

Lista los plugins instalados con su versión, marketplace de origen y estado de habilitación.

```bash theme={null}
claude plugin list [options]
```

**Opciones:**

| Opción        | Descripción                                                       | Predeterminado |
| :------------ | :---------------------------------------------------------------- | :------------- |
| `--json`      | Salida como JSON                                                  |                |
| `--available` | Incluir plugins disponibles desde marketplaces. Requiere `--json` |                |
| `-h, --help`  | Mostrar ayuda para el comando                                     |                |

### plugin details

Muestra el inventario de componentes de un plugin y el costo de tokens proyectado. La salida lista todos los componentes que el plugin contribuye, agrupados como Skills (skills y comandos), Agents, Hooks, y servidores MCP, junto con una estimación de cuántos tokens añade a cada sesión.

```bash theme={null}
claude plugin details <name>
```

**Argumentos:**

* `<name>`: Nombre del plugin o `plugin-name@marketplace-name`

**Opciones:**

| Opción       | Descripción                   | Predeterminado |
| :----------- | :---------------------------- | :------------- |
| `-h, --help` | Mostrar ayuda para el comando |                |

La salida muestra dos cifras de costo para cada componente:

* **Always-on:** tokens añadidos a cada sesión por el texto de listado del plugin, como descripciones de skills, descripciones de agents, y nombres de comandos, independientemente de si algún componente se activa.
* **On-invoke:** tokens que cuesta un componente cuando se activa. Se muestra por componente, no como total del plugin, porque una sesión típica invoca solo un subconjunto de componentes.

Este ejemplo muestra cómo se ve la salida para un plugin con dos skills:

```
security-guidance 1.2.0
  Real-time security analysis for Claude Code sessions
  Source: security-guidance@claude-code-marketplace

Component inventory
  Skills (2)  scan-dependencies, review-changes
  Agents (0)
  Hooks (1)  (harness-only — no model context cost)
  MCP servers (0)

Projected token cost
  Always-on:   ~180 tok   added to every session

Per-component (rounded)
  component            always-on  on-invoke
  scan-dependencies        ~100      ~2400
  review-changes            ~80      ~1800

  On-invoke cost is paid each time a skill or agent fires.
  Token counts are estimates and may differ from actual usage.
```

El total always-on se calcula a través de la API `count_tokens` para tu modelo activo. Los números por componente se escalan proporcionalmente desde ese total. Si la API es inaccesible, el comando recurre a una estimación basada en caracteres.

### plugin tag

Crea una etiqueta de lanzamiento de git para el plugin en el directorio actual. Ejecuta desde dentro de la carpeta del plugin. Consulta [Etiquetar lanzamientos de plugins](/es/plugin-dependencies#tag-plugin-releases-for-version-resolution).

```bash theme={null}
claude plugin tag [options]
```

**Opciones:**

| Opción        | Descripción                                                                         | Predeterminado |
| :------------ | :---------------------------------------------------------------------------------- | :------------- |
| `--push`      | Enviar la etiqueta al repositorio remoto después de crearla                         |                |
| `--dry-run`   | Imprimir lo que se etiquetaría sin crear la etiqueta                                |                |
| `-f, --force` | Crear la etiqueta incluso si el árbol de trabajo está sucio o la etiqueta ya existe |                |
| `-h, --help`  | Mostrar ayuda para el comando                                                       |                |

***

## Herramientas de depuración y desarrollo

### Comandos de depuración

Usa `claude --debug` para ver detalles de carga de plugins:

Esto muestra:

* Qué plugins se están cargando
* Cualquier error en los manifiestos del plugin
* Registro de skills, agents y hooks
* Inicialización del servidor MCP

### Problemas comunes

| Problema                            | Causa                               | Solución                                                                                                                                                                       |
| :---------------------------------- | :---------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Plugin no se carga                  | `plugin.json` inválido              | Ejecuta `claude plugin validate` o `/plugin validate` para verificar `plugin.json`, frontmatter de skill/agent/comando y `hooks/hooks.json` para errores de sintaxis y esquema |
| Skills no aparecen                  | Estructura de directorio incorrecta | Asegúrate de que `skills/` o `commands/` esté en la raíz del plugin, no dentro de `.claude-plugin/`                                                                            |
| Hooks no se disparan                | Script no ejecutable                | Ejecuta `chmod +x script.sh`                                                                                                                                                   |
| MCP server falla                    | Falta `${CLAUDE_PLUGIN_ROOT}`       | Usa la variable para todas las rutas del plugin                                                                                                                                |
| Errores de ruta                     | Se utilizan rutas absolutas         | Todas las rutas deben ser relativas y comenzar con `./`                                                                                                                        |
| LSP `Executable not found in $PATH` | Servidor de lenguaje no instalado   | Instala el binario (p. ej., `npm install -g typescript-language-server typescript`)                                                                                            |

### Mensajes de error de ejemplo

**Errores de validación de manifiesto**:

* `Invalid JSON syntax: Unexpected token } in JSON at position 142`: busca comas faltantes, comas extra o cadenas sin comillas
* `Plugin has an invalid manifest file at .claude-plugin/plugin.json. Validation errors: name: Required`: falta un campo requerido
* `Plugin has a corrupt manifest file at .claude-plugin/plugin.json. JSON parse error: ...`: error de sintaxis JSON

**Errores de carga de plugin**:

* `Warning: No commands found in plugin my-plugin custom directory: ./cmds. Expected .md files or SKILL.md in subdirectories.`: la ruta del comando existe pero no contiene archivos de comando válidos
* `Plugin directory not found at path: ./plugins/my-plugin. Check that the marketplace entry has the correct path.`: la ruta `source` en marketplace.json apunta a un directorio inexistente
* `Plugin my-plugin has conflicting manifests: both plugin.json and marketplace entry specify components.`: elimina definiciones de componentes duplicadas o elimina `strict: false` en la entrada del marketplace

### Solución de problemas de hooks

**El script del hook no se ejecuta**:

1. Verifica que el script sea ejecutable: `chmod +x ./scripts/your-script.sh`
2. Verifica la línea shebang: La primera línea debe ser `#!/bin/bash` o `#!/usr/bin/env bash`
3. Verifica que la ruta use `${CLAUDE_PLUGIN_ROOT}`: `"command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/your-script.sh"`
4. Prueba el script manualmente: `./scripts/your-script.sh`

**El hook no se dispara en los eventos esperados**:

1. Verifica que el nombre del evento sea correcto (sensible a mayúsculas): `PostToolUse`, no `postToolUse`
2. Verifica que el patrón del matcher coincida con tus herramientas: `"matcher": "Write|Edit"` para operaciones de archivo
3. Confirma que el tipo de hook sea válido: `command`, `http`, `mcp_tool`, `prompt`, o `agent`

### Solución de problemas del servidor MCP

**El servidor no se inicia**:

1. Verifica que el comando exista y sea ejecutable
2. Verifica que todas las rutas usen la variable `${CLAUDE_PLUGIN_ROOT}`
3. Verifica los registros del servidor MCP: `claude --debug` muestra errores de inicialización
4. Prueba el servidor manualmente fuera de Claude Code

**Las herramientas del servidor no aparecen**:

1. Asegúrate de que el servidor esté correctamente configurado en `.mcp.json` o `plugin.json`
2. Verifica que el servidor implemente correctamente el protocolo MCP
3. Busca tiempos de espera de conexión en la salida de depuración

### Errores de estructura de directorio

**Síntomas**: El plugin se carga pero faltan componentes (skills, agents, hooks).

**Estructura correcta**: Los componentes deben estar en la raíz del plugin, no dentro de `.claude-plugin/`. Solo `plugin.json` pertenece a `.claude-plugin/`.

```text theme={null}
my-plugin/
├── .claude-plugin/
│   └── plugin.json      ← Solo el manifiesto aquí
├── commands/            ← A nivel de raíz
├── agents/              ← A nivel de raíz
└── hooks/               ← A nivel de raíz
```

Si tus componentes están dentro de `.claude-plugin/`, muévelos a la raíz del plugin.

**Lista de verificación de depuración**:

1. Ejecuta `claude --debug` y busca mensajes "loading plugin"
2. Verifica que cada directorio de componentes esté listado en la salida de depuración
3. Verifica que los permisos de archivo permitan leer los archivos del plugin

***

## Referencia de distribución y versionado

### Gestión de versiones

Claude Code utiliza la versión del plugin como clave de caché que determina si hay una actualización disponible. Cuando ejecuta `/plugin update` o se activa la actualización automática, Claude Code calcula la versión actual y omite la actualización si coincide con la que ya está instalada.

La versión se resuelve a partir de la primera de estas que esté configurada:

1. El campo `version` en el `plugin.json` del plugin
2. El campo `version` en la entrada del marketplace del plugin en `marketplace.json`
3. El SHA del commit de git del origen del plugin, para fuentes `github`, `url`, `git-subdir` y relative-path en un marketplace alojado en git
4. `unknown`, para fuentes `npm` o directorios locales que no estén dentro de un repositorio de git

Esto le proporciona dos formas de versionar un plugin:

| Enfoque                   | Cómo                                                                      | Comportamiento de actualización                                                                                                                                                        | Mejor para                                            |
| :------------------------ | :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------- |
| **Versión explícita**     | Establezca `"version": "2.1.0"` en `plugin.json`                          | Los usuarios reciben actualizaciones solo cuando aumenta este campo. Enviar nuevos commits sin aumentarlo no tiene efecto, y `/plugin update` informa "already at the latest version". | Plugins publicados con ciclos de lanzamiento estables |
| **Versión de commit-SHA** | Omita `version` tanto de `plugin.json` como de la entrada del marketplace | Los usuarios reciben actualizaciones en cada nuevo commit a la fuente de git del plugin                                                                                                | Plugins internos o de equipo en desarrollo activo     |

<Warning>
  Si establece `version` en `plugin.json`, debe aumentarlo cada vez que desee que los usuarios reciban cambios. Enviar nuevos commits por sí solo no es suficiente, porque Claude Code ve la misma cadena de versión y mantiene la copia en caché. Si está iterando rápidamente, deje `version` sin establecer para que se use el SHA del commit de git en su lugar.
</Warning>

Si utiliza versiones explícitas, siga el [versionado semántico](https://semver.org) (`MAJOR.MINOR.PATCH`): aumente MAJOR para cambios de ruptura, MINOR para nuevas características, PATCH para correcciones de errores. Documente los cambios en un `CHANGELOG.md`.

***

## Ver también

* [Plugins](/es/plugins) - Tutoriales y uso práctico
* [Marketplaces de plugins](/es/plugin-marketplaces) - Crear y gestionar marketplaces
* [Skills](/es/skills) - Detalles de desarrollo de skills
* [Subagents](/es/sub-agents) - Configuración y capacidades del agent
* [Hooks](/es/hooks) - Manejo de eventos y automatización
* [MCP](/es/mcp) - Integración de herramientas externas
* [Configuración](/es/settings) - Opciones de configuración para plugins
