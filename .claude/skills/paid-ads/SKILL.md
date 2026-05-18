---
name: paid-ads
description: >
  Planifica, audita y optimiza campanas de paid media para clientes de E-SELEC:
  Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, PPC, SEM, paid social,
  retargeting, ROAS, CPA, CPC, CPM, presupuesto, audiencias, bidding,
  estructura de campana, conversion tracking, landing pages y optimizacion de
  inversion publicitaria. Usalo cuando se hable de campanas de Ads, paid media,
  Google Ads, Facebook/Instagram Ads, LinkedIn Ads, presupuesto publicitario,
  ROAS/CPA o si conviene correr anuncios. Para crear textos/variaciones de ads,
  usar ad-creative.
---

# Paid Ads - E-SELEC

## Proposito

Tomar decisiones de campanas pagadas con objetivo, tracking, presupuesto, audiencia, estructura y riesgos claros antes de gastar dinero.

Esta skill no crea, edita, pausa ni lanza campanas reales. Produce auditoria, estrategia, estructura o plan de optimizacion.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`
8. `.claude/skills/analytics-tracking/SKILL.md`
9. `.claude/skills/page-cro/SKILL.md` para landing/post-click
10. `.claude/skills/ad-creative/SKILL.md` si hacen falta anuncios
11. `.claude/skills/copywriting/SKILL.md` si falta propuesta/copy
12. `.claude/skills/ab-test-setup/SKILL.md` si propones experimento
13. `protocols/activos-criticos.md`
14. `protocols/gestion-accesos.md` si se usan cuentas, tokens, pixels o APIs

Necesitas objetivo, conversion, presupuesto y estado de tracking. Sin eso no hay plan final.

## Niveles

- PA3 - listo: objetivo, presupuesto, tracking, landing, audiencia, estructura, medicion y riesgos verificados.
- PA2 - plan fuerte: objetivo y estructura claros; faltan datos de cuenta o medicion parcial.
- PA1 - orientativo: hay idea de campana, pero faltan presupuesto, tracking o conversion.
- PA0 - bloqueado: falta objetivo, conversion, presupuesto o landing.

## Workflow

1. Definir objetivo: awareness, trafico, leads, ventas, app, retargeting.
2. Definir conversion primaria, valor y metrica: CPA, ROAS, leads, revenue.
3. Verificar tracking: pixel, GA4, conversiones, UTMs, consentimiento.
4. Elegir plataforma segun intencion, audiencia, formato, presupuesto y datos.
5. Revisar landing/post-click con `page-cro` si aplica.
6. Disenar estructura: campanas, ad sets/grupos, audiencias, exclusions, presupuesto.
7. Definir creatividades necesarias y pasar a `ad-creative` si corresponde.
8. Definir plan de aprendizaje, optimizacion y reporte.
9. Preparar output con `templates/plan-paid-ads.md`.

## Reglas

- No recomendar conversion campaigns sin tracking verificado.
- No gastar presupuesto real sin Orden de Cambio.
- No optimizar solo por metrica de plataforma; contrastar con GA4/CRM si existe.
- No escalar durante aprendizaje sin datos suficientes.
- Siempre incluir exclusiones: clientes actuales, convertidos recientes y audiencias irrelevantes.
- Distinguir problema de anuncio, audiencia, landing, oferta y tracking.
- No prometer ROAS/CPA futuro.

## Bloqueos

- no hay objetivo ni conversion definida;
- no hay presupuesto;
- no hay landing u oferta;
- tracking no existe o no se puede verificar para campanas de conversion;
- se piden cambios reales en Ads, pixels, presupuesto o billing sin aprobacion.

## Referencias

- `references/platform-guide.md`: seleccion de plataforma, estructura y metricas.
- `references/platform-rules.md`: bloqueadores, validacion de eventos y reglas por plataforma.
- `templates/plan-paid-ads.md`: formato de salida.
- `checklists/revision.md`: revision final.
