# Fuentes oficiales y validacion

Consulta estas fuentes cuando el trabajo dependa de elegibilidad para rich results o reglas especificas.

## Fuentes oficiales

- Google structured data intro: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Google general structured data guidelines: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Google supported structured data features: https://developers.google.com/search/docs/guides/search-gallery
- Rich Results Test / Schema Markup Validator: https://developers.google.com/search/docs/appearance/structured-data
- LocalBusiness structured data: https://developers.google.com/search/docs/appearance/structured-data/local-business
- FAQPage structured data: https://developers.google.com/search/docs/appearance/structured-data/faqpage

## Reglas operativas

- JSON-LD es recomendado por Google si el sitio lo permite.
- Validar rich results con Rich Results Test.
- Validar schema.org general con Schema Markup Validator.
- Search Console ayuda a revisar mejoras, errores y acciones manuales cuando hay acceso.
- Google no garantiza rich results aunque el schema sea valido.
- El marcado debe representar el contenido principal visible.
- No marcar contenido oculto, enganoso, irrelevante o falso.
- Las URLs de imagen deben ser rastreables e indexables.
- La pagina no debe estar bloqueada a Googlebot, noindex o robots si se espera rich result.

## Antes de publicar

1. Comprobar que no hay schema duplicado por plugin.
2. Validar JSON.
3. Validar elegibilidad.
4. Revisar warnings.
5. Documentar que queda como advertencia aceptada.
6. Publicar solo con Orden de Cambio si toca produccion.
