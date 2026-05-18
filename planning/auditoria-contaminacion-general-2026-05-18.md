# Auditoria de contaminacion general - 2026-05-18

## Objetivo

Revisar si nombres, casos o datos de clientes reales viven en carpetas generales donde puedan contaminar instrucciones reutilizables.

## Alcance

Revisado:

- `.claude/skills/`
- `.claude/agents/`
- `.claude/commands/`
- `.claude/rules/`
- `quality/`
- `protocols/`
- `agency/`
- `planning/`
- `registries/`
- `AGENTS.md`

## Evidencia

Comandos usados:

```powershell
rg -n -i "computer[- ]?chamber[ií]|computerchamberi|stramondo|cashier|chashier|bottega|shogun|tallermotoshogun|venezuela|madrid" .claude\skills .claude\agents .claude\commands quality protocols agency README.md CLAUDE.md AGENTS.md

rg -n -i "computer[- ]?chamber[ií]|computerchamberi|stramondo|cashier|chashier|bottega|shogun|tallermotoshogun|venezuela|madrid" .claude\rules AGENTS.md
```

Resultado:

- `.claude/rules/` y `AGENTS.md`: sin coincidencias de clientes reales.
- `.claude/skills/`: sin casos reales criticos; `seo-canon` conserva ejemplos pedagogicos genericos de Madrid, no nombres de clientes.
- `.claude/commands/`: multiples ejemplos usaban nombres de clientes reales.
- `.claude/agents/loops-leader.md`: un loop estaba atado a un cliente concreto de Meta Ads.
- `agency/`, `planning/` y `registries/`: contienen clientes reales como historia, inventario y trazabilidad.

## Consulta Claude

Claude recomendó:

1. anonimizar ejemplos de commands;
2. generalizar el loop de Meta Ads;
3. no tocar `seo-canon`;
4. no tocar `agency/`, `planning/` ni `registries/`;
5. añadir regla preventiva en `commands/README.md`.

## Ajustes aplicados

- Reemplazados ejemplos de clientes reales en 18 commands por slugs inventados como `cliente-servicios`, `cliente-ecommerce`, `cliente-reservas`, `cliente-b2b`, `cliente-local` y `agencia-demo`.
- Generalizado `LOOP: meta-ads-semanal` para leer el cliente activo con Meta Ads desde `AGENTS.md` o `agency/context.md`.
- Añadida nota en `.claude/commands/README.md`: no usar clientes reales en ejemplos reutilizables.

## Decision de no tocar

No se modificaron `agency/`, `planning/` ni `registries/` porque son capas de memoria, historia y trazabilidad. Ahi los clientes reales son informacion operacional, no instrucciones reutilizables.

## Estado

Completado. Grep final sin clientes reales en commands/loops reutilizables y `protocol_guard.py` limpio.
