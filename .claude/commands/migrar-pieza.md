---
description: Evalua una pieza legacy y prepara su migracion al sistema v2 sin copiarla automaticamente.
argument-hint: "<ruta-legacy> [objetivo]"
---

# Migrar pieza legacy

Evalua la pieza indicada usando:

- `.claude/rules/migracion-claude-code.md`
- `.claude/skills/migration-audit/SKILL.md`
- `protocols/migracion-claude-code.md`
- `registries/registro-migracion.md`

No copies archivos automaticamente. Primero produce dictamen:

1. Responsabilidad real.
2. Destino Claude Code correcto.
3. Decision: conservar, fusionar, reescribir, archivar o no migrar.
4. Riesgos.
5. Prueba de calidad.
6. Registro necesario.

Argumentos recibidos:

```text
$ARGUMENTS
```
