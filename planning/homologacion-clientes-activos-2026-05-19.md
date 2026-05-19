# Homologacion de clientes activos v2 - 2026-05-19

## Objetivo

Comprobar que los clientes activos migrados a `clients/` pueden trabajarse con Claude Code sin arrastrar caos del sistema legacy ni mezclar datos reales dentro de instrucciones generales.

## Regla de trabajo

No se reescriben carpetas completas por estetica. Solo se ajusta lo necesario para que cada cliente tenga:

- contexto suficiente;
- memoria operativa;
- historial de acciones;
- mensajes pendientes;
- tareas actuales;
- manifest de outputs;
- proxima prioridad unica.

## Checklist general

| Cliente | Estado v2 | Homologacion | Proxima prioridad |
|---|---|---|---|
| `computer-chamberi` | activo v2 | hecha 2026-05-19 | verificar medicion y linea base SEO/tecnica |
| `cashier-bubble-tea` | activo v2 | hecha 2026-05-19 | confirmar envio del informe y preparar propuesta Ano 3 |
| `la-bottega-del-gusto` | activo v2 | hecha 2026-05-19 | cerrar bloqueadores de go-live con Orden de Cambio |
| `stramondo-venezuela` | activo v2 | hecha 2026-05-19 | validar estado actual Meta Ads y calidad real de leads |
| `shogun-motors` | historico/inactivo | no aplica | fuera de loops, informes y tareas |

## Computer Chamberi

### Fuentes revisadas

- `clients/computer-chamberi/context.md`
- `clients/computer-chamberi/memory.md`
- `clients/computer-chamberi/log.md`
- `clients/computer-chamberi/mensajes.md`
- `clients/computer-chamberi/tasks.md`
- `clients/computer-chamberi/outputs/manifest.md`
- `clients/computer-chamberi/outputs/auditoria-arranque-v2-2026-05-13.md`
- `clients/computer-chamberi/outputs/evidencia-seo-2026-05-12.md`

### Decision

El cliente esta suficientemente homologado para operar en v2 en modo lectura y diagnostico parcial fuerte.

No se reescribio `context.md` porque ya esta saneado y util. La accion correcta fue crear un output breve de homologacion, actualizar manifest/log y marcar `client-audit v2` como cubierto.

### Bloqueo vigente

No ejecutar auditoria SEO final, CRO ni informes hasta verificar medicion y fuentes vivas o declarar explicitamente que el output es parcial.

## Chashier Bubble Tea

### Fuentes revisadas

- `clients/cashier-bubble-tea/context.md`
- `clients/cashier-bubble-tea/memory.md`
- `clients/cashier-bubble-tea/log.md`
- `clients/cashier-bubble-tea/mensajes.md`
- `clients/cashier-bubble-tea/tasks.md`
- `clients/cashier-bubble-tea/outputs/manifest.md`

### Decision

El cliente tiene estructura v2 completa, pero `tasks.md` estaba desactualizado frente al log.

No se reescribio `context.md` ni se borraron mensajes. Se corrigieron solo tareas probadas por evidencia:

- informe de resultados 2 anos: preparado/finalizado segun `log.md` 2026-03-27;
- canonical: fijado en WordPress segun `log.md` 2026-04-20;
- validacion GSC de canonical: se mantiene pendiente.

### Prioridad vigente

Confirmar envio/uso del informe y preparar propuesta Ano 3 antes de abrir nuevos frentes tecnicos.

## La Bottega del Gusto

### Fuentes revisadas

- `clients/la-bottega-del-gusto/context.md`
- `clients/la-bottega-del-gusto/brand.md`
- `clients/la-bottega-del-gusto/memory.md`
- `clients/la-bottega-del-gusto/log.md`
- `clients/la-bottega-del-gusto/mensajes.md`
- `clients/la-bottega-del-gusto/tasks.md`
- `clients/la-bottega-del-gusto/outputs/manifest.md`

### Decision

El cliente esta homologado para operar en v2, pero se trata como cliente sensible por WordPress/WooCommerce, pagos, envios, impuestos, accesos y go-live.

No se reescribio `tasks.md` porque ya separa estado hecho, urgente, importante, rutina y archivos que no deben usarse. Se corrigio solo un dato obsoleto de `context.md`: el catalogo vigente es 170 productos publicados, 0 sin precio y 82 sin imagen.

### Prioridad vigente

Cerrar bloqueadores de go-live con Orden de Cambio antes de tocar produccion: rotacion/revocacion de accesos expuestos o temporales, pasarela real, Envia real, impuestos/IVA, imagenes prioritarias y prueba E2E de checkout.

## Siguiente paso

Auditar duplicaciones entre agents, skills y commands para reducir ambigüedad operativa sin borrar primitivas utiles.

## Stramondo Venezuela

### Fuentes revisadas

- `clients/stramondo-venezuela/context.md`
- `clients/stramondo-venezuela/memory.md`
- `clients/stramondo-venezuela/log.md`
- `clients/stramondo-venezuela/mensajes.md`
- `clients/stramondo-venezuela/tasks.md`
- `clients/stramondo-venezuela/outputs/manifest.md`

### Decision

El cliente esta homologado para operar en v2, pero se trata como cliente sensible por Meta Ads, presupuesto, token externo y decisiones de campañas.

No se ejecuto conector Meta Ads ni se tocaron tokens. Se corrigieron solo inconsistencias documentales: cabeceras antiguas y tabla de estado que seguia mostrando la campaña B2B como activa aunque `context.md`, `log.md`, `memory.md` y `mensajes.md` del 2026-05-11 la registran como `PAUSED`.

### Prioridad vigente

Antes de reactivar, escalar presupuesto o cambiar placements, validar estado actual en Ads Manager/API y calidad real de leads en WhatsApp Business. No usar eventos `messaging_*` como conversiones reales sin validacion manual.
