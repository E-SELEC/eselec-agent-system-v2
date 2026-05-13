---
name: ab-test-setup
description: >
  Disena, documenta y evalua A/B tests y experimentos para clientes de
  E-SELEC: split tests, hipotesis, variantes, sample size, baseline conversion,
  MDE, metricas primarias/secundarias/guardrail, duracion, trafico, QA,
  resultados, tests de pagina, copy, CTA, formularios, pricing o CRO. Usalo
  cuando se hable de A/B test, experimento, test de variantes, cual version es
  mejor, significancia, muestra, hipotesis o duracion de test.
---

# A/B Test Setup - E-SELEC

## Proposito

Disenar experimentos que produzcan aprendizaje confiable, no solo "probar por probar".

Esta skill no implementa tests reales. Prepara plan, requisitos, medicion y criterios de decision.

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
9. `.claude/skills/page-cro/SKILL.md` o skill origen de la hipotesis
10. `protocols/activos-criticos.md`

## Niveles

- AB3 - listo: hipotesis, baseline, muestra, duracion, metricas, QA y decision definidos.
- AB2 - plan fuerte: hipotesis y metricas listas, faltan muestra exacta o herramienta.
- AB1 - orientativo: idea de test sin datos suficientes.
- AB0 - bloqueado: falta hipotesis, conversion o medicion.

## Workflow

1. Definir observacion: dato, hallazgo CRO o problema.
2. Formular hipotesis: porque X, creemos Y causara Z para audiencia A.
3. Definir control y variante con un cambio principal.
4. Elegir metrica primaria, secundarias y guardrails.
5. Revisar baseline, trafico y sample size con `references/sample-size.md`.
6. Definir duracion minima y maximo razonable.
7. Definir QA, tracking y riesgos.
8. Preparar plan con `templates/plan-ab-test.md`.

## Reglas

- No testear sin metrica primaria.
- No testear si tracking no esta verificado.
- No parar antes de muestra/duracion por mirar resultados.
- No proponer MVT sin mucho trafico.
- Si no hay trafico suficiente, recomendar decision cualitativa o cambio directo.
- No implementar herramienta, snippet o experimento real sin Orden de Cambio.

## Bloqueos

- no hay hipotesis;
- no hay baseline o metrica;
- no hay trafico suficiente y se quiere significancia;
- el test cambia precio, checkout, Ads, tracking o web sin aprobacion;
- se quiere llamar ganador a un resultado inconcluso.

## Referencias

- `references/sample-size.md`: muestra y duracion.
- `templates/plan-ab-test.md`: formato de salida.
- `checklists/revision.md`: revision final.
