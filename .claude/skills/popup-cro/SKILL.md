---
name: popup-cro
description: >
  Audita, disena y optimiza popups, modals, overlays, slide-ins, sticky bars,
  announcement banners y elementos interruptivos de conversion para clientes
  de E-SELEC: exit intent, email popup, lead capture popup, discount popup,
  scroll trigger, notification bar, overlay, popup conversion, frecuencia,
  segmentacion, mobile, accesibilidad, GDPR y medicion. Usalo cuando se hable
  de popups, modales, banners, overlays, exit intent o captacion mediante
  interrupcion. Para formularios normales usar form-cro; para pagina completa,
  page-cro.
---

# Popup CRO - E-SELEC

## Proposito

Mejorar conversion con popups o banners sin degradar experiencia, marca, SEO movil, privacidad ni confianza.

Esta skill no implementa popups reales. Produce auditoria, estrategia, copy, reglas de disparo o hipotesis de test.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`
8. `.claude/skills/page-cro/SKILL.md` para contexto de pagina
9. `.claude/skills/form-cro/SKILL.md` si el popup captura datos
10. `.claude/skills/analytics-tracking/SKILL.md` para eventos
11. `.claude/skills/ab-test-setup/SKILL.md` si propones test
12. `protocols/activos-criticos.md`

Necesitas conocer objetivo, pagina/contexto, audiencia, trigger y frecuencia. Si faltan, marca el output como parcial.

## Niveles

- PU3 - validado: objetivo, trigger, audiencia, frecuencia, mobile, accesibilidad y tracking comprobados.
- PU2 - diagnostico fuerte: popup/contexto visible y objetivo claro; faltan datos cuantitativos completos.
- PU1 - orientativo: hay idea o captura parcial, pero faltan reglas, medicion o contexto.
- PU0 - bloqueado: falta objetivo, oferta, pagina/contexto o mecanismo de cierre.

## Workflow

1. Definir proposito: email, lead magnet, descuento, anuncio, feedback, exit save.
2. Identificar audiencia, pagina, fuente de trafico y momento del journey.
3. Revisar trigger: click, scroll, exit, tiempo, page count, comportamiento.
4. Revisar oferta y copy: valor claro, CTA, declinar, privacidad.
5. Revisar UX: cierre visible, frecuencia, conflictos con otros overlays, mobile.
6. Revisar cumplimiento: consentimiento, GDPR, accesibilidad, SEO movil/interstitial.
7. Revisar medicion: impressions, close, focus, submit, conversion, annoyance signals.
8. Preparar output con `templates/auditoria-popup-cro.md`.

## Reglas

- No mostrar popup antes de que exista contexto suficiente, salvo aviso necesario.
- Todo popup debe tener cierre claro y facil.
- No usar copy manipulativo para declinar.
- No bloquear checkout, formularios criticos o contenido movil de forma intrusiva.
- No pedir datos innecesarios ni pre-marcar consentimiento.
- No recomendar test sin baseline, trafico y tracking.
- No tocar web, CMS, CMP, GTM, scripts ni herramientas de popup sin Orden de Cambio.

## Bloqueos

- no hay objetivo u oferta;
- no se sabe donde o cuando aparece;
- no hay forma clara de cerrar;
- el popup incumple privacidad/accesibilidad o puede danar SEO movil;
- se piden cambios reales sin aprobacion.

## Referencias

- `references/popup-patterns.md`: patrones por tipo de popup.
- `templates/auditoria-popup-cro.md`: formato de salida.
- `checklists/revision.md`: revision final.
