# plan-email-sequence

Disena una secuencia de email sin activarla.

## Uso

```text
/plan-email-sequence [agencia/cliente] [tipo/trigger] [--write]
```

## Workflow

1. Leer `.claude/skills/email-sequence/SKILL.md`.
2. Leer contexto de agencia o cliente y `quality/criterios-output.md`.
3. Confirmar trigger, audiencia, objetivo, consentimiento y exit conditions.
4. Entregar usando `templates/email-sequence-plan.md`.

## Reglas

- No activar automatizaciones.
- No importar listas.
- No enviar emails.
- Si hay implementacion real, abrir Orden de Cambio.
