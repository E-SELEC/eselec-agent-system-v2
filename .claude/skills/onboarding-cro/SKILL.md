---
name: onboarding-cro
description: >
  Audita y optimiza onboarding post-signup, activacion, first-run experience,
  time-to-value, setup completion, aha moment, checklist de onboarding, empty
  states, tours, tooltips, recuperacion de usuarios atascados y primeros pasos
  de producto para clientes de E-SELEC. Usalo cuando se hable de onboarding,
  activation rate, usuarios que se registran pero no usan el producto, primer
  valor, setup incompleto, baja activacion, first session experience o usuarios
  nuevos que abandonan. Para registro previo, usar signup-flow-cro.
---

# Onboarding CRO - E-SELEC

## Proposito

Acelerar el tiempo hasta el primer valor y aumentar activacion sin ocultar friccion, forzar pasos innecesarios ni romper retencion.

Esta skill no implementa cambios reales. Produce auditoria, redisenio recomendado o hipotesis de test.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`
8. `.claude/skills/signup-flow-cro/SKILL.md` si el problema empieza antes del alta
9. `.claude/skills/analytics-tracking/SKILL.md` para activacion y cohortes
10. `.claude/skills/ab-test-setup/SKILL.md` si propones test
11. `protocols/activos-criticos.md`

Necesitas conocer que accion cuenta como activacion. Si no existe, la primera tarea es definirla.

## Niveles

- OB3 - validado: activacion definida, flujo revisado, medicion/cohortes y drop-offs disponibles.
- OB2 - diagnostico fuerte: flujo visible y activacion propuesta; faltan cohortes o datos completos.
- OB1 - orientativo: hay descripcion parcial, pero faltan metricas, pantallas o definicion clara.
- OB0 - bloqueado: no hay producto/flujo, no se conoce activacion ni primer valor.

## Workflow

1. Definir producto, usuario objetivo y promesa de valor.
2. Definir activacion: evento o accion que predice retencion.
3. Mapear desde signup completado hasta primer valor.
4. Revisar primera sesion: objetivo unico, pasos, bloqueos, permisos, setup y datos vacios.
5. Revisar empty states, checklist, tours, tooltips, ayuda y soporte.
6. Revisar coordinacion email/in-app si existe.
7. Revisar medicion: activation rate, time-to-value, step drop-off, D1/D7/D30 retention.
8. Preparar output con `templates/auditoria-onboarding-cro.md`.

## Reglas

- La primera sesion debe tener un objetivo claro.
- Tutorial no sustituye experiencia de valor.
- No proponer checklists largos sin priorizar valor.
- No recomendar emails si no hay relacion con acciones in-app.
- No llamar activacion a una accion que no conecta con retencion.
- No tocar producto, app, emails, CRM, tracking ni datos de usuario sin Orden de Cambio.

## Bloqueos

- no se conoce el producto o la promesa de valor;
- no hay activacion definida ni forma razonable de proponerla;
- no se puede ver flujo, captura o pasos;
- la recomendacion afecta datos de usuarios, emails, producto o tracking sin aprobacion;
- faltan datos y el output no se marca como parcial.

## Referencias

- `references/onboarding-patterns.md`: patrones de activacion.
- `templates/auditoria-onboarding-cro.md`: formato de salida.
- `checklists/revision.md`: revision final.
