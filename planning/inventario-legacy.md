# Inventario legacy inicial

## Estado

- Fecha: 2026-05-12
- Sprint: P0 seguridad/protocolos
- Item: P0-001
- Alcance: sistema legacy en `C:/Users/rondr/OneDrive/Desktop/E-SELEC - copia`
- Estado: inventario inicial, no auditoria exhaustiva final

## Proposito

Este inventario identifica las piezas del sistema antiguo E-SELEC y propone su destino correcto dentro del sistema v2 basado en Claude Code.

No migra contenido. No copia secretos. No decide implementaciones finales. Sirve para evitar que la migracion se haga por carpetas completas o por intuicion.

## Exclusiones de seguridad

No se deben inventariar copiando contenido sensible:

- `.env`
- tokens
- credentials
- application passwords
- claves API
- exports privados
- binarios pesados
- imagenes de auditorias
- PDFs/DOCX/XLSX finales
- carpetas `.git` embebidas en skills legacy

Cuando se detecta riesgo de secreto, se registra solo la ruta y el tipo de riesgo, nunca el valor.

## Resumen cuantitativo

| Area legacy | Archivos | Textuales | Bytes aprox. | Lectura inicial |
|---|---:|---:|---:|---|
| `.agents` | 144 | 141 | 1.184.367 | skills marketing legacy |
| `.archive` | 4 | 4 | 44.136 | historico |
| `.claude` | 1 | 1 | 3.111 | configuracion local legacy |
| `agency` | 18 | 18 | 120.232 | memoria interna E-SELEC |
| `agents` | 83 | 83 | 753.947 | prompts, lideres, entidades estructurales |
| `clients` | 114 | 87 | 5.047.795 | memoria y outputs de clientes |
| `kling-producer-workspace` | 16 | 16 | 57.162 | workspace herramienta video |
| `logs` | 1 | 0 | 8.569 | logs runtime |
| `outputs` | 10 | 3 | 2.741.417 | scrapes/capturas globales |
| `scripts` | 50 | 29 | 3.702.596 | conectores y automatizaciones |
| `sistema` | 13 | 13 | 143.539 | protocolos, registros e indices |

Extensiones textuales detectadas:

| Extension | Cantidad |
|---|---:|
| `.md` | 313 |
| `.json` | 54 |
| `.py` | 30 |
| `.txt` | 4 |

## Mapa global de destinos Claude Code

| Tipo de pieza legacy | Destino v2 probable | Motivo |
|---|---|---|
| Instrucciones globales raiz | `CLAUDE.md`, `AGENTS.md`, `.claude/rules/` | separar reglas siempre activas de reglas contextuales |
| Protocolos transversales | `protocols/` + `.claude/rules/` + hooks | parte humana como protocolo; parte automatizable como hook |
| Skills marketing | `.claude/skills/<skill>/SKILL.md` | procedimientos bajo demanda |
| Lideres/agentes especializados | `.claude/agents/*.md` | subagents nativos si necesitan contexto propio |
| Loops | `.claude/commands/` o scheduled tasks | acciones repetibles por nombre |
| Memoria cliente | `clients/[cliente]/` | nunca skill |
| Outputs cliente | Drive/outputs seleccionados + `manifest.md` | no migrar todo al repo |
| Scripts conectores | `scripts/` saneado + `.mcp.example.json` | separar herramienta, secreto y permiso |
| Registros globales | `registries/` | trazabilidad |
| Historico | `legacy/` o archivo externo | no contexto activo |

## Inventario raiz

| Ruta | Responsabilidad legacy | Destino v2 probable | Prioridad | Riesgo |
|---|---|---|---|---|
| `AGENTS.md` | instrucciones globales E-SELEC para agentes | extraer nucleo a `AGENTS.md`, reglas largas a `.claude/rules/`, protocolos a `protocols/` | P0/P1 | alto si se copia completo: contexto gigante y contradicciones |
| `CLAUDE.md` | instrucciones globales equivalentes para Claude | extraer solo imports y reglas siempre activas | P0/P1 | alto si mantiene manual monolitico |
| `README.md` | descripcion del sistema legacy | `legacy/` o referencia historica | P3 | bajo |
| `config.py` | carga configuracion y variables `.env` | `scripts/config.example.py` o modulo saneado futuro | P0/P9 | alto por gestion de secretos |
| `run.py` | entrada CLI legacy | commands/scripts saneados por caso | P2/P9 | medio-alto; puede disparar conectores |
| `instalar.py` | instalacion/setup legacy | revisar antes de migrar | P3 | medio |
| `.gitignore` | reglas ignore legacy | comparar con v2, conservar solo patrones utiles | P0 | bajo |

