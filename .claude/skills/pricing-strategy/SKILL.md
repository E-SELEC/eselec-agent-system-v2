---
name: pricing-strategy
description: >
  Ayuda con pricing, packaging y monetizacion para E-SELEC o clientes:
  precios, tiers, freemium, free trial, value metric, willingness to pay,
  price increase, annual vs monthly, per seat pricing, packaging, pricing page
  y cuanto cobrar. Usalo cuando se hable de estrategia de precios,
  monetizacion, planes, subir precios o pricing incorrecto. Para paywalls
  in-app usar paywall-upgrade-cro.
---

# Pricing Strategy - E-SELEC

## Proposito

Tomar decisiones de pricing con contexto de valor, mercado, clientes, costes, riesgo y plan de validacion.

Esta skill no cambia precios reales ni publica planes. Produce diagnostico, estructura, hipotesis o plan de investigacion.

## Fuentes obligatorias

Lee contexto de agencia o cliente, `quality/criterios-output.md`, y si aplica `.claude/skills/page-cro/SKILL.md`, `.claude/skills/paywall-upgrade-cro/SKILL.md`, `.claude/skills/sales-enablement/SKILL.md`, `.claude/skills/analytics-tracking/SKILL.md`, `protocols/activos-criticos.md`.

Necesitas producto/servicio, cliente objetivo, oferta, pricing actual, alternativas y objetivo de negocio.

## Niveles

- PR3 - listo: mercado, valor, costes, competidores, metricas, propuesta y riesgos definidos.
- PR2 - fuerte: recomendacion razonada con datos parciales.
- PR1 - orientativo: hipotesis con contexto limitado.
- PR0 - bloqueado: falta oferta, cliente objetivo o pricing actual/propuesto.

## Workflow

1. Definir negocio, ICP, motion y objetivo: crecimiento, revenue, margen, posicionamiento.
2. Revisar pricing actual, planes, metricas y fricciones.
3. Revisar valor percibido, alternativas y competidores.
4. Elegir value metric y packaging.
5. Proponer estructura y riesgos.
6. Definir validacion: entrevistas, encuesta, test, cohortes o rollout.
7. Preparar output con `templates/pricing-strategy-plan.md`.

## Reglas

- No decidir precio solo por coste.
- No prometer conversion/revenue.
- No cambiar precios, checkout, planes ni propuestas sin Orden de Cambio.
- Marcar si faltan datos de margen, churn, ARPU o competencia.

## Bloqueos

- falta oferta o ICP;
- no hay pricing actual/propuesto;
- se pide cambiar precios reales sin aprobacion;
- faltan datos clave y no se marca parcial.

## Referencias

- `references/pricing-patterns.md`: modelos y validacion.
- `templates/pricing-strategy-plan.md`: formato de salida.
- `checklists/revision.md`: revision final.
