---
name: form-cro
description: >
  Audita y optimiza formularios no signup para clientes de E-SELEC: formularios
  de contacto, lead capture, demo, presupuesto, quote request, encuestas,
  formularios de aplicacion, checkout forms, abandono de formulario, campos,
  etiquetas, errores, mobile, privacidad, completion rate, field drop-off,
  conversion de leads y friccion. Usalo cuando se hable de form CRO,
  formulario que no convierte, demasiados campos, form abandonment o lead forms.
---

# Form CRO - E-SELEC

## Proposito

Mejorar la tasa de completado de formularios sin perder datos realmente necesarios ni romper seguimiento, privacidad o operaciones.

Esta skill no toca formularios reales. Produce auditoria, redisenio recomendado o plan de test.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`, contrato CRO / pagina y tracking
8. `.claude/skills/page-cro/SKILL.md` si el formulario vive en una landing/pagina
9. `.claude/skills/analytics-tracking/SKILL.md` si hay conversion/eventos
10. `.claude/skills/ab-test-setup/SKILL.md` si propones test
11. `protocols/activos-criticos.md`

Necesitas ver el formulario o su estructura de campos. Si no hay captura, URL o descripcion de campos, no entregues auditoria final.

## Niveles

- FC3 - validado: formulario revisado, campos, mobile, errores y tracking/completion medidos.
- FC2 - diagnostico fuerte: formulario visible y objetivo claro; faltan datos cuantitativos o field analytics.
- FC1 - orientativo: hay descripcion/captura parcial, faltan metricas y contexto.
- FC0 - bloqueado: falta formulario, objetivo o datos que se capturan.

## Workflow

1. Definir tipo de formulario: contacto, demo, presupuesto, lead magnet, encuesta, checkout.
2. Identificar conversion principal y que pasa despues del envio.
3. Inventariar campos: requerido/opcional, motivo, uso real, sensibilidad.
4. Revisar friccion: cantidad de campos, orden, labels, placeholders, ayudas, errores, mobile.
5. Revisar confianza: privacidad, respuesta esperada, seguridad, no spam, prueba cerca.
6. Revisar medicion: view, start, field completion, errors, submit, success.
7. Priorizar: quitar, hacer opcional, reagrupar, cambiar copy, multi-step, validacion, tracking.
8. Preparar output con `templates/auditoria-form-cro.md`.

## Reglas

- Cada campo debe justificar su existencia.
- No pedir datos sensibles si no son necesarios.
- Telefono debe ser opcional salvo que el proceso lo requiera.
- Mensaje libre debe ser opcional o guiado cuando sea posible.
- No recomendar test si no hay medicion/trafico.
- No tocar formulario/CMS/CRM/GTM sin Orden de Cambio.

## Bloqueos

- no hay formulario visible;
- no se sabe que conversion busca;
- se piden cambios reales sin aprobacion;
- el formulario captura PII sensible sin justificacion;
- la recomendacion rompe CRM, ventas o cumplimiento legal.

## Referencias

- `references/form-patterns.md`: patrones y campos por tipo de formulario.
- `templates/auditoria-form-cro.md`: formato de salida.
- `checklists/revision.md`: revision final.
