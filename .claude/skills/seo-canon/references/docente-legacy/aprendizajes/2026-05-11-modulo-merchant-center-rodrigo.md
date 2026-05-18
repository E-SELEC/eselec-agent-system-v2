# Modulo Google Merchant Center - Rodrigo

- Fecha: 2026-05-11
- Estado: aprendido / pendiente de verificacion viva de fuentes oficiales
- Fuente: `agents/docente/seo/fuentes/2026-05-11-manual-seo-migraciones-schema-merchant.md`
- Alcance: laboratorio del Docente SEO
- Restriccion: no modifica `agents/seo/`

---

## Idea central

Google Merchant Center es la herramienta de Google para subir, gestionar y
revisar datos de producto.

No es solo para anuncios.

```text
Merchant Center no es solo Ads.
Merchant Center es infraestructura de producto para Google.
```

Regla:

```text
Merchant Center debe coincidir con la web.
```

Si el ecommerce esta mal organizado, Merchant Center lo va a evidenciar.

---

## Lugar en el sistema SEO

Merchant Center conecta con:

- SEO ecommerce;
- Shopping organico / free listings;
- Shopping Ads si aplica;
- Performance Max si aplica;
- productos;
- categorias;
- WooCommerce;
- schema Product;
- feeds;
- stock;
- precios;
- imagenes;
- politicas de envio;
- politicas de devolucion;
- GA4 ecommerce;
- Merchant diagnostics;
- Search Console y Looker Studio si se reporta.

---

## Ecommerce nuevo vs existente

### Ecommerce nuevo

Merchant Center se configura despues de tener productos reales, URLs finales,
precios, stock, politicas, imagenes y checkout funcional.

Flujo:

```text
1. Confirmar ecommerce funcional
2. Confirmar productos reales
3. Confirmar categorias
4. Confirmar precios
5. Confirmar stock
6. Crear cuenta Merchant Center
7. Verificar web
8. Configurar metodo de feed
9. Subir productos
10. Configurar envio
11. Configurar devoluciones
12. Revisar politicas
13. Corregir errores
14. Revisar fichas visibles
15. Revisar schema Product
16. Revisar GA4 ecommerce
17. Medir
```

Regla:

```text
Merchant Center no se configura antes de tener catalogo limpio.
```

### Ecommerce existente

Primero se audita.

Flujo:

```text
1. Revisar acceso
2. Revisar cuenta Merchant Center
3. Revisar dominio verificado
4. Revisar metodos de feed
5. Revisar productos activos
6. Revisar productos rechazados
7. Revisar diagnosticos
8. Revisar precios
9. Revisar stock
10. Revisar imagenes
11. Revisar envio
12. Revisar devoluciones
13. Revisar politicas
14. Cruzar con WooCommerce
15. Cruzar con web visible
16. Revisar schema
17. Priorizar correcciones
```

---

## Que NO es Merchant Center

Merchant Center no es:

- sustituto de WooCommerce;
- sustituto de schema Product;
- solucion para catalogo desordenado;
- solo herramienta de Ads;
- lugar para inventar disponibilidad;
- lugar para corregir manualmente algo que el feed sobrescribe;
- sistema que se configura una vez y se olvida.

Regla:

```text
Merchant Center amplifica la calidad o el desorden del catalogo.
```

---

## Datos de producto

Un producto en Merchant Center es tan bueno como los datos que lo describen.

Datos clave:

- id;
- title;
- description;
- link;
- image_link;
- price;
- availability;
- brand;
- gtin/mpn si aplica;
- condition;
- product_type;
- google_product_category;
- shipping;
- returns;
- item_group_id para variaciones.

Regla:

```text
Stock, precio y disponibilidad deben coincidir en WooCommerce, ficha visible,
schema y feed.
```

---

## Feed y metodos de envio

Merchant Center puede recibir datos mediante:

- hoja de calculo;
- feed programado;
- Content API;
- integracion WooCommerce;
- plugin;
- feed manual;
- automatizaciones.

Criterio:

```text
El equipo debe saber de donde viene el dato antes de corregirlo.
```

