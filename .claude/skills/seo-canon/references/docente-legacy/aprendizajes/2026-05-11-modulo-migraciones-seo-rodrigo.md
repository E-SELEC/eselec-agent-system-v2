# Modulo Migraciones SEO - Rodrigo

- Fecha: 2026-05-11
- Estado: aprendido / pendiente de verificacion viva de fuentes oficiales
- Fuente: `agents/docente/seo/fuentes/2026-05-11-manual-seo-migraciones-schema-merchant.md`
- Alcance: laboratorio del Docente SEO
- Restriccion: no modifica `agents/seo/`

---

## Idea central

Una migracion SEO es cualquier cambio importante que puede alterar como Google
rastrea, indexa, entiende o posiciona una web.

La explicacion simple:

```text
Una migracion SEO no es solo cambiar una web.
Es trasladar trafico, URLs, autoridad, indexacion, senales y confianza sin
romper lo que ya funciona.
```

Regla dura:

```text
Una migracion mal hecha puede destruir anos de SEO.
```

La migracion SEO no se trata como tarea de diseno o desarrollo. Es una operacion
de riesgo.

---

## Que bloques toca una migracion

Una migracion puede afectar:

1. SEO tecnico: redirecciones, canonicals, indexacion, robots, sitemaps, status
   codes, HTTPS y crawlability.
2. Arquitectura: URLs, menus, categorias, jerarquias, profundidad de clics y
   enlaces internos.
3. SEO On-Page: titles, metas, H1, H2, contenido y schema.
4. Contenido: paginas que se mantienen, fusionan, eliminan, nacen o cambian.
5. Autoridad: backlinks, URLs enlazadas, enlaces internos y autoridad historica.
6. Medicion: GTM, GA4, GSC, eventos y ecommerce tracking.
7. Negocio: leads, ventas, formularios, llamadas, reservas e ingresos.

---

## Tipos de migracion

No todas tienen el mismo riesgo.

Tipos:

- cambio de dominio;
- cambio de subdominio;
- HTTP -> HTTPS;
- cambio de CMS;
- rediseno;
- cambio de estructura de URLs;
- cambio de arquitectura;
- migracion ecommerce;
- fusion de webs;
- separacion de webs;
- cambio de idioma / internacionalizacion;
- cambio de servidor / hosting;
- cambio de plantilla / theme.

Regla:

```text
Un rediseno que cambia contenido, arquitectura o enlaces internos tambien es
una migracion SEO.
```

---

## Riesgos por tipo

Cambio de dominio:

- riesgo muy alto;
- cambian todas las URLs;
- cambian senales de dominio;
- requiere redirecciones completas;
- requiere GSC en ambos dominios;
- puede haber caida temporal;
- puede perder autoridad si fallan redirecciones.

HTTP -> HTTPS:

- riesgo medio-alto si se hace mal;
- revisar redirecciones;
- contenido mixto;
- canonicals;
- sitemap;
- enlaces internos;
- propiedades GSC.

Cambio de CMS:

- riesgo alto;
- cambian plantillas, sitemaps, canonicals, filtros, categorias, schema,
  renderizado y velocidad.

Cambio de URLs:

- riesgo alto;
- Google conoce la URL antigua;
- hay que trasladar senales con 301, enlaces internos y canonicals correctos.

Migracion ecommerce:

- riesgo alto;
- afecta categorias, productos, filtros, stock, precios, schema Product, carrito,
  checkout, Merchant Center y tracking ecommerce.

---

## Principio de proteccion

Antes de migrar, identificar que no se puede romper:

- URLs con trafico;
- URLs con impresiones;
- URLs con conversiones;
- URLs con backlinks;
- URLs con buenas posiciones;
- URLs enlazadas internamente;
- landings locales;
- productos/categorias con ventas;
- formularios;
- eventos;
- fichas GBP conectadas;
- Merchant Center, si aplica.

Regla:

```text
No se elimina, cambia ni fusiona una URL con valor sin revisar datos.
```

---

## Inventario previo

Fuentes del inventario:

- Screaming Frog;
- sitemap;
- GSC;
- GA4;
- backlinks;
- CMS;
- Merchant Center si es ecommerce;
- GBP si hay SEO local;
- logs o historico si existe.

Datos por URL:

```text
URL antigua:
Tipo:
Estado:
Clics:
Impresiones:
Conversiones:
Backlinks:
Enlaces internos:
Nueva URL:
Accion:
Riesgo:
Responsable:
```

---

## Mapa de redirecciones

Regla:

```text
Cada URL antigua con valor debe tener destino equivalente o decision documentada.
```

Buenas practicas:

- usar 301 para movimientos permanentes;
- evitar cadenas;
- evitar bucles;
- redirigir a equivalente real;
- no redirigir todo a Home;
- probar antes del lanzamiento;
- validar despues.

Error grave:

```text
Redirigir URLs comerciales o con backlinks a paginas genericas sin equivalencia.
```

