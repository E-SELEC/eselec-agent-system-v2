---
source_url: https://code.claude.com/docs/es/permission-modes
fetched_url: https://code.claude.com/docs/es/permission-modes.md
category: Primeros pasos
status: 200
scraped_at: 2026-05-15T14:27:27+00:00
sha256_16: 36dbd58c3c58ea09
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Elige un modo de permisos

> Controla si Claude pregunta antes de editar archivos o ejecutar comandos. Cicla entre modos con Shift+Tab en la CLI o usa el selector de modo en VS Code, Desktop y claude.ai.

Cuando Claude quiere editar un archivo, ejecutar un comando de shell o hacer una solicitud de red, se detiene y te pide que apruebes la acción. Los modos de permisos controlan con qué frecuencia ocurre esa pausa. El modo que elijas forma el flujo de una sesión: el modo predeterminado te hace revisar cada acción a medida que llega, mientras que los modos más flexibles permiten que Claude trabaje en tramos más largos sin interrupciones e informe cuando haya terminado. Elige más supervisión para trabajo sensible, o menos interrupciones cuando confías en la dirección.

## Modos disponibles

Cada modo hace un compromiso diferente entre conveniencia y supervisión. La tabla a continuación muestra qué puede hacer Claude sin un aviso de permisos en cada modo.

