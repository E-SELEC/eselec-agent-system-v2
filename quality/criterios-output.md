# Criterios de output por servicio

## Estado

- ID: P1-002
- Fecha: 2026-05-12
- Responsable: Codex + Arquitecto
- Sistema: E-SELEC Agent System v2
- Estado: vigente

## Objetivo

Definir que debe cumplir un entregable de E-SELEC para considerarse bueno.

Este documento convierte el diagnostico `quality/diagnostico-calidad.md` en contratos de salida verificables.

La regla es:

```text
Un output no esta terminado porque suena bien.
Esta terminado cuando cumple el objetivo, usa datos suficientes, declara limites y deja una decision accionable.
```

## Criterios universales

Todo output debe cumplir estos criterios antes de entregarse.

| Criterio | Pregunta de control | Bloquea si falla |
|---|---|---|
| Objetivo claro | Se entiende para que existe el output? | Si |
| Audiencia clara | Esta escrito para Rodrigo, cliente final o equipo interno? | Si |
| Fuentes declaradas | Dice con que datos se hizo? | Si, si hay decision de negocio |
| Datos faltantes | Dice que no se pudo verificar? | Si, si puede cambiar la conclusion |
| Decision accionable | Deja claro que hacer despues? | Si |
| Prioridad | Distingue urgente/importante/rutinario o impacto/esfuerzo cuando aplica? | Si |
| Evidencia | Cada hallazgo importante tiene razon o dato detras? | Si |
| No inventa | No rellena huecos con suposiciones no marcadas? | Si |
| Tono adecuado | Usa lenguaje claro para la audiencia? | No siempre, pero debe corregirse |
| Cierre | Explica estado, limites y siguiente paso? | Si |

## Escala de calidad

Usar esta escala internamente antes de cerrar:

| Nivel | Estado | Significado |
|---|---|---|
| 0 | Bloqueado | Falta informacion critica o hay riesgo de decision falsa |
| 1 | Parcial | Util con datos incompletos, debe marcar limitaciones |
| 2 | Aceptable | Cumple objetivo basico con evidencia suficiente |
| 3 | Bueno | Prioriza, explica impacto y deja siguiente accion clara |
| 4 | Excelente | Ademas anticipa riesgos, dependencias y criterios de validacion |

Regla:

- Nivel 0 no se entrega como output final.
- Nivel 1 se entrega solo si se marca como parcial.
- Nivel 2 es minimo aceptable.
- Nivel 3 es el estandar E-SELEC.
- Nivel 4 es deseable en estrategia, auditorias e informes importantes.

## Contrato 1 - Auditoria de cliente

Usar para:

- `client-audit`;
- revision general de cliente;
- "como esta este cliente";
- inicio de trabajo con cliente existente;
- actualizacion de `context.md`.

### Objetivo

Entender el estado real del cliente y decidir una sola proxima prioridad logica.

### Inputs minimos

- `clients/[cliente]/context.md`
- `clients/[cliente]/log.md`
- `clients/[cliente]/mensajes.md`
- `clients/[cliente]/tasks.md` si existe
- `clients/[cliente]/memory.md` si existe
- fuentes vivas disponibles si el diagnostico depende de datos recientes

### Estructura obligatoria

```text
# Auditoria: [cliente]
Fecha:
Nivel de datos: completo / parcial / minimo

## 1. Snapshot del negocio
## 2. Estado de presencia digital
## 3. Servicios E-SELEC activos
## 4. Hallazgos principales
## 5. Bloqueos o datos faltantes
## 6. Proxima prioridad unica
## 7. Acciones siguientes
## 8. Notas para agentes
```

### Criterios de aceptacion

- Resume el negocio en maximo 2 frases.
- No enumera mas de 5 hallazgos principales.
- Incluye una prioridad unica, no una lista plana de tareas.
- Distingue estado real de deseo o plan.
- Marca datos faltantes como `pendiente de verificar`.
- Si actualiza `context.md`, registra que cambio.

### Bloquea si

- no existe `context.md` y el cliente no esta siendo creado;
- hay contradiccion entre `context.md` y `log.md` que cambia la prioridad;
- faltan datos criticos para decidir y el output no se marca como parcial;
- propone ejecutar produccion sin aplicar activos criticos.

### Checklist de revision

- [ ] Lei contexto, log, mensajes y memoria disponible.
- [ ] No repeti tareas ya completadas en log.
- [ ] Identifique maximo una prioridad principal.
- [ ] Marque datos faltantes.
- [ ] Actualice o propuse actualizar `context.md` si habia datos nuevos.

## Contrato 2 - Auditoria SEO

Usar para:

- `seo-audit`;
- SEO tecnico;
- perdida de trafico;
- problemas de indexacion;
- revision on-page;
- SEO local cuando aplique.

### Objetivo

Detectar los problemas SEO que mas afectan visibilidad, trafico o conversion organica, y priorizar las correcciones.

### Inputs minimos

- URL o dominio.
- Objetivo SEO del cliente.
- Estado de servicios contratados.
- `context.md`, `log.md`, `memory.md`.
- GSC si existe.
- SEMrush si existe.
- Datos tecnicos disponibles: sitemap, robots, PageSpeed, crawl, CMS.

### Jerarquia de fuentes

1. GSC: impresiones, clics, CTR, queries, paginas y fechas reales.
2. SEMrush: competidores, visibilidad estimada, gaps, backlinks, keyword difficulty.
3. PageSpeed/Chrome: rendimiento y Core Web Vitals.
4. Sitio renderizado: estructura, schema, UX tecnico.
5. Contexto del cliente: objetivos, servicios, historial.

Si falta GSC o SEMrush, marcar diagnostico como parcial.

### Estructura obligatoria

```text
# Auditoria SEO: [cliente / dominio]
Fecha:
Nivel de datos:
Fuentes usadas:

## 1. Resumen ejecutivo
## 2. Top 3 problemas prioritarios
## 3. Hallazgos tecnicos
## 4. Hallazgos on-page/contenido
## 5. Hallazgos autoridad/local/LLM si aplica
## 6. Matriz impacto/esfuerzo
## 7. Plan de accion priorizado
## 8. Datos faltantes y como obtenerlos
```

### Criterios de aceptacion

- Cada hallazgo importante incluye evidencia.
- Distingue tecnico, contenido, autoridad, local y medicion.
- No diagnostica schema solo con `curl` o `web_fetch`.
- Cruza GSC + SEMrush cuando ambas fuentes existan.
- Prioriza por impacto y esfuerzo.
- No propone contenido si hay bloqueo tecnico critico sin resolver.

