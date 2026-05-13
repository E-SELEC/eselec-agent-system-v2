---
name: product-marketing-context
description: >
  Crea o actualiza contexto de product marketing, posicionamiento, ICP,
  personas, problemas, diferenciacion, objeciones, customer language, proof
  points y goals para evitar repetir informacion base en otras skills. Usalo
  cuando se hable de product context, marketing context, positioning, ICP,
  target audience, customer language, propuesta de valor o contexto de producto.
---

# Product Marketing Context - E-SELEC

## Proposito

Crear una fuente compacta de contexto comercial para que las demas skills produzcan mejores outputs sin reinventar audiencia, posicionamiento ni pruebas.

Esta skill puede proponer o actualizar un archivo de contexto, pero debe aplicar control de artefactos. No debe inventar datos de cliente ni convertir suposiciones en verdad.

## Fuentes obligatorias

Lee contexto de agencia o cliente, `quality/criterios-output.md`, `protocols/control-artefactos.md`, y si existe el contexto previo del cliente/agencia.

Para clientes, prioriza `clients/[cliente]/context.md` y outputs aprobados. Para agencia, prioriza `agency/context.md`, `agency/brand.md` y materiales vigentes.

## Ubicacion recomendada

- Cliente: `clients/[cliente]/context.md` si es contexto principal, o `clients/[cliente]/marketing-context.md` si conviene separarlo.
- Agencia: `agency/context.md` o `agency/product-marketing-context.md`.
- No guardar contexto vivo dentro de `.claude/skills/`; las skills solo contienen instrucciones.

## Niveles

- PM3 - listo: contexto completo, fuentes claras, datos faltantes marcados y archivo destino definido.
- PM2 - fuerte: base util con algunos gaps.
- PM1 - orientativo: borrador con supuestos visibles.
- PM0 - bloqueado: falta producto/oferta o fuente minima.

## Workflow

1. Buscar contexto existente y outputs aprobados.
2. Auto-draft desde fuentes reales cuando existan: README, web, proposals, context, logs, briefs.
3. Separar datos confirmados de supuestos o preguntas.
4. Completar secciones: producto, audiencia, personas, problemas, competidores, diferenciacion, objeciones, switching, lenguaje, voz, pruebas y goals.
5. Marcar contradicciones y pedir confirmacion si afectan decisiones.
6. Preparar output usando `templates/product-marketing-context.md`.
7. Si se escribe archivo, registrar artefacto y ejecutar guard de cierre.

## Reglas

- Customer language literal vale mas que copy pulido.
- No inventar metricas, clientes, logos, testimonios ni claims.
- No mezclar contexto de clientes distintos.
- Toda suposicion debe quedar marcada como pendiente.
- Si el contexto contradice una fuente viva o aprobada, no decidir solo: escalar la contradiccion.

## Bloqueos

- no hay producto/oferta;
- se pide afirmar datos no verificados;
- hay contradiccion relevante entre fuentes;
- se pide sobrescribir contexto vivo sin registrar artefacto.

## Referencias

- `references/context-sections.md`: secciones y criterios.
- `templates/product-marketing-context.md`: formato de salida.
- `checklists/revision.md`: revision final.
