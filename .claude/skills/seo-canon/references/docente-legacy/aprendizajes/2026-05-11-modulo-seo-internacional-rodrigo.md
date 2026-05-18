# Modulo SEO Internacional - Aprendizaje del Docente

- Fecha: 2026-05-11
- Origen: `Manual_SEO_Priorizacion_IA_Internacional_Roles_EXACTO.pdf`
- Estado: aprendido / pendiente de convertir en ejercicios

---

## Que debe aprender el Docente

El SEO internacional optimiza una web para posicionar correctamente en diferentes paises, idiomas o regiones, mostrando a cada usuario la version mas adecuada segun idioma, ubicacion, intencion y mercado.

Regla principal:

```text
SEO internacional no es traducir una web.
Es adaptar arquitectura, URLs, contenido, medicion, autoridad,
experiencia y senales tecnicas a cada mercado real.
```

---

## Multilingue vs multirregional

El equipo debe distinguir:

```text
Multilingue:
contenido en mas de un idioma.

Multirregional:
contenido orientado a diferentes paises o regiones.

Mixto:
contenido en varios idiomas y tambien adaptado por pais.
```

Ejemplos:

```text
/es/        espanol general
/en/        ingles general
/es-es/     espanol para Espana
/es-mx/     espanol para Mexico
/en-us/     ingles para Estados Unidos
/en-gb/     ingles para Reino Unido
```

---

## Arquitectura internacional

Opciones comunes:

```text
ccTLD:
dominio.es, dominio.mx, dominio.fr

subdominio:
es.dominio.com, mx.dominio.com

subcarpeta:
dominio.com/es/, dominio.com/mx/
```

El Docente no debe ensenar una opcion universal.

La decision depende de:

```text
mercado
presupuesto
autoridad
capacidad tecnica
CMS
equipo local
contenido disponible
necesidad legal o comercial
mantenimiento
```

---

## Hreflang

Hreflang ayuda a Google a entender versiones alternativas por idioma o region.

Reglas que el equipo debe memorizar:

```text
usar codigos validos de idioma y pais
cada version debe apuntar a sus equivalentes
debe existir reciprocidad
cada version debe incluir self-reference
solo se usa en URLs reales, publicadas, indexables y equivalentes
no se mezcla con canonicals contradictorias
x-default se usa para selector global o version neutral
```

Error grave:

```text
Crear hreflang hacia paginas no indexables, redirigidas,
no equivalentes, bloqueadas o con canonical a otra version.
```

---

## Canonical y hreflang

Regla operativa:

```text
Cada version internacional indexable debe tener canonical hacia si misma,
salvo casos especiales revisados por senior.
```

No se debe canonicalizar una version regional hacia otra si se espera que ambas posicionen.

---

## Traduccion vs localizacion

El equipo debe entender esta diferencia:

```text
Traduccion:
cambia idioma.

Localizacion:
adapta vocabulario, oferta, moneda, confianza, ejemplos,
legales, CTAs, metodo de contacto, disponibilidad y SERP.
```

Ejemplo:

```text
Espana: reparacion de ordenadores
Mexico: reparacion de computadoras
```

No se decide una estrategia de Mexico con SERPs de Espana.

---

## Keyword research internacional

Cada mercado requiere:

```text
keywords locales
SERP local
competidores locales
intencion local
volumen por pais
dificultad por pais
lenguaje comercial local
conversion esperada por mercado
```

Regla:

```text
Una keyword traducida no equivale a una keyword valida.
```

---

## Indexacion y discovery

Google debe poder descubrir todas las versiones.

Evitar:

```text
redirecciones automaticas obligatorias por idioma o IP
versiones ocultas al crawler
selectores sin enlaces HTML
sitemaps incompletos
hreflang solo parcial
bloqueos en robots.txt
canonicals cruzadas incorrectas
```

Sitemaps internacionales pueden incluir hreflang si estan bien mantenidos.

---

## Ecommerce internacional

En ecommerce, traducir no basta.

Hay que revisar:

```text
moneda
precios
impuestos
envios
devoluciones
stock por pais
metodos de pago
checkout
Merchant Center
schema Product
idioma de fichas
trust local
legal local
```

Un error comercial puede afectar SEO, shopping, conversion y reputacion.

---

## Medicion internacional

El equipo debe segmentar:

```text
GSC por propiedad, pagina, pais y consulta
GA4 por pais, idioma, landing, canal y conversion
Looker Studio por mercado
Merchant Center por pais
GBP por ubicacion si aplica
```

Sin medicion separada, el equipo no sabe que mercado funciona.

---

## QA internacional

Antes de publicar:

```text
URLs correctas
idioma correcto
hreflang reciproco
canonical correcta
sitemap actualizado
robots correcto
contenido localizado
CTA local
moneda y precios correctos
schema coherente
tracking funcionando
selector de idioma usable
version movil revisada
changelog actualizado
```

---

## Errores que el Docente debe corregir

```text
Traducir sin investigar mercado.
Crear paises sin demanda real.
Usar hreflang como arreglo de duplicados.
Canonicalizar todas las versiones a una sola URL.
No usar x-default cuando aplica.
Forzar redirecciones por IP.
No segmentar GSC y GA4.
No adaptar precios, moneda, envios o confianza.
Publicar contenido traducido sin localizacion.
No revisar SERPs locales.
No documentar cambios internacionales.
```

---

## Regla final

```text
Antes de internacionalizar, el equipo debe responder:
que mercado, que idioma, que arquitectura, que URLs,
que hreflang, que canonical, que SERP, que keyword,
que contenido, que medicion, que riesgo y que responsable.
```
