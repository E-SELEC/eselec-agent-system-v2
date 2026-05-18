# Auditoria SEM / Paid Ads - 2026-05-18

## Objetivo

Revisar si el area SEM necesita un canon nuevo o si basta con reforzar la skill `paid-ads` para evitar errores de medicion, plataforma y riesgo operativo.

## Evidencia leida

- Agentes v2: `sem-leader`, `sem-google`, `sem-meta`, `sem-linkedin`, `sem-tiktok`, `sem-analitica`.
- Skill v2: `.claude/skills/paid-ads/SKILL.md`.
- Referencias v2: `platform-guide.md`, `revision.md`.
- Legacy: `../agents/sem/leader-sem.md`, `sem-google.md`, `sem-meta.md`, `sem-linkedin.md`, `sem-tiktok.md`, `sem-analitica.md`.
- Consulta Claude: realizada con agente `alineacion`, modo `plan`, sin edicion de archivos.

## Diagnostico

SEM v2 ya tiene una estructura correcta:

- `sem-leader` separa la capa del problema: objetivo, tracking, oferta, audiencia, presupuesto, creatividad, landing o cuenta.
- `paid-ads` exige objetivo, conversion, presupuesto, tracking, landing, medicion y riesgos.
- Los bloqueos de produccion ya existen: no lanzar, pausar, escalar presupuesto ni tocar conversiones/pixels sin Orden de Cambio.

El punto debil estaba en las referencias bajo demanda:

- `platform-guide.md` era demasiado breve para decisiones de alto riesgo.
- Faltaban bloqueadores por plataforma.
- Faltaba una regla general para no confundir metricas de plataforma con resultados reales de negocio.

## Decision

No crear un canon SEM por ahora.

Motivo: SEO necesitaba canon porque tenia criterio historico transversal que debia gobernar cualquier tarea SEO profunda. SEM ya tiene una skill procedimental fuerte. El problema no era falta de canon, sino falta de reglas practicas bajo demanda dentro de `paid-ads`.

## Ajustes aplicados

- Ampliado `.claude/skills/paid-ads/references/platform-guide.md` con bloqueadores por plataforma.
- Creado `.claude/skills/paid-ads/references/platform-rules.md` con reglas de validacion de eventos, metricas y plataformas.
- Enlazado `platform-rules.md` desde `.claude/skills/paid-ads/SKILL.md`.

## Contaminacion evitada

No se copio ningun dato, nombre, cuenta, campana ni caso real de cliente dentro de la skill general.

La leccion operativa se dejo como principio abstracto: clics, eventos de mensajeria o senales de plataforma no equivalen a leads, respuestas o ventas sin validacion externa.

## Estado

Completado. Pendiente solo validacion final con `protocol_guard.py`.
