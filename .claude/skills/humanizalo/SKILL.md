---
name: humanizalo
description: >
  Revisa, reescribe y humaniza textos que suenan genericos, artificiales o
  demasiado producidos por IA. Usalo para hacer copy, emails, informes, posts,
  propuestas o textos de marca mas humanos, especificos, naturales y con voz
  real sin cambiar el mensaje central.
---

# Humanizalo - E-SELEC

## Proposito

Quitar patrones de escritura artificial y devolver un texto mas natural, especifico y con voz humana.

Esta skill no inventa datos ni cambia claims. Edita tono, ritmo, claridad, densidad y personalidad.

## Fuentes obligatorias

Lee el texto original, el contexto de agencia o cliente si aplica, `quality/criterios-output.md`, y si es copy comercial `.claude/skills/copy-editing/SKILL.md` o `.claude/skills/copywriting/SKILL.md`.

Necesitas audiencia, objetivo, canal, tono deseado y nivel de libertad para reescritura.

## Niveles

- HU3 - listo: texto reescrito, score, cambios y patrones corregidos.
- HU2 - fuerte: texto mejorado, faltan detalles de voz o contexto.
- HU1 - orientativo: mejora ligera con contexto parcial.
- HU0 - bloqueado: falta texto o no se puede cambiar el tono sin perder intencion.

## Workflow

1. Identificar objetivo, audiencia, canal y voz.
2. Escanear patrones artificiales usando `references/human-writing-patterns.md`.
3. Reescribir sin cambiar hechos, claims, CTA ni promesas.
4. Variar ritmo, reducir scaffolding, cortar relleno y hacer el texto mas concreto.
5. Puntuar en claridad, ritmo, confianza, autenticidad, densidad y voz.
6. Iterar hasta nivel aceptable o explicar limite.
7. Entregar usando `templates/humanization-review.md`.

## Reglas

- Mantener el mensaje central.
- No inventar datos, emociones, fuentes ni testimonios.
- No forzar humor o personalidad si no encaja con marca.
- No borrar tecnicismos necesarios para el publico.
- Respetar idioma del entregable.

## Bloqueos

- falta texto fuente;
- no hay permiso para cambiar tono o estructura;
- el texto requiere datos o claims que no existen;
- humanizar implicaria alterar sentido legal/comercial sensible.

## Referencias

- `references/human-writing-patterns.md`: patrones y correcciones.
- `templates/humanization-review.md`: formato de salida.
- `checklists/revision.md`: revision final.
