---
name: analytics-tracking
description: >
  Audita, diseña o mejora medicion digital para clientes de E-SELEC: GA4,
  Google Tag Manager, eventos, conversiones, UTMs, consent mode, pixels,
  dataLayer, formularios, llamadas, WhatsApp, e-commerce, informes y calidad
  de datos. Usalo cuando se hable de tracking, analitica, conversiones, GA4,
  GTM, eventos duplicados, medicion rota, atribucion o "como medimos esto".
---

# Analytics Tracking - E-SELEC

## Proposito

Crear medicion que permita tomar decisiones reales.

Esta skill no existe para medir todo. Existe para responder:

- que decision necesita datos;
- que eventos/conversiones hacen falta;
- que herramientas intervienen;
- que esta roto o sin verificar;
- que se puede implementar sin riesgo;
- que requiere Orden de Cambio.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`, contrato de tracking/medicion si existe
8. `protocols/activos-criticos.md`
9. `protocols/gestion-accesos.md`
10. `.claude/skills/ingesta-evidencia/SKILL.md` si vas a usar exports
11. `.claude/skills/verificacion-medicion/SKILL.md` si vas a decidir nivel de datos

No pidas ni pegues measurement IDs privados, tokens, cookies, client secrets, usuarios, passwords ni datos personales.

## Principios

1. Medir para decidir, no para acumular eventos.
2. Cada evento debe tener una decision asociada.
3. Conversion primero, detalle despues.
4. No duplicar eventos.
5. No enviar PII a GA4, GTM, pixels ni dataLayer.
6. No tocar produccion sin Orden de Cambio.
7. Si no se verifica en DebugView/GTM Preview/fuente viva, marcar como parcial.

## Niveles de tracking

- T3 - verificado: eventos/conversiones probados en fuente viva, triggers correctos, sin duplicados y con consentimiento revisado.
- T2 - plan implementable: plan claro con eventos, triggers, propiedades y validacion pendiente.
- T1 - diagnostico orientativo: contexto o capturas, sin prueba viva.
- T0 - bloqueado: falta objetivo de negocio, fuente, acceso o hay riesgo de PII/secreto.

Regla:

- T0 no produce plan final.
- T1 solo orienta.
- T2 permite preparar implementacion.
- T3 permite informe o decision de negocio.

## Workflow

### 1. Definir decision

Antes de hablar de eventos, responde:

- que quiere saber Rodrigo o el cliente;
- que decision se tomara con el dato;
- que conversion importa;
- que canal o servicio depende de esa medicion.

Si no hay decision, no diseñes tracking.

### 2. Mapear estado actual

Identifica:

- herramientas: GA4, GTM, Meta Pixel, Google Ads, CRM, WordPress, WooCommerce, formularios;
- conversiones actuales;
- eventos existentes;
- fuentes de trafico;
- consentimiento/cookies;
- limitaciones de acceso;
- si hay datos contradictorios.

### 3. Elegir modo de trabajo

| Modo | Uso | Output |
|---|---|---|
| Auditoria | "esta rota la medicion", "GA4 no cuadra", "eventos duplicados" | diagnostico de tracking |
| Plan | "que eventos medimos", "necesito tracking plan" | plan de eventos/conversiones |
| Implementacion guiada | "como lo configuro" | pasos tecnicos sin tocar produccion |
| Validacion | "esta funcionando" | checklist de pruebas y evidencias |

### 4. Diseñar eventos

Usa formato `objeto_accion` en minusculas:

- `form_submitted`
- `cta_clicked`
- `whatsapp_clicked`
- `phone_clicked`
- `checkout_started`
- `purchase_completed`

Pon contexto en propiedades, no en nombres largos.

Lee `references/event-taxonomy.md` para ejemplos por tipo de negocio.

### 5. Definir propiedades minimas

Usa solo propiedades utiles:

- `page_location`
- `page_title`
- `cta_location`
- `form_name`
- `service_category`
- `lead_type`
- `value`
- `currency`
- `source`
- `medium`
- `campaign`

No usar:

- emails;
- telefonos;
- nombres;
- DNI/NIF;
- direcciones;
- IDs personales sin hash/consentimiento;
- contenido de mensajes libres.

### 6. Validar privacidad y consentimiento

Para UE/Espana:

- analytics y marketing deben respetar consentimiento;
- pixels de Ads/Meta no deben disparar antes de consentimiento si aplica;
- no enviar PII;
- revisar retencion de datos;
- documentar limitaciones por consent/ad blockers.

### 7. Preparar output

Usa `templates/plan-tracking.md`.

Debe incluir:

- objetivo de medicion;
- herramientas;
- eventos;
- conversiones;
- triggers;
- propiedades;
- pruebas;
- riesgos;
- nivel T0/T1/T2/T3;
- siguiente accion unica.

### 8. Bloquear produccion si aplica

Aplicar `protocols/activos-criticos.md` antes de:

- publicar GTM;
- crear/modificar conversiones GA4;
- enlazar Google Ads;
- modificar pixels;
- tocar WordPress/WooCommerce;
- cambiar formularios;
- alterar consent/cookies;
- cambiar eventos de compra o leads.

## Referencias

- `references/event-taxonomy.md`: eventos recomendados por tipo de negocio.
- `references/ga4-gtm-notes.md`: patrones tecnicos GA4/GTM y validacion.
- `templates/plan-tracking.md`: formato de salida.
- `checklists/revision.md`: revision final.
