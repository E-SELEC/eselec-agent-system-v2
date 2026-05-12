---
name: ai-seo
description: >
  Audita, planifica u optimiza visibilidad en respuestas AI y buscadores
  generativos para clientes de E-SELEC: AI SEO, AEO, GEO, LLM SEO,
  AI Overviews, ChatGPT Search, Perplexity, Claude, Gemini, Copilot, citas AI,
  menciones de marca, answer blocks, contenido citable, extractabilidad,
  entidades, presencia en terceros, robots.txt para crawlers AI y medicion de
  share of voice AI. Usalo cuando se hable de aparecer en respuestas AI, ser
  citado por modelos, optimizar para ChatGPT/Perplexity/Gemini/Claude o
  mejorar visibilidad en AI search.
---

# AI SEO - E-SELEC

## Proposito

Mejorar la probabilidad de que un cliente sea encontrado, entendido y citado por sistemas de busqueda AI sin vender humo.

AI SEO no reemplaza SEO. Se apoya en SEO tecnico, contenido claro, autoridad, schema, presencia externa y medicion por consultas.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`, contrato AI SEO si existe
8. `.claude/skills/seo-audit/SKILL.md`
9. `.claude/skills/schema-markup/SKILL.md` si hay datos estructurados
10. `.claude/skills/site-architecture/SKILL.md` si hay hubs, clusters o arquitectura
11. `.claude/skills/ingesta-evidencia/SKILL.md` si usas capturas, exports o outputs legacy
12. `protocols/activos-criticos.md`

Para afirmaciones sobre una plataforma AI, usa evidencia actual: captura, fecha, query exacta, ubicacion/idioma si importa, fuente citada y competidores citados.

## Principios

1. No prometas citas AI, rich results ni rankings.
2. Mide por consulta y plataforma; no por sensacion.
3. Distingue visibilidad, mencion, cita, enlace y trafico.
4. No uses estadisticas legacy o de terceros sin fuente y fecha.
5. Optimiza primero contenido verificable, util y extractable.
6. No cambies robots.txt, noindex, sitemap, CDN, Cloudflare ni plugins sin Orden de Cambio.
7. No crees contenido falso, reviews falsas, claims no verificables ni autoridad inventada.

## Niveles de evidencia AI

- AI3 - verificado: queries probadas en plataformas definidas, capturas o registro, fuentes citadas, competidores y fecha.
- AI2 - parcial fuerte: evidencia SEO/schema/contenido y algunas pruebas manuales, pero no cobertura completa de plataformas.
- AI1 - orientativo: contexto y supuestos razonables, sin pruebas actuales por query.
- AI0 - bloqueado: falta cliente, dominio, queries objetivo o pagina/contenido a evaluar.

Regla:

- AI0 no produce plan final.
- AI1 solo da hipotesis.
- AI2 permite roadmap interno.
- AI3 permite informe o recomendacion fuerte.

## Workflow

### 1. Definir alcance

Identifica:

- objetivo: ser citado, mejorar menciones, crear contenido, auditar presencia, revisar robots.txt;
- plataformas: Google AI Overviews/AI Mode, ChatGPT Search, Perplexity, Claude, Gemini, Copilot;
- mercado e idioma;
- consultas prioritarias;
- paginas candidatas;
- competidores;
- decision que Rodrigo tomara con el resultado.

Si no hay queries objetivo, primero crea una lista corta de 10-20 consultas con intencion clara.

### 2. Medir visibilidad AI

Usa `templates/auditoria-ai-seo.md`.

Por cada consulta registra:

- fecha;
- plataforma;
- prompt/query exacta;
- si aparece respuesta AI;
- si el cliente es citado;
- si el cliente es mencionado sin cita;
- competidores citados;
- URLs citadas;
- notas de sesgo: ubicacion, idioma, login, personalizacion.

No mezcles resultados de dias distintos como si fueran una unica foto.

### 3. Revisar fundamentos SEO

AI search depende de que el contenido sea rastreable, indexable y entendible.

Comprueba:

- indexacion basica;
- robots.txt;
- sitemap;
- canonicals;
- velocidad y renderizado;
- estructura de headings;
- schema;
- autoridad y enlaces;
- presencia local o de entidad.

Si hay problemas SEO criticos, prioriza `seo-audit` antes de AI SEO avanzado.

### 4. Revisar extractabilidad

Usa `references/content-patterns.md`.

Evalua si el contenido tiene:

- respuesta directa al inicio;
- definiciones claras;
- tablas comparativas;
- listas paso a paso;
- FAQs visibles;
- datos con fuente;
- autor/fecha;
- lenguaje especifico, no generico;
- parrafos que se entienden fuera de contexto.

AI cita bloques utiles, no paginas bonitas.

### 5. Revisar autoridad y presencia externa

Identifica:

- menciones en medios, directorios, reviews, foros, YouTube, redes o plataformas sectoriales;
- consistencia de nombre, categoria, telefono, direccion y servicios;
- perfiles de confianza;
- fuentes de terceros que las plataformas AI citan para esas queries.

No recomiendes crear presencia externa falsa o spam. Recomienda presencia verificable.

### 6. Revisar crawlers y robots

Usa `references/ai-crawler-access.md`.

Antes de recomendar cambios:

- verifica robots.txt actual;
- identifica si hay reglas para bots AI;
- diferencia crawlers de busqueda, entrenamiento y fetch iniciado por usuario;
- confirma docs oficiales recientes antes de tocar reglas;
- aplica Orden de Cambio si se modifica produccion.

No asumas que permitir o bloquear un bot siempre aumenta visibilidad. Es decision de negocio.

### 7. Preparar plan

Debe incluir:

- nivel AI0-AI3;
- consultas priorizadas;
- estado actual;
- brechas frente a competidores;
- quick wins;
- contenido a crear/mejorar;
- schema/arquitectura necesaria;
- presencia externa;
- riesgos;
- siguiente accion unica.

## Bloqueos

Bloquea o marca como parcial si:

- no hay queries objetivo;
- no hay dominio o cliente claro;
- se quieren conclusiones sin fecha/plataforma/query;
- se usan cifras sin fuente;
- se pide cambiar robots.txt/CDN/noindex/sitemap sin Orden de Cambio;
- se pide prometer citas AI;
- hay claims de autoridad, resultados o datos no verificables.

## Referencias

- `references/content-patterns.md`: patrones de contenido extractable y citable.
- `references/ai-crawler-access.md`: crawlers, robots.txt y fuentes oficiales.
- `templates/auditoria-ai-seo.md`: formato de auditoria/plan.
- `checklists/revision.md`: revision final.
