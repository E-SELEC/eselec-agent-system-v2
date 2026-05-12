# Regla de migracion Claude Code

Usar esta regla para cualquier cambio que adapte piezas del sistema legacy E-SELEC al sistema v2.

## Principio rector

No se migra una carpeta. Se migra una responsabilidad.

Cada pieza legacy debe clasificarse antes de moverse:

| Si la pieza es... | Va a... |
|---|---|
| Instruccion siempre activa, corta y transversal | `CLAUDE.md` o `AGENTS.md` |
| Regla aplicable por tema, ruta o tipo de trabajo | `.claude/rules/` |
| Procedimiento reutilizable bajo demanda | `.claude/skills/<nombre>/SKILL.md` |
| Trabajador especializado con contexto propio | `.claude/agents/<nombre>.md` |
| Comando repetible iniciado por Rodrigo | `.claude/commands/` |
| Integracion externa compartida | `.mcp.json` sin secretos |
| Script local revisado | `scripts/` |
| Memoria de cliente | `clients/[cliente]/memory.md`, `context.md`, `log.md` o `mensajes.md` |
| Historico sin uso operativo directo | `legacy/` o no se migra |

## Criterios de calidad

Una migracion no esta completa hasta que:

- La pieza tiene propietario y proposito claro.
- No duplica otra pieza viva.
- No contiene secretos.
- No mezcla memoria historica con instrucciones operativas.
- Tiene criterio de activacion.
- Tiene criterio de parada.
- Tiene formato de salida esperado.
- Tiene prueba o checklist de verificacion.
- Queda registrada en `registries/registro-migracion.md`.

## Regla contra resultados mediocres

Si un output puede salir generico, ambiguo o pobre, la causa debe diagnosticarse antes de culpar al modelo:

- Falta de contexto correcto.
- Contexto excesivo o contradictorio.
- Skill no cargada.
- Agente equivocado.
- Ausencia de ejemplos de calidad.
- Falta de datos vivos.
- Criterio de evaluacion inexistente.
- Permisos demasiado abiertos o demasiado estrechos.
