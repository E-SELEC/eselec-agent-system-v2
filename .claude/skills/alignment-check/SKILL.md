---
name: alignment-check
description: Audita si un sistema Claude Code esta alineado con la documentacion oficial. Usalo para revisar CLAUDE.md, rules, skills, agents, commands, settings, hooks, MCP, contexto cargado, permisos, estructura del repo y calidad de la configuracion antes de proponer cambios.
---

# Alignment Check

## Proposito

Revisar una configuracion Claude Code sin prejuicios. La auditoria debe partir de fuentes oficiales, leer evidencia actual del repo y proponer correcciones concretas sin editar archivos.

## Recursos

Lee estos archivos cuando hagan falta:

- `references/fuentes-claude-code.md`: indice de URLs oficiales usadas como fuente.
- `references/claude-docs/manifest.md`: manifest de las paginas oficiales scrapeadas.
- `references/indice-tematico.md`: mapa de tema -> fuente oficial local.
- `references/claude-code-spec.md`: resumen operativo neutral de las reglas Claude Code.
- `checklists/sistema-completo.md`: checklist para auditoria completa.
- `checklists/observacion-sesion.md`: checklist para revisar calidad de una sesion o output.
- `templates/hallazgo.md`: formato de cada hallazgo.
- `templates/reporte-alineacion.md`: formato de reporte completo.

## Reglas

1. No tomes reportes anteriores como verdad.
2. No digas que algo esta mal solo porque existe.
3. Para cada hallazgo, cita la regla o fuente que aplica.
4. Distingue entre hecho e inferencia.
5. No propongas borrar piezas sin explicar que las reemplaza.
6. No edites archivos, no muevas carpetas y no ejecutes comandos destructivos.
7. Usa `Bash` solo para diagnostico de lectura: `git status`, `rg`, conteos, validaciones o guards.
8. No leas ni imprimas secretos.
9. Antes de hallazgos `alto` o `critico`, lee la fuente oficial local del tema segun `references/indice-tematico.md`.
10. Antes de proponer ejecutar un cambio estructural, cita la fuente oficial local que lo justifica.
11. Toda afirmacion de conteo, existencia o ausencia debe incluir el comando, Glob o Grep que la genero y el resultado observado.
12. No uses README, AGENTS.md, registros o reportes como inventario real. Sirven como declaracion; el inventario real sale del filesystem.
13. Si no verificaste una afirmacion con filesystem, marcala como `pendiente de verificacion` y no la conviertas en ajuste a ejecutar.

## Flujo de auditoria

### 1. Definir alcance

Clasifica la solicitud:

- `completa`: revisar todo el sistema.
- `profunda`: revisar todas las fuentes oficiales locales y toda la carpeta del sistema por capas.
- `focalizada`: revisar una pieza concreta.
- `posterior-a-cambio`: revisar una modificacion reciente.
- `calidad`: revisar por que una salida puede ser floja o inconsistente.

### 2. Leer fuentes base

Para auditorias completas o focalizadas, empieza con:

1. `references/indice-tematico.md`.
2. `references/claude-code-spec.md`.
3. La fuente oficial local del tema auditado.
4. `CLAUDE.md`.
5. `AGENTS.md`.
6. `.claude/settings.json`.
7. `.claude/rules/`.

Para auditorias profundas:

1. Lee `references/claude-docs/manifest.md`.
2. Lee `references/indice-tematico.md`.
3. Recorre todas las categorias oficiales por lotes.
4. Lee el sistema por capas: `CLAUDE.md`, `AGENTS.md`, `.claude/`, `core/`, `protocols/`, `quality/`, `registries/`, `planning/`, `agency/`, `clients/` y `scripts/`.
5. Si el contexto no permite todo de una vez, resume cada lote antes de seguir y declara cobertura.

Lee `references/fuentes-claude-code.md` si necesitas volver de archivo local a URL original.

### 3. Inventariar

Cuenta y cruza:

- agentes en `.claude/agents/*.md`;
- skills en `.claude/skills/*/SKILL.md`;
- commands en `.claude/commands/*.md`;
- rules en `.claude/rules/*.md`;
- hooks y permisos en `.claude/settings.json`;
- MCP en `.mcp.json` o `.mcp.example.json`.

Regla de inventario:

- Cada conteo debe mostrar `EVIDENCIA OPERATIVA`.
- Usa filesystem, no README, para probar existencia.
- Si una lista sale de un README, etiquetala como `declarado`, no como `confirmado`.
- Antes de afirmar que falta un archivo, busca por ruta exacta y por patron.

