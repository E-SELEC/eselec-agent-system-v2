---
source_url: https://code.claude.com/docs/es/whats-new
fetched_url: https://code.claude.com/docs/es/whats-new.md
category: Novedades
status: 200
scraped_at: 2026-05-15T14:28:50+00:00
sha256_16: 11c3121609cebe4f
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Novedades

> Un resumen semanal de las características notables de Claude Code, con fragmentos de código, demostraciones y contexto sobre por qué importan.

El resumen semanal para desarrolladores destaca las características más propensas a cambiar la forma en que trabaja. Cada entrada incluye código ejecutable, una breve demostración y un enlace a la documentación completa. Para cada corrección de errores y mejora menor, consulte el [registro de cambios](/es/changelog).

<Update label="Week 19" description="May 4–8, 2026" tags={["v2.1.128–v2.1.136"]}>
  **Los plugins se cargan desde archivos `.zip` y URLs**: `--plugin-dir` ahora acepta archivos `.zip`, y `--plugin-url` obtiene un archivo de plugin para la sesión actual.

  También esta semana: **`worktree.baseRef`** elige si los nuevos worktrees se ramifican desde el remoto predeterminado o desde `HEAD` local; **reglas de negación dura en modo automático** bloquean acciones incondicionalmente independientemente de excepciones de permiso; y **los hooks ven el nivel de esfuerzo activo** a través de `effort.level` y `$CLAUDE_EFFORT`.

  [Lea el resumen de la Week 19 →](/es/whats-new/2026-w19)
</Update>

<Update label="Week 18" description="April 27 – May 1, 2026" tags={["v2.1.120–v2.1.126"]}>
  **Windows sin Git Bash**: Git para Windows ya no es necesario, y Claude Code usa PowerShell como herramienta de shell cuando Bash no está disponible.

  También esta semana: **`claude ultrareview`** trae revisión de código en la nube a CI y scripts; **`claude project purge`** limpia el estado local de un proyecto; y pegar una **URL de PR en `/resume`** encuentra la sesión que la creó.

  [Lea el resumen de la Week 18 →](/es/whats-new/2026-w18)
</Update>

<Update label="Week 17" description="April 20–24, 2026" tags={["v2.1.114–v2.1.119"]}>
  **`/ultrareview`** se abre como una vista previa de investigación pública: una flota de agentes cazadores de errores se ejecuta en la nube y los hallazgos llegan automáticamente a su CLI o Desktop.

  También esta semana: **session recap** le muestra qué sucedió mientras una terminal no estaba enfocada; **custom themes** le permite crear y enviar paletas de colores desde `/theme` o un plugin; y **Claude Code en la web** recibe un rediseño con una nueva barra lateral de sesiones y diseño de arrastrar y soltar.

  [Lea el resumen de la Week 17 →](/es/whats-new/2026-w17)
</Update>

<Update label="Week 16" description="April 13–17, 2026" tags={["v2.1.105–v2.1.113"]}>
  **Claude Opus 4.7** llega como el nuevo predeterminado en Max y Team Premium, con un nuevo nivel de esfuerzo `xhigh` que es la configuración recomendada para la mayoría del trabajo de codificación y un control deslizante interactivo `/effort` para ajustarlo.

  También esta semana: **Routines** en Claude Code en la web disparan agentes en la nube con plantillas desde una programación, evento de GitHub o llamada API; **notificaciones push móviles** le avisan a su teléfono cuando una tarea larga finaliza o Claude lo necesita; `/usage` muestra qué está impulsando sus límites; y la CLI se traslada a binarios nativos.

  [Lea el resumen de la Week 16 →](/es/whats-new/2026-w16)
</Update>

<Update label="Week 15" description="April 6–10, 2026" tags={["v2.1.92–v2.1.101"]}>
  **Ultraplan** entra en vista previa temprana: redacte un plan en la nube desde su CLI, revíselo y comente en un editor web, luego ejecútelo de forma remota o extráigalo localmente. La primera ejecución ahora crea automáticamente un entorno en la nube para usted.

  También esta semana: la herramienta **Monitor** transmite eventos de fondo a la conversación para que Claude pueda monitorear registros y reaccionar en vivo, `/loop` se autoajusta cuando omite el intervalo, `/team-onboarding` empaqueta su configuración en una guía reproducible, y `/autofix-pr` activa la corrección automática de PR desde su terminal.

  [Lea el resumen de la Week 15 →](/es/whats-new/2026-w15)
</Update>

<Update label="Week 14" description="March 30 – April 3, 2026" tags={["v2.1.86–v2.1.91"]}>
  **Computer use** llega a la CLI en vista previa de investigación: Claude puede abrir aplicaciones nativas, hacer clic en la interfaz de usuario y verificar cambios desde su terminal. Lo mejor para cerrar el ciclo en cosas que solo una GUI puede verificar.

  También esta semana: lecciones interactivas `/powerup`, renderizado de pantalla alternativa sin parpadeos, una anulación de tamaño de resultado MCP por herramienta de hasta 500K, y ejecutables de plugin en la `PATH` de la herramienta Bash.

  [Lea el resumen de la Week 14 →](/es/whats-new/2026-w14)
</Update>

<Update label="Week 13" description="March 23–27, 2026" tags={["v2.1.83–v2.1.85"]}>
  **Auto mode** llega en vista previa de investigación: un clasificador maneja sus solicitudes de permiso para que las acciones seguras se ejecuten sin interrupción y las arriesgadas se bloqueen. El término medio entre aprobar todo y `--dangerously-skip-permissions`.

  También esta semana: uso de computadora en la aplicación Desktop, corrección automática de PR en Web, búsqueda de transcripción con `/`, una herramienta PowerShell nativa para Windows, y hooks `if` condicionales.

  [Lea el resumen de la Week 13 →](/es/whats-new/2026-w13)
</Update>
