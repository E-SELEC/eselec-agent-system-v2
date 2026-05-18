# Mapa de canibalizacion SEO y estructura destino

Fecha: 2026-05-12
Responsables conceptuales: Arquitecto + Docente SEO + Fenix
Estado: diagnostico previo a cambios operativos
Decision: no modificar `agents/seo/` todavia

## 1. Proposito

Este documento responde a la pregunta de Rodrigo:

> Si el Docente SEO ya tiene el conocimiento, deberia saber donde ubicar toda la informacion dentro de cada agente, eliminando canibalizaciones y creando una estructura mas acorde con como se trabaja el SEO?

Respuesta:

Si. Ese es el camino correcto.

Pero antes de borrar carpetas o modificar prompts, el sistema necesita un mapa que diga:

- que existe
- para que sirve
- donde se duplica
- que debe quedar como canon
- que debe quedar como referencia
- que debe archivarse
- que debe transferirse a cada agente
- que no debe tocarse todavia

Este archivo es ese mapa.

## 2. Sustento desde Claude Code oficial

La documentacion oficial de Claude Code refuerza cuatro criterios importantes para E-SELEC:

1. Memoria de proyecto:
   Claude Code usa archivos `CLAUDE.md` como instrucciones persistentes. Tambien reconoce `AGENTS.md`, pero recomienda que `CLAUDE.md` lo importe si ese archivo es la fuente de instrucciones de otros agentes. Ademas recomienda instrucciones especificas, concisas y revisadas periodicamente.
   Fuente: https://docs.anthropic.com/en/docs/claude-code/memory

2. Subagentes:
   Los subagentes deben ser asistentes especializados para tareas especificas, con contexto propio, prompt propio, permisos concretos y responsabilidad limitada. La documentacion recomienda disenar subagentes enfocados, con descripciones detalladas y acceso limitado a herramientas.
   Fuente: https://docs.anthropic.com/en/docs/claude-code/sub-agents

3. Settings y permisos:
   Las instrucciones guian comportamiento, pero la configuracion y permisos controlan herramientas, entorno y seguridad. Esto confirma que en E-SELEC no basta con "decirle" al agente que no toque activos criticos: tambien hay que apoyar la conducta con protocolos, guard y permisos.
   Fuente: https://docs.anthropic.com/en/docs/claude-code/settings

4. Hooks y validaciones:
   Claude Code permite hooks que se ejecutan automaticamente en puntos del ciclo de vida. En E-SELEC, El Escolta cumple una funcion equivalente de cierre y verificacion. La idea correcta es que las reglas importantes no dependan solo de memoria humana o prompt.
   Fuente: https://docs.anthropic.com/en/docs/claude-code/hooks

5. Workflow seguro:
   Para trabajos complejos, la documentacion recomienda encontrar archivos relevantes, entender como interactuan, aplicar cambios pequenos y verificables, y validar despues.
   Fuente: https://docs.anthropic.com/en/docs/claude-code/common-workflows

Conclusion para E-SELEC:

El Docente SEO no debe llenar prompts de teoria. Debe convertir conocimiento en reglas concretas, responsabilidades, pruebas y cambios pequenos. Esto coincide con el criterio del Arquitecto.

## 3. Inventario de conocimiento SEO existente

### 3.1. Laboratorio del Docente SEO - aprendizajes

Ubicacion: `agents/docente/seo/aprendizajes/`

