# plan-ab-test

Disena un A/B test medible sin implementarlo.

## Uso

```text
/plan-ab-test [cliente] [hipotesis o pagina] [--write]
```

Ejemplos:

```text
/plan-ab-test cliente-servicios CTA de contacto en home
/plan-ab-test cliente-reservas formulario de reservas
/plan-ab-test cliente-ecommerce landing pedido online
```

## Workflow

1. Leer `.claude/skills/ab-test-setup/SKILL.md`.
2. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
   - `quality/criterios-output.md`
3. Identificar la observacion que origina la hipotesis.
4. Definir hipotesis, control, variante y metrica primaria.
5. Revisar tracking, baseline, trafico, muestra y duracion.
6. Entregar usando `templates/plan-ab-test.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/plan-ab-test-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No implementar test real.
- No tocar web, Ads, pricing, tracking ni checkout.
- No proponer test sin metrica primaria.
- No declarar ganador sin muestra, duracion y criterio definidos.
- Si hay implementacion real, abrir Orden de Cambio.
