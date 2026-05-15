---
source_url: https://code.claude.com/docs/es/platforms
fetched_url: https://code.claude.com/docs/es/platforms.md
category: Primeros pasos
status: 200
scraped_at: 2026-05-15T14:27:30+00:00
sha256_16: 98724b580b2da664
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plataformas e integraciones

> Elija dónde ejecutar Claude Code y qué conectar. Compare la CLI, Desktop, VS Code, JetBrains, web, móvil e integraciones como Chrome, Slack e CI/CD.

Claude Code ejecuta el mismo motor subyacente en todas partes, pero cada superficie está optimizada para una forma diferente de trabajar. Esta página le ayuda a elegir la plataforma adecuada para su flujo de trabajo y conectar las herramientas que ya utiliza.

## Dónde ejecutar Claude Code

Elija una plataforma según cómo le guste trabajar y dónde viva su proyecto.

| Plataforma                        | Mejor para                                                                                                       | Lo que obtiene                                                                                                                                                                                       |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CLI](/es/quickstart)             | Flujos de trabajo de terminal, scripting, servidores remotos                                                     | Conjunto completo de características, [Agent SDK](/es/headless), [uso de computadora](/es/computer-use) en macOS (Pro y Max), proveedores de terceros                                                |
| [Desktop](/es/desktop)            | Revisión visual, sesiones paralelas, configuración administrada                                                  | Visor de diferencias, vista previa de aplicaciones, [uso de computadora](/es/desktop#let-claude-use-your-computer) y [Dispatch](/es/desktop#sessions-from-dispatch) en Pro y Max                     |
| [VS Code](/es/vs-code)            | Trabajar dentro de VS Code sin cambiar a una terminal                                                            | Diferencias en línea, terminal integrada, contexto de archivo                                                                                                                                        |
| [JetBrains](/es/jetbrains)        | Trabajar dentro de IntelliJ, PyCharm, WebStorm u otros IDE de JetBrains                                          | Visor de diferencias, intercambio de selección, sesión de terminal                                                                                                                                   |
| [Web](/es/claude-code-on-the-web) | Tareas de larga duración que no necesitan mucha dirección, o trabajo que debe continuar cuando está desconectado | Nube administrada por Anthropic, continúa después de desconectarse                                                                                                                                   |
| Móvil                             | Iniciar y monitorear tareas mientras está lejos de su computadora                                                | Sesiones en la nube desde la aplicación Claude para iOS y Android, [Remote Control](/es/remote-control) para sesiones locales, [Dispatch](/es/desktop#sessions-from-dispatch) a Desktop en Pro y Max |

La CLI es la superficie más completa para el trabajo nativo de terminal: scripting y el Agent SDK son solo CLI. Los proveedores de terceros también funcionan en [VS Code](/es/vs-code#use-third-party-providers). Las implementaciones empresariales de [Desktop](/es/desktop) admiten Vertex AI y proveedores de puerta de enlace; para Bedrock o Foundry, use la CLI o VS Code en lugar de Desktop. Desktop y las extensiones de IDE intercambian algunas características solo de CLI por revisión visual e integración más estrecha del editor. La web se ejecuta en la nube de Anthropic, por lo que las tareas continúan después de desconectarse. Móvil es un cliente delgado en esas mismas sesiones en la nube o en una sesión local a través de Remote Control, y puede enviar tareas a Desktop con Dispatch.

Puede mezclar superficies en el mismo proyecto. La configuración, la memoria del proyecto y los servidores MCP se comparten entre las superficies locales.

## Conecte sus herramientas

Las integraciones permiten que Claude trabaje con servicios fuera de su base de código.

| Integración                          | Qué hace                                         | Úselo para                                                                          |
| :----------------------------------- | :----------------------------------------------- | :---------------------------------------------------------------------------------- |
| [Chrome](/es/chrome)                 | Controla su navegador con sus sesiones iniciadas | Prueba de aplicaciones web, rellenar formularios, automatizar sitios sin una API    |
| [GitHub Actions](/es/github-actions) | Ejecuta Claude en su canalización de CI          | Revisiones automáticas de PR, clasificación de problemas, mantenimiento programado  |
| [GitLab CI/CD](/es/gitlab-ci-cd)     | Lo mismo que GitHub Actions para GitLab          | Automatización impulsada por CI en GitLab                                           |
| [Code Review](/es/code-review)       | Revisa automáticamente cada PR                   | Detectar errores antes de la revisión humana                                        |
| [Slack](/es/slack)                   | Responde a menciones de `@Claude` en sus canales | Convertir informes de errores en solicitudes de extracción desde el chat del equipo |

Para integraciones no listadas aquí, [servidores MCP](/es/mcp) y [conectores](/es/desktop#connect-external-tools) le permiten conectar casi cualquier cosa: Linear, Notion, Google Drive o sus propias API internas.

## Trabaje cuando está lejos de su terminal

Claude Code offers several ways to work when you're not at your terminal. They differ in what triggers the work, where Claude runs, and how much you need to set up.

|                                                | Trigger                                                                                        | Claude runs on                                                                               | Setup                                                                                                                                | Best for                                                      |
| :--------------------------------------------- | :--------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------ |
| [Dispatch](/en/desktop#sessions-from-dispatch) | Message a task from the Claude mobile app                                                      | Your machine (Desktop)                                                                       | [Pair the mobile app with Desktop](https://support.claude.com/en/articles/13947068)                                                  | Delegating work while you're away, minimal setup              |
| [Remote Control](/en/remote-control)           | Drive a running session from [claude.ai/code](https://claude.ai/code) or the Claude mobile app | Your machine (CLI or VS Code)                                                                | Run `claude remote-control`                                                                                                          | Steering in-progress work from another device                 |
| [Channels](/en/channels)                       | Push events from a chat app like Telegram or Discord, or your own server                       | Your machine (CLI)                                                                           | [Install a channel plugin](/en/channels#quickstart) or [build your own](/en/channels-reference)                                      | Reacting to external events like CI failures or chat messages |
| [Slack](/en/slack)                             | Mention `@Claude` in a team channel                                                            | Anthropic cloud                                                                              | [Install the Slack app](/en/slack#setting-up-claude-code-in-slack) with [Claude Code on the web](/en/claude-code-on-the-web) enabled | PRs and reviews from team chat                                |
| [Scheduled tasks](/en/scheduled-tasks)         | Set a schedule                                                                                 | [CLI](/en/scheduled-tasks), [Desktop](/en/desktop-scheduled-tasks), or [cloud](/en/routines) | Pick a frequency                                                                                                                     | Recurring automation like daily reviews                       |

Si no está seguro de por dónde empezar, [instale la CLI](/es/quickstart) y ejecútela en un directorio de proyecto. Si prefiere no usar una terminal, [Desktop](/es/desktop-quickstart) le proporciona el mismo motor con una interfaz gráfica.

## Recursos relacionados

### Plataformas

* [Inicio rápido de CLI](/es/quickstart): instale y ejecute su primer comando en la terminal
* [Desktop](/es/desktop): revisión visual de diferencias, sesiones paralelas, uso de computadora y Dispatch
* [VS Code](/es/vs-code): la extensión Claude Code dentro de su editor
* [JetBrains](/es/jetbrains): la extensión para IntelliJ, PyCharm y otros IDE de JetBrains
* [Claude Code en la web](/es/claude-code-on-the-web): sesiones en la nube que continúan ejecutándose cuando se desconecta
* Móvil: la aplicación Claude para [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) y [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude) para iniciar y monitorear tareas mientras está lejos de su computadora

### Integraciones

* [Chrome](/es/chrome): automatice tareas del navegador con sus sesiones iniciadas
* [Uso de computadora](/es/computer-use): permita que Claude abra aplicaciones y controle su pantalla en macOS
* [GitHub Actions](/es/github-actions): ejecute Claude en su canalización de CI
* [GitLab CI/CD](/es/gitlab-ci-cd): lo mismo para GitLab
* [Code Review](/es/code-review): revisión automática en cada solicitud de extracción
* [Slack](/es/slack): envíe tareas desde el chat del equipo, obtenga PR de vuelta

### Acceso remoto

* [Dispatch](/es/desktop#sessions-from-dispatch): envíe un mensaje con una tarea desde su teléfono y puede generar una sesión de Desktop
* [Remote Control](/es/remote-control): controle una sesión en ejecución desde su teléfono o navegador
* [Channels](/es/channels): envíe eventos desde aplicaciones de chat o sus propios servidores a una sesión
* [Scheduled tasks](/es/scheduled-tasks): ejecute indicaciones en un horario recurrente