### Bloquea si

- no hay dominio o URL;
- el output afirma datos de GSC/GA4/SEMrush sin haberlos consultado;
- detecta riesgo en produccion y no aplica activos criticos;
- falta acceso a fuentes clave y no se marca como parcial.

### Checklist de revision

- [ ] Declare fuentes usadas.
- [ ] Marque fuentes faltantes.
- [ ] Inclui evidencia por hallazgo.
- [ ] Priorice top 3.
- [ ] Separe quick wins de correcciones estructurales.
- [ ] Deje siguiente accion concreta.

## Contrato 3 - Informe mensual de cliente

Usar para:

- `reports-cliente`;
- revision mensual;
- entregable ejecutivo para cliente.

### Objetivo

Comunicar que paso, que significan los resultados y que decision recomienda E-SELEC.

### Inputs minimos

- Periodo del informe.
- Servicios activos.
- Acciones del mes desde `log.md`.
- Datos reales disponibles: GA4, GSC, GBP, Ads, redes, ventas o CRM.
- Objetivos del cliente.
- Pendientes o bloqueos.

### Estructura obligatoria

```text
# Informe mensual: [cliente]
Periodo:
Nivel de datos:

## 1. Resumen ejecutivo
## 2. Que se hizo este mes
## 3. Resultados principales
## 4. Lectura de negocio
## 5. Alertas o bloqueos
## 6. Recomendacion del proximo mes
## 7. Acciones propuestas
```

### Criterios de aceptacion

- No es una lista de tareas; interpreta resultados.
- Traduce metricas a negocio.
- Indica que subio, bajo o quedo igual.
- Explica por que importa.
- Incluye maximo 3 prioridades del siguiente periodo.
- Si faltan datos, lo dice sin esconderlo.

### Bloquea si

- no hay periodo definido;
- no hay datos ni acciones del mes y no se marca como informe parcial;
- contradice `log.md`;
- promete resultados no medidos.

### Checklist de revision

- [ ] Periodo claro.
- [ ] Acciones ejecutadas cruzadas con log.
- [ ] Datos reales diferenciados de observaciones.
- [ ] Recomendacion clara.
- [ ] Lenguaje adecuado al nivel tecnico del cliente.

## Contrato 4 - Proximos pasos / roadmap

Usar para:

- `reports-proxpasos`;
- plan de 30 dias;
- propuesta de trabajo posterior a auditoria;
- priorizacion semanal.

### Objetivo

Decidir que hacer despues, en que orden y por que.

### Inputs minimos

- Estado actual.
- Objetivo de negocio.
- Pendientes de log/mensajes/tasks.
- Restricciones de cliente.
- Datos disponibles.

### Estructura obligatoria

```text
# Proximos pasos: [cliente]

## 1. Situacion actual
## 2. Cuello de botella principal
## 3. Prioridades
## 4. Plan 7 dias
## 5. Plan 30 dias
## 6. Dependencias
## 7. Decisiones que necesita Rodrigo
```

### Criterios de aceptacion

- Maximo 3 prioridades activas.
- Cada accion tiene motivo.
- Incluye impacto, esfuerzo y dependencia.
- No mezcla ideas de ampliacion con tareas contratadas sin marcarlo.
- No propone acciones que requieren datos faltantes sin pedirlos.

### Bloquea si

- hay una urgencia no atendida;
- el plan depende de acceso inexistente y no propone como obtenerlo;
- incluye mas de 5 acciones sin priorizar.

## Contrato 5 - CRO / pagina

Usar para:

- `page-cro`;
- landing page;
- home;
- pricing;
- feature page;
- pagina que no convierte.

### Objetivo

Identificar fricciones de conversion y proponer cambios accionables priorizados.

### Nivel CRO

- PC3: pagina revisada, objetivo/trafico/conversion medidos, tracking comprobado y recomendaciones priorizadas.
- PC2: pagina revisada y objetivo claro, pero faltan datos cuantitativos o tracking completo.
- PC1: captura/texto suficiente para orientar, pero faltan trafico, objetivo medido o contexto.
- PC0: falta pagina, objetivo de conversion o audiencia.

### Inputs minimos

- URL o captura.
- Objetivo de conversion.
- Fuente de trafico.
- Audiencia.
- Datos de conversion si existen.
- Estado de tracking.

### Estructura obligatoria

```text
# CRO: [pagina]

## 1. Objetivo de conversion
## 2. Diagnostico rapido
## 3. Quick wins
## 4. Cambios de alto impacto
## 5. Ideas de test
## 6. Copy alternativo
## 7. Riesgos y dependencias
```

### Criterios de aceptacion

- Clasifica nivel PC0/PC1/PC2/PC3.
- Evalua propuesta de valor, CTA, jerarquia visual, confianza, objeciones y friccion.
- Distingue cambio recomendado de test recomendado.
- No recomienda test A/B si no hay trafico suficiente.
- Incluye copy alternativo solo para elementos clave.
- Considera mobile.
- Declara medicion disponible y datos faltantes.
- Prioriza por impacto/esfuerzo.

### Bloquea si

- no se conoce el objetivo de conversion;
- no se puede ver la pagina y no hay captura;
- hay fallo tecnico critico que impide evaluar conversion.
- se piden cambios reales en web/CMS/formularios/Ads/tracking sin Orden de Cambio.

## Contrato 6 - SEM / Paid Ads

Usar para:

- Google Ads;
- Meta Ads;
- LinkedIn Ads;
- auditoria de campanas;
- propuesta de campana.

### Objetivo

Mejorar eficiencia de adquisicion o definir una campana medible sin quemar presupuesto.

### Inputs minimos

- Plataforma.
- Objetivo.
- Presupuesto.
- Conversion esperada.
- Landing page.
- Tracking/pixel.
- Audiencia.
- Estado historico si existe.

### Estructura obligatoria

```text
# Paid Ads: [cliente / plataforma]

## 1. Objetivo y restriccion principal
## 2. Estado de tracking
## 3. Diagnostico o estrategia
## 4. Estructura de campana
## 5. Audiencias
## 6. Creatividades / mensajes
## 7. Presupuesto y aprendizaje
## 8. Riesgos y checks antes de lanzar
```

### Criterios de aceptacion

