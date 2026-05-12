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
3. `protocols/README.md`
4. `registries/registro-artefactos.md`
5. `registries/registro-accesos.md`

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

