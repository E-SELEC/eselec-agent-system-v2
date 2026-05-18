# Manifest outputs - Stramondo Venezuela

## Estado

- Fecha de migracion minima: 2026-05-18
- Fuente legacy: `../clients/stramondo-venezuela/`
- Politica: no se migran outputs historicos completos al repo v2.

## Archivos migrados

| Archivo | Uso | Estado |
|---|---|---|
| `context.md` | Perfil operativo del cliente | Migrado desde legacy |
| `memory.md` | Aprendizajes acumulados del cliente | Migrado desde legacy |
| `log.md` | Historial de trabajo ejecutado | Migrado desde legacy |
| `mensajes.md` | Alertas y dependencias entre agentes | Migrado desde legacy |
| `tasks.md` | Snapshot de tareas activas | Migrado desde legacy |

## Outputs legacy

No se copiaron outputs historicos.

Si un output legacy es necesario para una tarea v2:

1. leerlo desde legacy;
2. extraer solo el resumen necesario;
3. no copiar secretos, exports brutos ni archivos pesados;
4. registrar cualquier output nuevo aqui.

## Nota sensible

El cliente depende de Meta Ads y tokens externos. Los archivos migrados contienen
estado operativo y metadatos de cuenta, pero no valores de token.

## Riesgo

Medio por presupuesto publicitario y accesos Meta Ads; la migracion actual no
toca campanas, conectores ni produccion.
