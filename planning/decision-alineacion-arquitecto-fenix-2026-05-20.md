# Decision de alineacion - Arquitecto, Fenix y Escolta

Fecha: 2026-05-20
Responsable: Codex
Alcance: roles internos de gobierno estructural en E-SELEC v2

## Contexto

Rodrigo pidio que Codex contrastara el sistema contra el planteamiento de alineacion Claude Code y decidiera que hacer con Arquitecto, Fenix y piezas relacionadas, sin asumir que la hipotesis inicial era correcta.

No existe aqui una conversacion literal entre Codex y Claude. La decision se basa en:

- documentacion oficial Claude Code revisada;
- agente local `alineacion`;
- archivos reales del repo v2;
- registros de migracion ya existentes.

## Fuentes oficiales usadas como criterio

- https://code.claude.com/docs/es/claude-directory
- https://code.claude.com/docs/es/memory
- https://code.claude.com/docs/es/sub-agents
- https://code.claude.com/docs/es/skills
- https://code.claude.com/docs/es/hooks-guide
- https://code.claude.com/docs/es/settings

Puntos relevantes:

- `.claude/` es el lugar nativo para agents, skills, commands, rules, settings, hooks y memoria.
- `CLAUDE.md`/memoria debe ser conciso; procedimientos largos deben ir a skills o referencias bajo demanda.
- Los subagentes sirven para trabajos especializados con contexto aislado y herramientas restringidas.
- Los hooks/permisos son el lugar correcto para controles que no deben depender solo de que un agente recuerde una regla.
- Las restricciones de herramientas en subagentes son sanas para roles de gobierno.

## Evidencia local revisada

- `.claude/agents/arquitecto.md` ya existe como subagente nativo read-only.
- `.claude/agents/fenix.md` ya existe como subagente nativo read-only.
- `.claude/agents/alineacion.md` ya existe para auditar piezas contra documentacion oficial Claude Code.
- `.claude/skills/alignment-check/SKILL.md` ya existe como procedimiento de auditoria de alineacion.
- `.claude/settings.json` ya contiene permisos y hook activo de bloqueo de datos sensibles.
- `registries/registro-migracion.md` ya documenta que `agents/arquitecto/arquitecto.md` y `agents/fenix/fenix.md` fueron migrados a `.claude/agents/`.
- `planning/cierre-migracion-v2.md` ya declara que v2 es la base limpia y que el legado no debe migrarse en bloque.

## Decision ejecutiva

La decision correcta no es volver a migrar Arquitecto y Fenix.

La decision correcta es declarar que **v2 es la base activa** y que las versiones legacy de Arquitecto, Fenix, protocolos y carpetas antiguas quedan como referencia historica/migratoria, no como comportamiento activo.

## Matriz de roles

| Pieza | Ubicacion activa | Decision | Motivo |
|---|---|---|---|
| Arquitecto | `.claude/agents/arquitecto.md` | Mantener como subagente read-only | Su funcion es observar patrones, fricciones y decisiones de sistema; si edita directamente puede convertirse en otro ejecutor y contaminar gobierno con implementacion. |
| Fenix | `.claude/agents/fenix.md` | Mantener como subagente read-only | Debe diagnosticar piezas rotas/desconectadas y proponer sanacion; el agente principal ejecuta cambios con trazabilidad. |
| Alineacion | `.claude/agents/alineacion.md` + `alignment-check` | Mantener como auditor tecnico Claude Code | Es la pieza que responde "segun Claude Code"; no sustituye a Arquitecto ni Fenix. |
| Escolta | `scripts/protocol_guard.py` + hooks/settings | Tratar como guard, no como agente conversacional | Los cierres y bloqueos deben ser verificables; no dependen de personalidad o memoria. |
| Legacy Arquitecto/Fenix | sistema anterior | No optimizar como activo | Ya fueron migrados; seguir ajustandolos crea doble fuente de verdad. |

## Lo que no se debe hacer

1. No crear otra carpeta de Arquitecto o Fenix en legacy.
2. No copiar prompts largos de legacy a `CLAUDE.md`.
3. No dar herramientas de escritura a Fenix por defecto.
4. No convertir Arquitecto en observador permanente cargado siempre en contexto.
5. No borrar legacy todavia solo por parecer viejo; primero se decide politica de archivo/historico.
6. No crear canons por analogia sin pasar por `.claude/rules/canon-admision.md`.

## Ajuste al razonamiento previo

Antes de revisar v2, era razonable pensar que habia que migrar Arquitecto/Fenix hacia `.claude/agents`.

Despues de revisar evidencia local, esa conclusion queda corregida: **esa migracion ya ocurrio**. La nueva tarea no es construir, sino impedir duplicidad y cerrar criterio de uso.

## Flujo operativo recomendado

Cuando Rodrigo pregunte "segun Claude" o "sistema de alineacion":

1. Usar `alineacion`.
2. Leer fuente oficial local u online de Claude Code.
3. Probar evidencia contra filesystem.
4. Separar hecho, inferencia y recomendacion.
5. Si hay cambio estructural, pasar por Fenix.
6. Si hay patron humano/sistema, pasar por Arquitecto.
7. Si se modifican archivos, cerrar con registro y guard.

Cuando nazca, cambie o muera una pieza:

1. Arquitecto decide si el cambio tiene sentido sistemico.
2. Fenix lista dependencias y saneamiento minimo.
3. Codex/agente principal ejecuta con `apply_patch`.
4. Registros se actualizan.
5. Escolta valida cierre.

## Riesgos pendientes

- El repo raiz legacy sigue existiendo junto a v2; si alguien trabaja desde la carpeta equivocada, puede reactivar instrucciones viejas.
- `git status` de v2 muestra elementos locales no versionados o eliminados que no fueron resueltos en esta decision (`.env.example`, `.agents/`, `.claude/agent-memory/`, `.claude/settings.local.json`, `.claude/worktrees/`, `.codex/`). No se tocaron porque no forman parte directa de la decision Arquitecto/Fenix.
- Los hooks actuales bloquean datos sensibles, pero los controles de artefactos/activos criticos pueden seguir dependiendo parcialmente del guard manual. Conviene reforzarlos despues de una prueba controlada, no de golpe.

## Decision final

E-SELEC debe operar Arquitecto, Fenix, Alineacion y Escolta desde v2.

El legado se conserva solo como fuente historica o de migracion. Cualquier optimizacion futura debe hacerse en v2 y justificar por que no basta con las piezas existentes.
