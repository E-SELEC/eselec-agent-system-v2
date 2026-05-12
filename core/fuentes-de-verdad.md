# Fuentes de verdad

| Tipo de dato | Fuente principal | Fuente secundaria |
|---|---|---|
| Tareas | Notion | `clients/[cliente]/tasks.md` |
| Perfil cliente | `clients/[cliente]/context.md` | Notion |
| Memoria operativa cliente | `clients/[cliente]/memory.md` | `log.md` |
| Historial ejecutado | `log.md` | - |
| Alertas/dependencias | `mensajes.md` | - |
| Datos vivos | API/MCP/conector oficial | snapshot en contexto |
| Credenciales | Gestor externo o `.env` local | nunca repo |

Si hay contradiccion entre un dato vivo y un snapshot local, se documenta la diferencia antes de continuar.

