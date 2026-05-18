# Lectura del sistema completo previa a reestructuracion SEO

Fecha: 2026-05-11
Responsables conceptuales: Arquitecto + Docente SEO + Fenix
Estado: aprendizaje previo, sin cambios operativos en `agents/seo/`

## Decision inicial

El Agente SEO no debe recibir cambios hasta que el Docente SEO entienda primero como funciona el sistema E-SELEC.

La tarea no es "meter mas informacion SEO" en los prompts. La tarea correcta es entender:

- quien decide
- quien ejecuta
- que archivo es fuente de verdad
- que protocolo protege el sistema
- que conocimiento SEO vive en cada capa
- que informacion esta duplicada
- que informacion esta obsoleta
- que cambio puede romper clientes, medicion, URLs, webs o autoridad

Por tanto, el estado queda asi:

1. `agents/seo/` queda congelado.
2. El Docente SEO continua en fase de lectura y diagnostico.
3. Fenix no elimina carpetas todavia; primero debe existir un mapa de canibalizacion y destino.
4. Arquitecto valida que cualquier cambio futuro tenga razon de sistema, no solo razon de contenido.

## Alcance leido

Se revisaron las capas principales del sistema:

- Archivos raiz: `AGENTS.md`, `CLAUDE.md`, `README.md`.
- Protocolos globales: activos criticos, control de artefactos, gestion de secretos, El Escolta, El Fenix, El Arquitecto, El Docente y cierre humano.
- Indices y registros: mapa del sistema, herramientas vivas, registro de accesos, registro de artefactos y reporte de guard.
- Agencia: contexto, marca, historial, log, mensajes, loops, preferencias de Rodrigo y criterios/observaciones del Arquitecto.
- Agentes: lider clientes, lider agencia, lideres de area, sub-agentes SEO, CRO, SEM, Social, Reports, Web, Loops, Calibracion, Arquitecto, Fenix y Docente.
- Clientes: contextos, logs, mensajes, tasks, memorias y manifests de Chashier, Computer Chamberi, La Bottega del Gusto, Stramondo Venezuela y Shogun Motors.
- Skills: inventario funcional de skills de marketing, SEO, CRO, tracking, schema, arquitectura, limpieza de carpetas y WooCommerce.
- Scripts: inventario operativo de conectores, scrapers, router, guard, WordPress, Meta, GA4, GBP, Kling y utilidades.
- Archivos historicos y outputs: inventariados para entender contexto, pero no tratados como fuente de verdad actual salvo que un indice, manifest, contexto o log vigente los respalde.

Exclusiones conscientes:

- No se leyeron secretos ni valores completos de `.env`.
- No se trataron imagenes, binarios, PDFs ni capturas como canon operativo; solo se inventariaron cuando aplicaba.
- No se modifico ningun archivo de cliente ni produccion.

## Lo que debe entender el Docente SEO del sistema E-SELEC

### 1. E-SELEC no es una carpeta de prompts

E-SELEC funciona como un sistema operativo de agencia:

- `AGENTS.md` define las reglas globales.
- Los lideres orquestan.
- Los sub-agentes ejecutan tareas concretas.
- Los clientes tienen memoria propia.
- Los protocolos protegen cambios sensibles.
- Los registros evitan que los artefactos se vuelvan ruido.
- El Arquitecto mejora el sistema.
- El Docente forma criterio.
- El Fenix sana estructuras cuando hay piezas desconectadas.

El Docente SEO no debe actuar como repositorio de informacion. Debe convertir conocimiento SEO en conducta verificable.

### 2. Las fuentes de verdad no son todas iguales

Para SEO, una recomendacion no vale igual si viene de:

- GSC: datos reales de Google Search.
- GA4: comportamiento, eventos y negocio.
- SEMrush: estimaciones, competencia, gaps y diagnostico.
- NeuronWriter: optimizacion semantica por URL.
- Screaming Frog o crawler: estructura tecnica rastreada.
- WordPress/WooCommerce: estado real del CMS.
- `context.md`: snapshot interno del cliente.
- `log.md`: historial de lo ejecutado.
- `mensajes.md`: alertas y dependencias vivas.
- outputs antiguos: evidencia historica, no necesariamente verdad actual.

