# Indice tematico Claude Code

Este indice le dice al agente `alineacion` que fuente oficial local debe leer segun el tipo de pieza que esta auditando.

La biblioteca local vive en `references/claude-docs/` y se genera desde las URLs oficiales listadas en `fuentes-claude-code.md`.

## Regla central

Antes de emitir un hallazgo `alto` o `critico`, lee la fuente oficial local del tema. Si no puedes leerla, marca el hallazgo como `pendiente de verificacion oficial`.

Antes de ejecutar o pedir ejecutar un cambio estructural, el plan debe citar la fuente oficial local que lo justifica.

## Auditoria profunda

Cuando Rodrigo pida una auditoria profunda del sistema:

1. Leer `references/claude-docs/manifest.md`.
2. Leer `references/claude-code-spec.md`.
3. Revisar todas las categorias oficiales del manifest.
4. Leer el repo completo por capas: `CLAUDE.md`, `AGENTS.md`, `.claude/`, `core/`, `protocols/`, `quality/`, `registries/`, `planning/`, `agency/`, `clients/` y `scripts/`.
5. No recomendar cambios estructurales hasta haber cruzado docs oficiales locales con evidencia actual del repo.

Si la documentacion completa no cabe en contexto, trabajar por lotes tematicos y declarar que lotes se leyeron antes de cerrar.

## Mapa por tema

### Instrucciones persistentes y contexto

Usar cuando se revise:

- `CLAUDE.md`
- `AGENTS.md`
- instrucciones globales
- importaciones `@archivo`
- exceso de contexto
- memoria del proyecto

Fuentes locales:

- `claude-docs/es/claude-directory.md`
- `claude-docs/es/memory.md`
- `claude-docs/es/context-window.md`
- `claude-docs/es/best-practices.md`
- `claude-docs/es/how-claude-code-works.md`

### Rules

Usar cuando se revise:

- `.claude/rules/`
- reglas por ruta o tema
- duplicacion con `CLAUDE.md`, `AGENTS.md` o skills

Fuentes locales:

- `claude-docs/es/claude-directory.md`
- `claude-docs/es/settings.md`
- `claude-docs/es/best-practices.md`

### Skills

Usar cuando se revise:

- `.claude/skills/`
- `SKILL.md`
- `description`
- `when_to_use`
- `disable-model-invocation`
- `user-invocable`
- `allowed-tools`
- `context: fork`
- `skillOverrides`
- presupuesto de listado de skills
- archivos `references/`, `templates/`, `checklists/`, `scripts/`

Fuentes locales:

- `claude-docs/es/skills.md`
- `claude-docs/es/commands.md`
- `claude-docs/es/settings.md`
- `claude-docs/es/tools-reference.md`

### Commands

Usar cuando se revise:

- `.claude/commands/`
- slash commands
- duplicacion command/skill
- comandos manuales de Rodrigo

Fuentes locales:

- `claude-docs/es/commands.md`
- `claude-docs/es/skills.md`
- `claude-docs/es/cli-reference.md`
- `claude-docs/es/interactive-mode.md`

### Subagents y equipos de agentes

Usar cuando se revise:

- `.claude/agents/`
- `tools`
- `disallowedTools`
- `model`
- `permissionMode`
- `mcpServers`
- `hooks`
- `maxTurns`
- `skills`
- `memory`
- `background`
- `isolation`
- `color`
- agentes que prometen escribir, crear, editar, implementar, ejecutar o auditar

Fuentes locales:

- `claude-docs/es/sub-agents.md`
- `claude-docs/es/agents.md`
- `claude-docs/es/agent-view.md`
- `claude-docs/es/agent-teams.md`
- `claude-docs/es/worktrees.md`
- `claude-docs/es/tools-reference.md`

### Permisos, settings y seguridad

Usar cuando se revise:

- `.claude/settings.json`
- `permissions`
- `allow`
- `deny`
- `defaultMode`
- `acceptEdits`
- `plan`
- `auto`
- `dontAsk`
- `bypassPermissions`
- sandboxing
- acceso a archivos sensibles

Fuentes locales:

- `claude-docs/es/settings.md`
- `claude-docs/es/permissions.md`
- `claude-docs/es/permission-modes.md`
- `claude-docs/es/sandboxing.md`
- `claude-docs/es/security.md`
- `claude-docs/es/tools-reference.md`

### Hooks

Usar cuando se revise:

- `PreToolUse`
- `PostToolUse`
- `Stop`
- `SubagentStart`
- `SubagentStop`
- hooks en `settings.json`
- hooks en frontmatter de agentes
- guards de seguridad o calidad

Fuentes locales:

- `claude-docs/es/hooks.md`
- `claude-docs/es/hooks-guide.md`
- `claude-docs/es/settings.md`
- `claude-docs/es/sub-agents.md`

### MCP y conectores

Usar cuando se revise:

- `.mcp.json`
- `.mcp.example.json`
- servidores MCP
- Notion, Drive, Gmail, GSC, GA4, Ads, Slack u otros datos vivos
- conectores con secretos
- herramientas externas mencionadas por agents o skills

Fuentes locales:

- `claude-docs/es/mcp.md`
- `claude-docs/es/settings.md`
- `claude-docs/es/third-party-integrations.md`
- `claude-docs/es/network-config.md`
- `claude-docs/es/security.md`

### Ejecucion, CLI y automatizacion

Usar cuando se revise:

- `headless`
- scheduled tasks
- channels
- deep links
- comandos CLI
- automatizaciones
- tareas recurrentes

Fuentes locales:

- `claude-docs/es/headless.md`
- `claude-docs/es/scheduled-tasks.md`
- `claude-docs/es/channels.md`
- `claude-docs/es/deep-links.md`
- `claude-docs/es/cli-reference.md`
- `claude-docs/es/env-vars.md`

### SDK de Agente

Usar cuando se revise:

- uso programatico de agentes
- Agent SDK Python o TypeScript
- sesiones
- permisos del SDK
- custom tools
- streaming
- hosting

Fuentes locales:

- `claude-docs/es/agent-sdk/overview.md`
- `claude-docs/es/agent-sdk/agent-loop.md`
- `claude-docs/es/agent-sdk/sessions.md`
- `claude-docs/es/agent-sdk/permissions.md`
- `claude-docs/es/agent-sdk/mcp.md`
- `claude-docs/es/agent-sdk/custom-tools.md`
- `claude-docs/es/agent-sdk/python.md`
- `claude-docs/es/agent-sdk/typescript.md`

### Diagnostico, errores y depuracion

Usar cuando se revise:

- `/doctor`
- errores de configuracion
- troubleshooting
- debug config
- settings invalidos

Fuentes locales:

- `claude-docs/es/troubleshooting.md`
- `claude-docs/es/troubleshoot-install.md`
- `claude-docs/es/debug-your-config.md`
- `claude-docs/es/errors.md`
- `claude-docs/es/settings.md`

## Verificaciones automaticas recomendadas

Estas reglas no son conclusiones sobre E-SELEC. Son pruebas neutrales que el agente debe aplicar al repo actual.

- Si un agente usa palabras como `crea`, `edita`, `modifica`, `implementa`, `ejecuta` o `corrige`, revisar que sus `tools` permitan esa accion o que el cuerpo diga claramente que solo recomienda.
- Si un agente tiene `skills:` en frontmatter, confirmar que cada skill exista y no tenga `disable-model-invocation: true`.
- Si un agente promete aprender o calibrar, revisar si `memory` esta definido o si existe otro mecanismo de memoria.
- Si un agente puede correr mucho trabajo, revisar `maxTurns`.
- Si existe `.claude/commands/X.md` y `.claude/skills/X/SKILL.md`, marcar posible duplicacion y revisar si hay razon para conservar ambos.
- Si un `SKILL.md` menciona archivos de apoyo, verificar que existan.
- Si una carpeta fuera de `.claude/` contiene instrucciones criticas, verificar que alguna rule, skill, agent o `CLAUDE.md` indique cuando leerla.
- Si el sistema menciona MCP o datos vivos, verificar `.mcp.json`, `.mcp.example.json` o documentacion de conector seguro.
- Si se revisa un hook, ejecutar su autoprueba cuando exista antes de recomendar cambios.
