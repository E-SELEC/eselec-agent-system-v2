# Modulo Datos Estructurados Avanzado / Schema - Rodrigo

- Fecha: 2026-05-11
- Estado: aprendido / pendiente de verificacion viva de fuentes oficiales
- Fuente: `agents/docente/seo/fuentes/2026-05-11-manual-seo-migraciones-schema-merchant.md`
- Skill de apoyo usada: `schema-markup`
- Alcance: laboratorio del Docente SEO
- Restriccion: no modifica `agents/seo/`

---

## Idea central

Los datos estructurados, o Schema Markup, explican de forma estandarizada que
hay en una pagina.

La explicacion simple:

```text
Schema no es magia SEO.
Schema es una capa de claridad tecnica.
```

Schema no sustituye contenido. Ayuda a Google a entender mejor el contenido que
ya existe.

Regla:

```text
Schema aumenta claridad, no convierte contenido debil en contenido fuerte.
```

---

## Principios de calidad

1. Debe representar contenido visible.
2. Debe coincidir con la pagina.
3. Debe usar el tipo correcto.
4. Debe tener propiedades requeridas.
5. Debe evitar duplicados contradictorios.
6. Debe validarse antes de publicar.
7. Debe monitorizarse en Search Console.
8. Debe actualizarse cuando cambian datos comerciales.

Regla:

```text
No se implementa schema que no puedas explicar.
```

---

## Web nueva vs web existente

### Web nueva

Schema se planifica desde la arquitectura.

Flujo:

```text
1. Definir tipos de pagina
2. Asignar schema por plantilla
3. Definir fuente de datos
4. Implementar en plantilla
5. Validar en herramientas
6. Publicar
7. Revisar en Search Console
```

Ejemplos:

- home -> Organization / WebSite;
- servicio local -> LocalBusiness / Service / BreadcrumbList;
- producto -> Product / Offer / BreadcrumbList;
- articulo -> Article / BlogPosting;
- FAQs visibles -> FAQPage si aplica.

### Web existente

Primero se audita. No se añade schema encima sin saber que existe.

Flujo:

```text
1. Detectar schema existente
2. Identificar fuente del schema
3. Validar errores
4. Detectar duplicados
5. Detectar schema incorrecto
6. Revisar coincidencia con contenido visible
7. Revisar Search Console
8. Priorizar correcciones
9. Eliminar contradicciones
10. Añadir schema faltante
11. Documentar fuente y mantenimiento
```

Riesgo comun:

```text
WooCommerce genera Product schema.
Plugin SEO genera Product schema.
Plugin de reviews genera Product schema.
Plugin de schema genera Product schema.
```

Resultado posible: duplicidad y contradiccion.

---

## Que NO es Schema

Schema no es:

- truco SEO;
- garantia de rich result;
- sustituto de contenido;
- forma de meter datos invisibles;
- solucion para falta de autoridad;
- excusa para inventar reseñas;
- capa decorativa;
- algo que se instala sin mantenimiento.

Regla:

```text
Schema valido no garantiza rich result.
```

---

## Tipos principales

Organization:

- home/sobre nosotros;
- nombre;
- URL;
- logo;
- sameAs;
- contacto si aplica.

LocalBusiness:

- negocios locales;
- NAP;
- horarios;
- ubicacion;
- telefono;
- URL;
- debe coincidir con GBP y web.

BreadcrumbList:

- paginas con breadcrumbs;
- debe coincidir con ruta visible y arquitectura real.

Product:

- fichas de producto;
- nombre;
- imagen;
- precio/oferta;
- disponibilidad;
- marca/SKU si aplica;
- debe coincidir con web y Merchant Center.

Offer:

- precio;
- moneda;
- disponibilidad;
- URL;
- condiciones si aplica.

Review / AggregateRating:

- solo reseñas reales;
- no inventar estrellas;
- seguir politicas.

Article / BlogPosting:

- articulos;
- headline;
- autor;
- fechas;
- imagen;
- publisher.

FAQPage:

- solo FAQs visibles;
- no depender de FAQ schema como tactica principal de visibilidad.

WebSite / SearchAction:

- marca y busqueda interna si aplica.

ItemList / Carousel:

- listados o colecciones cuando corresponde.

MerchantReturnPolicy / shipping:

- ecommerce;
- debe coincidir con politicas visibles y Merchant Center.

ProfilePage:

- perfiles cuando el tipo de pagina lo justifica.

---

## Schema en WordPress y WooCommerce

En WordPress, Schema puede venir de:

- tema;
- plugin SEO;
- plugin schema;
- WooCommerce;
- plugin de reviews;
- desarrollo manual;
- GTM.

Regla:

```text
Una fuente principal de schema siempre que sea posible.
```

WooCommerce:

- suele generar Product;
- puede combinarse con plugin SEO;
- hay que revisar precio, stock, reviews y oferta;
- evitar duplicados.

Error tipico:

```text
Instalar un plugin de schema encima de WooCommerce + Rank Math/Yoast sin revisar duplicados.
```

---

## Schema y Merchant Center