| Archivo | Funcion actual | Decision |
|---|---|---|
| `2026-05-09-personalidad-claridad-sistema.md` | Personalidad pedagogica del Docente SEO | Mantener como identidad docente |
| `2026-05-09-marco-maestro-seo-rodrigo.md` | Marco conceptual maestro del SEO | Canon base |
| `2026-05-09-ejecucion-seo-rodrigo.md` | Ejecucion paso a paso para web nueva/existente | Canon operativo |
| `2026-05-09-modulo-semrush-rodrigo.md` | Uso de SEMrush como diagnostico, investigacion y seguimiento | Procedimiento por herramienta |
| `2026-05-09-modulo-gsc-rodrigo.md` | Uso de Search Console como realidad de Google Search | Procedimiento por herramienta y fuente principal de datos SEO reales |
| `2026-05-09-modulo-ga4-rodrigo.md` | Uso de GA4 para comportamiento, eventos y negocio | Procedimiento de medicion/CRO |
| `2026-05-09-modulo-neuronwriter-rodrigo.md` | Optimizacion semantica por URL | Procedimiento de contenido |
| `2026-05-10-modulo-gtm-rodrigo.md` | Medicion con GTM | Procedimiento tecnico de tracking |
| `2026-05-10-modulo-screaming-frog-rodrigo.md` | Rastreo tecnico y auditoria crawler | Procedimiento tecnico |
| `2026-05-10-modulo-gbp-rodrigo.md` | SEO local y GBP | Procedimiento local |
| `2026-05-10-modulo-wordpress-woocommerce-rodrigo.md` | SEO en CMS/ecommerce | Procedimiento CMS/ecommerce |
| `2026-05-10-modulo-looker-studio-rodrigo.md` | Reporting y dashboards | Procedimiento reporting |
| `2026-05-11-modulo-migraciones-seo-rodrigo.md` | Migraciones SEO | Procedimiento alto riesgo |
| `2026-05-11-modulo-schema-avanzado-rodrigo.md` | Datos estructurados avanzados | Procedimiento tecnico/contenido |
| `2026-05-11-modulo-merchant-center-rodrigo.md` | Google Merchant Center | Procedimiento ecommerce |
| `2026-05-11-modulo-serp-manual-rodrigo.md` | Analisis SERP manual | Canon de decision antes de contenido |
| `2026-05-11-modulo-qa-seo-rodrigo.md` | Control de calidad antes de publicar | Canon de salida |
| `2026-05-11-modulo-seo-changelog-rodrigo.md` | Registro de cambios SEO | Canon de trazabilidad |
| `2026-05-11-modulo-priorizacion-tareas-seo-rodrigo.md` | Priorizacion por impacto/esfuerzo/riesgo | Canon de decision |
| `2026-05-11-modulo-seo-ia-externo-rodrigo.md` | SEO para IA externa | Procedimiento IA/AEO |
| `2026-05-11-modulo-seo-internacional-rodrigo.md` | SEO internacional | Procedimiento especializado |
| `2026-05-11-modulo-roles-permisos-seo-rodrigo.md` | Roles, permisos y RACI | Gobierno operativo |
| `2026-05-09-refuerzo-links-manual-seo.md` | Inventario de fuentes enlazadas | Referencia de estudio |
| `2026-05-11-lectura-profunda-agents-seo.md` | Diagnostico de prompts SEO actuales | Historico vivo de diagnostico |
| `2026-05-11-ruta-formacion-agentes-seo.md` | Ruta formativa previa | Mantener como insumo, no como canon final |
| `2026-05-11-matriz-competencias-agentes-seo.md` | Matriz previa de competencias | Mantener como insumo, necesita depuracion |
| `2026-05-11-lectura-sistema-completo-previa-reestructuracion.md` | Lectura del sistema antes de tocar SEO | Canon de restriccion actual |
| `2026-05-12-mapa-canibalizacion-seo-y-estructura-destino.md` | Este mapa | Canon de transicion |

### 3.2. Fuentes PDF del Docente SEO

Ubicacion: `agents/docente/seo/fuentes/`

| Archivo | Funcion actual | Decision |
|---|---|---|
| `2026-05-09-manual-seo-pdf-links.md` | Fuente con links del manual inicial | Mantener como fuente historica |
| `2026-05-10-manual-seo-post-neuronwriter.md` | Fuente PDF de modulos post NEURONwriter | Mantener como fuente historica |
| `2026-05-11-manual-seo-migraciones-schema-merchant.md` | Fuente PDF migraciones/schema/merchant | Mantener como fuente historica |
| `2026-05-11-manual-seo-serp-qa-changelog.md` | Fuente PDF SERP/QA/changelog | Mantener como fuente historica |
| `2026-05-11-manual-seo-priorizacion-ia-internacional-roles.md` | Fuente PDF priorizacion/IA/internacional/roles | Mantener como fuente historica |

Regla:

Las fuentes explican de donde vino el aprendizaje. No deben ser usadas por los agentes operativos como manual directo.

