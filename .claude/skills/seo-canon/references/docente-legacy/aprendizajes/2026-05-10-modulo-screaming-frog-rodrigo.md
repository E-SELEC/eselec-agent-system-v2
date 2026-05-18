# Modulo Screaming Frog SEO Spider - Rodrigo

- Fecha: 2026-05-10
- Estado: aprendido / pendiente de verificacion viva de fuentes
- Fuente: `agents/docente/seo/fuentes/2026-05-10-manual-seo-post-neuronwriter.md`
- Alcance: laboratorio del Docente SEO
- Restriccion: no modifica `agents/seo/`

---

## Idea central

Screaming Frog SEO Spider es una herramienta de rastreo tecnico SEO.

La idea simple:

```text
Screaming Frog no decide la estrategia.
Screaming Frog muestra como esta construida y conectada una web por dentro.
```

No se usa para sacar una lista de errores. Se usa para entender estructura,
indexabilidad, arquitectura, enlaces internos, problemas tecnicos y riesgos.

---

## Lugar en el sistema

```text
SEMrush -> investiga mercado, competencia, keywords y oportunidades.
GSC -> muestra como Google ve y muestra la web.
GA4 -> mide comportamiento y conversion.
GTM -> implementa medicion.
NEURONwriter -> optimiza contenido.
Screaming Frog -> rastrea y diagnostica la web por dentro.
```

Screaming Frog conecta con:

- SEO tecnico;
- arquitectura;
- indexacion;
- rastreo;
- redirecciones;
- canonicals;
- directivas;
- JavaScript SEO;
- enlazado interno;
- imagenes;
- sitemaps;
- hreflang;
- structured data;
- integraciones con GSC, GA4 y PageSpeed.

---

## Web nueva vs web existente

### Web nueva

Se usa antes de publicar y justo despues del lanzamiento.

Flujo:

```text
1. Rastrear staging
2. Revisar URLs finales
3. Revisar codigos 200/3XX/4XX/5XX
4. Revisar noindex accidental
5. Revisar canonicals
6. Revisar titles/metas/H1/H2
7. Revisar enlaces internos
8. Revisar sitemap
9. Revisar robots
10. Revisar imagenes/ALT
11. Revisar schema
12. Revisar Core Web Vitals via PageSpeed API
13. Publicar
14. Rastrear produccion
```

Mentalidad:

```text
En web nueva, Screaming Frog sirve para evitar publicar errores tecnicos.
```

### Web existente

Se usa para diagnosticar estructura real, errores, duplicados, redirecciones,
paginas huerfanas y activos sensibles.

Flujo:

```text
1. Definir alcance
2. Elegir modo spider o list
3. Configurar user-agent
4. Decidir si respetar robots
5. Activar JavaScript rendering si aplica
6. Conectar GSC
7. Conectar GA4
8. Conectar PageSpeed
9. Ejecutar crawl
10. Exportar issues
11. Cruzar con trafico/conversion
12. Priorizar por impacto
```

Mentalidad:

```text
En web existente, Screaming Frog sirve para entender que hay, que esta roto y
que no se debe tocar sin cuidado.
```

---

## Modos de rastreo

Spider Mode:

```text
Rastrea una web desde una URL inicial siguiendo enlaces internos.
```

List Mode:

```text
Rastrea una lista concreta de URLs.
```

Uso de List Mode:

- validar URLs de una migracion;
- revisar URLs exportadas de GSC;
- revisar URLs con backlinks;
- comprobar estados de sitemap;
- comprobar redirecciones.

---

## Configuracion inicial de crawl

Antes de rastrear, definir:

- dominio;
- subdominio;
- protocolo correcto HTTP/HTTPS;
- user-agent;
- robots;
- velocidad;
- JavaScript rendering;
- limites;
- include/exclude;
- integraciones.

Regla:

```text
No se interpreta un crawl sin saber con que configuracion se hizo.
```

---

## Tabs principales

El equipo debe dominar:

- Internal;
- External;
- Response Codes;
- Page Titles;
- Meta Description;
- H1;
- H2;
- Images;
- Canonicals;
- Directives;
- Hreflang;
- Structured Data;
- JavaScript;
- Links;
- PageSpeed;
- Search Console;
- Analytics.

---

## Response Codes

Codigos clave:

- 200: OK;
- 301: redireccion permanente;
- 302: redireccion temporal;
- 404: no encontrada;
- 500: error servidor.

Proceso para 404:

```text
1. Filtrar 4XX.
2. Ver URL afectada.
3. Revisar Inlinks.
4. Ver desde donde se enlaza.
5. Corregir enlace interno o redirigir si tiene valor.
```

Redirecciones:

- detectar cadenas;
- detectar bucles;
- validar mapa de migracion;
- revisar que las paginas importantes no pasen por saltos innecesarios.

---

## On-page tecnico

