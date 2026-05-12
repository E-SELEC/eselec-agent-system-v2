# /auditoria-semanal

Revisa el estado semanal de clientes activos y detecta bloqueos, estancamientos, mensajes pendientes y tareas sin avance.

## Uso

```text
/auditoria-semanal
/auditoria-semanal --write
```

Argumentos:

- sin argumentos: solo lectura, devuelve resumen en chat.
- `--write`: guarda un resumen en `agency/outputs/resumen-semanal-[YYYY-MM-DD].md` si el alcance esta aprobado.

## Objetivo

Dar a Rodrigo una vista de control semanal:

- que clientes estan activos;
- que clientes estan estancados;
- que mensajes siguen pendientes;
- que tareas urgentes o importantes no tienen avance reciente;
- que debe atenderse primero.

## Reglas

- No bloquear el comando por un cliente con archivos incompletos.
- No marcar tareas como hechas.
- No modificar `log.md`, `tasks.md` ni `mensajes.md`.
- No crear output salvo `--write` o peticion explicita.
- Si se crea output, aplicar `protocols/control-artefactos.md` y actualizar manifest si corresponde.
- Si aparece riesgo de produccion, acceso, Ads, web, GBP o datos vivos, marcarlo; no ejecutar.

## Lectura

1. Identifica clientes en `clients/`.
2. Excluye `_template`, `.template`, carpetas archivadas y clientes marcados como baja cuando esa informacion exista.
3. Por cada cliente, lee si existen:
   - `context.md`
   - `memory.md`
   - `log.md`
   - `mensajes.md`
   - `tasks.md`
4. Lee `agency/mensajes.md` para alertas globales.

## Detecciones

Por cliente detecta:

- fecha de ultima entrada de `log.md`;
- mas de 7 dias sin log: `estancado`;
- mas de 14 dias sin log: `urgente revisar`;
- mensajes con `ESTADO: pendiente`;
- tareas urgentes/importantes sin evidencia reciente en log;
- contradicciones entre tasks/log/mensajes;
- datos faltantes que impiden diagnostico.

## Clasificacion

Estado por cliente:

- Activo: log reciente o tareas en avance.
- Estancado: mas de 7 dias sin avance visible.
- Urgente revisar: mas de 14 dias sin avance o alerta critica.
- Parcial: archivos insuficientes para evaluar.

Prioridad:

- Urgente: cliente puede notarlo, riesgo operativo, gasto, reputacion o produccion.
- Importante: bloqueo o coste acumulativo.
- Rutinario: seguimiento sin riesgo inmediato.

## Salida en chat

```text
AUDITORIA SEMANAL
Fecha: [YYYY-MM-DD]

Resumen:
- Activos: [N]
- Estancados: [N]
- Urgente revisar: [N]
- Parciales/sin datos: [N]

Estado por cliente:
| Cliente | Ultimo log | Estado | Mensajes pendientes | Tareas criticas | Nota |
|---|---|---|---|---|---|

Alertas urgentes:
- [cliente/agencia]: [alerta] -> [accion sugerida]

Tareas atascadas:
- [cliente]: [tarea] -> [motivo]

Incidencias de datos:
- [cliente]: [archivo ausente / formato / contradiccion]

Recomendacion semanal:
1. [accion principal]
2. [accion secundaria]
3. [accion opcional]
```

## Escritura opcional

Si se usa `--write`, crea:

```text
agency/outputs/resumen-semanal-[YYYY-MM-DD].md
```

El archivo debe contener el mismo resumen del chat con mas detalle solo si hace falta.

No crear PDF, DOCX ni archivos pesados.

## Criterio de exito

El command funciona si Rodrigo puede entender en menos de 3 minutos:

- que clientes requieren atencion;
- que esta bloqueado;
- que alerta es prioritaria;
- que siguiente accion conviene hacer primero.