### 3.3. Prompts operativos SEO

Ubicacion: `agents/seo/`

| Archivo | Rol actual | Problema detectado | Decision |
|---|---|---|---|
| `leader-seo.md` | Orquesta SEO y decide sub-agentes | Tiene principios SEO utiles, pero mezcla orquestacion con mini-canon SEO | Mantener. Futuro cambio minimo: decision tree, prioridades, riesgos, fuentes de verdad |
| `seo-tecnico.md` | Diagnostico tecnico, indexacion, crawl, performance, schema tecnico | Tiene SEMrush workflows y criterios on-page que pueden solaparse con Organico | Mantener. Futuro: limitar a desbloqueo tecnico y QA tecnico |
| `seo-organico.md` | Keywords, intencion, contenido, arquitectura de contenido, canibalizacion | Carga mucha produccion de contenido y algunos criterios que podrian vivir en canon/procedimiento | Mantener. Futuro: reforzar intencion, keyword-URL, canibalizacion y GSC/SEMrush |
| `seo-local.md` | GBP, NAP, reseñas, landings locales, map pack | Correcto, pero debe proteger permisos GBP y cambios locales reales | Mantener. Futuro: conectar con roles/permisos y QA local |
| `seo-llms.md` | IA/AEO/GEO y visibilidad en LLMs | Necesita actualizarse con modulo SEO IA externo y limites de medicion | Mantener. Futuro: reducir fantasia de herramienta y exigir evidencia |
| `seo-web.md` | Validacion SEO de arquitectura web | Correctamente no define arquitectura, pero debe integrarse con QA, migraciones y changelog | Mantener. Futuro: gate prepublicacion/postpublicacion |

Regla:

Los prompts operativos no deben contener manuales completos. Deben contener:

- rol
- limites
- inputs obligatorios
- arbol de decision
- protocolos
- entregable
- criterios de aprobado
- cuando escalar

### 3.4. Referencias dentro de agents/seo

| Archivo | Funcion actual | Problema | Decision |
|---|---|---|---|
| `agents/seo/semrush-workflows.md` | Base amplia de workflows SEMrush para SEO, SEM, Social, agencia y mercado | Es demasiado transversal para vivir dentro de `agents/seo`; canibaliza SEM/Social/Agencia y duplica el modulo SEMrush del Docente | Mantener por ahora. Futuro: mover o dividir a procedimientos por herramienta/area |
| `agents/seo/referencias/seo-onpage-semrush.md` | Referencia larga de on-page desde SEMrush | Es referencia, no canon. Puede contradecir el marco maestro o quedar obsoleta | Mantener por ahora. Futuro: clasificar como referencia externa versionada |

Regla:

Las referencias no son autoridad final. El canon E-SELEC manda sobre referencias de herramientas.

### 3.5. Skills relacionadas

Ubicacion: `.agents/skills/`

| Skill | Funcion | Decision |
|---|---|---|
| `seo-audit` | Auditorias SEO y diagnostico | Mantener como skill de ejecucion |
| `site-architecture` | Arquitectura, URLs, navegacion, enlazado | Mantener, pero WEB es dueño primario de arquitectura |
| `ai-seo` | Optimizacion para IA/LLMs | Mantener como skill de apoyo, no canon |
| `schema-markup` | Datos estructurados | Mantener como skill tecnica especializada |
| `analytics-tracking` | GA4/GTM/medicion | Mantener como skill para Reports/WEB/SEO tecnico |
| `woocommerce-setup` | WooCommerce | Mantener para WEB/ecommerce, no para SEO solo |
| `folder-cleanup` | Limpieza de carpetas y artefactos | Usar cuando Fenix limpie, no ahora |

Regla:

Las skills son capacidades de ejecucion. No reemplazan al Docente ni a los prompts. Se invocan cuando la tarea concreta lo requiere.

## 4. Canibalizaciones detectadas

### 4.1. SEMrush duplicado

Duplicado entre:

- `agents/docente/seo/aprendizajes/2026-05-09-modulo-semrush-rodrigo.md`
- `agents/seo/semrush-workflows.md`
- secciones SEMrush dentro de `leader-seo.md`
- secciones SEMrush dentro de cada sub-agente SEO
- referencias SEMrush on-page

