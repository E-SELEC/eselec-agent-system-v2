# generar-ad-creative

Genera o itera creatividades de anuncios sin subirlas a plataformas.

## Uso

```text
/generar-ad-creative [cliente] [plataforma/formato] [--write]
```

Ejemplos:

```text
/generar-ad-creative stramondo-venezuela Meta Ads reels
/generar-ad-creative computer-chamberi Google RSA reparacion portatiles
/generar-ad-creative la-bottega-del-gusto Meta Ads reservas
```

## Workflow

1. Leer `.claude/skills/ad-creative/SKILL.md`.
2. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
   - `quality/criterios-output.md`
3. Confirmar plataforma, formato, objetivo, audiencia, oferta y restricciones.
4. Crear variaciones por angulo y validar limites.
5. Entregar usando `templates/ad-creative-set.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/ad-creative-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No subir anuncios.
- No tocar campañas reales.
- No inventar claims ni resultados.
- No ignorar limites de caracteres.
- Si hay implementacion real, abrir Orden de Cambio.
