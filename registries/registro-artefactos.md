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

