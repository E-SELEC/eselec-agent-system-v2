# revisar-web-visual

Revisa visualmente una pagina web contra una referencia o criterio de calidad.

## Uso

```text
/revisar-web-visual [cliente] [url/screenshot] [referencia] [--write]
```

## Workflow

1. Leer `.claude/skills/web-feedback-loop/SKILL.md`.
2. Leer contexto de cliente y protocolos.
3. Capturar estado actual y referencia.
4. Entregar usando `templates/web-feedback-report.md`.

## Reglas

- No editar web real sin Orden de Cambio.
- No instalar plugins ni tocar CSS/tema sin aprobacion.
- Verificar mobile y desktop si se implementa.
