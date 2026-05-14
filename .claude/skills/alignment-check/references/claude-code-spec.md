# Especificacion neutral Claude Code

Esta referencia resume reglas operativas de Claude Code para auditorias de alineacion. No describe problemas de E-SELEC. Los problemas se detectan leyendo el repo.

Ultima revision local: 2026-05-14.

## Principio

Claude Code funciona mejor cuando cada tipo de conocimiento vive en la primitiva correcta:

- instrucciones persistentes pequenas;
- reglas condicionales;
- skills bajo demanda;
- subagents con contexto propio;
- commands para flujos invocados;
- settings para permisos y hooks;
- MCP para herramientas externas;
- archivos de proyecto como memoria, evidencia o datos.

## CLAUDE.md

- Se carga al iniciar sesiones del proyecto.
- Debe contener lo que casi siempre importa.
- Si una seccion es larga o procedimental, probablemente pertenece a una rule o skill.
- Las importaciones con `@archivo` deben usarse con cuidado porque inyectan contexto.

## Rules

- Viven en `.claude/rules/`.
- Sirven para reglas que aplican por tema, ruta o contexto.
- No deben duplicar grandes bloques de `CLAUDE.md` o skills.
- Si una regla se vuelve un procedimiento paso a paso, conviene moverla a skill.

## Skills

- Viven en `.claude/skills/<nombre>/SKILL.md`.
- La descripcion ayuda a decidir cuando usar la skill.
- El cuerpo se carga cuando la skill se usa.
- Los archivos de apoyo deben quedar en `references/`, `templates/`, `checklists/` o `scripts/` y estar mencionados desde `SKILL.md`.
- Una skill debe representar un procedimiento, criterio o capacidad reutilizable.

## Subagents

- Viven en `.claude/agents/*.md`.
- Deben tener `name` y `description`.
- Pueden definir herramientas con `tools`.
- Si `tools` esta definido, actua como lista acotada.
- `permissionMode`, `maxTurns`, `memory`, `skills`, `model`, `effort` y `color` ayudan a controlar comportamiento.
- Un subagent se justifica cuando necesita contexto propio, herramientas acotadas o delegacion repetida.
- Si solo lee y reformatea una instruccion, podria ser skill en vez de agente.

## Commands

- Viven en `.claude/commands/`.
- Sirven para flujos invocados por slash command o por el usuario.
- Si un command y una skill resuelven exactamente el mismo flujo, hay que reportar posible duplicacion.
- No se debe borrar un command solo por existir. Primero hay que mapear su uso, equivalencia y riesgo.

## Settings

- `.claude/settings.json` controla permisos, allow/deny, hooks y entorno del proyecto.
- Modos validos observados por Claude Code actual: `default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`.
- `default` es comportamiento estandar.
- `plan` evita ejecucion y sirve para auditorias.
- `bypassPermissions` es de alto riesgo y debe justificarse muy bien.
- Los hooks deben reducir riesgo sin imprimir secretos.

## Hooks

- `PreToolUse` sirve para bloquear antes de ejecutar.
- `PostToolUse` sirve para validar despues.
- `Stop` y eventos de subagent sirven para cierre y trazabilidad.
- Un hook debe ser verificable, estable y no depender de secretos en repo.

## MCP

- `.mcp.json` define servidores MCP compartidos por el proyecto.
- No debe contener secretos reales.
- Si el sistema promete usar Notion, GSC, GA4, Ads, Drive u otros datos vivos, debe existir un mecanismo documentado: MCP, script seguro o conector externo.

## Carpetas fuera de `.claude`

- `clients/`, `agency/`, `core/`, `protocols/`, `quality/`, `planning/`, `registries/` y `scripts/` son archivos del proyecto.
- Claude puede leerlos si una regla, skill, agente o instruccion los llama.
- No se cargan automaticamente solo por existir.
- Si contienen instrucciones criticas, debe existir una ruta clara para cargarlas.

## Anti-patrones a verificar

- Instrucciones siempre cargadas que solo aplican a casos raros.
- Duplicacion entre `CLAUDE.md`, `AGENTS.md`, rules y skills.
- Agentes que prometen ejecutar pero no tienen herramientas para hacerlo.
- Skills con referencias no enlazadas.
- Commands y skills equivalentes sin razon clara.
- MCP prometido pero no configurado.
- Hooks ausentes para acciones sensibles.
- Archivos de otro sistema dentro de skills sin uso por Claude Code.
