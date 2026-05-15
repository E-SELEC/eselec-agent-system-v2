---
source_url: https://code.claude.com/docs/es/agents
fetched_url: https://code.claude.com/docs/es/agents.md
category: Crear con Claude Code, agentes y automatizacion
status: 200
scraped_at: 2026-05-15T14:27:38+00:00
sha256_16: 8de342b1e690efd4
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ejecutar agentes en paralelo

> Compare las formas en que Claude Code puede realizar múltiples tareas simultáneamente: subagentes, vista de agentes, equipos de agentes y sesiones de worktree aisladas.

[Subagentes](/es/sub-agents), [vista de agentes](/es/agent-view), [equipos de agentes](/es/agent-teams) y [worktrees](/es/worktrees) cada uno paraleliza el trabajo de una manera diferente. El correcto depende de si desea permanecer en cada conversación usted mismo, delegar tareas y volver a verificar más tarde, o si desea que Claude coordine un grupo de trabajadores para usted.

| Enfoque                               | Lo que le proporciona                                                                                                                                              | Úselo cuando                                                                                                                                       |
| :------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Subagentes](/es/sub-agents)          | Trabajadores delegados dentro de una sesión que realizan una tarea secundaria en su propio contexto y devuelven un resumen                                         | Una tarea secundaria inundaría su conversación principal con resultados de búsqueda, registros o contenidos de archivos que no volverá a consultar |
| [Vista de agentes](/es/agent-view)    | Una pantalla para enviar y monitorear sesiones que se ejecutan en segundo plano, abierta con `claude agents`. Vista previa de investigación                        | Tiene varias tareas independientes y desea delegarlas, verificar el estado de un vistazo e intervenir solo cuando una lo necesite                  |
| [Equipos de agentes](/es/agent-teams) | Múltiples sesiones coordinadas con una lista de tareas compartida y mensajería entre agentes, administradas por un líder. Experimental y deshabilitado por defecto | Desea que Claude divida un proyecto en partes, las asigne y mantenga a los trabajadores sincronizados                                              |
| [Worktrees](/es/worktrees)            | Checkouts de git separados para que las sesiones paralelas nunca toquen los archivos de los demás                                                                  | Está ejecutando varias sesiones usted mismo, o sus subagentes editan archivos superpuestos                                                         |
| [`/batch`](/es/commands)              | Una división planificada de un cambio grande en 5 a 30 subagentes aislados en worktree que cada uno abre una solicitud de extracción                               | Una migración en toda la repo o refactorización mecánica que puede describir en una instrucción                                                    |

En cada enfoque, los trabajadores son sesiones de Claude. Para involucrar una herramienta diferente, expóngala a Claude como un [servidor MCP](/es/mcp).

Puede combinar estos enfoques. La vista de agentes mueve automáticamente cada sesión enviada a su propio worktree cuando necesita editar archivos, y una sesión en la que está trabajando puede generar subagentes que cada uno obtenga su propio worktree.

<Note>
  Ejecutar varias sesiones o subagentes a la vez multiplica el uso de tokens. Consulte [Costos](/es/costs) para obtener detalles de uso y límites de velocidad.
</Note>

## Elija un enfoque

El enfoque correcto depende de quién coordina el trabajo, si los trabajadores necesitan comunicarse y si editan los mismos archivos:

* **¿Quién coordina el trabajo?** Si desea que Claude delegue y recopile resultados dentro de una conversación, use [subagentes](/es/sub-agents). Si está delegando tareas independientes y volviendo a verificarlas, use [vista de agentes](/es/agent-view). Si desea que Claude planifique, asigne y supervise un grupo de trabajadores, use [equipos de agentes](/es/agent-teams), que son experimentales y están deshabilitados por defecto.
* **¿Necesitan los trabajadores hablar entre sí?** Los subagentes reportan resultados nuevamente a la conversación que los generó, y las sesiones de vista de agentes reportan solo a usted. Los compañeros de equipo en un equipo de agentes comparten una lista de tareas y se envían mensajes directamente entre sí.
* **¿Tocan las tareas los mismos archivos?** Aísle el trabajo con [worktrees](/es/worktrees). Los subagentes y las sesiones que ejecuta usted mismo pueden usar cada uno un worktree separado. Los equipos de agentes no aíslan a los compañeros de equipo en worktrees, así que [particione el trabajo](/es/agent-teams#avoid-file-conflicts) para que cada compañero de equipo sea propietario de un conjunto diferente de archivos.

## Verifique el trabajo en ejecución

El comando para verificar el trabajo en ejecución depende de qué enfoque utilizó:

* Para sesiones en segundo plano, `claude agents` abre [vista de agentes](/es/agent-view): una pantalla que muestra cada sesión, su estado y cuáles necesitan su entrada.
* Para subagentes en la sesión actual, `/agents` abre un panel con una pestaña **Running** que enumera subagentes activos y una pestaña **Library** donde puede [crear y editar subagentes personalizados](/es/sub-agents#use-the-%2Fagents-command). A pesar del nombre similar, esto es separado de `claude agents`.
* Para cualquier cosa que se ejecute en segundo plano de la sesión actual, `/tasks` enumera cada elemento y le permite verificar, adjuntar o detener.

Para una vista de escritorio de todas sus sesiones, consulte [sesiones paralelas en la aplicación de escritorio](/es/desktop#work-in-parallel-with-sessions).

## Obtenga más información

Cada guía a continuación cubre la configuración y configuración para un enfoque:

* [Crear subagentes personalizados](/es/sub-agents): defina especialistas reutilizables y controle qué herramientas pueden usar.
* [Administrar agentes con vista de agentes](/es/agent-view): envíe sesiones, observe su estado y adjunte cuando una lo necesite.
* [Orquestar equipos de agentes](/es/agent-teams): configure un líder y compañeros de equipo, asigne tareas y revise su trabajo.
* [Ejecutar sesiones paralelas con worktrees](/es/worktrees): inicie Claude en un checkout aislado, controle qué se copia y limpie después.