Error tipico:

```text
Editar producto directamente en Merchant Center cuando el error viene del feed.
```

Si el feed sobrescribe, la correccion debe hacerse en la fuente.

---

## Diagnosticos

Merchant Center muestra productos con problemas.

Proceso:

```text
1. Entrar en Merchant Center.
2. Revisar diagnosticos.
3. Clasificar problemas.
4. Identificar fuente del dato.
5. Comparar con ficha visible.
6. Comparar con schema Product.
7. Corregir en fuente correcta.
8. Solicitar/revisar revalidacion si aplica.
```

No corregir a ciegas.

---

## Precio, stock y disponibilidad

Riesgos:

- precio en feed distinto al visible;
- disponibilidad en feed distinta a web;
- schema dice InStock y web dice agotado;
- variantes con stock incorrecto;
- descuentos mal formateados;
- moneda incorrecta.

Regla:

```text
La informacion comercial debe ser identica en web, WooCommerce, schema y
Merchant Center.
```

---

## Envio, devoluciones y politicas

Merchant Center requiere datos claros de envio y devolucion.

Revisar:

- costes de envio;
- tiempos;
- paises;
- devoluciones;
- politica visible en web;
- consistencia con datos estructurados si se usan;
- consistencia con checkout.

Regla:

```text
No se declara una politica en Merchant Center que la web no respalde claramente.
```

---

## Merchant Center y WooCommerce

Merchant Center debe sincronizarse con WooCommerce.

Revisar:

- plugin/feed usado;
- productos incluidos;
- productos excluidos;
- categorias;
- atributos;
- variaciones;
- stock;
- precios;
- imagenes;
- schema Product;
- errores de feed.

Regla:

```text
WooCommerce es fuente operativa. Merchant Center debe reflejarla correctamente.
```

---

## Merchant Center y Schema Product

Merchant Center puede usar datos de landing y structured data para validar o
actualizar informacion.

Comparar:

```text
Web visible:
Schema Product:
Feed:
Merchant Center:
WooCommerce:
```

Error grave:

```text
Schema dice InStock, Merchant dice out_of_stock y la web muestra disponible.
```

---

## Merchant Center y GA4 ecommerce

Merchant Center muestra productos en Google.
GA4 mide que pasa despues en la web.

Revisar:

- sesiones desde Shopping/free listings si se identifican;
- view_item;
- add_to_cart;
- begin_checkout;
- purchase;
- revenue;
- productos que reciben trafico pero no venden.

Regla:

```text
No basta con que Merchant Center apruebe productos. Hay que medir si generan valor.
```

---

## Merchant Center y Google Ads

Puede vincularse con Google Ads para Shopping Ads y Performance Max.

Pero para el Docente SEO:

```text
Merchant Center debe entenderse primero como calidad de datos de producto.
Ads es una capa posterior.
```

---

## Categorias, productos agotados y restricciones

Categorias:

- deben estar bien organizadas;
- deben mapearse a product_type y/o google_product_category si aplica;
- deben coincidir con estructura ecommerce.

Productos agotados:

- stock real;
- disponibilidad correcta;
- alternativas si aplica;
- no mandar informacion falsa.

Productos restringidos:

- revisar politicas;
- no forzar productos que incumplen;
- documentar restricciones.

---

## Titulos, descripciones e imagenes

Titulo de feed:

- claro;
- con producto real;
- atributos relevantes;
- sin relleno engañoso;
- distinto al title SEO si hace falta, pero coherente.

Descripcion:

- precisa;
- util;
- alineada con ficha visible;
- sin claims falsos.

Imagenes:

- calidad suficiente;
- producto claro;
- no imagen rota;
- no placeholder;
- coincidir con producto.

---

## Rutas de correccion

Antes de corregir, identificar fuente:

- WooCommerce;
- plugin/feed;
- schema;
- Merchant Center;
- politica web;
- checkout;
- imagen;
- atributo.

Regla:

```text
No corrijas en Merchant Center lo que se va a sobrescribir desde el feed.
```

