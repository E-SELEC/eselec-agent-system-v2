# auditar-ai-seo

Audita visibilidad en respuestas AI y prepara un plan AI SEO sin tocar produccion.

## Uso

```text
/auditar-ai-seo [cliente] [queries/plataforma opcional] [--write]
```

Ejemplos:

```text
/auditar-ai-seo cliente-servicios reparacion ordenadores
/auditar-ai-seo cliente-local SEO local + AI Overviews
/auditar-ai-seo agencia-demo servicios marketing digital
```

## Workflow

1. Leer `.claude/skills/ai-seo/SKILL.md`.
2. Definir objetivo, mercado, idioma y plataformas.
3. Leer:
   - `clients/[cliente]/context.md` o `agency/context.md`
   - memoria/log/mensajes/tasks si existen
   - outputs/manifest si existe
4. Definir 10-20 queries si Rodrigo no las da.
5. Registrar evidencia por plataforma si se prueba en vivo o con capturas.
6. Revisar fundamentos SEO, schema, arquitectura y extractabilidad.
7. Entregar usando `templates/auditoria-ai-seo.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/auditoria-ai-seo-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No prometer aparicion en AI.
- No cambiar robots.txt.
- No cambiar CDN/WAF/noindex/sitemap.
- No publicar contenido.
- No inventar datos de visibilidad.
- Si hay implementacion real, abrir Orden de Cambio.
