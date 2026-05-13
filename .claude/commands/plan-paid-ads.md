# plan-paid-ads

Planifica o audita una campana paid media sin tocar cuentas reales.

## Uso

```text
/plan-paid-ads [cliente] [plataforma/objetivo] [--write]
```

Ejemplos:

```text
/plan-paid-ads stramondo-venezuela Meta Ads leads
/plan-paid-ads computer-chamberi Google Ads reparacion ordenadores
/plan-paid-ads la-bottega-del-gusto retargeting reservas
```

## Workflow

1. Leer `.claude/skills/paid-ads/SKILL.md`.
2. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/tasks.md` si existe
   - `clients/[cliente]/outputs/manifest.md`
   - `quality/criterios-output.md`
3. Confirmar objetivo, conversion, presupuesto, landing y tracking.
4. Disenar plataforma, estructura, audiencias, exclusiones y medicion.
5. Entregar usando `templates/plan-paid-ads.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/plan-paid-ads-YYYY-MM-DD.md
```

Despues:

- actualizar manifest;
- actualizar log;
- aplicar control de artefactos;
- ejecutar checks de secretos antes de commit.

## Reglas

- No tocar cuentas reales de Ads.
- No cambiar presupuesto, campañas, pixels ni billing.
- No proponer conversion campaigns sin tracking.
- No inventar CPA, ROAS ni conversiones.
- Si hay implementacion real, abrir Orden de Cambio.
