---
name: content-strategy
description: >
  Planifica estrategia de contenido para clientes de E-SELEC: pilares,
  clusters, calendario editorial, blog strategy, ideas de contenido, roadmap,
  topic clusters, contenidos SEO, contenidos para AI SEO, contenidos
  comerciales, contenidos locales, contenido por buyer journey, brief editorial,
  priorizacion de temas, gaps de contenido y que publicar. Usalo cuando se
  pregunte que contenido crear, sobre que escribir, como organizar un blog,
  como convertir SEO/AI SEO en piezas editoriales o como planificar contenido.
---

# Content Strategy - E-SELEC

## Proposito

Decidir que contenido crear, en que orden y por que.

Esta skill no escribe piezas completas. Convierte objetivos de negocio, SEO, AI SEO, ventas y recursos disponibles en un plan editorial priorizado.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`, contrato Content strategy si existe
8. `.claude/skills/seo-audit/SKILL.md` si el plan depende de keywords/rendimiento organico
9. `.claude/skills/ai-seo/SKILL.md` si el plan busca citas o visibilidad AI
10. `.claude/skills/site-architecture/SKILL.md` si hay hubs, clusters o nuevas paginas
11. `.claude/skills/schema-markup/SKILL.md` si hay FAQ, Article, HowTo, Product o breadcrumbs
12. `.claude/skills/ingesta-evidencia/SKILL.md` si usas exports de GSC/SEMrush/GA4, research o legacy

No inventes volumen, dificultad, conversiones ni queries. Si faltan datos, marca la estrategia como parcial.

## Principios

1. Contenido existe para mover una decision, no para llenar calendario.
2. Cada tema debe conectar con negocio, busqueda, autoridad o conversion.
3. SEO primero captura demanda; contenido compartible crea demanda.
4. AI SEO exige contenido claro, citable y verificable.
5. No crear clusters si la web no puede alojarlos o enlazarlos bien.
6. No publicar contenido medico, legal, financiero o sensible sin fuentes y revision adecuada.
7. Un calendario sin prioridad es ruido.

## Niveles de estrategia

- CS3 - validada: contexto, objetivos, datos SEO/AI/ventas, recursos, calendario y priorizacion con evidencia.
- CS2 - plan fuerte: contexto y evidencia parcial suficientes, con datos faltantes declarados.
- CS1 - orientativa: hay negocio/audiencia, pero faltan datos de demanda, rendimiento o recursos.
- CS0 - bloqueada: falta objetivo, audiencia, oferta o cliente.

Regla:

- CS0 no produce plan final.
- CS1 solo orienta.
- CS2 permite roadmap interno.
- CS3 permite plan editorial operativo.

## Workflow

### 1. Definir objetivo

Clasifica el objetivo principal:

- trafico organico;
- leads;
- autoridad de marca;
- AI visibility;
- soporte/educacion;
- conversion;
- retencion;
- lanzamiento;
- reputacion local.

Si hay mas de un objetivo, prioriza uno principal y uno secundario.

### 2. Mapear audiencia y oferta

Identifica:

- cliente ideal;
- problemas/deseos;
- objeciones;
- servicios/productos;
- etapa de compra;
- mercado e idioma;
- tono y recursos disponibles.

No planifiques temas que atraen publico que E-SELEC o el cliente no quiere vender.

### 3. Revisar evidencia

Usa fuentes disponibles:

- GSC: queries, paginas, CTR, impresiones.
- SEMrush/Ahrefs: gaps, dificultad, competidores, clusters.
- GA4/CRM: conversiones y contenidos que ayudan a vender.
- ventas/soporte: preguntas, objeciones, lenguaje real.
- AI SEO: queries donde el cliente no aparece o no es citado.
- log/memory: que ya se probo y que Rodrigo aprobo/rechazo.

Si falta evidencia, indica como obtenerla.

### 4. Elegir tipo de contenido

Usa `references/content-types.md`.

Tipos principales:

- pieza SEO informativa;
- pagina de servicio;
- hub/pillar;
- spoke;
- comparativa;
- caso de estudio;
- FAQ;
- guia;
- plantilla/recurso;
- pieza socializable;
- contenido local;
- contenido AI-citable.

### 5. Crear pilares y clusters

Define 3-5 pilares maximo.

Cada pilar debe tener:

- motivo de negocio;
- audiencia;
- intencion de busqueda;
- relacion con servicio;
- piezas principales;
- enlaces internos necesarios;
- dependencia de web/schema/tracking si aplica.

### 6. Priorizar

Usa `references/prioritization.md`.

Puntua cada tema por:

- impacto de negocio;
- demanda o evidencia;
- cercania a conversion;
- autoridad diferencial;
- esfuerzo;
- riesgo;
- dependencia.

No priorices por volumen solo.

### 7. Preparar calendario

El calendario debe ser realista.

Incluye:

- frecuencia;
- responsable;
- formato;
- fecha propuesta;
- fuente necesaria;
- estado: idea, brief, redaccion, revision, publicado;
- siguiente accion.

### 8. Preparar output

Usa `templates/estrategia-contenido.md`.

Debe incluir:

- nivel CS0-CS3;
- objetivo;
- fuentes;
- pilares;
- backlog de temas;
- calendario 30/60/90 dias;
- dependencias;
- riesgos;
- siguiente accion unica.

## Bloqueos

Bloquea o marca como parcial si:

- no hay objetivo de negocio;
- no hay audiencia/oferta clara;
- faltan datos y se pretende entregar como plan definitivo;
- se proponen temas desconectados del servicio;
- el plan requiere paginas nuevas sin revisar arquitectura;
- se afirma potencial SEO/AI sin evidencia;
- se repiten contenidos ya descartados o fallidos en log;
- se requiere publicar en produccion sin Orden de Cambio.

## Referencias

- `references/content-types.md`: tipos de contenido y cuando usarlos.
- `references/prioritization.md`: scoring de temas y calendario.
- `templates/estrategia-contenido.md`: formato de salida.
- `checklists/revision.md`: revision final.
