# limpiar-carpeta-cliente

Audita y propone limpieza de carpeta de cliente. Ejecutar cambios requiere aprobacion.

## Uso

```text
/limpiar-carpeta-cliente [cliente] [carpeta/opcional] [--write]
```

## Workflow

1. Leer `.claude/skills/folder-cleanup/SKILL.md`.
2. Leer contexto, log, mensajes, tasks y manifest.
3. Inventariar sin mover nada.
4. Entregar propuesta usando `templates/folder-cleanup-report.md`.
5. Si hay aprobacion explicita, ejecutar solo acciones aprobadas y registrar.

## Reglas

- No borrar sin aprobacion.
- No usar delete recursivo.
- No tocar rutas fuera del cliente.
- Si hay contradiccion, parar y preguntar.
