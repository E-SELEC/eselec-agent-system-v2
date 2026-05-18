# auditar-onboarding

Audita onboarding post-signup y activacion sin tocar produccion.

## Uso

```text
/auditar-onboarding [cliente] [flujo/producto] [--write]
```

Ejemplos:

```text
/auditar-onboarding cliente-servicios nueva cuenta
/auditar-onboarding cliente-reservas reservas recurrentes
/auditar-onboarding cliente-ecommerce primera compra registrada
```

## Workflow

1. Leer `.claude/skills/onboarding-cro/SKILL.md`.
2. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
   - `quality/criterios-output.md`
3. Definir o marcar pendiente el evento de activacion.
4. Mapear desde signup completado hasta primer valor.
5. Revisar pasos, empty states, checklist, ayuda, email/in-app y medicion.
6. Entregar usando `templates/auditoria-onboarding-cro.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/auditoria-onboarding-cro-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No modificar producto real.
- No tocar emails, CRM, tracking ni datos de usuario.
- No inventar activation rate ni retencion.
- No llamar activacion a una accion no conectada con valor.
- Si hay implementacion real, abrir Orden de Cambio.