El Agente SEO debe aprender a preguntar siempre: "que fuente manda para este tipo de decision?"

### 3. SEO tiene riesgo operativo real

SEO no es solo contenido. Puede danar:

- URLs con trafico
- indexacion
- canonicals
- sitemaps
- arquitectura
- redirecciones
- datos estructurados
- medicion
- conversiones
- paginas con backlinks
- fichas locales
- ecommerce

Por eso cualquier cambio sobre web, CMS, indexacion, tracking, GBP, schema, URLs o contenido publicado puede activar Activos Criticos, Control de Artefactos, Gestion de Secretos y El Escolta.

### 4. El conocimiento SEO actual esta distribuido y puede canibalizarse

Existen varias capas con conocimiento SEO:

- modulos del Docente SEO en `agents/docente/seo/aprendizajes/`
- fuentes PDF resumidas en `agents/docente/seo/fuentes/`
- prompts reales en `agents/seo/`
- referencias como `agents/seo/semrush-workflows.md`
- referencias como `agents/seo/referencias/seo-onpage-semrush.md`
- skills como `seo-audit`, `site-architecture`, `ai-seo`, `schema-markup`, `analytics-tracking`
- contextos y outputs historicos por cliente

El problema no es falta de informacion. El problema es decidir que informacion es:

- canon
- referencia
- procedimiento
- ejemplo
- test
- historico
- obsoleto

Mientras eso no este claro, meter mas texto en los agentes SEO aumenta la confusion.

### 5. Web nueva y web existente deben cambiar el comportamiento del agente

El sistema debe formar al SEO para distinguir:

- web nueva: disenar antes de publicar
- web existente: medir, proteger y corregir antes de expandir

Esta diferencia debe afectar:

- orden de lectura
- herramientas usadas
- riesgos
- entregables
- prioridad
- autorizaciones
- metricas de revision

### 6. SEO no trabaja solo

SEO toca o depende de:

- WEB para arquitectura, desarrollo, CMS, redirects, performance y WooCommerce.
- CRO para conversion, CTA, formularios y experiencia.
- Reports para decision mensual y explicacion al cliente.
- SEM para paid search, datos de intencion y landings.
- Social/GBP para reputacion, presencia local y senales externas.
- Agencia para captacion, posicionamiento propio y casos de estudio.

El Docente SEO debe educar sin invadir responsabilidades de otros agentes.

## Diagnostico Arquitecto

El Arquitecto considera correcto el planteamiento nuevo de Rodrigo:

No tiene sentido seguir creando carpetas y fragmentos si antes no se define donde debe vivir cada pieza de conocimiento.

El fallo del enfoque anterior fue asumir que educar era conectar informacion. En realidad, educar el sistema es:

1. entender la arquitectura
2. detectar canibalizaciones
3. definir responsabilidades
4. crear pruebas de conducta
5. proponer cambios minimos
6. ejecutar solo con autorizacion

La informacion del Docente SEO es valiosa, pero todavia no esta convertida en una estructura operativa limpia para los agentes.

## Diagnostico Docente SEO

El Docente SEO ya tiene una base amplia de conocimiento:

- marco maestro SEO
- SEMrush
- GSC
- GA4
- NEURONwriter
- GTM
- Screaming Frog
- GBP
- WordPress/WooCommerce
- Looker Studio
- migraciones
- schema avanzado
- Merchant Center
- SERP manual
- QA SEO
- changelog
- priorizacion
- IA SEO externa
- internacional
- roles y permisos

Pero todavia falta el paso docente real:

- convertir ese conocimiento en competencias por agente
- definir que debe saber cada agente y que no
- evitar duplicidad entre sub-agentes
- crear evaluaciones
- preparar cambios de prompt con minimo ruido

