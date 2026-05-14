# /ingestar-conocimiento

Clasifica informacion nueva y decide donde debe vivir en E-SELEC v2.

## Uso

```text
/ingestar-conocimiento [URL, ruta, nota o tema]
/ingestar-conocimiento --write [URL, ruta, nota o tema]
```

## Objetivo

Evitar que nuevas fuentes, aprendizajes, capturas, exports o documentos entren al sistema como archivos sueltos.

## Reglas

- Sin `--write`: solo clasifica y propone destino.
- Con `--write`: crea o modifica archivos minimos si el destino es seguro.
- No guardar secretos, tokens, cookies, passwords ni sesiones.
- No copiar documentacion completa si basta URL + resumen + decision.
- No tocar produccion ni fuentes vivas.
- Si es preferencia de Rodrigo, proponer antes de escribir.
- Si es evidencia de cliente, usar `ingesta-evidencia`.
- Si afecta medicion, usar `verificacion-medicion`.

## Lectura

1. `knowledge/README.md`
2. `protocols/gestion-conocimiento.md`
3. `registries/registro-fuentes.md`
4. `core/fuentes-de-verdad.md`
5. destino candidato segun tipo

## Clasificacion

| Tipo | Destino |
|---|---|
| Documentacion oficial | `knowledge/[fuente]/` |
| Regla | `protocols/` o `.claude/rules/` |
| Procedimiento | `.claude/skills/` |
| Rol | `.claude/agents/` |
| Comando | `.claude/commands/` |
| Evidencia | `clients/[cliente]/outputs/evidencia-*.md` |
| Preferencia | `agency/preferencias-rodrigo.md` previa aprobacion |
| Historico | `legacy/` |
| Ruido | descartar |

## Salida

```text
CONOCIMIENTO
FUENTE:
TIPO:
NIVEL:
DESTINO:
DECISION:
RIESGOS:
ARCHIVOS:
SIGUIENTE PASO:
```

## Escritura

Si se usa `--write`:

1. crear o modificar archivo minimo;
2. actualizar `registries/registro-fuentes.md`;
3. actualizar `registries/registro-artefactos.md` si hay archivo nuevo o estructural;
4. ejecutar `git diff --check`;
5. ejecutar `python scripts/protocol_guard.py --no-report`.
