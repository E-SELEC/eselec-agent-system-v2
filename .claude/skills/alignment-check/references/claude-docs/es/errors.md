---
source_url: https://code.claude.com/docs/es/errors
fetched_url: https://code.claude.com/docs/es/errors.md
category: Crear con Claude Code, agentes y automatizacion
status: 200
scraped_at: 2026-05-15T14:27:51+00:00
sha256_16: a7288d093bd5d57a
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Referencia de errores

> Busque mensajes de error en tiempo de ejecución de Claude Code con lo que significa cada uno y cómo solucionarlo.

Esta página enumera los errores en tiempo de ejecución que Claude Code muestra y cómo recuperarse de cada uno, además de qué verificar cuando las respuestas parecen incorrectas sin un error. Para errores de instalación como `command not found` o fallos de TLS durante la configuración, consulte [Troubleshooting installation and login](/es/troubleshoot-install).

Estos errores y comandos de recuperación se aplican en la CLI, la [aplicación de escritorio](/es/desktop) y [Claude Code en la web](/es/claude-code-on-the-web), ya que los tres envuelven la misma CLI de Claude Code. Para problemas específicos de la superficie, consulte la sección de solución de problemas en la página de esa superficie.

<Note>
  Claude Code llama a la API de Claude para obtener respuestas del modelo, por lo que la mayoría de los errores en tiempo de ejecución se asignan a un código de error de API subyacente. Esta página cubre lo que significa cada error dentro de Claude Code y cómo recuperarse. Para las definiciones de código de estado HTTP sin procesar, consulte la [referencia de errores de la plataforma Claude](https://platform.claude.com/docs/en/api/errors).
</Note>

## Encuentre su error

Haga coincidir el mensaje que ve en su terminal con una sección a continuación.

| Mensaje                                                                              | Sección                                                                                                                      |
| :----------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| `API Error: 500 ... Internal server error`                                           | [Errores del servidor](#api-error-500-internal-server-error)                                                                 |
| `API Error: Repeated 529 Overloaded errors`                                          | [Errores del servidor](#api-error-repeated-529-overloaded-errors)                                                            |
| `Request timed out`                                                                  | [Errores del servidor](#request-timed-out), o [Red](#unable-to-connect-to-api) si el mensaje menciona su conexión a Internet |
| `<model> is temporarily unavailable, so auto mode cannot determine the safety of...` | [Errores del servidor](#auto-mode-cannot-determine-the-safety-of-an-action)                                                  |
| `Auto mode could not evaluate this action and is blocking it for safety`             | [Errores del servidor](#auto-mode-cannot-determine-the-safety-of-an-action)                                                  |
| `Auto mode classifier transcript exceeded context window`                            | [Errores del servidor](#auto-mode-cannot-determine-the-safety-of-an-action)                                                  |
| `You've hit your session limit` / `You've hit your weekly limit`                     | [Límites de uso](#youve-hit-your-session-limit)                                                                              |
| `Server is temporarily limiting requests`                                            | [Límites de uso](#server-is-temporarily-limiting-requests)                                                                   |
| `Request rejected (429)`                                                             | [Límites de uso](#request-rejected-429)                                                                                      |
| `Credit balance is too low`                                                          | [Límites de uso](#credit-balance-is-too-low)                                                                                 |
| `Not logged in · Please run /login`                                                  | [Autenticación](#not-logged-in)                                                                                              |
| `Invalid API key`                                                                    | [Autenticación](#invalid-api-key)                                                                                            |
| `This organization has been disabled`                                                | [Autenticación](#this-organization-has-been-disabled)                                                                        |
| `Routines are disabled by your organization's policy`                                | [Autenticación](#routines-are-disabled-by-your-organizations-policy)                                                         |
| `OAuth token revoked` / `OAuth token has expired`                                    | [Autenticación](#oauth-token-revoked-or-expired)                                                                             |
| `does not meet scope requirement user:profile`                                       | [Autenticación](#oauth-scope-requirement)                                                                                    |
| `Unable to connect to API`                                                           | [Red](#unable-to-connect-to-api)                                                                                             |
| `SSL certificate verification failed`                                                | [Red](#ssl-certificate-errors)                                                                                               |
| `403` with `x-deny-reason: host_not_allowed` in a cloud or routine session           | [Red](#host-not-allowed-in-a-cloud-session)                                                                                  |
| `Prompt is too long`                                                                 | [Errores de solicitud](#prompt-is-too-long)                                                                                  |
| `Error during compaction: Conversation too long`                                     | [Errores de solicitud](#error-during-compaction-conversation-too-long)                                                       |
| `Request too large`                                                                  | [Errores de solicitud](#request-too-large)                                                                                   |
| `Image was too large`                                                                | [Errores de solicitud](#image-was-too-large)                                                                                 |
| `PDF too large` / `PDF is password protected`                                        | [Errores de solicitud](#pdf-errors)                                                                                          |
| `Extra inputs are not permitted`                                                     | [Errores de solicitud](#extra-inputs-are-not-permitted)                                                                      |
| `There's an issue with the selected model`                                           | [Errores de solicitud](#theres-an-issue-with-the-selected-model)                                                             |
| `Claude Opus is not available with the Claude Pro plan`                              | [Errores de solicitud](#claude-opus-is-not-available-with-the-claude-pro-plan)                                               |
| `thinking.type.enabled is not supported for this model`                              | [Errores de solicitud](#thinking-type-enabled-is-not-supported-for-this-model)                                               |
| `max_tokens must be greater than thinking.budget_tokens`                             | [Errores de solicitud](#thinking-budget-exceeds-output-limit)                                                                |
| `API Error: 400 due to tool use concurrency issues`                                  | [Errores de solicitud](#tool-use-or-thinking-block-mismatch)                                                                 |
| Las respuestas parecen de menor calidad que lo habitual                              | [Calidad de respuesta](#responses-seem-lower-quality-than-usual)                                                             |

## Reintentos automáticos

Claude Code reintenta fallos transitorios antes de mostrarle un error. Los errores del servidor, respuestas sobrecargadas, tiempos de espera de solicitud, aceleraciones 429 temporales y conexiones perdidas se reintentan hasta 10 veces con retroceso exponencial. Mientras se reintenta, el spinner muestra una cuenta regresiva de `Retrying in Ns · attempt x/y`.

Cuando ve uno de los errores en esta página, esos reintentos ya se han agotado. Puede ajustar el comportamiento con dos variables de entorno:

| Variable                                  | Predeterminado | Efecto                                                                                                                                                    |
| :---------------------------------------- | :------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`CLAUDE_CODE_MAX_RETRIES`](/es/env-vars) | 10             | Número de intentos de reintento. Redúzcalo para que los fallos aparezcan más rápido en scripts; auméntelo para esperar a través de incidentes más largos. |
| [`API_TIMEOUT_MS`](/es/env-vars)          | 600000         | Tiempo de espera por solicitud en milisegundos. Auméntelo para redes lentas o proxies.                                                                    |

## Errores del servidor

Estos errores provienen de la infraestructura de Anthropic en lugar de su cuenta o solicitud.

### API Error: 500 Internal server error

Claude Code muestra el cuerpo de respuesta de API sin procesar para cualquier estado 5xx. El ejemplo a continuación muestra una respuesta 500:

```text theme={null}
API Error: 500 {"type":"error","error":{"type":"api_error","message":"Internal server error"}} · check status.claude.com
```

Esto indica un fallo inesperado dentro de la API. No es causado por su prompt, configuración o cuenta.

**Qué hacer:**

* Consulte [status.claude.com](https://status.claude.com) para ver incidentes activos
* Espere un minuto y luego envíe su mensaje nuevamente. Su mensaje original sigue en la conversación, por lo que para un prompt largo puede escribir `try again` en lugar de pegar todo de nuevo.
* Si el error persiste sin incidente publicado, ejecute `/feedback` para que Anthropic pueda investigar con los detalles de su solicitud. Consulte [Reportar un error](#report-an-error) si `/feedback` no está disponible en su proveedor.

### API Error: Repeated 529 Overloaded errors

La API está temporalmente a capacidad en todos los usuarios. Claude Code ya ha reintentado varias veces antes de mostrar este mensaje:

```text theme={null}
API Error: Repeated 529 Overloaded errors · check status.claude.com
```

Un 529 no es su límite de uso y no cuenta contra su cuota.

**Qué hacer:**

* Consulte [status.claude.com](https://status.claude.com) para ver avisos de capacidad
* Intente de nuevo en unos minutos
* Ejecute `/model` y cambie a un modelo diferente para continuar trabajando, ya que la capacidad se rastrea por modelo. Claude Code le solicita que haga esto cuando un modelo está bajo una carga particularmente alta, por ejemplo `Opus is experiencing high load, please use /model to switch to Sonnet`.

### Request timed out

La API no respondió antes de la fecha límite de conexión.

```text theme={null}
Request timed out
```

Esto puede suceder durante períodos de alta carga o cuando se genera una respuesta muy grande. El tiempo de espera de solicitud predeterminado es de 10 minutos.

**Qué hacer:**

* Reintente la solicitud
* Para tareas de larga duración, divida el trabajo en prompts más pequeños
* Si una red lenta o proxy es la causa, aumente `API_TIMEOUT_MS` como se describe en [Reintentos automáticos](#automatic-retries)
* Si los tiempos de espera son frecuentes y su red es de otro modo saludable, consulte [Errores de red y conexión](#network-and-connection-errors) a continuación

### Auto mode cannot determine the safety of an action

El modelo que [auto mode](/es/permission-modes#eliminate-prompts-with-auto-mode) utiliza para clasificar acciones no pudo producir una decisión, por lo que auto mode no aprobó la acción automáticamente. El mensaje que ve depende de por qué falló el clasificador.

Las lecturas, búsquedas y ediciones dentro de su directorio de trabajo omiten el clasificador, por lo que continúan funcionando en todos estos casos.

Cuando el modelo clasificador está sobrecargado:

```text theme={null}
<model> is temporarily unavailable, so auto mode cannot determine the safety of <tool> right now. Wait briefly and then try this action again.
```

**Qué hacer:**

* Reintente después de unos segundos; Claude ve el mismo mensaje y generalmente reintenta por su cuenta
* Si los reintentos continúan fallando, continúe con tareas de solo lectura y vuelva a la acción bloqueada más tarde
* Esto es transitorio e independiente de la [elegibilidad de auto mode](/es/permission-modes#eliminate-prompts-with-auto-mode); no necesita cambiar la configuración

Cuando el clasificador devolvió una respuesta no analizable:

```text theme={null}
Auto mode could not evaluate this action and is blocking it for safety — run with --debug for details
```

**Qué hacer:**

* Reintente la acción; esto generalmente tiene éxito en el siguiente intento
* Ejecute `claude --debug` y repita la acción para ver la respuesta del clasificador subyacente en el registro de depuración

Cuando la conversación ha crecido más que la ventana de contexto del clasificador:

```text theme={null}
Auto mode classifier transcript exceeded context window — falling back to manual approval (try /compact to reduce conversation size)
```

En una sesión interactiva, auto mode vuelve a una solicitud de permiso normal para esa acción para que pueda aprobarla o denegarla manualmente. En [modo no interactivo](/es/headless) la ejecución se cancela porque la transcripción solo crece y reintentar no puede tener éxito.

**Qué hacer:**

* Apruebe o deniegue la acción en la solicitud que aparece
* Ejecute `/compact` para reducir el tamaño de la conversación para que las acciones posteriores se ajusten nuevamente dentro de la ventana del clasificador

## Límites de uso

Estos errores significan que se ha alcanzado una cuota vinculada a su cuenta o plan. Son distintos de los [errores del servidor](#server-errors), que afectan a todos.

### You've hit your session limit

Los planes de suscripción incluyen una asignación de uso continuo. Cuando se agota, ve uno de estos mensajes:

```text theme={null}
You've hit your session limit · resets 3:45pm
You've hit your weekly limit · resets Mon 12:00am
You've hit your Opus limit · resets 3:45pm
```

Claude Code bloquea solicitudes adicionales hasta la hora de reinicio que se muestra en el mensaje.

**Qué hacer:**

* Espere la hora de reinicio que se muestra en el error
* Ejecute `/usage` para ver los límites de su plan y cuándo se reinician
* Ejecute `/extra-usage` para comprar uso adicional en Pro y Max, o para solicitarlo a su administrador en Team y Enterprise. Consulte [Extra usage for paid plans](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans) para saber cómo se factura esto.
* Para actualizar su plan para obtener límites base más altos, consulte [claude.com/pricing](https://claude.com/pricing)

Para ver su asignación restante antes de alcanzar el límite, agregue los campos `rate_limits` a una [línea de estado personalizada](/es/statusline#rate-limit-usage), o en la aplicación de escritorio haga clic en el [anillo de uso](/es/desktop#check-usage) junto al selector de modelo.

### Server is temporarily limiting requests

La API aplicó una aceleración de corta duración que no está relacionada con su cuota de plan.

```text theme={null}
API Error: Server is temporarily limiting requests (not your usage limit)
```

Esto se [reintenta automáticamente](#automatic-retries) antes de mostrarse.

**Qué hacer:**

* Espere brevemente e intente de nuevo
* Consulte [status.claude.com](https://status.claude.com) si persiste

### Request rejected (429)

Ha alcanzado el límite de velocidad configurado para su clave de API, proyecto de Amazon Bedrock o proyecto de Google Vertex AI.

```text theme={null}
API Error: Request rejected (429) · this may be a temporary capacity issue
```

**Qué hacer:**

* Ejecute `/status` y confirme que la credencial activa es la que espera. Un `ANTHROPIC_API_KEY` extraviado en su entorno puede enrutar solicitudes a través de una clave de nivel bajo en lugar de su suscripción.
* Consulte la consola de su proveedor para los límites activos y solicite un nivel más alto si es necesario
* Para claves de API de Anthropic, consulte la [referencia de límites de velocidad](https://platform.claude.com/docs/en/api/rate-limits) para saber cómo funcionan los niveles y cómo establecer límites por espacio de trabajo
* Reduzca la concurrencia: reduzca [`CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY`](/es/env-vars), evite ejecutar muchos subagentos paralelos, o cambie a un modelo más pequeño con `/model` para ejecuciones de alto volumen con scripts

### Credit balance is too low

Su organización de Console se ha quedado sin créditos prepagados.

```text theme={null}
Credit balance is too low
```

**Qué hacer:**

* Agregue créditos en [platform.claude.com/settings/billing](https://platform.claude.com/settings/billing), y considere habilitar la recarga automática allí para que el saldo se rellene antes de llegar a cero
* Cambie a autenticación de suscripción con `/login` si tiene un plan Pro, Max, Team o Enterprise
* Establezca límites de gasto por espacio de trabajo en la Console para evitar que un único proyecto agote el saldo de la organización. Consulte [Manage costs effectively](/es/costs).

## Errores de autenticación

Estos errores significan que Claude Code no puede probar quién es usted ante la API. Ejecute `/status` en cualquier momento para ver qué credencial está actualmente activa.

### Not logged in

No hay credencial válida disponible para esta sesión.

```text theme={null}
Not logged in · Please run /login
```

**Qué hacer:**

* Ejecute `/login` para autenticarse con su suscripción de Claude o cuenta de Console
* Si esperaba que una variable de entorno lo autenticara, confirme que `ANTHROPIC_API_KEY` está configurada y exportada en el shell donde lanzó `claude`
* Para CI o automatización donde el inicio de sesión interactivo no es posible, configure un script [`apiKeyHelper`](/es/settings#available-settings) que obtenga una clave al inicio
* Consulte [Authentication precedence](/es/authentication#authentication-precedence) para entender qué credencial gana cuando hay varias presentes

Si se le solicita que inicie sesión repetidamente, consulte [Not logged in or token expired](/es/troubleshoot-install#not-logged-in-or-token-expired) para correcciones del reloj del sistema y Keychain de macOS.

### Invalid API key

La variable de entorno `ANTHROPIC_API_KEY` o el script `apiKeyHelper` devolvió una clave que la API rechazó.

```text theme={null}
Invalid API key · Fix external API key
```

**Qué hacer:**

* Verifique si hay errores tipográficos y confirme que la clave no ha sido revocada en la [Console](https://platform.claude.com/settings/keys)
* Ejecute `env | grep ANTHROPIC` en el mismo shell. Herramientas como direnv, complementos de shell dotenv e IDE terminals pueden cargar una clave obsoleta desde un archivo `.env` en su proyecto sin que la configure explícitamente.
* Desactive `ANTHROPIC_API_KEY` y ejecute `/login` para usar autenticación de suscripción en su lugar
* Si la clave proviene de un script [`apiKeyHelper`](/es/settings#available-settings), ejecute el script directamente para confirmar que imprime una clave válida en stdout
* Ejecute `/status` para confirmar qué fuente de credencial está usando realmente Claude Code

### This organization has been disabled

Una `ANTHROPIC_API_KEY` obsoleta de una organización de Console deshabilitada está anulando su inicio de sesión de suscripción.

```text theme={null}
Your ANTHROPIC_API_KEY belongs to a disabled organization · Unset the environment variable to use your other credentials
API Error: 400 ... This organization has been disabled.
```

Las variables de entorno tienen prioridad sobre `/login`, por lo que una clave exportada en su perfil de shell o cargada desde un archivo `.env` se usa incluso cuando tiene una suscripción Pro o Max que funciona. En modo no interactivo (`-p`), la clave siempre se usa cuando está presente.

**Qué hacer:**

* Desactive `ANTHROPIC_API_KEY` en el shell actual y elimínelo de su perfil de shell, luego relance `claude`
* Ejecute `/status` después para confirmar que la credencial activa es su suscripción
* Si no hay variable de entorno configurada y el error persiste, la organización deshabilitada es la vinculada a su `/login`. Póngase en contacto con el soporte o inicie sesión con una cuenta diferente.

### Routines are disabled by your organization's policy

Su administrador de Team o Enterprise ha desactivado las rutinas a nivel de organización. El error aparece cuando intenta crear o ejecutar una rutina, incluyendo desde `/schedule` y la interfaz de usuario [Routines](/es/routines) en claude.ai/code.

```text theme={null}
Routines are disabled by your organization's policy.
```

Esta es una configuración del lado del servidor, por lo que no se puede anular desde la configuración local, variables de entorno o banderas de CLI.

**Qué hacer:**

* Pida a su administrador que habilite el botón **Routines** en [claude.ai/admin-settings/claude-code](https://claude.ai/admin-settings/claude-code)
* Para trabajo programado único que no requiere rutinas a nivel de organización, consulte [scheduled tasks](/es/scheduled-tasks)

### OAuth token revoked or expired

Su inicio de sesión guardado ya no es válido. Un token revocado significa que cerró sesión en todas partes o un administrador eliminó el acceso; un token expirado significa que la actualización automática falló a mitad de sesión.

```text theme={null}
OAuth token revoked · Please run /login
OAuth token has expired · Please run /login
API Error: 401 ... authentication_error
```

**Qué hacer:**

* Ejecute `/login` para iniciar sesión de nuevo
* Si el error regresa dentro de la misma sesión después de volver a autenticarse, ejecute `/logout` primero para borrar completamente el token almacenado, luego `/login`
* Para solicitudes repetidas de inicio de sesión en lanzamientos, consulte las comprobaciones del reloj del sistema y Keychain de macOS en [Troubleshooting](/es/troubleshoot-install#not-logged-in-or-token-expired)
* Para otras fallas incluyendo `403 Forbidden` y problemas del navegador OAuth, consulte [Login and authentication](/es/troubleshoot-install#login-and-authentication)

### OAuth scope requirement

El token almacenado es anterior a un alcance de permiso que una característica más nueva necesita. Lo ve más a menudo desde `/usage` y el indicador de uso de la línea de estado:

```text theme={null}
OAuth token does not meet scope requirement: user:profile
```

**Qué hacer:**

* Ejecute `/login` para crear un nuevo token con los alcances actuales. No necesita cerrar sesión primero.

## Errores de red y conexión

Estos errores significan que una solicitud de red desde Claude Code no pudo alcanzar su destino. Generalmente se originan en su red local, proxy o firewall, o en la política de red del entorno en la nube.

### Unable to connect to API

La conexión TCP a la API falló o nunca se completó.

```text theme={null}
Unable to connect to API. Check your internet connection
Unable to connect to API (ECONNREFUSED)
Unable to connect to API (ECONNRESET)
Unable to connect to API (ETIMEDOUT)
fetch failed
Request timed out. Check your internet connection and proxy settings
```

Las causas comunes incluyen sin acceso a Internet, una VPN que bloquea `api.anthropic.com`, o un proxy corporativo requerido que no está configurado.

**Qué hacer:**

* Confirme que puede alcanzar el host de API desde el mismo shell ejecutando `curl -I https://api.anthropic.com`. En Windows PowerShell use `curl.exe -I https://api.anthropic.com` para que no se use el alias `Invoke-WebRequest` incorporado.
* Si está detrás de un proxy corporativo, configure `HTTPS_PROXY` antes de lanzar Claude Code y consulte [Network configuration](/es/network-config)
* Si enruta a través de una puerta de enlace LLM o relé, configure [`ANTHROPIC_BASE_URL`](/es/env-vars) a su dirección. Consulte [LLM gateway configuration](/es/llm-gateway) para la configuración.
* Asegúrese de que su firewall permite los hosts enumerados en [Network access requirements](/es/network-config#network-access-requirements)
* Los fallos intermitentes se [reintentan automáticamente](#automatic-retries); los fallos persistentes apuntan a un problema de red local

Si `curl` tiene éxito pero Claude Code aún falla, la causa suele ser algo entre el tiempo de ejecución y la red en lugar de la red misma:

* En Linux y WSL, verifique `/etc/resolv.conf` para un servidor de nombres inalcanzable. WSL en particular puede heredar un resolutor roto del host.
* En macOS, un cliente VPN que fue desconectado o desinstalado puede dejar una interfaz de túnel o regla de enrutamiento. Verifique `ifconfig` para interfaces `utun` obsoletas y elimine la extensión de red de la VPN en Configuración del Sistema.
* Docker Desktop y tiempos de ejecución de contenedores similares pueden interceptar tráfico saliente. Ciérrelos y reintente para descartar esto.

### SSL certificate errors

Un proxy o dispositivo de seguridad en su red está interceptando tráfico TLS con su propio certificado, y Claude Code no lo confía.

```text theme={null}
Unable to connect to API: SSL certificate verification failed. Check your proxy or corporate SSL certificates
Unable to connect to API: Self-signed certificate detected
```

**Qué hacer:**

* Exporte el paquete de CA de su organización y apunte Claude Code a él con `NODE_EXTRA_CA_CERTS=/path/to/ca-bundle.pem`
* Consulte [Network configuration](/es/network-config#custom-ca-certificates) para obtener instrucciones de configuración completas
* No configure `NODE_TLS_REJECT_UNAUTHORIZED=0`, que deshabilita completamente la validación de certificados

### Host not allowed in a cloud session

Una solicitud HTTP saliente desde una sesión en la nube o rutina fue bloqueada por la política de red del entorno.

```text theme={null}
HTTP 403
x-deny-reason: host_not_allowed
```

También puede ver un certificado TLS que no coincide con el certificado real del destino. El entorno en la nube enruta el tráfico saliente a través de un proxy que aplica la política de red, por lo que un certificado que no coincide significa que el proxy terminó la conexión, no el destino.

Esto no es un problema de red del lado del cliente. Las sesiones en la nube y las [routines](/es/routines) se ejecutan dentro de un entorno aislado cuyo tráfico saliente se filtra a la lista de permitidos del entorno. El entorno **Default** utiliza acceso **Trusted**, que permite la [lista de permitidos predeterminada](/es/claude-code-on-the-web#default-allowed-domains) de registros de paquetes, API de proveedores de nube, registros de contenedores y dominios de desarrollo comunes, pero bloquea todo lo demás.

**Qué hacer:**

* Abra la rutina para editar, o inicie una sesión en la nube. Seleccione el icono de nube que muestra el nombre de su entorno, como **Default**, para abrir el selector. Pase el cursor sobre su entorno y haga clic en el icono de configuración.
* En el diálogo **Update cloud environment**, cambie **Network access** de **Trusted** a **Custom**, luego agregue el dominio bloqueado a **Allowed domains**. Ingrese un dominio por línea. Marque **Also include default list of common package managers** para mantener la [lista de permitidos predeterminada](/es/claude-code-on-the-web#default-allowed-domains) junto con sus dominios personalizados. Seleccione **Full** en su lugar si desea acceso sin restricciones.
* Haga clic en **Save changes**. La siguiente ejecución utiliza la lista de permitidos actualizada.

Consulte [Network access](/es/claude-code-on-the-web#network-access) para los niveles de acceso y la lista de permitidos predeterminada. Las sesiones locales de CLI no se ven afectadas por esta política.

## Errores de solicitud

Estos errores significan que la API recibió su solicitud pero rechazó su contenido.

### Prompt is too long

La conversación más los archivos adjuntos exceden la ventana de contexto del modelo.

```text theme={null}
Prompt is too long
```

**Qué hacer:**

* Ejecute `/compact` para resumir turnos anteriores y liberar espacio, o `/clear` para comenzar de nuevo
* Ejecute `/context` para ver un desglose de lo que está consumiendo la ventana: prompt del sistema, herramientas, archivos de memoria y mensajes
* Deshabilite los servidores MCP que no está usando con `/mcp disable <name>` para eliminar sus definiciones de herramientas del contexto
* Recorte archivos de memoria `CLAUDE.md` grandes, o mueva instrucciones a [reglas de alcance de ruta](/es/memory#path-specific-rules) que se carguen solo cuando sea relevante
* Los subagentos heredan cada definición de herramienta MCP de la sesión padre, lo que puede llenar su ventana de contexto antes del primer turno. Deshabilite los servidores MCP que no está usando antes de generar subagentos.
* Auto-compact está activado de forma predeterminada y normalmente previene este error. Si ha configurado [`DISABLE_AUTO_COMPACT`](/es/env-vars), vuelva a habilitarlo o ejecute `/compact` manualmente antes de que la ventana se llene.

Consulte [Explore the context window](/es/context-window) para una vista interactiva de cómo se llena el contexto.

### Error during compaction: Conversation too long

`/compact` en sí falló porque no hay suficiente contexto libre para contener el resumen que produce.

```text theme={null}
Error during compaction: Conversation too long. Press esc twice to go up a few messages and try again.
```

Esto puede suceder cuando la ventana ya está llena en el momento en que se activa auto-compact, o cuando ejecuta `/compact` después de ver `Prompt is too long`.

**Qué hacer:**

* Presione Esc dos veces para abrir la lista de mensajes y retroceder varios turnos. Esto elimina los mensajes más recientes del contexto. Luego ejecute `/compact` de nuevo.
* Si retroceder no libera suficiente espacio, ejecute `/clear` para comenzar una sesión nueva. Su conversación anterior se conserva y se puede reabrirse con `/resume`.

### Request too large

El cuerpo de solicitud sin procesar excedió el límite de bytes de la API antes de la tokenización, generalmente debido a un archivo o archivo adjunto grande pegado.

```text theme={null}
Request too large (max 30 MB). Double press esc to go back and remove or shrink the attached content.
```

Este es un límite de tamaño en la solicitud HTTP, separado del [límite de ventana de contexto](#prompt-is-too-long).

**Qué hacer:**

* Presione Esc dos veces y retroceda más allá del turno que agregó el contenido de tamaño excesivo
* Haga referencia a archivos grandes por ruta en lugar de pegar su contenido, para que Claude pueda leerlos en fragmentos
* Para imágenes, consulte [Image was too large](#image-was-too-large) a continuación

### Image was too large

Una imagen pegada o adjunta excede los límites de tamaño o dimensión de la API.

```text theme={null}
Image was too large. Double press esc to go back and try again with a smaller image.
API Error: 400 ... image dimensions exceed max allowed size
```

La imagen permanece en el historial de conversación después del error, por lo que cada mensaje posterior falla con el mismo error hasta que la elimine.

**Qué hacer:**

* Presione Esc dos veces y retroceda más allá del turno donde se agregó la imagen
* Cambie el tamaño de la imagen antes de pegarla. La API acepta imágenes de hasta 8000 píxeles en el borde más largo para una sola imagen, o 2000 píxeles cuando hay muchas imágenes en contexto.
* Tome una captura de pantalla más ajustada de la región relevante en lugar de la pantalla completa

### PDF errors

El PDF que adjuntó no se pudo procesar.

```text theme={null}
PDF too large (max 100 pages, 32 MB). Try splitting it or extracting text first.
PDF is password protected. Try removing protection or extracting text first.
The PDF file was not valid. Try converting to a different format first.
```

**Qué hacer:**

* Para PDF de tamaño excesivo, pida a Claude que lea un rango de páginas con la herramienta Read en lugar de adjuntar el archivo completo, o extraiga texto con una herramienta como `pdftotext` y haga referencia al archivo de salida por ruta
* Para PDF protegidos o inválidos, elimine la contraseña o reexporte el archivo desde su aplicación de origen, luego intente de nuevo

### Extra inputs are not permitted

Un proxy o puerta de enlace LLM entre Claude Code y la API eliminó el encabezado de solicitud `anthropic-beta`, por lo que la API rechazó campos que dependen de él.

```text theme={null}
API Error: 400 ... Extra inputs are not permitted ... context_management
API Error: 400 ... Extra inputs are not permitted ... tools.0.custom.input_examples
API Error: 400 ... Unexpected value(s) for the `anthropic-beta` header
```

Claude Code envía campos solo de beta como `context_management`, `effort` e `input_examples` de herramientas junto con un encabezado `anthropic-beta` que los habilita. Cuando una puerta de enlace reenvía el cuerpo pero elimina el encabezado, la API ve campos que no reconoce.

**Qué hacer:**

* Configure su puerta de enlace para reenviar el encabezado `anthropic-beta`. Consulte [LLM gateway configuration](/es/llm-gateway).
* Como alternativa, configure [`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`](/es/env-vars) antes de lanzar. Esto deshabilita características que requieren el encabezado beta para que las solicitudes tengan éxito a través de una puerta de enlace que no puede reenviarlo.

### There's an issue with the selected model

El nombre del modelo configurado no fue reconocido o su cuenta carece de acceso a él.

```text theme={null}
There's an issue with the selected model (claude-...). It may not exist or you may not have access to it. Run /model to select a different one.
```

**Qué hacer:**

* Ejecute `/model` para elegir entre modelos disponibles para su cuenta
* Use un alias como `sonnet` u `opus` en lugar de un ID completamente versionado. Los alias rastrean la última versión para que no se vuelvan obsoletos. Consulte [Model configuration](/es/model-config).
* Si el modelo incorrecto sigue apareciendo, un ID obsoleto se establece en algún lugar. Verifique en [orden de prioridad](/es/model-config#setting-your-model): la bandera `--model`, la variable de entorno `ANTHROPIC_MODEL`, luego el campo `model` en `.claude/settings.local.json`, el `.claude/settings.json` de su proyecto, y `~/.claude/settings.json`. Elimine el valor obsoleto y Claude Code vuelve a su valor predeterminado de cuenta.
* Para implementaciones de Vertex AI, consulte [Vertex AI troubleshooting](/es/google-vertex-ai#troubleshooting).

### Claude Opus is not available with the Claude Pro plan

Su plan de suscripción activo no incluye el modelo que seleccionó.

```text theme={null}
Claude Opus is not available with the Claude Pro plan · Select a different model in /model
```

**Qué hacer:**

* Ejecute `/model` y seleccione un modelo que su plan incluya
* Si actualizó su plan recientemente y aún ve esto, ejecute `/logout` luego `/login`. El token almacenado refleja su plan en el momento en que inició sesión, por lo que actualizar en la web no entra en vigor en una sesión existente hasta que se vuelva a autenticar.
* Consulte [claude.com/pricing](https://claude.com/pricing) para ver qué modelos incluye cada plan

### thinking.type.enabled is not supported for this model

Su versión de Claude Code es anterior a la mínima para Opus 4.7. La CLI envió una configuración de pensamiento que el modelo ya no acepta.

```text theme={null}
API Error: 400 ... "thinking.type.enabled" is not supported for this model. Use "thinking.type.adaptive" and "output_config.effort" to control thinking behavior.
```

**Qué hacer:**

* Ejecute `claude update` para actualizar a v2.1.111 o posterior, luego reinicie Claude Code
* Si no puede actualizar, ejecute `/model` y seleccione Opus 4.6 o Sonnet en su lugar
* Si lo encuentra en el Agent SDK, consulte [SDK troubleshooting](/es/agent-sdk/quickstart#troubleshooting)

### Thinking budget exceeds output limit

El presupuesto de pensamiento extendido configurado excede la longitud de respuesta máxima, por lo que no hay espacio para la respuesta real.

```text theme={null}
API Error: 400 ... max_tokens must be greater than thinking.budget_tokens
```

Claude Code ajusta estos valores automáticamente en la API de Anthropic. Típicamente ve este error en Amazon Bedrock o Google Vertex AI cuando [`MAX_THINKING_TOKENS`](/es/env-vars) se establece más alto que el límite de salida del proveedor, o cuando el modo de plan aumenta el presupuesto de pensamiento.

**Qué hacer:**

* Reduzca `MAX_THINKING_TOKENS`, o aumente [`CLAUDE_CODE_MAX_OUTPUT_TOKENS`](/es/env-vars) por encima del presupuesto de pensamiento
* Consulte [Extended thinking](/es/model-config#extended-thinking) para saber cómo el presupuesto interactúa con la longitud de salida

### Tool use or thinking block mismatch

El historial de conversación llegó a la API en un estado inconsistente, generalmente después de que se interrumpió una llamada de herramienta o se editó un turno a mitad de flujo.

```text theme={null}
API Error: 400 due to tool use concurrency issues. Run /rewind to recover the conversation.
API Error: 400 ... unexpected `tool_use_id` found in `tool_result` blocks
API Error: 400 ... thinking blocks ... cannot be modified
```

Las tres variantes significan lo mismo: la secuencia de bloques `tool_use`, `tool_result` y `thinking` en el historial ya no coincide con lo que la API espera.

**Qué hacer:**

* Ejecute `/rewind`, o presione Esc dos veces, para retroceder a un checkpoint antes del turno corrupto y continuar desde allí. Consulte [Checkpointing](/es/checkpointing) para saber cómo se crean y restauran los checkpoints.

## Las respuestas parecen de menor calidad de lo habitual

Si las respuestas de Claude parecen menos capaces de lo que espera pero no se muestra ningún error, la causa suele ser el estado de la conversación en lugar del modelo en sí. Claude Code no cambia silenciosamente las versiones del modelo. Puede cambiar a un modelo alternativo en casos específicos como cuando se alcanza una cuota de Opus o cuando una región de Bedrock o Vertex AI carece de su modelo; la verificación de selección de modelo a continuación detecta ambos, y [Model configuration](/es/model-config) explica cuándo se aplica la alternativa.

Verifique estos primero:

* **Selección de modelo**: ejecute `/model` para confirmar que está en el modelo que espera. Una opción anterior de `/model` o una variable de entorno `ANTHROPIC_MODEL` pueden tenerlo en un modelo más pequeño de lo que pretendía.
* **Nivel de esfuerzo**: ejecute `/effort` para verificar el nivel de razonamiento actual y auméntelo para depuración difícil o trabajo de diseño. Los valores predeterminados varían según el modelo, así que verifique antes de asumir que está por debajo del máximo. Consulte [Adjust effort level](/es/model-config#adjust-effort-level) para valores predeterminados por modelo y el atajo `ultrathink`.
* **Presión de contexto**: ejecute `/context` para ver qué tan llena está la ventana. Si está cerca de la capacidad, ejecute `/compact` en un punto natural o `/clear` para comenzar de nuevo. Consulte [Explore the context window](/es/context-window) para saber cómo auto-compact afecta los turnos anteriores.
* **Instrucciones obsoletas**: archivos `CLAUDE.md` grandes u obsoletos y definiciones de herramientas MCP consumen contexto y pueden dirigir respuestas. `/doctor` marca archivos de memoria de tamaño excesivo y definiciones de subagentos; `/context` muestra el uso de tokens de herramientas MCP.

Cuando una respuesta sale mal, retroceder generalmente funciona mejor que responder con correcciones. Presione Esc dos veces o ejecute `/rewind` para retroceder a antes del turno malo, luego reformule el prompt con más especificidades. Corregir en el hilo mantiene el intento incorrecto en contexto, lo que puede anclar respuestas posteriores a él. Consulte [Checkpointing](/es/checkpointing).

Si la calidad aún parece incorrecta después de verificar lo anterior, ejecute `/feedback` y describa lo que esperaba versus lo que obtuvo. La retroalimentación enviada de esta manera incluye la transcripción de la conversación, que es la forma más rápida para que Anthropic diagnostique una regresión real. Consulte [Report an error](#report-an-error) si `/feedback` no está disponible en su proveedor.

## Reportar un error

Esta página cubre errores de la API de Claude. Para errores de otros componentes de Claude Code, consulte la guía relevante:

* El servidor MCP no se pudo conectar o autenticar: [MCP](/es/mcp)
* El script de hook falló o bloqueó una herramienta: [Debug hooks](/es/hooks#debug-hooks)
* Permiso denegado o errores del sistema de archivos durante la instalación: [Troubleshooting](/es/troubleshoot-install)

Si un error no aparece aquí o la corrección sugerida no ayuda:

* Ejecute `/feedback` dentro de Claude Code para enviar la transcripción y una descripción a Anthropic. El comando también ofrece abrir un problema de GitHub rellenado previamente. La retroalimentación no está disponible en implementaciones de Bedrock, Vertex AI y Foundry.
* Ejecute `/doctor` para verificar problemas de configuración local
* Consulte [status.claude.com](https://status.claude.com) para ver incidentes activos
* Busque [problemas existentes](https://github.com/anthropics/claude-code/issues) en GitHub
