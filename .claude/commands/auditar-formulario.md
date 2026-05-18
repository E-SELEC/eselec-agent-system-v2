# auditar-formulario

Audita un formulario para mejorar conversion sin tocar produccion.

## Uso

```text
/auditar-formulario [cliente] [formulario/URL] [--write]
```

Ejemplos:

```text
/auditar-formulario cliente-servicios formulario de contacto
/auditar-formulario cliente-reservas pagina de reservas
/auditar-formulario cliente-ecommerce formulario pedido online
```

## Workflow

1. Leer `.claude/skills/form-cro/SKILL.md`.
2. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
   - `quality/criterios-output.md`
3. Confirmar formulario visible, captura o inventario de campos.
4. Identificar objetivo, campos, uso real de datos y medicion.
5. Revisar friccion, confianza, errores, mobile y privacidad.
6. Entregar usando `templates/auditoria-form-cro.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/auditoria-form-cro-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No modificar formularios reales.
- No tocar CRM, WordPress, GTM ni integraciones.
- No pedir datos sensibles sin justificacion.
- No inventar completion rate, errores ni field drop-off.
- Si hay implementacion real, abrir Orden de Cambio.
