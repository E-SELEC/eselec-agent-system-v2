---
source_url: https://code.claude.com/docs/es/agent-view
fetched_url: https://code.claude.com/docs/es/agent-view.md
category: Crear con Claude Code, agentes y automatizacion
status: 200
scraped_at: 2026-05-15T14:27:40+00:00
sha256_16: fb9e29a443049868
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Gestionar múltiples agentes con la vista de agentes

> Distribuya y gestione muchas sesiones de Claude Code desde una pantalla. La vista de agentes muestra qué está haciendo cada sesión y cuáles necesitan su entrada.

La vista de agentes, abierta con `claude agents`, es una pantalla para todas sus sesiones en segundo plano: qué se está ejecutando, qué necesita su entrada y qué está hecho. Distribuya nuevas sesiones, observe su estado de un vistazo en lugar de desplazarse por transcripciones, e intervenga solo cuando una lo necesite. Cada sesión en segundo plano es una conversación completa de Claude Code que sigue ejecutándose sin una terminal conectada, por lo que puede abrirla, responder y marcharse cuando quiera.

<img src="https://mintcdn.com/claude-code/1B48Qz2Z9hac4SLG/images/agent-view-light.png?fit=max&auto=format&n=1B48Qz2Z9hac4SLG&q=85&s=7a186c96ed47d6700d084d77e786be65" className="dark:hidden" alt="Vista de agentes en una terminal: el encabezado muestra Claude Code v2.1.140, el modelo, el directorio de trabajo y un recuento de resumen. Las sesiones se agrupan bajo Necesita entrada, Trabajando y Completado, con una entrada de distribución en la parte inferior y un pie de página de sugerencias de teclado." width="1772" height="780" data-path="images/agent-view-light.png" />

<img src="https://mintcdn.com/claude-code/1B48Qz2Z9hac4SLG/images/agent-view-dark.png?fit=max&auto=format&n=1B48Qz2Z9hac4SLG&q=85&s=a5bed7434bae368faea3a8f023b52aa2" className="hidden dark:block" alt="Vista de agentes en una terminal: el encabezado muestra Claude Code v2.1.140, el modelo, el directorio de trabajo y un recuento de resumen. Las sesiones se agrupan bajo Necesita entrada, Trabajando y Completado, con una entrada de distribución en la parte inferior y un pie de página de sugerencias de teclado." width="1772" height="780" data-path="images/agent-view-dark.png" />

Utilice la vista de agentes cuando tenga varias tareas independientes en las que Claude pueda trabajar sin que usted observe cada paso. Distribuya una corrección de errores, una revisión de solicitud de extracción y una investigación de prueba inestable como tres filas, continúe trabajando en otra ventana y verifique cuando una fila muestre que la necesita o tenga un resultado.

Cuando desee trabajar de forma más directa en la sesión de cualquier agente, conéctese a la fila para entrar en la conversación completa.

Para comparar la vista de agentes con subagentes, equipos de agentes y worktrees, consulte [Ejecutar agentes en paralelo](/es/agents).

<Note>
  La vista de agentes es una vista previa de investigación y requiere Claude Code v2.1.139 o posterior. Verifique su versión con `claude --version`. La interfaz y los atajos de teclado pueden cambiar a medida que la función evoluciona.
</Note>

Esta página cubre:

