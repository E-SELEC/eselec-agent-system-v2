---
source_url: https://code.claude.com/docs/es/agent-sdk/plugins
fetched_url: https://code.claude.com/docs/es/agent-sdk/plugins.md
category: SDK de Agente
status: 200
scraped_at: 2026-05-15T14:28:37+00:00
sha256_16: 82a2468ba0a4b3b0
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugins en el SDK

> Cargue plugins personalizados para extender Claude Code con comandos, agentes, skills y hooks a través del Agent SDK

Los plugins le permiten extender Claude Code con funcionalidad personalizada que se puede compartir entre proyectos. A través del Agent SDK, puede cargar programáticamente plugins desde directorios locales para agregar comandos slash personalizados, agentes, skills, hooks y servidores MCP a sus sesiones de agente.

## ¿Qué son los plugins?

Los plugins son paquetes de extensiones de Claude Code que pueden incluir:

* **Skills**: Capacidades invocadas por el modelo que Claude utiliza de forma autónoma (también se pueden invocar con `/skill-name`)
* **Agents**: Subagentes especializados para tareas específicas
* **Hooks**: Controladores de eventos que responden al uso de herramientas y otros eventos
* **MCP servers**: Integraciones de herramientas externas a través del Model Context Protocol

<Note>
  El directorio `commands/` es un formato heredado. Use `skills/` para nuevos plugins. Claude Code continúa admitiendo ambos formatos para compatibilidad hacia atrás.
</Note>

Para obtener información completa sobre la estructura de plugins y cómo crear plugins, consulte [Plugins](/es/plugins).

## Cargando plugins