---

## Validaciones tecnicas

Antes de lanzar:

- robots;
- noindex;
- canonicals;
- sitemap;
- status codes;
- enlaces internos;
- hreflang si aplica;
- schema;
- imagenes;
- mobile;
- velocidad;
- GTM/GA4;
- eventos;
- formularios;
- checkout si ecommerce.

Despues de lanzar:

- crawl produccion;
- validar 301;
- revisar 404;
- revisar canonicals;
- enviar sitemap;
- inspeccionar URLs clave;
- revisar GSC;
- revisar GA4;
- revisar eventos;
- revisar Merchant Center si aplica;
- revisar GBP si aplica.

---

## Migracion y contenido

Decisiones posibles:

- mantener;
- mejorar;
- fusionar;
- redirigir;
- noindexar;
- eliminar con criterio;
- crear nueva URL.

Regla:

```text
No se elimina contenido solo porque parece viejo.
Primero se revisa trafico, impresiones, backlinks, conversion y funcion estrategica.
```

---

## Migracion y schema

Riesgos:

- schema desaparece;
- schema duplicado;
- schema incorrecto;
- schema no coincide con contenido visible;
- Product schema pierde precio/stock;
- LocalBusiness queda obsoleto;
- BreadcrumbList no refleja nueva arquitectura.

Regla:

```text
En migracion, el schema debe mantenerse o mejorar, no desaparecer por cambio de
plantilla o plugin.
```

---

## Migracion local y ecommerce

SEO local:

- revisar landing local;
- NAP;
- LocalBusiness schema;
- GBP;
- enlaces desde perfil;
- telefono;
- formularios;
- rutas;
- resenas.

Ecommerce:

- categorias;
- productos;
- filtros;
- canonicals;
- schema Product;
- Merchant Center;
- stock;
- precios;
- carrito;
- checkout;
- ecommerce tracking.

Regla:

```text
Una migracion ecommerce no esta validada hasta comprobar productos, checkout,
schema Product, Merchant Center y tracking de compras.
```

---

## Migracion y medicion

Revisar:

- GTM instalado una sola vez;
- GA4 funcionando;
- eventos clave;
- formularios;
- click_phone;
- click_whatsapp;
- purchase;
- Search Console;
- conversiones;
- ecommerce tracking;
- Looker Studio si existe dashboard.

Regla:

```text
No se puede evaluar una migracion si la medicion se rompe durante el cambio.
```

---

## Equipo y responsabilidades

Una migracion requiere responsables:

- SEO;
- desarrollo;
- contenido;
- analytics;
- ecommerce;
- local;
- cliente/aprobador;
- QA.

Cada cambio debe tener:

```text
Accion:
Responsable:
Riesgo:
Fecha:
Validacion:
Estado:
```

---

## Protocolo migracion SEO

Antes:

```text
1. Definir tipo de migracion
2. Clasificar riesgo
3. Crear inventario completo
4. Identificar URLs con valor
5. Crear mapa de redirecciones
6. Revisar arquitectura nueva
7. Revisar contenido
8. Revisar canonicals
9. Revisar sitemap
10. Revisar robots/noindex
11. Revisar schema
12. Revisar medicion
13. Preparar validacion
```

Durante:

```text
1. Lanzar en ventana controlada
2. Activar redirecciones
3. Revisar status codes
4. Revisar indexabilidad
5. Revisar GTM/GA4
6. Revisar formularios/checkout
7. Revisar sitemap
8. Revisar URLs clave
```

Despues:

```text
1. Crawl produccion
2. Revisar GSC
3. Enviar sitemap
4. Inspeccionar URLs prioritarias
5. Revisar 404/500
6. Revisar caidas
7. Revisar conversiones
8. Revisar backlinks importantes
9. Revisar Merchant Center/GBP si aplica
10. Medir 2, 4, 8 y 12 semanas
```

---

## Errores comunes

1. Migrar sin inventario.
2. Cambiar URLs sin redirecciones.
3. Redirigir todo a Home.
4. No revisar URLs con backlinks.
5. Perder titles/metas/H1.
6. Perder contenido.
7. Romper enlaces internos.
8. Dejar noindex en produccion.
9. Mantener canonicals al staging.
10. Enviar sitemap con URLs antiguas.
11. Romper GTM/GA4.
12. Perder schema.
13. No revisar Merchant Center.
14. No revisar GBP.
15. No medir despues.

---

## Regla final para relevo

Una migracion SEO no se ejecuta para "cambiar la web".

```text
Se ejecuta para trasladar valor sin romper trafico, autoridad, indexacion,
conversiones ni confianza.
```

Cada migracion debe poder responder:

```text
Que cambia.
Que URLs tienen valor.
Que se mantiene.
Que se redirige.
Que se elimina.
Que se fusiona.
Que riesgos existen.
Que se valida antes.
Que se valida despues.
Como sabremos si funciono.
```
