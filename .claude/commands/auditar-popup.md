# auditar-popup

Audita un popup, modal, overlay, slide-in o banner sin tocar produccion.

## Uso

```text
/auditar-popup [cliente] [popup/pagina] [--write]
```

Ejemplos:

```text
/auditar-popup cliente-ecommerce popup newsletter
/auditar-popup cliente-reservas banner reservas
/auditar-popup cliente-servicios exit intent contacto
```

## Workflow

1. Leer `.claude/skills/popup-cro/SKILL.md`.
2. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
   - `quality/criterios-output.md`
3. Confirmar objetivo, oferta, pagina, trigger, frecuencia y audiencia.
4. Revisar UX, mobile, accesibilidad, privacidad, SEO movil y medicion.
5. Entregar usando `templates/auditoria-popup-cro.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/auditoria-popup-cro-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No modificar popups reales.
- No tocar CMS, CMP, GTM, scripts ni herramientas de popup.
- No usar declinar manipulativo.
- No inventar conversion rate ni close rate.
- Si hay implementacion real, abrir Orden de Cambio.
