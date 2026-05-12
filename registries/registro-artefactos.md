# Registro de artefactos

Este registro lista archivos, carpetas, outputs, scripts o documentos operativos creados o modificados por agentes.

## Formato

```text
### YYYY-MM-DD - ruta
- Area:
- Agente:
- Tipo:
- Motivo:
- Estado:
- Reemplaza a:
- Accion recomendada:
- Riesgo:
```

## Entradas

### 2026-05-12 - rol de migracion Claude Code
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: rol/protocolo/skill/command
- Motivo: crear la autoridad operativa que migrara el sistema legacy al sistema v2 usando primitivas oficiales de Claude Code.
- Estado: vigente
- Reemplaza a: migraciones manuales sin criterio unificado.
- Accion recomendada: usar antes de mover cualquier pieza legacy.
- Riesgo: bajo; no incluye secretos ni datos de clientes.

### 2026-05-12 - planning/plan-maestro-migracion.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: plan maestro / backlog
- Motivo: organizar la migracion completa para que Rodrigo entienda que se hara, por que se hara y como se comprobara, siguiendo Claude Code y considerando la complejidad del sistema legacy.
- Estado: vigente
- Reemplaza a: avance por intuicion o por tareas sueltas sin secuencia global.
- Accion recomendada: usar como mapa de ruta en cada sesion de migracion y actualizar backlog al cerrar fases.
- Riesgo: bajo; documento operativo sin secretos ni datos privados de clientes.

### 2026-05-12 - planning/inventario-legacy.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: inventario de migracion
- Motivo: completar P0-001 mapeando el sistema legacy por areas, responsabilidades, riesgos y destino Claude Code probable.
- Estado: vigente
- Reemplaza a: lectura informal del legacy sin mapa operativo.
- Accion recomendada: usar como entrada para P0-002 auditoria de scripts con secretos historicos.
- Riesgo: bajo; no contiene secretos ni valores de credenciales.

### 2026-05-12 - planning/auditoria-scripts-sensibles.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: auditoria de seguridad / scripts
- Motivo: completar P0-002 detectando scripts legacy con credenciales hardcodeadas, OAuth, tokens, escrituras de `.env`, servicios externos o riesgo de produccion.
- Estado: vigente
- Reemplaza a: sospecha informal sobre scripts sensibles.
- Accion recomendada: ejecutar P0-003 `gestion-secretos` antes de migrar cualquier script S3/S4.
- Riesgo: bajo como documento; no contiene valores secretos.

### 2026-05-12 - protocols/gestion-accesos.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: protocolo / regla
- Motivo: completar P0-003 migrando el protocolo canonico legacy de gestion de secretos al sistema v2 adaptado a Claude Code, scripts, MCP, hooks y registros.
- Estado: vigente
- Reemplaza a: dependencia del protocolo legacy `sistema/protocolos/gestion-secretos.md` como unica fuente.
- Accion recomendada: usar antes de migrar scripts, conectores, MCP o cualquier acceso S2/S3/S4.
- Riesgo: bajo; no contiene valores secretos.

### 2026-05-12 - protocols/control-artefactos.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: protocolo / regla
- Motivo: completar P0-004 migrando el protocolo canonico legacy de control de artefactos al sistema v2, adaptado a GitHub, `.claude/`, outputs ignorados, manifests y registros.
- Estado: vigente
- Reemplaza a: dependencia del protocolo legacy `sistema/protocolos/control-artefactos.md` como unica fuente.
- Accion recomendada: usar antes de crear, modificar, mover, archivar o eliminar archivos/carpetas relevantes.
- Riesgo: bajo; protocolo sin datos privados ni secretos.

### 2026-05-12 - protocols/activos-criticos.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: protocolo / regla
- Motivo: completar P0-005 migrando el protocolo canonico legacy de activos criticos al sistema v2, con niveles A/B/C/D, Orden de Cambio, fuentes de verdad, diagnostico por capas y relacion con Claude Code.
- Estado: vigente
- Reemplaza a: dependencia del protocolo legacy `sistema/protocolos/activos-criticos.md` como unica fuente.
- Accion recomendada: usar antes de tocar produccion, datos vivos, fuentes de verdad, scripts externos, MCP, Ads, WordPress, WooCommerce, hosting, DNS o accesos.
- Riesgo: bajo; protocolo sin datos privados ni secretos.

### 2026-05-12 - protocols/cierre-humano.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: protocolo / regla
- Motivo: completar P0-006 migrando el protocolo canonico legacy de cierre humano al sistema v2 para que cada tarea cierre con explicacion clara, estado, riesgos y siguiente paso.
- Estado: vigente
- Reemplaza a: dependencia del protocolo legacy `sistema/protocolos/cierre-humano.md` como unica fuente.
- Accion recomendada: usar al cerrar cualquier tarea con trabajo detras, cambios, riesgos, commits, registros, scripts o migracion.
- Riesgo: bajo; protocolo sin datos privados ni secretos.

