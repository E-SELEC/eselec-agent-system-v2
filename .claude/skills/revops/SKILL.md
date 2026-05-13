---
name: revops
description: >
  Disena y mejora revenue operations: lead lifecycle, MQL/SQL, lead scoring,
  routing, pipeline stages, CRM hygiene, marketing-to-sales handoff, SLAs,
  deal desk, CRM automation, dashboards y procesos que conectan marketing,
  ventas y customer success. Usalo cuando se hable de RevOps, CRM, pipeline,
  leads que no llegan a ventas, scoring, routing o revenue operations.
---

# RevOps - E-SELEC

## Proposito

Ordenar procesos de ingresos antes de automatizarlos, con definiciones, owners, SLAs, datos y metricas.

Esta skill no modifica CRM ni automatizaciones reales. Produce especificacion operativa.

## Fuentes obligatorias

Lee contexto de agencia o cliente, `quality/criterios-output.md`, y si aplica `.claude/skills/analytics-tracking/SKILL.md`, `.claude/skills/email-sequence/SKILL.md`, `.claude/skills/sales-enablement/SKILL.md`, `protocols/activos-criticos.md`, `protocols/gestion-accesos.md`.

Necesitas GTM motion, stack, etapas actuales, problema y objetivo.

## Niveles

- RV3 - listo: lifecycle, scoring, routing, pipeline, owners, SLAs, datos y metricas definidos.
- RV2 - fuerte: proceso recomendado con datos parciales.
- RV1 - orientativo: diagnostico inicial.
- RV0 - bloqueado: falta stack/proceso/objetivo.

## Workflow

1. Definir GTM motion, stack, volumen y problema.
2. Mapear lifecycle y fuentes de verdad.
3. Definir stage criteria, owners y SLAs.
4. Definir scoring/routing y fallback.
5. Definir pipeline, campos requeridos y hygiene.
6. Definir dashboard y metricas.
7. Preparar output con `templates/revops-spec.md`.

## Reglas

- Definir antes de automatizar.
- CRM es fuente de verdad si se declara.
- No tocar CRM, workflows, imports ni integraciones sin Orden de Cambio.
- No crear reglas sin owner/fallback.

## Bloqueos

- no hay objetivo RevOps;
- no se conoce stack o fuente de verdad;
- se pide automatizar proceso no definido;
- se pide modificar CRM real sin aprobacion.

## Referencias

- `references/revops-patterns.md`: lifecycle y routing.
- `templates/revops-spec.md`: formato de salida.
- `checklists/revision.md`: revision final.