Cargue plugins proporcionando sus rutas del sistema de archivos local en su configuración de opciones. El campo `type` debe ser `"local"`, el único valor que acepta el SDK. Para usar un plugin distribuido a través de un [marketplace](/es/plugin-marketplaces) o repositorio remoto, descárguelo primero y proporcione la ruta del directorio local. El SDK admite cargar múltiples plugins desde diferentes ubicaciones.

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  for await (const message of query({
    prompt: "Hello",
    options: {
      plugins: [
        { type: "local", path: "./my-plugin" },
        { type: "local", path: "/absolute/path/to/another-plugin" }
      ]
    }
  })) {
    // Plugin commands, agents, and other features are now available
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query


  async def main():
      async for message in query(
          prompt="Hello",
          options={
              "plugins": [
                  {"type": "local", "path": "./my-plugin"},
                  {"type": "local", "path": "/absolute/path/to/another-plugin"},
              ]
          },
      ):
          # Plugin commands, agents, and other features are now available
          pass


  asyncio.run(main())
  ```
</CodeGroup>

### Especificaciones de ruta

Las rutas de plugins pueden ser:

* **Rutas relativas**: Se resuelven en relación con su directorio de trabajo actual (por ejemplo, `"./plugins/my-plugin"`)
* **Rutas absolutas**: Rutas completas del sistema de archivos (por ejemplo, `"/home/user/plugins/my-plugin"`)

<Note>
  La ruta debe apuntar al directorio raíz del plugin (el directorio que contiene `.claude-plugin/plugin.json`).
</Note>

## Verificando la instalación del plugin

Cuando los plugins se cargan correctamente, aparecen en el mensaje de inicialización del sistema. Puede verificar que sus plugins estén disponibles:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  for await (const message of query({
    prompt: "Hello",
    options: {
      plugins: [{ type: "local", path: "./my-plugin" }]
    }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      // Check loaded plugins
      console.log("Plugins:", message.plugins);
      // Example: [{ name: "my-plugin", path: "./my-plugin" }]

      // Check available commands from plugins
      console.log("Commands:", message.slash_commands);
      // Example: ["/help", "/compact", "my-plugin:custom-command"]
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query


  async def main():
      async for message in query(
          prompt="Hello", options={"plugins": [{"type": "local", "path": "./my-plugin"}]}
      ):
          if message.type == "system" and message.subtype == "init":
              # Check loaded plugins
              print("Plugins:", message.data.get("plugins"))
              # Example: [{"name": "my-plugin", "path": "./my-plugin"}]

              # Check available commands from plugins
              print("Commands:", message.data.get("slash_commands"))
              # Example: ["/help", "/compact", "my-plugin:custom-command"]


  asyncio.run(main())
  ```
</CodeGroup>

## Usando skills de plugins

Los skills de los plugins se espacian automáticamente con el nombre del plugin para evitar conflictos. Cuando se invocan como comandos slash, el formato es `plugin-name:skill-name`.

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  // Load a plugin with a custom /greet skill
  for await (const message of query({
    prompt: "/my-plugin:greet", // Use plugin skill with namespace
    options: {
      plugins: [{ type: "local", path: "./my-plugin" }]
    }
  })) {
    // Claude executes the custom greeting skill from the plugin
    if (message.type === "assistant") {
      console.log(message.message.content);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, AssistantMessage, TextBlock


  async def main():
      # Load a plugin with a custom /greet skill
      async for message in query(
          prompt="/demo-plugin:greet",  # Use plugin skill with namespace
          options={"plugins": [{"type": "local", "path": "./plugins/demo-plugin"}]},
      ):
          # Claude executes the custom greeting skill from the plugin
          if isinstance(message, AssistantMessage):
              for block in message.content:
                  if isinstance(block, TextBlock):
                      print(f"Claude: {block.text}")


  asyncio.run(main())
  ```
</CodeGroup>

<Note>
  Si instaló un plugin a través de la CLI (por ejemplo, `/plugin install my-plugin@marketplace`), aún puede usarlo en el SDK proporcionando su ruta de instalación. Verifique `~/.claude/plugins/` para plugins instalados por CLI.
</Note>

## Ejemplo completo

Aquí hay un ejemplo completo que demuestra la carga y el uso de plugins:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";
  import * as path from "path";

  async function runWithPlugin() {
    const pluginPath = path.join(__dirname, "plugins", "my-plugin");

    console.log("Loading plugin from:", pluginPath);

    for await (const message of query({
      prompt: "What custom commands do you have available?",
      options: {
        plugins: [{ type: "local", path: pluginPath }],
        maxTurns: 3
      }
    })) {
      if (message.type === "system" && message.subtype === "init") {
        console.log("Loaded plugins:", message.plugins);
        console.log("Available commands:", message.slash_commands);
      }

      if (message.type === "assistant") {
        console.log("Assistant:", message.message.content);
      }
    }
  }

  runWithPlugin().catch(console.error);
  ```

  ```python Python theme={null}
  #!/usr/bin/env python3
  """Example demonstrating how to use plugins with the Agent SDK."""

  from pathlib import Path
  import anyio
  from claude_agent_sdk import (
      AssistantMessage,
      ClaudeAgentOptions,
      TextBlock,
      query,
  )


  async def run_with_plugin():
      """Example using a custom plugin."""
      plugin_path = Path(__file__).parent / "plugins" / "demo-plugin"

      print(f"Loading plugin from: {plugin_path}")

      options = ClaudeAgentOptions(
          plugins=[{"type": "local", "path": str(plugin_path)}],
          max_turns=3,
      )

      async for message in query(
          prompt="What custom commands do you have available?", options=options
      ):
          if message.type == "system" and message.subtype == "init":
              print(f"Loaded plugins: {message.data.get('plugins')}")
              print(f"Available commands: {message.data.get('slash_commands')}")

          if isinstance(message, AssistantMessage):
              for block in message.content:
                  if isinstance(block, TextBlock):
                      print(f"Assistant: {block.text}")


  if __name__ == "__main__":
      anyio.run(run_with_plugin)
  ```
</CodeGroup>

## Referencia de estructura de plugin

Un directorio de plugin debe contener un archivo de manifiesto `.claude-plugin/plugin.json`. Opcionalmente puede incluir:

```text theme={null}
my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Required: plugin manifest
├── skills/                   # Agent Skills (invoked autonomously or via /skill-name)
│   └── my-skill/
│       └── SKILL.md
├── commands/                 # Legacy: use skills/ instead
│   └── custom-cmd.md
├── agents/                   # Custom agents
│   └── specialist.md
├── hooks/                    # Event handlers
│   └── hooks.json
└── .mcp.json                # MCP server definitions
```

Para obtener información detallada sobre cómo crear plugins, consulte:

* [Plugins](/es/plugins) - Guía completa de desarrollo de plugins
* [Plugins reference](/es/plugins-reference) - Especificaciones técnicas y esquemas

## Casos de uso comunes

### Desarrollo y pruebas

Cargue plugins durante el desarrollo sin instalarlos globalmente:

```typescript theme={null}
plugins: [{ type: "local", path: "./dev-plugins/my-plugin" }];
```

### Extensiones específicas del proyecto

Incluya plugins en su repositorio de proyecto para consistencia en todo el equipo:

```typescript theme={null}
plugins: [{ type: "local", path: "./project-plugins/team-workflows" }];
```

### Múltiples fuentes de plugins

Combine plugins de diferentes ubicaciones:

```typescript theme={null}
plugins: [
  { type: "local", path: "./local-plugin" },
  { type: "local", path: "~/.claude/custom-plugins/shared-plugin" }
];
```

## Troubleshooting

### Plugin no se carga

Si su plugin no aparece en el mensaje de inicialización:

1. **Verifique la ruta**: Asegúrese de que la ruta apunte al directorio raíz del plugin (que contiene `.claude-plugin/`)
2. **Valide plugin.json**: Asegúrese de que su archivo de manifiesto tenga una sintaxis JSON válida
3. **Verifique los permisos de archivo**: Asegúrese de que el directorio del plugin sea legible

### Los skills no aparecen

Si los skills del plugin no funcionan:

1. **Use el espacio de nombres**: Los skills del plugin requieren el formato `plugin-name:skill-name` cuando se invocan como comandos slash
2. **Verifique el mensaje de inicialización**: Verifique que el skill aparezca en `slash_commands` con el espacio de nombres correcto
3. **Valide los archivos de skill**: Asegúrese de que cada skill tenga un archivo `SKILL.md` en su propio subdirectorio bajo `skills/` (por ejemplo, `skills/my-skill/SKILL.md`)

### Problemas de resolución de ruta

Si las rutas relativas no funcionan:

1. **Verifique el directorio de trabajo**: Las rutas relativas se resuelven desde su directorio de trabajo actual
2. **Use rutas absolutas**: Para mayor confiabilidad, considere usar rutas absolutas
3. **Normalice las rutas**: Use utilidades de ruta para construir rutas correctamente

## Ver también

* [Plugins](/es/plugins) - Guía completa de desarrollo de plugins
* [Plugins reference](/es/plugins-reference) - Especificaciones técnicas
* [Slash Commands](/es/agent-sdk/slash-commands) - Usando comandos slash en el SDK
* [Subagents](/es/agent-sdk/subagents) - Trabajando con agentes especializados
* [Skills](/es/agent-sdk/skills) - Usando Agent Skills
