# Backlog de migracion

Este backlog ordena las acciones de migracion. Cada item debe cerrarse con registro en `registries/registro-migracion.md`.

## Estados

- `pendiente`
- `en curso`
- `bloqueado`
- `hecho`

## Prioridad P0 - Seguridad y base

Decision de prioridad: empezar por P0 antes de P1. Motivo: si no blindamos secretos, artefactos, activos criticos y cierre, cualquier migracion de calidad puede arrastrar errores estructurales o riesgos de produccion.

| ID | Estado | Accion | Resultado esperado |
|---|---|---|---|
| P0-001 | hecho | Crear inventario legacy inicial | `planning/inventario-legacy.md` |
| P0-002 | pendiente | Auditar scripts con secretos historicos | lista saneamiento sin valores reales |
| P0-003 | pendiente | Migrar protocolo gestion-secretos | `protocols/gestion-secretos.md` |
| P0-004 | pendiente | Migrar protocolo control-artefactos | `protocols/control-artefactos.md` |
| P0-005 | pendiente | Migrar protocolo activos-criticos | `protocols/activos-criticos.md` |
| P0-006 | pendiente | Migrar cierre-humano | `protocols/cierre-humano.md` |
| P0-007 | pendiente | Disenar hook bloqueo secretos | `.claude/hooks/` |

## Prioridad P1 - Calidad y criterio

P1 empieza despues de completar los controles minimos P0. Motivo: la baja calidad de outputs se diagnosticara mejor cuando el sistema ya tenga fuentes, registros y permisos ordenados.

| ID | Estado | Accion | Resultado esperado |
|---|---|---|---|
| P1-001 | pendiente | Crear matriz de causas de baja calidad | `quality/diagnostico-calidad.md` |
| P1-002 | pendiente | Crear criterios de output por servicio | `quality/criterios-output.md` |
| P1-003 | pendiente | Migrar skill `client-audit` | `.claude/skills/client-audit/` |
| P1-004 | pendiente | Migrar skill `seo-audit` | `.claude/skills/seo-audit/` |
| P1-005 | pendiente | Migrar Docente como rol de aprendizaje | `.claude/agents/docente.md` o rule |

## Prioridad P2 - Operacion

| ID | Estado | Accion | Resultado esperado |
|---|---|---|---|
| P2-001 | pendiente | Crear Lider Clientes v2 | `.claude/agents/leader-clientes.md` |
| P2-002 | pendiente | Crear Lider Agencia v2 | `.claude/agents/leader-agencia.md` |
| P2-003 | pendiente | Convertir loop alertas pendientes en command | `.claude/commands/alertas-pendientes.md` |
| P2-004 | pendiente | Convertir auditoria semanal en command | `.claude/commands/auditoria-semanal.md` |
| P2-005 | pendiente | Definir cliente piloto | `planning/piloto-01.md` |

## Prioridad P3 - Migracion amplia

| ID | Estado | Accion | Resultado esperado |
|---|---|---|---|
| P3-001 | pendiente | Migrar estructura de agencia | `agency/` v2 completo |
| P3-002 | pendiente | Migrar cliente piloto | `clients/[cliente]/` |
| P3-003 | pendiente | Migrar resto de skills por uso | `.claude/skills/` |
| P3-004 | pendiente | Migrar agentes especialistas | `.claude/agents/` |
| P3-005 | pendiente | Sanear y migrar conectores | `scripts/` y `.mcp.example.json` |
