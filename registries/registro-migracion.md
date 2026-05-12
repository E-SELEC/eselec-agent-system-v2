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

### 2026-05-12 - decision de prioridad P0 seguridad/protocolos
- Responsable: Codex + Arquitecto
- Tipo: decision de migracion
- Responsabilidad real: ordenar la primera fase de trabajo despues del plan maestro.
- Destino Claude Code: `planning/backlog-migracion.md`, `planning/sprint-00-seguridad-protocolos.md`
- Decision: conservar
- Motivo: antes de mejorar outputs SEO/informes hay que blindar secretos, artefactos, activos criticos y cierre para no migrar riesgos al sistema v2.
- Riesgo: bajo; decision organizativa sin datos privados.
- Prueba de calidad: P0 tiene sprint propio, criterios de salida y backlog marcado.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-001 inventario legacy inicial
- Responsable: Codex + Arquitecto
- Tipo: inventario de migracion
- Responsabilidad real: mapear el sistema legacy por areas, responsabilidades, riesgos y destino Claude Code probable antes de migrar piezas.
- Destino Claude Code: `planning/inventario-legacy.md`
- Decision: conservar
- Motivo: evita migrar por carpetas completas y crea base para P0-002 y protocolos criticos.
- Riesgo: bajo; no contiene secretos ni valores de credenciales.
- Prueba de calidad: incluye resumen cuantitativo, mapa de destinos Claude Code, clasificacion por carpetas, riesgos y siguiente accion.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-002 auditoria scripts con secretos historicos
- Responsable: Codex + Arquitecto
- Tipo: auditoria de seguridad
- Responsabilidad real: detectar scripts legacy que no deben migrarse al v2 sin saneamiento por credenciales hardcodeadas, OAuth, tokens, `.env`, servicios externos o produccion.
- Destino Claude Code: `planning/auditoria-scripts-sensibles.md`, `registries/registro-accesos.md`
- Decision: conservar
- Motivo: bloquea la migracion insegura de scripts y prepara P0-003 gestion-secretos.
- Riesgo: bajo; no contiene valores de secretos.
- Prueba de calidad: clasifica scripts bloqueados, alto riesgo, revisables y bajo riesgo; define acciones antes de migrar.
- Estado: implementado
- Commit: pendiente
