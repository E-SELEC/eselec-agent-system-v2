# Mapa commands -> skills - 2026-05-18

## Objetivo

Revisar si hay duplicacion real entre commands, skills y agents, y dejar claro que pieza gobierna cada flujo.

## Evidencia

Comando usado:

```powershell
$skillNames = Get-ChildItem .claude\skills -Directory |
  Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') } |
  Select-Object -ExpandProperty Name

Get-ChildItem .claude\commands -Filter *.md |
  Where-Object { $_.Name -ne 'README.md' } |
  ForEach-Object {
    $content = Get-Content -Raw $_.FullName
    [regex]::Matches($content, '\.claude/skills/([^/`]+)|\.claude\\skills\\([^\\`]+)') |
      ForEach-Object { if ($_.Groups[1].Value) { $_.Groups[1].Value } else { $_.Groups[2].Value } }
  } | Sort-Object -Unique
```

Resultado:

- 43 commands revisados.
- 0 referencias a skills inexistentes.
- 5 skills sin command directo: `alignment-check`, `client-audit`, `reports`, `seo-audit`, `seo-canon`.
- Esas 5 no estan huerfanas: se usan desde agentes o rutas internas.
- 2 commands no dependen de una skill de dominio: `alertas-pendientes` y `auditoria-semanal`; son controles/loops multi-cliente.

## Decision

No hay duplicacion rota que corregir ahora.

El patron sano queda asi:

- command = entrada practica, contexto, `--write`, manifest/log/protocolos;
- skill = procedimiento especializado y criterio de dominio;
- agent = rol/orquestacion, decide que skill o command conviene usar.

## Mapa

| Command | Skill principal | Estado |
|---|---|---|
| `alertas-pendientes` | sin skill; control multi-cliente | valido |
| `aplicar-psicologia-marketing` | `marketing-psychology` | valido |
| `auditar-ai-seo` | `ai-seo` | valido |
| `auditar-cro-pagina` | `page-cro` | valido |
| `auditar-formulario` | `form-cro` | valido |
| `auditar-onboarding` | `onboarding-cro` | valido |
| `auditar-paywall` | `paywall-upgrade-cro` | valido |
| `auditar-popup` | `popup-cro` | valido |
| `auditar-schema` | `schema-markup` | valido |
| `auditar-signup-flow` | `signup-flow-cro` | valido |
| `auditar-tracking` | `analytics-tracking` | valido |
| `auditar-woocommerce` | `woocommerce-setup` | valido |
| `auditoria-semanal` | sin skill; control semanal | valido |
| `crear-product-marketing-context` | `product-marketing-context` | valido |
| `crear-prompt` | `prompt-master` | valido |
| `crear-sales-enablement` | `sales-enablement` | valido |
| `crear-social-content` | `social-content` | valido |
| `escribir-cold-email` | `cold-email` | valido |
| `escribir-copy` | `copywriting` | valido |
| `generar-ad-creative` | `ad-creative` | valido |
| `generar-marketing-ideas` | `marketing-ideas` | valido |
| `humanizar-texto` | `humanizalo` | valido |
| `ingestar-evidencia` | `ingesta-evidencia` | valido |
| `limpiar-carpeta-cliente` | `folder-cleanup` | valido |
| `migrar-pieza` | `migration-audit` | valido |
| `plan-ab-test` | `ab-test-setup` | valido |
| `plan-arquitectura-web` | `site-architecture` | valido |
| `plan-churn-prevention` | `churn-prevention` | valido |
| `plan-competitor-page` | `competitor-alternatives` | valido |
| `plan-contenido` | `content-strategy` | valido |
| `plan-email-sequence` | `email-sequence` | valido |
| `plan-free-tool` | `free-tool-strategy` | valido |
| `plan-launch` | `launch-strategy` | valido |
| `plan-lead-magnet` | `lead-magnets` | valido |
| `plan-paid-ads` | `paid-ads` | valido |
| `plan-pricing` | `pricing-strategy` | valido |
| `plan-programmatic-seo` | `programmatic-seo` | valido |
| `plan-referral-program` | `referral-program` | valido |
| `plan-revops` | `revops` | valido |
| `producir-video-kling` | `kling-producer` | valido |
| `revisar-copy` | `copy-editing` | valido |
| `revisar-web-visual` | `web-feedback-loop` | valido |
| `verificar-medicion` | `verificacion-medicion` | valido |

## Skills sin command directo

| Skill | Uso real |
|---|---|
| `alignment-check` | agente `alineacion` |
| `client-audit` | `leader-clientes`, `agency-onboarding`, `agency-retencion`, Reports |
| `reports` | agentes Reports |
| `seo-audit` | lider y especialistas SEO, reputacion, web |
| `seo-canon` | lider y especialistas SEO |

## Consulta Claude

Consulta intentada con agente `alineacion`, modo `plan`, pero el CLI devolvio falta de uso disponible. Se aplico solo una decision documental de bajo riesgo basada en evidencia local.

## Cambio aplicado

Se actualizo `.claude/commands/README.md` para documentar el patron:

- command = entrada practica;
- skill = procedimiento especializado;
- agent = rol/orquestacion.

## Estado

Completado. `protocol_guard.py` limpio.