## `.claude` legacy

| Ruta | Responsabilidad legacy | Destino v2 probable | Prioridad | Riesgo |
|---|---|---|---|---|
| `.claude/settings.local.json` | permisos locales acumulados | no migrar directo; derivar politica compartida a `.claude/settings.json` | P0/P5 | medio; puede contener permisos demasiado amplios |

Decision inicial: no copiar configuracion local. Solo extraer reglas compartibles, revisadas y seguras.

## `sistema/`

Responsabilidad: gobierno transversal del sistema legacy.

| Pieza | Destino v2 | Prioridad | Decision inicial |
|---|---|---|---|
| `sistema/protocolos/gestion-secretos.md` | `protocols/gestion-secretos.md` + rule/hook | P0-003 | migrar primero |
| `sistema/protocolos/control-artefactos.md` | `protocols/control-artefactos.md` + registro/hook | P0-004 | migrar primero |
| `sistema/protocolos/activos-criticos.md` | `protocols/activos-criticos.md` + rule/hook | P0-005 | migrar primero |
| `sistema/protocolos/cierre-humano.md` | `protocols/cierre-humano.md` + cierre de agente | P0-006 | migrar primero |
| `sistema/protocolos/el-escolta.md` | `protocols/el-escolta.md` + hook de cierre | P0/P5 | migrar despues de base |
| `sistema/protocolos/el-fenix.md` | subagent/rule/protocol | P2/P12 | migrar tras protocolos base |
| `sistema/protocolos/el-arquitecto.md` | subagent/rule/protocol | P2/P12 | fusionar con rol actual si procede |
| `sistema/protocolos/el-docente.md` | subagent/rule/protocol | P1/P12 | clave para calidad |
| `sistema/protocolos/semrush-acceso.md` | protocolo o script docs, revisar sensibilidad | P0/P9 | no migrar sin auditoria de accesos |
| `sistema/registros/registro-accesos.md` | `registries/registro-accesos.md` | P0 | resumir estado, no copiar secretos |
| `sistema/registros/registro-artefactos.md` | `registries/registro-artefactos.md` | P0 | mantener trazabilidad legacy |
| `sistema/indices/mapa-sistema.md` | `planning/mapa-responsabilidades.md` o rule | P1 | usar como base |
| `sistema/indices/herramientas-vivas.md` | `planning/herramientas-vivas.md` | P9 | revisar contra conectores actuales |

Decision inicial: `sistema/protocolos/` es la fuente canonica de protocolos. `agency/protocolos/` no debe prevalecer si contradice.

## `agents/`

Responsabilidad: prompts, lideres, especialistas y entidades estructurales legacy.

| Area | Rutas principales | Destino v2 probable | Prioridad | Decision inicial |
|---|---|---|---|---|
| Lider Clientes | `agents/leader-clients.md` | `.claude/agents/leader-clientes.md` | P2 | reescribir, no copiar literal |
| Agencia | `agents/agency/*` | `.claude/agents/leader-agencia.md` + subagents selectivos | P2/P11 | fusionar y reducir |
| Arquitecto | `agents/arquitecto/arquitecto.md` | ya existe `arquitecto-migracion-claude`; posible `arquitecto.md` futuro | P12 | fusionar cuidadosamente |
| Calibracion | `agents/calibracion/calibracion.md` | `protocols/correccion-calidad.md` + Docente | P1/P13 | migrar por funcion, no como agente aislado todavia |
| CRO | `agents/cro/*` | subagents o skills CRO | P3 | despues de seguridad/calidad |
| Docente | `agents/docente/*` | `.claude/agents/docente.md`, `quality/`, `registries/registro-aprendizajes.md` | P1/P12 | clave para mejorar calidad |
| Fenix | `agents/fenix/fenix.md` | `.claude/agents/fenix.md` + protocol | P2/P12 | migrar tras protocolos |
| Loops | `agents/loops/leader-loops.md` | `.claude/commands/` o scheduled tasks | P2/P8 | convertir por loop |
| Reports | `agents/reports/*` | subagent Reports + skill reporting | P1/P2 | relevante para calidad informes |
| SEM | `agents/sem/*` | subagents/skills Ads | P3 | no antes de P0/P1 |
| SEO | `agents/seo/*` | leader SEO, skills SEO, quality evals, references | P1/P7 | prioridad de calidad |
| Social | `agents/social/*` | subagents/skills content | P3 | despues |
| Web | `agents/web/*` | subagents/skills web, protocolos activos criticos | P2/P3 | sensible si toca produccion |

