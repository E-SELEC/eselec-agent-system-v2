# Patrones de arquitectura web

Usa estos patrones como punto de partida. Ajusta siempre al cliente, idioma, mercado, servicios y evidencia.

## Negocio local / servicios

Uso: clinicas, talleres, restaurantes, servicios profesionales, negocios con SEO local.

```text
Home /
|-- Servicios /servicios/
|   |-- Servicio principal /servicios/servicio-principal/
|   |-- Servicio secundario /servicios/servicio-secundario/
|-- Zonas si aplica /zonas/
|   |-- Zona principal /zonas/zona-principal/
|-- Sobre nosotros /sobre-nosotros/
|-- Resenas /resenas/
|-- Blog /blog/
|-- Contacto /contacto/
|-- Legal /privacidad/ /aviso-legal/
```

Prioridad: servicios, contacto, confianza local, GBP, llamadas, WhatsApp, formularios.

## E-commerce / WooCommerce

Uso: tiendas online, catalogos con categorias, productos o pagos.

```text
Home /
|-- Tienda /tienda/
|   |-- Categoria /categoria/categoria-principal/
|   |   |-- Producto /producto/nombre-producto/
|-- Ofertas /ofertas/
|-- Guias /guias/
|-- Ayuda /ayuda/
|   |-- Envios /ayuda/envios/
|   |-- Devoluciones /ayuda/devoluciones/
|-- Contacto /contacto/
|-- Carrito /carrito/
|-- Mi cuenta /mi-cuenta/
```

Prioridad: categorias, producto, filtros, checkout, schema product, tracking e-commerce, no romper checkout.

## Web corporativa / agencia / B2B

Uso: marca corporativa, servicios profesionales, captacion de leads.

```text
Home /
|-- Servicios /servicios/
|   |-- Servicio A /servicios/servicio-a/
|   |-- Servicio B /servicios/servicio-b/
|-- Sectores /sectores/
|-- Casos /casos/
|-- Recursos /recursos/
|-- Sobre nosotros /sobre-nosotros/
|-- Contacto /contacto/
```

Prioridad: propuesta de valor, servicios, prueba social, formularios y rutas a conversion.

## Hub SEO / contenido

Uso: captacion organica por clusters, blog, guias o recursos.

```text
Home /
|-- Recursos /recursos/
|   |-- Guia principal /recursos/tema-principal/
|   |-- Plantillas /recursos/plantillas/
|-- Blog /blog/
|   |-- Categoria /blog/categoria/
|   |-- Post /blog/post/
|-- Servicios /servicios/
|-- Contacto /contacto/
```

Prioridad: hubs, spokes, enlazado interno, intencion de busqueda, evitar canibalizacion.

## Landing de campana

Uso: Google Ads, Meta Ads, captacion puntual, oferta especifica.

```text
Landing /landing/oferta/
|-- Gracias /landing/oferta/gracias/
|-- Legal /privacidad/
```

Prioridad: conversion, tracking, velocidad, mensaje-landing coherente, no mezclar con navegacion extensa.

## Hibrido

Uso: cliente con servicios, SEO, contenido, campañas y captacion.

```text
Home /
|-- Servicios /servicios/
|-- Soluciones /soluciones/
|-- Recursos /recursos/
|-- Casos /casos/
|-- Blog /blog/
|-- Contacto /contacto/
```

Prioridad: separar conversion directa de captacion organica, y conectar ambas con enlaces contextuales.

## Reglas rapidas

- Negocio local: estructura plana, servicios visibles, contacto fuerte.
- E-commerce: categorias primero, productos no huerfanos, checkout intocable sin Orden de Cambio.
- B2B: servicios + casos + contacto.
- Contenido: hubs claros y enlaces hacia conversion.
- Landing: foco extremo, tracking antes de invertir.
- Reestructura: nunca sin inventario y redirects.
