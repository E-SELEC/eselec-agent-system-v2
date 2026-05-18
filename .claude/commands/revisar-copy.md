# revisar-copy

Revisa y pule copy existente sin publicarlo ni cambiar su mensaje central.

## Uso

```text
/revisar-copy [cliente] [pieza/alcance] [--write]
```

Ejemplos:

```text
/revisar-copy cliente-servicios hero home
/revisar-copy cliente-local texto servicio
/revisar-copy agencia-demo propuesta comercial
```

## Workflow

1. Leer `.claude/skills/copy-editing/SKILL.md`.
2. Confirmar que existe texto base. Si no existe, usar `copywriting`.
3. Leer:
   - `clients/[cliente]/context.md` o `agency/context.md`
   - memoria/log/mensajes/tasks si existen
   - brand/preferencias si aplica
   - outputs/manifest si existe
4. Ejecutar pasadas de claridad, tono, beneficio, prueba, especificidad, emocion y CTA.
5. Clasificar claims: permitido, necesita prueba, suavizar o eliminar.
6. Entregar usando `templates/revision-copy.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/revision-copy-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No publicar en web.
- No modificar Ads/email/CMS.
- No inventar claims ni pruebas.
- No cambiar el mensaje central sin indicarlo.
- Si hay implementacion real, abrir Orden de Cambio.
