# crear-prompt

Crea o mejora un prompt listo para usar en una herramienta IA.

## Uso

```text
/crear-prompt [target tool] [tarea] [--write]
```

## Workflow

1. Leer `.claude/skills/prompt-master/SKILL.md`.
2. Confirmar target tool si falta.
3. Extraer tarea, formato, restricciones y criterios de exito.
4. Entregar usando `templates/prompt-output.md`.

## Reglas

- No ejecutar la herramienta destino.
- No pedir razonamiento visible.
- Si se escribe archivo, registrar artefacto.
