# auditar-paywall

Audita un paywall, upgrade screen, upsell modal o feature gate sin tocar produccion.

## Uso

```text
/auditar-paywall [cliente] [pantalla/trigger] [--write]
```

Ejemplos:

```text
/auditar-paywall cliente-ecommerce limite de pedidos registrados
/auditar-paywall cliente-servicios upgrade soporte premium
/auditar-paywall cliente-reservas pantalla de reserva premium
```

## Workflow

1. Leer `.claude/skills/paywall-upgrade-cro/SKILL.md`.
2. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
   - `quality/criterios-output.md`
3. Confirmar modelo, trigger, plan actual, valor previo y metrica de upgrade.
4. Revisar copy, pricing, escape hatch, checkout, post-upgrade, guardrails y medicion.
5. Entregar usando `templates/auditoria-paywall-upgrade.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/auditoria-paywall-upgrade-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No modificar paywalls reales.
- No tocar producto, pricing, checkout, billing, emails ni tracking.
- No usar dark patterns.
- No inventar revenue, churn ni upgrade rate.
- Si hay implementacion real, abrir Orden de Cambio.
