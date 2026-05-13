# crear-product-marketing-context

Crea o actualiza contexto de product marketing con posicionamiento, ICP, customer language y proof points.

## Uso

```text
/crear-product-marketing-context [agencia/cliente] [producto/oferta] [--write]
```

## Workflow

1. Leer `.claude/skills/product-marketing-context/SKILL.md`.
2. Leer contexto de agencia o cliente, `quality/criterios-output.md` y `protocols/control-artefactos.md`.
3. Buscar contexto existente y fuentes aprobadas.
4. Entregar usando `templates/product-marketing-context.md`.
5. Si `--write`, guardar en la ruta acordada y registrar artefacto.

## Reglas

- No guardar contexto dentro de `.claude/skills/`.
- No inventar claims.
- No sobrescribir contexto vivo sin control de artefactos.
- Contradicciones relevantes se escalan antes de escribir.