Decision:

Crear una sola fuente futura:

`agents/docente/seo/procedimientos/semrush-seo.md`

Los prompts solo deben decir cuando usar SEMrush y que decision sacar, no explicar toda la herramienta.

### 4.2. On-page duplicado

Duplicado entre:

- marco maestro SEO
- ejecucion SEO
- SEO Organico
- SEO Tecnico
- `seo-onpage-semrush.md`
- NeuronWriter
- QA SEO

Decision:

Separar:

- SEO Organico: intencion, contenido, keyword-URL, internal linking editorial.
- SEO Tecnico: indexabilidad, canonicals, rendimiento, schema tecnico, errores de plantilla.
- NeuronWriter: optimizacion semantica de una URL ya definida.
- QA SEO: puerta de salida antes de publicar.

### 4.3. Arquitectura duplicada

Duplicado entre:

- marco maestro SEO
- ejecucion SEO
- SEO Organico
- SEO Web
- skill `site-architecture`
- agentes WEB

Decision:

WEB define arquitectura.
SEO Organico propone mapa keyword -> URL.
SEO Web valida si la arquitectura de WEB respeta SEO.
Lider SEO decide dependencia y orden.

### 4.4. Schema duplicado

Duplicado entre:

- SEO Tecnico
- SEO Organico
- SEO Web
- modulo schema avanzado
- NeuronWriter schema
- skill `schema-markup`
- WooCommerce module

Decision:

Schema se divide asi:

- SEO Organico: recomienda schema segun tipo de contenido.
- SEO Tecnico: valida implementacion tecnica y errores.
- WEB: implementa en CMS/codigo cuando aplique.
- WooCommerce/WEB: Product, Offer, Breadcrumb y ecommerce.
- QA SEO: verifica que el schema coincida con contenido visible.

### 4.5. IA SEO duplicado

Duplicado entre:

- SEO LLMs
- modulo SEO IA externo
- NeuronWriter AI Score
- SEMrush AI Visibility
- AI SEO skill
- marco maestro SEO

Decision:

SEO LLMs debe ser responsable del criterio IA/AEO/GEO, pero debe quedar anclado a:

- claridad
- cobertura
- estructura
- presencia externa
- datos verificables
- medicion con limitaciones

No debe prometer visibilidad IA sin evidencia.

### 4.6. Medicion duplicada

Duplicado entre:

- GSC module
- GA4 module
- GTM module
- Looker Studio module
- Reports
- SEO Tecnico
- SEO Organico

Decision:

SEO usa medicion para decidir.
Reports usa medicion para explicar.
WEB/Tracking implementa medicion.
GTM/GA4 son procedimientos, no responsabilidades absolutas del SEO.

### 4.7. Priorizacion duplicada

Duplicado entre:

- AGENTS.md sistema de prioridad
- modulo priorizacion SEO
- leader-seo decision tree
- SEO tecnico priorizacion de errores
- SEO organico quick wins

Decision:

El Lider SEO debe tener una matriz corta:

Prioridad SEO = impacto + esfuerzo + riesgo + fuente de datos + estado de web nueva/existente.

Los sub-agentes priorizan dentro de su area, pero el Lider SEO decide orden global.

### 4.8. QA y changelog no conectados

Actualmente existen como aprendizaje, pero no estan conectados de forma fuerte en los prompts SEO.

Decision:

Todo cambio SEO futuro debe cerrar con:

- QA SEO
- changelog si se toco URL, contenido, title/meta, indexacion, schema, enlazado interno, sitemap, robots, GBP o tracking
- registro de artefactos si se creo output/documento

## 5. Estructura destino recomendada

Esta estructura NO se crea todavia. Es la propuesta destino.

