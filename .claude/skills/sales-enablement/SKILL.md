---
name: sales-enablement
description: >
  Crea y revisa materiales comerciales para E-SELEC o clientes: sales decks,
  pitch decks, one-pagers, objection handling, demo scripts, talk tracks,
  proposal templates, ROI calculators, buyer persona cards, sales playbooks y
  materiales para ayudar a ventas a cerrar. Usalo cuando se hable de deck,
  propuesta, one-pager, objeciones, demo script, playbook o sales collateral.
---

# Sales Enablement - E-SELEC

## Proposito

Crear materiales que ventas pueda usar de verdad: especificos por persona, etapa y objecion, con prueba y siguiente paso claro.

Esta skill no envia propuestas ni modifica documentos comerciales finales sin aprobacion.

## Fuentes obligatorias

Lee contexto de agencia o cliente, marca/preferencias si aplica, `quality/criterios-output.md`, y cuando aplique `.claude/skills/copywriting/SKILL.md`, `.claude/skills/competitor-alternatives/SKILL.md`, `.claude/skills/pricing-strategy/SKILL.md` si existe, y `protocols/activos-criticos.md`.

Necesitas asset, audiencia, etapa de venta, objetivo y pruebas/claims permitidos.

## Niveles

- SE3 - listo: asset, persona, etapa, mensaje, prueba, objeciones y CTA definidos.
- SE2 - fuerte: material usable, faltan datos de venta o diseno final.
- SE1 - orientativo: estructura con contexto parcial.
- SE0 - bloqueado: falta asset, audiencia, objetivo o prueba.

## Workflow

1. Definir asset: deck, one-pager, objection doc, demo script, proposal, playbook.
2. Definir usuario del asset: Rodrigo, SDR, closer, champion, prospect.
3. Definir etapa: prospeccion, discovery, demo, negociacion, cierre.
4. Mapear persona, dolor, diferenciadores, prueba, objeciones y CTA.
5. Crear estructura y copy.
6. Revisar claims, precio, competencia y aprobaciones.
7. Preparar output con `templates/sales-enablement-asset.md`.

## Reglas

- Scannable antes que exhaustivo.
- Un asset debe servir a una etapa concreta.
- Cada claim necesita fuente o se marca pendiente.
- No prometer precios/resultados no aprobados.
- No enviar propuesta final ni usar datos sensibles sin aprobacion.

## Bloqueos

- no se sabe que asset se necesita;
- no hay audiencia/persona;
- faltan pruebas para claims clave;
- el material contiene pricing no aprobado;
- se pide enviar al prospecto sin aprobacion.

## Referencias

- `references/sales-asset-patterns.md`: tipos de asset.
- `templates/sales-enablement-asset.md`: formato de salida.
- `checklists/revision.md`: revision final.
