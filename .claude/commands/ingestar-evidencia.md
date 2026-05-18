# ingestar-evidencia

Convierte un export, captura, output legacy o dato vivo en evidencia saneada para v2.

## Uso

```text
/ingestar-evidencia [cliente] [fuente/tema] [--write]
```

Ejemplos:

```text
/ingestar-evidencia cliente-servicios GSC
/ingestar-evidencia cliente-servicios SEMrush --write
/ingestar-evidencia cliente-b2b Meta Ads
```

## Workflow

1. Leer `.claude/skills/ingesta-evidencia/SKILL.md`.
2. Identificar cliente, fuente, periodo y decision que se quiere soportar.
3. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/outputs/manifest.md`
4. Clasificar riesgo: bajo, medio, alto o bloqueado.
5. Clasificar evidencia: E0, E1, E2 o E3.
6. Extraer solo metricas y hallazgos necesarios.
7. Declarar limitaciones y decisiones permitidas/prohibidas.
8. Si no se usa `--write`, responder en chat.
9. Si se usa `--write`, guardar:

```text
clients/[cliente]/outputs/evidencia-[tema]-YYYY-MM-DD.md
```

## Reglas

- No guardar exports brutos en GitHub.
- No reproducir secretos ni PII.
- No convertir E1/E2 en output final.
- No mezclar datos reales con estimaciones sin etiquetarlo.
- No tocar produccion.

## Cierre con escritura

Si se crea archivo:

- actualizar `clients/[cliente]/outputs/manifest.md`;
- actualizar `clients/[cliente]/log.md`;
- actualizar `registries/registro-artefactos.md` si tiene impacto estrategico o reusable;
- ejecutar checks de secretos antes de commit.
