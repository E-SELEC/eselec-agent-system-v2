---
name: migration-audit
description: Audita una pieza del sistema legacy E-SELEC y decide como migrarla al sistema v2 usando primitivas oficiales de Claude Code.
allowed-tools: Read Grep Glob
---

# Migration Audit

Usa esta skill cuando tengas que evaluar una pieza legacy antes de migrarla.

## Objetivo

Evitar migraciones por arrastre. La salida debe decidir si la pieza se conserva, fusiona, reescribe, archiva o no se migra.

## Proceso

1. Lee la pieza legacy candidata.
2. Identifica su responsabilidad real.
3. Busca duplicados o contradicciones en v2.
4. Clasifica el destino correcto:
   - `CLAUDE.md`
   - `.claude/rules/`
   - `.claude/skills/`
   - `.claude/agents/`
   - `.claude/commands/`
   - `.mcp.json`
   - `scripts/`
   - `clients/`
   - `agency/`
   - `legacy/`
5. Evalua riesgo de secreto o activo critico.
6. Define prueba de calidad.
7. Registra decision en `registries/registro-migracion.md`.

## Checklist de calidad

- La pieza tiene una sola responsabilidad.
- No duplica otra fuente viva.
- No mezcla procedimiento con historico.
- No incluye secretos ni rutas privadas innecesarias.
- Tiene activador claro.
- Tiene criterio de salida.
- Tiene verificacion.

## Salida

```text
Pieza evaluada:
Responsabilidad:
Destino recomendado:
Decision:
Motivo:
Riesgos:
Prueba de calidad:
Registro a crear:
```
