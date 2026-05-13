---
name: paywall-upgrade-cro
description: >
  Audita y optimiza paywalls, upgrade screens, upsell modals, feature gates,
  trial expiration screens, usage limit screens, in-app pricing y prompts de
  conversion free-to-paid para clientes de E-SELEC. Usalo cuando se hable de
  paywall, upgrade, upsell, feature gate, convertir gratis a pago, freemium
  conversion, trial-to-paid, limit reached, plan upgrade prompt o usuarios que
  no pagan. Para pagina publica de precios usar page-cro; para pricing general,
  pricing-strategy.
---

# Paywall Upgrade CRO - E-SELEC

## Proposito

Mejorar conversion a pago o upgrade en producto sin usar presion indebida, romper confianza, bloquear valor critico ni generar churn.

Esta skill no implementa paywalls reales. Produce auditoria, redisenio recomendado, copy o hipotesis de test.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`
8. `.claude/skills/onboarding-cro/SKILL.md` para valor/activacion previa
9. `.claude/skills/page-cro/SKILL.md` si conecta con pagina de precios
10. `.claude/skills/analytics-tracking/SKILL.md` para eventos y revenue
11. `.claude/skills/ab-test-setup/SKILL.md` si propones test
12. `protocols/activos-criticos.md`

Necesitas conocer plan/modelo, trigger, usuario afectado, valor ya recibido y metrica de upgrade. Si falta, marca parcial.

## Niveles

- PW3 - validado: trigger, valor previo, planes, metrica, revenue, friccion y guardrails comprobados.
- PW2 - diagnostico fuerte: pantalla/flujo visible y modelo claro; faltan datos cuantitativos completos.
- PW1 - orientativo: hay idea o captura parcial, faltan metricas, planes o contexto de usuario.
- PW0 - bloqueado: falta modelo de pago, trigger, oferta o camino de salida.

## Workflow

1. Definir contexto: freemium, trial, tier upgrade, feature gate, usage limit.
2. Identificar usuario: estado, valor recibido, accion que intenta hacer, plan actual.
3. Revisar trigger: feature click, limite, trial ending, time-based, usage milestone.
4. Revisar propuesta: beneficio, comparacion, pricing, prueba, urgencia, objeciones.
5. Revisar UX: camino a pago, escape hatch, continuar gratis, no bloquear flujo critico.
6. Revisar post-upgrade: acceso inmediato, confirmacion, guia y soporte.
7. Revisar medicion: impression, CTA, checkout start, purchase, revenue, churn/refund.
8. Preparar output con `templates/auditoria-paywall-upgrade.md`.

## Reglas

- El usuario debe haber recibido o entendido valor antes del ask.
- Todo paywall debe explicar que desbloquea y por que importa ahora.
- Debe existir salida clara: no ahora, seguir gratis, downgrade o alternativa.
- No usar dark patterns: cierre oculto, plan preseleccionado confuso, culpa o presion enganosa.
- No recomendar cambios de pricing sin contexto suficiente.
- No recomendar test sin baseline, trafico, revenue tracking y guardrails.
- No tocar producto, pricing, checkout, billing, emails ni tracking sin Orden de Cambio.

## Bloqueos

- no hay modelo de pago o oferta clara;
- no se sabe cuando aparece el paywall;
- no hay camino de salida;
- el cambio puede afectar checkout, billing, precios o datos de usuario sin aprobacion;
- se quieren conclusiones de revenue/churn sin datos o sin marcar parcialidad.

## Referencias

- `references/paywall-patterns.md`: patrones por tipo de paywall.
- `templates/auditoria-paywall-upgrade.md`: formato de salida.
- `checklists/revision.md`: revision final.