### Observacion SEO

SEO tiene alta densidad de conocimiento:

- `agents/seo/leader-seo.md`
- `agents/seo/seo-organico.md`
- `agents/seo/seo-tecnico.md`
- `agents/seo/seo-local.md`
- `agents/seo/seo-llms.md`
- `agents/seo/seo-web.md`
- `agents/seo/semrush-workflows.md`
- `agents/seo/referencias/seo-onpage-semrush.md`
- `agents/docente/seo/aprendizajes/*`
- `agents/docente/seo/fuentes/*`

Decision inicial: no migrar SEO como bloque. Primero crear canon/calidad:

1. separar procedimientos en skills;
2. separar criterio docente en `quality/` o `registries/registro-aprendizajes.md`;
3. crear subagent SEO solo despues de resolver canibalizacion;
4. usar P1 para atacar calidad de outputs SEO/informes.

## `.agents/skills/`

Responsabilidad: skills legacy de marketing y operaciones.

Skills detectadas:

| Skill legacy | Destino v2 probable | Prioridad inicial |
|---|---|---|
| `client-audit` | `.claude/skills/client-audit/SKILL.md` | P1 |
| `seo-audit` | `.claude/skills/seo-audit/SKILL.md` | P1 |
| `folder-cleanup` | `.claude/skills/folder-cleanup/SKILL.md` | P1/P2 |
| `analytics-tracking` | `.claude/skills/analytics-tracking/SKILL.md` | P1/P9 |
| `site-architecture` | `.claude/skills/site-architecture/SKILL.md` | P1/P2 |
| `schema-markup` | `.claude/skills/schema-markup/SKILL.md` | P1/P2 |
| `copywriting` | `.claude/skills/copywriting/SKILL.md` | P2 |
| `copy-editing` | `.claude/skills/copy-editing/SKILL.md` | P2 |
| `humanizalo` | revisar y migrar sin `.git` embebido | P1/P2 |
| `woocommerce-setup` | migrar solo tras protocolos de activos criticos | P2/P9 |
| `paid-ads`, `ad-creative` | Ads/SEM posterior | P3 |
| restantes marketing | migracion por uso real | P3 |

Riesgos detectados:

- Algunas skills contienen `evals/`, lo cual es positivo para calidad y debe conservarse si es util.
- Algunas skills tienen `references/`, deben mantenerse como archivos de apoyo, no meter todo en `SKILL.md`.
- `humanizalo` y `prompt-master` contienen carpetas `.git` internas: no migrar esas carpetas.

Decision inicial: migrar skills por prioridad y con `migration-audit`, nunca copiar toda `.agents/skills/`.

## `agency/`

Responsabilidad: memoria interna E-SELEC, preferencias, outputs de captacion y observaciones de Arquitecto.

| Ruta | Destino v2 probable | Prioridad | Decision inicial |
|---|---|---|---|
| `agency/context.md` | `agency/context.md` v2 | P11 | migrar resumen vigente |
| `agency/brand.md` | `agency/brand.md` v2 | P11 | migrar tras revisar actualidad |
| `agency/preferencias-rodrigo.md` | rule/memory de agencia, segun sensibilidad | P1/P11 | clave para calidad |
| `agency/log.md` | legacy acta; v2 empieza registro propio | P0/P11 | no copiar entero como contexto |
| `agency/mensajes.md` | `agency/mensajes.md` v2 | P11 | migrar pendientes vigentes |
| `agency/history.md` | `legacy/` o registro aprendizajes | P12 | resumir |
| `agency/loops-activos.md` | commands/scheduled tasks | P8 | convertir por loop |
| `agency/arquitecto/*` | Arquitecto/Fenix/planificacion | P12 | fusionar |
| `agency/outputs/*` | outputs historicos; no subir todo | P3/P11 | seleccionar si aporta |
| `agency/protocolos/activos-criticos.md` | no canonico si contradice `sistema/protocolos` | P0 | comparar y archivar/fusionar |