- No lanza ni recomienda escalar sin tracking.
- Distingue problema de anuncio vs landing.
- Incluye metrica primaria: CPA, ROAS, leads, CTR, CPC, CPM segun objetivo.
- Incluye fase de aprendizaje.
- Incluye exclusiones y riesgos de solapamiento cuando aplica.

### Bloquea si

- no hay objetivo ni conversion definida;
- no hay presupuesto;
- no hay tracking para campanas de conversion;
- implica cambios reales en Ads sin Orden de Cambio.

## Contrato 7 - Social / contenido

Usar para:

- calendario de redes;
- posts;
- estrategia social;
- captions;
- ideas de contenido.

### Objetivo

Crear contenido coherente con objetivo, audiencia, canal y fase del cliente.

### Inputs minimos

- Canal.
- Audiencia.
- Objetivo: visibilidad, comunidad, leads, ventas, reputacion.
- Tono de marca.
- Servicios/productos.
- Calendario o frecuencia.

### Estructura obligatoria

```text
# Social: [cliente / canal]

## 1. Objetivo
## 2. Lineas de contenido
## 3. Piezas propuestas
## 4. Copy/caption
## 5. Recomendacion visual
## 6. CTA
## 7. Medicion
```

### Criterios de aceptacion

- No crea contenido generico que podria servir para cualquier cliente.
- Cada pieza tiene objetivo.
- El CTA coincide con la fase del funnel.
- El tono coincide con marca y publico.
- Si falta identidad de marca, se marca.

### Bloquea si

- no hay marca/tono suficiente para contenido visible;
- el contenido promete informacion no verificada;
- usa claims legales/salud/finanzas sin fuente.

## Contrato 8 - Web / arquitectura

Usar para:

- estructura web;
- menu;
- sitemap;
- landing;
- WordPress/WooCommerce;
- cambios de URLs.

### Objetivo

Proponer o modificar estructura web sin romper SEO, conversion ni operacion.

### Inputs minimos

- Objetivo de la web.
- Audiencia.
- Servicios/productos.
- CMS.
- Estado SEO actual.
- URLs existentes si hay rediseño.
- Tracking.
- Restricciones tecnicas.

### Estructura obligatoria

```text
# Web: [cliente]

## 1. Objetivo de la estructura
## 2. Mapa de paginas
## 3. Jerarquia y navegacion
## 4. SEO por pagina
## 5. Conversion por pagina
## 6. Riesgos tecnicos
## 7. Redirecciones / tracking / lanzamiento
```

### Criterios de aceptacion

- Cada pagina tiene objetivo.
- URLs nuevas tienen motivo.
- Cambios de URLs consideran 301.
- SEO valida arquitectura antes de lanzamiento cuando aplica.
- Tracking y formularios se contemplan.
- Activos criticos se aplican antes de produccion.

### Bloquea si

- hay cambio de URLs sin plan de redirecciones;
- hay WooCommerce/checkout/pagos sin Orden de Cambio;
- no se conoce CMS o acceso necesario para implementar;
- afecta produccion sin aprobacion.

## Contrato 9 - Copy / contenido

Usar para:

- landing copy;
- anuncios;
- emails;
- posts de blog;
- metadatos;
- textos comerciales.

### Objetivo

Crear texto persuasivo, claro y adaptado al canal sin sonar generico ni inflado.

### Inputs minimos

- Audiencia.
- Oferta.
- Dolor/deseo.
- Diferenciador.
- Canal.
- Accion deseada.
- Tono.
- Restricciones.

### Estructura obligatoria

Depende del canal, pero siempre debe incluir:

- objetivo del texto;
- version final;
- razonamiento breve;
- variantes si se pidieron;
- notas de uso.

### Criterios de aceptacion

- Dice algo especifico del cliente.
- Evita frases comodin.
- Tiene CTA claro.
- No exagera claims.
- Se adapta al canal.
- Si es SEO, respeta intencion de busqueda.

### Bloquea si

- no se sabe que oferta se vende;
- no hay audiencia;
- exige claims que no se pueden sostener.

## Contrato 10 - Agencia / estrategia interna

Usar para:

- captacion;
- propuestas internas;
- pricing;
- onboarding;
- retencion;
- reputacion E-SELEC.

### Objetivo

Tomar decisiones internas que mejoren E-SELEC como negocio sin mezclarlo con trabajo de clientes.

### Inputs minimos

- `agency/context.md`
- `agency/log.md`
- `agency/mensajes.md`
- preferencias de Rodrigo;
- datos reales si existen.

### Estructura obligatoria

```text
# Agencia: [tema]

## 1. Situacion
## 2. Problema principal
## 3. Opciones
## 4. Recomendacion
## 5. Riesgos
## 6. Siguiente accion
```

### Criterios de aceptacion

- No mezcla cliente con agencia.
- Incluye decision recomendada, no solo opciones.
- Considera coste, tiempo y retorno.
- Registra aprendizajes si Rodrigo corrige.

### Bloquea si

- usa datos de cliente sin necesidad;
- propone cambios comerciales sin contexto suficiente;
- requiere acceso o accion real sin protocolo.

## Contrato 11 - Verificacion de medicion

Usar para:

- comprobar GA4, GSC, GBP, SEMrush, Ads o conversiones;
- decidir si una auditoria puede ser final o debe ser parcial;
- preparar informes mensuales;
- resolver dudas de tracking, fuentes vivas o lineas base.

### Objetivo

Establecer si los datos disponibles permiten tomar decisiones fiables.

### Inputs minimos

- cliente y dominio;
- servicio afectado;
- periodo de analisis;
- contexto, log, mensajes y memoria;
- fuentes vivas o exports disponibles;
- decision que se quiere tomar.

### Estructura obligatoria

```text
# Verificacion de medicion: [cliente]
Fecha:
Periodo revisado:
Servicio afectado:
Nivel de medicion:
Permiso de uso:

## 1. Resumen ejecutivo
## 2. Fuentes revisadas
## 3. Contradicciones o riesgos
## 4. Que se puede afirmar
## 5. Que no se puede afirmar todavia
## 6. Impacto en el siguiente output
## 7. Proxima accion unica
```

### Criterios de aceptacion

- Identifica fuentes verificadas y faltantes.
- Confirma si cada fuente corresponde al cliente correcto.
- Declara periodo y alcance.
- Clasifica Nivel 0/1/2/3.
- Dice si el siguiente output puede ser final, parcial, orientativo o bloqueado.
- No pide ni registra secretos.

### Bloquea si

