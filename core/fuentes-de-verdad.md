# Fuentes de verdad

| Tipo de dato | Fuente principal | Fuente secundaria |
|---|---|---|
| Tareas | Notion | `clients/[cliente]/tasks.md` |
| Perfil cliente | `clients/[cliente]/context.md` | Notion |
| Memoria operativa cliente | `clients/[cliente]/memory.md` | `log.md` |
| Historial ejecutado | `log.md` | - |
| Alertas/dependencias | `mensajes.md` | - |
| Datos vivos | API/MCP/conector oficial | snapshot en contexto |
| Evidencia saneada | `clients/[cliente]/outputs/evidencia-*.md` | export/captura/output legacy no versionado |
| Credenciales | Gestor externo o `.env` local | nunca repo |

Si hay contradiccion entre un dato vivo y un snapshot local, se documenta la diferencia antes de continuar.

Los exports brutos no son fuente de verdad dentro del repo. Primero deben pasar por `ingesta-evidencia` y quedar resumidos con fuente, periodo, nivel E0/E1/E2/E3 y limites.

