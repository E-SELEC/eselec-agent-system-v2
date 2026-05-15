---
source_url: https://code.claude.com/docs/es/admin-setup
fetched_url: https://code.claude.com/docs/es/admin-setup.md
category: Administracion
status: 200
scraped_at: 2026-05-15T14:27:51+00:00
sha256_16: 1cdc88b8c5d2233f
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configurar Claude Code para su organización

> Un mapa de decisiones para administradores que implementan Claude Code, cubriendo proveedores de API, configuración administrada, aplicación de políticas, monitoreo de uso y manejo de datos.

Claude Code aplica la política de la organización a través de configuraciones administradas que tienen prioridad sobre la configuración local del desarrollador. Usted entrega esa configuración desde la consola de administración de Claude, su sistema de gestión de dispositivos móviles (MDM), o un archivo en disco. La configuración controla qué herramientas, comandos, servidores y destinos de red puede alcanzar Claude.

Esta página lo guía a través de las decisiones de implementación en orden. Cada fila se vincula a la sección a continuación y a la página de referencia para esa área.

<Note>
  SSO, aprovisionamiento SCIM y asignación de asientos se configuran a nivel de cuenta de Claude. Consulte la [Guía del administrador empresarial de Claude](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide) y [asignación de asientos](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan) para esos pasos.
</Note>

