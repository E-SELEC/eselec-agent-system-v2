---
source_url: https://code.claude.com/docs/es/computer-use
fetched_url: https://code.claude.com/docs/es/computer-use.md
category: Primeros pasos
status: 200
scraped_at: 2026-05-15T14:27:34+00:00
sha256_16: 8f148135022144e6
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Permitir que Claude use su computadora desde la CLI

> Habilite computer use en la CLI de Claude Code para que Claude pueda abrir aplicaciones, hacer clic, escribir y ver su pantalla en macOS. Pruebe aplicaciones nativas, depure problemas visuales y automatice herramientas solo GUI sin salir de su terminal.

<Note>
  {/* plan-availability: feature=computer-use plans=pro,max */}

  Computer use es una vista previa de investigación en macOS que requiere un plan Pro o Max. No está disponible en planes Team o Enterprise. Requiere Claude Code v2.1.85 o posterior y una sesión interactiva, por lo que no está disponible en modo no interactivo con la bandera `-p`.
</Note>

Computer use permite que Claude abra aplicaciones, controle su pantalla y trabaje en su máquina de la manera que lo haría usted. Desde la CLI, Claude puede compilar una aplicación Swift, lanzarla, hacer clic en cada botón y capturar una pantalla del resultado, todo en la misma conversación donde escribió el código.

