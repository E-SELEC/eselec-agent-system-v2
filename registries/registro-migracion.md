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

### 2026-05-12 - P0-003 protocolo gestion-secretos
- Responsable: Codex + Arquitecto
- Tipo: protocolo de seguridad
- Responsabilidad real: definir como se clasifican, registran, bloquean y rotan secretos/accesos en el sistema v2.
- Destino Claude Code: `protocols/gestion-accesos.md`, `.claude/rules/gestion-accesos.md`
- Decision: reescribir
- Motivo: adaptar el protocolo canonico legacy a la estructura Claude Code y a los hallazgos P0-002.
- Riesgo: bajo; no contiene valores de secretos.
- Prueba de calidad: incluye clasificacion S1-S4, ubicaciones permitidas, flujo operativo, politica para scripts, MCP y requisitos para hook P0-007.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-004 protocolo control-artefactos
- Responsable: Codex + Arquitecto
- Tipo: protocolo de trazabilidad
- Responsabilidad real: definir como se crean, ubican, registran y cierran artefactos en el sistema v2.
- Destino Claude Code: `protocols/control-artefactos.md`, `.claude/rules/control-artefactos.md`
- Decision: reescribir
- Motivo: adaptar el protocolo canonico legacy a la estructura v2, GitHub, `.claude/`, manifests, outputs ignorados y registros.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: incluye definicion de artefacto, registros, campos obligatorios, politica de repo, prohibiciones, cierre y checklist antes de commit.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-005 protocolo activos-criticos
- Responsable: Codex + Arquitecto
- Tipo: protocolo de seguridad operacional
- Responsabilidad real: definir como clasificar y aprobar acciones que puedan afectar produccion, datos, fuentes de verdad, integraciones o accesos.
- Destino Claude Code: `protocols/activos-criticos.md`, `.claude/rules/activos-criticos.md`
- Decision: reescribir
- Motivo: adaptar el protocolo canonico legacy a la estructura v2, Claude Code, scripts, MCP, subagents y fuentes de verdad.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: incluye niveles A/B/C/D, Orden corta/completa, diagnostico por capas, anti-restore, fuentes de verdad, condiciones de parada y checklist.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-006 protocolo cierre-humano
- Responsable: Codex + Arquitecto
- Tipo: protocolo de cierre / comunicacion operativa
- Responsabilidad real: definir como explicar a Rodrigo, al cierre de cada tarea, que se pidio, que se hizo, que cambio, que no se toco, que se encontro, estado y siguiente paso.
- Destino Claude Code: `protocols/cierre-humano.md`, `.claude/rules/cierre-humano.md`
- Decision: reescribir
- Motivo: adaptar el protocolo canonico legacy a la estructura v2 y al flujo de migracion con backlog, commits, registros y El Escolta.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: incluye cierre normal, cierre corto, checklist de migracion, tono obligatorio, relacion con Claude Code, El Escolta y otros protocolos.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-007 hook bloqueo de datos sensibles
- Responsable: Codex + Arquitecto
- Tipo: hook de seguridad
- Responsabilidad real: bloquear antes de ejecutar una herramienta los intentos de escribir, mover, versionar o introducir datos sensibles en archivos o comandos.
- Destino Claude Code: `.claude/hooks/block-sensitive-data.py`, `.claude/settings.json`
- Decision: conservar con adaptacion
- Motivo: Claude Code permite hooks `PreToolUse` con decision `deny`; este control convierte el protocolo de accesos sensibles en una barrera automatica.
- Riesgo: bajo; no contiene secretos reales y solo usa patrones defensivos.
- Prueba de calidad: autoprueba del hook, JSON valido de settings, busqueda defensiva de patrones sensibles y `git diff --check`.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P1-001 diagnostico de calidad de outputs
- Responsable: Codex + Arquitecto
- Tipo: diagnostico de calidad / matriz de causas raiz
- Responsabilidad real: explicar por que los outputs pueden salir flojos aunque el legacy tenga criterios y agentes, y definir decisiones de migracion para corregirlo.
- Destino Claude Code: `quality/diagnostico-calidad.md`, `quality/README.md`
- Decision: crear
- Motivo: antes de migrar skills o agentes de SEO/informes, el sistema necesita saber que problema de calidad esta corrigiendo.
- Riesgo: bajo; documento de arquitectura sin secretos ni datos privados.
- Prueba de calidad: cruza documentacion Claude Code, estructura legacy, matriz de causas, diagnostico por area y acciones P1.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P1-002 criterios de output por servicio
- Responsable: Codex + Arquitecto
- Tipo: criterios de calidad / contratos de salida
- Responsabilidad real: definir que debe cumplir cada tipo de entregable para considerarse bueno, parcial o bloqueado.
- Destino Claude Code: `quality/criterios-output.md`
- Decision: crear
- Motivo: corregir la causa Q-002 y Q-003 del diagnostico de calidad: criterio sin contrato y verificacion insuficiente.
- Riesgo: bajo; documento operativo sin secretos ni datos privados.
- Prueba de calidad: incluye criterios universales, escala 0-4, contratos por servicio, bloqueos y checklist final.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P1-003 skill client-audit
- Responsable: Codex + Arquitecto
- Tipo: skill operativa Claude Code
- Responsabilidad real: auditar un cliente existente o nuevo, reconstruir estado real y definir una proxima prioridad verificable.
- Destino Claude Code: `.claude/skills/client-audit/`
- Decision: reescribir
- Motivo: adaptar la skill legacy a Claude Code con instrucciones compactas, archivos de apoyo, contrato de salida y checklist.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: incluye `SKILL.md`, plantilla de auditoria, checklist de revision, bloqueos y relacion con `quality/criterios-output.md`.
- Estado: implementado
- Commit: pendiente
