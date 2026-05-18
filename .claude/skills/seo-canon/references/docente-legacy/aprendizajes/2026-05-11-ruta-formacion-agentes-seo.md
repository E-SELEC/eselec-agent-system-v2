# Ruta de formacion para agentes SEO - Docente SEO

- Fecha: 2026-05-11
- Responsable: Docente SEO
- Objetivo: educar a los agentes SEO actuales sin modificar todavia sus prompts operativos
- Estado: borrador / insumo de diagnostico no aplicado

---

## Nota del Arquitecto

El 2026-05-11 Rodrigo pidio que el Arquitecto hablara con el Docente antes de
educar agentes.

Resultado:

```text
Esta ruta no es educacion aplicada.
Es insumo de diagnostico.
No autoriza modificar prompts operativos.
```

Ver:

```text
agency/arquitecto/propuestas-2026-05-11.md
```

---

## Proposito

Esta ruta convierte el marco maestro SEO de Rodrigo en un programa de formacion para los agentes de `agents/seo`.

La idea no es que los agentes memoricen herramientas.

La idea es que aprendan criterio:

```text
que mirar
por que importa
que fuente pesa mas
que accion toca
que riesgo existe
quien debe aprobar
como se valida
como se registra
```

---

## Regla principal del Docente

```text
Un agente SEO no esta educado cuando conoce una herramienta.
Esta educado cuando sabe convertir datos en decisiones seguras,
priorizadas, ejecutables y medibles.
```

---

## Niveles de formacion

### Nivel 1 - Marco mental SEO

Todos los agentes deben dominar:

```text
SEO como sistema
web nueva vs web existente
intencion de busqueda
keyword -> URL
arquitectura
indexacion
contenido util
autoridad
CRO
medicion
```

Prueba:

```text
Explicar por que no se empieza una estrategia SEO creando blogs.
Explicar que puede romperse al cambiar una URL.
Explicar la diferencia entre disenar una web nueva y corregir una web existente.
```

---

### Nivel 2 - Fuentes de decision

Todos los agentes deben entender:

```text
SEMrush = estimacion, competencia, gaps, auditorias y oportunidades.
GSC = datos reales de Google Search.
GA4 = comportamiento, eventos, conversiones y negocio.
NeuronWriter = optimizacion semantica de una URL con intencion definida.
Screaming Frog = rastreo tecnico propio.
GTM = implementacion y validacion de eventos.
```

Prueba:

```text
Dada una URL, decir que aporta SEMrush, que aporta GSC y que aporta GA4.
Dado un hallazgo, decir si es dato real, estimacion o recomendacion de herramienta.
```

---

### Nivel 3 - Ejecucion por contexto

El agente debe diferenciar:

```text
Web nueva:
brief -> investigacion -> arquitectura -> mapeo -> contenido -> tecnica -> QA -> publicacion -> medicion.

Web existente:
datos -> proteccion de activos -> auditoria -> optimizacion -> mejora -> expansion -> medicion.
```

Prueba:

```text
Crear un protocolo de 10 pasos para una web nueva.
Crear un protocolo de 10 pasos para una web existente sin romper activos.
```

---

### Nivel 4 - Operacion por herramienta

Los agentes deben poder usar las herramientas con criterio:

```text
SEMrush:
Domain Overview, Organic Research, Keyword Gap, Site Audit, Position Tracking, On Page SEO Checker.

GSC:
Performance, Page Indexing, URL Inspection, Sitemaps, CWV, HTTPS, Links, Manual Actions.

GA4:
Traffic Acquisition, Landing Pages, Pages and Screens, Events, Key Events, Ecommerce, Funnels, Paths.

NeuronWriter:
queries, competidores, Content Score, NLP Terms, AI Score, briefs, GSC integration, WordPress integration.

GTM:
tags, triggers, variables, preview, debug, publish, rollback.

Screaming Frog:
crawl, indexability, canonicals, redirects, status codes, metadata, hreflang, schema, exports.
```

Prueba:

```text
Cada agente debe producir un entregable accionable, no una lista de capturas.
```

---

### Nivel 5 - Especializacion

Cada agente recibe especializacion segun su rol:

```text
Lider SEO:
orquestacion, dependencias, prioridad, riesgo, activacion de agentes, consolidacion.

SEO Tecnico:
indexacion, rastreo, canonicals, robots, sitemap, redirecciones, CWV, schema, migraciones, QA tecnico.

SEO Organico:
SERP manual, keyword research, intencion, arquitectura, contenido, NeuronWriter, canibalizacion, enlazado interno.

SEO Local:
GBP, NAP, resenas, directorios, map pack, landings locales, GA4/GSC/GBP, permisos sensibles.

SEO LLMs:
IA externa, bots, llms.txt, contenido citable, entidad, prompts, referencias externas, medicion de referrals.

SEO Web:
validacion de arquitectura, checklist de lanzamiento, GSC/GA4/GTM, schema base, QA, changelog.
```

Prueba:

```text
Cada agente debe resolver un caso practico de su area y explicar que NO debe tocar.
```

---

### Nivel 6 - Gobierno operativo

Todos los agentes deben aprender:

```text
priorizacion
QA SEO
SEO changelog
roles y permisos
control de activos criticos
gestion de secretos
control de artefactos
cuanto escalar a senior
cuando no ejecutar
```

Prueba:

```text
Dado un cambio SEO, clasificar impacto, esfuerzo, riesgo, responsable, aprobador, rollback y fecha de revision.
```

---

## Metodo de educacion

El Docente educa en cuatro rondas:

```text
1. Lectura:
el agente estudia el modulo relevante.

2. Simulacion:
el agente resuelve un caso sin tocar activos reales.

3. Correccion:
el Docente compara la respuesta contra el marco maestro.

4. Habilitacion:
el agente queda autorizado para ejecutar tareas de bajo riesgo en su area.
```

Un agente no pasa de simulacion a ejecucion si:

```text
confunde fuentes
no prioriza
no documenta
no identifica riesgos
no sabe que URL afecta
no define metrica de validacion
no sabe cuando escalar
```

---

## Examen minimo comun

Todos los agentes deben poder responder:

```text
1. Que diferencia hay entre SEMrush, GSC y GA4?
2. Cuando se optimiza una URL existente y cuando se crea una nueva?
3. Que datos revisas antes de eliminar una pagina?
4. Que haces si una pagina importante no esta indexada?
5. Que significa una keyword con muchas impresiones y bajo CTR?
6. Que evento debe medir GA4 en una web de servicios?
7. Por que no se toca robots.txt sin criterio?
8. Como detectas canibalizacion?
9. Que debe contener un changelog SEO?
10. Que cambios requieren aprobacion senior?
```

---

## Orden recomendado para educar a los agentes

```text
1. Lider SEO
2. SEO Tecnico
3. SEO Organico
4. SEO Web
5. SEO Local
6. SEO LLMs
```

Motivo:

```text
Primero se educa al orquestador.
Despues al agente que desbloquea la base tecnica.
Luego al que produce contenido y arquitectura.
Despues al que valida webs nuevas.
Finalmente se especializa local e IA.
```

---

## Regla de cierre

```text
Educar agentes no es meter mas instrucciones.
Es mejorar su criterio para que ejecuten menos cosas sueltas
y mas decisiones correctas.
```
