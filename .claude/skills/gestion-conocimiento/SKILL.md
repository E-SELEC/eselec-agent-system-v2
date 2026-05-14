---
name: gestion-conocimiento
description: >
  Clasifica, sanea y ubica informacion nueva en E-SELEC v2. Usar cuando entren
  URLs, documentacion oficial, notas, capturas, exports, aprendizajes, outputs
  legacy o cualquier material que deba organizarse en carpetas, knowledge,
  protocols, skills, agents, commands, clients, agency, quality, planning o legacy.
---

# Gestion Conocimiento

## Proposito

Poner orden antes de guardar informacion nueva.

Esta skill decide si algo se guarda, se resume, se convierte en pieza operativa o se descarta.

## Fuentes obligatorias

Lee:

1. `knowledge/README.md`
2. `protocols/gestion-conocimiento.md`
3. `registries/registro-fuentes.md`
4. `core/fuentes-de-verdad.md`

Si el tema es Claude Code, lee `knowledge/claude-code/indice-oficial.md`.

## Workflow

1. Identifica la fuente: URL, archivo, nota, export o aprendizaje.
2. Clasifica tipo: oficial, evidencia, procedimiento, regla, rol, comando, memoria, preferencia, historico o ruido.
3. Clasifica nivel: K3, K2, K1 o K0.
4. Busca duplicados en el destino probable.
5. Decide destino unico.
6. Resume solo lo necesario.
7. Registra en `registries/registro-fuentes.md`.
8. Si crea o modifica archivos, registra en `registries/registro-artefactos.md`.
9. Ejecuta guard antes de cerrar.

## Destino rapido

| Tipo | Destino |
|---|---|
| Fuente oficial | `knowledge/[fuente]/` |
| Regla obligatoria | `protocols/` o `.claude/rules/` |
| Procedimiento reutilizable | `.claude/skills/` |
| Rol/routing | `.claude/agents/` |
| Comando repetible | `.claude/commands/` |
| Evidencia de cliente | `clients/[cliente]/outputs/evidencia-*.md` |
| Memoria cliente | `clients/[cliente]/memory.md` |
| Preferencia Rodrigo | `agency/preferencias-rodrigo.md` previa aprobacion |
| Calidad | `quality/` |
| Roadmap | `planning/` |
| Historico | `legacy/` |

## Bloqueos

No guardar si contiene:

- secretos;
- tokens;
- passwords;
- cookies;
- PII;
- dumps completos;
- fuente equivocada;
- datos vivos no verificados;
- material sin decision posible.

## Salida

```text
CONOCIMIENTO

FUENTE:

TIPO:

NIVEL:

DESTINO:

DECISION:

RIESGOS:

REGISTROS:

SIGUIENTE PASO:
```
