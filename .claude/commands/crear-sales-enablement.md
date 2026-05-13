# crear-sales-enablement

Crea un material comercial sin enviarlo ni publicarlo.

## Uso

```text
/crear-sales-enablement [agencia/cliente] [asset/persona] [--write]
```

## Workflow

1. Leer `.claude/skills/sales-enablement/SKILL.md`.
2. Leer contexto de agencia o cliente y `quality/criterios-output.md`.
3. Confirmar asset, usuario, etapa, persona, objetivo y claims permitidos.
4. Entregar usando `templates/sales-enablement-asset.md`.

## Reglas

- No enviar propuestas finales.
- No usar pricing no aprobado.
- No inventar pruebas.
- Si hay envio/publicacion real, abrir Orden de Cambio.
