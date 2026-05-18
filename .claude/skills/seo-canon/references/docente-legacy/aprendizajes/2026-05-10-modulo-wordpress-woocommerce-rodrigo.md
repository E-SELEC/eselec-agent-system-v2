# Modulo WordPress / WooCommerce SEO - Rodrigo

- Fecha: 2026-05-10
- Estado: aprendido / pendiente de verificacion viva de fuentes
- Fuente: `agents/docente/seo/fuentes/2026-05-10-manual-seo-post-neuronwriter.md`
- Alcance: laboratorio del Docente SEO
- Restriccion: no modifica `agents/seo/`

---

## Idea central

Este modulo es de implementacion real.

WordPress es el CMS. WooCommerce es la capa ecommerce.

```text
El SEO define que debe hacerse.
WordPress/WooCommerce es donde muchas de esas decisiones se implementan.
```

Riesgo:

```text
El error no suele ser no saber SEO.
El error suele ser saber que hay que hacer, pero tocar mal el CMS.
```

WordPress y WooCommerce pueden romper:

- URLs;
- categorias;
- etiquetas;
- canonicals;
- plugins;
- indexacion;
- productos;
- checkout;
- medicion;
- rendimiento.

---

## WordPress dentro del marco SEO

WordPress afecta a:

- arquitectura;
- paginas;
- entradas;
- categorias;
- etiquetas;
- menus;
- breadcrumbs;
- slugs;
- titles/metas;
- H1/H2;
- imagenes;
- ALT;
- sitemap;
- robots/noindex;
- redirecciones;
- plugins;
- schema;
- velocidad;
- formularios;
- tracking.

Regla:

```text
No se toca WordPress sin saber que parte del SEO afecta.
```

---

## WooCommerce dentro del marco SEO

WooCommerce afecta a:

- categorias de producto;
- fichas de producto;
- atributos;
- etiquetas;
- filtros/facetas;
- productos variables;
- productos agotados;
- schema Product;
- carrito;
- checkout;
- pasarelas;
- ecommerce tracking;
- indexacion de categorias/productos;
- ingresos organicos.

Regla:

```text
WooCommerce no es solo catalogo. Es arquitectura SEO + conversion + medicion.
```

---

## Web nueva vs web existente

### Web nueva + WordPress SEO

```text
1. Definir arquitectura SEO
2. Definir permalinks
3. Crear paginas principales
4. Configurar plugin SEO
5. Configurar sitemap
6. Configurar indexacion
7. Crear menus
8. Crear breadcrumbs
9. Optimizar titles/metas/H1
10. Optimizar imagenes
11. Instalar GTM/GA4
12. Validar formularios
13. Rastrear con Screaming Frog
14. Enviar sitemap a GSC
15. Medir
```

### Web existente + WordPress SEO

```text
1. Backup
2. Confirmar entorno
3. Auditar plugins
4. Crawl Screaming Frog
5. Revisar GSC
6. Revisar GA4
7. Revisar URLs con valor
8. Revisar indexacion
9. Revisar permalinks/slugs
10. Revisar categorias/etiquetas
11. Revisar redirecciones
12. Revisar rendimiento
13. Priorizar cambios
14. Ejecutar con control
15. Validar
```

### Ecommerce nuevo + WooCommerce SEO

```text
1. Definir categorias
2. Definir atributos
3. Definir productos
4. Configurar URLs
5. Configurar plugin SEO
6. Configurar schema
7. Configurar imagenes
8. Configurar categorias indexables
9. Optimizar descripciones
10. Configurar productos relacionados
11. Revisar carrito/checkout
12. Configurar GA4 ecommerce
13. Configurar Merchant Center, si aplica
14. Rastrear tienda
15. Medir ventas
```

### Ecommerce existente + WooCommerce SEO

```text
1. Backup
2. Crawl completo
3. Revisar categorias con trafico
4. Revisar productos con trafico
5. Revisar productos con ventas
6. Revisar productos agotados
7. Revisar duplicados
8. Revisar filtros/parametros
9. Revisar canonicals
10. Revisar schema Product
11. Revisar imagenes
12. Revisar checkout
13. Revisar ecommerce tracking
14. Priorizar categorias/productos
15. Ejecutar mejoras
16. Medir ingresos organicos
```

---

## Accesos y seguridad

Antes de tocar:

```text
1. Confirmar entorno: produccion o staging.
2. Hacer backup si el cambio es relevante.
3. Confirmar rol del usuario.
4. Confirmar que se va a tocar.
5. Documentar cambio.
6. Ejecutar.
7. Revisar.
8. Registrar resultado.
```

Regla:

```text
No se cambia produccion como si fuera un borrador.
```

---

## Permalinks y slugs

Permalinks:

- definen estructura base de URLs;
- pueden afectar toda la web;
- no se cambian sin plan de redirecciones.

Slugs:

- deben ser claros;
- deben ser estables;
- deben reflejar intencion;
- no se cambian por estetica si la URL tiene valor.

Regla:

```text
Cambiar una URL existente es una accion de riesgo SEO.
```

---

## Paginas, entradas, categorias y etiquetas

Paginas:

- servicios;
- landings;
- contacto;
- home;
- paginas comerciales.

Entradas:

- blog;
- guias;
- recursos;
- contenido informacional.

Categorias:

- organizan contenido;
- pueden ser indexables si tienen valor.

Etiquetas:

- suelen generar thin content si se usan sin criterio;
- no deben indexarse automaticamente sin estrategia.

Error comun:

```text
Indexar etiquetas y archivos sin valor, generando contenido pobre o duplicado.
```

---

## Menus, breadcrumbs y arquitectura

Menus:

