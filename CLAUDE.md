@AGENTS.md

## Claude Code

Este repositorio debe seguir la arquitectura oficial de Claude Code:

- Instrucciones persistentes pequenas en `CLAUDE.md` y `AGENTS.md`.
- Reglas modulares en `.claude/rules/`.
- Skills procedimentales en `.claude/skills/<skill>/SKILL.md`.
- Subagents nativos en `.claude/agents/*.md`.
- Comandos reutilizables en `.claude/commands/`.
- Configuracion compartida en `.claude/settings.json`.
- MCP compartido solo en `.mcp.json` cuando no incluya secretos.
- Fuentes y documentacion externa en `knowledge/`, registradas en `registries/registro-fuentes.md`.

No migrar piezas del sistema legacy por arrastre. Toda migracion debe justificar que primitiva de Claude Code corresponde usar y como se comprobara la calidad.