### 2026-05-12 - .claude/hooks/block-sensitive-data.py
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: hook de seguridad / configuracion Claude Code
- Motivo: completar P0-007 creando un hook `PreToolUse` que bloquea escrituras o comandos con rutas o valores sensibles antes de que se ejecuten.
- Estado: vigente
- Reemplaza a: proteccion manual basada solo en `.gitignore` y protocolo escrito.
- Accion recomendada: ejecutar `python .claude/hooks/block-sensitive-data.py --self-test` despues de modificar el hook o `.claude/settings.json`.
- Riesgo: bajo; el script contiene patrones defensivos y datos de prueba construidos sin valores reales.

### 2026-05-12 - quality/diagnostico-calidad.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: diagnostico de calidad / matriz de causas raiz
- Motivo: completar P1-001 identificando por que los outputs pueden carecer de calidad, criterio o acertividad y que piezas v2 deben corregirlo.
- Estado: vigente
- Reemplaza a: diagnostico informal de baja calidad sin matriz accionable.
- Accion recomendada: usar como base directa de P1-002 `quality/criterios-output.md`.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - quality/criterios-output.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: criterios de calidad / contratos de salida
- Motivo: completar P1-002 creando contratos verificables para auditorias, SEO, informes, proximos pasos, CRO, SEM, Social, Web, Copy y Agencia.
- Estado: vigente
- Reemplaza a: criterios dispersos en prompts legacy sin aceptacion estandarizada por entregable.
- Accion recomendada: usar como fuente obligatoria al migrar skills y lideres operativos.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/skills/client-audit/
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: skill operativa Claude Code
- Motivo: completar P1-003 migrando `client-audit` como skill bajo demanda con plantilla y checklist de calidad.
- Estado: vigente
- Reemplaza a: `.agents/skills/client-audit/SKILL.md` como prompt legacy directo.
- Accion recomendada: usar como primera skill piloto para auditorias de cliente antes de migrar Lider Clientes.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/skills/seo-audit/
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: skill operativa Claude Code
- Motivo: completar P1-004 migrando `seo-audit` como skill bajo demanda con evidencia, jerarquia de fuentes, plantilla y checklist de revision.
- Estado: vigente
- Reemplaza a: `.agents/skills/seo-audit/SKILL.md` como prompt legacy directo.
- Accion recomendada: usar como skill piloto para auditorias SEO antes de migrar Lider SEO.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/agents/docente.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: subagent Claude Code / aprendizaje operativo
- Motivo: completar P1-005 migrando El Docente como rol read-only para convertir fallos y correcciones en criterio examinable.
- Estado: vigente
- Reemplaza a: `agents/docente/docente.md` como prompt legacy directo.
- Accion recomendada: usar despues de outputs rechazados, correcciones de Rodrigo o fallos de criterio repetibles.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/agents/leader-clientes.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: subagent Claude Code / orquestacion de clientes
- Motivo: completar P2-001 creando Lider Clientes v2 como orquestador ligero, read-only y alineado con skills/reglas/contratos de calidad.
- Estado: vigente
- Reemplaza a: `agents/leader-clients.md` como prompt legacy directo.
- Accion recomendada: usar al mencionar un cliente, revisar estado, priorizar proximos pasos o enrutar trabajo hacia `client-audit`/`seo-audit`.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/agents/leader-agencia.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: subagent Claude Code / orquestacion interna
- Motivo: completar P2-002 creando Lider Agencia v2 como orquestador ligero y read-only para trabajo interno de E-SELEC.
- Estado: vigente
- Reemplaza a: `agents/agency/leader-agency.md` como prompt legacy directo.
- Accion recomendada: usar con modo agencia, tareas internas, captacion, reputacion, onboarding, retencion, finanzas y operaciones internas.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/commands/alertas-pendientes.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: command Claude Code / workflow recurrente
- Motivo: completar P2-003 convirtiendo `LOOP: alertas-pendientes` en command invocable con lectura consolidada y escritura opcional.
- Estado: vigente
- Reemplaza a: seccion `LOOP 3 - Alertas Pendientes` de `agents/loops/leader-loops.md`.
- Accion recomendada: usar para revisar mensajes pendientes antes de reuniones, cierres semanales o decisiones de prioridad.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/commands/auditoria-semanal.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: command Claude Code / workflow recurrente
- Motivo: completar P2-004 convirtiendo `LOOP: auditoria-semanal` en command invocable para detectar bloqueos, estancamientos y tareas atascadas.
- Estado: vigente
- Reemplaza a: seccion `LOOP 1 - Auditoria Semanal` de `agents/loops/leader-loops.md`.
- Accion recomendada: usar al inicio de semana o antes de planificar prioridades de clientes.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - planning/piloto-01.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: decision operativa / piloto
- Motivo: completar P2-005 definiendo Computer Chamberi como primer cliente piloto para probar operacion v2 sin tocar produccion.
- Estado: vigente
- Reemplaza a: decision informal de cliente piloto.
- Accion recomendada: ejecutar P3-002 migrando estructura minima de `computer-chamberi`.
- Riesgo: bajo; no contiene secretos ni datos privados sensibles.

