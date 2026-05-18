# plan-arquitectura-web

Disena o audita la arquitectura web de un cliente sin tocar produccion.

## Uso

```text
/plan-arquitectura-web [cliente] [alcance opcional] [--write]
```

Ejemplos:

```text
/plan-arquitectura-web cliente-servicios servicios y SEO local
/plan-arquitectura-web cliente-ecommerce menu y URLs
/plan-arquitectura-web cliente-local redisenar estructura
```

## Workflow

1. Leer `.claude/skills/site-architecture/SKILL.md`.
2. Identificar alcance: web nueva, reestructura, menu, URLs, enlazado interno o migracion.
3. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
4. Verificar si hay datos SEO/conversion suficientes. Si no, marcar SA1/SA2.
5. Si se usan exports o outputs legacy, pasar por `ingesta-evidencia`.
6. Clasificar nivel SA0/SA1/SA2/SA3.
7. Entregar usando `templates/arquitectura-web.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/arquitectura-web-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No tocar WordPress.
- No tocar WooCommerce.
- No cambiar menus reales.
- No crear redirects reales.
- No cambiar canonical, noindex, sitemap ni robots.
- No publicar cambios de tracking.
- No cambiar URLs sin inventario y plan 301.
- Si hay implementacion real, abrir Orden de Cambio.