- no se puede asociar la fuente al cliente correcto;
- hay contradiccion que cambia la decision;
- se afirma rendimiento, trafico, ranking o conversion sin fuente verificada;
- la siguiente accion implica produccion sin protocolo.

## Contrato 12 - Ingesta de evidencia

Usar para:

- convertir exports o capturas en evidencia interna;
- resumir outputs legacy antes de usarlos en v2;
- preparar datos de GSC, GA4, SEMrush, GBP, Ads, WordPress o WooCommerce;
- decidir que puede guardarse en GitHub y que debe quedar fuera.

### Objetivo

Crear evidencia minima, trazable y segura sin guardar dumps, secretos ni datos personales.

### Inputs minimos

- cliente;
- fuente original;
- dominio/cuenta/propiedad;
- periodo;
- servicio afectado;
- decision que soporta;
- archivo/export/captura/output origen.

### Estructura obligatoria

```text
# Evidencia [tema] - [cliente]

## Estado
## Proposito
## Fuentes revisadas
## Evidencia extraida
## Contradicciones o dudas
## Que permite hacer ahora
## Que no permite hacer todavia
## Proxima accion unica
```

### Criterios de aceptacion

- Clasifica evidencia E0/E1/E2/E3.
- Declara fuente, periodo y cliente/dominio.
- Separa dato real, estimacion, hipotesis y conclusion.
- Resume solo lo necesario.
- Declara limitaciones.
- No contiene secretos, PII ni exports brutos.
- Actualiza manifest/log/registro si se guarda.

### Bloquea si

- contiene secretos, cookies, tokens, claves o passwords;
- contiene PII innecesaria;
- no se puede confirmar cliente/dominio;
- no hay periodo;
- se quiere usar E1/E2 como output final.

## Contrato 13 - Analytics tracking

Usar para:

- auditoria GA4/GTM;
- planes de eventos;
- conversion tracking;
- UTMs;
- validacion de formularios, llamadas, WhatsApp o compras;
- medicion para CRO, Ads, SEO o informes.

### Objetivo

Definir o auditar medicion que permita tomar decisiones reales sin duplicar eventos, perder conversiones ni enviar datos sensibles.

### Inputs minimos

- cliente;
- decision que debe informar la medicion;
- conversion principal;
- herramientas actuales;
- contexto tecnico;
- restricciones de privacidad/consentimiento;
- evidencia o estado actual si existe.

### Estructura obligatoria

```text
# Plan de tracking: [cliente / sitio]

Fecha:
Nivel de tracking:
Modo:
Herramientas:
Produccion tocada:

## 1. Decision que debe informar
## 2. Estado actual
## 3. Conversiones principales
## 4. Eventos recomendados
## 5. Implementacion propuesta
## 6. Validacion
## 7. Riesgos y bloqueos
## 8. Datos faltantes
## 9. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica Nivel T0/T1/T2/T3.
- Cada evento tiene trigger, propiedades y decision asociada.
- Distingue evento normal de conversion.
- Revisa duplicados.
- Revisa consentimiento y privacidad.
- No incluye PII ni secretos.
- No propone publicar cambios sin Orden de Cambio.

### Bloquea si

- no hay objetivo de negocio o conversion;
- requiere acceso sensible no disponible;
- hay datos contradictorios que cambian el plan;
- se pide publicar GTM/GA4/pixels sin aprobacion;
- el plan enviaria PII a herramientas de analytics o Ads.

## Contrato 14 - Site architecture / arquitectura web

Usar para:

- estructura web;
- sitemap visual;
- menu y navegacion;
- URLs;
- redirecciones;
- enlazado interno;
- redisenos;
- arquitectura para SEO local, servicios, e-commerce o contenido.

### Objetivo

Proponer una estructura web clara, accionable y segura, sin romper SEO, conversion, tracking ni operaciones reales.

### Inputs minimos

- cliente o dominio;
- objetivo de la web;
- audiencia;
- servicios/productos;
- CMS;
- URLs existentes si hay redisenio o reestructura;
- estado SEO/conversion disponible;
- restricciones tecnicas;
- fuentes usadas.

### Estructura obligatoria

```text
# Arquitectura web: [cliente / sitio]
Fecha:
Nivel de arquitectura:
Alcance:
Fuentes usadas:
Produccion tocada:

## 1. Objetivo de la arquitectura
## 2. Estado actual
## 3. Principios de diseno
## 4. Mapa de paginas propuesto
## 5. Mapa de URLs
## 6. Navegacion
## 7. Enlazado interno
## 8. Redirecciones y riesgos SEO
## 9. Dependencias
## 10. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel SA0/SA1/SA2/SA3.
- Cada pagina principal tiene objetivo.
- Las URLs propuestas tienen motivo.
- Distingue pagina nueva, mantener, fusionar, redirigir, revisar o eliminar.
- Los cambios de URLs contemplan 301.
- Header, footer, mobile y breadcrumbs se contemplan cuando aplican.
- El enlazado interno apoya SEO y conversion.
- Marca datos faltantes y riesgos de produccion.
- No toca WordPress, WooCommerce, redirects, tracking ni formularios sin Orden de Cambio.

### Bloquea si

- no hay objetivo de la web;
- no hay dominio o cliente claro;
- se pide reestructura sin inventario de URLs;
- se pide cambiar URLs sin plan de redirecciones;
- hay WooCommerce, checkout, pagos, formularios o reservas sin Orden de Cambio;
- afirma rendimiento SEO/conversion sin fuente verificada;
- contradice `context.md` o `log.md`.

## Contrato 15 - Schema markup / datos estructurados

Usar para:

- schema JSON-LD;
- structured data;
- rich results;
- Organization/WebSite/LocalBusiness;
- BreadcrumbList;
- Article/BlogPosting;
- Product/Offer;
- FAQPage;
- Review/AggregateRating;
- errores de schema en Search Console.

### Objetivo

Crear o corregir datos estructurados que representen contenido real, visible y verificable sin prometer rich results ni tocar produccion sin aprobacion.

### Inputs minimos

- cliente o dominio;
- URL o pagina;
- tipo de pagina;
- contenido visible;
- schema actual si existe;
- CMS o stack;
- objetivo del schema;
- fuentes usadas.

### Estructura obligatoria

