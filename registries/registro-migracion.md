# Registro de migracion

Este registro documenta decisiones de migracion desde el sistema legacy E-SELEC al sistema v2.

## Formato

```text
### YYYY-MM-DD - pieza legacy
- Responsable:
- Tipo:
- Responsabilidad real:
- Destino Claude Code:
- Decision: conservar | fusionar | reescribir | archivar | no migrar
- Motivo:
- Riesgo:
- Prueba de calidad:
- Estado:
- Commit:
```

## Entradas

### 2026-05-12 - rol arquitecto-migracion-claude
- Responsable: Codex + Arquitecto
- Tipo: subagent / protocolo / skill / command
- Responsabilidad real: crear el rol que gobernara la migracion del sistema legacy al sistema v2 siguiendo Claude Code.
- Destino Claude Code: `.claude/agents/`, `.claude/rules/`, `.claude/skills/`, `.claude/commands/`, `protocols/`
- Decision: conservar
- Motivo: el sistema necesita una autoridad de migracion que evite copiar desorden y diagnostique problemas de calidad como fallos de arquitectura, no solo como fallos del modelo.
- Riesgo: bajo; no migra datos de clientes ni secretos.
- Prueba de calidad: existe mapa de decision, formato de dictamen, checklist de calidad y registro obligatorio.
- Estado: implementado
- Commit: este mismo cambio; consultar `git log --oneline` para el hash final.