Decision inicial: migrar primero preferencias de Rodrigo cuando abramos P1 calidad, porque pueden explicar parte de la brecha entre "output correcto" y "output deseado".

## `clients/`

Responsabilidad: memoria, tareas, mensajes, logs y outputs por cliente.

Clientes detectados:

| Cliente/carpeta | Estado inicial | Destino v2 | Prioridad |
|---|---|---|---|
| `.template` | plantilla legacy | comparar con `clients/_template/` v2 | P10 |
| `cashier-bubble-tea` | activo | migrar como cliente activo | P10/P15 |
| `computer-chamberi` | activo, buen candidato SEO | posible cliente piloto | P10/P14 |
| `la-bottega-del-gusto` | activo, alto riesgo web/WooCommerce | migrar con cautela tras P0 | P10/P14 |
| `stramondo-venezuela` | activo, Meta Ads/social | migrar tras conectores/ads | P10/P15 |
| `shogun-motors` | baja voluntaria 2026-04-17 | legacy/no activo | P15 |

Estructura valiosa por cliente:

- `context.md`
- `memory.md`
- `log.md`
- `mensajes.md`
- `tasks.md`
- `outputs/manifest.md`

Riesgos:

- `outputs/` contiene PDFs, DOCX, imagenes, HTML, JSON, ZIP y artefactos de desarrollo.
- No se deben subir outputs completos al repo v2 sin filtro.
- `tasks.md` es snapshot; Notion sigue siendo fuente principal cuando este disponible.

Decision inicial: cliente piloto recomendado para P14: `computer-chamberi`, porque permite probar calidad SEO sin tocar produccion de ecommerce ni Ads.

## `scripts/`

Responsabilidad: conectores, automatizaciones, scrapers, generadores y guard.

### Clasificacion inicial

| Grupo | Scripts | Destino v2 | Riesgo |
|---|---|---|---|
| Guard/protocolos | `protocol_guard.py`, `security_crawler.py` | migrar temprano tras auditoria | medio |
| Routing/modelos | `model_router.py`, `ollama_connector.py` | revisar si sigue siendo necesario | bajo-medio |
| Informes | `report_generator.py`, `generar_informe_pdf.py` | migrar tras P1/P13 | medio |
| Scraping web/SEO | `seo_scraper.py`, `web_scraper.py` | migrar con tests y limites | medio |
| Google/Drive/GA4/GBP | `drive_connector.py`, `ga4_connector.py`, `get_gbp_account_id.py`, `gbp_setup_computer_chamberi.py` | scripts saneados o MCP | alto |
| Notion | `notion_connector.py` | preferir MCP si disponible; script si escribe local | medio |
| Meta Ads | `meta_ads_connector.py`, `refresh_meta_token.py` | migrar tras P0/P9 | alto |
| WordPress/WooCommerce | `wp_connector.py`, `deploy_bottega_plugin.py`, `woo_activacion_bottega.py`, `woo_debug.py`, `woo_paginas_legales.py` | bloqueados hasta saneamiento | alto |
| Hostinger | `hostinger_connector.py` | bloqueado hasta P0/P9 | alto |
| Kling | `kling_connector.py`, `kling_guide.md` | migrar con dry-run y secretos externos | medio-alto |
| SEMrush/manual | `semrush_login.py`, capturas/raw txt/png | no migrar capturas; revisar procedimiento | medio |

### Scripts con patrones sensibles

Se detectaron referencias a tokens, secretos, passwords, Authorization, claves o credenciales en varios scripts. Esto no significa que todos contengan secretos reales, pero todos requieren P0-002 antes de migrar:

