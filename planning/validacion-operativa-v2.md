# Validacion operativa post-migracion v2

Fecha: 2026-05-13
Responsable: Codex + Arquitecto
Estado: limpio

## Objetivo

Comprobar que el sistema v2 no solo esta migrado, sino que puede arrancar con una base coherente: backlog cerrado, agentes con frontmatter valido, skills presentes, commands presentes, archivos obligatorios existentes y guard limpio.

## Comprobaciones ejecutadas

| Comprobacion | Resultado |
|---|---|
| `git status --short` | limpio antes de iniciar validacion |
| `python scripts/protocol_guard.py --no-report` | limpio |
| Backlog de migracion | 24/24 items en `hecho` |
| Agentes v2 con frontmatter valido | 46/46 subagents reales |
| Archivos markdown en `.claude/agents/` | 47 incluyendo `README.md` |
| Skills con `SKILL.md` | 43/43 |
| Commands basicos | 44/44 |
| Archivos obligatorios de protocolos/calidad/cierre | 9/9 |

## Ajuste realizado

Durante la validacion se detecto que `.claude/agents/arquitecto-migracion-claude.md` no tenia `effort:` en el frontmatter.

Se corrigio con:

```yaml
effort: high
```

## Correccion de conteo

La cifra anterior decia "Agentes v2 totales: 47".

La lectura precisa es:

- 46 subagents reales.
- 47 archivos Markdown dentro de `.claude/agents/` si se incluye `README.md`.

## Estado final

El sistema v2 esta listo para primer uso operativo.

La primera tarea real debe entrar por:

- `leader-clientes` si es cliente;
- `leader-agencia` si es trabajo interno;
- `arquitecto-migracion-claude` solo si aparece una pieza legacy nueva que aun no se haya decidido.

## Riesgo residual

Los conectores productivos siguen bloqueados/deferidos por decision consciente. Esto no impide usar el sistema v2; solo evita tocar produccion o accesos sin una version segura.
