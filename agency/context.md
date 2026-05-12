# Contexto Agencia - E-SELEC

## Estado

- Fecha de migracion v2: 2026-05-12
- Fuente legacy: `agency/context.md`, `AGENTS.md`, logs de migracion
- Responsable: Rodrigo
- Slogan: Data-driven solutions
- Tipo: agencia de marketing digital
- Mercado principal: Espana, con clientes internacionales cuando el negocio lo requiere
- Nivel de datos: parcial

## Identidad

E-SELEC ayuda a empresas a popularizarse digitalmente en distintos canales: SEO, SEO local, web, analitica, paid media, redes, CRO y AI Search.

El criterio operativo es data-driven: toda recomendacion importante debe basarse en datos, evidencia saneada o una limitacion declarada.

## Clientes activos v2

| Cliente | Carpeta | Sector | Servicios principales | Estado |
|---|---|---|---|---|
| Chashier Bubble Tea | `cashier-bubble-tea` | hosteleria | SEO, RRSS, Web | activo legacy, pendiente migrar v2 |
| La Bottega del Gusto | `la-bottega-del-gusto` | retail alimentacion | SEO local, Web | activo legacy, pendiente migrar v2 |
| Stramondo Venezuela | `stramondo-venezuela` | distribucion B2B | Meta Ads, RRSS | activo legacy, pendiente migrar v2 |
| Computer Chamberi | `computer-chamberi` | servicios tecnicos | SEO organico, SEO local, Web | cliente piloto v2 |
| Shogun Motors | `shogun-motors` | automocion/taller | SEO, Web, Local | baja voluntaria 2026-04-17; solo historico |

## Areas internas

| Area | Objetivo | Estado v2 |
|---|---|---|
| Captacion | conseguir oportunidades nuevas | pendiente migrar |
| Reputacion | mejorar presencia propia de E-SELEC | pendiente migrar |
| Onboarding | ordenar altas de cliente y fuentes de verdad | pendiente migrar |
| Retencion | reducir churn y detectar riesgos | pendiente migrar |
| Finanzas | pricing, margenes y operaciones | pendiente migrar |
| Arquitectura | mejorar sistema de agentes | activo en migracion v2 |

## Herramientas

| Herramienta | Uso | Estado v2 |
|---|---|---|
| GitHub | versionar sistema v2 | activo |
| Claude/Codex | ejecucion y arquitectura del sistema | activo |
| Notion | tareas y CRM | pendiente reconectar/documentar v2 |
| Google Drive | almacenamiento de cliente | pendiente reconectar/documentar v2 |
| GSC | SEO real | pendiente ingesta/conector seguro |
| GA4 | analitica y conversiones | pendiente verificacion segura |
| GBP | SEO local | pendiente verificacion segura |
| SEMrush | SEO competitivo y visibilidad estimada | pendiente ingesta/conector seguro |
| Meta Ads | campanas Stramondo | pendiente sanear conector |
| WordPress/WooCommerce | webs clientes | requiere Orden de Cambio antes de produccion |

## Riesgos actuales

- Conectores legacy pueden contener credenciales, sesiones o rutas sensibles.
- No migrar scripts legacy completos sin auditoria.
- No usar datos de cliente como fuente viva sin `ingesta-evidencia` y `verificacion-medicion`.
- No tocar produccion sin `protocols/activos-criticos.md`.

## Prioridad interna actual

1. Terminar piloto Computer Chamberi con datos GSC/SEMrush saneados o vivos.
2. Migrar skills restantes por prioridad real.
3. Migrar agentes especialistas como subagents ligeros.
4. Sanear conectores.
5. Convertir loops pendientes en commands o automations solo cuando ya funcionen manualmente.
