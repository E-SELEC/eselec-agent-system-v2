# Checklist de revision - Schema Markup

Antes de entregar, comprobar:

## Contexto

- [ ] Lei contexto, memoria, log, mensajes y tasks si existen.
- [ ] Revise manifest de outputs por auditorias SEO/schema previas.
- [ ] Declare URL, tipo de pagina y fuentes.
- [ ] No repeti una recomendacion ya descartada en log.

## Contenido visible

- [ ] El schema representa contenido visible.
- [ ] No marque contenido oculto.
- [ ] No invente reviews, ratings, precios, stock, horarios, coordenadas ni autores.
- [ ] FAQPage solo se usa si las FAQs estan visibles.
- [ ] BreadcrumbList coincide con jerarquia/URLs.

## Tecnico

- [ ] JSON valido.
- [ ] Uso JSON-LD salvo motivo contrario.
- [ ] No duplique schema generado por plugins.
- [ ] Use `@graph` si hay varios tipos relacionados.
- [ ] Use `@id` estables.
- [ ] Diferencie errores de warnings.

## Validacion y riesgo

- [ ] Clasifique nivel SM0-SM3.
- [ ] Cite validacion hecha o pendiente.
- [ ] No prometi rich results ni rankings.
- [ ] No toque WordPress, plugin, tema, GTM, CMS ni deploy real sin Orden de Cambio.
- [ ] No inclui secretos, credenciales, PII ni exports brutos.
