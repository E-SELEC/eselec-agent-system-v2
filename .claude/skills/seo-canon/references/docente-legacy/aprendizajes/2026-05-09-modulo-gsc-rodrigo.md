# Modulo Google Search Console - Rodrigo

- Fecha: 2026-05-09
- Estado: aprendido / pendiente de verificacion viva de enlaces oficiales
- Fuente: instruccion directa de Rodrigo al Docente SEO
- Alcance: laboratorio del Docente SEO
- Restriccion: no modifica `agents/seo/`

---

## Idea central

Google Search Console es mas importante que SEMrush cuando se trabaja una web
existente porque SEMrush estima y GSC muestra datos reales de Google Search.

Regla interna:

```text
SEMrush ayuda a descubrir oportunidades.
Search Console ayuda a validar la realidad en Google.
GA4 ayuda a saber si ese trafico genera negocio.
```

GSC no es una herramienta para "hacer SEO" directamente. Es una herramienta
para diagnosticar, medir, validar y priorizar SEO con datos reales.

La frase operativa:

```text
Google Search Console no se abre para mirar numeros.
Se abre para encontrar decisiones.
```

---

## Como se conecta con el marco maestro SEO

GSC se conecta con:

1. Diagnostico SEO: rendimiento organico, consultas reales, paginas con clics,
   paginas con impresiones y oportunidades.
2. SEO tecnico: indexacion, rastreo, inspeccion de URLs, sitemaps, HTTPS y
   problemas detectados por Google.
3. SEO On-Page: CTR, queries, paginas con bajo rendimiento, titles/metas e
   intencion de busqueda real.
4. SEO de contenidos: contenidos con impresiones, contenidos sin clics,
   long-tail, caidas y contenidos que deben actualizarse.
5. SEO local: consultas locales, paginas locales, dispositivo movil, pais y
   rendimiento organico de landings locales.
6. Autoridad/enlaces: enlaces externos detectados por Google, paginas mas
   enlazadas, texto de enlace y enlaces internos.
7. CRO aplicado al SEO: paginas con trafico SEO que luego deben cruzarse con
   GA4 para saber si convierten.
8. Medicion: clics, impresiones, CTR, posicion media, indexacion y evolucion.

---

## Web nueva vs web existente

### Web nueva

En una web nueva, GSC se usa para comprobar que Google puede descubrir,
rastrear, indexar y empezar a mostrar la web.

Flujo:

```text
1. Verificar propiedad
2. Enviar sitemap
3. Inspeccionar URLs importantes
4. Solicitar indexacion de URLs clave
5. Revisar informe de indexacion
6. Revisar errores detectados por Google
7. Medir primeras impresiones
8. Detectar primeras queries
9. Optimizar snippets iniciales
10. Crear seguimiento mensual
```

Mentalidad:

```text
En web nueva no buscamos grandes conclusiones todavia.
Primero validamos que Google puede encontrar, entender e indexar.
```

### Web existente

En una web existente, GSC se usa para diagnosticar que funciona, que cae, que
tiene potencial y que esta bloqueado.

Flujo:

```text
1. Revisar rendimiento general
2. Detectar paginas con trafico
3. Detectar paginas con muchas impresiones
4. Detectar paginas con bajo CTR
5. Detectar consultas reales
6. Revisar paginas indexadas
7. Revisar paginas no indexadas
8. Inspeccionar URLs prioritarias
9. Revisar enlaces internos/externos
10. Revisar Core Web Vitals
11. Revisar acciones manuales y seguridad
12. Cruzar con GA4
13. Crear roadmap de mejoras
```

Mentalidad:

```text
En web existente no se toca nada importante sin revisar GSC.
```

---

## Configuracion inicial

Antes de analizar, hay que verificar la propiedad correctamente.

Tipos de propiedad:

- Propiedad de dominio: incluye http, https, www, sin www y subdominios.
- Propiedad de prefijo de URL: incluye solo una version concreta.

Criterio profesional:

```text
Lo ideal suele ser propiedad de dominio.
Si solo existe prefijo de URL, se trabaja con eso y se documenta la limitacion.
```

Entregable minimo:

```text
Cliente:
Dominio:
Tipo de propiedad:
Metodo de verificacion:
Fecha:
Usuario propietario:
Usuarios añadidos:
GA4 conectado:
Sitemap enviado:
Observaciones:
```

Error tipico:

```text
Verificar solo una variante de URL y asumir que se esta viendo toda la web.
```

---

## Informe de rendimiento

El informe de rendimiento es el corazon de GSC.

Metricas principales:

- Clics: entradas desde Google Search.
- Impresiones: veces que Google mostro la web.
- CTR: clics divididos entre impresiones.
- Posicion media: posicion promedio del resultado superior de la propiedad.

Criterios:

- No todos los clics valen igual; pueden ser informacionales y no generar
  negocio.
- Muchas impresiones y pocos clics pueden indicar title debil, meta floja,
  intencion mal alineada, competencia mas fuerte o una SERP con mucho ruido.
- Un CTR bajo no siempre es malo; depende de posicion, intencion, marca,
  anuncios, mapas, videos y resultados enriquecidos.
- La posicion media no es ranking exacto actual; es una media afectada por
  pais, dispositivo, fecha, personalizacion y tipo de resultado.

Proceso correcto:

```text
1. Elegir rango de fechas: 3, 6, 12 o 16 meses segun analisis.
2. Activar clics, impresiones, CTR y posicion media.
3. Revisar consultas.
4. Revisar paginas.
5. Cruzar consulta + pagina.
6. Filtrar por dispositivo.
7. Filtrar por pais.
8. Exportar datos y convertirlos en decisiones.
```

El paso profesional es cruzar consulta + URL.

Ejemplo:

```text
Consulta: seo local madrid
URL que aparece: /blog/que-es-seo-local/
URL ideal: /seo-local-madrid/

Interpretacion:
Google esta mostrando una URL informacional para una intencion posiblemente
comercial. Puede haber mala arquitectura, falta de landing comercial o
canibalizacion.
```

Entregable:

```text
Consulta | URL | Clics | Impresiones | CTR | Posicion | Intencion | Problema | Accion
```

---

## Como convertir rendimiento en acciones

### Muchas impresiones + bajo CTR

Posibles causas:

- title poco atractivo;
- meta description debil;
- intencion mal enfocada;
- competidor mas fuerte;
- falta de diferenciador;
- SERP con mapas, anuncios o respuestas directas.

Accion:

```text
1. Revisar consulta.
2. Revisar URL posicionada.
3. Buscar la consulta en Google.
4. Comparar titles competidores.
5. Mejorar title y meta.
6. Añadir propuesta de valor real.
7. Medir en 2-4 semanas.
```

### Posicion 4-15

Google ya considera relevante la URL, pero no lo suficiente para top 3.

Acciones:

- revisar contenido frente al top 3;
- mejorar profundidad;
- añadir FAQs;
- añadir ejemplos;
- añadir enlaces internos;
- mejorar title/H1;
- revisar Core Web Vitals si la pagina es lenta;
- buscar autoridad externa si la competencia tiene mucha mas autoridad.

### Muchas impresiones + posicion baja

Google prueba la pagina, pero no la considera suficientemente fuerte.

Acciones:

- validar intencion;
- revisar si rankea la URL correcta;
- mejorar contenido;
- mejorar arquitectura;
- añadir enlaces internos;
- crear URL especifica solo si la intencion no esta cubierta.

### Clics altos + sin conversion

GSC no mide conversion. Se cruza con GA4.

Acciones:

- identificar pagina con clics en GSC;
- revisar conversion en GA4;
- revisar CTA, telefono, WhatsApp, formulario, confianza, movil y friccion.

### Pagina importante sin impresiones

Acciones:

- inspeccionar URL;
- confirmar indexacion;
- revisar canonical;
- revisar noindex;
- revisar enlaces internos;
- revisar sitemap;
- revisar intencion;
- revisar canibalizacion.

---

## Informe de indexacion de paginas

El informe de indexacion responde:

```text
Que paginas conoce Google?
Cuales ha indexado?
Cuales no ha indexado?
Por que no las ha indexado?
```

Regla:

```text
No todas las URLs no indexadas son un problema.
```

Correcto que no se indexe:

- carrito;
- checkout;
- cuenta;
- filtros sin valor;
- parametros duplicados;
- busqueda interna;
- paginas con noindex intencional.

Problema si no se indexa:

- servicio principal;
- categoria importante;
- producto importante;
- landing local;
- articulo estrategico;
- pagina con backlinks.

Motivos comunes:

- Crawled - currently not indexed;
- Discovered - currently not indexed;
- Alternate page with proper canonical tag;
- Duplicate without user-selected canonical;
- Excluded by noindex tag;
- Blocked by robots.txt;
- Not found 404;
- Page with redirect.