- `scripts/deploy_bottega_plugin.py`
- `scripts/drive_connector.py`
- `scripts/ga4_connector.py`
- `scripts/gbp_setup_computer_chamberi.py`
- `scripts/get_gbp_account_id.py`
- `scripts/hostinger_connector.py`
- `scripts/kling_connector.py`
- `scripts/kling_guide.md`
- `scripts/meta_ads_connector.py`
- `scripts/model_router.py`
- `scripts/ollama_connector.py`
- `scripts/protocol_guard.py`
- `scripts/refresh_meta_token.py`
- `scripts/report_generator.py`
- `scripts/security_crawler.py`
- `scripts/semrush_login.py`
- `scripts/woo_activacion_bottega.py`
- `scripts/woo_debug.py`
- `scripts/woo_paginas_legales.py`
- `scripts/wp_connector.py`

Decision inicial: P0-002 debe auditar scripts con salida de metadatos, no valores.

## `outputs/`

Responsabilidad: scrapes/capturas globales.

Decision inicial:

- No migrar al repo v2.
- Si un output es necesario para aprendizaje, convertirlo en resumen markdown sin datos sensibles.
- Las capturas y exports pesados deben vivir en Drive o permanecer legacy.

## `.archive/`

Responsabilidad: historico comprimido o documentos antiguos.

Decision inicial:

- No migrar al contexto activo.
- Solo revisar si una decision actual depende de este historico.
- Posible destino: `legacy/`.

## `kling-producer-workspace/`

Responsabilidad: workspace operativo/video AI.

Decision inicial:

- No migrar en P0.
- Revisar en P9 junto a `kling_connector.py`.
- Mantener fuera de contexto global.

## Riesgos principales detectados

| Riesgo | Evidencia | Mitigacion |
|---|---|---|
| Secretos historicos en scripts | patrones sensibles en scripts WordPress/WooCommerce y conectores | P0-002 antes de migrar scripts |
| Contexto global excesivo | `AGENTS.md` y `CLAUDE.md` legacy son largos | Fase 3, dividir en rules/skills/protocols |
| Duplicidad de protocolos | `sistema/protocolos/` y `agency/protocolos/` | elegir canon `sistema/protocolos/` |
| Skills con carpetas `.git` internas | `humanizalo`, `prompt-master` | migrar sin `.git` |
| Outputs pesados/sensibles | clientes y outputs globales contienen PDFs, imagenes, JSON, ZIP | no migrar en bloque |
| Calidad inconsistente | SEO/Docente/skills/prompts solapados | P1 calidad y matriz de causas |
| Produccion sensible | WordPress, WooCommerce, Ads, Hostinger | Orden de Cambio + dry-run |

## Prioridad de migracion inicial

### P0 - Seguridad/protocolos

1. Auditar scripts sensibles.
2. Migrar `gestion-secretos`.
3. Migrar `control-artefactos`.
4. Migrar `activos-criticos`.
5. Migrar `cierre-humano`.
6. Disenar hook bloqueo secretos.

### P1 - Calidad/criterio

1. Migrar preferencias de Rodrigo a lugar correcto.
2. Crear matriz de causas de baja calidad.
3. Migrar `client-audit`.
4. Migrar `seo-audit`.
5. Ordenar Docente SEO y criterios de output.

### P2 - Operacion

1. Lider Clientes.
2. Lider Agencia.
3. Commands de loops basicos.
4. Fenix/Arquitecto/Docente estructurales.

## Decisiones tomadas en este inventario

1. No copiar carpetas completas.
2. No migrar outputs completos.
3. No migrar scripts antes de P0-002.
4. Usar `sistema/protocolos/` como fuente canonica inicial.
5. Tratar `agency/protocolos/activos-criticos.md` como duplicado a comparar, no como canon.
6. Tratar `computer-chamberi` como candidato natural para piloto SEO.
7. Tratar `la-bottega-del-gusto` como cliente de alto riesgo operativo por WordPress/WooCommerce.
8. Tratar `shogun-motors` como legacy/no activo.

## Siguiente accion

Ejecutar P0-002:

```text
Auditar scripts con secretos historicos sin imprimir valores.
```

Salida esperada:

- lista de scripts bloqueados;
- tipo de acceso/riesgo;
- recomendacion: migrar a `.env`, reescribir, archivar o mantener bloqueado;
- actualizacion de `registries/registro-accesos.md`;
- actualizacion de `planning/backlog-migracion.md`.
