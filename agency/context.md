# Contexto Agencia - E-SELEC

## Estado

- Fecha de migracion v2: 2026-05-12
- Ultima actualizacion operativa: 2026-05-19
- Fuente legacy: `agency/context.md`, `AGENTS.md`, logs de migracion
- Responsable: Rodrigo
- Slogan: Data-driven solutions
- Tipo: agencia de marketing digital
- Mercado principal: Espana, con clientes internacionales cuando el negocio lo requiere
- Nivel de datos: parcial
- Fase actual: operacion v2 iniciada

## Identidad

E-SELEC ayuda a empresas a popularizarse digitalmente en distintos canales: SEO, SEO local, web, analitica, paid media, redes, CRO y AI Search.

El criterio operativo es data-driven: toda recomendacion importante debe basarse en datos, evidencia saneada o una limitacion declarada.

## Estado operativo v2

La migracion base del sistema v2 esta cerrada. Ya existen protocolos, lideres, agentes especialistas, skills, commands, guard de cierre y sprint operativo inicial.

La prioridad actual ya no es migrar piezas base, sino probar el sistema en uso real con bajo riesgo:

1. Operar con los 4 clientes activos ya migrados de forma minima a v2.
2. Mantener los loops en modo lectura hasta comprobar contexto, logs y mensajes de cada cliente.
3. Validar calibracion antes de guardar aprendizajes permanentes.
4. Elegir un solo conector seguro para especificar antes de tocar APIs o produccion.
5. No incluir clientes inactivos en loops, informes ni tareas salvo reactivacion explicita.

## Clientes y estado operativo

| Cliente | Carpeta | Sector | Servicios principales | Estado |
|---|---|---|---|---|
| Chashier Bubble Tea | `cashier-bubble-tea` | hosteleria | SEO, RRSS, Web | activo v2; migracion minima 2026-05-18 |
| La Bottega del Gusto | `la-bottega-del-gusto` | retail alimentacion | SEO local, Web | activo v2; migracion minima 2026-05-18 |
| Stramondo Venezuela | `stramondo-venezuela` | distribucion B2B | Meta Ads, RRSS | activo v2; migracion minima 2026-05-18 |
| Computer Chamberi | `computer-chamberi` | servicios tecnicos | SEO organico, SEO local, Web | activo v2; cliente piloto inicial |
| Shogun Motors | `shogun-motors` | automocion/taller | SEO, Web, Local | baja voluntaria 2026-04-17; solo historico |

## Areas internas

| Area | Objetivo | Estado v2 |
|---|---|---|
| Captacion | conseguir oportunidades nuevas | subagent v2 migrado; pendiente primer uso real |
| Reputacion | mejorar presencia propia de E-SELEC | subagent v2 migrado; pendiente primer uso real |
| Onboarding | ordenar altas de cliente y fuentes de verdad | subagent v2 migrado; pendiente primer uso real |
| Retencion | reducir churn y detectar riesgos | subagent v2 migrado; pendiente primer uso real |
| Finanzas | pricing, margenes y operaciones | subagent v2 migrado; pendiente primer uso real |
| Arquitectura | mejorar sistema de agentes | activo post-migracion; observa sprint operativo |

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
- No usar prioridades antiguas de migracion como si fueran tareas pendientes: backlog base ya esta cerrado.

## Prioridad interna actual

1. Completar Sprint 01 de operacion v2.
2. Ejecutar O1-003 `LOOP: auditoria-semanal` en modo lectura, sin cambios reales.
3. Probar O1-004 Calibracion con una correccion real o simulada.
4. Elegir O1-005 primer conector seguro para especificacion, no implementacion productiva.
5. Revisar cada cliente activo ya migrado antes de ejecutar loops o informes reales.