Clasificacion:

```text
No indexada y esta bien -> no requiere accion.
No indexada y deberia indexarse -> requiere diagnostico.
Indexada y no deberia estar -> requiere noindex, canonical, eliminacion o mejora.
```

Error tipico:

```text
Intentar indexarlo todo.
```

---

## URL Inspection Tool

La inspeccion de URL es diagnostico quirurgico de una URL concreta.

Se usa para:

- pagina nueva publicada;
- pagina importante no indexada;
- pagina con caida;
- pagina modificada recientemente;
- canonical dudoso;
- bloqueo;
- pagina que no aparece en Google;
- problemas de datos estructurados.

Proceso:

```text
1. Pegar URL exacta.
2. Revisar estado principal.
3. Revisar canonical declarada vs canonical elegida por Google.
4. Probar URL publicada.
5. Revisar pagina rastreada si esta disponible.
6. Solicitar indexacion solo si la pagina ya esta corregida y merece indexarse.
```

Entregable:

```text
URL:
Estado en Google:
Estado en vivo:
Canonical declarada:
Canonical elegida por Google:
Indexable:
Problema:
Accion:
Solicitar indexacion: si/no
```

Error tipico:

```text
Solicitar indexacion una y otra vez sin corregir la causa.
```

---

## Sitemaps

El sitemap ayuda a Google a descubrir URLs importantes.

Reglas:

```text
Sitemap enviado no significa pagina indexada.
Sitemap correcto no significa ranking.
Sitemap util ayuda a Google a encontrar URLs importantes.
```

Revisar que el sitemap:

- carga correctamente;
- no devuelve 404;
- no esta bloqueado;
- contiene URLs correctas;
- usa HTTPS correcto;
- no mezcla variantes www/sin www incorrectas;
- no incluye noindex;
- no incluye 404;
- no incluye redirecciones innecesarias.

Web nueva:

- publicar sitemap limpio;
- enviarlo en GSC;
- inspeccionar Home, servicios y categorias;
- revisar indexacion primeras semanas.

Web existente:

- limpiar URLs basura;
- eliminar URLs noindex, 404, redirigidas o duplicadas;
- confirmar paginas importantes incluidas;
- confirmar que Google puede leerlo.

---

## Core Web Vitals y HTTPS

Core Web Vitals en GSC usa datos reales de usuarios.

Metricas:

- LCP: carga del contenido principal.
- INP: respuesta de la pagina ante interacciones.
- CLS: estabilidad visual.

Proceso:

```text
1. Revisar mobile y desktop.
2. Identificar grupos de URLs afectadas.
3. Detectar metrica problematica.
4. Traducirlo en tarea tecnica por plantilla.
```

No decir "Core Web Vitals mal".

Decir:

```text
Plantilla afectada:
Metrica:
Ejemplo de URL:
Posible causa:
Accion tecnica:
Prioridad:
```

HTTPS:

- revisar URLs HTTP indexadas;
- revisar redireccion HTTP -> HTTPS;
- revisar canonical;
- revisar contenido mixto;
- revisar sitemap y enlaces internos.

Error tipico:

```text
Tener web visualmente en HTTPS, pero canonical, sitemap o enlaces internos en HTTP.
```

---

## Informe de enlaces

GSC muestra enlaces que Google ha encontrado, aunque no necesariamente todos
los enlaces actuales ni si son nofollow.

Revisar:

- paginas con mas enlaces externos;
- dominios que enlazan;
- textos de enlace;
- paginas con mas enlaces internos;
- paginas importantes con pocos enlaces internos.

Usos:

- proteger URLs con backlinks;
- reforzar paginas prioritarias con enlazado interno;
- usar paginas con autoridad externa para distribuir autoridad interna.

Regla:

```text
Una URL con backlinks no se elimina sin revisar.
```

---

## Acciones manuales, seguridad y removals

Siempre revisar:

```text
Security & Manual Actions
```

Si hay accion manual:

1. leer motivo exacto;
2. identificar URLs afectadas;
3. corregir;
4. documentar;
5. solicitar reconsideracion si aplica.

Si hay problema de seguridad:

1. detener SEO de contenidos;
2. avisar a desarrollo/hosting;
3. limpiar sitio;
4. validar en Search Console.

Removals:

- sirve para retirada temporal;
- no reemplaza noindex;
- no arregla arquitectura;
- no debe usarse para canibalizacion normal;
- requiere solucion permanente en la web.

---

## Aplicaciones por area

### On-Page

Proceso:

```text
1. Filtrar por pagina.
2. Revisar consultas asociadas.
3. Clasificar intencion.
4. Revisar CTR y posicion.
5. Comparar SERP real.
6. Decidir cambios on-page.
```

Acciones:

- bajo CTR -> title/meta;
- posicion 4-15 -> contenido y enlaces internos;
- URL incorrecta -> canibalizacion/arquitectura;
- consulta comercial en articulo -> crear o reforzar landing;
- consulta informacional en landing -> ajustar contenido o crear apoyo.

### Contenidos

GSC ayuda a decidir:

- mejorar contenido existente;
- crear contenido nuevo;
- fusionar;
- eliminar/noindexar con criterio.

Nunca eliminar solo porque no hay clics. Antes revisar impresiones, enlaces,
conversiones y posibilidad de fusion.

### Tecnico

Auditoria tecnica basica con GSC:

```text
1. Page Indexing
2. Sitemaps
3. URL Inspection
4. Core Web Vitals
5. HTTPS
6. Manual actions
7. Seguridad
8. Documentar
9. Priorizar
```

GSC no sustituye crawler tecnico, SEMrush ni GA4.

### Local

GSC no es Google Business Profile, pero ayuda a analizar landings locales.

Revisar:

- consultas con ciudad/zona;
- paginas locales;
- dispositivo movil;
- pais;
- rendimiento organico de landings locales.

Acciones:

- mejorar title local;
- reforzar NAP;
- añadir contenido local real;
- añadir FAQs locales;
- enlazar desde Home;
- enlazar desde GBP a la landing correcta.

### IA / AEO / LLMs

GSC no muestra directamente recomendaciones de IA, pero ayuda a detectar:

- consultas largas;
- preguntas reales;
- busquedas comparativas;
- busquedas con "mejor";
- busquedas locales;
- dudas que pueden convertirse en FAQs.

### GSC + GA4

GSC responde:

```text
Como llega el usuario desde Google?
```

GA4 responde:

```text
Que hace despues de entrar?
```

Matriz:

```text
Muchos clics + conversiones -> proteger y reforzar.
Muchos clics + pocas conversiones -> CRO.
Muchas impresiones + pocos clics -> snippet/intencion.
Poca impresion + pagina importante -> indexacion/enlaces/contenido/autoridad.
Trafico informacional sin conversion -> enlaces hacia paginas comerciales.
```

---

## Rutinas

### Semanal

Revisar:

1. caidas bruscas de clics;
2. paginas importantes sin impresiones;
3. errores nuevos de indexacion;
4. URLs importantes no indexadas;
5. seguridad;
6. acciones manuales;
7. sitemaps con errores;
8. cambios raros en consultas principales.

Entregable:

```text
Fecha:
Cambios relevantes:
Problemas detectados:
URLs afectadas:
Acciones urgentes:
Responsable:
```

### Mensual

Revisar:

- clics;
- impresiones;
- CTR;
- posicion media;
- top consultas;
- top paginas;
- consultas ganadas/perdidas;
- paginas ganadoras/perdedoras;
- bajo CTR;
- oportunidades posicion 4-15;
- indexacion;
- Core Web Vitals;
- enlaces.

Entregable:

```text
Resumen:
Que subio:
Que bajo:
Que paginas tienen oportunidad:
Que problemas tecnicos existen:
Que acciones se ejecutaran:
Que se medira el proximo mes:
```

---

## Protocolos finales

### Web nueva + GSC

```text
1. Verificar propiedad
2. Enviar sitemap
3. Inspeccionar Home
4. Inspeccionar paginas principales
5. Solicitar indexacion solo en URLs estrategicas
6. Revisar Page Indexing
7. Revisar canonical elegida por Google
8. Revisar HTTPS
9. Revisar Core Web Vitals cuando haya datos
10. Revisar primeras impresiones
11. Detectar primeras queries
12. Ajustar titles/metas
13. Revisar contenido sin impresiones
14. Crear reporte inicial
```

No hacer:

- solicitar indexacion de paginas pobres;
- enviar sitemap con URLs basura;
- esperar rankings inmediatos;
- tocar todo cada semana sin datos;
- confundir falta de datos con problema grave.

### Web existente + GSC

