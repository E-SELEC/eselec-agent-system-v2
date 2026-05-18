# Modulo Control de Calidad SEO - Rodrigo

- Fecha: 2026-05-11
- Estado: aprendido / pendiente de verificacion viva de fuentes oficiales
- Fuente: `agents/docente/seo/fuentes/2026-05-11-manual-seo-serp-qa-changelog.md`
- Alcance: laboratorio del Docente SEO
- Restriccion: no modifica `agents/seo/`

---

## Idea central

El control de calidad SEO antes de publicar es el proceso de revisar una URL,
plantilla, producto, categoria, articulo, landing, rediseno o cambio tecnico
antes de que salga a produccion o antes de considerarlo terminado.

La explicacion simple:

```text
Control de calidad SEO no es revisar si "se ve bien".
Es confirmar que la URL puede ser rastreada, indexada, entendida, medida y usada correctamente.
```

Regla principal:

```text
Nada importante se publica sin revision SEO.
```

Muchos errores SEO no se ven a simple vista:

- noindex accidental;
- canonical incorrecta;
- title vacio;
- H1 duplicado;
- formulario sin medicion;
- enlace interno roto;
- imagen pesada;
- schema invalido;
- URL fuera del sitemap;
- producto con precio distinto al feed;
- WhatsApp sin evento;
- pagina no apta para mobile.

---

## Donde encaja

QA SEO conecta todos los bloques:

1. SEO tecnico: rastreo, indexacion, canonicals, robots, noindex, sitemap,
   status codes y redirecciones.
2. SEO On-Page: title, meta, H1, H2/H3, contenido, enlaces internos e imagenes.
3. SEO de contenidos: intencion, estructura, claridad, profundidad,
   actualizacion y diferenciacion.
4. SEO local: NAP, telefono, mapa, GBP, LocalBusiness y eventos de llamada.
5. Ecommerce SEO: precio, stock, Product schema, Merchant Center, imagenes,
   categorias y checkout.
6. Medicion: GTM, GA4, eventos, eventos clave, ecommerce tracking.
7. UX/CRO: mobile, CTA, formularios, WhatsApp, telefono, velocidad y friccion.

---

## Que NO es QA SEO

No es:

- mirar la pagina por encima;
- revisar solo diseno;
- confiar en que el plugin SEO esta en verde;
- publicar porque ya esta subido;
- revisar despues de que el cliente se queje;
- revisar solo desktop;
- revisar solo contenido;
- revisar solo tecnica;
- asumir que si WordPress guarda, Google lo entendera.

Regla:

```text
Publicar no significa terminar.
Terminar significa publicar, validar y documentar.
```

---

## Web nueva vs web existente

### Web nueva

QA debe hacerse antes y despues del lanzamiento.

Flujo:

```text
1. Revisar staging
2. Validar arquitectura
3. Validar URLs
4. Validar indexacion
5. Validar titles/metas/H1
6. Validar contenido
7. Validar enlaces internos
8. Validar imagenes
9. Validar schema
10. Validar mobile
11. Validar velocidad
12. Validar GTM/GA4
13. Validar formularios
14. Lanzar
15. Rastrear produccion
16. Enviar sitemap
17. Inspeccionar URLs clave
18. Documentar
```

### Web existente

QA protege lo que ya funciona.

Flujo:

```text
1. Confirmar URL actual
2. Revisar datos GSC/GA4 si la URL tiene valor
3. Revisar cambios propuestos
4. Validar que no cambia slug sin plan
5. Validar indexacion
6. Validar canonical
7. Validar contenido
8. Validar enlaces
9. Validar medicion
10. Publicar
11. Revisar en produccion
12. Registrar changelog
13. Programar revision
```

---

## Checklist general

Tecnica:

- status code 200;
- indexable;
- sin noindex accidental;
- robots correcto;
- canonical correcto;
- sitemap;
- redirecciones;
- enlaces rotos;
- staging no indexable si aplica;
- produccion indexable si aplica.

On-Page:

- title;
- meta;
- H1;
- H2/H3;
- contenido;
- CTA;
- enlaces internos;
- imagenes;
- ALT.

Schema:

- tipo correcto;
- validado;
- sin errores criticos;
- coincide con contenido visible.

Mobile / UX:

- mobile revisado;
- CTA visible;
- formulario probado;
- WhatsApp probado;
- telefono probado;
- velocidad razonable;
- Core Web Vitals si aplica.

Medicion:

- GTM;
- GA4;
- eventos;
- eventos clave;
- formulario;
- ecommerce.

Ecommerce:

