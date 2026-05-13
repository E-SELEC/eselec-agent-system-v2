# Inventario de agentes legacy

Fecha: 2026-05-13
Responsable: Codex + Arquitecto
Fase: P3-004

## Resultado rapido

- Archivos markdown legacy bajo `agents/`: 81.
- Agentes v2 existentes antes de P3-004: 5.
- Agentes especialistas a migrar como `.claude/agents/`: 34.
- Archivos que no deben migrarse como agentes directos: referencias, fuentes y aprendizajes del Docente.

## Ya existe en v2

- `.claude/agents/leader-clientes.md`
- `.claude/agents/leader-agencia.md`
- `.claude/agents/docente.md`
- `.claude/agents/arquitecto-migracion-claude.md`
- `.claude/agents/README.md`

## Agentes a migrar

### Equipo Clientes - lideres de area

| Legacy | Destino v2 | Estado |
|---|---|---|
| `agents/seo/leader-seo.md` | `.claude/agents/seo-leader.md` | hecho |
| `agents/cro/leader-cro.md` | `.claude/agents/cro-leader.md` | hecho |
| `agents/sem/leader-sem.md` | `.claude/agents/sem-leader.md` | hecho |
| `agents/social/leader-social.md` | `.claude/agents/social-leader.md` | hecho |
| `agents/reports/leader-reports.md` | `.claude/agents/reports-leader.md` | hecho |
| `agents/web/leader-web.md` | `.claude/agents/web-leader.md` | hecho |

### Equipo Clientes - especialistas

| Area | Especialistas legacy | Destino |
|---|---|---|
| SEO | `seo-tecnico`, `seo-organico`, `seo-local`, `seo-llms`, `seo-web` | `.claude/agents/seo-*.md` - hecho |
| CRO | `cro-funnels`, `cro-landing`, `cro-formularios`, `cro-tests`, `cro-uxui` | `.claude/agents/cro-*.md` - hecho |
| SEM | `sem-google`, `sem-meta`, `sem-linkedin`, `sem-tiktok`, `sem-analitica` | `.claude/agents/sem-*.md` - hecho |
| Social | `social-estrategia`, `social-contenido`, `social-comunidad` | `.claude/agents/social-*.md` - hecho |
| Reports | `reports-cliente`, `reports-alertas`, `reports-proxpasos` | `.claude/agents/reports-*.md` - hecho |
| Web | `web-arquitectura`, `web-diseno`, `web-desarrollo`, `web-implementacion`, `web-mantenimiento`, `web-feedback-loop` | `.claude/agents/web-*.md` - hecho |

### Equipo Agencia - especialistas

| Legacy | Destino v2 | Estado |
|---|---|---|
| `agency-captacion.md` | `.claude/agents/agency-captacion.md` | hecho |
| `agency-reputacion.md` | `.claude/agents/agency-reputacion.md` | hecho |
| `agency-onboarding.md` | `.claude/agents/agency-onboarding.md` | hecho |
| `agency-retencion.md` | `.claude/agents/agency-retencion.md` | hecho |
| `agency-finanzas.md` | `.claude/agents/agency-finanzas.md` | hecho |

### Gobernanza y loops

| Legacy | Destino v2 | Estado |
|---|---|---|
| `agents/arquitecto/arquitecto.md` | `.claude/agents/arquitecto.md` | pendiente |
| `agents/fenix/fenix.md` | `.claude/agents/fenix.md` | pendiente |
| `agents/calibracion/calibracion.md` | `.claude/agents/calibracion.md` | pendiente |
| `agents/loops/leader-loops.md` | `.claude/agents/loops-leader.md` | pendiente |

## No migrar como agente directo

Estos archivos se tratan como conocimiento, fuentes o referencia, no como subagents ejecutables:

- `agents/docente/seo/aprendizajes/*`
- `agents/docente/seo/fuentes/*`
- `agents/seo/referencias/*`
- `agents/seo/semrush-workflows.md`
- `agents/README.md`
- `agents/docente/guia-interna-sistema-e-selec.md`

## Orden recomendado

1. Lideres de area clientes: desbloquean routing desde `leader-clientes`.
2. Especialistas SEO/CRO/SEM: mayor uso operativo y riesgo de calidad.
3. Especialistas Social/Reports/Web: salida a entregables, informes y web.
4. Especialistas Agencia: captacion, reputacion, onboarding, retencion y finanzas.
5. Gobernanza y loops: calibracion, fenix, arquitecto y loops.

## Criterio v2

Cada agente debe quedar como subagent breve:

- proposito unico;
- activacion clara;
- lectura obligatoria;
- skills/commands que puede usar;
- permisos y bloqueos;
- formato de salida;
- criterios de parada.

No se copian prompts legacy completos si mezclan memoria, fuentes o ejecucion sin guardrails.
