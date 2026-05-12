---
name: schema-markup
description: >
  Audita, disena o corrige datos estructurados y schema JSON-LD para clientes
  de E-SELEC: Organization, WebSite, LocalBusiness, BreadcrumbList, Article,
  FAQPage, Product, Offer, Review, Service, ItemList, rich results, Search
  Console enhancements, errores de schema, validacion de Google, schema.org,
  breadcrumbs y datos estructurados para SEO o AI search. Usalo cuando se hable
  de schema markup, structured data, JSON-LD, rich snippets, estrellas, FAQ,
  producto, negocio local, breadcrumbs, knowledge panel o datos estructurados.
---

# Schema Markup - E-SELEC

## Proposito

Ayudar a buscadores y sistemas AI a entender una pagina sin inventar informacion ni forzar rich results.

Schema no es magia SEO. Es una capa de claridad tecnica. Solo se considera correcto si representa contenido visible, verificable y actual.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`, contrato Schema markup
8. `protocols/activos-criticos.md`
9. `protocols/control-artefactos.md`
10. `.claude/skills/seo-audit/SKILL.md` si el schema forma parte de auditoria SEO
11. `.claude/skills/site-architecture/SKILL.md` si hay breadcrumbs, menus o jerarquia
12. `.claude/skills/ingesta-evidencia/SKILL.md` si usas HTML exportado, crawl, captura o output legacy

Tambien necesitas al menos una fuente de pagina:

- URL publica;
- HTML renderizado;
- captura completa;
- CMS/WordPress fields;
- contenido visible pegado por Rodrigo;
- output saneado que describa la pagina.

No crees schema final si no puedes verificar el contenido visible.

## Principios

1. Schema debe coincidir con lo que el usuario ve en la pagina.
2. JSON-LD es el formato preferido si la web lo permite.
3. Usar el tipo mas especifico que sea correcto, no el mas ambicioso.
4. No prometer rich results; Google puede no mostrarlos aunque el schema sea valido.
5. No marcar contenido oculto, falso, irrelevante o desactualizado.
6. No inventar reviews, rating, precios, stock, horarios, coordenadas, autores ni preguntas frecuentes.
7. No tocar produccion sin Orden de Cambio.

## Niveles de schema

- SM3 - validado: contenido visible comprobado, JSON-LD generado o revisado, Rich Results Test/Schema Validator revisado y riesgos documentados.
- SM2 - implementable: contenido y datos suficientes, JSON-LD o plan listo, validacion externa pendiente.
- SM1 - recomendacion: contexto suficiente para recomendar tipos de schema, pero falta HTML/URL/datos exactos.
- SM0 - bloqueado: falta pagina, contenido visible, tipo de pagina o datos requeridos.

Regla:

- SM0 no produce schema final.
- SM1 no entrega codigo como definitivo.
- SM2 permite preparar implementacion.
- SM3 permite cierre tecnico o brief de publicacion.

## Workflow

### 1. Definir pagina y objetivo

Identifica:

- tipo de pagina;
- URL;
- objetivo SEO o rich result esperado;
- audiencia;
- contenido visible;
- CMS o stack;
- schema existente si lo hay.

Si el objetivo es "estrellas", "FAQ en Google" o "knowledge panel", aclara que elegibilidad no garantiza aparicion.

### 2. Revisar contenido visible

Antes de escribir JSON-LD, comprueba que la pagina muestra:

- nombre real del negocio/producto/articulo;
- descripcion;
- imagenes;
- precios, disponibilidad o servicios si aplican;
- preguntas/respuestas si FAQ;
- autor y fechas si articulo;
- direccion/telefono/horarios si LocalBusiness;
- breadcrumbs si BreadcrumbList.

Si el contenido no esta visible, no lo marques.

### 3. Revisar schema existente

Detecta:

- multiples bloques contradictorios;
- plugins SEO que ya generan schema;
- errores de tipos o propiedades;
- IDs duplicados;
- datos desactualizados;
- warnings aceptables vs errores bloqueantes.

En WordPress, revisa si Yoast, Rank Math, WooCommerce u otro plugin ya genera schema para evitar duplicados.

### 4. Elegir tipos

Usa `references/schema-types.md`.

Regla practica:

- Home: `Organization` + `WebSite`.
- Pagina local: `LocalBusiness` si datos locales estan verificados.
- Servicio: `Service` o pagina web + Organization, segun contenido.
- Blog: `Article` o `BlogPosting`.
- Producto: `Product` + `Offer` solo si precio/stock son visibles y reales.
- FAQ: `FAQPage` solo si las preguntas y respuestas son visibles.
- Jerarquia: `BreadcrumbList`.

### 5. Crear JSON-LD

Usa `@graph` cuando haya varios tipos relacionados.

Usa `@id` estables:

```text
https://dominio.com/#organization
https://dominio.com/#website
https://dominio.com/pagina/#webpage
```

No incluyas datos personales innecesarios. No incluyas emails, IDs internos, tokens ni datos privados.

### 6. Preparar validacion

Usa `references/google-guidelines.md`.

Validacion esperada:

- Rich Results Test para elegibilidad Google.
- Schema Markup Validator para schema.org general.
- URL Inspection/Search Console si ya esta publicado y hay acceso.

Si no puedes ejecutar herramientas, deja pasos exactos de validacion y clasifica como SM2 o inferior.

### 7. Preparar output

Usa `templates/plan-schema.md`.

Debe incluir:

- nivel SM0-SM3;
- pagina;
- schema actual;
- schema recomendado;
- JSON-LD si procede;
- validacion;
- riesgos;
- implementacion;
- siguiente accion unica.

## Bloqueos

Bloquea o marca como parcial si:

- no hay URL, pagina o contenido visible;
- se pide marcar contenido inexistente;
- se pide inventar reviews/rating/precio/stock/horarios;
- hay schema duplicado y no se puede saber quien lo genera;
- el cambio requiere WordPress, plugin, tema, GTM, CMS o deploy real sin Orden de Cambio;
- hay contradiccion entre contexto, pagina y datos estructurados;
- se pide prometer rich results o rankings.

## Referencias

- `references/schema-types.md`: tipos, usos y riesgos comunes.
- `references/google-guidelines.md`: fuentes oficiales y reglas de validacion.
- `templates/plan-schema.md`: formato de salida.
- `checklists/revision.md`: revision final.
