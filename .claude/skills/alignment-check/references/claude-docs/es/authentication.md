---
source_url: https://code.claude.com/docs/es/authentication
fetched_url: https://code.claude.com/docs/es/authentication.md
category: Administracion
status: 200
scraped_at: 2026-05-15T14:27:53+00:00
sha256_16: 9d3f6c68533f7e39
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Autenticación

> Inicie sesión en Claude Code y configure la autenticación para individuos, equipos y organizaciones.

Claude Code admite múltiples métodos de autenticación según su configuración. Los usuarios individuales pueden iniciar sesión con una cuenta de Claude.ai, mientras que los equipos pueden usar Claude for Teams o Enterprise, la Claude Console, o un proveedor de nube como Amazon Bedrock, Google Vertex AI o Microsoft Foundry.

## Inicie sesión en Claude Code

Después de [instalar Claude Code](/es/setup#install-claude-code), ejecute `claude` en su terminal. En el primer lanzamiento, Claude Code abre una ventana del navegador para que inicie sesión.

Si el navegador no se abre automáticamente, presione `c` para copiar la URL de inicio de sesión al portapapeles y luego péguelo en su navegador.

Si su navegador muestra un código de inicio de sesión en lugar de redirigirse después de que inicie sesión, péguelo en el terminal en el símbolo del sistema `Paste code here if prompted`. Esto sucede cuando el navegador no puede alcanzar el servidor de devolución de llamada local de Claude Code, lo cual es común en WSL2, sesiones SSH y contenedores.

Puede autenticarse con cualquiera de estos tipos de cuenta:

* **Suscripción Claude Pro o Max**: inicie sesión con su cuenta de Claude.ai. Suscríbase en [claude.com/pricing](https://claude.com/pricing?utm_source=claude_code\&utm_medium=docs\&utm_content=authentication_pro_max).
* **Claude for Teams o Enterprise**: inicie sesión con la cuenta de Claude.ai que su administrador de equipo le invitó a usar.
* **Claude Console**: inicie sesión con sus credenciales de Console. Su administrador debe haberle [invitado](#claude-console-authentication) primero.
* **Proveedores de nube**: si su organización usa [Amazon Bedrock](/es/amazon-bedrock), [Google Vertex AI](/es/google-vertex-ai) o [Microsoft Foundry](/es/microsoft-foundry), establezca las variables de entorno requeridas antes de ejecutar `claude`. No se necesita inicio de sesión en el navegador.

Para cerrar sesión y volver a autenticarse, escriba `/logout` en el símbolo del sistema de Claude Code.

Si tiene problemas para iniciar sesión, consulte [solución de problemas de autenticación](/es/troubleshoot-install#login-and-authentication).

## Configure la autenticación del equipo

Para equipos y organizaciones, puede configurar el acceso a Claude Code de una de estas formas:

* [Claude for Teams o Enterprise](#claude-for-teams-or-enterprise), recomendado para la mayoría de los equipos
* [Claude Console](#claude-console-authentication)
* [Amazon Bedrock](/es/amazon-bedrock)
* [Google Vertex AI](/es/google-vertex-ai)
* [Microsoft Foundry](/es/microsoft-foundry)

### Claude for Teams o Enterprise

[Claude for Teams](https://claude.com/pricing?utm_source=claude_code\&utm_medium=docs\&utm_content=authentication_teams#team-&-enterprise) y [Claude for Enterprise](https://anthropic.com/contact-sales?utm_source=claude_code\&utm_medium=docs\&utm_content=authentication_enterprise) proporcionan la mejor experiencia para organizaciones que usan Claude Code. Los miembros del equipo obtienen acceso tanto a Claude Code como a Claude en la web con facturación centralizada y gestión de equipos.

* **Claude for Teams**: plan de autoservicio con características de colaboración, herramientas de administración y gestión de facturación. Mejor para equipos más pequeños.
* **Claude for Enterprise**: añade SSO, captura de dominio, permisos basados en roles, API de cumplimiento y configuración de políticas administradas para configuraciones de Claude Code en toda la organización. Mejor para organizaciones más grandes con requisitos de seguridad y cumplimiento.

<Steps>
  <Step title="Suscribirse">
    Suscríbase a [Claude for Teams](https://claude.com/pricing?utm_source=claude_code\&utm_medium=docs\&utm_content=authentication_teams_step#team-&-enterprise) o póngase en contacto con ventas para [Claude for Enterprise](https://anthropic.com/contact-sales?utm_source=claude_code\&utm_medium=docs\&utm_content=authentication_enterprise_step).
  </Step>

  <Step title="Invitar a miembros del equipo">
    Invite a miembros del equipo desde el panel de administración.
  </Step>

  <Step title="Instalar e iniciar sesión">
    Los miembros del equipo instalan Claude Code e inician sesión con sus cuentas de Claude.ai.
  </Step>
</Steps>

### Autenticación de Claude Console

Para organizaciones que prefieren facturación basada en API, puede configurar el acceso a través de Claude Console.

<Steps>
  <Step title="Crear o usar una cuenta de Console">
    Use su cuenta de Claude Console existente o cree una nueva.
  </Step>

  <Step title="Agregar usuarios">
    Puede agregar usuarios mediante cualquiera de estos métodos:

    * Invitar usuarios en masa desde dentro de Console: Settings -> Members -> Invite
    * [Configurar SSO](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)
  </Step>

  <Step title="Asignar roles">
    Al invitar usuarios, asigne uno de:

    * **Rol Claude Code**: los usuarios solo pueden crear claves API de Claude Code
    * **Rol Developer**: los usuarios pueden crear cualquier tipo de clave API
  </Step>

  <Step title="Los usuarios completan la configuración">
    Cada usuario invitado necesita:

    * Aceptar la invitación de Console
    * [Verificar requisitos del sistema](/es/setup#system-requirements)
    * [Instalar Claude Code](/es/setup#install-claude-code)
    * Iniciar sesión con credenciales de cuenta de Console
  </Step>
</Steps>

### Autenticación del proveedor de nube

Para equipos que usan Amazon Bedrock, Google Vertex AI o Microsoft Foundry:

<Steps>
  <Step title="Seguir la configuración del proveedor">
    Siga la [documentación de Bedrock](/es/amazon-bedrock), [documentación de Vertex](/es/google-vertex-ai) o [documentación de Microsoft Foundry](/es/microsoft-foundry).
  </Step>

  <Step title="Distribuir configuración">
    Distribuya las variables de entorno e instrucciones para generar credenciales de nube a sus usuarios. Lea más sobre cómo [administrar la configuración aquí](/es/settings).
  </Step>

  <Step title="Instalar Claude Code">
    Los usuarios pueden [instalar Claude Code](/es/setup#install-claude-code).
  </Step>
</Steps>

## Gestión de credenciales

Claude Code administra de forma segura sus credenciales de autenticación:

* **Ubicación de almacenamiento**:
  * En macOS, las credenciales se almacenan en el Keychain de macOS cifrado.
  * En Linux, las credenciales se almacenan en `~/.claude/.credentials.json` con modo de archivo `0600`.
  * En Windows, las credenciales se almacenan en `%USERPROFILE%\.claude\.credentials.json` y heredan los controles de acceso del directorio de su perfil de usuario, lo que restringe el archivo a su cuenta de usuario de forma predeterminada.
  * Si ha establecido la variable de entorno `CLAUDE_CONFIG_DIR` en Linux o Windows, el archivo `.credentials.json` se encuentra en ese directorio en su lugar.
  * Claude Code administra `.credentials.json` a través de `/login` y `/logout`. Para enrutar solicitudes a través de un punto final de API personalizado, establezca la variable de entorno [`ANTHROPIC_BASE_URL`](/es/env-vars) en su lugar.
* **Tipos de autenticación admitidos**: credenciales de Claude.ai, credenciales de API de Claude, Azure Auth, Bedrock Auth y Vertex Auth.
* **Scripts de credenciales personalizados**: la configuración [`apiKeyHelper`](/es/settings#available-settings) se puede configurar para ejecutar un script de shell que devuelva una clave API.
* **Intervalos de actualización**: por defecto, `apiKeyHelper` se llama después de 5 minutos o en respuesta HTTP 401. Establezca la variable de entorno `CLAUDE_CODE_API_KEY_HELPER_TTL_MS` para intervalos de actualización personalizados.
* **Aviso de helper lento**: si `apiKeyHelper` tarda más de 10 segundos en devolver una clave, Claude Code muestra un aviso de advertencia en la barra de símbolo del sistema mostrando el tiempo transcurrido. Si ve este aviso regularmente, verifique si su script de credenciales se puede optimizar.

`apiKeyHelper`, `ANTHROPIC_API_KEY` y `ANTHROPIC_AUTH_TOKEN` se aplican solo a sesiones de CLI de terminal. Claude Desktop y sesiones remotas usan OAuth exclusivamente y no llaman a `apiKeyHelper` ni leen variables de entorno de clave API.

### Precedencia de autenticación

Cuando hay múltiples credenciales presentes, Claude Code elige una en este orden:

1. Credenciales del proveedor de nube, cuando `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX` o `CLAUDE_CODE_USE_FOUNDRY` está establecido. Consulte [integraciones de terceros](/es/third-party-integrations) para la configuración.
2. Variable de entorno `ANTHROPIC_AUTH_TOKEN`. Se envía como encabezado `Authorization: Bearer`. Use esto cuando enrute a través de una [puerta de enlace LLM o proxy](/es/llm-gateway) que se autentica con tokens de portador en lugar de claves API de Anthropic.
3. Variable de entorno `ANTHROPIC_API_KEY`. Se envía como encabezado `X-Api-Key`. Use esto para acceso directo a la API de Anthropic con una clave de [Claude Console](https://platform.claude.com). En modo interactivo, se le solicita una vez que apruebe o rechace la clave, y su elección se recuerda. Para cambiarla más tarde, use el botón de alternancia "Use custom API key" en `/config`. En modo no interactivo (`-p`), la clave siempre se usa cuando está presente.
4. Salida del script [`apiKeyHelper`](/es/settings#available-settings). Use esto para credenciales dinámicas o rotativas, como tokens de corta duración obtenidos de un almacén.
5. Variable de entorno `CLAUDE_CODE_OAUTH_TOKEN`. Un token OAuth de larga duración generado por [`claude setup-token`](#generate-a-long-lived-token). Use esto para canalizaciones de CI y scripts donde el inicio de sesión del navegador no está disponible.
6. Credenciales OAuth de suscripción de `/login`. Este es el predeterminado para usuarios de Claude Pro, Max, Team y Enterprise.

Si tiene una suscripción activa de Claude pero también tiene `ANTHROPIC_API_KEY` establecido en su entorno, la clave API tiene precedencia una vez aprobada. Esto puede causar fallos de autenticación si la clave pertenece a una organización deshabilitada o expirada. Ejecute `unset ANTHROPIC_API_KEY` para volver a su suscripción y verifique `/status` para confirmar qué método está activo.

[Claude Code en la Web](/es/claude-code-on-the-web) siempre usa sus credenciales de suscripción. `ANTHROPIC_API_KEY` y `ANTHROPIC_AUTH_TOKEN` en el entorno de sandbox no las anulan.

### Generar un token de larga duración

<Note>
  Starting June 15, 2026, Agent SDK and `claude -p` usage on subscription plans will draw from a new monthly Agent SDK credit, separate from your interactive usage limits. See [Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) for details.
</Note>

Para canalizaciones de CI, scripts u otros entornos donde el inicio de sesión interactivo del navegador no está disponible, genere un token OAuth de un año con `claude setup-token`:

```bash theme={null}
claude setup-token
```

El comando lo guía a través de la autorización OAuth e imprime un token en el terminal. No guarda el token en ningún lugar; cópielo y establézcalo como la variable de entorno `CLAUDE_CODE_OAUTH_TOKEN` donde desee autenticarse:

```bash theme={null}
export CLAUDE_CODE_OAUTH_TOKEN=your-token
```

Este token se autentica con su suscripción de Claude y requiere un plan Pro, Max, Team o Enterprise. Se limita solo a inferencia y no puede establecer sesiones de [Remote Control](/es/remote-control).

[Bare mode](/es/headless#start-faster-with-bare-mode) no lee `CLAUDE_CODE_OAUTH_TOKEN`. Si su script pasa `--bare`, autentíquese con `ANTHROPIC_API_KEY` o un `apiKeyHelper` en su lugar.
