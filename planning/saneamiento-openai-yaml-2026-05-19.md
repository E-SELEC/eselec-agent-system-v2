# Saneamiento openai.yaml en skills - 2026-05-19

## Objetivo

Resolver el pendiente de la Fase 16 sobre los archivos `.claude/skills/*/agents/openai.yaml` y decidir si debian permanecer en el sistema v2.

## Decision

Se eliminaron 40 archivos `.claude/skills/*/agents/openai.yaml`.

## Por que se eliminaron

Claude Code usa estas primitivas principales en este repo:

- `.claude/agents/*.md` para subagentes.
- `.claude/skills/<skill>/SKILL.md` para skills.
- `.claude/commands/*.md` para comandos.
- `.claude/rules/*.md` para reglas.

Los archivos `openai.yaml` contenian metadatos de interfaz (`display_name`, `short_description`, `default_prompt`) y no eran leidos por Claude Code como parte nativa del sistema.

Claude pidio confirmar si habia un consumidor externo. Con la evidencia local y la aclaracion de Rodrigo de que fueron creados por Codex durante la migracion, se concluyo que no hay consumidor externo conocido. Por eso se eliminaron con inventario y commit propio.

## Evidencia

Comandos usados:

```powershell
git ls-files -- '.claude/skills/*/agents/openai.yaml'
rg "openai\.yaml|agents/openai|agents\\openai|default_prompt|display_name|short_description" . --glob "!clients/**/outputs/**" --glob "!legacy/**" --glob "!outputs/**"
```

Resultado:

- 40 archivos `openai.yaml` rastreados por Git.
- No habia referencias internas operativas en agents, commands, skills, scripts o README.
- Las unicas referencias utiles estaban en planning/registros recientes, donde ya se marcaban como pendiente de revision.

## Archivos eliminados

- `.claude/skills/ab-test-setup/agents/openai.yaml`
- `.claude/skills/ad-creative/agents/openai.yaml`
- `.claude/skills/ai-seo/agents/openai.yaml`
- `.claude/skills/analytics-tracking/agents/openai.yaml`
- `.claude/skills/churn-prevention/agents/openai.yaml`
- `.claude/skills/cold-email/agents/openai.yaml`
- `.claude/skills/competitor-alternatives/agents/openai.yaml`
- `.claude/skills/content-strategy/agents/openai.yaml`
- `.claude/skills/copy-editing/agents/openai.yaml`
- `.claude/skills/copywriting/agents/openai.yaml`
- `.claude/skills/email-sequence/agents/openai.yaml`
- `.claude/skills/folder-cleanup/agents/openai.yaml`
- `.claude/skills/form-cro/agents/openai.yaml`
- `.claude/skills/free-tool-strategy/agents/openai.yaml`
- `.claude/skills/humanizalo/agents/openai.yaml`
- `.claude/skills/ingesta-evidencia/agents/openai.yaml`
- `.claude/skills/kling-producer/agents/openai.yaml`
- `.claude/skills/launch-strategy/agents/openai.yaml`
- `.claude/skills/lead-magnets/agents/openai.yaml`
- `.claude/skills/marketing-ideas/agents/openai.yaml`
- `.claude/skills/marketing-psychology/agents/openai.yaml`
- `.claude/skills/onboarding-cro/agents/openai.yaml`
- `.claude/skills/page-cro/agents/openai.yaml`
- `.claude/skills/paid-ads/agents/openai.yaml`
- `.claude/skills/paywall-upgrade-cro/agents/openai.yaml`
- `.claude/skills/popup-cro/agents/openai.yaml`
- `.claude/skills/pricing-strategy/agents/openai.yaml`
- `.claude/skills/product-marketing-context/agents/openai.yaml`
- `.claude/skills/programmatic-seo/agents/openai.yaml`
- `.claude/skills/prompt-master/agents/openai.yaml`
- `.claude/skills/referral-program/agents/openai.yaml`
- `.claude/skills/reports/agents/openai.yaml`
- `.claude/skills/revops/agents/openai.yaml`
- `.claude/skills/sales-enablement/agents/openai.yaml`
- `.claude/skills/schema-markup/agents/openai.yaml`
- `.claude/skills/signup-flow-cro/agents/openai.yaml`
- `.claude/skills/site-architecture/agents/openai.yaml`
- `.claude/skills/social-content/agents/openai.yaml`
- `.claude/skills/web-feedback-loop/agents/openai.yaml`
- `.claude/skills/woocommerce-setup/agents/openai.yaml`

## Impacto

- Reduce ruido estructural dentro de las skills.
- Evita que futuros agentes interpreten esos archivos como una primitiva viva.
- Mantiene el sistema mas alineado con Claude Code: cada skill vive en su `SKILL.md`.

## Rollback

Si aparece una herramienta externa que realmente necesite esos archivos, se recuperan desde el historial de Git del commit anterior a esta fase.

