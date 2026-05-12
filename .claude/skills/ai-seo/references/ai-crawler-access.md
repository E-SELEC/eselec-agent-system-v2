# Crawlers AI, robots.txt y acceso

Las reglas de bots AI cambian. Antes de modificar robots.txt o una configuracion de CDN, verifica documentacion oficial actual y abre Orden de Cambio.

## Fuentes oficiales utiles

- OpenAI publishers/developers FAQ: https://help.openai.com/en/articles/12627856-publishers-and-developers-faq
- Anthropic crawler help center: https://support.anthropic.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Perplexity crawler docs: https://docs.perplexity.ai/guides/bots
- Google common crawlers: https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers
- Google robots.txt interpretation: https://developers.google.com/search/reference/robots_txt

## Reglas operativas

- robots.txt controla crawling, no es una herramienta para ocultar contenido sensible.
- noindex, auth o password protegen indexacion/contenido de otra forma.
- `Googlebot` y `Google-Extended` no significan lo mismo.
- algunos proveedores separan bots de busqueda, entrenamiento y acciones iniciadas por usuario.
- las reglas pueden tardar en recachearse.
- Cloudflare, WAF, CDN o plugins pueden bloquear aunque robots.txt permita.

## Auditoria minima de robots.txt

Registrar:

- URL revisada: `https://dominio.com/robots.txt`
- fecha;
- status HTTP;
- reglas para `*`;
- reglas para Googlebot/Bingbot;
- reglas para bots AI declarados;
- sitemap declarado;
- conflictos con CDN/WAF si se conocen.

## Antes de recomendar cambios

1. Confirmar objetivo de negocio: permitir cita, bloquear entrenamiento, reducir carga, proteger contenido.
2. Confirmar bot y documentacion oficial.
3. Confirmar impacto posible en Google/Bing/AI search.
4. Preparar diff de robots.txt.
5. Pedir aprobacion si toca produccion.

## No hacer

- No copiar listas de bots antiguas sin verificar.
- No bloquear Googlebot por intentar bloquear AI.
- No asumir que permitir un bot garantiza citas.
- No tocar robots.txt por curiosidad.
