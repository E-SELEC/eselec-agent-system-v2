---
name: copy-editing
description: >
  Revisa, edita y mejora copy existente para clientes de E-SELEC sin cambiar
  el mensaje central: proofreading, polish, copy feedback, mejorar texto,
  tighten copy, limpiar texto, revisar claims, claridad, tono, CTA, beneficios,
  prueba, especificidad, lenguaje generico, texto demasiado largo, copy debil,
  hero, landing, pagina de servicio, email corto, anuncio base o entregable
  comercial. Usalo cuando ya exista texto y haga falta pulirlo, no escribirlo
  desde cero.
---

# Copy Editing - E-SELEC

## Proposito

Mejorar un texto existente sin traicionar su objetivo, audiencia ni mensaje central.

Esta skill no sustituye a `copywriting`. Si no existe texto base, usa `copywriting`. Si el problema es estrategia de pagina, usa `page-cro` o `content-strategy`.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`, contrato Copy editing si existe
8. `agency/brand.md` si el texto representa a E-SELEC
9. `agency/preferencias-rodrigo.md` si existe en v2
10. `.claude/skills/copywriting/SKILL.md` si vas a comparar contra el brief de copy
11. `.claude/skills/humanizalo/SKILL.md` solo si existe y Rodrigo pide humanizar de forma explicita

No agregues claims nuevos, cifras, promesas, testimonios, precios o garantias. Solo puedes mantenerlos si ya existen y estan permitidos por las fuentes.

## Principios

1. Preservar intencion antes de embellecer.
2. Claridad antes que estilo.
3. Cada edicion debe tener motivo.
4. Reducir ruido, no quitar sustancia.
5. Suavizar claims no probados.
6. Mejorar CTA sin cambiar la oferta.
7. Mantener tono de marca y canal.

## Niveles de edicion

- CE3 - listo: texto revisado, claims comprobados, CTA claro, tono consistente y cambios explicados.
- CE2 - revisado con pendientes: texto mejorado, pero faltan pruebas o aprobacion de algun claim.
- CE1 - feedback: se detectan problemas y direccion, pero falta contexto para editar con seguridad.
- CE0 - bloqueado: falta texto base, objetivo, audiencia o hay claims sensibles sin fuente.

Regla:

- CE0 no produce version final.
- CE1 puede dar diagnostico.
- CE2 puede pasar a revision.
- CE3 puede entregarse o implementarse con aprobacion si toca produccion.

## Workflow

### 1. Identificar alcance

Define:

- tipo de texto;
- canal;
- audiencia;
- objetivo;
- accion primaria;
- tono esperado;
- si quieres edicion ligera, media o fuerte.

Si Rodrigo no especifica, usa edicion media: mejora claridad y conversion sin rehacerlo todo.

### 2. Leer texto sin editar

Primero identifica:

- mensaje central;
- promesa principal;
- objecion que intenta resolver;
- CTA;
- pruebas/claims;
- partes que funcionan.

No empieces reescribiendo. Primero entiende que intenta lograr.

### 3. Ejecutar pasadas

Usa `references/editing-sweeps.md`.

Pasadas:

1. Claridad.
2. Tono y voz.
3. Beneficio / "so what".
4. Prueba / claims.
5. Especificidad.
6. Energia emocional.
7. Riesgo y CTA.

Para textos cortos, puedes hacer una version compacta agrupando pasadas.

### 4. Limpiar lenguaje

Usa `references/plain-language.md`.

Detecta:

- palabras infladas;
- frases comodin;
- voz pasiva;
- muletillas;
- adjetivos sin prueba;
- frases que suenan a IA.

No conviertas todo en lenguaje plano si el tono de marca requiere elegancia. La meta es claridad, no sequedad.

### 5. Revisar claims

Clasifica claims:

- permitido: aparece en fuentes;
- necesita prueba: podria quedarse si Rodrigo aporta evidencia;
- suavizar: convertir absoluto en formulacion prudente;
- eliminar: riesgo alto o falso.

Nunca inventes pruebas para salvar un claim.

### 6. Entregar cambios

Usa `templates/revision-copy.md`.

Incluye:

- nivel CE0-CE3;
- diagnostico breve;
- version editada;
- cambios principales;
- claims/riesgos;
- alternativas si aporta valor;
- siguiente accion unica.

## Bloqueos

Bloquea o marca como parcial si:

- no hay texto base;
- no hay objetivo o audiencia;
- hay claims legales/salud/finanzas sin fuente;
- hay cifras, testimonios o garantias sin evidencia;
- el texto contradice contexto, log o marca;
- se quiere publicar en web, Ads, email o CMS sin aprobacion.

## Referencias

- `references/editing-sweeps.md`: pasadas de revision.
- `references/plain-language.md`: reemplazos y frases a evitar.
- `templates/revision-copy.md`: formato de salida.
- `checklists/revision.md`: revision final.
