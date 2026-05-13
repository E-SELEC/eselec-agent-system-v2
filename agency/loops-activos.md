# Loops Activos - E-SELEC v2

## Estado

- Fecha de migracion v2: 2026-05-12
- Fuente legacy: `agency/loops-activos.md`
- Estado general: pendientes de convertir a commands, scheduled tasks o automations segun riesgo

## Loops heredados

| Loop legacy | Frecuencia | Estado v2 | Destino recomendado |
|---|---|---|---|
| `auditoria-semanal` | semanal | convertido parcialmente | `.claude/commands/auditoria-semanal.md` |
| `alertas-pendientes` | semanal | convertido parcialmente | `.claude/commands/alertas-pendientes.md` |
| `informe-mensual` | mensual | pendiente | command + skill reports |
| `meta-ads-semanal` | semanal | pendiente | despues de sanear Meta Ads |
| `arquitecto-diario` | cierre de jornada | pendiente | command o heartbeat interno |
| `arquitecto-semanal` | semanal | pendiente | command de revision sistema |

## Historial de ejecucion v2

| Fecha | Loop | Modo | Resultado |
|---|---|---|---|
| 2026-05-13 | `auditoria-semanal` | lectura con output interno | O1-003 ejecutado; resumen en `agency/outputs/resumen-semanal-2026-05-13.md`. |

## Reglas v2

- No automatizar un loop hasta que su command funcione manualmente.
- No ejecutar loops con fuentes vivas sin `ingesta-evidencia` y `verificacion-medicion`.
- No crear cron/scheduled task para Ads, GBP, WordPress o datos sensibles sin Orden de Cambio.
- Registrar cada ejecucion en log o manifest correspondiente.

## Prioridad de conversion

1. `informe-mensual`: depende de reports + medicion.
2. `meta-ads-semanal`: depende de conector Meta saneado.
3. `arquitecto-diario`: depende de definir output util y no ruidoso.
4. `arquitecto-semanal`: despues de tener mas piezas v2 migradas.
