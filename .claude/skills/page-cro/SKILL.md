---
name: page-cro
description: >
  Audita, diagnostica y mejora conversion de paginas de marketing para
  clientes de E-SELEC: CRO, landing pages, homepages, paginas de servicio,
  pricing, feature pages, blog posts con CTA, propuesta de valor, CTA,
  jerarquia visual, friccion, confianza, social proof, objeciones, mobile,
  formularios, UX, conversion rate, bounce rate, test ideas y optimizacion de
  pagina. Usalo cuando se hable de conversion, pagina que no convierte,
  landing page, mejorar conversiones, baja tasa de conversion, mucha salida o
  feedback CRO sobre una URL/captura.
---

# Page CRO - E-SELEC

## Proposito

Diagnosticar por que una pagina no convierte y decidir que cambiar primero.

Esta skill no publica cambios. Produce una auditoria o plan CRO priorizado. Si el problema es solo copy, usa `copywriting` o `copy-editing`. Si el problema es formulario, delega en `form-cro` cuando exista. Si el problema es arquitectura, usa `site-architecture`.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`, contrato CRO / pagina
8. `.claude/skills/analytics-tracking/SKILL.md` si la conclusion depende de conversiones, eventos o formularios
9. `.claude/skills/copywriting/SKILL.md` si recomiendas reescritura
10. `.claude/skills/copy-editing/SKILL.md` si solo recomiendas pulir texto
11. `.claude/skills/site-architecture/SKILL.md` si hay problemas de navegacion, URL o jerarquia
12. `protocols/activos-criticos.md`

Necesitas al menos una vista de la pagina:

- URL publica;
- captura desktop/mobile;
- HTML/render;
- documento de wireframe;
- texto y estructura pegados por Rodrigo.

Si no puedes ver la pagina, no hagas auditoria final.

## Principios

1. CRO empieza por objetivo y fuente de trafico.
2. Una pagina debe tener una accion primaria clara.
3. La propuesta de valor debe entenderse en 5 segundos.
4. Cada recomendacion debe explicar impacto, esfuerzo y evidencia.
5. No recomendar A/B test si no hay trafico suficiente o medicion.
6. No tocar produccion sin Orden de Cambio.
7. No optimizar conversion a costa de claims falsos o experiencia enganosa.

## Niveles CRO

- PC3 - validado: pagina revisada, objetivo/trafico/conversion medidos, tracking comprobado, recomendaciones priorizadas.
- PC2 - diagnostico fuerte: pagina revisada y objetivo claro; faltan datos cuantitativos o tracking completo.
- PC1 - orientativo: hay captura/texto, pero faltan trafico, objetivo medido o contexto suficiente.
- PC0 - bloqueado: falta pagina, objetivo de conversion o audiencia.

Regla:

- PC0 no produce plan final.
- PC1 solo orienta.
- PC2 permite roadmap interno.
- PC3 permite plan de implementacion o test.

## Workflow

### 1. Definir contexto de conversion

Identifica:

- tipo de pagina;
- audiencia;
- fuente de trafico;
- accion primaria;
- accion secundaria;
- dispositivo principal;
- conversion actual si existe;
- que pasa despues del click/formulario.

Si no hay accion primaria, la primera recomendacion es definirla.

### 2. Revisar medicion

Antes de concluir, comprueba:

- evento/conversion principal;
- formulario/CTA trackeado;
- GA4/GTM/Ads si aplica;
- heatmaps/session recordings si existen;
- periodo y volumen de datos.

Si no hay medicion, marca PC1/PC2 y recomienda `analytics-tracking`.

### 3. Analizar la pagina

Usa `references/page-review.md`.

Evalua en orden:

1. propuesta de valor;
2. mensaje vs fuente de trafico;
3. CTA y jerarquia;
4. prueba/confianza;
5. objeciones;
6. friccion;
7. mobile;
8. velocidad/percepcion;
9. accesibilidad basica;
10. coherencia SEO/AI si aplica.

### 4. Priorizar hallazgos

No listes 30 mejoras.

Clasifica:

- critico: bloquea conversion o comprension;
- alto: mejora probable de conversion;
- medio: mejora experiencia/confianza;
- bajo: pulido.

Cada hallazgo debe tener:

- evidencia;
- impacto esperado;
- esfuerzo;
- dependencia;
- accion recomendada.

### 5. Distinguir cambios de tests

Usa `references/experiments.md`.

Regla:

- Si el problema es obvio y de bajo riesgo, recomendar cambio directo.
- Si hay varias soluciones plausibles y trafico suficiente, recomendar test.
- Si no hay trafico/medicion, no proponer A/B test como prioridad.

### 6. Preparar output

Usa `templates/auditoria-cro-pagina.md`.

Debe incluir:

- nivel PC0-PC3;
- objetivo;
- fuentes;
- diagnostico;
- quick wins;
- cambios de alto impacto;
- test ideas;
- copy/CTA sugerido;
- datos faltantes;
- siguiente accion unica.

## Bloqueos

Bloquea o marca como parcial si:

- no hay pagina visible;
- no hay objetivo de conversion;
- no se conoce audiencia/oferta;
- se quieren conclusiones cuantitativas sin medicion;
- se propone test sin trafico o tracking;
- se piden cambios reales en web/CMS/Ads/formularios sin Orden de Cambio;
- la recomendacion implica claims falsos, dark patterns o degradar UX.

## Referencias

- `references/page-review.md`: checklist de diagnostico por area.
- `references/experiments.md`: ideas de tests por tipo de pagina.
- `templates/auditoria-cro-pagina.md`: formato de salida.
- `checklists/revision.md`: revision final.
