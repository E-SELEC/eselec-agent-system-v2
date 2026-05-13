---
name: ad-creative
description: >
  Genera, revisa e itera creatividades de anuncios para clientes de E-SELEC:
  headlines, descriptions, primary text, RSA headlines, Google Ads copy, Meta
  ad copy, LinkedIn ad text, TikTok hooks, bulk ad variations, creative angles,
  creative testing, iteracion segun rendimiento y validacion de limites por
  plataforma. Usalo cuando se necesiten variaciones de anuncios, ad copy,
  hooks, headlines, descripciones o creatividad a escala. Para estrategia,
  presupuesto y targeting usar paid-ads.
---

# Ad Creative - E-SELEC

## Proposito

Crear o iterar anuncios que respeten plataforma, audiencia, oferta, claims verificables, limites de caracteres y plan de test.

Esta skill no sube anuncios a plataformas. Produce variaciones, matriz creativa, brief visual o recomendaciones de iteracion.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `agency/brand.md` o marca del cliente si existe
8. `quality/criterios-output.md`
9. `.claude/skills/paid-ads/SKILL.md`
10. `.claude/skills/copywriting/SKILL.md`
11. `.claude/skills/copy-editing/SKILL.md`
12. `.claude/skills/ab-test-setup/SKILL.md` si defines test creativo
13. `protocols/activos-criticos.md`

Necesitas plataforma, formato, audiencia, oferta y objetivo. Sin eso, no entregues set final.

## Niveles

- AC3 - listo: plataforma/formato, audiencia, oferta, limites, claims y plan de test validados.
- AC2 - fuerte: variaciones listas, faltan datos de performance o alguna restriccion.
- AC1 - orientativo: borradores con contexto parcial.
- AC0 - bloqueado: falta plataforma, formato, oferta, audiencia u objetivo.

## Workflow

1. Definir plataforma y formato: Google RSA, Meta feed, LinkedIn, TikTok, display, video.
2. Definir objetivo, audiencia, etapa de awareness y oferta.
3. Identificar angulos: dolor, resultado, prueba, comparacion, urgencia real, identidad.
4. Crear variaciones por angulo respetando `references/platform-specs.md`.
5. Revisar claims: no inventar cifras, premios, testimonios, precios ni garantias.
6. Revisar combinabilidad: en RSA cada headline debe funcionar sola.
7. Preparar output con `templates/ad-creative-set.md`.
8. Si hay datos de performance, separar winners, losers, aprendizajes y proximas variaciones.

## Reglas

- Validar longitud de cada pieza.
- No usar claims sin fuente.
- No crear anuncios que contradigan landing/oferta.
- No generar variaciones casi identicas para inflar volumen.
- No violar politicas sensibles de plataforma.
- No recomendar subir anuncios sin revision humana y Orden de Cambio.

## Bloqueos

- no hay plataforma/formato;
- no hay oferta o CTA;
- no se conoce audiencia;
- los claims requeridos no tienen fuente;
- el anuncio pertenece a sector sensible y no hay reglas/compliance suficientes.

## Referencias

- `references/platform-specs.md`: limites por plataforma.
- `templates/ad-creative-set.md`: formato de salida.
- `checklists/revision.md`: revision final.
