# Auditoria de duplicaciones agents / skills / commands - 2026-05-19

## Objetivo

Confirmar si el sistema v2 tiene duplicacion operativa entre agentes, skills y commands, y corregir solo lo que cause confusion real.

## Evidencia ejecutada

```powershell
$agents = (Get-ChildItem .claude\agents -Filter *.md | Where-Object {$_.Name -ne 'README.md'}).Count
$skills = (Get-ChildItem .claude\skills -Directory | Where-Object {Test-Path (Join-Path $_.FullName 'SKILL.md')}).Count
$commands = (Get-ChildItem .claude\commands -Filter *.md | Where-Object {$_.Name -ne 'README.md'}).Count
```

Resultado:

- 47 agents.
- 46 skills con `SKILL.md`.
- 43 commands.

Mapa previo revisado:

- `planning/mapa-commands-skills-2026-05-18.md`
- Resultado previo: 43 commands revisados, 0 referencias a skills inexistentes, 5 skills sin command directo pero usadas por agentes/rutas internas, 2 commands multi-cliente sin skill.

## Hallazgos

### DPL-001 - Routing SEO con etiqueta obsoleta

Evidencia:

```powershell
rg -n "futuro" .claude\agents
```

Resultado relevante:

- `.claude/agents/seo-leader.md`: la tabla de routing decia `futuro seo-tecnico`, aunque `.claude/agents/seo-tecnico.md` ya existe.

Decision:

- Corregido a `seo-tecnico`.
- Riesgo bajo.
- Beneficio: evita que el lider SEO trate un especialista existente como si no estuviera migrado.

### DPL-002 - `openai.yaml` dentro de skills

Evidencia:

```powershell
rg --files .claude\skills -g "openai.yaml"
```

Resultado:

- 40 archivos `.claude/skills/*/agents/openai.yaml`.
- No se encontraron referencias internas en agents, commands, README, planning o registros.

Decision:

- No se eliminan en esta fase.
- Se registran como pendiente de saneamiento.
- Motivo: parecen metadatos de formato OpenAI/legacy, no primitivas Claude Code, pero no se descarta que una herramienta externa los lea.

## Estado del patron

El patron actual es correcto:

- command = entrada practica para Rodrigo;
- skill = procedimiento especializado;
- agent = rol, orquestacion y routing;
- canon = referencia profunda bajo demanda, no memoria de cliente;
- cliente = datos reales y outputs especificos.

## Siguiente paso recomendado

Antes de borrar los 40 `openai.yaml`, confirmar si alguna herramienta externa al repo los consume. Si no hay consumidor externo, abrir Fase 17 para eliminarlos ordenadamente con inventario, registro y commit propio.
