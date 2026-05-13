---
name: churn-prevention
description: >
  Disena estrategias para reducir churn, cancelaciones y perdida de revenue:
  cancel flows, save offers, dunning, failed payment recovery, pause
  subscription, downgrade, win-back, retention, exit surveys, churn signals,
  involuntary churn y reactivacion. Usalo cuando se hable de churn, cancel flow,
  customers leaving, failed payments o retencion.
---

# Churn Prevention - E-SELEC

## Proposito

Reducir churn voluntario e involuntario con flujos respetuosos, ofertas adecuadas, dunning y medicion.

Esta skill no modifica billing, cancel flows ni emails reales. Produce plan o especificacion.

## Fuentes obligatorias

Lee contexto, `quality/criterios-output.md`, y si aplica `.claude/skills/email-sequence/SKILL.md`, `.claude/skills/onboarding-cro/SKILL.md`, `.claude/skills/pricing-strategy/SKILL.md`, `.claude/skills/analytics-tracking/SKILL.md`, `protocols/activos-criticos.md`, `protocols/gestion-accesos.md`.

Necesitas tipo de churn, billing/subscription context, metricas y restricciones legales.

## Niveles

- CH3 - listo: churn, motivos, billing, flow, offers, dunning, metricas y guardrails definidos.
- CH2 - fuerte: plan util con datos parciales.
- CH1 - orientativo: hipotesis de retencion.
- CH0 - bloqueado: falta tipo de churn, producto o billing context.

## Workflow

1. Separar churn voluntario vs involuntario.
2. Mapear cancel flow o dunning actual.
3. Definir motivos, segmentos y offers.
4. Definir emails/win-back si aplica.
5. Definir medicion: churn, save rate, recovery, LTV, refunds, complaints.
6. Preparar output con `templates/churn-prevention-plan.md`.

## Reglas

- No ocultar cancelacion ni usar dark patterns.
- Save offer debe coincidir con motivo.
- Dunning debe ser claro y respetuoso.
- No tocar billing, subscriptions, cancel flow ni emails sin Orden de Cambio.

## Bloqueos

- no se conoce tipo de churn;
- no hay contexto de billing/subscription;
- se piden cambios reales de cancelacion/billing sin aprobacion;
- faltan restricciones legales y el cambio depende de ellas.

## Referencias

- `references/churn-patterns.md`: cancel flow y dunning.
- `templates/churn-prevention-plan.md`: formato de salida.
- `checklists/revision.md`: revision final.
