# /alertas-pendientes

Consolida mensajes pendientes de clientes y agencia.

## Uso

```text
/alertas-pendientes
/alertas-pendientes --write
```

Argumentos:

- sin argumentos: solo lectura, devuelve consolidado en chat.
- `--write`: ademas de devolver el consolidado, propone o escribe una entrada en `agency/mensajes.md` si el alcance esta aprobado.

## Objetivo

Detectar mensajes con `ESTADO: pendiente` para que Rodrigo vea que requiere atencion sin revisar cada carpeta.

## Reglas

- No bloquear si un cliente no tiene `mensajes.md`; registrar incidencia y continuar.
- No duplicar alertas ya consolidadas en `agency/mensajes.md`.
- No marcar mensajes como ejecutados.
- No modificar archivos salvo que el comando incluya `--write` o Rodrigo lo pida explicitamente.
- Si se modifica `agency/mensajes.md`, aplicar `protocols/control-artefactos.md`.
- Si una alerta implica produccion, accesos o datos vivos, aplicar `protocols/activos-criticos.md` y `protocols/gestion-accesos.md`.

## Lectura

1. Identifica clientes en `clients/`.
2. Excluye carpetas `_template`, `.template`, archivadas u obvias de plantilla.
3. Para cada cliente activo, lee `clients/[cliente]/mensajes.md` si existe.
4. Lee `agency/mensajes.md`.
5. Extrae bloques o lineas con:
   - `ESTADO: pendiente`
   - `[pendiente]`
   - mensajes sin marca clara de `ejecutado`, si el formato legacy lo permite.

## Clasificacion

Clasifica cada alerta:

- Urgente: cliente puede notarlo, afecta produccion, Ads, web, reputacion, acceso o dinero.
- Importante: tiene coste acumulativo o bloquea trabajo.
- Rutinaria: informacion o seguimiento sin riesgo inmediato.

## Salida en chat

Usa este formato:

```text
ALERTAS PENDIENTES
Fecha: [YYYY-MM-DD]

Resumen:
- Urgentes: [N]
- Importantes: [N]
- Rutinarias: [N]
- Clientes con incidencias de lectura: [N]

Urgentes:
- [cliente/agencia] [origen -> destino] [mensaje resumido] [accion sugerida]

Importantes:
- ...

Rutinarias:
- ...

Incidencias:
- [cliente]: [archivo ausente / formato no reconocido / vacio]

Siguiente paso recomendado:
[una accion concreta]
```

## Escritura opcional

Si se usa `--write`, añade una sola entrada al final de `agency/mensajes.md`:

```text
---
[CONSOLIDADO COMMAND: alertas-pendientes - YYYY-MM-DD]

DE: Command Alertas Pendientes
PARA: Lider Agencia / Rodrigo
TIPO: alerta
FECHA: YYYY-MM-DD
ESTADO: pendiente
MENSAJE: Se detectaron [N] mensajes pendientes.
DETALLE:
- [cliente/agencia]: [resumen]
ACCION SUGERIDA: [accion]
---
```

Si no hay alertas nuevas:

```text
---
[CONSOLIDADO COMMAND: alertas-pendientes - YYYY-MM-DD]

DE: Command Alertas Pendientes
PARA: Lider Agencia / Rodrigo
TIPO: info
FECHA: YYYY-MM-DD
ESTADO: ejecutado
MENSAJE: 0 mensajes pendientes nuevos detectados.
ACCION SUGERIDA: Sin accion.
---
```

## Criterio de exito

El comando funciona si Rodrigo puede leer el consolidado en menos de 3 minutos y saber:

- que alerta atender primero;
- que cliente o area esta afectado;
- que accion sugiere el sistema;
- si hay archivos ausentes o formatos que corregir.

