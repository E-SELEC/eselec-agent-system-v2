# Tipos de schema para E-SELEC

Usa esta referencia para elegir el tipo correcto. No todos los tipos producen rich results.

| Tipo | Uso | Datos minimos | Riesgo |
|---|---|---|---|
| `Organization` | Home, about, marca corporativa | name, url, logo si existe | bajo |
| `WebSite` | Home/sitio completo | name, url | bajo |
| `WebPage` | Pagina especifica | name, url, isPartOf | bajo |
| `BreadcrumbList` | Paginas con jerarquia visible | items con position, name, item | bajo-medio |
| `LocalBusiness` | Negocio fisico/local | name, address, phone, hours si visibles | medio |
| `Service` | Paginas de servicios | serviceType, provider, areaServed si aplica | medio |
| `Article` / `BlogPosting` | Blog o noticias | headline, datePublished, author, image si existe | medio |
| `Product` | Producto e-commerce | name, image, description, offers si visible | alto |
| `Offer` | Precio/oferta | price, currency, availability, url | alto |
| `FAQPage` | FAQ visible en la pagina | preguntas y respuestas visibles | medio |
| `Review` / `AggregateRating` | Reviews elegibles y visibles | ratingValue, count, review source | alto |
| `ItemList` | Listados, categorias, rankings | list items visibles | medio |

## Seleccion rapida

### Home

- `Organization`
- `WebSite`
- `WebPage`

### Servicio local

- `LocalBusiness` si el negocio local esta verificado.
- `Service` si la pagina describe un servicio claro.
- `BreadcrumbList` si hay jerarquia visible.

### Blog

- `BlogPosting`
- `BreadcrumbList`
- `Organization` como publisher si procede.

### Producto / WooCommerce

- `Product`
- `Offer`
- `BreadcrumbList`

Bloquea si precio, disponibilidad o imagen no son reales o no estan visibles.

### FAQ

- `FAQPage`

Bloquea si las preguntas/respuestas no estan visibles para el usuario.

## Riesgos comunes

- Duplicar schema generado por plugins.
- Usar `Product` para servicios sin producto real.
- Usar `AggregateRating` sin reviews visibles o elegibles.
- Marcar FAQs ocultas.
- Poner datos de GBP que no coinciden con la web.
- Usar datos antiguos de horario, precio o disponibilidad.
- Crear breadcrumbs que no coinciden con URLs o navegacion.

## Regla de compatibilidad

Cuando haya varios tipos, usar `@graph` y conectar con `@id`.

Ejemplo de IDs:

```text
https://example.com/#organization
https://example.com/#website
https://example.com/servicios/reparacion/#webpage
```