Ejemplos validos:

```text
EVIDENCIA OPERATIVA:
- Comando: Get-ChildItem -LiteralPath '.claude\skills' -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') } | Measure-Object
- Resultado: 44 skills con SKILL.md
- Alcance: .claude/skills/*/SKILL.md
```

```text
EVIDENCIA OPERATIVA:
- Patron: .claude/agents/*.md
- Resultado: 47 agentes, excluyendo README.md
- Alcance: archivos Markdown directos en .claude/agents/
```

### 4. Evaluar por primitiva

Usa estas preguntas:

- `CLAUDE.md`: contiene solo instrucciones siempre necesarias?
- Rules: se activan por tema/ruta y no duplican instrucciones?
- Skills: representan procedimientos reutilizables bajo demanda?
- Agents: necesitan contexto propio, herramientas acotadas o delegacion repetida?
- Commands: representan flujos manuales utiles o duplican skills?
- Settings: permisos y hooks reducen riesgo sin bloquear el trabajo?
- MCP: hay conectores definidos sin secretos cuando el sistema los menciona?
- Carpetas del repo: lo importante tiene mecanismo claro de carga o lectura?

### 4.1 Aplicar verificaciones automaticas

Usa estas pruebas neutrales:

- Si un agente dice `crea`, `edita`, `modifica`, `implementa`, `ejecuta` o `corrige`, revisa si sus `tools` permiten esa accion o si el cuerpo limita su rol a recomendar.
- Si un agente tiene `skills:`, confirma que cada skill existe y no usa `disable-model-invocation: true`.
- Si un agente debe aprender, calibrar o recordar, revisa `memory` o mecanismo alternativo.
- Si un agente puede trabajar en varias vueltas, revisa `maxTurns`.
- Si existe `.claude/commands/X.md` y `.claude/skills/X/SKILL.md`, revisa si hay duplicacion real y si la skill tiene prioridad.
- Si una skill menciona archivos de apoyo, confirma que existan.
- Si el sistema promete MCP o datos vivos, confirma `.mcp.json`, `.mcp.example.json`, script seguro o decision documentada.
- Si hay hook con autoprueba, ejecuta la autoprueba antes de recomendar cambios.

### 5. Clasificar hallazgos

Usa esta escala:

- `critico`: rompe o puede romper seguridad, permisos, hooks, MCP, carga de contexto, ejecucion real, secretos, datos vivos o una fuente de verdad. Ejemplo ancla: un hook de secretos no se ejecuta, un agente con permisos de escritura puede tocar produccion sin orden de cambio, o un MCP con secretos reales queda versionado.
- `alto`: la pieza promete una capacidad que no puede cumplir, causa ambiguedad operativa fuerte o puede degradar de forma probable la calidad de auditorias, ejecucion o delegacion. Ejemplo ancla: un agente dice que implementa pero solo tiene herramientas de lectura, o una skill critica no existe aunque varios agentes dependan de ella.
- `medio`: mejora clara que reduce confusion, duplicacion mantenible o friccion, pero no bloquea el uso normal ni expone datos. Ejemplo ancla: commands y skills funcionan, pero falta un mapa que explique cual es wrapper y cual es procedimiento vivo.
- `bajo`: limpieza, indice, documentacion o claridad sin impacto operativo directo. Ejemplo ancla: un README no lista una skill existente, o una descripcion podria ser mas precisa sin cambiar comportamiento.

Si dudas entre dos niveles, usa el menor y explica la condicion que lo elevaria. No uses palabras como `fuerte`, `probable` o `critico` sin evidencia operativa.

### 6. Recomendar

Ordena las acciones por seguridad:

1. Lectura e inventario.
2. Cambios reversibles.
3. Reduccion de contexto.
4. Permisos y hooks.
5. Fusion o eliminacion de piezas.
6. MCP y datos vivos.

Nunca conviertas una auditoria en ejecucion. La implementacion requiere aprobacion aparte.

## Modo observacion

Cuando el problema sea calidad, criterio o acierto de una sesion, usa `checklists/observacion-sesion.md`.

La observacion debe decir:

- que modo de trabajo se uso;
- que fuentes se leyeron;
- que agente o skill debio activarse;
- donde se rompio el flujo;
- si el ajuste corresponde a rule, skill, agent, command, settings, hook, memoria o proceso humano.
