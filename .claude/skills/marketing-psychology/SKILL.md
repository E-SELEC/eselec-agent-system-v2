---
name: marketing-psychology
description: >
  Aplica psicologia, behavioral science, mental models y principios de decision
  a marketing, copy, CRO, pricing, onboarding, retencion o persuasion etica.
  Usalo para psychology, mental models, cognitive bias, nudges, persuasion,
  social proof, scarcity, loss aversion, framing, buyer behavior o decision-making.
---

# Marketing Psychology - E-SELEC

## Proposito

Usar modelos psicologicos de forma etica para diagnosticar friccion, mejorar decisiones de marketing y proponer hipotesis testeables.

Esta skill no manipula ni justifica dark patterns. Produce diagnostico, modelos aplicables, cambios sugeridos y pruebas.

## Fuentes obligatorias

Lee contexto de agencia o cliente, `quality/criterios-output.md`, y si aplica `.claude/skills/product-marketing-context/SKILL.md`, `.claude/skills/copywriting/SKILL.md`, `.claude/skills/copy-editing/SKILL.md`, `.claude/skills/page-cro/SKILL.md`, `.claude/skills/form-cro/SKILL.md`, `.claude/skills/pricing-strategy/SKILL.md`, `.claude/skills/onboarding-cro/SKILL.md` y `protocols/activos-criticos.md`.

Necesitas comportamiento deseado, audiencia, etapa del journey, friccion observada, activo a revisar y evidencia disponible.

## Niveles

- MP3 - listo: modelos aplicados con evidencia, recomendacion, guardrail etico y prueba.
- MP2 - fuerte: modelos y acciones claros, faltan datos de comportamiento.
- MP1 - orientativo: lectura psicologica con contexto parcial.
- MP0 - bloqueado: falta comportamiento objetivo o activo a revisar.

## Workflow

1. Definir comportamiento objetivo: click, signup, compra, respuesta, activacion, retencion.
2. Ubicar etapa: awareness, consideration, decision, onboarding o retention.
3. Identificar friccion: motivacion, habilidad, prompt, confianza, claridad o riesgo.
4. Elegir modelos de `references/psychology-models.md`.
5. Traducir cada modelo en una accion concreta y etica.
6. Definir hipotesis y prueba si aplica.
7. Preparar output usando `templates/psychology-review.md`.

## Reglas

- Explicar por que aplica cada modelo.
- Convertir teoria en cambio observable.
- Incluir guardrail etico.
- Preferir hipotesis testeables frente a certezas.
- No proponer escasez falsa, urgencia falsa, confusion o friccion deliberada.

## Bloqueos

- no hay comportamiento objetivo;
- se pide manipular o ocultar informacion;
- el modelo psicologico no se puede conectar con una accion concreta;
- se pide implementar cambios reales sin aprobacion.

## Referencias

- `references/psychology-models.md`: modelos y usos.
- `templates/psychology-review.md`: formato de salida.
- `checklists/revision.md`: revision final.
