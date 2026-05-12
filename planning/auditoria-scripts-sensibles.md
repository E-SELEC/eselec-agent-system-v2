# P0-002 - Auditoria de scripts sensibles

## Estado

- Fecha: 2026-05-12
- Sprint: P0 seguridad/protocolos
- Item: P0-002
- Alcance: `scripts/` del sistema legacy
- Estado: completado como auditoria inicial

## Objetivo

Detectar scripts legacy que no deben migrarse al sistema v2 sin saneamiento previo.

La auditoria busca:

- credenciales hardcodeadas;
- manejo de tokens/OAuth;
- escritura de `.env` o archivos de token;
- llamadas a servicios externos;
- riesgo de tocar produccion;
- existencia o ausencia de `dry-run`.

## Regla de seguridad

No se copian ni reproducen valores de secretos. Este documento solo registra rutas, nombres de variables sensibles y tipo de riesgo.

## Resultado ejecutivo

| Resultado | Cantidad | Interpretacion |
|---|---:|---|
| Scripts con credenciales hardcodeadas por nombre de variable | 4 | bloqueo inmediato |
| Scripts con OAuth/token/env o servicios externos criticos | 13 | no migrar hasta saneamiento |
| Scripts revisables antes de migrar | 6 | migrar solo con checklist |
| Scripts de bajo riesgo inicial | 2 | migrables con documentacion |

## Bloqueo inmediato

Estos scripts no deben migrarse ni ejecutarse desde v2 hasta retirar credenciales hardcodeadas, mover configuracion a `.env`/gestor externo y decidir si siguen vigentes.

| Script | Riesgo | Evidencia segura | Accion |
|---|---|---|---|
| `scripts/deploy_bottega_plugin.py` | S4 | variables sensibles: `WP_USER`, `WP_PASS`; llamadas WordPress/WooCommerce | bloquear, sanear o archivar |
| `scripts/woo_activacion_bottega.py` | S4 | variables sensibles: `WP_USER`, `WP_PASS`; llamadas GET/PATCH/POST/PUT | bloquear, sanear o archivar |
| `scripts/woo_debug.py` | S4 | variables sensibles: `WP_USER`, `WP_PASS`; llamadas GET/PUT | bloquear, sanear o archivar |
| `scripts/woo_paginas_legales.py` | S4 | variables sensibles: `WP_USER`, `WP_PASS`; llamadas POST/PUT | bloquear, sanear o archivar |

Decision: estos scripts quedan en legacy bloqueado. Si se necesitan, se reescriben desde cero con dry-run, variables de entorno y Orden de Cambio.

## Alto riesgo por accesos externos

Estos scripts no muestran necesariamente secretos hardcodeados, pero manejan accesos, OAuth, tokens, servicios externos o produccion. No deben migrarse sin revision.

| Script | Servicio | Riesgo | Motivo | Accion |
|---|---|---|---|---|
| `scripts/drive_connector.py` | Google Drive OAuth | S4 | token OAuth local, archivo de token, lectura Drive | reescribir usando ruta token fuera repo |
| `scripts/ga4_connector.py` | GA4 OAuth | S4 | token OAuth, credentials file, escritura token local | migrar tras `gestion-secretos` |
| `scripts/gbp_setup_computer_chamberi.py` | Google Business Profile OAuth | S4 | token OAuth, Authorization header, setup cliente | migrar solo si sigue vigente |
| `scripts/get_gbp_account_id.py` | Google Business Profile OAuth | S4 | crea token temporal y lo borra | reemplazar por flujo seguro o archivar |
| `scripts/hostinger_connector.py` | Hostinger API | S4 | usa token API por entorno y consulta hosting | migrar con dry-run y registro de acceso |
| `scripts/meta_ads_connector.py` | Meta Ads | S4 | usa token de acceso y consulta cuenta publicitaria | migrar tras protocolo Ads/accesos |
| `scripts/refresh_meta_token.py` | Meta Ads | S4 | recibe token manual y escribe `.env` | no migrar tal cual; reemplazar por gestor seguro |
| `scripts/wp_connector.py` | WordPress REST | S4 | carga `.env`, Authorization, acciones WP | migrar solo con dry-run y Orden de Cambio |
| `scripts/kling_connector.py` | Kling API | S3/S4 | genera JWT temporal, usa claves API y puede consumir creditos | conservar patron dry-run, revisar secretos |
| `scripts/notion_connector.py` | Notion API | S3 | usa API key desde config, crea/actualiza tareas | preferir MCP; mantener script solo para sync local |
| `scripts/semrush_login.py` | navegador/SEMrush | S3/S4 | perfil o sesion local; posible acceso autenticado | no migrar hasta definir politica SEMrush |
| `scripts/browser_config.py` | navegador local | S3 | rutas/perfil de navegador; no secreto directo | revisar antes de migrar |
| `scripts/security_crawler.py` | crawler defensivo WP/Woo | S3 | escanea superficie publica y patrones de secretos | migrar tras protocolo de activos criticos |

