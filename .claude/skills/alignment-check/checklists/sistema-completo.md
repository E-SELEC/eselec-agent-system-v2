# Checklist de auditoria completa

Usar este checklist cuando Rodrigo pida revisar el sistema completo, arquitectura Claude Code, alineacion o control interno.

## Preparacion

- [ ] Confirmar alcance: completa, focalizada, posterior-a-cambio o calidad.
- [ ] Ejecutar `git status --short`.
- [ ] No tocar archivos.
- [ ] No leer `.env`, secretos ni credenciales.
- [ ] Leer `references/claude-code-spec.md`.

## Inventario

- [ ] Contar `.claude/agents/*.md`.
- [ ] Contar `.claude/skills/*/SKILL.md`.
- [ ] Contar `.claude/commands/*.md`.
- [ ] Contar `.claude/rules/*.md`.
- [ ] Verificar `.claude/settings.json`.
- [ ] Verificar `.mcp.json` o `.mcp.example.json`.
- [ ] Listar carpetas de proyecto con instrucciones o memoria.

## CLAUDE.md y AGENTS.md

- [ ] Revisar si `CLAUDE.md` contiene solo instrucciones siempre necesarias.
- [ ] Revisar si importa archivos largos.
- [ ] Revisar si `AGENTS.md` duplica rules, skills o protocolos.
- [ ] Separar instrucciones globales de procedimientos.

## Rules

- [ ] Revisar duplicacion entre rules.
- [ ] Revisar duplicacion con `CLAUDE.md` o `AGENTS.md`.
- [ ] Revisar si falta `paths` o activacion condicional cuando aplique.

## Skills

- [ ] Revisar frontmatter `name` y `description`.
- [ ] Verificar que referencias, templates y checklists esten enlazados desde `SKILL.md`.
- [ ] Identificar skills que son demasiado largas.
- [ ] Identificar archivos de apoyo no usados.
- [ ] Comparar skills con commands para detectar duplicacion real.

## Agents

- [ ] Revisar `name` y `description`.
- [ ] Revisar `tools` contra proposito.
- [ ] Revisar `permissionMode`.
- [ ] Revisar `maxTurns`.
- [ ] Revisar `memory` cuando el agente deba aprender.
- [ ] Revisar `skills` cuando dependa de procedimientos.
- [ ] Marcar agentes que podrian ser skills solo si hay evidencia.

## Commands

- [ ] Listar commands.
- [ ] Mapear command contra skill equivalente.
- [ ] Clasificar: manual util, duplicado probable, dudoso.
- [ ] No recomendar eliminacion sin reemplazo claro.

## Settings, hooks y permisos

- [ ] Validar modo de permisos.
- [ ] Revisar allow/deny.
- [ ] Revisar hooks.
- [ ] Confirmar que hooks no imprimen secretos.
- [ ] Verificar si acciones sensibles tienen control.

## MCP y datos vivos

- [ ] Revisar si el sistema menciona herramientas externas.
- [ ] Confirmar mecanismo: MCP, script seguro o pendiente documentado.
- [ ] Verificar que no haya secretos en `.mcp.json`.

## Salida

- [ ] Cada hallazgo incluye fuente, evidencia, impacto y recomendacion.
- [ ] Separar hechos de inferencias.
- [ ] Ordenar por severidad.
- [ ] Proponer siguiente paso pequeno y seguro.
