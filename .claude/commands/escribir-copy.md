# escribir-copy

Escribe o mejora copy comercial para un cliente sin publicarlo.

## Uso

```text
/escribir-copy [cliente] [pieza/alcance] [--write]
```

Ejemplos:

```text
/escribir-copy computer-chamberi hero home
/escribir-copy la-bottega-del-gusto pagina servicio
/escribir-copy agencia E-SELEC landing captacion
```

## Workflow

1. Leer `.claude/skills/copywriting/SKILL.md`.
2. Identificar pieza, audiencia, oferta, objetivo y accion primaria.
3. Leer:
   - `clients/[cliente]/context.md` o `agency/context.md`
   - memoria/log/mensajes/tasks si existen
   - brand/preferencias si aplica
   - outputs/manifest si existe
4. Revisar pruebas disponibles y claims prohibidos.
5. Escribir usando `templates/copy-output.md`.
6. Marcar nivel CW0-CW3.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/copy-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No publicar en web.
- No modificar Ads/email/CMS.
- No inventar claims.
- No prometer resultados.
- Si hay implementacion real, abrir Orden de Cambio.
