# Backlog de migracion

Este backlog ordena las acciones de migracion. Cada item debe cerrarse con registro en `registries/registro-migracion.md`.

## Estados

- `pendiente`
- `en curso`
- `bloqueado`
- `hecho`

## Prioridad P0 - Seguridad y base

Decision de prioridad: empezar por P0 antes de P1. Motivo: si no blindamos secretos, artefactos, activos criticos y cierre, cualquier migracion de calidad puede arrastrar errores estructurales o riesgos de produccion.

| ID | Estado | Accion | Resultado esperado |
|---|---|---|---|
| P0-001 | hecho | Crear inventario legacy inicial | `planning/inventario-legacy.md` |
| P0-002 | hecho | Auditar scripts con secretos historicos | `planning/auditoria-scripts-sensibles.md` |
| P0-003 | hecho | Migrar protocolo gestion-secretos | `protocols/gestion-accesos.md` |
| P0-004 | hecho | Migrar protocolo control-artefactos | `protocols/control-artefactos.md` |
| P0-005 | hecho | Migrar protocolo activos-criticos | `protocols/activos-criticos.md` |
| P0-006 | hecho | Migrar cierre-humano | `protocols/cierre-humano.md` |
| P0-007 | hecho | Disenar hook bloqueo secretos | `.claude/hooks/` |

## Prioridad P1 - Calidad y criterio

P1 empieza despues de completar los controles minimos P0. Motivo: la baja calidad de outputs se diagnosticara mejor cuando el sistema ya tenga fuentes, registros y permisos ordenados.

| ID | Estado | Accion | Resultado esperado |
|---|---|---|---|
| P1-001 | hecho | Crear matriz de causas de baja calidad | `quality/diagnostico-calidad.md` |
| P1-002 | hecho | Crear criterios de output por servicio | `quality/criterios-output.md` |
| P1-003 | hecho | Migrar skill `client-audit` | `.claude/skills/client-audit/` |
| P1-004 | hecho | Migrar skill `seo-audit` | `.claude/skills/seo-audit/` |
| P1-005 | hecho | Migrar Docente como rol de aprendizaje | `.claude/agents/docente.md` |
| P1-006 | hecho | Crear verificacion de medicion post-piloto | `.claude/skills/verificacion-medicion/` + `.claude/commands/verificar-medicion.md` |
| P1-007 | hecho | Crear ingesta segura de evidencia | `.claude/skills/ingesta-evidencia/` + `.claude/commands/ingestar-evidencia.md` |

## Prioridad P2 - Operacion

| ID | Estado | Accion | Resultado esperado |
|---|---|---|---|
| P2-001 | hecho | Crear Lider Clientes v2 | `.claude/agents/leader-clientes.md` |
| P2-002 | hecho | Crear Lider Agencia v2 | `.claude/agents/leader-agencia.md` |
| P2-003 | hecho | Convertir loop alertas pendientes en command | `.claude/commands/alertas-pendientes.md` |
| P2-004 | hecho | Convertir auditoria semanal en command | `.claude/commands/auditoria-semanal.md` |
| P2-005 | hecho | Definir cliente piloto | `planning/piloto-01.md` |

## Prioridad P3 - Migracion amplia

| ID | Estado | Accion | Resultado esperado |
|---|---|---|---|
| P3-001 | hecho | Migrar estructura de agencia | `agency/` v2 completo |
| P3-002 | hecho | Migrar cliente piloto | `clients/computer-chamberi/` |
| P3-003 | en curso | Migrar resto de skills por uso | `.claude/skills/` |
| P3-004 | pendiente | Migrar agentes especialistas | `.claude/agents/` |
| P3-005 | pendiente | Sanear y migrar conectores | `scripts/` y `.mcp.example.json` |

### Skills migradas dentro de P3-003

| Skill | Estado | Motivo |
|---|---|---|
| `analytics-tracking` | hecho | desbloquea GA4/GTM/eventos/conversiones para informes, CRO, Ads y SEO final |
| `site-architecture` | hecho | ordena paginas, URLs, navegacion, enlazado interno y redirecciones antes de cambios web/SEO |
| `schema-markup` | hecho | evita datos estructurados genericos o falsos y conecta SEO tecnico con arquitectura/breadcrumbs |
| `ai-seo` | hecho | formaliza visibilidad en respuestas AI con evidencia por query/plataforma y sin promesas falsas |
| `content-strategy` | hecho | convierte SEO/AI SEO/ventas en pilares, clusters, calendario y prioridades accionables |
| `copywriting` | hecho | convierte briefs y estrategias en copy claro, verificable y orientado a conversion |
| `copy-editing` | hecho | revisa textos existentes, claims, claridad, tono y CTA antes de entrega/publicacion |
| `page-cro` | hecho | diagnostica conversion de paginas completas: propuesta, CTA, confianza, friccion, mobile y medicion |
| `form-cro` | hecho | diagnostica friccion de formularios, campos, privacidad, mobile y medicion |
| `ab-test-setup` | hecho | convierte hipotesis CRO en experimentos medibles con muestra, metricas y guardrails |
| `signup-flow-cro` | hecho | optimiza registros, altas de cuenta y trials sin romper activacion posterior |
| `onboarding-cro` | hecho | mejora activacion, time-to-value y primer valor post-signup |
| `popup-cro` | hecho | optimiza popups, modales, overlays y banners sin danar UX/SEO movil |
| `paywall-upgrade-cro` | hecho | optimiza paywalls, upsells y upgrades con guardrails de revenue/confianza |
| `paid-ads` | hecho | planifica paid media con objetivo, tracking, presupuesto, estructura y riesgos |
| `ad-creative` | hecho | genera e itera anuncios con limites de plataforma, claims verificables y plan de test |
| `social-content` | hecho | crea piezas y calendarios sociales por canal, audiencia, tono y objetivo |
| `programmatic-seo` | hecho | planifica paginas SEO a escala con datos, template, arquitectura e indexacion |
| `competitor-alternatives` | hecho | estructura paginas de alternativas/comparativas con fuentes fechadas y honestidad |
| `cold-email` | hecho | escribe outreach frio con personalizacion real, prueba y CTA de baja friccion |
| `email-sequence` | hecho | disena secuencias lifecycle con trigger, cadencia, consentimiento y metricas |
| `lead-magnets` | hecho | planifica recursos de captacion con oferta, gating, entrega, nurture y medicion |
| `sales-enablement` | hecho | crea materiales comerciales por persona, etapa, objecion, prueba y CTA |
| `pricing-strategy` | hecho | analiza pricing, packaging y monetizacion con validacion y guardrails |
| `revops` | hecho | disena lifecycle, scoring, routing, pipeline, owners, SLAs y metricas |
| `churn-prevention` | hecho | planifica retencion, cancel flow, dunning, offers y guardrails |
| `referral-program` | hecho | planifica referidos/afiliados con incentivos, tracking, reglas y antifraude |
