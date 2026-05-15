---
source_url: https://code.claude.com/docs/es/auto-mode-config
fetched_url: https://code.claude.com/docs/es/auto-mode-config.md
category: Administracion
status: 200
scraped_at: 2026-05-15T14:27:54+00:00
sha256_16: 8c20caffe95f55bd
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configurar el modo automático

> Indique al clasificador del modo automático qué repositorios, buckets y dominios confía su organización. Establezca el contexto del entorno, anule las reglas de bloqueo y permiso predeterminadas e inspeccione su configuración efectiva con los subcomandos de CLI del modo automático.

[El modo automático](/es/permission-modes#eliminate-prompts-with-auto-mode) permite que Claude Code se ejecute sin solicitudes de permiso al enrutar cada llamada de herramienta a través de un clasificador que bloquea cualquier cosa irreversible, destructiva o dirigida fuera de su entorno. Utilice el bloque de configuración `autoMode` para indicar a ese clasificador qué repositorios, buckets y dominios confía su organización, de modo que deje de bloquear operaciones internas rutinarias.

<Note>
  El modo automático está disponible en los planes Max, Team, Enterprise y API a través de la API de Anthropic. No está disponible en Pro ni en Bedrock, Vertex o Foundry. Si Claude Code informa que el modo automático no está disponible para su cuenta, consulte los [requisitos completos](/es/permission-modes#eliminate-prompts-with-auto-mode), que también cubren los modelos compatibles y la habilitación de administrador en los planes Team y Enterprise.
</Note>

De forma predeterminada, el clasificador solo confía en el directorio de trabajo y en los remotos configurados del repositorio actual. Las acciones como enviar a la organización de control de código fuente de su empresa o escribir en un bucket de nube del equipo se bloquean hasta que las agregue a `autoMode.environment`.

Para saber cómo habilitar el modo automático y qué bloquea de forma predeterminada, consulte [Modos de permiso](/es/permission-modes#eliminate-prompts-with-auto-mode). Esta página es la referencia de configuración.

Esta página cubre cómo:

* [Elegir dónde establecer reglas](#where-the-classifier-reads-configuration) en CLAUDE.md, configuración de usuario y configuración administrada
* [Definir infraestructura de confianza](#define-trusted-infrastructure) con `autoMode.environment`
* [Anular las reglas de bloqueo y permiso](#override-the-block-and-allow-rules) cuando los valores predeterminados no se ajustan a su canalización
* [Inspeccionar su configuración efectiva](#inspect-the-defaults-and-your-effective-config) con los subcomandos `claude auto-mode`
* [Revisar denegaciones](#review-denials) para saber qué agregar a continuación

## Dónde el clasificador lee la configuración

El clasificador lee el mismo contenido [CLAUDE.md](/es/memory) que carga Claude, por lo que una instrucción como "nunca force push" en el CLAUDE.md de su proyecto dirige tanto a Claude como al clasificador al mismo tiempo. Comience allí para convenciones de proyecto y reglas de comportamiento.

Para reglas que se aplican en todos los proyectos, como infraestructura de confianza o reglas de denegación en toda la organización, utilice el bloque de configuración `autoMode`. El clasificador lee `autoMode` de los siguientes ámbitos:

| Ámbito                           | Archivo                                                   | Usar para                                                            |
| :------------------------------- | :-------------------------------------------------------- | :------------------------------------------------------------------- |
| Un desarrollador                 | `~/.claude/settings.json`                                 | Infraestructura de confianza personal                                |
| Un proyecto, un desarrollador    | `.claude/settings.local.json`                             | Buckets o servicios de confianza por proyecto, gitignored            |
| En toda la organización          | [Configuración administrada](/es/server-managed-settings) | Infraestructura de confianza distribuida a todos los desarrolladores |
| Bandera `--settings` o Agent SDK | JSON en línea                                             | Anulaciones por invocación para automatización                       |

El clasificador no lee `autoMode` de la configuración de proyecto compartida en `.claude/settings.json`, por lo que un repositorio registrado no puede inyectar sus propias reglas de permiso.

Las entradas de cada ámbito se combinan. Un desarrollador puede extender `environment`, `allow`, `soft_deny` y `hard_deny` con entradas personales pero no puede eliminar entradas que proporciona la configuración administrada. Debido a que las reglas de permiso actúan como excepciones a las reglas de bloqueo suave dentro del clasificador, una entrada `allow` agregada por un desarrollador puede anular una entrada `soft_deny` de la organización: la combinación es aditiva, no un límite de política dura.

<Note>
  El clasificador es una segunda puerta que se ejecuta después del [sistema de permisos](/es/permissions). Para acciones que nunca deben ejecutarse independientemente de la intención del usuario o la configuración del clasificador, utilice `permissions.deny` en la configuración administrada, que bloquea la acción antes de que se consulte el clasificador y no puede ser anulada.
</Note>

## Definir infraestructura de confianza

Para la mayoría de las organizaciones, `autoMode.environment` es el único campo que necesita establecer. Indica al clasificador qué repositorios, buckets y dominios son de confianza: el clasificador lo utiliza para decidir qué significa "externo", por lo que cualquier destino no listado es un objetivo potencial de exfiltración.

La lista de entorno predeterminada confía en el repositorio de trabajo y sus remotos configurados. Para agregar sus propias entradas junto con ese valor predeterminado, incluya la cadena literal `"$defaults"` en la matriz. Las entradas predeterminadas se insertan en esa posición, por lo que sus entradas personalizadas pueden ir antes o después de ellas.

```json theme={null}
{
  "autoMode": {
    "environment": [
      "$defaults",
      "Source control: github.example.com/acme-corp and all repos under it",
      "Trusted cloud buckets: s3://acme-build-artifacts, gs://acme-ml-datasets",
      "Trusted internal domains: *.corp.example.com, api.internal.example.com",
      "Key internal services: Jenkins at ci.example.com, Artifactory at artifacts.example.com"
    ]
  }
}
```

Las entradas son prosa, no regex o patrones de herramientas. El clasificador las lee como reglas en lenguaje natural. Escríbalas como lo haría al describir su infraestructura a un nuevo ingeniero. Una sección de entorno exhaustiva cubre:

* **Organización**: el nombre de su empresa y para qué se utiliza principalmente Claude Code, como desarrollo de software, automatización de infraestructura o ingeniería de datos
* **Control de código fuente**: cada organización de GitHub, GitLab o Bitbucket a la que sus desarrolladores envían
* **Proveedores de nube y buckets de confianza**: nombres de buckets o prefijos que Claude debería poder leer y escribir
* **Dominios internos de confianza**: nombres de host para API, paneles y servicios dentro de su red, como `*.internal.example.com`
* **Servicios internos clave**: CI, registros de artefactos, índices de paquetes internos, herramientas de incidentes
* **Contexto adicional**: restricciones de industria regulada, infraestructura multiinquilino o requisitos de cumplimiento que afecten lo que el clasificador debe tratar como riesgoso

Una plantilla de inicio útil: complete los campos entre corchetes y elimine las líneas que no se apliquen.

```json theme={null}
{
  "autoMode": {
    "environment": [
      "$defaults",
      "Organization: {COMPANY_NAME}. Primary use: {PRIMARY_USE_CASE, e.g. software development, infrastructure automation}",
      "Source control: {SOURCE_CONTROL, e.g. GitHub org github.example.com/acme-corp}",
      "Cloud provider(s): {CLOUD_PROVIDERS, e.g. AWS, GCP, Azure}",
      "Trusted cloud buckets: {TRUSTED_BUCKETS, e.g. s3://acme-builds, gs://acme-datasets}",
      "Trusted internal domains: {TRUSTED_DOMAINS, e.g. *.internal.example.com, api.example.com}",
      "Key internal services: {SERVICES, e.g. Jenkins at ci.example.com, Artifactory at artifacts.example.com}",
      "Additional context: {EXTRA, e.g. regulated industry, multi-tenant infrastructure, compliance requirements}"
    ]
  }
}
```

Cuanto más contexto específico proporcione, mejor podrá el clasificador distinguir operaciones internas rutinarias de intentos de exfiltración.

No necesita completar todo de una vez. Un despliegue razonable: comience con los valores predeterminados y agregue su organización de control de código fuente y servicios internos clave, lo que resuelve los falsos positivos más comunes como enviar a sus propios repositorios. Agregue dominios de confianza y buckets de nube a continuación. Complete el resto a medida que surjan bloqueos.

## Anular las reglas de bloqueo y permiso

Tres campos adicionales le permiten reemplazar las listas de reglas integradas del clasificador: `autoMode.hard_deny` para límites de seguridad incondicionales, `autoMode.soft_deny` para acciones destructivas que la intención del usuario puede anular, y `autoMode.allow` para excepciones. Cada uno es una matriz de descripciones en prosa, leídas como reglas en lenguaje natural. Para bloqueos basados en patrones de herramientas que se ejecutan antes del clasificador, utilice [`permissions.deny`](/es/permissions).

Dentro del clasificador, la precedencia funciona en cuatro niveles:

* Las reglas `hard_deny` bloquean incondicionalmente. La intención del usuario y las excepciones `allow` no se aplican.
* Las reglas `soft_deny` bloquean a continuación. La intención del usuario y las excepciones `allow` pueden anular estas.
* Las reglas `allow` luego anulan las reglas `soft_deny` coincidentes como excepciones.
* La intención explícita del usuario anula los bloqueos suaves restantes: si el mensaje del usuario describe directa y específicamente la acción exacta que Claude está a punto de tomar, el clasificador la permite incluso cuando una regla `soft_deny` coincide.

Las solicitudes generales no cuentan como intención explícita. Pedirle a Claude que "limpie el repositorio" no autoriza force-push, pero pedirle que "force-push esta rama" sí.

Para flexibilizar, agregue a `allow` cuando el clasificador marca repetidamente un patrón rutinario que las excepciones predeterminadas no cubren. Para endurecer, agregue a `soft_deny` para riesgos destructivos específicos de su entorno que los valores predeterminados pierden, o a `hard_deny` para límites de seguridad que nunca deben cruzarse. Para mantener las reglas integradas mientras agrega las suyas propias, incluya la cadena literal `"$defaults"` en la matriz. Las reglas predeterminadas se insertan en esa posición, por lo que sus reglas personalizadas pueden ir antes o después de ellas, y continúa heredando actualizaciones a medida que la lista integrada cambia en las versiones.

```json theme={null}
{
  "autoMode": {
    "environment": [
      "$defaults",
      "Source control: github.example.com/acme-corp and all repos under it"
    ],
    "allow": [
      "$defaults",
      "Deploying to the staging namespace is allowed: staging is isolated from production and resets nightly",
      "Writing to s3://acme-scratch/ is allowed: ephemeral bucket with a 7-day lifecycle policy"
    ],
    "soft_deny": [
      "$defaults",
      "Never run database migrations outside the migrations CLI, even against dev databases",
      "Never modify files under infra/terraform/prod/: production infrastructure changes go through the review workflow"
    ],
    "hard_deny": [
      "$defaults",
      "Never send repository contents to third-party code-review APIs"
    ]
  }
}
```

<Danger>
  Establecer cualquiera de `environment`, `allow`, `soft_deny` o `hard_deny` sin `"$defaults"` reemplaza la lista predeterminada completa para esa sección. Una matriz `soft_deny` sin `"$defaults"` descarta todas las reglas de bloqueo integradas, incluido force push, `curl | bash` y despliegues de producción. Una matriz `hard_deny` sin `"$defaults"` descarta las reglas integradas de exfiltración de datos y omisión de verificación de seguridad.
</Danger>

Cada sección se evalúa de forma independiente, por lo que establecer `environment` solo deja intactas las listas predeterminadas `allow`, `soft_deny` y `hard_deny`. Solo omita `"$defaults"` cuando tenga la intención de asumir la propiedad completa de la lista. Para hacerlo de forma segura, ejecute `claude auto-mode defaults` para imprimir las reglas integradas, cópielas en su archivo de configuración, luego revise cada regla contra su propia canalización y tolerancia al riesgo.

## Inspeccione los valores predeterminados y su configuración efectiva

Tres subcomandos de CLI lo ayudan a inspeccionar y validar su configuración.

Imprima las reglas `environment`, `allow`, `soft_deny` y `hard_deny` integradas como JSON:

```bash theme={null}
claude auto-mode defaults
```

Imprima lo que el clasificador realmente utiliza como JSON, con su configuración aplicada donde se establece y valores predeterminados en caso contrario:

```bash theme={null}
claude auto-mode config
```

Obtenga retroalimentación de IA sobre sus reglas `allow`, `soft_deny` y `hard_deny` personalizadas:

```bash theme={null}
claude auto-mode critique
```

Ejecute `claude auto-mode config` después de guardar su configuración para confirmar que las reglas efectivas son las que espera, con `"$defaults"` expandido en su lugar. Si ha escrito reglas personalizadas, `claude auto-mode critique` las revisa y marca entradas que son ambiguas, redundantes o probables que causen falsos positivos. Si necesita eliminar o reescribir una regla integrada en lugar de agregar una junto a ella, guarde la salida de `claude auto-mode defaults` en un archivo, edite las listas y pegue el resultado en su archivo de configuración en lugar de `"$defaults"`.

## Review denials

Cuando el modo automático deniega una llamada de herramienta, la denegación se registra en `/permissions` bajo la pestaña Denegados recientemente. Presione `r` en una acción denegada para marcarla para reintentar: cuando salga del diálogo, Claude Code envía un mensaje indicando al modelo que puede reintentar esa llamada de herramienta y reanuda la conversación.

Las denegaciones repetidas para el mismo destino generalmente significan que el clasificador carece de contexto. Agregue ese destino a `autoMode.environment`, luego ejecute `claude auto-mode config` para confirmar que surtió efecto.

Para reaccionar a las denegaciones mediante programación, utilice el [hook `PermissionDenied`](/es/hooks#permissiondenied).

## See also

* [Permission modes](/es/permission-modes#eliminate-prompts-with-auto-mode): qué es el modo automático, qué bloquea de forma predeterminada y cómo habilitarlo
* [Managed settings](/es/server-managed-settings): implemente la configuración `autoMode` en toda su organización
* [Permissions](/es/permissions): reglas de permiso, pregunta y denegación que se aplican antes de que se ejecute el clasificador
* [Settings](/es/settings): la referencia de configuración completa, incluida la clave `autoMode`
