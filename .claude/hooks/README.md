# Hooks Claude

Aqui viviran hooks de seguridad y cierre.

Prioridad inicial:

1. Bloquear secretos. Implementado en `block-sensitive-data.py`.
2. Detectar cambios en activos criticos.
3. Exigir registro de artefactos.
4. Ejecutar guard de cierre.

## Hook activo

### `block-sensitive-data.py`

Tipo: `PreToolUse`.

Matcher:

```text
Write|Edit|MultiEdit|Bash
```

Funcion:

- bloquea escrituras sobre rutas sensibles como `.env`, credenciales, tokens, llaves privadas y archivos de certificado;
- bloquea valores sensibles de alta confianza;
- bloquea asignaciones con nombres sensibles y valores no placeholder;
- bloquea comandos shell que intenten escribir, mover o versionar archivos sensibles.

Autoprueba:

```bash
python .claude/hooks/block-sensitive-data.py --self-test
```

Fuente operativa:

- `protocols/gestion-accesos.md`
- `protocols/control-artefactos.md`
- `protocols/activos-criticos.md`
