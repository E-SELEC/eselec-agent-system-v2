# Piloto 01 - Computer Chamberi

> STATUS: ARCHIVADO - decision de piloto tomada. Este documento queda como historia de migracion, no como canon operativo.

## Estado

- ID: P2-005
- Fecha: 2026-05-12
- Cliente piloto: `computer-chamberi`
- Estado: definido, no migrado aun

## Decision

El primer piloto de operacion v2 sera **Computer Chamberi**.

Este piloto probara el sistema nuevo sin tocar produccion:

- `leader-clientes`;
- `client-audit`;
- `seo-audit`;
- contratos de calidad;
- commands `alertas-pendientes` y `auditoria-semanal`;
- Docente si Rodrigo corrige o rechaza el output.

## Por que este cliente

Computer Chamberi es el mejor piloto inicial porque:

- tiene trabajo SEO real y reciente;
- tiene datos suficientes para probar calidad de auditoria;
- tiene oportunidades claras de CTR, contenido y SEO local;
- no depende de Ads con presupuesto activo;
- no es ecommerce/WooCommerce de alto riesgo;
- permite probar `seo-audit` sin ejecutar cambios en produccion;
- el inventario legacy ya lo marco como candidato natural para piloto SEO.

## Por que no los otros primero

| Cliente | Motivo para no empezar |
|---|---|
| `la-bottega-del-gusto` | Riesgo alto por WordPress/WooCommerce, tienda, checkout y operaciones reales. Mejor despues de validar protocolos con un piloto menos sensible. |
| `stramondo-venezuela` | Riesgo operativo por Meta Ads y presupuesto real. Requiere conectores/Ads saneados antes. |
| `cashier-bubble-tea` | Valido para fase posterior, pero Computer Chamberi prueba mejor SEO/calidad por volumen de datos. |
| `shogun-motors` | Cliente dado de baja; debe quedar como legacy/no activo. |

## Alcance del piloto

### Incluye

1. Migrar estructura minima del cliente a v2:
   - `context.md`
   - `memory.md`
   - `log.md`
   - `mensajes.md`
   - `tasks.md`
   - `outputs/manifest.md`

2. Ejecutar lectura con `leader-clientes`.

3. Ejecutar auditoria con `client-audit`.

4. Ejecutar auditoria SEO con `seo-audit` en modo diagnostico.

5. Evaluar output contra `quality/criterios-output.md`.

6. Registrar incidencias de calidad.

### No incluye

- Cambios en WordPress.
- Cambios en titles/metas reales.
- Cambios en GBP.
- Cambios en GSC/GA4.
- Ejecucion de scripts con credenciales.
- Migrar outputs historicos completos.
- Subir PDFs, capturas, exports o archivos pesados.

## Datos a migrar con cautela

Migrar solo resumen vigente y referencias necesarias.

No copiar:

- secretos;
- tokens;
- exports brutos;
- capturas;
- rutas sensibles de credenciales;
- archivos pesados;
- historico completo de outputs.

Si un output legacy es necesario, crear una referencia en `outputs/manifest.md` o resumirlo.

## Prueba de calidad del piloto

El piloto pasa si:

- `leader-clientes` identifica estado, prioridad y ruta sin cargar contexto excesivo;
- `client-audit` produce una prioridad unica y no una lista plana;
- `seo-audit` declara fuentes, datos faltantes, evidencia y top 3 problemas;
- ningun output afirma datos no consultados;
- no se toca produccion;
- no se filtran secretos;
- los registros quedan actualizados;
- Rodrigo puede entender que hacer despues.

## Orden recomendado

1. P3-002: migrar carpeta minima de `computer-chamberi`.
2. Ejecutar `client-audit` sobre el cliente migrado.
3. Ejecutar `seo-audit` usando datos disponibles.
4. Comparar resultado contra `quality/criterios-output.md`.
5. Si Rodrigo corrige el resultado, activar `docente`.
6. Ajustar skill/leader antes de migrar mas clientes.

## Riesgos

| Riesgo | Mitigacion |
|---|---|
| Contexto legacy contiene rutas o notas sensibles | Migrar resumen, no copiar todo a ciegas |
| GSC/GA4 requieren accesos vivos | Marcar output como parcial si no se consultan |
| Se confunde diagnostico con ejecucion SEO | Prohibir cambios en produccion durante piloto |
| Output SEO vuelve a ser generico | Validar con contrato `quality/criterios-output.md` |

## Siguiente paso

Ejecutar P3-002:

```text
Migrar cliente piloto `computer-chamberi` con estructura minima y sin outputs pesados.
```
