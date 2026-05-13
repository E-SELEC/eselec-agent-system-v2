---
name: email-sequence
description: >
  Disena y optimiza secuencias de email no frias: welcome sequence, nurture,
  drip campaign, onboarding emails, re-engagement, post-purchase, lifecycle
  emails, email automation, trigger-based emails, email funnel y workflows.
  Usalo cuando se hable de secuencia de emails, automatizacion, welcome series,
  drip, nurture, lifecycle o emails post-captura. Para cold outreach usar
  cold-email.
---

# Email Sequence - E-SELEC

## Proposito

Crear secuencias que muevan a una audiencia conocida hacia una accion sin saturar, duplicar mensajes ni romper consentimiento.

Esta skill no configura automatizaciones reales. Produce estrategia, emails, cadencia y medicion.

## Fuentes obligatorias

Lee contexto de agencia o cliente, `quality/criterios-output.md`, y si aplica `.claude/skills/lead-magnets/SKILL.md`, `.claude/skills/copywriting/SKILL.md`, `.claude/skills/onboarding-cro/SKILL.md`, `.claude/skills/analytics-tracking/SKILL.md`, `protocols/activos-criticos.md` y `protocols/gestion-accesos.md`.

Necesitas trigger, audiencia, objetivo, permiso/consentimiento y salida de la secuencia.

## Niveles

- ES3 - listo: trigger, segmento, objetivo, cadencia, emails, exit conditions y metricas definidos.
- ES2 - fuerte: secuencia usable, faltan automatizacion o datos historicos.
- ES1 - orientativo: idea con contexto parcial.
- ES0 - bloqueado: falta audiencia, trigger, objetivo o consentimiento.

## Workflow

1. Definir tipo: welcome, nurture, onboarding, re-engagement, post-purchase.
2. Definir trigger, segmento, objetivo y exit conditions.
3. Mapear emails: proposito unico, timing, subject, preview, CTA.
4. Revisar consentimiento, frecuencia y solapamiento con otros emails.
5. Definir metricas: open, click, reply, conversion, unsubscribe, spam.
6. Preparar output con `templates/email-sequence-plan.md`.

## Reglas

- Un email, un objetivo.
- Value before ask.
- No enviar ni configurar automatizaciones sin Orden de Cambio.
- No escribir a audiencias sin consentimiento.
- No prometer resultados no medidos.

## Bloqueos

- no hay trigger;
- no hay audiencia/segmento;
- falta objetivo;
- no hay permiso/consentimiento;
- se pide activar automatizacion real sin aprobacion.

## Referencias

- `references/email-sequence-patterns.md`: tipos y cadencias.
- `templates/email-sequence-plan.md`: formato de salida.
- `checklists/revision.md`: revision final.