- reflejan jerarquia;
- deben enlazar paginas clave;
- no deben esconder servicios importantes.

Breadcrumbs:

- ayudan a usuario y buscador;
- refuerzan jerarquia;
- deben ser coherentes con arquitectura.

Regla:

```text
El menu no es solo diseño. Es distribucion de autoridad y claridad.
```

---

## Plugin SEO, indexacion y sitemap

Plugin SEO:

- titles;
- metas;
- canonicals;
- sitemap;
- schema;
- breadcrumbs;
- robots/noindex.

No confiar en defaults sin revisar.

Indexacion:

- revisar noindex global;
- revisar plantillas;
- revisar categorias;
- revisar etiquetas;
- revisar archivos autor/fecha;
- revisar productos/categorias.

Sitemap:

- debe incluir URLs indexables importantes;
- no debe incluir noindex, 404 o redirecciones innecesarias.

---

## Redirecciones, imagenes y rendimiento

Redirecciones:

- necesarias al cambiar slugs;
- deben ser 301 si el cambio es permanente;
- evitar cadenas y bucles.

Imagenes:

- nombre descriptivo;
- ALT natural;
- peso optimizado;
- dimensiones;
- formatos adecuados.

Rendimiento:

- cache;
- plugins;
- builder;
- imagenes;
- scripts;
- hosting;
- Core Web Vitals.

Regla:

```text
Cada plugin puede ayudar, pero tambien puede añadir peso, conflicto o riesgo.
```

---

## Builders y formularios

Builders como Elementor, Gutenberg o Divi pueden afectar:

- HTML;
- headings;
- velocidad;
- responsive;
- shortcodes;
- renderizado;
- CTAs;
- formularios.

Formularios:

- deben funcionar;
- deben medir `form_submit`;
- deben confirmar recepcion;
- deben evitar friccion innecesaria;
- deben validarse en desktop y movil.

---

## WooCommerce: categorias, productos y atributos

Categorias de producto:

- pueden captar demanda SEO;
- deben tener texto util;
- deben enlazar productos;
- deben evitar duplicados;
- deben tener title/meta/H1 claros.

Productos:

- nombre;
- descripcion corta;
- descripcion larga;
- imagenes;
- precio;
- stock;
- schema;
- productos relacionados;
- opiniones si aplica.

Atributos:

- utiles para filtros;
- peligrosos si generan muchas URLs indexables sin valor.

Filtros/facetas:

- controlar indexacion;
- evitar duplicados;
- revisar canonicals;
- definir que combinaciones merecen indexarse.

---

## Productos agotados y duplicados

Producto agotado:

- mantener si volvera;
- ofrecer alternativa;
- no eliminar si tiene trafico/backlinks;
- redirigir solo si no volvera y hay equivalente.

Duplicados:

- variantes mal creadas;
- productos similares;
- categorias repetidas;
- descripciones copiadas.

Regla:

```text
No se elimina producto con trafico, ventas o backlinks sin analisis.
```

---

## Carrito, checkout y medicion

Carrito, checkout y cuenta no suelen ser URLs SEO, pero afectan negocio.

Revisar:

- friccion;
- errores;
- pasarela;
- tiempos;
- confianza;
- medicion ecommerce;
- eventos `begin_checkout` y `purchase`.

Regla:

```text
SEO ecommerce no termina en trafico. Termina en ingresos medidos.
```

---

## Plantilla interna de auditoria

```text
Cliente:
Dominio:
Fecha:
Responsable:
CMS:
Tema:
Builder:
Plugin SEO:
WooCommerce: si/no

1. Accesos y seguridad
- Rol:
- Backup:
- Staging:
- Usuarios:

2. Permalinks
- Estructura actual:
- Riesgos:
- Cambios propuestos:

3. Indexacion
- Noindex global:
- Paginas noindex:
- Categorias indexables:
- Etiquetas indexables:
- Archivos autor/fecha:

4. Sitemap
- URL:
- Tipos incluidos:
- Errores:
- Enviado a GSC:

5. Arquitectura
- Menu:
- Paginas principales:
- Categorias:
- Blog:
- Breadcrumbs:

6. On-Page
- Titles:
- Metas:
- H1:
- H2:
- Contenido:
- Imagenes/ALT:

7. Plugins
- SEO:
- Cache:
- Builder:
- Redirecciones:
- Schema:
- Conflictos:

8. WooCommerce
- Categorias:
- Productos:
- Atributos:
- Filtros:
- Checkout:
- Tracking:

9. Medicion
- GTM:
- GA4:
- GSC:
- Eventos:

10. Prioridades
- Urgente:
- Importante:
- Rutinario:
```

---

## Errores comunes

1. Cambiar permalinks sin redirecciones.
2. Cambiar slugs con trafico sin revisar GSC.
3. Indexar etiquetas sin valor.
4. Borrar productos con backlinks.
5. Instalar plugins sin medir impacto.
6. Usar builders rompiendo headings.
7. Publicar sin revisar mobile.
8. No medir formularios.
9. No medir ecommerce.
10. Cambiar categorias sin revisar arquitectura.
11. No hacer backup antes de cambios sensibles.
12. Tocar produccion sin staging cuando el cambio lo requiere.

---

## Regla final para relevo

WordPress/WooCommerce no se toca como editor visual.

```text
Se toca como sistema donde cada cambio puede afectar SEO, conversion, medicion
o ventas.
```

Cada cambio debe poder responder:

```text
Que URL toque.
Que intencion afecta.
Si cambia slug.
Si afecta indexacion.
Si afecta sitemap.
Si afecta medicion.
Como lo voy a validar.
Donde queda documentado.
```

Si una persona dice "ya cambie la pagina", todavia no trabaja profesionalmente.
