# Manifest outputs - Computer Chamberi

## Estado

- Fecha de migracion minima: 2026-05-12
- Politica: no se migran outputs historicos completos al repo v2.

## Outputs legacy referenciados, no copiados

| Archivo legacy | Uso | Estado v2 |
|---|---|---|
| `auditoria-seo-2026-05-07.md` | Diagnostico SEO legacy | Referencia historica, no migrado completo |
| `estrategia-seo-2026-05-07.md` | Estrategia SEO legacy | Referencia historica, no migrado completo |
| `ctr-audit-2026-05-07.md` | Auditoria CTR legacy | Referencia historica, no migrado completo |
| `plan-metas-ctr-2026-05-08.md` | Plan de metas legacy | Referencia historica, no migrado completo |

## Outputs v2

| Archivo v2 | Uso | Estado |
|---|---|---|
| `evidencia-seo-2026-05-12.md` | Paquete saneado de evidencia SEO desde outputs legacy | Vigente para auditoria parcial fuerte |
| `auditoria-arranque-v2-2026-05-13.md` | Auditoria de arranque operativo O1-001 en modo lectura | Vigente como diagnostico parcial fuerte |
| `conversaciones/diagnostico-seo-2026-05-16.json` | Conversacion real de diagnostico SEO usada como referencia historica del cliente | Movida desde `seo-canon`; no es canon general |
| `homologacion-v2-2026-05-19.md` | Revision de estructura, memoria y siguiente prioridad del cliente piloto v2 | Vigente; confirma medicion como proxima prioridad |

## Regla

Si un output legacy es necesario para una tarea v2:

1. leerlo desde legacy;
2. extraer solo el resumen necesario;
3. no copiar secretos, rutas sensibles ni exports brutos;
4. registrar cualquier output nuevo aqui.
