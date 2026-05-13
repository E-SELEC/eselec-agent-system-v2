---
name: programmatic-seo
description: >
  Planifica y revisa SEO programatico para clientes de E-SELEC: paginas a
  escala, pSEO, templates SEO, directorios, location pages, paginas de ciudad,
  integraciones, comparativas, plantillas con datos, sitemaps, indexacion,
  contenido unico por pagina, crawl budget y arquitectura de enlazado interno.
  Usalo cuando se hable de crear muchas paginas SEO, keyword + ciudad,
  programmatic SEO, data-driven pages o templated landing pages.
---

# Programmatic SEO - E-SELEC

## Proposito

Crear planes de paginas SEO a escala que tengan valor unico, datos fiables, arquitectura clara y control de indexacion.

Esta skill no genera ni publica paginas reales. Produce estrategia, template, matriz de datos o plan de lanzamiento.

## Fuentes obligatorias

Si el cliente existe, lee contexto, memoria, log, mensajes, tasks, manifest, `quality/criterios-output.md`, y cuando aplique:

- `.claude/skills/seo-audit/SKILL.md`
- `.claude/skills/content-strategy/SKILL.md`
- `.claude/skills/site-architecture/SKILL.md`
- `.claude/skills/schema-markup/SKILL.md`
- `.claude/skills/analytics-tracking/SKILL.md`
- `protocols/activos-criticos.md`

Necesitas patron de keyword, fuente de datos y criterio de valor unico por pagina.

## Niveles

- PS3 - listo: patron, datos, template, arquitectura, indexacion, schema, medicion y riesgos definidos.
- PS2 - fuerte: oportunidad y template claros; faltan datos completos o validacion tecnica.
- PS1 - orientativo: idea de paginas a escala con evidencia parcial.
- PS0 - bloqueado: falta patron, datos o valor unico.

## Workflow

1. Validar oportunidad: patron de busqueda, intent, volumen/distribucion, competidores.
2. Validar datos: fuente, frescura, permisos, campos, calidad y actualizacion.
3. Definir template con secciones unicas y condicionales.
4. Definir URL, hub/spokes, breadcrumbs, enlaces y sitemap.
5. Definir indexacion: publicar, noindex, fases, canonicals y crawl budget.
6. Definir schema y tracking.
7. Preparar output con `templates/programmatic-seo-plan.md`.

## Reglas

- Calidad sobre cantidad.
- No crear doorway pages ni paginas con solo variables cambiadas.
- No usar datos publicos sin aportar valor adicional.
- No publicar paginas sin revisar arquitectura, noindex/canonicals y tracking.
- No prometer trafico.

## Bloqueos

- no hay patron de keyword;
- no hay fuente de datos;
- no hay valor unico por pagina;
- se propone generar paginas sin control de indexacion;
- se piden cambios de URLs/CMS/sitemap sin Orden de Cambio.

## Referencias

- `references/pseo-patterns.md`: playbooks.
- `templates/programmatic-seo-plan.md`: formato de salida.
- `checklists/revision.md`: revision final.
