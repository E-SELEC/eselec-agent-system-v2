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
| `cashier-bubble-tea` | activo v2 | pendiente | revisar contexto y tareas despues del piloto |
| `la-bottega-del-gusto` | activo v2 | pendiente | revisar bloqueos de produccion/e-commerce |
| `stramondo-venezuela` | activo v2 | pendiente | revisar Meta Ads y estado de conector |
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

## Siguiente paso

Homologar `cashier-bubble-tea` con el mismo criterio: revisar estructura, no copiar outputs legacy pesados, mantener datos reales dentro del cliente y definir una unica prioridad operativa.
