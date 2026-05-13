# plan-churn-prevention

Disena retencion/cancel flow/dunning sin tocar billing real.

## Uso

```text
/plan-churn-prevention [agencia/cliente] [flujo/problema] [--write]
```

## Workflow

1. Leer `.claude/skills/churn-prevention/SKILL.md`.
2. Leer contexto y `quality/criterios-output.md`.
3. Confirmar tipo de churn, billing, motivos, segmentos y restricciones.
4. Entregar usando `templates/churn-prevention-plan.md`.

## Reglas

- No tocar billing.
- No cambiar cancel flows.
- No activar emails.
- Si hay implementacion real, abrir Orden de Cambio.
