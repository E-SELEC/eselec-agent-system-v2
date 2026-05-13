# Inventario P3-005 - conectores y scripts

Fecha: 2026-05-13
Responsable: Codex + Arquitecto
Fase: P3-005

## Objetivo

Sanear la capa de scripts/conectores antes de traerla al sistema v2.

La regla de esta fase es simple: ningun script legacy entra por copia directa si maneja accesos, produce cambios reales, consume creditos, escribe `.env`, depende de sesiones locales o toca produccion.

## Fuentes revisadas

- `planning/auditoria-scripts-sensibles.md`
- `scripts/README.md`
- `protocols/gestion-accesos.md`
- `protocols/activos-criticos.md`
- `protocols/control-artefactos.md`
- `protocols/cierre-humano.md`

## Estado actual v2

- `scripts/` existe con solo `README.md`.
- No existe `.mcp.example.json`.
- `.gitignore` ya bloquea `.env`, credenciales, archivos de token y secretos.
- Existe `registries/registro-accesos.md`.
- Existe `registries/registro-artefactos.md`.

## Decisiones por grupo

| Grupo | Legacy | Decision P3-005 | Motivo |
|---|---|---|---|
| Guard de cierre | `scripts/protocol_guard.py` | migrar adaptado | Necesario para cerrar tareas v2 con revision local. |
| MCP local | `.mcp.json` no presente en legacy | crear `.mcp.example.json` | Documenta configuracion local sin valores reales. |
| WordPress/Woo hardcodeado | `deploy_bottega_plugin.py`, `woo_*.py` | bloquear/no migrar | Riesgo S4 y scripts de produccion con credenciales historicas. |
| Google OAuth | Drive, GA4, GBP | deferir | Requieren flujo OAuth seguro, token fuera del repo y prueba sin datos reales. |
| Meta Ads | `meta_ads_connector.py`, `refresh_meta_token.py` | deferir | Ads y renovacion manual no deben migrar sin gestion segura de accesos. |
| Hostinger/WP REST | `hostinger_connector.py`, `wp_connector.py` | deferir | Toca hosting, webs y produccion; requiere Orden de Cambio y dry-run. |
| Kling | `kling_connector.py` | deferir | Puede consumir creditos; necesita dry-run y limites explicitos. |
| Notion | `notion_connector.py` | no migrar por defecto | MCP debe ser preferente; script solo si hace falta sync local. |
| Scrapers publicos | `seo_scraper.py`, `web_scraper.py`, `security_crawler.py` | deferir | Utiles, pero requieren limites, user-agent y control de outputs. |
| Reporting/PDF | `report_generator.py`, `generar_informe_pdf.py` | deferir | Deben esperar a que informes v2 tengan contrato estable. |
| Modelo local | `model_router.py`, `ollama_connector.py` | no migrar ahora | Claude Code v2 usa rutas por agente/skill; Ollama puede documentarse aparte. |
| Capturas/raw exports | `.png`, `.txt` de sesiones | no migrar | Son outputs, no scripts fuente. |

## Piezas que se migran en P3-005

1. `scripts/protocol_guard.py` adaptado a rutas v2:
   - `registries/registro-artefactos.md`
   - `registries/registro-accesos.md`
   - `outputs/system/protocol-guard-latest.md`

2. `.mcp.example.json`:
   - solo estructura;
   - valores de ejemplo;
   - sin credenciales reales;
   - `.mcp.json` local ignorado por git.

3. `scripts/README.md` ampliado:
   - politica de entrada de scripts;
   - estados permitido/deferido/bloqueado;
   - comandos de validacion.

## Criterio de cierre P3-005

- Backlog P3-005 marcado como hecho.
- Scripts S4 legacy documentados como bloqueados o deferidos, no copiados.
- Existe guard v2 ejecutable sin secretos.
- Existe `.mcp.example.json` seguro.
- `.gitignore` protege `.mcp.json`.
- Registro de migracion y artefactos actualizado.
