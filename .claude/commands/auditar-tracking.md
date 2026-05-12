# auditar-tracking

Audita o disena la medicion de un cliente sin tocar produccion.

## Uso

```text
/auditar-tracking [cliente] [alcance opcional] [--write]
```

Ejemplos:

```text
/auditar-tracking computer-chamberi GA4
/auditar-tracking cashier-bubble-tea formularios
/auditar-tracking stramondo-venezuela Meta Ads
```

## Workflow

1. Leer `.claude/skills/analytics-tracking/SKILL.md`.
2. Identificar modo: auditoria, plan, implementacion guiada o validacion.
3. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
4. Definir decision que debe informar la medicion.
5. Revisar herramientas declaradas: GA4, GTM, Ads, Meta Pixel, formularios, llamadas, WhatsApp, WooCommerce.
6. Clasificar Nivel T0/T1/T2/T3.
7. Entregar plan usando `templates/plan-tracking.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/evidencia-tracking-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No publicar GTM.
- No modificar GA4.
- No tocar pixels ni conversiones.
- No tocar WordPress/WooCommerce.
- No pedir ni guardar secretos.
- No enviar PII a analytics.
- Si hay implementacion real, abrir Orden de Cambio.