El Docente SEO no debe modificar prompts mientras este en fase de aprendizaje.

## Diagnostico Fenix

Fenix no debe eliminar carpetas ahora.

Primero debe existir un mapa que clasifique cada archivo SEO como:

- mantener como canon
- mantener como referencia
- fusionar
- archivar
- eliminar
- reubicar
- convertir en test

Eliminar antes de mapear puede borrar contexto util o romper trazabilidad.

La limpieza estructural vendra despues del diagnostico de canibalizacion.

## Riesgos detectados

1. Exceso de informacion distribuida sin jerarquia.
2. Riesgo de prompts SEO demasiado largos y poco ejecutables.
3. Duplicidad entre Docente, referencias SEMrush, prompts SEO y skills.
4. Mezcla posible entre contenido canonico y outputs historicos.
5. Riesgo de que el SEO Organico, SEO Tecnico, SEO Web y SEO Local invadan responsabilidades si no se delimitan.
6. Riesgo de modificar URLs, indexacion, GBP, schema o tracking sin aplicar protocolos.
7. Riesgo de reportar datos de herramientas estimadas como si fueran datos reales.
8. Riesgo de crear contenido nuevo antes de proteger activos SEO existentes.

## Estructura recomendada antes de tocar agents/seo

### Fase 1 - Mapa de canibalizacion SEO

Crear un documento que liste:

- archivo
- tipo de conocimiento
- estado
- duplicidades
- agente afectado
- decision propuesta

### Fase 2 - Fuente de verdad SEO

Definir una jerarquia:

- Canon operativo SEO
- Procedimientos por herramienta
- Referencias de estudio
- Simulaciones y tests
- Historico

### Fase 3 - Competencias por agente SEO

Definir que debe saber cada uno:

- Lider SEO: orquestacion, prioridad, riesgo y asignacion
- SEO Tecnico: indexacion, rastreo, performance, schema tecnico, migraciones, QA
- SEO Organico: intencion, keyword-URL, contenido, canibalizacion, enlazado interno, GSC/SEMrush
- SEO Local: GBP, NAP, landings locales, reseñas, local pack, GSC local
- SEO LLMs: IA/AEO/GEO, claridad, presencia externa, citas, herramientas IA
- SEO Web: validacion SEO de arquitectura creada por WEB, no arquitectura primaria

### Fase 4 - Pruebas de conducta

Antes de cambiar prompts, crear simulaciones:

- web nueva
- web existente con caida
- canibalizacion
- migracion
- ecommerce
- local SEO
- IA SEO
- bajo CTR
- trafico sin conversion
- URL con backlinks

### Fase 5 - Orden de Cambio

Solo despues de las fases anteriores se propone modificar `agents/seo/`.

El cambio debe:

- ser minimo
- evitar duplicar manuales enteros
- apuntar a conducta
- incluir pruebas
- registrar artefactos
- pasar El Escolta

## Acuerdo operativo

Arquitecto:
El Docente SEO debe entender el sistema antes de formar agentes. No se aprueba reestructuracion sin mapa previo.

Docente SEO:
Continua en aprendizaje. Solo puede escribir dentro de `agents/docente/seo/` hasta nueva autorizacion.

Fenix:
Queda reservado para la fase de limpieza estructural. No borra carpetas sin mapa de canibalizacion y aprobacion.

SEO:
No genera cambios en prompts ni operaciones hasta que exista diagnostico, competencias y pruebas.

## Proximo paso recomendado

Crear:

`agents/docente/seo/aprendizajes/2026-05-11-mapa-canibalizacion-seo-y-estructura-destino.md`

Ese documento debe responder:

1. Que archivos SEO existen.
2. Que funcion cumple cada uno.
3. Que informacion se duplica.
4. Que debe quedar como canon.
5. Que debe quedar como referencia.
6. Que debe archivarse.
7. Que debe transferirse a cada agente.
8. Que no debe tocarse todavia.

Hasta ese mapa, no se modifica `agents/seo/`.
