---
name: web-feedback-loop
description: >
  Revisa visualmente paginas web, compara contra referencias y propone
  iteraciones de diseno en estructura, jerarquia, legibilidad, CTA y marca.
  Usalo para visual quality check, hacer que una pagina se parezca a una
  referencia, iterar diseño web, revisar screenshots o validar una pagina.
---

# Web Feedback Loop - E-SELEC

## Proposito

Evaluar una pagina web como experiencia visual y convertir brechas en cambios concretos, medibles y seguros.

Esta skill no toca produccion por defecto. Propone cambios o instrucciones; editar web real requiere Orden de Cambio.

## Fuentes obligatorias

Lee contexto de cliente, `agency/brand.md` si aplica, `quality/criterios-output.md`, `.claude/skills/page-cro/SKILL.md` si el objetivo incluye conversion, `.claude/skills/site-architecture/SKILL.md` si afecta estructura, `protocols/activos-criticos.md` y `protocols/control-artefactos.md`.

Necesitas URL o screenshot actual, referencia o criterio de calidad, dispositivo objetivo, objetivo de pagina y restricciones CMS/tema.

## Niveles

- WFL3 - listo: captura actual, referencia, scoring, brechas, cambios priorizados y verificacion.
- WFL2 - fuerte: scoring y cambios claros, falta screenshot o referencia completa.
- WFL1 - orientativo: revision parcial.
- WFL0 - bloqueado: falta pagina actual o criterio de referencia.

## Workflow

1. Capturar estado actual con URL, HTML, screenshot o imagen aportada.
2. Capturar referencia o criterio.
3. Puntuar estructura, jerarquia, legibilidad, CTA y marca.
4. Crear tabla de brechas y priorizar por impacto/riesgo.
5. Proponer iteracion pequena, verificable y reversible.
6. Si se implementa, requerir Orden de Cambio y verificar antes/despues.
7. Entregar usando `templates/web-feedback-report.md`.

## Reglas

- Distinguir problema visual, problema CRO y problema SEO.
- No hacer redisenos completos si se pidio iteracion puntual.
- No tocar WordPress, CSS, contenido o tema sin Orden de Cambio.
- Verificar mobile y desktop cuando haya cambios visuales.
- No usar imagenes o claims de marca no aprobados.

## Bloqueos

- falta pagina actual o referencia;
- no hay acceso/captura suficiente para evaluar;
- el cambio propuesto afecta estructura, SEO o conversion sin aprobacion;
- se pide modificar produccion sin Orden de Cambio.

## Referencias

- `references/web-visual-score.md`: dimensiones y umbrales.
- `templates/web-feedback-report.md`: formato de salida.
- `checklists/revision.md`: revision final.