- precio;
- stock;
- Product schema;
- Merchant Center;
- add to cart;
- checkout;
- purchase.

Local:

- NAP;
- GBP;
- mapa;
- telefono;
- LocalBusiness.

---

## QA por tipo de tarea

Landing:

- intencion;
- SERP;
- title/meta/H1;
- CTA;
- formularios;
- eventos;
- enlaces internos;
- mobile.

Articulo:

- intencion informacional;
- estructura;
- H2/H3;
- enlaces a paginas comerciales;
- autor/confianza;
- schema Article si aplica.

Producto:

- precio;
- stock;
- imagen;
- descripcion;
- schema Product;
- Merchant Center;
- add_to_cart;
- checkout.

Migracion:

- redirecciones;
- noindex;
- canonicals;
- sitemap;
- GSC;
- GA4;
- schema;
- Merchant/GBP si aplica.

GTM/GA4:

- Preview Mode;
- DebugView;
- eventos correctos;
- sin duplicidad;
- eventos clave justificados.

---

## Junior vs senior

Un junior no debe sin aprobacion:

- aprobar publicacion final solo;
- cambiar noindex;
- cambiar canonical;
- tocar robots.txt;
- cambiar URLs;
- publicar migraciones;
- aprobar ecommerce sin compra de prueba;
- validar schema critico solo;
- marcar eventos clave;
- cambiar GTM en produccion;
- publicar landings que convierten;
- eliminar contenido;
- solicitar indexacion de URLs criticas;
- enviar QA final al cliente sin revision.

Un junior si puede:

- completar checklist;
- revisar visual;
- probar enlaces;
- probar formularios;
- revisar titles/metas;
- revisar imagenes;
- pasar Rich Results Test;
- preparar incidencias;
- documentar pendientes.

Regla:

```text
La aprobacion final debe pasar por perfil senior cuando hay impacto SEO o negocio.
```

---

## Plantilla interna de QA SEO

```text
Cliente:
Dominio:
URL:
Fecha:
Responsable:
Tipo de tarea:
Web nueva / web existente:

1. Intencion
- Keyword principal:
- Intencion:
- Tipo de pagina:
- SERP validada:
- Canibalizacion revisada:

2. Tecnica
- Status code:
- Indexable:
- Noindex:
- Robots:
- Canonical:
- Sitemap:
- Redirecciones:
- Enlaces rotos:

3. On-Page
- Title:
- Meta:
- H1:
- H2/H3:
- Contenido:
- CTA:
- Enlaces internos:
- Imagenes:
- ALT:

4. Schema
- Tipo:
- Validado:
- Errores:
- Warnings:
- Coincide con contenido visible:

5. Mobile / UX
- Mobile revisado:
- CTA visible:
- Formulario:
- WhatsApp:
- Telefono:
- Velocidad:
- Core Web Vitals:

6. Medicion
- GTM:
- GA4:
- Eventos:
- Eventos clave:
- Formulario:
- Ecommerce:

7. Ecommerce, si aplica
- Precio:
- Stock:
- Product schema:
- Merchant Center:
- Add to cart:
- Checkout:

8. Local, si aplica
- NAP:
- GBP:
- Mapa:
- Telefono:
- LocalBusiness:

9. Aprobacion
- Revisado por:
- Aprobado:
- Pendientes:
- Fecha de publicacion:
- Fecha de revision:
```

---

## Errores comunes

1. Publicar con noindex.
2. Publicar con canonical incorrecta.
3. Publicar con URL de staging.
4. Publicar sin title.
5. Publicar con H1 generico.
6. Publicar sin enlaces internos.
7. Publicar formulario sin probar.
8. Publicar WhatsApp mal enlazado.
9. Publicar producto con precio incorrecto.
10. Publicar producto sin stock real.
11. Publicar schema invalido.
12. Publicar sin revisar mobile.
13. Publicar sin GA4/GTM.
14. Publicar con imagenes pesadas.
15. Publicar sin documentar.
16. Cambiar URL sin redireccion.
17. Eliminar contenido que posicionaba.
18. Solicitar indexacion antes de terminar.
19. Enviar al cliente sin QA.
20. No revisar despues de publicar.

---

## Regla final para relevo

QA SEO no se hace para llenar una lista.

```text
Se hace para evitar publicar errores que pueden afectar rastreo, indexacion,
conversion, medicion o negocio.
```

Cada QA debe poder responder:

```text
Que se reviso.
Que URL afecta.
Que riesgo habia.
Que fallo se encontro.
Que se corrigio.
Que queda pendiente.
Quien aprueba.
Cuando se revisa despues.
Donde queda documentado.
```
