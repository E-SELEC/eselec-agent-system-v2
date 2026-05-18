# plan-contenido

Planifica una estrategia de contenido priorizada para un cliente sin publicar nada.

## Uso

```text
/plan-contenido [cliente] [alcance opcional] [--write]
```

Ejemplos:

```text
/plan-contenido cliente-servicios SEO local 90 dias
/plan-contenido cliente-local blog + AI SEO
/plan-contenido agencia-demo captacion
```

## Workflow

1. Leer `.claude/skills/content-strategy/SKILL.md`.
2. Identificar objetivo: SEO, AI SEO, leads, autoridad, reputacion, soporte o lanzamiento.
3. Leer:
   - `clients/[cliente]/context.md` o `agency/context.md`
   - memoria/log/mensajes/tasks si existen
   - outputs/manifest si existe
4. Revisar evidencia disponible: GSC, SEMrush, AI SEO, ventas, soporte, log.
5. Definir pilares, clusters y backlog de temas.
6. Priorizar con `references/prioritization.md`.
7. Entregar usando `templates/estrategia-contenido.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/estrategia-contenido-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No publicar contenido.
- No tocar WordPress/CMS.
- No crear paginas reales.
- No inventar volumen, dificultad ni resultados.
- No prometer trafico ni citas AI.
- Si hay implementacion real, abrir Orden de Cambio.