Para ecommerce, Schema y Merchant Center deben ser coherentes.

Revisar:

- precio visible;
- precio en schema;
- precio en Merchant Center;
- disponibilidad visible;
- disponibilidad en schema;
- disponibilidad en Merchant Center;
- imagenes;
- GTIN/SKU/brand si aplica;
- politicas de envio/devolucion.

Regla:

```text
La ficha visible, el schema Product, WooCommerce y Merchant Center no pueden
contar historias distintas.
```

---

## Schema y Google Business Profile

LocalBusiness debe coincidir con:

- GBP;
- web;
- NAP;
- horarios;
- telefono;
- URL;
- direccion/area de servicio.

Si cambia el negocio local, se actualiza:

```text
GBP + web + schema
```

---

## Schema para IA / AEO / LLMs

Schema no garantiza aparicion en respuestas de IA.

Pero ayuda a clarificar:

- entidades;
- organizacion;
- productos;
- negocio local;
- autor;
- breadcrumbs;
- politicas;
- contenido estructurado.

Regla:

```text
Para IA, Schema debe reforzar claridad, no sustituir contenido util.
```

Una pagina con Organization schema pero texto generico sigue siendo debil.

---

## Como decidir que schema usar

Preguntar:

```text
Que tipo de pagina es?
Que contenido visible tiene?
Que entidad principal representa?
Que rich result podria aplicar?
Que fuente genera el dato?
Como se mantendra actualizado?
```

Regla:

```text
Si no puedes explicar por que esa pagina necesita ese schema, no lo implementes.
```

---

## Auditoria Schema

Proceso:

```text
1. Rastrear web con Screaming Frog o herramienta similar
2. Detectar paginas con schema
3. Detectar paginas sin schema importante
4. Identificar tipos
5. Identificar fuente
6. Validar errores
7. Revisar duplicados
8. Comparar con contenido visible
9. Revisar Search Console
10. Priorizar correcciones
```

Prioridad alta:

- schema contradice pagina;
- producto sin precio/stock correcto;
- LocalBusiness con NAP incorrecto;
- schema duplicado;
- errores en plantillas masivas;
- schema perdido en migracion.

Prioridad baja:

- schema decorativo;
- schema sin impacto claro;
- warnings menores que no afectan claridad.

---

## Schema en migraciones

En migraciones, Schema puede perderse.

Revisar:

- tipos de schema antes/despues;
- fuente del schema;
- Product;
- BreadcrumbList;
- LocalBusiness;
- Organization;
- FAQ si aplica;
- imagenes accesibles;
- URLs correctas;
- canonicals coherentes.

Regla:

```text
En una migracion, el schema debe sobrevivir o mejorar.
```

---

## Errores criticos

- schema contradice pagina;
- schema de producto sin precio;
- schema de producto con stock incorrecto;
- reseñas falsas;
- FAQ ocultas solo en schema;
- duplicados contradictorios;
- schema obsoleto;
- canonical y schema apuntan a entidades distintas;
- usar GTM para schema sin razon clara;
- no revisar Search Console despues de publicar.

---

## Protocolo Schema para web nueva

```text
1. Definir tipos de pagina
2. Asignar schema por plantilla
3. Definir fuente de datos
4. Implementar JSON-LD
5. Validar en Rich Results Test
6. Validar en Schema.org Validator
7. Revisar que coincide con contenido visible
8. Publicar
9. Revisar Search Console
10. Documentar fuente y mantenimiento
```

## Protocolo Schema para web existente

```text
1. Auditar schema actual
2. Identificar fuente
3. Revisar errores
4. Revisar duplicados
5. Revisar contenido visible
6. Revisar Merchant/GBP si aplica
7. Priorizar correcciones
8. Corregir fuente principal
9. Validar
10. Publicar
11. Revisar Search Console
12. Documentar
```

---

## Plantilla interna de auditoria Schema

```text
Cliente:
Dominio:
Fecha:
Responsable:

1. URL
- URL:
- Tipo de pagina:
- Intencion:

2. Fuente del schema
- Tema:
- Plugin SEO:
- Plugin schema:
- WooCommerce:
- Manual:
- GTM:

3. Schema detectado
- Tipo:
- Errores:
- Warnings:
- Duplicados:

4. Coherencia
- Coincide con contenido visible:
- Coincide con GBP:
- Coincide con Merchant Center:
- Coincide con canonical:

5. Accion
- Mantener:
- Corregir:
- Eliminar:
- Añadir:
- Prioridad:
- Responsable:
- Fecha de revision:
```

---

## Regla final para relevo

Schema no se implementa para decorar una web.

```text
Se implementa para explicar con precision entidades, contenido, productos,
negocio, rutas y politicas.
```

Cada trabajo con schema debe responder:

```text
Que pagina estoy marcando.
Que schema corresponde.
Que contenido visible lo respalda.
Que herramienta lo valida.
Que fuente lo genera.
Si hay duplicados.
Si coincide con GBP o Merchant Center.
Como se mantendra actualizado.
```

Si una persona dice "ya puse schema", todavia no entendio datos estructurados.
