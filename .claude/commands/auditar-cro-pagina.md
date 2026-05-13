# auditar-cro-pagina

Audita una pagina para mejorar conversion sin tocar produccion.

## Uso

```text
/auditar-cro-pagina [cliente] [URL o pagina] [--write]
```

Ejemplos:

```text
/auditar-cro-pagina computer-chamberi home
/auditar-cro-pagina la-bottega-del-gusto pagina de contacto
/auditar-cro-pagina cashier-bubble-tea landing pedido online
```

## Workflow

1. Leer `.claude/skills/page-cro/SKILL.md`.
2. Identificar pagina, audiencia, oferta, fuente de trafico y conversion principal.
3. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
4. Revisar vista de pagina, captura o estructura.
5. Revisar medicion. Si falta, marcar parcial.
6. Entregar usando `templates/auditoria-cro-pagina.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/auditoria-cro-pagina-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No tocar web/CMS.
- No modificar formularios.
- No modificar Ads ni tracking.
- No inventar conversion rate.
- No proponer A/B test sin medicion/trafico.
- Si hay implementacion real, abrir Orden de Cambio.