| Modo                                                                | Lo que se ejecuta sin preguntar                                                                                 | Mejor para                                      |
| :------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------- | :---------------------------------------------- |
| `default`                                                           | Solo lecturas                                                                                                   | Comenzar, trabajo sensible                      |
| [`acceptEdits`](#auto-approve-file-edits-with-acceptedits-mode)     | Lecturas, ediciones de archivos y comandos comunes del sistema de archivos (`mkdir`, `touch`, `mv`, `cp`, etc.) | Iterar en código que estás revisando            |
| [`plan`](#analyze-before-you-edit-with-plan-mode)                   | Solo lecturas                                                                                                   | Explorar una base de código antes de cambiarla  |
| [`auto`](#eliminate-prompts-with-auto-mode)                         | Todo, con verificaciones de seguridad de fondo                                                                  | Tareas largas, reducir fatiga de avisos         |
| [`dontAsk`](#allow-only-pre-approved-tools-with-dontask-mode)       | Solo herramientas preaprobadas                                                                                  | CI bloqueado y scripts                          |
| [`bypassPermissions`](#skip-all-checks-with-bypasspermissions-mode) | Todo                                                                                                            | Solo contenedores e máquinas virtuales aisladas |

En todos los modos excepto `bypassPermissions`, las escrituras en [rutas protegidas](#protected-paths) nunca se aprueban automáticamente, protegiendo el estado del repositorio y la configuración propia de Claude contra corrupción accidental.

Los modos establecen la línea base. Superpón [reglas de permisos](/es/permissions#manage-permissions) encima para preaprobación o bloqueo de herramientas específicas en cualquier modo excepto `bypassPermissions`, que omite completamente la capa de permisos.

## Cambiar modos de permisos

Puedes cambiar modos en medio de una sesión, al inicio o como predeterminado persistente. El modo se establece a través de estos controles, no pidiendo a Claude en el chat. Selecciona tu interfaz a continuación para ver cómo cambiarlo.

<Tabs>
  <Tab title="CLI">
    **Durante una sesión**: presiona `Shift+Tab` para ciclar `default` → `acceptEdits` → `plan`. El modo actual aparece en la barra de estado. No todos los modos están en el ciclo predeterminado:

    * `auto`: aparece cuando tu cuenta cumple los [requisitos del modo auto](#eliminate-prompts-with-auto-mode); ciclar hacia auto muestra un aviso de aceptación hasta que lo aceptes, o selecciona **No, no vuelvas a preguntar** para eliminar auto del ciclo
    * `bypassPermissions`: aparece después de que inicies con `--permission-mode bypassPermissions`, `--dangerously-skip-permissions`, o `--allow-dangerously-skip-permissions`; la variante `--allow-` añade el modo al ciclo sin activarlo
    * `dontAsk`: nunca aparece en el ciclo; establécelo con `--permission-mode dontAsk`

    Los modos opcionales habilitados se insertan después de `plan`, con `bypassPermissions` primero y `auto` último. Si tienes ambos habilitados, ciclarás a través de `bypassPermissions` en el camino a `auto`.

    **Al inicio**: pasa el modo como una bandera.

    ```bash theme={null}
    claude --permission-mode plan
    ```

    **Como predeterminado**: establece `defaultMode` en [settings](/es/settings#settings-files).

    ```json theme={null}
    {
      "permissions": {
        "defaultMode": "acceptEdits"
      }
    }
    ```

    La misma bandera `--permission-mode` funciona con `-p` para [ejecuciones no interactivas](/es/headless).
  </Tab>

  <Tab title="VS Code">
    **Durante una sesión**: haz clic en el indicador de modo en la parte inferior del cuadro de solicitud.

    **Como predeterminado**: establece `claudeCode.initialPermissionMode` en la configuración de VS Code, o usa el panel de configuración de la extensión Claude Code.

    El indicador de modo muestra estas etiquetas, asignadas al modo que cada una aplica:

    | Etiqueta de interfaz de usuario | Modo                |
    | :------------------------------ | :------------------ |
    | Pedir antes de editar           | `default`           |
    | Editar automáticamente          | `acceptEdits`       |
    | Modo de planificación           | `plan`              |
    | Modo automático                 | `auto`              |
    | Omitir permisos                 | `bypassPermissions` |

    El modo automático aparece en el indicador de modo después de que habilites **Permitir omitir permisos peligrosamente** en la configuración de la extensión, pero permanece no disponible hasta que tu cuenta cumpla todos los requisitos listados en la [sección de modo auto](#eliminate-prompts-with-auto-mode). La configuración `claudeCode.initialPermissionMode` no acepta `auto`; para comenzar en modo auto por defecto, establece `defaultMode` en tu [`settings.json`](/es/settings#settings-files) de Claude Code en su lugar.

    Omitir permisos también requiere el interruptor **Permitir omitir permisos peligrosamente** antes de que aparezca en el indicador de modo.

    Consulta la [guía de VS Code](/es/vs-code) para detalles específicos de la extensión.
  </Tab>

  <Tab title="JetBrains">
    El plugin de JetBrains ejecuta Claude Code en la terminal del IDE, por lo que cambiar modos funciona igual que en la CLI: presiona `Shift+Tab` para ciclar, o pasa `--permission-mode` al lanzar.
  </Tab>

  <Tab title="Desktop">
    Usa el selector de modo junto al botón de envío. Auto y Omitir permisos aparecen solo después de que los habilites en la configuración de Desktop. Consulta la [guía de Desktop](/es/desktop#choose-a-permission-mode).
  </Tab>

  <Tab title="Web y móvil">
    Usa el menú desplegable de modo junto al cuadro de solicitud en [claude.ai/code](https://claude.ai/code) o en la aplicación móvil. Los avisos de permisos aparecen en claude.ai para aprobación. Qué modos aparecen depende de dónde se ejecute la sesión:

    * **Sesiones en la nube** en [Claude Code en la web](/es/claude-code-on-the-web): Aceptar ediciones automáticamente y Modo de planificación. Pedir permisos, Automático y Omitir permisos no están disponibles.
    * **Sesiones de [Control remoto](/es/remote-control)** en tu máquina local: Pedir permisos, Aceptar ediciones automáticamente y Modo de planificación. Automático y Omitir permisos no están disponibles.

    Para Control remoto, también puedes establecer el modo de inicio al lanzar el host:

    ```bash theme={null}
    claude remote-control --permission-mode acceptEdits
    ```
  </Tab>
</Tabs>

## Auto-aprobar ediciones de archivos con modo acceptEdits

El modo `acceptEdits` permite que Claude cree y edite archivos en su directorio de trabajo sin solicitar confirmación. La barra de estado muestra `⏵⏵ accept edits on` mientras este modo está activo.

Además de ediciones de archivos, el modo `acceptEdits` auto-aprueba comandos Bash comunes del sistema de archivos: `mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, y `sed`. Estos comandos también se auto-aprueban cuando se prefijan con variables de entorno seguras como `LANG=C` o `NO_COLOR=1`, o envoltorios de procesos como `timeout`, `nice`, o `nohup`. Como las ediciones de archivos, la auto-aprobación se aplica solo a rutas dentro de su directorio de trabajo o `additionalDirectories`. Las rutas fuera de ese alcance, escrituras en [rutas protegidas](#protected-paths), y todos los demás comandos Bash aún solicitan confirmación.

Cuando la [herramienta PowerShell](/es/tools-reference#powershell-tool) está habilitada, el modo `acceptEdits` también auto-aprueba `Set-Content`, `Add-Content`, `Clear-Content`, y `Remove-Item` en rutas dentro del alcance, junto con sus alias comunes. Se aplican las mismas reglas de alcance y rutas protegidas.

Utilice `acceptEdits` cuando desee revisar cambios en su editor o a través de `git diff` después del hecho en lugar de aprobar cada edición en línea. Presione `Shift+Tab` una vez desde el modo predeterminado para entrar en él, o comience directamente con él:

```bash theme={null}
claude --permission-mode acceptEdits
```

## Analizar antes de editar con modo de planificación

El modo de planificación le dice a Claude que investigue y proponga cambios sin hacerlos. Claude lee archivos, ejecuta comandos de shell para explorar, y escribe un plan, pero no edita su fuente. Los avisos de permisos aún se aplican igual que en el modo predeterminado.

Entra en modo de planificación presionando `Shift+Tab` o prefijando una solicitud única con `/plan`. También puede comenzar en modo de planificación desde la CLI:

```bash theme={null}
claude --permission-mode plan
```

Presione `Shift+Tab` de nuevo para salir del modo de planificación sin aprobar un plan.

### Revisar y aprobar un plan

Cuando el plan está listo, Claude lo presenta y pregunta cómo proceder. Desde ese aviso puede:

* Aprobar e iniciar en modo automático
* Aprobar y aceptar ediciones
* Aprobar y revisar cada edición manualmente
* Continuar planificando con retroalimentación
* Refinar con [Ultraplan](/es/ultraplan) para revisión basada en navegador

Aprobando un plan se sale del modo de planificación y se cambia la sesión al modo de permisos que describe cada opción de aprobación, por lo que Claude comienza a editar. Para planificar de nuevo, vuelva al modo de planificación con `Shift+Tab`, o prefije su siguiente solicitud con `/plan`.

Presione `Ctrl+G` para abrir el plan propuesto en su editor de texto predeterminado y editarlo directamente antes de que Claude continúe. Cuando [`showClearContextOnPlanAccept`](/es/settings#available-settings) está habilitado, cada opción de aprobación también ofrece borrar el contexto de planificación primero.

Aceptar un plan también nombra la sesión a partir del contenido del plan automáticamente, a menos que ya haya establecido un nombre con `--name` o `/rename`.

### Establecer el modo de planificación como predeterminado

Para hacer que el modo de planificación sea el predeterminado para un proyecto, establezca `defaultMode` en `.claude/settings.json`:

```json theme={null}
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

## Eliminar avisos con modo automático

<Note>
  El modo automático requiere Claude Code v2.1.83 o posterior.
</Note>

El modo automático permite que Claude ejecute sin avisos de permisos. Un modelo clasificador separado revisa las acciones antes de que se ejecuten, bloqueando cualquier cosa que escale más allá de su solicitud, apunte a infraestructura no reconocida, o parezca impulsada por contenido hostil que Claude leyó.

El modo automático también instruye a Claude para ejecutar inmediatamente y minimizar preguntas aclaratorias. Para obtener ese comportamiento mientras mantiene avisos de permisos, establezca el [estilo de salida proactivo](/es/output-styles) en su lugar.

<Warning>
  El modo automático es una vista previa de investigación. Reduce avisos pero no garantiza seguridad. Úselo para tareas donde confía en la dirección general, no como reemplazo para revisión en operaciones sensibles.
</Warning>

El modo automático está disponible solo cuando su cuenta cumple todos estos requisitos:

* **Plan**: Max, Team, Enterprise, o API. No disponible en Pro.
* **Admin**: en Team y Enterprise, un administrador debe habilitarlo en [configuración de administrador de Claude Code](https://claude.ai/admin-settings/claude-code) antes de que los usuarios puedan activarlo. Los administradores también pueden bloquearlo estableciendo `permissions.disableAutoMode` a `"disable"` en [configuración administrada](/es/permissions#managed-settings).
* **Modelo**: Claude Sonnet 4.6, Opus 4.6, u Opus 4.7 en planes Team, Enterprise y API; solo Claude Opus 4.7 en planes Max. Otros modelos, incluyendo Haiku y modelos claude-3, no son compatibles.
* **Proveedor**: Solo API de Anthropic. No disponible en Bedrock, Vertex, o Foundry.

Si Claude Code reporta el modo automático como no disponible, uno de estos requisitos no se cumple; esto no es una interrupción transitoria. Un mensaje separado que nombra un modelo y dice que el modo automático "no puede determinar la seguridad" de una acción es una interrupción transitoria del clasificador; consulte la [referencia de errores](/es/errors#auto-mode-cannot-determine-the-safety-of-an-action).

### Qué bloquea el clasificador por defecto

El clasificador confía en su directorio de trabajo y en los remotos configurados de su repositorio. Todo lo demás se trata como externo hasta que [configure infraestructura confiable](/es/auto-mode-config).

**Bloqueado por defecto**:

* Descargar y ejecutar código, como `curl | bash`
* Enviar datos sensibles a puntos finales externos
* Despliegues y migraciones de producción
* Eliminación masiva en almacenamiento en la nube
* Otorgar permisos de IAM o repositorio
* Modificar infraestructura compartida
* Destruir irreversiblemente archivos que existían antes de la sesión
* Push forzado, o empujar directamente a `main`

**Permitido por defecto**:

* Operaciones de archivos locales en su directorio de trabajo
* Instalar dependencias declaradas en sus archivos de bloqueo o manifiestos
* Leer `.env` y enviar credenciales a su API coincidente
* Solicitudes HTTP de solo lectura
* Empujar a la rama en la que comenzó o una que Claude creó

Las solicitudes de acceso de red de sandbox se enrutan a través del clasificador en lugar de permitirse por defecto. Ejecute `claude auto-mode defaults` para ver las listas de reglas completas. Si las acciones rutinarias se bloquean, un administrador puede añadir repositorios confiables, depósitos y servicios a través de la configuración `autoMode.environment`: consulte [Configurar modo automático](/es/auto-mode-config).

### Límites que establece en la conversación

El clasificador trata los límites que establece en la conversación como una señal de bloqueo. Si le dice a Claude "no empuje" o "espere hasta que revise antes de desplegar", el clasificador bloquea acciones coincidentes incluso cuando las reglas predeterminadas las permitirían. Un límite permanece en vigor hasta que lo levante en un mensaje posterior. El propio juicio de Claude de que se cumplió una condición no lo levanta.

Los límites no se almacenan como reglas. El clasificador los relee de la transcripción en cada verificación, por lo que un límite puede perderse si [la compactación de contexto](/es/costs#reduce-token-usage) elimina el mensaje que lo estableció. Para una garantía dura, añada una [regla de denegación](/es/permissions#permission-rule-syntax) en su lugar.

### Cuándo el modo automático retrocede

Cada acción denegada muestra una notificación y aparece en `/permissions` bajo la pestaña Recientemente denegado, donde puede presionar `r` para reintentar con una aprobación manual.

Si el clasificador bloquea una acción 3 veces seguidas o 20 veces en total, el modo automático se pausa y Claude Code reanuda la solicitud. Aprobar la acción solicitada reanuda el modo automático. Estos umbrales no son configurables. Cualquier acción permitida reinicia el contador consecutivo, mientras que el contador total persiste para la sesión y se reinicia solo cuando su propio límite desencadena un retroceso.

En [modo no interactivo](/es/headless) con la bandera `-p`, los bloqueos repetidos abortan la sesión ya que no hay usuario para solicitar.

Los bloqueos repetidos generalmente significan que el clasificador carece de contexto sobre su infraestructura. Use `/feedback` para reportar falsos positivos, o haga que un administrador [configure infraestructura confiable](/es/auto-mode-config).

<AccordionGroup>
  <Accordion title="Cómo el clasificador evalúa acciones">
    Cada acción pasa por un orden de decisión fijo. El primer paso coincidente gana:

    1. Las acciones que coinciden con sus [reglas de permitir o denegar](/es/permissions#manage-permissions) se resuelven inmediatamente
    2. Las acciones de solo lectura y ediciones de archivos en su directorio de trabajo se auto-aprueban, excepto escrituras en [rutas protegidas](#protected-paths)
    3. Todo lo demás va al clasificador
    4. Si el clasificador bloquea, Claude recibe la razón e intenta una alternativa

    Al entrar en modo automático, se descartan las reglas de permitir amplias que otorgan ejecución de código arbitrario:

    * `Bash(*)` sin restricciones
    * Intérpretes con comodín como `Bash(python*)`
    * Comandos de ejecución del gestor de paquetes
    * Reglas `Agent` de permitir

    Las reglas estrechas como `Bash(npm test)` se mantienen. Las reglas descartadas se restauran cuando sale del modo automático.

    El clasificador ve mensajes de usuario, llamadas de herramientas, y su contenido de CLAUDE.md. Los resultados de herramientas se eliminan, por lo que el contenido hostil en un archivo o página web no puede manipularlo directamente. Una sonda separada del lado del servidor escanea los resultados de herramientas entrantes y marca contenido sospechoso antes de que Claude lo lea. Para más sobre cómo funcionan estas capas juntas, consulte el [anuncio del modo automático](https://claude.com/blog/auto-mode) y la [inmersión profunda de ingeniería](https://www.anthropic.com/engineering/claude-code-auto-mode).
  </Accordion>

  <Accordion title="Cómo el modo automático maneja subagentes">
    El clasificador verifica el trabajo de [subagentes](/es/sub-agents) en tres puntos:

    1. Antes de que un subagente comience, la descripción de tarea delegada se evalúa, por lo que una tarea que se ve peligrosa se bloquea en el momento de generación.
    2. Mientras el subagente se ejecuta, cada una de sus acciones pasa por el clasificador con las mismas reglas que la sesión principal, y cualquier `permissionMode` en el frontmatter del subagente se ignora.
    3. Cuando el subagente termina, el clasificador revisa su historial de acciones completo; si esa verificación de retorno marca una preocupación, se antepone una advertencia de seguridad a los resultados del subagente.
  </Accordion>

  <Accordion title="Costo y latencia">
    El clasificador se ejecuta en un modelo configurado por servidor que es independiente de su selección de `/model`, por lo que cambiar modelos no cambia la disponibilidad del clasificador. Las llamadas del clasificador cuentan hacia su uso de tokens. Cada verificación envía una porción de la transcripción más la acción pendiente, añadiendo un viaje de ida y vuelta antes de la ejecución. Las lecturas y ediciones de directorio de trabajo fuera de rutas protegidas omiten el clasificador, por lo que la sobrecarga proviene principalmente de comandos de shell y operaciones de red.
  </Accordion>
</AccordionGroup>

## Permitir solo herramientas preaprobadas con modo dontAsk

El modo `dontAsk` auto-deniega cada llamada de herramienta que de otro modo solicitaría. Solo las acciones que coinciden con tus reglas `permissions.allow` y [comandos Bash de solo lectura](/es/permissions#read-only-commands) pueden ejecutarse; las reglas `ask` explícitas se deniegan en lugar de solicitar. Esto hace que el modo sea completamente no interactivo para tuberías de CI o entornos restringidos donde predefines exactamente qué puede hacer Claude.

Establécelo al inicio con la bandera:

```bash theme={null}
claude --permission-mode dontAsk
```

## Omitir todas las verificaciones con modo bypassPermissions

El modo `bypassPermissions` desactiva los avisos de permisos y las verificaciones de seguridad para que las llamadas de herramientas se ejecuten inmediatamente. A partir de v2.1.126, esto incluye escrituras en [rutas protegidas](#protected-paths), que las versiones anteriores aún solicitaban. Las eliminaciones dirigidas al directorio raíz del sistema de archivos o al directorio de inicio, como `rm -rf /` y `rm -rf ~`, aún solicitan como un cortacircuitos contra errores del modelo. Use este modo solo en entornos aislados como contenedores, máquinas virtuales, o devcontainers sin acceso a internet, donde Claude Code no puede dañar su sistema anfitrión.

No puede entrar en `bypassPermissions` desde una sesión que se inició sin una de las banderas de habilitación; reinicie con una para habilitarlo:

```bash theme={null}
claude --permission-mode bypassPermissions
```

La bandera `--dangerously-skip-permissions` es equivalente.

En Linux y macOS, Claude Code se niega a iniciarse en este modo cuando se ejecuta como root o bajo `sudo`:

```text theme={null}
--dangerously-skip-permissions cannot be used with root/sudo privileges for security reasons
```

La verificación se omite automáticamente dentro de un sandbox reconocido. Para ejecutarse de forma autónoma en un contenedor, use la configuración de [dev container](/es/devcontainer), que ejecuta Claude Code como un usuario no root.

<Warning>
  `bypassPermissions` no ofrece protección contra inyección de solicitud o acciones no intencionadas. Para verificaciones de seguridad de fondo sin avisos, use [modo automático](#eliminate-prompts-with-auto-mode) en su lugar. Los administradores pueden bloquear este modo estableciendo `permissions.disableBypassPermissionsMode` a `"disable"` en [configuración administrada](/es/permissions#managed-settings).
</Warning>

## Rutas protegidas

Las escrituras en un pequeño conjunto de rutas nunca se auto-aprueban, en cada modo excepto `bypassPermissions`. Esto previene la corrupción accidental del estado del repositorio y la configuración propia de Claude. En `default`, `acceptEdits`, y `plan` estas escrituras solicitan; en `auto` se enrutan al clasificador; en `dontAsk` se deniegan; en `bypassPermissions` se permiten.

Directorios protegidos:

* `.git`
* `.vscode`
* `.idea`
* `.husky`
* `.claude`, excepto para `.claude/commands`, `.claude/agents`, `.claude/skills`, y `.claude/worktrees` donde Claude crea rutinariamente contenido

Archivos protegidos:

* `.gitconfig`, `.gitmodules`
* `.bashrc`, `.bash_profile`, `.zshrc`, `.zprofile`, `.profile`
* `.ripgreprc`
* `.mcp.json`, `.claude.json`

## Ver también

* [Permissions](/es/permissions): reglas de permitir, preguntar y denegar; políticas administradas
* [Configure auto mode](/es/auto-mode-config): dile al clasificador qué infraestructura confía tu organización
* [Hooks](/es/hooks): lógica de permisos personalizada a través de hooks `PreToolUse` y `PermissionRequest`
* [Ultraplan](/es/ultraplan): ejecuta modo de planificación en una sesión de Claude Code en la web con revisión basada en navegador
* [Security](/es/security): salvaguardas y mejores prácticas
* [Sandboxing](/es/sandboxing): aislamiento de sistema de archivos y red para comandos Bash
* [Non-interactive mode](/es/headless): ejecuta Claude Code con la bandera `-p`