| Decisión                                                                                     | Lo que está eligiendo                                                     | Referencia                                                                                                                               |
| :------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------- |
| [Elegir su proveedor de API](#choose-your-api-provider)                                      | Dónde Claude Code se autentica y cómo se factura                          | [Authentication](/es/authentication), [Bedrock](/es/amazon-bedrock), [Vertex AI](/es/google-vertex-ai), [Foundry](/es/microsoft-foundry) |
| [Decidir cómo llega la configuración a los dispositivos](#decide-how-settings-reach-devices) | Cómo la política administrada llega a las máquinas de los desarrolladores | [Server-managed settings](/es/server-managed-settings), [Settings files](/es/settings#settings-files)                                    |
| [Decidir qué aplicar](#decide-what-to-enforce)                                               | Qué herramientas, comandos e integraciones están permitidas               | [Permissions](/es/permissions), [Sandboxing](/es/sandboxing)                                                                             |
| [Configurar visibilidad de uso](#set-up-usage-visibility)                                    | Cómo rastrear el gasto y la adopción                                      | [Analytics](/es/analytics), [Monitoring](/es/monitoring-usage), [Costs](/es/costs)                                                       |
| [Revisar el manejo de datos](#review-data-handling)                                          | Retención de datos y postura de cumplimiento                              | [Data usage](/es/data-usage), [Security](/es/security)                                                                                   |

## Elegir su proveedor de API

Claude Code se conecta a Claude a través de uno de varios proveedores de API. Su elección afecta la facturación, la autenticación, qué postura de cumplimiento hereda y qué características de Claude Code pueden usar sus desarrolladores.

| Proveedor                     | Elija esto cuando                                                                                                                                  |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude for Teams / Enterprise | Desea Claude Code y claude.ai bajo una suscripción por asiento con ninguna infraestructura para ejecutar. Esta es la recomendación predeterminada. |
| Claude Console                | Es API-first o desea facturación de pago por uso                                                                                                   |
| Amazon Bedrock                | Desea heredar controles de cumplimiento y facturación de AWS existentes                                                                            |
| Google Vertex AI              | Desea heredar controles de cumplimiento y facturación de GCP existentes                                                                            |
| Microsoft Foundry             | Desea heredar controles de cumplimiento y facturación de Azure existentes                                                                          |

Algunas características de Claude Code requieren una cuenta de Claude.ai. [Claude Code en la web](/es/claude-code-on-the-web), [Routines](/es/routines), [Code Review](/es/code-review), [Remote Control](/es/remote-control) y la [extensión de Chrome](/es/chrome) no están disponibles solo a través de claves de API de Console o credenciales de proveedores en la nube. Si implementa a través de Bedrock, Vertex o Foundry, planifique si los desarrolladores también necesitan asientos de Claude for Teams o Enterprise. Cada página de características enumera sus requisitos de plan.

Para la comparación completa del proveedor que cubre autenticación, regiones y paridad de características, consulte la [descripción general de implementación empresarial](/es/third-party-integrations). La configuración de autenticación de cada proveedor está en [Authentication](/es/authentication).

Los requisitos de proxy y firewall en [Network configuration](/es/network-config) se aplican independientemente del proveedor. Si desea un único punto final frente a múltiples proveedores o registro de solicitudes centralizado, consulte [LLM gateway](/es/llm-gateway).

## Decidir cómo llega la configuración a los dispositivos

La configuración administrada define la política que tiene prioridad sobre la configuración local del desarrollador. Claude Code las busca en cuatro lugares y usa la primera que encuentra en un dispositivo determinado.

| Mecanismo               | Entrega                                                                                                                                                                                             | Prioridad | Plataformas    |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------- | :------------- |
| Server-managed          | Consola de administración de Claude.ai                                                                                                                                                              | Más alta  | Todas          |
| plist / registry policy | macOS: `com.anthropic.claudecode` plist<br />Windows: `HKLM\SOFTWARE\Policies\ClaudeCode`                                                                                                           | Alta      | macOS, Windows |
| File-based managed      | macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`<br />Linux y WSL: `/etc/claude-code/managed-settings.json`<br />Windows: `C:\Program Files\ClaudeCode\managed-settings.json` | Media     | Todas          |
| Windows user registry   | `HKCU\SOFTWARE\Policies\ClaudeCode`                                                                                                                                                                 | Más baja  | Solo Windows   |

La configuración administrada por servidor llega a los dispositivos en el momento de la autenticación y se actualiza cada hora durante las sesiones activas, sin infraestructura de punto final. Requieren un plan Claude for Teams o Enterprise, por lo que las implementaciones en otros proveedores necesitan uno de los mecanismos basados en archivos o a nivel del SO en su lugar.

Si su organización mezcla proveedores, configure [server-managed settings](/es/server-managed-settings) para usuarios de Claude.ai más un [respaldo basado en archivos o plist/registry](/es/settings#settings-files) para que otros usuarios aún reciban política administrada.

Las ubicaciones de plist y registro HKLM funcionan con cualquier proveedor y resisten la manipulación porque requieren privilegios de administrador para escribir. El registro de usuario de Windows en HKCU se puede escribir sin elevación, así que trátelo como un valor predeterminado de conveniencia en lugar de un canal de aplicación.

Por defecto, WSL lee solo la ruta de archivo de Linux en `/etc/claude-code`. Para extender su política de registro de Windows y `C:\Program Files\ClaudeCode` a WSL en la misma máquina, establezca [`wslInheritsWindowsSettings: true`](/es/settings#available-settings) en cualquiera de esas fuentes de solo administrador de Windows.

Cualquiera que sea el mecanismo que elija, los valores administrados tienen prioridad sobre la configuración de usuario y proyecto. La configuración de matriz como `permissions.allow` y `permissions.deny` fusionan entradas de todas las fuentes, por lo que los desarrolladores pueden extender listas administradas pero no eliminar de ellas.

Consulte [Server-managed settings](/es/server-managed-settings) y [Settings files and precedence](/es/settings#settings-files).

## Decidir qué aplicar

La configuración administrada puede bloquear herramientas, ejecución de sandbox, restringir servidores MCP y fuentes de plugins, y controlar qué hooks se ejecutan. Cada fila es una superficie de control con las claves de configuración que la impulsan.

| Control                                                                                | Lo que hace                                                                                     | Configuraciones clave                                                         |
| :------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| [Permission rules](/es/permissions)                                                    | Permitir, preguntar o denegar herramientas y comandos específicos                               | `permissions.allow`, `permissions.deny`                                       |
| [Permission lockdown](/es/permissions#managed-only-settings)                           | Solo se aplican reglas de permisos administradas; deshabilitar `--dangerously-skip-permissions` | `allowManagedPermissionRulesOnly`, `permissions.disableBypassPermissionsMode` |
| [Sandboxing](/es/sandboxing)                                                           | Aislamiento de sistema de archivos y red a nivel del SO con listas de permitidos de dominio     | `sandbox.enabled`, `sandbox.network.allowedDomains`                           |
| [Managed policy CLAUDE.md](/es/memory#deploy-organization-wide-claude-md)              | Instrucciones de toda la organización cargadas en cada sesión, no se pueden excluir             | Archivo en la ruta de política administrada                                   |
| [MCP server control](/es/mcp#managed-mcp-configuration)                                | Restringir qué servidores MCP pueden agregar o conectar los usuarios                            | `allowedMcpServers`, `deniedMcpServers`, `allowManagedMcpServersOnly`         |
| [Plugin marketplace control](/es/plugin-marketplaces#managed-marketplace-restrictions) | Restringir qué fuentes de marketplace pueden agregar e instalar los usuarios                    | `strictKnownMarketplaces`, `blockedMarketplaces`                              |
| [Hook restrictions](/es/settings#hook-configuration)                                   | Solo se cargan hooks administrados; restringir URLs de hooks HTTP                               | `allowManagedHooksOnly`, `allowedHttpHookUrls`                                |
| [Disable agent view](/es/agent-view#how-background-sessions-are-hosted)                | Desactivar `claude agents`, `--bg`, `/background` y el supervisor bajo demanda                  | `disableAgentView`                                                            |
| [Version floor](/es/settings)                                                          | Evitar que la actualización automática instale por debajo de un mínimo de toda la organización  | `minimumVersion`                                                              |

Las reglas de permisos y el sandboxing cubren diferentes capas. Denegar WebFetch bloquea la herramienta de búsqueda de Claude, pero si Bash está permitido, `curl` y `wget` aún pueden alcanzar cualquier URL. El sandboxing cierra esa brecha con una lista de permitidos de dominio de red aplicada a nivel del SO.

Para el modelo de amenaza que estos controles defienden, consulte [Security](/es/security).

## Configurar visibilidad de uso

Elija monitoreo basado en lo que necesita reportar.

| Capacidad           | Lo que obtiene                                                              | Disponibilidad        | Dónde comenzar                           |
| :------------------ | :-------------------------------------------------------------------------- | :-------------------- | :--------------------------------------- |
| Usage monitoring    | Exportación de OpenTelemetry de sesiones, herramientas y tokens             | Todos los proveedores | [Monitoring usage](/es/monitoring-usage) |
| Analytics dashboard | Métricas por usuario, seguimiento de contribuciones, tabla de clasificación | Solo Anthropic        | [Analytics](/es/analytics)               |
| Cost tracking       | Límites de gasto, límites de velocidad y atribución de uso                  | Solo Anthropic        | [Costs](/es/costs)                       |

Los proveedores de nube exponen el gasto a través de AWS Cost Explorer, GCP Billing o Azure Cost Management. Los planes Claude for Teams y Enterprise incluyen un panel de uso en [claude.ai/analytics/claude-code](https://claude.ai/analytics/claude-code).

## Revisar el manejo de datos

En planes de Team, Enterprise, Claude API y proveedores de nube, Anthropic no entrena modelos con su código o indicaciones. Su proveedor de API determina la retención y la postura de cumplimiento.

| Tema                      | Lo que debe saber                                                                            | Dónde comenzar                                 |
| :------------------------ | :------------------------------------------------------------------------------------------- | :--------------------------------------------- |
| Data usage policy         | Qué recopila Anthropic, cuánto tiempo se retiene, qué nunca se usa para entrenamiento        | [Data usage](/es/data-usage)                   |
| Zero Data Retention (ZDR) | Nada almacenado después de que se completa la solicitud. Disponible en Claude for Enterprise | [Zero data retention](/es/zero-data-retention) |
| Security architecture     | Modelo de red, cifrado, autenticación, pista de auditoría                                    | [Security](/es/security)                       |

Si necesita registro de auditoría a nivel de solicitud o enrutar tráfico por sensibilidad de datos, coloque una [LLM gateway](/es/llm-gateway) entre desarrolladores y su proveedor. Para requisitos regulatorios y certificaciones, consulte [Legal and compliance](/es/legal-and-compliance).

## Verificar e incorporar

Después de configurar la configuración administrada, haga que un desarrollador ejecute `/status` dentro de Claude Code. La salida incluye una línea que comienza con `Enterprise managed settings` seguida de la fuente entre paréntesis, una de `(remote)`, `(plist)`, `(HKLM)`, `(HKCU)`, o `(file)`. Consulte [Verificar configuración activa](/es/settings#verify-active-settings).

Comparta estos recursos para ayudar a los desarrolladores a comenzar:

* [Quickstart](/es/quickstart): recorrido de primera sesión desde la instalación hasta trabajar con un proyecto
* [Common workflows](/es/common-workflows): patrones para tareas cotidianas como revisión de código, refactorización y depuración
* [Claude 101](https://anthropic.skilljar.com/claude-101) y [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action): cursos de Anthropic Academy a su propio ritmo

Para problemas de inicio de sesión, dirija a los desarrolladores a [solución de problemas de autenticación](/es/troubleshoot-install#login-and-authentication). Las correcciones más comunes son:

* Ejecutar `/logout` luego `/login` para cambiar de cuenta
* Ejecutar `claude update` si falta la opción de autenticación empresarial
* Reiniciar la terminal después de actualizar

Si un desarrollador ve "You haven't been added to your organization yet," su asiento no incluye acceso a Claude Code y debe actualizarse en la consola de administración.

## Próximos pasos

Con el proveedor y el mecanismo de entrega elegidos, continúe con la configuración detallada:

* [Server-managed settings](/es/server-managed-settings): entregar política administrada desde la consola de administración de Claude
* [Settings reference](/es/settings): cada clave de configuración, ubicación de archivo y regla de precedencia
* [Amazon Bedrock](/es/amazon-bedrock), [Google Vertex AI](/es/google-vertex-ai), [Microsoft Foundry](/es/microsoft-foundry): implementación específica del proveedor
* [Claude Enterprise Administrator Guide](https://claude.com/resources/tutorials/claude-enterprise-administrator-guide): SSO, SCIM, gestión de asientos y guía de implementación