```text
# Schema markup: [cliente / pagina]
Fecha:
Nivel de schema:
URL:
Tipo de pagina:
Fuentes usadas:
Produccion tocada:

## 1. Objetivo
## 2. Contenido visible verificado
## 3. Schema actual
## 4. Schema recomendado
## 5. JSON-LD propuesto
## 6. Validacion
## 7. Implementacion
## 8. Bloqueos y datos faltantes
## 9. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel SM0/SM1/SM2/SM3.
- El schema coincide con contenido visible.
- No inventa reviews, ratings, precios, stock, horarios, coordenadas, autores ni FAQ.
- Usa JSON-LD salvo razon tecnica contraria.
- Revisa duplicados por plugins SEO o WooCommerce.
- Diferencia errores de warnings.
- Declara validacion hecha o pendiente.
- No promete rich results ni rankings.
- No toca CMS, plugin, tema, GTM ni deploy real sin Orden de Cambio.

### Bloquea si

- no hay URL, pagina o contenido visible;
- se pide marcar contenido inexistente u oculto;
- se pide inventar rating/reviews/precios/stock/horarios;
- hay schema duplicado y no se sabe quien lo genera;
- el cambio requiere produccion sin aprobacion;
- contradice contenido visible, `context.md` o `log.md`.

## Contrato 16 - AI SEO / visibilidad en respuestas AI

Usar para:

- AI SEO;
- AEO/GEO/LLM SEO;
- auditorias de ChatGPT, Perplexity, Gemini, Claude, Copilot o AI Overviews;
- contenido citable;
- respuestas directas;
- presencia en terceros;
- robots.txt para crawlers AI;
- share of voice AI.

### Objetivo

Medir y mejorar la probabilidad de que el cliente sea encontrado, mencionado o citado por respuestas AI con evidencia concreta, sin prometer resultados.

### Inputs minimos

- cliente/dominio;
- mercado e idioma;
- queries objetivo;
- plataformas a revisar;
- paginas candidatas;
- fecha de prueba;
- competidores si existen;
- fuentes usadas.

### Estructura obligatoria

```text
# Auditoria AI SEO: [cliente]
Fecha:
Nivel de evidencia AI:
Mercado/idioma:
Fuentes usadas:
Produccion tocada:

## 1. Objetivo
## 2. Consultas prioritarias
## 3. Visibilidad AI actual
## 4. Diagnostico
## 5. Brechas frente a competidores
## 6. Plan priorizado
## 7. Riesgos y limites
## 8. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel AI0/AI1/AI2/AI3.
- Declara query, plataforma, fecha y mercado.
- Distingue cita, mencion, enlace y trafico.
- No usa estadisticas sin fuente y fecha.
- Cruza SEO, schema, arquitectura y extractabilidad.
- Prioriza acciones por query/pagina.
- No promete aparecer en respuestas AI.
- No toca robots.txt, CDN, noindex, sitemap ni contenido publicado sin Orden de Cambio.

### Bloquea si

- no hay dominio o cliente claro;
- no hay queries objetivo;
- se quieren conclusiones sin pruebas fechadas o sin marcar parcialidad;
- se pide prometer citas AI;
- se pide cambiar robots.txt/CDN/noindex/sitemap sin aprobacion;
- los claims de autoridad o datos no son verificables.

## Contrato 17 - Content strategy / estrategia de contenido

Usar para:

- estrategia de contenido;
- calendario editorial;
- blog strategy;
- topic clusters;
- pilares de contenido;
- contenido SEO;
- contenido AI SEO;
- ideas de contenido;
- roadmap editorial;
- que publicar y en que orden.

### Objetivo

Decidir que contenido crear, en que orden y por que, conectando negocio, SEO, AI SEO, ventas y recursos disponibles.

### Inputs minimos

- cliente o agencia;
- objetivo principal;
- audiencia;
- oferta/servicios;
- mercado e idioma;
- evidencia disponible: GSC, SEMrush, AI SEO, ventas, soporte, log o research;
- recursos y restricciones;
- contenidos existentes si existen.

### Estructura obligatoria

```text
# Estrategia de contenido: [cliente]
Fecha:
Nivel de estrategia:
Objetivo principal:
Objetivo secundario:
Fuentes usadas:
Produccion tocada:

## 1. Diagnostico breve
## 2. Audiencia y oferta
## 3. Pilares de contenido
## 4. Clusters y temas
## 5. Calendario 30/60/90 dias
## 6. Enlazado y distribucion
## 7. Riesgos y datos faltantes
## 8. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel CS0/CS1/CS2/CS3.
- Cada pilar conecta con servicio, audiencia y objetivo.
- Cada tema tiene intencion, etapa y motivo.
- Prioriza por negocio, evidencia, conversion, autoridad y esfuerzo.
- Diferencia contenido SEO, AI SEO, comercial, local y socializable cuando aplica.
- Declara datos faltantes.
- No inventa volumen, dificultad, conversiones, rankings ni resultados.
- No publica ni toca CMS sin Orden de Cambio.

### Bloquea si

- no hay objetivo de negocio;
- no hay audiencia u oferta clara;
- se pretende plan definitivo sin evidencia suficiente;
- los temas no conectan con servicios reales;
- requiere nuevas paginas/URLs sin revisar arquitectura;
- promete trafico, leads o citas AI sin base;
- repite contenidos ya fallidos o descartados en log.

## Contrato 18 - Copywriting / copy comercial

Usar para:

- titulares;
- hero sections;
- paginas de servicio;
- landing pages;
- CTAs;
- value proposition;
- copy web;
- copy SEO/AI SEO;
- textos comerciales.

### Objetivo

Escribir copy claro, especifico y persuasivo que conecte oferta, audiencia y accion sin inventar claims.

### Inputs minimos

- cliente o agencia;
- pieza/canal;
- audiencia;
- oferta;
- objetivo;
- accion primaria;
- tono;
- pruebas o claims permitidos;
- restricciones.

### Estructura obligatoria

```text
# Copywriting: [cliente / pieza]
Fecha:
Nivel de copy:
Pieza:
Audiencia:
Objetivo:
Fuentes usadas:
Produccion tocada:

## 1. Contexto
## 2. Copy final
## 3. Variantes
## 4. Notas de uso
## 5. Riesgos o datos faltantes
## 6. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel CW0/CW1/CW2/CW3.
- Headline claro en 5 segundos.
- CTA alineado con la accion primaria.
- Beneficios concretos, no features sueltas.
- Tono acorde a cliente, canal y audiencia.
- No usa frases genericas intercambiables.
- No inventa cifras, pruebas, testimonios, precios, garantias ni resultados.
- Marca datos faltantes antes de publicar.