```text
1. Verificar acceso correcto
2. Revisar rendimiento 3, 6 y 12 meses
3. Identificar paginas con mas clics
4. Identificar paginas con mas impresiones
5. Detectar bajo CTR
6. Detectar posicion 4-15
7. Detectar caidas
8. Revisar indexacion
9. Revisar URLs no indexadas importantes
10. Inspeccionar URLs criticas
11. Revisar sitemap
12. Revisar Core Web Vitals
13. Revisar HTTPS
14. Revisar enlaces
15. Revisar seguridad y acciones manuales
16. Cruzar con GA4
17. Crear matriz de prioridades
18. Ejecutar y medir
```

No hacer:

- cambiar URLs sin revisar datos;
- eliminar paginas sin revisar clics, impresiones y enlaces;
- optimizar paginas irrelevantes antes que paginas con potencial;
- ignorar paginas con muchas impresiones;
- crear contenido nuevo si hay URLs actuales desaprovechadas;
- tratar GSC como rank tracker exacto.

---

## Plantilla interna de analisis GSC

```text
Cliente:
Dominio:
Fecha:
Responsable:

1. Estado general
- Clics:
- Impresiones:
- CTR:
- Posicion media:
- Periodo analizado:
- Comparativa:

2. Consultas
- Top consultas:
- Consultas con oportunidad:
- Consultas con bajo CTR:
- Consultas posicion 4-15:
- Consultas locales:
- Consultas transaccionales:

3. Paginas
- Top paginas:
- Paginas con mas impresiones:
- Paginas con bajo CTR:
- Paginas con caida:
- Paginas con oportunidad:

4. Indexacion
- URLs indexadas:
- URLs no indexadas:
- Motivos principales:
- URLs importantes afectadas:

5. Inspeccion URL
- URLs inspeccionadas:
- Estado:
- Canonical:
- Problemas:

6. Sitemap
- Sitemap enviado:
- Estado:
- Errores:
- URLs importantes incluidas:

7. Experiencia
- Core Web Vitals:
- HTTPS:
- Problemas:

8. Enlaces
- Paginas mas enlazadas externamente:
- Paginas mas enlazadas internamente:
- Paginas importantes con pocos enlaces internos:

9. Riesgos
- Acciones manuales:
- Seguridad:
- Removals:

10. Acciones recomendadas
- Accion:
- URL:
- Motivo:
- Prioridad:
- Responsable:
- Fecha de revision:
```

---

## Errores comunes

1. Creer que posicion media es ranking exacto.
2. Mirar solo clics e ignorar impresiones.
3. No filtrar por pagina.
4. No cruzar query + URL.
5. Mejorar contenido sin revisar intencion.
6. No revisar indexacion antes de optimizar.
7. Solicitar indexacion sin corregir problemas.
8. Pensar que sitemap garantiza indexacion.
9. Eliminar paginas sin revisar datos.
10. No cruzar GSC con GA4.
11. No revisar movil por separado.
12. No revisar acciones manuales/seguridad.
13. Obsesionarse con URLs no indexadas que no deberian indexarse.
14. Ignorar paginas con muchas impresiones y bajo CTR.
15. Reportar datos sin convertirlos en tareas.

---

## Formacion minima obligatoria

Orden recomendado:

Nivel 1 - Base:

1. Get started with Search Console.
2. Reports at a glance.
3. Performance report.
4. Page indexing report.
5. URL Inspection Tool.

Nivel 2 - Diagnostico:

6. Sitemaps report.
7. Core Web Vitals report.
8. HTTPS report.
9. Links report.
10. Manual actions/security issues.

Nivel 3 - Ejecucion SEO:

11. Performance common tasks.
12. Search Console + Google Analytics.
13. Why page is missing from Google.
14. Removals tool.
15. Search Essentials.

Nota:

```text
Rodrigo dio nombres de fuentes oficiales, pero no todas las URLs explicitas.
Antes de convertirlas en examen o modulo oficial para agentes reales, el
Docente SEO debe verificar cada enlace en fuente viva.
```

---

## Regla final para relevo

Cada revision de GSC debe terminar con:

```text
Que detecte.
Que URL afecta.
Por que importa.
Que accion toca.
Quien la ejecuta.
Cuando se revisa.
Como sabremos si funciono.
```

Si una persona no puede convertir datos de GSC en tareas, todavia no esta
haciendo SEO operativo. Esta mirando metricas.
