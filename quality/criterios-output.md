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

- Evalua propuesta de valor, CTA, jerarquia visual, confianza, objeciones y friccion.
- Distingue cambio recomendado de test recomendado.
- No recomienda test A/B si no hay trafico suficiente.
- Incluye copy alternativo solo para elementos clave.
- Considera mobile.

### Bloquea si

- no se conoce el objetivo de conversion;
- no se puede ver la pagina y no hay captura;
- hay fallo tecnico critico que impide evaluar conversion.

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
