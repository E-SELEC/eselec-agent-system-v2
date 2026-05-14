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
- `references/claude-code-spec.md`: resumen operativo neutral de las reglas Claude Code.
- `checklists/sistema-completo.md`: checklist para auditoria completa.
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

## Flujo de auditoria

### 1. Definir alcance

Clasifica la solicitud:

- `completa`: revisar todo el sistema.
- `focalizada`: revisar una pieza concreta.
- `posterior-a-cambio`: revisar una modificacion reciente.
- `calidad`: revisar por que una salida puede ser floja o inconsistente.

### 2. Leer fuentes base

Para auditorias completas, empieza con:

1. `references/claude-code-spec.md`.
2. `CLAUDE.md`.
3. `AGENTS.md`.
4. `.claude/settings.json`.
5. `.claude/rules/`.

Lee `references/fuentes-claude-code.md` si necesitas justificar de donde sale una regla.

### 3. Inventariar

Cuenta y cruza:

- agentes en `.claude/agents/*.md`;
- skills en `.claude/skills/*/SKILL.md`;
- commands en `.claude/commands/*.md`;
- rules en `.claude/rules/*.md`;
- hooks y permisos en `.claude/settings.json`;
- MCP en `.mcp.json` o `.mcp.example.json`.

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

### 5. Clasificar hallazgos

Usa esta escala:

- `critico`: la pieza promete una capacidad que no puede cumplir, o crea riesgo sensible.
- `alto`: causa confusion, duplicacion fuerte, mala carga de contexto o baja calidad probable.
- `medio`: mejora clara, pero no bloquea el uso normal.
- `bajo`: limpieza o mantenimiento.

### 6. Recomendar

Ordena las acciones por seguridad:

1. Lectura e inventario.
2. Cambios reversibles.
3. Reduccion de contexto.
4. Permisos y hooks.
5. Fusion o eliminacion de piezas.
6. MCP y datos vivos.

Nunca conviertas una auditoria en ejecucion. La implementacion requiere aprobacion aparte.