## Revisables antes de migrar

Estos scripts parecen utiles, pero deben entrar al v2 solo con checklist, limites y documentacion.

| Script | Uso | Riesgo | Accion |
|---|---|---|---|
| `scripts/seo_scraper.py` | auditoria SEO/scraping publico | S3 | migrar con limites, user-agent, outputs registrados |
| `scripts/web_scraper.py` | scraping publico/renderizado | S3 | migrar con limites y control de outputs |
| `scripts/report_generator.py` | informes | S2/S3 | migrar despues de criterios de calidad |
| `scripts/generar_informe_pdf.py` | PDF local | S2/S3 | migrar si se mantiene stack de PDF |
| `scripts/protocol_guard.py` | guard de cierre | S2/S3 | migrar temprano, ajustando rutas v2 |
| `scripts/kling_guide.md` | guia conector Kling | S2/S3 | convertir a docs/skill si se usa |

## Bajo riesgo inicial

| Script | Uso | Riesgo | Accion |
|---|---|---|---|
| `scripts/model_router.py` | routing de modelos | S1/S2 | revisar necesidad en v2 |
| `scripts/ollama_connector.py` | Ollama local | S2 | migrar solo si se mantiene Tier 0 local |

## Scripts no candidatos

No migrar al repo v2:

- capturas `.png`;
- raw exports `.txt`;
- outputs generados;
- archivos temporales;
- scripts ligados a una sesion puntual si no tienen uso futuro.

## Politica de migracion para scripts

Antes de mover un script a v2 debe cumplir:

1. Sin secretos hardcodeados.
2. Sin escritura de `.env` salvo herramienta aprobada.
3. Variables de entorno documentadas en `.env.example`.
4. `dry-run` por defecto si puede escribir, gastar dinero o tocar produccion.
5. Parametros no interactivos.
6. Logs sin secretos.
7. Output registrado en manifest o registry.
8. Orden de Cambio para WordPress, WooCommerce, Ads, GBP, Hostinger o produccion.
9. Prueba minima sin credenciales reales.

## Acciones recomendadas

### Accion inmediata

Marcar como bloqueados los cuatro scripts WordPress/WooCommerce con variables `WP_USER`/`WP_PASS`.

### Accion P0-003

Migrar `gestion-secretos` antes de tocar scripts.

### Accion P0-007

Crear hook de bloqueo de secretos que impida commits con:

- `WP_PASS =`
- `WP_USER =`
- `META_ACCESS_TOKEN =`
- `ck_...`
- `cs_...`
- `Bearer <valor>`
- `credentials.json`
- `token.json`

## Decisiones tomadas

1. Ningun script S4 se migra en bloque.
2. Los scripts WordPress/WooCommerce hardcodeados se bloquean.
3. Los conectores Google, Meta, Hostinger, WP y Kling requieren protocolo de secretos antes de migrar.
4. `notion_connector.py` se mantiene como candidato secundario porque MCP debe ser preferente.
5. `protocol_guard.py` se migrara, pero adaptado al v2, no copiado literal.
6. `seo_scraper.py` y `web_scraper.py` se consideran utiles, pero no antes de protocolos y control de artefactos.

## Siguiente accion

Ejecutar P0-003:

```text
Migrar protocolo gestion-secretos a protocols/gestion-secretos.md
```

Ese protocolo debe definir como se clasifican, registran, bloquean y rotan accesos antes de migrar cualquier script.