Revisar en masa:

- titles ausentes;
- titles duplicados;
- titles demasiado largos/cortos;
- metas ausentes;
- metas duplicadas;
- H1 ausentes;
- H1 duplicados;
- H2;
- contenido bajo;
- duplicados.

Regla:

```text
Screaming Frog detecta el problema tecnico; el SEO decide si importa y que se
hace con el.
```

---

## Canonicals y directivas

Revisar:

- canonical ausente;
- canonical hacia otra URL;
- canonical no indexable;
- canonical roto;
- canonical incoherente con sitemap;
- noindex accidental;
- nofollow;
- bloqueos robots;
- X-Robots-Tag.

Riesgo:

```text
Una URL importante con noindex o canonical incorrecta es prioridad alta.
```

---

## Enlazado interno y arquitectura

Screaming Frog ayuda a revisar:

- profundidad de clics;
- paginas huerfanas;
- inlinks;
- outlinks;
- anchors;
- paginas importantes poco enlazadas;
- enlaces rotos internos;
- arquitectura real frente a arquitectura deseada.

Regla:

```text
Una pagina estrategica no debe quedar escondida ni huerfana.
```

---

## Imagenes, JavaScript y structured data

Imagenes:

- peso;
- ALT;
- dimensiones;
- URLs rotas;
- formato.

JavaScript:

- activar renderizado cuando el contenido depende de JS;
- comparar HTML sin renderizar vs renderizado;
- revisar contenido visible para Google.

Structured Data:

- detectar presencia;
- revisar errores;
- validar tipos;
- comprobar coherencia con contenido visible.

---

## Integraciones

### GSC

Permite cruzar URLs con clics, impresiones, CTR y posicion.

Uso:

```text
Detectar problemas tecnicos en URLs que ya tienen valor real.
```

### GA4

Permite cruzar URLs con usuarios, sesiones, engagement y conversiones.

Uso:

```text
Priorizar errores en paginas con trafico o negocio.
```

### PageSpeed

Permite traer datos de rendimiento y Core Web Vitals por URL.

Uso:

```text
Priorizar problemas por plantilla, trafico y conversion.
```

---

## Paginas huerfanas y fuentes cruzadas

Una pagina huerfana puede no estar enlazada internamente, pero aparecer en:

- sitemap;
- GSC;
- GA4;
- backlinks;
- listas antiguas.

Screaming Frog ayuda a detectarlas cruzando fuentes.

Regla:

```text
Una pagina huerfana con trafico, backlinks o conversion no se elimina sin
analisis.
```

---

## Custom Search y Custom Extraction

Custom Search sirve para encontrar elementos:

- GTM;
- GA4;
- textos legales;
- bloques concretos;
- shortcodes;
- etiquetas;
- contenido duplicado.

Custom Extraction sirve para extraer datos especificos:

- schema;
- precios;
- breadcrumbs;
- elementos HTML;
- datos de producto;
- patrones internos.

---

## Migraciones SEO

En una migracion, Screaming Frog es obligatorio.

Antes:

```text
1. Crawl completo de la web antigua.
2. Exportar URLs indexables.
3. Exportar URLs con trafico desde GSC/GA4.
4. Exportar URLs con backlinks.
5. Crear mapa de redirecciones.
6. Revisar canonicals.
7. Revisar sitemaps.
```

Staging:

```text
1. Rastrear staging.
2. Revisar noindex.
3. Revisar canonicals.
4. Revisar enlaces internos.
5. Revisar URLs finales.
6. Revisar redirecciones previstas.
```

Despues:

```text
1. Crawl produccion.
2. Revisar 404.
3. Revisar 301.
4. Revisar cadenas.
5. Revisar canonicals.
6. Revisar sitemap.
7. Revisar GSC.
```

---

## Convertir crawl en tareas

No entregar "300 errores".

Entregar:

```text
Problema:
URLs afectadas:
Tipo:
Impacto:
Datos cruzados:
Prioridad:
Responsable:
Accion:
Validacion:
```

Priorizacion:

1. errores que impiden rastreo/indexacion;
2. errores en URLs con trafico/conversion/backlinks;
3. errores masivos de plantilla;
4. mejoras on-page con oportunidad;
5. detalles menores.

---

## Regla final para relevo

Screaming Frog no se usa para sacar errores.

```text
Se usa para entender como esta construida una web y decidir que corregir primero.
```

Cada crawl debe poder responder:

```text
Que rastree.
Con que configuracion.
Cuantas URLs encontre.
Que problemas criticos hay.
Que URLs estrategicas estan afectadas.
Que errores son tecnicos.
Que errores son de contenido.
Que errores son de arquitectura.
Que se debe corregir primero.
Quien debe corregirlo.
Cuando se validara.
```

Si una persona dice "saque un crawl y hay 300 errores", todavia no esta
haciendo auditoria SEO.
