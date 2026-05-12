# Protocolo de Migracion Claude Code

## Proposito

Migrar el sistema legacy E-SELEC al sistema v2 de forma ordenada, comprobable y alineada con Claude Code.

Este protocolo existe porque el sistema legacy contiene valor real, pero tambien mezcla prompts largos, protocolos, memoria, scripts, outputs, criterios, historico y accesos sensibles.

## Principio base

La unidad de migracion no es el archivo. Es la responsabilidad.

## Fases

### Fase 1 - Inventario

Para cada pieza candidata:

- Ruta.
- Tipo.
- Responsable.
- Proposito.
- Estado.
- Riesgo.
- Duplicados.
- Fuente de verdad.

### Fase 2 - Clasificacion Claude Code

Asignar una primitiva:

- `CLAUDE.md`
- `.claude/rules/`
- `.claude/skills/`
- `.claude/agents/`
- `.claude/commands/`
- `.claude/settings.json`
- `.mcp.json`
- `scripts/`
- `clients/`
- `agency/`
- `legacy/`

### Fase 3 - Saneamiento

Antes de migrar:

- Eliminar secretos.
- Separar historico de instruccion.
- Reducir texto redundante.
- Resolver contradicciones.
- Definir activador y criterio de salida.
- Anadir ejemplo o prueba cuando el output sea subjetivo.

### Fase 4 - Migracion

Crear o modificar la pieza v2 minima necesaria.

No se permite:

- Copiar carpetas completas sin filtro.
- Meter procedimientos largos en `CLAUDE.md`.
- Convertir memoria de cliente en skill.
- Crear subagents sin descripcion clara y herramientas acotadas.
- Subir scripts que toquen produccion sin dry-run.

### Fase 5 - Comprobacion

Toda migracion debe pasar:

- Revision de duplicados.
- Revision de secretos.
- Revision de activador.
- Revision de salida.
- Prueba manual o checklist.
- Registro en `registries/registro-migracion.md`.

### Fase 6 - Compaginacion

Despues de migrar, comprobar que la nueva pieza convive con:

- `CLAUDE.md`
- `AGENTS.md`
- Reglas existentes.
- Skills existentes.
- Subagents existentes.
- Registros.
- Fuentes de verdad.

Si hay conflicto, se corrige antes de continuar.

## Criterio de exito

Una migracion es buena cuando mejora al menos una de estas dimensiones:

- Calidad del output.
- Claridad de activacion.
- Reduccion de contexto.
- Seguridad.
- Trazabilidad.
- Reutilizacion.
- Menos contradicciones.
- Mejor criterio operativo.

## Criterio de rechazo

No migrar si:

- La pieza es obsoleta.
- Solo duplica otra instruccion.
- Depende de secretos no saneados.
- No tiene utilidad operativa actual.
- Produce outputs sin criterio verificable.