```text
agents/docente/seo/
|
|-- canon/
|   |-- canon-operativo-seo.md
|   |-- fuentes-de-verdad-seo.md
|   |-- matriz-web-nueva-vs-existente.md
|   |-- matriz-prioridad-riesgo-seo.md
|
|-- procedimientos/
|   |-- semrush-seo.md
|   |-- gsc-seo.md
|   |-- ga4-seo.md
|   |-- gtm-seo.md
|   |-- neuronwriter-seo.md
|   |-- screaming-frog-seo.md
|   |-- gbp-seo-local.md
|   |-- wordpress-woocommerce-seo.md
|   |-- migraciones-seo.md
|   |-- schema-seo.md
|   |-- merchant-center-seo.md
|   |-- seo-ia-externo.md
|   |-- seo-internacional.md
|
|-- evaluaciones/
|   |-- lider-seo.md
|   |-- seo-tecnico.md
|   |-- seo-organico.md
|   |-- seo-local.md
|   |-- seo-llms.md
|   |-- seo-web.md
|
|-- historico/
|   |-- fuentes/
|   |-- aprendizajes-originales/
|
|-- mapas/
|   |-- mapa-canibalizacion-seo-y-estructura-destino.md
```

La estructura actual puede mantenerse hasta que Rodrigo apruebe la migracion. No se mueve nada sin Orden de Cambio.

## 6. Estructura destino de conocimiento por agente

### 6.1. Lider SEO

Debe aprender:

- diferenciar web nueva vs web existente
- decidir fuente de verdad por caso
- activar sub-agente correcto
- priorizar por impacto/esfuerzo/riesgo
- detectar activos criticos
- exigir QA y changelog
- no ejecutar tareas tecnicas ni contenido directamente

No debe aprender:

- todos los pasos internos de cada herramienta
- redaccion completa de contenido
- configuraciones profundas de GA4/GTM/GBP/WooCommerce

Cambio futuro esperado:

Agregar una seccion corta: "Decision SEO obligatoria antes de activar sub-agentes".

### 6.2. SEO Tecnico

Debe aprender:

- indexacion
- rastreo
- canonicals
- robots
- sitemap
- CWV/performance
- schema tecnico
- migraciones
- QA tecnico
- changelog tecnico
- riesgo de tocar produccion

No debe aprender:

- estrategia editorial completa
- calendario de contenido
- captacion de backlinks como tarea principal
- CRO visual, salvo cuando afecte performance/medicion

Cambio futuro esperado:

Convertirlo en desbloqueador tecnico con protocolos de alto riesgo.

### 6.3. SEO Organico

Debe aprender:

- investigacion de intencion
- keyword research
- SERP manual
- mapa keyword -> URL
- canibalizacion
- contenido existente antes de crear nuevo
- optimizacion de title/meta/H1/H2/contenido
- enlazado interno editorial
- NeuronWriter como apoyo, no como estrategia
- GSC + SEMrush para priorizar

No debe aprender:

- cambios tecnicos de servidor/CMS
- implementacion de schema en codigo
- tocar URLs sin revisar activos
- crear paginas por cada keyword parecida

Cambio futuro esperado:

Reforzar que cada URL existe por intencion, no por keyword aislada.

### 6.4. SEO Local

Debe aprender:

- GBP
- NAP
- categorias
- servicios/productos
- reseñas
- landings locales
- queries locales GSC
- citaciones
- riesgos de suspensiones/duplicados
- permisos GBP

No debe aprender:

- automatizar cambios GBP sin aprobacion
- estrategia organic nacional si no aplica
- reporting general de agencia

Cambio futuro esperado:

Conectar local con roles/permisos y activos criticos.

### 6.5. SEO LLMs

Debe aprender:

- IA/AEO/GEO
- contenido citable
- claridad y estructura
- entidades y presencia externa
- limitaciones de medicion
- bots y acceso
- llms.txt como apoyo, no magia
- validacion manual en motores IA

No debe aprender:

- prometer rankings en IA
- depender solo de herramientas de AI Visibility
- sustituir SEO clasico

Cambio futuro esperado:

Actualizarlo con el modulo SEO IA externo y reducir cualquier instruccion especulativa.

### 6.6. SEO Web

Debe aprender:

- validar arquitectura creada por WEB
- validar mapa keyword -> URL
- checklist prepublicacion
- noindex/canonical/sitemap
- schema basico
- tracking basico
- QA SEO antes de lanzamiento
- migracion si aplica
- changelog de lanzamiento

No debe aprender:

- definir arquitectura completa solo
- implementar cambios visuales o codigo
- tocar produccion sin WEB/Activos Criticos

Cambio futuro esperado:

Convertirlo en gate SEO de web nueva y redisenos, no en arquitecto paralelo.

## 7. Que se debe archivar o mover en el futuro

No se archiva ahora. Se propone:

| Elemento | Accion futura |
|---|---|
| `agents/seo/semrush-workflows.md` | Dividir por area o mover a `procedimientos/semrush-seo.md` y referencias SEM/Agency si aplica |
| `agents/seo/referencias/seo-onpage-semrush.md` | Mover a referencia externa versionada o dejar como documento de estudio, no prompt |
| `agents/docente/seo/aprendizajes/2026-05-11-ruta-formacion-agentes-seo.md` | Mantener como historico/insumo tras crear evaluaciones nuevas |
| `agents/docente/seo/aprendizajes/2026-05-11-matriz-competencias-agentes-seo.md` | Mantener como insumo, no aplicar tal cual |
| fuentes PDF | Mantener en `fuentes/` o mover a `historico/fuentes/` si se aprueba |

## 8. Que no debe tocarse todavia

No tocar todavia:

- `agents/seo/leader-seo.md`
- `agents/seo/seo-tecnico.md`
- `agents/seo/seo-organico.md`
- `agents/seo/seo-local.md`
- `agents/seo/seo-llms.md`
- `agents/seo/seo-web.md`
- `AGENTS.md`
- `CLAUDE.md`
- `sistema/protocolos/`
- clientes reales
- scripts
- conectores
- outputs historicos

Motivo:

Todavia falta transformar este mapa en evaluaciones por agente y Orden de Cambio.

## 9. Orden correcto de ejecucion desde aqui

### Paso 1 - Crear canon operativo resumido

Crear un canon SEO de maximo 8-12 paginas internas equivalentes, no un manual gigante.

Debe contener:

- principio base
- web nueva vs web existente
- fuentes de verdad
- matriz prioridad/riesgo
- regla URL-intencion
- proteccion de activos
- QA/changelog
- cierre con medicion

### Paso 2 - Crear procedimientos por herramienta

Convertir los modulos largos en procedimientos separados:

- SEMrush
- GSC
- GA4
- GTM
- NeuronWriter
- Screaming Frog
- GBP
- WordPress/WooCommerce
- Looker Studio
- Migraciones
- Schema
- Merchant Center
- IA externo
- Internacional

### Paso 3 - Crear evaluaciones por agente

Primero:

`agents/docente/seo/evaluaciones/lider-seo.md`

Luego:

- SEO Tecnico
- SEO Organico
- SEO Web
- SEO Local
- SEO LLMs

Cada evaluacion debe incluir:

- diagnostico actual
- 5 conductas nuevas maximas
- 3 casos practicos
- errores a evitar
- criterio de aprobado
- cambio minimo sugerido

### Paso 4 - Orden de Cambio

Antes de tocar prompts:

- archivo afectado
- seccion afectada
- conducta que cambia
- texto propuesto
- riesgo
- rollback
- prueba que debe pasar

### Paso 5 - Actualizacion gradual

Orden:

1. `leader-seo.md`
2. `seo-tecnico.md`
3. `seo-organico.md`
4. `seo-web.md`
5. `seo-local.md`
6. `seo-llms.md`

## 10. Decision final

El planteamiento anterior de "capacitar al SEO docente y luego conectar conocimientos" era util como primera aproximacion, pero insuficiente.

El planteamiento correcto ahora es:

```text
Docente SEO entiende el sistema
-> identifica canibalizaciones
-> crea canon y procedimientos
-> crea evaluaciones
-> propone cambios minimos
-> Fenix limpia estructura
-> Escolta valida cierre
-> agentes SEO quedan habilitados por pruebas, no por haber leido documentos
```

Hasta completar estos pasos, los agentes SEO no deben recibir cambios operativos.

## 11. Proximo artefacto recomendado

Crear:

`agents/docente/seo/canon/canon-operativo-seo.md`

Pero solo despues de aprobar esta estructura destino o confirmar que Rodrigo quiere que el Docente avance con esta arquitectura.