### Bloquea si

- falta oferta, audiencia u objetivo;
- no hay accion primaria;
- se piden claims no verificables;
- contradice contexto, log o marca;
- se quiere publicar en web, Ads, email o CMS sin aprobacion.

## Contrato 19 - Copy editing / revision de copy

Usar para:

- revisar copy existente;
- proofread;
- pulir texto;
- mejorar claridad;
- revisar claims;
- limpiar tono;
- hacer copy sweep;
- mejorar CTA;
- detectar texto generico o demasiado largo.

### Objetivo

Mejorar un texto existente preservando su mensaje central, corrigiendo claridad, tono, beneficios, claims, especificidad y CTA.

### Inputs minimos

- texto base;
- cliente o agencia;
- pieza/canal;
- audiencia;
- objetivo;
- accion primaria;
- tono esperado;
- pruebas o claims permitidos.

### Estructura obligatoria

```text
# Revision de copy: [cliente / pieza]
Fecha:
Nivel de edicion:
Pieza:
Audiencia:
Objetivo:
Fuentes usadas:
Produccion tocada:

## 1. Diagnostico breve
## 2. Version editada
## 3. Cambios principales
## 4. Claims y pruebas
## 5. Alternativas utiles
## 6. Datos faltantes o dudas
## 7. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel CE0/CE1/CE2/CE3.
- Preserva mensaje central.
- Mejora claridad y especificidad.
- Mantiene tono de marca/canal.
- Revisa claims y pruebas.
- Diferencia cambios obligatorios de mejoras opcionales.
- No agrega cifras, promesas, testimonios, precios ni garantias.
- Deja CTA claro y siguiente accion.

### Bloquea si

- no hay texto base;
- falta objetivo o audiencia;
- hay claims sensibles sin fuente;
- contradice contexto, log o marca;
- se quiere publicar en web, Ads, email o CMS sin aprobacion.

## Contrato 20 - Form CRO / formularios

Usar para:

- `form-cro`;
- formularios de contacto, demo, presupuesto, lead magnet, encuesta o aplicacion;
- abandono de formulario;
- friccion por campos;
- errores, validacion, mobile o privacidad;
- formularios conectados a CRM, email, Ads o analytics.

### Objetivo

Mejorar la tasa de completado de un formulario sin perder datos necesarios, romper seguimiento, danar ventas ni capturar informacion sensible innecesaria.

### Inputs minimos

- cliente o pagina;
- formulario visible, captura o inventario de campos;
- objetivo del formulario;
- que ocurre despues del envio;
- campos requeridos/opcionales;
- medicion disponible: views, starts, submits, completion, errors o field drop-off;
- restricciones de privacidad, CRM, ventas o CMS.

### Estructura obligatoria

```text
# Auditoria Form CRO: [cliente / formulario]
Fecha:
Nivel Form CRO:
Formulario:
Objetivo:
Fuentes usadas:
Produccion tocada:

## 1. Diagnostico ejecutivo
## 2. Estado de medicion
## 3. Inventario de campos
## 4. Hallazgos
## 5. Diseno recomendado
## 6. Tests posibles
## 7. Riesgos y dependencias
## 8. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel FC0/FC1/FC2/FC3.
- Cada campo requerido tiene motivo y uso real.
- Distingue campo necesario, opcional, eliminable o sensible.
- Revisa labels, placeholders, ayuda, errores, CTA, mensaje de exito y mobile.
- Revisa confianza: privacidad, expectativa de respuesta, seguridad y prueba cercana.
- Revisa medicion y marca datos faltantes.
- No recomienda test A/B sin trafico, baseline y tracking.
- No toca formulario, CRM, GTM, CMS ni emails sin Orden de Cambio.

### Bloquea si

- no hay formulario visible, captura o inventario de campos;
- no se conoce la conversion buscada;
- el formulario captura PII sensible sin justificacion;
- la recomendacion puede romper CRM, ventas, tracking o cumplimiento;
- se piden cambios reales sin aprobacion.

## Contrato 21 - A/B testing / experimentos

Usar para:

- `ab-test-setup`;
- split tests;
- tests de pagina, CTA, copy, formulario, pricing, checkout o flujo;
- hipotesis CRO;
- sample size, MDE, baseline, duracion o significancia;
- decision de ganador/perdedor/inconcluso.

### Objetivo

Disenar experimentos que produzcan aprendizaje confiable y decisiones accionables, evitando tests sin medicion, sin trafico o con interpretaciones falsas.

### Inputs minimos

- observacion o problema que origina el test;
- hipotesis;
- control y variante;
- metrica primaria;
- metricas secundarias y guardrails;
- baseline de conversion;
- trafico disponible;
- herramienta o forma de ejecucion;
- periodo minimo y riesgos.

### Estructura obligatoria

```text
# Plan A/B test: [cliente / test]
Fecha:
Nivel test:
Pagina/flujo:
Produccion tocada:

## 1. Hipotesis
## 2. Diseno
## 3. Metricas
## 4. Muestra y viabilidad
## 5. QA y tracking
## 6. Decision
## 7. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel AB0/AB1/AB2/AB3.
- Formula hipotesis con observacion, cambio, resultado, audiencia y metrica.
- Control y variante tienen un cambio principal.
- Define metrica primaria, secundarias y guardrails.
- Declara baseline, trafico, MDE, muestra o limitacion de muestra.
- Define duracion minima y criterio para no parar temprano.
- Incluye QA y verificacion de tracking.
- Recomienda cambio directo o investigacion cualitativa si no hay trafico suficiente.
- No llama ganador a un resultado inconcluso.

### Bloquea si

- falta hipotesis o problema real;
- no hay conversion/metrica primaria;
- el tracking no esta verificado;
- no hay trafico suficiente y se exige significancia;
- el experimento toca precio, checkout, Ads, tracking o web sin Orden de Cambio.

## Contrato 22 - Signup Flow CRO / registro

Usar para:

- `signup-flow-cro`;
- signup, registro, creacion de cuenta o trial;
- baja conversion de registro;
- friccion por campos, password, SSO, captcha o verificacion;
- account creation, trial activation o signup abandonment.

### Objetivo

Reducir friccion de alta sin perder datos necesarios, romper autenticacion, incumplir requisitos legales ni perjudicar activacion posterior.

### Inputs minimos

- cliente, producto o flujo;
- tipo de signup: trial, freemium, pagado, waitlist, B2B o B2C;
- pasos/pantallas/capturas o inventario de campos;
- conversion objetivo;
- que ocurre despues del submit;
- metricas disponibles: view, start, step completion, submit, verification, activation handoff;
- restricciones de auth, compliance, pagos o CRM.

### Estructura obligatoria

```text
# Auditoria Signup Flow CRO: [cliente / flujo]
Fecha:
Nivel Signup Flow:
Flujo:
Conversion objetivo:
Fuentes usadas:
Produccion tocada:

## 1. Diagnostico ejecutivo
## 2. Mapa del flujo
## 3. Estado de medicion
## 4. Hallazgos
## 5. Flujo recomendado
## 6. Riesgo para onboarding
## 7. Tests posibles
## 8. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel SF0/SF1/SF2/SF3.
- Cada campo requerido tiene motivo antes del primer valor.
- Distingue datos necesarios ahora de datos que pueden pasar a onboarding.
- Revisa auth, SSO, password, verificacion, terminos, captcha, errores y mobile.
- Evalua si la mejora de signup puede empeorar activacion.
- Declara medicion disponible y datos faltantes.
- No recomienda test sin baseline, trafico y tracking.
- No toca auth, producto, pagos, CRM, email ni tracking sin Orden de Cambio.

### Bloquea si

- no hay flujo visible, captura o descripcion de pasos;
- no se conoce la conversion objetivo;
- hay requisitos legales/compliance desconocidos que cambian campos o verificacion;
- la recomendacion puede romper auth, pagos, CRM, seguridad o activacion;
- se piden cambios reales sin aprobacion.

## Contrato 23 - Onboarding CRO / activacion

Usar para:

- `onboarding-cro`;
- onboarding post-signup;
- activacion;
- first-run experience;
- aha moment;
- time-to-value;
- empty states, checklist, tours, tooltips o setup;
- usuarios que se registran pero no usan el producto.

### Objetivo

Aumentar activacion y reducir tiempo hasta primer valor con un flujo medible, claro y conectado a retencion.

### Inputs minimos

- producto o servicio;
- promesa de valor;
- usuario objetivo;
- evento de activacion o propuesta de evento;
- flujo post-signup;
- pasos, pantallas o capturas;
- metricas disponibles: activation rate, time-to-value, setup completion, drop-off, D1/D7/D30;
- canales de apoyo: email, in-app, soporte o CRM.

### Estructura obligatoria

```text
# Auditoria Onboarding CRO: [cliente / flujo]
Fecha:
Nivel Onboarding:
Flujo:
Activacion definida:
Fuentes usadas:
Produccion tocada:

## 1. Diagnostico ejecutivo
## 2. Definicion de activacion
## 3. Mapa del onboarding
## 4. Hallazgos
## 5. Flujo recomendado
## 6. Medicion
## 7. Tests posibles
## 8. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel OB0/OB1/OB2/OB3.
- Define o marca pendiente el evento de activacion.
- Conecta activacion con valor real y retencion, no solo con una pantalla vista.
- Revisa primera sesion, pasos, empty states, checklist, ayuda y usuarios atascados.
- Distingue onboarding in-app de emails de seguimiento.
- Declara medicion disponible y datos faltantes.
- No propone tests sin baseline, trafico y tracking.
- No toca producto, emails, CRM, tracking ni datos de usuario sin Orden de Cambio.

### Bloquea si

- no se conoce producto, usuario o promesa de valor;
- no hay activacion definida ni datos suficientes para proponerla;
- no se puede ver flujo, captura o pasos;
- se quieren conclusiones de retencion sin cohortes o sin marcar parcialidad;
- se piden cambios reales sin aprobacion.

## Contrato 24 - Popup CRO / overlays

Usar para:

- `popup-cro`;
- popups, modals, overlays, slide-ins, sticky bars o announcement banners;
- exit intent;
- email popup, lead capture popup o discount popup;
- scroll trigger, notification bar, overlay o interrupciones de conversion.

### Objetivo

Mejorar conversion con elementos interruptivos sin degradar experiencia, marca, SEO movil, accesibilidad ni privacidad.

### Inputs minimos

- cliente o pagina;
- objetivo del popup;
- oferta o mensaje;
- audiencia/segmento;
- paginas donde aparece;
- trigger y frecuencia;
- captura o copy actual/propuesto;
- medicion disponible: impressions, close, submit, conversion, bounce o revenue/leads;
- restricciones de privacidad, consentimiento, mobile y SEO.

### Estructura obligatoria

```text
# Auditoria Popup CRO: [cliente / popup]
Fecha:
Nivel Popup CRO:
Popup:
Objetivo:
Fuentes usadas:
Produccion tocada:

## 1. Diagnostico ejecutivo
## 2. Configuracion actual o propuesta
## 3. Medicion
## 4. Hallazgos
## 5. Version recomendada
## 6. Conflictos y riesgos
## 7. Tests posibles
## 8. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel PU0/PU1/PU2/PU3.
- Define objetivo, oferta, audiencia, pagina, trigger y frecuencia.
- Incluye regla de cierre, declinar y cooldown.
- Revisa mobile, accesibilidad, consentimiento y SEO movil.
- Revisa conflictos con cookie banner, chat, checkout u otros popups.
- Declara medicion disponible y datos faltantes.
- No recomienda test sin baseline, trafico y tracking.
- No toca CMS, CMP, GTM, scripts ni herramientas de popup sin Orden de Cambio.

### Bloquea si

- no hay objetivo u oferta;
- no se sabe donde o cuando aparece;
- no hay forma clara de cerrar;
- puede incumplir privacidad/accesibilidad o danar SEO movil;
- se piden cambios reales sin aprobacion.

## Contrato 25 - Paywall / upgrade CRO

Usar para:

- `paywall-upgrade-cro`;
- paywalls, upgrade screens, upsell modals o feature gates;
- trial expiration screens;
- usage limit screens;
- in-app pricing;
- conversion free-to-paid, trial-to-paid o tier upgrade.

### Objetivo

Mejorar conversion a pago o upgrade dentro del producto sin usar patrones oscuros, romper confianza, bloquear valor critico ni aumentar churn.

### Inputs minimos

- cliente/producto;
- modelo de monetizacion;
- plan actual y plan objetivo;
- trigger del paywall;
- valor ya recibido por el usuario;
- pantalla/copy actual o propuesta;
- pricing y camino de pago;
- camino de salida: no ahora, seguir gratis, downgrade o alternativa;
- metricas: impression, CTA, checkout start, upgrade, revenue, churn/refund;
- guardrails de confianza, soporte y retencion.

