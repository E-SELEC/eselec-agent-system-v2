# humanizar-texto

Humaniza un texto sin cambiar su mensaje central.

## Uso

```text
/humanizar-texto [agencia/cliente] [texto o archivo] [--write]
```

## Workflow

1. Leer `.claude/skills/humanizalo/SKILL.md`.
2. Leer contexto de agencia o cliente si aplica.
3. Confirmar canal, audiencia, tono y libertad de edicion.
4. Entregar usando `templates/humanization-review.md`.

## Reglas

- No inventar claims.
- No cambiar intencion legal/comercial sensible.
- Si se escribe archivo, registrar artefacto.
