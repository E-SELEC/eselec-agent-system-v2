---
name: seo-canon
description: >
  Aplica el canon SEO historico de E-SELEC sin resumirlo ni reemplazarlo. Usalo
  para auditorias SEO profundas, caidas de trafico, arquitectura SEO,
  migraciones, canibalizacion, GSC/SEMrush, SEO local, SEO internacional,
  schema, QA SEO, formacion de criterio SEO o cuando Rodrigo mencione el
  Docente SEO antiguo, canon SEO operativo o "tu mente es el canon".
---

# SEO Canon - E-SELEC

## Proposito

Conectar el canon SEO legacy de E-SELEC con Claude Code v2 sin crear un nuevo
Docente SEO y sin modificar el canon original.

Esta skill no reemplaza `seo-audit`. Le da criterio. `seo-audit` ejecuta la
auditoria; `seo-canon` decide como pensar el caso.

## Regla principal

No resumas, reescribas ni "mejores" el canon como fuente principal.

El canon completo vive en:

```text
references/docente-legacy/
```

El mapa completo de lectura vive en:

```text
references/indice-canon-seo.md
```

Antes de usar el canon, abre ese indice y decide que archivos exactos requiere
la tarea. No cargues todo por costumbre.

## Metodo heredado del Docente

Antes de responder, separa:

- concepto;
- criterio;
- evidencia;
- ejemplo;
- accion.

Regla de voz:

```text
claridad -> coherencia -> orden -> ejemplo -> accion
```

No uses una palabra grande sin abrirla.

## Lectura minima por tipo de trabajo

Si el caso no aparece aqui o requiere reconstruccion de agentes SEO, lee primero
`references/indice-canon-seo.md`.

| Caso | Lee |
|---|---|
| Forma de pensar SEO general | `references/docente-legacy/aprendizajes/2026-05-09-marco-maestro-seo-rodrigo.md` |
| Ejecucion SEO en web nueva o existente | `references/docente-legacy/aprendizajes/2026-05-09-ejecucion-seo-rodrigo.md` |
| Caida de trafico o rankings | marco maestro + ejecucion + GSC + SEMrush |
| Diagnostico con GSC | `references/docente-legacy/aprendizajes/2026-05-09-modulo-gsc-rodrigo.md` |
| Diagnostico con SEMrush | `references/docente-legacy/aprendizajes/2026-05-09-modulo-semrush-rodrigo.md` |
| Medicion y comportamiento | `references/docente-legacy/aprendizajes/2026-05-09-modulo-ga4-rodrigo.md` |
| Contenido y optimizacion semantica | `references/docente-legacy/aprendizajes/2026-05-09-modulo-neuronwriter-rodrigo.md` |
| SEO local / GBP | `references/docente-legacy/aprendizajes/2026-05-10-modulo-gbp-rodrigo.md` |
| Rastreo tecnico | `references/docente-legacy/aprendizajes/2026-05-10-modulo-screaming-frog-rodrigo.md` |
| WordPress / WooCommerce | `references/docente-legacy/aprendizajes/2026-05-10-modulo-wordpress-woocommerce-rodrigo.md` |
| Migraciones SEO | `references/docente-legacy/aprendizajes/2026-05-11-modulo-migraciones-seo-rodrigo.md` |
| Schema avanzado | `references/docente-legacy/aprendizajes/2026-05-11-modulo-schema-avanzado-rodrigo.md` |
| SERP manual | `references/docente-legacy/aprendizajes/2026-05-11-modulo-serp-manual-rodrigo.md` |
| Priorizacion de tareas | `references/docente-legacy/aprendizajes/2026-05-11-modulo-priorizacion-tareas-seo-rodrigo.md` |
| QA antes de publicar | `references/docente-legacy/aprendizajes/2026-05-11-modulo-qa-seo-rodrigo.md` |
| Changelog SEO | `references/docente-legacy/aprendizajes/2026-05-11-modulo-seo-changelog-rodrigo.md` |
| SEO IA / AEO / LLM | `references/docente-legacy/aprendizajes/2026-05-11-modulo-seo-ia-externo-rodrigo.md` |
| SEO internacional | `references/docente-legacy/aprendizajes/2026-05-11-modulo-seo-internacional-rodrigo.md` |
| Roles, permisos y responsabilidad | `references/docente-legacy/aprendizajes/2026-05-11-modulo-roles-permisos-seo-rodrigo.md` |
| Formacion o evaluacion de agentes SEO | `references/indice-canon-seo.md` + `references/docente-legacy/aprendizajes/2026-05-11-ruta-formacion-agentes-seo.md` |
| Matriz de competencias SEO | `references/indice-canon-seo.md` + `references/docente-legacy/aprendizajes/2026-05-11-matriz-competencias-agentes-seo.md` |
| Lectura profunda de agentes SEO antiguos | `references/indice-canon-seo.md` + `references/docente-legacy/aprendizajes/2026-05-11-lectura-profunda-agents-seo.md` |
| Lectura del sistema antes de reestructurar | `references/indice-canon-seo.md` + `references/docente-legacy/aprendizajes/2026-05-11-lectura-sistema-completo-previa-reestructuracion.md` |
| Reconstruccion de agentes SEO | `references/docente-legacy/aprendizajes/2026-05-12-mapa-canibalizacion-seo-y-estructura-destino.md` |
| Reporting o dashboard SEO | `references/indice-canon-seo.md` + GA4 + GSC + SEMrush + Looker Studio + changelog |
| GTM o tracking SEO | `references/indice-canon-seo.md` + `references/docente-legacy/aprendizajes/2026-05-10-modulo-gtm-rodrigo.md` |
| Merchant Center / ecommerce SEO | `references/indice-canon-seo.md` + `references/docente-legacy/aprendizajes/2026-05-11-modulo-merchant-center-rodrigo.md` |
| Patron de caida SEO multi-idioma | `references/patrones/patron-diagnostico-caida-seo-multidioma.md` |

## Principios que siempre aplican

1. SEO no es hacer cosas sueltas: cada accion afecta a otra.
2. En web nueva, disena antes de publicar.
3. En web existente, mide, protege y corrige antes de expandir.
4. El SEO tecnico desbloquea el SEO organico.
5. No afirmes "algoritmo" como causa sin descartar cambios tecnicos, URLs,
   indexacion, canonicals, hreflang, redirects, sitemap y datos reales.
6. Una URL debe tener una intencion principal.
7. Una intencion importante debe tener una URL principal.
8. Todo lo demas debe apoyar, no competir.
9. SEMrush ayuda a entender mercado, competencia y oportunidad.
10. GSC muestra comportamiento real en Google Search.
11. La prioridad nace del cruce entre datos, impacto, esfuerzo y riesgo.
12. No cambies produccion SEO sin Orden de Cambio.

## Como usarlo con otras skills

- Para auditoria SEO, usa esta skill como criterio y luego `seo-audit` como
  procedimiento.
- Para contenido, combina esta skill con `content-strategy`, `copywriting` o
  `copy-editing`.
- Para AI SEO, combina esta skill con `ai-seo`.
- Para arquitectura web, combina esta skill con `site-architecture`.
- Para schema, combina esta skill con `schema-markup`.

## Salida esperada cuando apliques el canon

Incluye una seccion breve:

```text
CRITERIO SEO APLICADO
Indice consultado: si/no
Canon leido:
Principio usado:
Evidencia:
Decision:
Riesgo:
Siguiente paso:
```

Si no leiste el canon relevante, no digas que lo aplicaste.