### Estructura obligatoria

```text
# Auditoria Paywall Upgrade CRO: [cliente / flujo]
Fecha:
Nivel Paywall:
Pantalla/trigger:
Objetivo:
Fuentes usadas:
Produccion tocada:

## 1. Diagnostico ejecutivo
## 2. Contexto de monetizacion
## 3. Medicion
## 4. Hallazgos
## 5. Version recomendada
## 6. Riesgos y guardrails
## 7. Tests posibles
## 8. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel PW0/PW1/PW2/PW3.
- Explica por que el usuario ve el paywall en ese momento.
- Confirma que hubo valor antes del ask o marca el riesgo.
- Incluye beneficio, comparacion, precio, CTA y escape hatch claro.
- Revisa checkout/billing/post-upgrade y soporte.
- Incluye guardrails de churn, refunds, soporte, confianza y revenue.
- No recomienda test sin baseline, revenue tracking y guardrails.
- No toca producto, pricing, checkout, billing, emails ni tracking sin Orden de Cambio.

### Bloquea si

- no hay modelo de pago u oferta clara;
- no se sabe cuando aparece el paywall;
- no hay camino de salida;
- el cambio puede afectar precios, checkout, billing o datos de usuario sin aprobacion;
- se quieren conclusiones de revenue/churn sin datos o sin marcar parcialidad.

## Contrato 26 - Paid Ads / campanas pagadas

Usar para:

- `paid-ads`;
- Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads o PPC;
- estrategia, auditoria u optimizacion de campanas;
- presupuesto, audiencias, bidding, retargeting, ROAS, CPA o SEM;
- decision sobre si conviene correr anuncios.

### Objetivo

Definir o evaluar una campana pagada con objetivo, conversion, tracking, presupuesto, estructura y riesgos claros antes de gastar dinero.

### Inputs minimos

- cliente;
- plataforma o plataformas candidatas;
- objetivo de campana;
- conversion primaria y valor;
- presupuesto;
- landing/oferta;
- audiencia;
- estado de tracking/pixel/GA4/UTMs;
- datos historicos si existen;
- restricciones de geografia, marca, compliance o plataforma.

### Estructura obligatoria

```text
# Paid Ads: [cliente / plataforma]
Fecha:
Nivel Paid Ads:
Plataforma:
Objetivo:
Fuentes usadas:
Produccion tocada:

## 1. Resumen ejecutivo
## 2. Objetivo y conversion
## 3. Estado de tracking y landing
## 4. Estructura recomendada
## 5. Audiencias y exclusiones
## 6. Creatividades necesarias
## 7. Plan de aprendizaje y optimizacion
## 8. Riesgos y bloqueos
## 9. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel PA0/PA1/PA2/PA3.
- Define objetivo, conversion primaria, presupuesto y metrica de exito.
- Verifica o marca pendiente tracking/pixel/GA4/UTMs.
- Revisa landing y oferta antes de recomendar gasto.
- Elige plataforma por intencion, audiencia, formato, presupuesto y datos.
- Incluye estructura, audiencias, exclusiones, plan de aprendizaje y criterio de pausa/escala.
- Distingue problema de anuncio, audiencia, landing, oferta y tracking.
- No promete CPA/ROAS futuro.
- No toca cuentas, pixels, presupuestos, billing ni campanas sin Orden de Cambio.

### Bloquea si

- no hay objetivo ni conversion definida;
- no hay presupuesto;
- no hay landing u oferta;
- tracking no existe o no puede verificarse para campanas de conversion;
- se piden cambios reales en Ads, pixels, presupuesto o billing sin aprobacion.

## Contrato 27 - Ad Creative / anuncios

Usar para:

- `ad-creative`;
- headlines, descriptions, primary text, hooks o RSA headlines;
- Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads o X Ads;
- variaciones a escala;
- iteracion de anuncios segun performance;
- creative testing.

### Objetivo

Crear o iterar anuncios que respeten plataforma, audiencia, oferta, claims verificables, limites de caracteres y plan de test.

### Inputs minimos

- cliente;
- plataforma y formato;
- objetivo;
- audiencia;
- oferta/landing;
- etapa de awareness;
- restricciones de marca/compliance;
- claims permitidos y fuentes;
- datos de performance si se itera.

### Estructura obligatoria

```text
# Ad Creative: [cliente / plataforma]
Fecha:
Nivel Creative:
Plataforma/formato:
Objetivo:
Fuentes usadas:
Produccion tocada:

## 1. Contexto
## 2. Angulos
## 3. Variaciones
## 4. Combinaciones recomendadas
## 5. Claims y riesgos
## 6. Plan de test creativo
## 7. Siguiente accion unica
```

### Criterios de aceptacion

- Clasifica nivel AC0/AC1/AC2/AC3.
- Define plataforma, formato, objetivo, audiencia y oferta.
- Organiza anuncios por angulos diferenciados.
- Incluye conteo de caracteres y estado frente a limite.
- Revisa claims, precios, pruebas, testimonios y garantias.
- Alinea copy con landing y campana.
- Marca riesgos de politica si aplica.
- No declara ganadores sin datos.
- No sube anuncios ni toca campanas sin Orden de Cambio.

### Bloquea si

- falta plataforma o formato;
- falta oferta, CTA o audiencia;
- los claims requeridos no tienen fuente;
- la pieza pertenece a sector sensible y no hay reglas/compliance suficientes;
- se pide publicar/subir anuncios sin aprobacion.

## Plantilla de revision final

Antes de entregar cualquier output relevante, completar mentalmente:

```text
Output:
Audiencia:
Nivel de calidad estimado: 0/1/2/3/4
Fuentes usadas:
Datos faltantes:
Decision recomendada:
Riesgos:
Siguiente paso:
```

Si el nivel es 0, no entregar como final.

Si el nivel es 1, abrir con:

```text
Basado en datos parciales.
Falta verificar: [fuentes].
```

## Relacion con la migracion

Los siguientes trabajos deben usar este documento:

- P1-003 `client-audit`;
- P1-004 `seo-audit`;
- P1-005 Docente;
- P2-001 Lider Clientes;
- P2-002 Lider Agencia;
- cualquier skill migrada desde `.agents/skills/`.

Ninguna skill operativa debe migrarse sin:

- contrato de output;
- checklist de revision;
- condiciones de bloqueo;
- manejo de datos parciales.