Si el error viene de schema, se corrige schema.
Si viene de WooCommerce, se corrige WooCommerce.
Si viene de politica visible, se corrige la pagina/politica.

---

## Automatizaciones y reglas de atributos

Las automatizaciones pueden ayudar, pero no sustituyen catalogo limpio.

Reglas de atributos:

- modifican o completan datos segun reglas;
- pueden solucionar patrones;
- tambien pueden ocultar problemas de origen.

Regla:

```text
Una regla de atributo debe documentarse y tener motivo claro.
```

---

## Search Console, Looker Studio y migraciones

Search Console y Merchant Center son distintas:

- GSC muestra rendimiento en Google Search;
- Merchant Center muestra si Google acepta y usa datos comerciales del producto.

Looker Studio:

- Merchant Center debe entrar en reporting ecommerce si hay datos/conector/export;
- no debe quedar aislado.

Migraciones ecommerce:

```text
1. Revisar feed antes
2. Revisar URLs de producto
3. Revisar schema Product
4. Revisar Merchant Center
5. Lanzar
6. Revalidar productos
7. Revisar rechazos
8. Revisar GA4 ecommerce
```

Error:

```text
Merchant Center sigue enviando usuarios a URLs antiguas o productos rotos.
```

---

## Rutinas

Semanal:

```text
1. Revisar diagnosticos
2. Revisar productos rechazados
3. Revisar precio/stock
4. Revisar alertas
5. Revisar feed
6. Revisar productos importantes
7. Priorizar correcciones
```

Mensual:

```text
1. Revisar salud de cuenta
2. Revisar productos activos
3. Revisar categorias
4. Revisar politicas
5. Revisar datos frente a WooCommerce
6. Revisar schema Product
7. Revisar GA4 ecommerce
8. Revisar acciones de mejora
```

---

## Plantilla interna de auditoria Merchant Center

```text
Cliente:
Dominio:
Fecha:
Responsable:
Merchant Center ID:

1. Cuenta
- Acceso:
- Dominio verificado:
- Estado:

2. Feed
- Metodo:
- Fuente:
- Frecuencia:
- Errores:

3. Productos
- Activos:
- Rechazados:
- Con advertencias:
- Prioritarios:

4. Datos comerciales
- Precio:
- Stock:
- Disponibilidad:
- Moneda:
- Imagenes:

5. Politicas
- Envio:
- Devoluciones:
- Restricciones:
- Visible en web:

6. WooCommerce
- Fuente de datos:
- Plugin:
- Categorias:
- Variaciones:

7. Schema
- Product schema:
- Coincide con feed:
- Errores:

8. Medicion
- GA4 ecommerce:
- Eventos:
- Revenue:

9. Acciones
- Problema:
- Fuente:
- Correccion:
- Responsable:
- Prioridad:
- Fecha de revision:
```

---

## Errores comunes

1. Pensar que Merchant Center solo sirve para Ads.
2. Subir productos con catalogo desordenado.
3. No revisar diagnosticos.
4. Corregir en Merchant lo que sobrescribe el feed.
5. Precio distinto entre web y feed.
6. Stock distinto entre web, schema y Merchant.
7. Imagenes malas o rotas.
8. Politicas no visibles en web.
9. No revisar productos rechazados.
10. No conectar con WooCommerce.
11. No revisar variaciones.
12. No revisar productos agotados.
13. No medir GA4 ecommerce.
14. No revisar despues de migracion.
15. No documentar reglas de atributos.
16. No revisar schema Product.

---

## Regla final para relevo

Merchant Center no se usa para subir productos.

```text
Se usa para asegurar que Google recibe datos comerciales correctos, consistentes
y utiles sobre productos reales.
```

Cada trabajo debe poder responder:

```text
Que productos revise.
De donde viene el feed.
Que errores hay.
Que fuente causa el error.
Si precio coincide.
Si stock coincide.
Si schema Product coincide.
Si WooCommerce coincide.
Que politica respalda el dato.
Que correccion toca.
Como se medira despues.
```

Si una persona dice "ya subi el feed", todavia no entendio Merchant Center.
