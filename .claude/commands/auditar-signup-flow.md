# auditar-signup-flow

Audita un flujo de registro o alta de prueba sin tocar produccion.

## Uso

```text
/auditar-signup-flow [cliente] [flujo/URL] [--write]
```

Ejemplos:

```text
/auditar-signup-flow cliente-servicios alta de cuenta
/auditar-signup-flow cliente-reservas registro de reservas
/auditar-signup-flow cliente-ecommerce cuenta para pedidos online
```

## Workflow

1. Leer `.claude/skills/signup-flow-cro/SKILL.md`.
2. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
   - `quality/criterios-output.md`
3. Confirmar flujo visible, captura o mapa de pasos/campos.
4. Definir conversion objetivo y pantalla posterior.
5. Revisar campos, auth, SSO, password, verificacion, mobile y medicion.
6. Entregar usando `templates/auditoria-signup-flow.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/auditoria-signup-flow-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No modificar flujo real.
- No tocar auth, producto, pagos, email, CRM ni tracking.
- No pedir datos sensibles sin justificacion.
- No inventar completion rate ni drop-off.
- Si hay implementacion real, abrir Orden de Cambio.
