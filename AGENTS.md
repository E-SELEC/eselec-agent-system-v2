# E-SELEC v2 - Instrucciones para agentes

## Identidad

E-SELEC es una agencia de marketing digital orientada a soluciones data-driven para clientes internacionales.

## Regla principal

Antes de ejecutar, identifica el modo:

- `cliente`: trabajo para un cliente concreto.
- `agencia`: trabajo interno de E-SELEC.
- `sistema`: arquitectura, protocolos, agentes, scripts o automatizaciones.

## Lectura obligatoria por modo

### Cliente

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md`
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md`

### Agencia

1. `agency/context.md`
2. `agency/brand.md`
3. `agency/log.md`
4. `agency/mensajes.md`

### Sistema

1. `core/fuentes-de-verdad.md`
2. `core/prioridades.md`
3. `knowledge/README.md`
4. `protocols/README.md`
5. `protocols/migracion-claude-code.md`
6. `registries/registro-fuentes.md`
7. `registries/registro-artefactos.md`
8. `registries/registro-accesos.md`
9. `registries/registro-migracion.md`

## Migracion desde legacy

Toda migracion desde el sistema anterior debe pasar por el rol `arquitecto-migracion-claude` o por la skill `migration-audit`.

No se permite migrar por carpetas completas. Se migra por responsabilidad y se decide el destino correcto segun Claude Code: `CLAUDE.md`, rules, skills, subagents, commands, MCP, scripts, memoria, registros o legacy.

## Gestion de conocimiento

Toda URL, documentacion, nota, captura, export, aprendizaje o informacion nueva debe pasar por `bibliotecario`, `/ingestar-conocimiento` o la skill `gestion-conocimiento` antes de crear carpetas o archivos nuevos.

El destino por defecto de fuentes externas es `knowledge/` + `registries/registro-fuentes.md`, no `planning/` ni carpetas de cliente.

## Seguridad

- Nunca guardes secretos reales en este repositorio.
- Nunca subas `.env`, tokens, credenciales OAuth, application passwords ni claves API.
- Antes de tocar webs, Ads, GBP, WooCommerce, WordPress, automatizaciones o datos reales, abre Orden de Cambio.
- Si detectas credenciales en codigo, no las reproduzcas: registra metadatos y recomienda rotacion.

## Cierre

Toda tarea con cambios debe cerrar con:

- Que se pidio.
- Que se hizo.
- Que archivos cambiaron.
- Que no se toco.
- Riesgos o bloqueos.
- Estado actual.
- Siguiente paso recomendado.

