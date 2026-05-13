# producir-video-kling

Prepara prompts y parametros para un video AI con Kling sin ejecutarlo.

## Uso

```text
/producir-video-kling [agencia/cliente] [idea de video] [--write]
```

## Workflow

1. Leer `.claude/skills/kling-producer/SKILL.md`.
2. Confirmar sujeto, destino, mood, estilo, movimiento y restricciones.
3. Revisar imagen de referencia si existe.
4. Entregar usando `templates/video-production-plan.md`.

## Reglas

- No usar `--execute` sin aprobacion explicita.
- No consumir creditos sin mostrar coste.
- No usar imagenes sin permiso.
- Si se genera output de cliente, registrar artefacto.