Esta página cubre cómo funciona computer use en la CLI. Para la aplicación de escritorio, consulte [computer use en Desktop](/es/desktop#let-claude-use-your-computer).

## Qué puede hacer con computer use

Computer use maneja tareas que requieren una GUI: cualquier cosa que normalmente tendría que dejar la terminal y hacer manualmente.

* **Compilar y validar aplicaciones nativas**: pida a Claude que compile una aplicación de barra de menú de macOS. Claude escribe el Swift, lo compila, lo lanza y hace clic en cada control para verificar que funciona antes de que usted lo abra.
* **Pruebas de UI de extremo a extremo**: señale a Claude una aplicación Electron local y diga "prueba el flujo de incorporación". Claude abre la aplicación, hace clic en el registro y captura cada paso. Sin configuración de Playwright, sin arnés de prueba.
* **Depurar problemas visuales y de diseño**: dígale a Claude "el modal se está cortando en ventanas pequeñas". Claude redimensiona la ventana, reproduce el error, captura una pantalla, parcha el CSS y verifica la corrección. Claude ve lo que usted ve.
* **Impulsar herramientas solo GUI**: interactúe con herramientas de diseño, paneles de control de hardware, el simulador de iOS o aplicaciones propietarias que no tienen CLI ni API.

## Cuándo se aplica computer use

Claude tiene varias formas de interactuar con una aplicación o servicio. Computer use es la más amplia y lenta, por lo que Claude intenta la herramienta más precisa primero:

* Si tiene un [servidor MCP](/es/mcp) para el servicio, Claude lo usa.
* Si la tarea es un comando shell, Claude usa Bash.
* Si la tarea es trabajo en navegador y tiene [Claude en Chrome](/es/chrome) configurado, Claude lo usa.
* Si ninguno de esos se aplica, Claude usa computer use.

El control de pantalla se reserva para cosas que nada más puede alcanzar: aplicaciones nativas, simuladores y herramientas sin API.

## Habilitar computer use

Computer use está disponible como un servidor MCP integrado llamado `computer-use`. Está desactivado de forma predeterminada hasta que lo habilite.

<Steps>
  <Step title="Abra el menú MCP">
    En una sesión interactiva de Claude Code, ejecute:

    ```text theme={null}
    /mcp
    ```

    Encuentre `computer-use` en la lista de servidores. Se muestra como deshabilitado.
  </Step>

  <Step title="Habilite el servidor">
    Seleccione `computer-use` y elija **Enable**. La configuración persiste por proyecto, por lo que solo hace esto una vez para cada proyecto donde desee computer use.
  </Step>

  <Step title="Otorgue permisos de macOS">
    La primera vez que Claude intente usar su computadora, verá un mensaje para otorgar dos permisos de macOS:

    * **Accessibility**: permite que Claude haga clic, escriba y desplace
    * **Screen Recording**: permite que Claude vea lo que hay en su pantalla

    El mensaje incluye enlaces para abrir el panel de Configuración del Sistema relevante. Otorgue ambos, luego seleccione **Try again** en el mensaje. macOS puede requerir que reinicie Claude Code después de otorgar Screen Recording.
  </Step>
</Steps>

Después de la configuración, pida a Claude que haga algo que necesite la GUI:

```text theme={null}
Build the app target, launch it, and click through each tab to make
sure nothing crashes. Screenshot any error states you find.
```

## Apruebe aplicaciones por sesión

Habilitar el servidor `computer-use` no otorga a Claude acceso a todas las aplicaciones en su máquina. La primera vez que Claude necesita una aplicación específica en una sesión, aparece un mensaje en su terminal mostrando:

* Qué aplicaciones Claude desea controlar
* Cualquier permiso adicional solicitado, como acceso al portapapeles
* Cuántas otras aplicaciones se ocultarán mientras Claude trabaja

Elija **Allow for this session** o **Deny**. Las aprobaciones duran para la sesión actual. Puede aprobar múltiples aplicaciones a la vez cuando Claude las solicita juntas.

Las aplicaciones con amplio alcance muestran una advertencia adicional en el mensaje para que sepa qué otorga aprobarlas:

| Advertencia                                | Se aplica a                                              |
| :----------------------------------------- | :------------------------------------------------------- |
| Equivalente a acceso shell                 | Terminal, iTerm, VS Code, Warp y otras terminales e IDEs |
| Puede leer o escribir cualquier archivo    | Finder                                                   |
| Puede cambiar la configuración del sistema | System Settings                                          |

Estas aplicaciones no están bloqueadas. La advertencia le permite decidir si la tarea justifica ese nivel de acceso.

El nivel de control de Claude también varía según la categoría de aplicación: los navegadores y plataformas de trading son solo lectura, las terminales e IDEs son solo clic, y todo lo demás obtiene control total. Consulte [permisos de aplicación en Desktop](/es/desktop#app-permissions) para el desglose completo de niveles.

## Cómo Claude trabaja en su pantalla

Comprender el flujo le ayuda a anticipar qué hará Claude y cómo intervenir.

### Una sesión a la vez

Computer use mantiene un bloqueo en toda la máquina mientras está activo. Si otra sesión de Claude Code ya está usando su computadora, los nuevos intentos fallan con un mensaje que le dice qué sesión mantiene el bloqueo. Termine o salga de esa sesión primero.

### Las aplicaciones se ocultan mientras Claude trabaja

Cuando Claude comienza a controlar su pantalla, otras aplicaciones visibles se ocultan para que Claude interactúe solo con las aplicaciones aprobadas. Su ventana de terminal permanece visible y se excluye de las capturas de pantalla, por lo que puede ver la sesión y Claude nunca ve su propio resultado.

Cuando Claude termina el turno, las aplicaciones ocultas se restauran automáticamente.

### Detener en cualquier momento

Cuando Claude adquiere el bloqueo, aparece una notificación de macOS: "Claude is using your computer · press Esc to stop". Presione `Esc` en cualquier lugar para abortar la acción actual inmediatamente, o presione `Ctrl+C` en la terminal. De cualquier manera, Claude libera el bloqueo, muestra sus aplicaciones y le devuelve el control.

Una segunda notificación aparece cuando Claude termina.

## Seguridad y el límite de confianza

<Warning>
  A diferencia de la [herramienta Bash en sandbox](/es/sandboxing), computer use se ejecuta en su escritorio real con acceso a las aplicaciones que aprueba. Claude verifica cada acción e identifica posibles inyecciones de solicitud desde el contenido en pantalla, pero el límite de confianza es diferente. Consulte la [guía de seguridad de computer use](https://support.claude.com/en/articles/14128542) para mejores prácticas.
</Warning>

Los guardarraíles integrados reducen el riesgo sin requerir configuración:

* **Aprobación por aplicación**: Claude solo puede controlar aplicaciones que ha aprobado en la sesión actual.
* **Advertencias centinela**: las aplicaciones que otorgan acceso shell, sistema de archivos o configuración del sistema se marcan antes de que las apruebe.
* **Terminal excluida de capturas de pantalla**: Claude nunca ve su ventana de terminal, por lo que los mensajes en pantalla en su sesión no pueden retroalimentarse al modelo.
* **Escape global**: la tecla `Esc` aborta computer use desde cualquier lugar, y la pulsación de tecla se consume para que la inyección de solicitud no pueda usarla para descartar diálogos.
* **Archivo de bloqueo**: solo una sesión puede controlar su máquina a la vez.

## Flujos de trabajo de ejemplo

Estos ejemplos muestran formas comunes de combinar computer use con tareas de codificación.

### Validar una compilación nativa

Después de hacer cambios en una aplicación de macOS o iOS, haga que Claude compile y verifique en un solo paso:

```text theme={null}
Build the MenuBarStats target, launch it, open the preferences window,
and verify the interval slider updates the label. Screenshot the
preferences window when you're done.
```

Claude ejecuta `xcodebuild`, lanza la aplicación, interactúa con la UI y reporta lo que encuentra.

### Reproducir un error de diseño

Cuando un error visual solo aparece en ciertos tamaños de ventana, deje que Claude lo encuentre:

```text theme={null}
The settings modal clips its footer on narrow windows. Resize the app
window down until you can reproduce it, screenshot the clipped state,
then check the CSS for the modal container.
```

Claude redimensiona la ventana, captura el estado roto y lee las hojas de estilo relevantes.

### Probar un flujo de simulador

Impulse el simulador de iOS sin escribir XCTest:

```text theme={null}
Open the iOS Simulator, launch the app, tap through the onboarding
screens, and tell me if any screen takes more than a second to load.
```

Claude controla el simulador de la misma manera que lo haría con un ratón.

## Diferencias de la aplicación de escritorio

Las superficies CLI y Desktop comparten el mismo motor de computer use. Algunos controles específicos de Desktop aún no están en la CLI:

| Característica                  | Desktop                                                      | CLI                                |
| :------------------------------ | :----------------------------------------------------------- | :--------------------------------- |
| Habilitar                       | Alternar en **Settings > General** (bajo **Desktop app**)    | Habilitar `computer-use` en `/mcp` |
| Lista de aplicaciones denegadas | Configurable en Settings                                     | Aún no disponible                  |
| Alternar auto-unhide            | Opcional                                                     | Siempre activado                   |
| Integración de Dispatch         | Las sesiones generadas por Dispatch pueden usar computer use | No aplicable                       |

## Solución de problemas

### "Computer use is in use by another Claude session"

Otra sesión de Claude Code mantiene el bloqueo. Termine la tarea en esa sesión o salga de ella. Si la otra sesión se bloqueó, el bloqueo se libera automáticamente cuando Claude detecta que el proceso ya no se está ejecutando.

### El mensaje de permisos de macOS sigue reapareciendo

macOS a veces requiere un reinicio del proceso solicitante después de otorgar Screen Recording. Salga completamente de Claude Code e inicie una nueva sesión. Si el mensaje persiste, abra **System Settings > Privacy & Security > Screen Recording** y confirme que su aplicación de terminal está listada y habilitada.

### `computer-use` no aparece en `/mcp`

El servidor solo aparece en configuraciones elegibles. Verifique que:

* Está en macOS. Computer use no está disponible en Linux o Windows.
* Está ejecutando Claude Code v2.1.85 o posterior. Ejecute `claude --version` para verificar.
* Está en un plan Pro o Max. Ejecute `/status` para confirmar su suscripción.
* Está autenticado a través de claude.ai. Computer use no está disponible con proveedores de terceros como Amazon Bedrock, Google Cloud Vertex AI o Microsoft Foundry. Si accede a Claude exclusivamente a través de un proveedor de terceros, necesita una cuenta separada de claude.ai para usar esta característica.
* Está en una sesión interactiva. Computer use no está disponible en modo no interactivo con la bandera `-p`.

## Ver también

* [Computer use en Desktop](/es/desktop#let-claude-use-your-computer): la misma capacidad con una página de configuración gráfica
* [Claude en Chrome](/es/chrome): automatización de navegador para tareas basadas en web
* [MCP](/es/mcp): conecte Claude a herramientas y APIs estructuradas
* [Sandboxing](/es/sandboxing): cómo la herramienta Bash de Claude aísla el acceso al sistema de archivos y red
* [Guía de seguridad de computer use](https://support.claude.com/en/articles/14128542): mejores prácticas para computer use seguro
