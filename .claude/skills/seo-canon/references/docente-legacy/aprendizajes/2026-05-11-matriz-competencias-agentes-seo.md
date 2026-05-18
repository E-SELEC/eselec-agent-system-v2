# Matriz de competencias para agentes SEO - Docente SEO

- Fecha: 2026-05-11
- Fuente: marco maestro SEO de Rodrigo + lectura profunda de `agents/seo`
- Estado: borrador / insumo de diagnostico no aplicado

---

## Nota del Arquitecto

El 2026-05-11 Rodrigo pidio que el Arquitecto hablara con el Docente antes de
educar agentes.

Resultado:

```text
Esta matriz no es autorizacion para modificar agentes.
Sirve para diagnosticar brechas y disenar pruebas.
La educacion real debe empezar por conducta observable y simulaciones.
```

Ver:

```text
agency/arquitecto/propuestas-2026-05-11.md
```

---

## Leyenda

```text
D = debe dominar
A = debe aplicar con autonomia
C = debe conocer y escalar
S = solo senior o con aprobacion
```

---

## Matriz por agente

| Competencia | Lider SEO | Tecnico | Organico | Local | LLMs | SEO Web |
|---|---:|---:|---:|---:|---:|---:|
| Marco maestro SEO | D | A | A | A | A | A |
| Web nueva vs existente | D | A | A | A | A | D |
| Priorizacion impacto/esfuerzo/riesgo | D | A | A | A | A | A |
| SEMrush | A | A | D | A | A | A |
| GSC | D | D | D | A | A | A |
| GA4 | A | A | A | A | A | A |
| NeuronWriter | C | C | D | C | A | C |
| GTM | C | A | C | C | C | A |
| Screaming Frog | C | D | A | C | C | A |
| GBP | C | C | C | D | A | C |
| WordPress / WooCommerce | C | A | A | C | C | A |
| Looker Studio | A | C | C | C | C | C |
| Migraciones SEO | S | D | C | C | C | A |
| Schema avanzado | C | D | A | A | A | A |
| Merchant Center | C | A | C | C | C | C |
| Analisis SERP manual | A | A | D | A | A | A |
| QA SEO | D | D | A | A | A | D |
| SEO Changelog | D | A | A | A | A | A |
| SEO para IA externo | A | A | C | A | D | C |
| SEO internacional | A | A | A | C | C | A |
| Roles y permisos | D | A | C | A | C | A |

---

## Educacion especifica por agente

### Lider SEO

Debe aprender primero:

```text
orquestacion
dependencias
prioridad
riesgo
activacion correcta de subagentes
SEMrush + GSC + GA4 como fuentes combinadas
control de artefactos
changelog
roles y permisos
```

Brecha principal:

```text
El prompt actual ya coordina bien,
pero necesita integrar de forma mas explicita
priorizacion, changelog, QA, roles/permisos,
SEO internacional y criterios de IA externa.
```

Prueba:

```text
Dado un cliente con web existente, datos parciales y varias alertas,
decidir que agente actua primero, que no se toca y que queda como propuesta.
```

---

### SEO Tecnico

Debe aprender primero:

```text
GSC Page Indexing
URL Inspection
Screaming Frog
Site Audit
robots.txt
sitemap
canonicals
redirecciones
Core Web Vitals
schema avanzado
migraciones
QA tecnico
changelog
```

Brecha principal:

```text
El prompt actual es fuerte en correcciones tecnicas,
pero debe conectarse mejor con migraciones, QA, changelog,
Screaming Frog, roles/permisos y protocolos de activos criticos.
```

Prueba:

```text
Diagnosticar por que una URL importante no indexa y entregar accion,
riesgo, rollback y metrica de validacion.
```

---

### SEO Organico

Debe aprender primero:

```text
analisis SERP manual
keyword research
intencion
keyword -> URL
canibalizacion
GSC Performance
NeuronWriter
contenido util
clusters
enlazado interno
CRO basico
```

Brecha principal:

```text
Debe corregirse pedagogicamente la regla "una pagina = una keyword principal"
para ensenar "una URL = una intencion principal".
Puede haber keywords secundarias dentro de la misma URL si comparten intencion.
```

Prueba:

```text
Dado un grupo de keywords parecidas, decidir si van en una URL,
varias URLs, blog, landing, categoria o se descartan.
```

---

### SEO Local

Debe aprender primero:

```text
GBP
NAP
resenas
directorios
map pack
landings locales
GSC por queries locales
GA4 por llamadas, WhatsApp y formularios
permisos sensibles de GBP
IA externa local
```

Brecha principal:

```text
El prompt actual entiende GBP y NAP,
pero debe reforzar permisos, medicion de conversion local,
Merchant/GBP si aplica y conexion con IA externa.
```

Prueba:

```text
Auditar un negocio local y distinguir acciones en GBP,
acciones en web, acciones en directorios y acciones de medicion.
```

---

### SEO LLMs

Debe aprender primero:

```text
SEO para IA externo
AEO
GEO
LLMO
bots de IA
robots.txt
llms.txt con prudencia
contenido citable
entidades
Bing / Copilot
Perplexity
ChatGPT Search
Google AI Overviews / AI Mode
medicion de referrals
pruebas manuales documentadas
```

Brecha principal:

```text
El prompt actual es una buena base,
pero debe actualizarse para no tratar "LLMs" como una sola cosa.
Debe separar bots, buscadores IA, respuestas generativas,
acciones de usuario, entrenamiento, citabilidad y medicion.
```

Prueba:

```text
Dado un cliente, documentar como aparece en ChatGPT, Perplexity,
Google AI y Copilot, que fuentes se citan y que accion toca.
```

---

### SEO Web

Debe aprender primero:

```text
web nueva
arquitectura SEO
mapeo keyword -> URL
validacion predesarrollo
checklist prelanzamiento
GSC
GA4
GTM
schema base
QA SEO
changelog
SEO internacional si aplica
```

Brecha principal:

```text
El prompt actual valida bien arquitectura y lanzamiento,
pero debe incorporar con mas fuerza medicion, QA, changelog,
eventos clave, internacional y control de permisos antes de publicar.
```

Prueba:

```text
Revisar una arquitectura propuesta por WEB y decidir si se aprueba,
se corrige o se bloquea el lanzamiento.
```

---

## Orden de transferencia al prompt operativo

Cuando Rodrigo autorice modificar `agents/seo`, el orden seguro sera:

```text
1. leader-seo.md
2. seo-tecnico.md
3. seo-organico.md
4. seo-web.md
5. seo-local.md
6. seo-llms.md
```

No se recomienda actualizar todos de golpe sin pruebas.

---

## Criterio de aprobacion docente

Un agente queda educado cuando:

```text
entiende su limite
entiende sus dependencias
usa fuentes correctas
prioriza por impacto y riesgo
produce accion implementable
documenta cambios
deja metrica de revision
sabe cuando escalar
```

Si falla uno de esos puntos, no esta listo para ejecutar sin supervision.