* [Inicio rápido](#quick-start): asigne a Claude una tarea para trabajar en segundo plano, verifique su estado e intervenga cuando sea necesario
* [Monitorear sesiones con la vista de agentes](#monitor-sessions-with-agent-view), incluidos iconos de estado, vista previa y respuesta, conexión, organización y atajos de teclado
* [Distribuir nuevos agentes](#dispatch-new-agents) desde la vista de agentes, desde dentro de una sesión o desde su shell
* [Gestionar sesiones desde el shell](#manage-sessions-from-the-shell)
* [Cómo se alojan las sesiones en segundo plano](#how-background-sessions-are-hosted) por el proceso supervisor

## Inicio rápido

Este tutorial cubre el bucle principal de la vista de agentes: distribuir una tarea, observar cómo se actualiza su fila mientras Claude trabaja, echar un vistazo para verificar y responder, y conectarse para la conversación completa. La sesión que distribuye sigue ejecutándose después de cerrar la vista de agentes, por lo que puede irse y volver a ella.

<Steps>
  <Step title="Abrir la vista de agentes">
    Desde su shell, ejecute:

    ```bash theme={null}
    claude agents
    ```

    La vista de agentes se abre con una entrada en la parte inferior y una tabla que se completa a medida que comienzan las sesiones. Presione `Esc` en cualquier momento para volver a su shell. Sus sesiones siguen ejecutándose mientras está fuera y reaparecen la próxima vez que abra la vista de agentes.
  </Step>

  <Step title="Distribuir una sesión">
    Escriba un mensaje describiendo una tarea y presione `Enter`. Una nueva sesión en segundo plano comienza en esa tarea y aparece como una fila que muestra si está funcionando, esperando su entrada o está hecha. La nueva sesión utiliza el modelo mostrado en el encabezado de la vista de agentes y el mismo [modo de permisos](#permission-mode-model-and-effort) que obtendría ejecutando `claude` en ese directorio.

    Cada mensaje que ingrese aquí inicia su propia sesión nueva. Escribir otro mensaje y presionar `Enter` lanza una segunda sesión junto a la primera en lugar de enviar una continuación a ella. Puede ejecutar varias en paralelo de esta manera.

    Cada sesión utiliza su cuota de suscripción de forma independiente, así que consulte [Limitaciones](#limitations) antes de distribuir muchas a la vez.
  </Step>

  <Step title="Echar un vistazo y responder">
    Seleccione una fila con las teclas de flecha y presione `Space` para abrir el panel de vista previa. Muestra la salida más reciente de la sesión, o la pregunta en la que está esperando, en lugar de la transcripción completa. Escriba una respuesta y presione `Enter` para enviarla sin salir de la vista de agentes.
  </Step>

  <Step title="Conectar y desconectar">
    Presione `Enter` o `→` en una fila para conectarse cuando desee la conversación completa. La sesión toma el control de la terminal exactamente como si hubiera ejecutado `claude`. Presione `←` en un mensaje vacío para desconectarse y volver a la tabla.
  </Step>

  <Step title="Traer una sesión existente">
    Para mover una sesión que ya tiene abierta a la vista de agentes, ejecute `/bg` dentro de ella, o presione `←` en un mensaje vacío para enviarla al segundo plano y abrir la vista de agentes en un paso. La sesión sigue ejecutándose y aparece como una fila junto a las que distribuyó.
  </Step>
</Steps>

Puede usar `claude agents` como su punto de entrada principal en lugar de `claude`: distribuya cada tarea desde la vista de agentes, conéctese cuando desee la conversación completa, y presione `←` para volver a la tabla.

## Monitorear sesiones con la vista de agentes

Ejecute `claude agents` para abrir la vista de agentes. Toma el control de la terminal completa y enumera cada sesión agrupada por estado, con sesiones fijadas y las que lo necesitan en la parte superior. Cada fila muestra el nombre de la sesión, la actividad actual y cuánto tiempo hace que cambió por última vez.

La lista cubre cada sesión en segundo plano que ha iniciado, en todos sus proyectos. Una sesión que trabaja en un repositorio y otra en un worktree diferente aparecen aquí, independientemente de qué directorio abrió la vista de agentes. Las sesiones interactivas que tiene abiertas en otras terminales no aparecen hasta que las [envíe al segundo plano](#from-inside-a-session). Los [subagentes](/es/sub-agents) y [compañeros de equipo](/es/agent-teams) que una sesión genera no se enumeran como filas separadas.

Para limitar la vista a un proyecto, inicie con `claude agents --cwd <path>`. Solo aparecen las sesiones iniciadas en ese directorio, incluidas las que se ejecutan en un [worktree](/es/worktrees) distribuido desde él.

```text theme={null}
Pinned
  ✽ clawd walk cycle          Write assets/sprites/clawd-walk.png           3m

Ready for review
  ∙ jump physics              github.com/example/game/pull/2048          ●  2h

Needs input
  ✻ power-up design           needs input: double jump or wall climb?       1m

Working
  ✽ collision detection       Edit src/physics/CollisionSystem.ts           2m
  ✢ playtest level 3          run 12 · all checkpoints cleared           in 4m

Completed
  ✻ title screen              result: menu, options, and credits done       9m
  ∙ sound effects             result: 14 SFX exported to assets/audio       4h
  … 6 more
```

### Leer el estado de la sesión

Cada fila comienza con un icono cuyo color y animación muestran el estado de la sesión:

| Estado           | El icono se muestra como | Qué significa                                                                       |
| :--------------- | :----------------------- | :---------------------------------------------------------------------------------- |
| Funcionando      | Animado                  | Claude está ejecutando activamente herramientas o generando una respuesta           |
| Necesita entrada | Amarillo                 | Claude está esperando una pregunta específica o una decisión de permiso de su parte |
| Inactivo         | Atenuado                 | La sesión no tiene nada que hacer y está lista para su próximo mensaje              |
| Completado       | Verde                    | La tarea se completó exitosamente                                                   |
| Falló            | Rojo                     | La tarea terminó con un error                                                       |
| Detenido         | Gris                     | La sesión fue detenida con `Ctrl+X` o `claude stop`                                 |

Por separado, la forma del icono muestra si el proceso subyacente está ejecutándose:

| Forma             | Qué significa                                                                                                                          |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| `✻` o `✽` animado | El proceso de la sesión está activo y responde inmediatamente                                                                          |
| `∙`               | El proceso ha salido. Aún puede echar un vistazo, responder o conectarse, y Claude reinicia desde donde se quedó                       |
| `✢`               | Una sesión [`/loop`](/es/scheduled-tasks) durmiendo entre iteraciones. La fila muestra su recuento de ejecución y una cuenta regresiva |

Las sesiones en segundo plano no necesitan ninguna terminal abierta para seguir funcionando. Un [proceso supervisor](#the-supervisor-process) separado las ejecuta, por lo que puede cerrar la vista de agentes, cerrar su shell o iniciar una nueva sesión interactiva y su trabajo distribuido sigue adelante.

El estado de la sesión persiste en el disco a través de actualizaciones automáticas y reinicios del supervisor. Si su máquina se duerme o se apaga, las sesiones en ejecución se detienen; reinícielas con `claude respawn --all`.

### Resúmenes de filas

El resumen de una línea en cada fila es generado por un [modelo de clase Haiku](/es/model-config) para que la fila pueda decirle qué está haciendo la sesión, qué necesita o qué produjo sin abrir la transcripción. Mientras una sesión está funcionando activamente, el resumen se actualiza como máximo una vez cada 15 segundos, más una vez cuando cada turno termina.

Cada actualización es una solicitud corta de clase Haiku a través de su proveedor normal, facturada y manejada bajo los mismos [términos de uso de datos](/es/data-usage) que la sesión misma.

### Estado de la solicitud de extracción

Cuando una sesión abre una solicitud de extracción, aparece un punto de estado en el borde derecho de la fila, vinculado a la solicitud de extracción en terminales que admiten hipervínculos. Cuando la sesión ha abierto más de una solicitud de extracción, el recuento aparece antes del punto y el color refleja cuál necesita más atención.

| Color del punto | Estado de la solicitud de extracción                               |
| :-------------- | :----------------------------------------------------------------- |
| Amarillo        | Esperando verificaciones o revisión, o las verificaciones fallaron |
| Verde           | Las verificaciones pasaron y ninguna revisión está bloqueando      |
| Púrpura         | Fusionado                                                          |
| Gris            | Borrador o cerrado                                                 |

Para la mayoría de las tareas, esta fila es donde recopila el resultado: revise y fusione la solicitud de extracción cuando el punto se vuelva verde.

### Echar un vistazo y responder

Presione `Space` en una fila seleccionada para abrir el panel de vista previa. Muestra qué necesita la sesión de usted, su salida más reciente y cualquier solicitud de extracción que haya abierto. La mayoría de las veces esto es suficiente, y nunca necesita abrir la transcripción completa.

Escriba una respuesta en el panel de vista previa y presione `Enter` para enviarla a esa sesión. Cuando la sesión está haciendo una pregunta de opción múltiple, el panel de vista previa muestra las opciones y puede presionar una tecla numérica para elegir una. Para otras sesiones bloqueadas, presione `Tab` para llenar la entrada con una respuesta sugerida que puede editar antes de enviar. Prefije una respuesta con `!` para enviar un comando Bash en su lugar.

Use `↑` y `↓` para echar un vistazo a sesiones adyacentes sin cerrar el panel, o `→` para conectarse.

### Conectarse a una sesión

Presione `Enter` o `→` en una fila seleccionada para conectarse. La vista de agentes es reemplazada por la sesión interactiva completa, exactamente como si hubiera ejecutado `claude` en ese directorio. Cuando se conecta, Claude publica un breve resumen de lo que sucedió mientras estaba fuera.

Mientras está conectado, la sesión se comporta como cualquier otra sesión de Claude Code: cada [comando](/es/commands), atajo de teclado y función funciona.

Presione `←` en un mensaje vacío para desconectarse y volver a la vista de agentes. Si un diálogo tiene el enfoque y no responde a `←`, presione `Ctrl+Z` para desconectarse inmediatamente.

Desconectarse nunca detiene una sesión en segundo plano: `←`, `Ctrl+C`, `Ctrl+D`, `Ctrl+Z` y `/exit` la dejan ejecutándose. Para terminar una sesión desde dentro de ella, ejecute `/stop`.

Después de haber distribuido o enviado una sesión al segundo plano, presionar `←` en un mensaje vacío funciona desde cualquier sesión de Claude Code, no solo desde las que se conectó desde la vista de agentes. Envía la sesión actual al segundo plano y abre la vista de agentes con esa sesión preseleccionada, por lo que puede cambiar de sesión sin salir de la terminal. Puede desactivar este atajo en `/config`.

### Organizar la lista

La vista de agentes agrupa sesiones para que las que necesitan entrada estén en la parte superior, con `Ready for review` y `Needs input` por encima de `Working` y `Completed`. Estos nombres de grupo no se asignan uno a uno a los [estados](#read-session-state) anteriores: una sesión se mueve a `Ready for review` cuando tiene una solicitud de extracción abierta, y `Completed` recopila sesiones terminadas, fallidas y detenidas juntas. Presione `Ctrl+S` para agrupar por directorio en su lugar. Su elección persiste entre ejecuciones.

Dentro de un grupo:

* Presione `Ctrl+T` para fijar una sesión en la parte superior
* Presione `Shift+↑` o `Shift+↓` para reordenar sesiones
* Presione `Ctrl+R` para renombrar una sesión
* Presione `Enter` en un encabezado de grupo para contraerlo

Para eliminar una sesión de la lista, presione `Ctrl+X` para detenerla y `Ctrl+X` nuevamente dentro de dos segundos para eliminarla. Presionar `Ctrl+X` en un encabezado de grupo elimina cada sesión en ese grupo después de la confirmación.

Eliminar elimina la sesión de la vista de agentes y limpia su [worktree](#how-file-edits-are-isolated), incluidos los cambios sin confirmar en ella, por lo que envíe o confirme el trabajo que desea conservar antes de eliminar. La transcripción de la conversación permanece en el disco y sigue siendo accesible a través de `claude --resume`.

Las sesiones completadas más antiguas se pliegan en una fila `… N more` para mantener la lista corta. Los fallos y las sesiones con una solicitud de extracción abierta siempre permanecen visibles.

### Filtrar sesiones

Escriba en la entrada de distribución para filtrar en lugar de distribuir:

| Filtro                      | Muestra                                                                                                     |
| :-------------------------- | :---------------------------------------------------------------------------------------------------------- |
| `a:<name>`                  | Sesiones que ejecutan el agente nombrado                                                                    |
| `s:<state>`                 | Sesiones en el estado dado, como `s:working`. También acepta `s:blocked` para todo lo que lo espera a usted |
| `#<number>` o una URL de PR | La sesión que trabaja en esa solicitud de extracción                                                        |

### Atajos de teclado

Presione `?` en la vista de agentes para ver cada atajo en contexto. La tabla a continuación los resume.

| Atajo                 | Acción                                                                                                |
| :-------------------- | :---------------------------------------------------------------------------------------------------- |
| `↑` / `↓`             | Moverse entre filas                                                                                   |
| `Enter`               | Conectarse a la sesión seleccionada, o distribuir si hay texto en la entrada                          |
| `Space`               | Abrir o cerrar el panel de vista previa para la sesión seleccionada                                   |
| `Shift+Enter`         | Distribuir y conectarse inmediatamente                                                                |
| `→`                   | Conectarse a la sesión seleccionada                                                                   |
| `Alt+1`..`Alt+9`      | Conectarse a la sesión 1–9 en el grupo actual                                                         |
| `Tab`                 | En una entrada vacía, examinar todos los subagentes. De lo contrario, aplicar la sugerencia resaltada |
| `Ctrl+S`              | Cambiar agrupación entre estado y directorio                                                          |
| `Ctrl+T`              | Fijar o desfijar la sesión seleccionada                                                               |
| `Ctrl+R`              | Renombrar la sesión seleccionada                                                                      |
| `Ctrl+G`              | Abrir el mensaje de distribución en su `$EDITOR`                                                      |
| `Ctrl+X`              | Detener la sesión; presione nuevamente dentro de dos segundos para eliminarla                         |
| `Shift+↑` / `Shift+↓` | Reordenar la sesión seleccionada                                                                      |
| `Esc`                 | Cerrar el panel de vista previa, limpiar la entrada o salir                                           |
| `Ctrl+C`              | Limpiar la entrada; presione dos veces para salir                                                     |
| `?`                   | Mostrar todos los atajos                                                                              |

## Distribuir nuevos agentes

Puede distribuir nuevas sesiones en segundo plano desde la vista de agentes, enviar una sesión interactiva existente al segundo plano o iniciar una directamente desde el shell.

### Desde la vista de agentes

Escriba un mensaje en la entrada en la parte inferior de la vista de agentes y presione `Enter` para iniciar una nueva sesión en segundo plano. La sesión se nombra automáticamente a partir del mensaje; renómbrela más tarde con `Ctrl+R`.

Pegue una imagen en el mensaje para incluir una captura de pantalla o diagrama con la tarea.

Prefije o mencione partes del mensaje para controlar cómo comienza la sesión:

| Entrada                                          | Efecto                                                                                                                                                                                           |
| :----------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `<agent-name> <prompt>`                          | Si la primera palabra coincide con un nombre de [subagente](/es/sub-agents) personalizado, ese subagente se ejecuta como el agente principal de la sesión con la configuración de su frontmatter |
| `@<agent-name>`                                  | Mencione un subagente personalizado en cualquier lugar del mensaje para ejecutarlo como el agente principal                                                                                      |
| `@<repo>`                                        | Mencione un repositorio bajo el directorio desde el que abrió la vista de agentes para ejecutar la sesión allí                                                                                   |
| `/<skill>`                                       | Sugiera [skills](/es/skills) para distribuir como el mensaje                                                                                                                                     |
| `#<number>` o una URL de solicitud de extracción | Si una sesión ya está trabajando en ese PR, selecciónela en lugar de distribuir                                                                                                                  |
| `Shift+Enter`                                    | Distribuya e inmediatamente conéctese a la nueva sesión                                                                                                                                          |

Empaquetar una tarea recurrente como un [skill](/es/skills) le permite iniciar el mismo flujo de trabajo desde la vista de agentes repetidamente sin reescribir el mensaje.

Cuando el mismo `@name` coincide tanto con un subagente como con un repositorio hermano, el subagente tiene prioridad. La coincidencia de primera palabra sin `@` también se aplica, por lo que un mensaje que comienza con uno de sus nombres de subagente distribuye ese subagente en lugar de tratar la palabra como texto plano. Use la forma `@` cuando desee ser explícito, o comience el mensaje con una palabra diferente para evitar la coincidencia.

#### Distribuir a un directorio específico

Una nueva sesión se ejecuta en el directorio desde el que abrió la vista de agentes. Para dirigirse a un directorio diferente:

* Abra `claude agents` en ese directorio.
* Abra `claude agents` en un directorio padre que contenga varios repositorios y mencione uno con `@<repo>` en el mensaje para ejecutar la sesión allí.
* Desde el shell, `cd` al directorio y ejecute `claude --bg "<prompt>"`.

Cuando la vista de agentes se agrupa por directorio, el directorio de la fila resaltada se convierte en el objetivo de distribución, por lo que puede desplazarse a un grupo y distribuir en él sin reescribir la ruta.

### Desde dentro de una sesión

Ejecute `/background` o su alias `/bg` para mover la conversación actual a una sesión en segundo plano. Pase un mensaje como `/bg run the test suite and fix any failures` para dar una instrucción más primero.

Enviar al segundo plano desde una sesión interactiva inicia un proceso nuevo que se reanuda desde la conversación guardada, por lo que ejecutar subagentes, [monitores](/es/tools-reference#monitor-tool) y comandos en segundo plano no se transfieren a él. Claude le pide que confirme antes de enviar al segundo plano cuando alguno está en ejecución. Una vez en segundo plano, la sesión puede iniciar nuevos subagentes, monitores y comandos en segundo plano, y esos continúan ejecutándose en desconexiones y reconexiones posteriores.

### Desde su shell

Pase `--bg` para iniciar una sesión que vaya directamente al segundo plano:

```bash theme={null}
claude --bg "investigate the flaky SettingsChangeDetector test"
```

Para ejecutar un subagente específico como el agente principal de la sesión, combine `--bg` con `--agent`:

```bash theme={null}
claude --agent code-reviewer --bg "address review comments on PR 1234"
```

Pase `--name` para establecer el nombre de visualización de la sesión en la vista de agentes en lugar del generado automáticamente:

```bash theme={null}
claude --bg --name "flaky-test-fix" "investigate the flaky SettingsChangeDetector test"
```

Después de enviar al segundo plano, Claude imprime el ID corto de la sesión y los comandos para administrarla:

```text theme={null}
backgrounded · 7c5dcf5d
  claude agents             list sessions
  claude attach 7c5dcf5d    open in this terminal
  claude logs 7c5dcf5d      show recent output
  claude stop 7c5dcf5d      stop this session
```

### Cómo se aíslan las ediciones de archivos

Cada sesión en segundo plano, ya sea iniciada desde la vista de agentes, `/bg` o `claude --bg`, comienza en su directorio de trabajo. Antes de editar archivos, Claude mueve la sesión a un [git worktree](/es/worktrees) aislado bajo `.claude/worktrees/`, de modo que las sesiones paralelas pueden leer el mismo checkout pero cada una escribe en la suya propia. Claude omite esto cuando la sesión ya está bajo `.claude/worktrees/`, cuando el directorio de trabajo no es un repositorio git, o para escrituras fuera del directorio de trabajo.

Fuera de un repositorio git, las sesiones escriben en el directorio de trabajo directamente y no están aisladas entre sí, por lo que evite distribuir sesiones paralelas que editen los mismos archivos.

El worktree se elimina cuando elimina la sesión, por lo que fusione o envíe los cambios que desee mantener antes de eliminar. Para encontrar la ruta del worktree de una sesión, eche un vistazo a la sesión o conéctese y verifique su directorio de trabajo.

Para hacer que un subagente siempre se ejecute en su propio worktree independientemente de cómo se inició, establezca [`isolation: worktree`](/es/sub-agents#supported-frontmatter-fields) en su frontmatter.

### Establecer el modelo

El nombre del modelo mostrado en el encabezado de la vista de agentes es el valor predeterminado de distribución. Las nuevas sesiones que inicia desde la entrada utilizan este modelo, que es la misma configuración que [`/model`](/es/model-config) controla en cualquier sesión. Para anularlo para toda la sesión de vista de agentes, pase `--model` al abrir la vista de agentes. Consulte [Modo de permiso, modelo y esfuerzo](#permission-mode-model-and-effort).

Cada sesión en segundo plano puede ejecutarse en un modelo diferente. Para anularlo para una sesión:

* Desde el shell, pase `--model` con `claude --bg`.
* Conéctese a una sesión en ejecución y ejecute `/model` allí. El cambio persiste si la sesión se reinicia.
* Distribuya un [subagente](/es/sub-agents) cuyo frontmatter establezca un campo `model`.

### Modo de permiso, modelo y esfuerzo

Una sesión en segundo plano lee su [configuración](/es/settings) desde el directorio en el que se ejecuta, igual que si hubiera iniciado `claude` allí.

El [modo de permiso](/es/permissions) depende de cómo inició la sesión. Enviar al segundo plano una sesión existente con `/bg` o `←` mantiene el modo de permiso actual, por lo que una sesión que cambió a `acceptEdits` o `auto` permanece en ese modo después de desconectarse. Distribuir desde la entrada de la vista de agentes o ejecutar `claude --bg` desde su shell utiliza el `defaultMode` de la configuración de ese directorio, o el `permissionMode` del [frontmatter del subagente distribuido](/es/sub-agents#supported-frontmatter-fields).

Para establecer valores predeterminados para cada sesión que distribuya desde la vista de agentes, pase cualquiera de `--permission-mode`, `--model` o `--effort` al abrirla:

```bash theme={null}
claude agents --permission-mode plan --model opus --effort high
```

<Note>
  Pasar `--permission-mode`, `--model` o `--effort` a `claude agents` requiere Claude Code v2.1.142 o posterior. Las versiones anteriores rechazan estas banderas con un error de opción desconocida.
</Note>

Los valores predeterminados activos aparecen en el pie de página debajo de la entrada de distribución.

Sin estas banderas, la sesión utiliza el `defaultMode` de la configuración de ese directorio o el `permissionMode` del [frontmatter del subagente distribuido](/es/sub-agents#supported-frontmatter-fields), y el modelo mostrado en el encabezado de la vista de agentes.

El uso de `bypassPermissions` o `auto` se rechaza hasta que haya aceptado ese modo ejecutando `claude` con él una vez de forma interactiva, ya que esos modos permiten que una sesión que no está viendo actúe sin aprobación. Lo mismo se aplica si pasa el modo a `claude agents` o a `claude --bg --permission-mode`.

### Configuración, plugins y servidores MCP

La vista de agentes acepta las mismas banderas de configuración que `claude` para cargar configuración, plugins, servidores MCP y directorios adicionales. Cada bandera se aplica a la vista de agentes en sí y se pasa a cada sesión que distribuya desde ella, por lo que un plugin o servidor MCP que cargue de esta manera está disponible en esas sesiones también.

| Bandera                                                                                          | Efecto                                                                             |
| :----------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| [`--settings <file-or-json>`](/es/settings)                                                      | Anule la configuración para la vista de agentes y las sesiones distribuidas        |
| [`--add-dir <path>`](/es/permissions#additional-directories-grant-file-access-not-configuration) | Otorgue acceso a archivos a un directorio adicional                                |
| [`--plugin-dir <path>`](/es/plugins)                                                             | Cargue un plugin desde un directorio local                                         |
| [`--mcp-config <file-or-json>`](/es/mcp)                                                         | Cargue servidores MCP desde un archivo de configuración o cadena JSON              |
| `--strict-mcp-config`                                                                            | Use solo los servidores MCP de `--mcp-config`, ignorando otra configuración de MCP |

Repita `--add-dir`, `--plugin-dir` o `--mcp-config` una vez por valor. La forma separada por espacios, como `--add-dir a b c`, no es compatible con `claude agents`.

El siguiente ejemplo abre la vista de agentes con una anulación de configuración y un directorio adicional:

```bash theme={null}
claude agents --settings ./ci-settings.json --add-dir ../shared-lib
```

## Gestionar sesiones desde el shell

Cada sesión en segundo plano tiene un ID corto que puede usar desde el shell. El ID se imprime cuando inicia una sesión con `claude --bg`, y el ID de cada sesión es su nombre de directorio bajo `~/.claude/jobs/`. Estos comandos son útiles para scripting o cuando no desea abrir la vista de agentes.

| Comando                | Propósito                                                                           |
| :--------------------- | :---------------------------------------------------------------------------------- |
| `claude agents`        | Abrir la vista de agentes                                                           |
| `claude attach <id>`   | Conectarse a una sesión en esta terminal                                            |
| `claude logs <id>`     | Imprimir la salida reciente de la sesión                                            |
| `claude stop <id>`     | Detener una sesión. También acepta `claude kill`                                    |
| `claude respawn <id>`  | Reiniciar una sesión detenida con su conversación intacta                           |
| `claude respawn --all` | Reiniciar cada sesión detenida                                                      |
| `claude rm <id>`       | Eliminar una sesión de la lista. Limpia su worktree si no hay cambios sin confirmar |

## Cómo se alojan las sesiones en segundo plano

Cada sesión listada en la vista de agentes se considera una sesión en segundo plano, independientemente de si está actualmente conectado a ella. Por el contrario, una sesión iniciada ejecutando `claude` directamente está vinculada a esa terminal y finaliza cuando se cierra, a menos que la [envíe al segundo plano](#from-inside-a-session).

### El proceso supervisor

Las sesiones en segundo plano se alojan mediante un proceso supervisor por usuario, separado de su terminal y de la vista de agentes. Se inicia automáticamente la primera vez que envía una sesión al segundo plano o abre la vista de agentes, y no lo administra directamente.

El supervisor y sus sesiones se autentican con las mismas credenciales que sus sesiones interactivas y no realizan conexiones de red adicionales más allá de la API del modelo.

Cada sesión en segundo plano es su propio proceso de Claude Code, administrado por el supervisor en lugar de estar vinculado a su terminal. Una sesión que está funcionando activamente, esperando su entrada o tiene una terminal conectada mantiene su proceso ejecutándose.

Una vez que una sesión finaliza y permanece sin conectar durante aproximadamente una hora, el supervisor detiene su proceso para liberar recursos. La transcripción y el estado permanecen en el disco, y la próxima vez que se conecte, eche un vistazo o responda, el supervisor inicia un proceso nuevo desde donde se quedó. Cuando cada sesión ha finalizado y no hay terminal conectada, el supervisor mismo sale e inicia nuevamente la próxima vez que lo necesite.

El supervisor observa el binario de Claude Code instalado en el disco y se reinicia en la nueva versión después de que el [actualizador automático](/es/setup#auto-updates) regular lo reemplace. Esta es una observación de archivo local, no una verificación de red. Las sesiones en segundo plano son procesos desconectados, por lo que siguen ejecutándose durante el reinicio y el nuevo supervisor se reconecta a ellas.

### Dónde se almacena el estado

El estado de la sesión se almacena en su directorio de configuración de Claude Code. Si establece [`CLAUDE_CONFIG_DIR`](/es/env-vars), el supervisor usa ese directorio en lugar de `~/.claude` y se ejecuta como una instancia separada con sus propias sesiones.

| Ruta                             | Contenidos                                                                                          |
| :------------------------------- | :-------------------------------------------------------------------------------------------------- |
| `~/.claude/daemon.log`           | Registro del supervisor                                                                             |
| `~/.claude/daemon/roster.json`   | Lista de sesiones en segundo plano en ejecución, utilizada para reconectarse después de un reinicio |
| `~/.claude/jobs/<id>/state.json` | Estado por sesión mostrado en la vista de agentes                                                   |

### Desactivar la vista de agentes

Para desactivar completamente los agentes en segundo plano y la vista de agentes, establezca la configuración `disableAgentView` [setting](/es/settings) en `true` o establezca la variable de entorno `CLAUDE_CODE_DISABLE_AGENT_VIEW`. Los administradores pueden aplicar esto a través de [configuraciones administradas](/es/permissions#managed-settings).

## Solución de problemas

### `claude agents` enumera subagentes en lugar de abrir la vista de agentes

Si `claude agents` imprime un recuento seguido de sus subagentes configurados y luego sale, la vista de agentes no está disponible en su entorno. Las versiones anteriores no abrían la vista de agentes en todos los entornos, incluyendo cuando se conecta a través de Bedrock, Vertex AI o Foundry. Ejecute `claude update` para instalar la versión más reciente.

Si la vista de agentes aún no se abre después de actualizar, verifique si ha sido [desactivada](#turn-off-agent-view) por una configuración o variable de entorno.

### La vista de agentes se abre sin sesiones

La vista de agentes está vacía hasta que distribuya su primera sesión. Escriba un mensaje en la entrada en la parte inferior y presione `Enter`.

### No se pueden abrir agentes porque hay tareas en segundo plano en ejecución

Si presionar `←` para poner en segundo plano la sesión actual muestra `Cannot open agents — N background task(s) running`, la sesión tiene trabajo en vuelo como un subagente, un flujo de trabajo o un comando de shell en segundo plano, y el atajo no lo abandonará silenciosamente. Ejecute `/tasks` para ver qué se está ejecutando, luego `/bg` para confirmar abandonarlos. Vea [Desde dentro de una sesión](#from-inside-a-session) para saber qué se transfiere y qué no cuando pone en segundo plano.

### Mensaje rechazado por ser demasiado corto

La entrada de distribución espera una descripción de tarea, no un abridor conversacional. Un mensaje más corto de cuatro caracteres se rechaza con una sugerencia `Too short` para que una pulsación de tecla extraviada no inicie una sesión. Describa lo que desea que haga la sesión, como `investigate the flaky checkout test`.

### Las sesiones se muestran como detenidas después de despertar su máquina

Las sesiones en segundo plano no sobreviven al sueño o apagado, por lo que las sesiones que se estaban ejecutando se muestran como detenidas después de despertar. Conéctese, eche un vistazo o responda a cualquiera de ellas y la sesión se reiniciará desde donde se quedó. Para reiniciarlas todas a la vez, ejecute `claude respawn --all`.

### Una sesión es lenta para responder después de conectarse

Una vez que una sesión ha terminado y se ha quedado sin conectar durante aproximadamente una hora, el supervisor detiene su proceso para liberar recursos. Conectarse inicia un proceso nuevo desde donde se quedó, lo que toma un momento. Las sesiones que están funcionando o esperando su entrada nunca se detienen de esta manera.

### `.claude/worktrees/` se está llenando

Los worktrees se eliminan cuando elimina la sesión que los creó. Si una sesión terminó sin limpiar, enumere las entradas sobrantes con `git worktree list` en el directorio del proyecto y elimine cada una con `git worktree remove <path>`. Vea [Limpiar worktrees](/es/worktrees#clean-up-worktrees).

## Limitaciones

La vista de agentes está en vista previa de investigación con las siguientes limitaciones:

* **Se aplican límites de velocidad**: las sesiones en segundo plano consumen el uso de su suscripción igual que las sesiones interactivas, por lo que ejecutar diez agentes en paralelo usa cuota aproximadamente diez veces más rápido que ejecutar uno.
* **Las sesiones son locales**: las sesiones en segundo plano se ejecutan en su máquina y se detienen si entra en modo de suspensión o se apaga.
* **Los worktrees se eliminan con la sesión**: fusione o envíe cambios antes de eliminar una sesión que editó archivos en su propio worktree.

## Recursos relacionados

Para otras formas de ejecutar Claude en paralelo, consulte:

* [Ejecutar agentes en paralelo](/es/agents): compare la vista de agentes con subagentes, equipos de agentes y worktrees
* [Equipos de agentes](/es/agent-teams): coordine múltiples sesiones que se envíen mensajes entre sí
* [Claude Code en la web](/es/claude-code-on-the-web): ejecute sesiones en un entorno en la nube administrado en lugar de localmente
