# auditar-schema

Audita o disena schema JSON-LD para una pagina sin tocar produccion.

## Uso

```text
/auditar-schema [cliente] [URL o alcance opcional] [--write]
```

Ejemplos:

```text
/auditar-schema computer-chamberi home
/auditar-schema la-bottega-del-gusto LocalBusiness
/auditar-schema cashier-bubble-tea producto WooCommerce
```

## Workflow

1. Leer `.claude/skills/schema-markup/SKILL.md`.
2. Identificar pagina, URL, tipo de contenido y objetivo.
3. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
4. Verificar contenido visible o marcar SM0/SM1.
5. Revisar schema actual si hay HTML, crawl, captura o fuente viva.
6. Elegir tipos segun `references/schema-types.md`.
7. Entregar usando `templates/plan-schema.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/schema-markup-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No tocar WordPress.
- No tocar plugins SEO.
- No tocar WooCommerce.
- No publicar JSON-LD.
- No cambiar GTM ni templates reales.
- No inventar reviews, rating, precio, stock, horarios ni datos locales.
- Si hay implementacion real, abrir Orden de Cambio.
