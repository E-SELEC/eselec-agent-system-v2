---
source_url: https://code.claude.com/docs/es/agent-sdk/typescript
fetched_url: https://code.claude.com/docs/es/agent-sdk/typescript.md
category: SDK de Agente
status: 200
scraped_at: 2026-05-15T14:28:47+00:00
sha256_16: e5a33890f1e428ed
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Referencia del SDK de Agent - TypeScript

> Referencia completa de la API del SDK de Agent de TypeScript, incluyendo todas las funciones, tipos e interfaces.

<script src="/components/typescript-sdk-type-links.js" defer />

## Instalación

```bash theme={null}
npm install @anthropic-ai/claude-agent-sdk
```

<Note>
  El SDK incluye un binario nativo de Claude Code para su plataforma como una dependencia opcional como `@anthropic-ai/claude-agent-sdk-darwin-arm64`. No necesita instalar Claude Code por separado. Si su gestor de paquetes omite las dependencias opcionales, el SDK lanza `Native CLI binary for <platform> not found`; en su lugar, establezca [`pathToClaudeCodeExecutable`](#options) en un binario `claude` instalado por separado.
</Note>

## Funciones

### `query()`

La función principal para interactuar con Claude Code. Crea un generador asincrónico que transmite mensajes a medida que llegan.

```typescript theme={null}
function query({
  prompt,
  options
}: {
  prompt: string | AsyncIterable<SDKUserMessage>;
  options?: Options;
}): Query;
```

#### Parámetros

| Parámetro | Tipo                                                             | Descripción                                                                              |
| :-------- | :--------------------------------------------------------------- | :--------------------------------------------------------------------------------------- |
| `prompt`  | `string \| AsyncIterable<`[`SDKUserMessage`](#sdkusermessage)`>` | El mensaje de entrada como una cadena o iterable asincrónico para el modo de transmisión |
| `options` | [`Options`](#options)                                            | Objeto de configuración opcional (vea el tipo Options a continuación)                    |

#### Devuelve

Devuelve un objeto [`Query`](#query-object) que extiende `AsyncGenerator<`[`SDKMessage`](#sdkmessage)`, void>` con métodos adicionales.

### `startup()`

Precalienta el subproceso CLI iniciándolo y completando el protocolo de inicialización antes de que un mensaje esté disponible. El identificador [`WarmQuery`](#warmquery) devuelto acepta un mensaje más tarde y lo escribe en un proceso ya listo, por lo que la primera llamada a `query()` se resuelve sin pagar el costo de generación e inicialización del subproceso en línea.

```typescript theme={null}
function startup(params?: {
  options?: Options;
  initializeTimeoutMs?: number;
}): Promise<WarmQuery>;
```

#### Parámetros

| Parámetro             | Tipo                  | Descripción                                                                                                                                                                                               |
| :-------------------- | :-------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `options`             | [`Options`](#options) | Objeto de configuración opcional. Igual que el parámetro `options` para `query()`                                                                                                                         |
| `initializeTimeoutMs` | `number`              | Tiempo máximo en milisegundos para esperar la inicialización del subproceso. Por defecto es `60000`. Si la inicialización no se completa a tiempo, la promesa se rechaza con un error de tiempo de espera |

#### Devuelve

Devuelve una `Promise<`[`WarmQuery`](#warmquery)`>` que se resuelve una vez que el subproceso se ha generado y ha completado su protocolo de inicialización.

#### Ejemplo

Llame a `startup()` temprano, por ejemplo al inicio de la aplicación, luego llame a `.query()` en el identificador devuelto una vez que un mensaje esté listo. Esto mueve la generación del subproceso e inicialización fuera de la ruta crítica.

```typescript theme={null}
import { startup } from "@anthropic-ai/claude-agent-sdk";

// Pague el costo de inicio por adelantado
const warm = await startup({ options: { maxTurns: 3 } });

// Más tarde, cuando un mensaje esté listo, esto es inmediato
for await (const message of warm.query("What files are here?")) {
  console.log(message);
}
```

### `tool()`

Crea una definición de herramienta MCP segura de tipos para usar con servidores MCP del SDK.

```typescript theme={null}
function tool<Schema extends AnyZodRawShape>(
  name: string,
  description: string,
  inputSchema: Schema,
  handler: (args: InferShape<Schema>, extra: unknown) => Promise<CallToolResult>,
  extras?: { annotations?: ToolAnnotations }
): SdkMcpToolDefinition<Schema>;
```

#### Parámetros

| Parámetro     | Tipo                                                              | Descripción                                                                                             |
| :------------ | :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| `name`        | `string`                                                          | El nombre de la herramienta                                                                             |
| `description` | `string`                                                          | Una descripción de lo que hace la herramienta                                                           |
| `inputSchema` | `Schema extends AnyZodRawShape`                                   | Esquema Zod que define los parámetros de entrada de la herramienta (soporta tanto Zod 3 como Zod 4)     |
| `handler`     | `(args, extra) => Promise<`[`CallToolResult`](#calltoolresult)`>` | Función asincrónica que ejecuta la lógica de la herramienta                                             |
| `extras`      | `{ annotations?: `[`ToolAnnotations`](#toolannotations)` }`       | Anotaciones opcionales de herramienta MCP que proporcionan sugerencias de comportamiento a los clientes |

#### `ToolAnnotations`

Re-exportado desde `@modelcontextprotocol/sdk/types.js`. Todos los campos son sugerencias opcionales; los clientes no deben confiar en ellos para decisiones de seguridad.

| Campo             | Tipo      | Predeterminado | Descripción                                                                                                                                                                                  |
| :---------------- | :-------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `title`           | `string`  | `undefined`    | Título legible por humanos para la herramienta                                                                                                                                               |
| `readOnlyHint`    | `boolean` | `false`        | Si es `true`, la herramienta no modifica su entorno                                                                                                                                          |
| `destructiveHint` | `boolean` | `true`         | Si es `true`, la herramienta puede realizar actualizaciones destructivas (solo significativo cuando `readOnlyHint` es `false`)                                                               |
| `idempotentHint`  | `boolean` | `false`        | Si es `true`, las llamadas repetidas con los mismos argumentos no tienen efecto adicional (solo significativo cuando `readOnlyHint` es `false`)                                              |
| `openWorldHint`   | `boolean` | `true`         | Si es `true`, la herramienta interactúa con entidades externas (por ejemplo, búsqueda web). Si es `false`, el dominio de la herramienta es cerrado (por ejemplo, una herramienta de memoria) |

```typescript theme={null}
import { tool } from "@anthropic-ai/claude-agent-sdk";
import { z } from "zod";

const searchTool = tool(
  "search",
  "Search the web",
  { query: z.string() },
  async ({ query }) => {
    return { content: [{ type: "text", text: `Results for: ${query}` }] };
  },
  { annotations: { readOnlyHint: true, openWorldHint: true } }
);
```

### `createSdkMcpServer()`

Crea una instancia de servidor MCP que se ejecuta en el mismo proceso que su aplicación.

```typescript theme={null}
function createSdkMcpServer(options: {
  name: string;
  version?: string;
  tools?: Array<SdkMcpToolDefinition<any>>;
}): McpSdkServerConfigWithInstance;
```

#### Parámetros

| Parámetro         | Tipo                          | Descripción                                                          |
| :---------------- | :---------------------------- | :------------------------------------------------------------------- |
| `options.name`    | `string`                      | El nombre del servidor MCP                                           |
| `options.version` | `string`                      | Cadena de versión opcional                                           |
| `options.tools`   | `Array<SdkMcpToolDefinition>` | Matriz de definiciones de herramientas creadas con [`tool()`](#tool) |

### `listSessions()`

Descubre y enumera sesiones pasadas con metadatos ligeros. Filtre por directorio de proyecto o enumere sesiones en todos los proyectos.

```typescript theme={null}
function listSessions(options?: ListSessionsOptions): Promise<SDKSessionInfo[]>;
```

#### Parámetros

| Parámetro                  | Tipo      | Predeterminado | Descripción                                                                                     |
| :------------------------- | :-------- | :------------- | :---------------------------------------------------------------------------------------------- |
| `options.dir`              | `string`  | `undefined`    | Directorio para enumerar sesiones. Cuando se omite, devuelve sesiones en todos los proyectos    |
| `options.limit`            | `number`  | `undefined`    | Número máximo de sesiones a devolver                                                            |
| `options.includeWorktrees` | `boolean` | `true`         | Cuando `dir` está dentro de un repositorio git, incluya sesiones de todas las rutas de worktree |

#### Tipo de retorno: `SDKSessionInfo`

| Propiedad      | Tipo                  | Descripción                                                                                      |
| :------------- | :-------------------- | :----------------------------------------------------------------------------------------------- |
| `sessionId`    | `string`              | Identificador de sesión único (UUID)                                                             |
| `summary`      | `string`              | Título de visualización: título personalizado, resumen generado automáticamente o primer mensaje |
| `lastModified` | `number`              | Última hora de modificación en milisegundos desde la época                                       |
| `fileSize`     | `number \| undefined` | Tamaño del archivo de sesión en bytes. Solo se completa para almacenamiento JSONL local          |
| `customTitle`  | `string \| undefined` | Título de sesión establecido por el usuario (a través de `/rename`)                              |
| `firstPrompt`  | `string \| undefined` | Primer mensaje de usuario significativo en la sesión                                             |
| `gitBranch`    | `string \| undefined` | Rama Git al final de la sesión                                                                   |
| `cwd`          | `string \| undefined` | Directorio de trabajo para la sesión                                                             |
| `tag`          | `string \| undefined` | Etiqueta de sesión establecida por el usuario (vea [`tagSession()`](#tagsession))                |
| `createdAt`    | `number \| undefined` | Hora de creación en milisegundos desde la época, de la marca de tiempo de la primera entrada     |

#### Ejemplo

Imprima las 10 sesiones más recientes para un proyecto. Los resultados se ordenan por `lastModified` descendente, por lo que el primer elemento es el más nuevo. Omita `dir` para buscar en todos los proyectos.

```typescript theme={null}
import { listSessions } from "@anthropic-ai/claude-agent-sdk";

const sessions = await listSessions({ dir: "/path/to/project", limit: 10 });

for (const session of sessions) {
  console.log(`${session.summary} (${session.sessionId})`);
}
```

### `getSessionMessages()`

Lee mensajes de usuario y asistente de una transcripción de sesión pasada.

```typescript theme={null}
function getSessionMessages(
  sessionId: string,
  options?: GetSessionMessagesOptions
): Promise<SessionMessage[]>;
```

#### Parámetros

| Parámetro        | Tipo     | Predeterminado | Descripción                                                                                    |
| :--------------- | :------- | :------------- | :--------------------------------------------------------------------------------------------- |
| `sessionId`      | `string` | requerido      | UUID de sesión a leer (vea `listSessions()`)                                                   |
| `options.dir`    | `string` | `undefined`    | Directorio de proyecto para encontrar la sesión. Cuando se omite, busca en todos los proyectos |
| `options.limit`  | `number` | `undefined`    | Número máximo de mensajes a devolver                                                           |
| `options.offset` | `number` | `undefined`    | Número de mensajes a omitir desde el inicio                                                    |

#### Tipo de retorno: `SessionMessage`

| Propiedad            | Tipo                    | Descripción                                            |
| :------------------- | :---------------------- | :----------------------------------------------------- |
| `type`               | `"user" \| "assistant"` | Rol del mensaje                                        |
| `uuid`               | `string`                | Identificador de mensaje único                         |
| `session_id`         | `string`                | Sesión a la que pertenece este mensaje                 |
| `message`            | `unknown`               | Carga útil de mensaje sin procesar de la transcripción |
| `parent_tool_use_id` | `null`                  | Reservado                                              |

#### Ejemplo

```typescript theme={null}
import { listSessions, getSessionMessages } from "@anthropic-ai/claude-agent-sdk";

const [latest] = await listSessions({ dir: "/path/to/project", limit: 1 });

if (latest) {
  const messages = await getSessionMessages(latest.sessionId, {
    dir: "/path/to/project",
    limit: 20
  });

  for (const msg of messages) {
    console.log(`[${msg.type}] ${msg.uuid}`);
  }
}
```

### `getSessionInfo()`

Lee metadatos para una única sesión por ID sin escanear el directorio de proyecto completo.

```typescript theme={null}
function getSessionInfo(
  sessionId: string,
  options?: GetSessionInfoOptions
): Promise<SDKSessionInfo | undefined>;
```

#### Parámetros

| Parámetro     | Tipo     | Predeterminado | Descripción                                                                                   |
| :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------- |
| `sessionId`   | `string` | requerido      | UUID de la sesión a buscar                                                                    |
| `options.dir` | `string` | `undefined`    | Ruta del directorio del proyecto. Cuando se omite, busca en todos los directorios de proyecto |

Devuelve [`SDKSessionInfo`](#return-type-sdksessioninfo), o `undefined` si la sesión no se encuentra.

### `renameSession()`

Cambia el nombre de una sesión añadiendo una entrada de título personalizado. Las llamadas repetidas son seguras; el título más reciente gana.

```typescript theme={null}
function renameSession(
  sessionId: string,
  title: string,
  options?: SessionMutationOptions
): Promise<void>;
```

#### Parámetros

| Parámetro     | Tipo     | Predeterminado | Descripción                                                                                   |
| :------------ | :------- | :------------- | :-------------------------------------------------------------------------------------------- |
| `sessionId`   | `string` | requerido      | UUID de la sesión a renombrar                                                                 |
| `title`       | `string` | requerido      | Nuevo título. Debe ser no vacío después de recortar espacios en blanco                        |
| `options.dir` | `string` | `undefined`    | Ruta del directorio del proyecto. Cuando se omite, busca en todos los directorios de proyecto |

### `tagSession()`

Etiqueta una sesión. Pase `null` para borrar la etiqueta. Las llamadas repetidas son seguras; la etiqueta más reciente gana.

```typescript theme={null}
function tagSession(
  sessionId: string,
  tag: string | null,
  options?: SessionMutationOptions
): Promise<void>;
```

#### Parámetros

| Parámetro     | Tipo             | Predeterminado | Descripción                                                                                   |
| :------------ | :--------------- | :------------- | :-------------------------------------------------------------------------------------------- |
| `sessionId`   | `string`         | requerido      | UUID de la sesión a etiquetar                                                                 |
| `tag`         | `string \| null` | requerido      | Cadena de etiqueta, o `null` para borrar                                                      |
| `options.dir` | `string`         | `undefined`    | Ruta del directorio del proyecto. Cuando se omite, busca en todos los directorios de proyecto |

### `resolveSettings()`

Resuelve la configuración efectiva de Claude Code para un directorio determinado utilizando el mismo motor de fusión que la CLI, sin generar la CLI de Claude. Úselo para inspeccionar qué configuración vería una llamada a `query()` antes de invocar una.

<Note>
  Esta función es alfa y su API puede cambiar antes de la estabilización. Lee fuentes MDM, incluidas plist de macOS y HKLM/HKCU de Windows, para paridad con el inicio de la CLI, pero no ejecuta el subproceso `policyHelper` configurado por el administrador. El campo `permissions.defaultMode` se devuelve tal como está de todos los niveles, incluida la configuración del proyecto. El filtro de confianza que la CLI aplica antes de honrar los modos de permiso escalonados no se aplica.
</Note>

```typescript theme={null}
function resolveSettings(
  options?: ResolveSettingsOptions
): Promise<ResolvedSettings>;
```

#### Parámetros

`resolveSettings()` acepta un único objeto de opciones. Todos los campos son opcionales.

| Parámetro                       | Tipo                                  | Predeterminado    | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------ | :------------------------------------ | :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `options.cwd`                   | `string`                              | `process.cwd()`   | Directorio para resolver la configuración del proyecto y local relativa a                                                                                                                                                                                                                                                                                                                                                                                       |
| `options.settingSources`        | [`SettingSource`](#settingsource)`[]` | Todas las fuentes | Qué fuentes del sistema de archivos cargar. Pase `[]` para omitir la configuración del usuario, proyecto y local. La configuración de políticas administradas se carga en todos los casos                                                                                                                                                                                                                                                                       |
| `options.managedSettings`       | `Settings`                            | `undefined`       | Configuración de política restrictiva suministrada por el host de incrustación. Se descarta por defecto cuando una política administrada implementada por el administrador está presente; se fusiona bajo ese nivel cuando [`parentSettingsBehavior`](/es/settings#available-settings) es `"merge"`. Las claves no restrictivas como `model` se descartan silenciosamente para que esta opción pueda restringir la política administrada pero no flexibilizarla |
| `options.serverManagedSettings` | `Settings`                            | `undefined`       | Carga útil de configuración administrada por servidor desde `/api/claude_code/settings`. Las claves no restrictivas pasan sin filtrar                                                                                                                                                                                                                                                                                                                           |

#### Tipo de retorno: `ResolvedSettings`

`resolveSettings()` devuelve un objeto que describe la configuración fusionada y la fuente que contribuyó a cada clave.

| Propiedad    | Tipo                                                | Descripción                                                                                      |
| :----------- | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| `effective`  | `Settings`                                          | Configuración fusionada después de aplicar todas las fuentes habilitadas en orden de precedencia |
| `provenance` | `Partial<Record<keyof Settings, ProvenanceEntry>>`  | Para cada clave de nivel superior en `effective`, qué fuente suministró el valor                 |
| `sources`    | `Array<{ source, settings, path?, policyOrigin? }>` | Configuración sin procesar por fuente, ordenada de precedencia más baja a más alta               |

#### Ejemplo

El ejemplo a continuación resuelve la configuración para un directorio de proyecto e imprime la fuente que controla el período de limpieza.

```typescript theme={null}
import { resolveSettings } from "@anthropic-ai/claude-agent-sdk";

const { effective, provenance } = await resolveSettings({
  cwd: "/path/to/project",
  settingSources: ["user", "project", "local"],
});

console.log(`Cleanup period: ${effective.cleanupPeriodDays} days`);
console.log(`Set by: ${provenance.cleanupPeriodDays?.source}`);
```

## Tipos

### `Options`

Objeto de configuración para la función `query()`.

| Propiedad                         | Tipo                                                                                                     | Predeterminado                                     | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------- | :------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `abortController`                 | `AbortController`                                                                                        | `new AbortController()`                            | Controlador para cancelar operaciones                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `additionalDirectories`           | `string[]`                                                                                               | `[]`                                               | Directorios adicionales a los que Claude puede acceder                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `agent`                           | `string`                                                                                                 | `undefined`                                        | Nombre del agente para el hilo principal. El agente debe estar definido en la opción `agents` o en la configuración                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `agents`                          | `Record<string, [`AgentDefinition`](#agentdefinition)>`                                                  | `undefined`                                        | Defina subagentes mediante programación                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `allowDangerouslySkipPermissions` | `boolean`                                                                                                | `false`                                            | Habilite omitir permisos. Requerido cuando se usa `permissionMode: 'bypassPermissions'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `allowedTools`                    | `string[]`                                                                                               | `[]`                                               | Herramientas para aprobar automáticamente sin solicitar. Esto no restringe Claude a solo estas herramientas; las herramientas no listadas caen en `permissionMode` y `canUseTool`. Use `disallowedTools` para bloquear herramientas. Vea [Permisos](/es/agent-sdk/permissions#allow-and-deny-rules)                                                                                                                                                                                                                                                              |
| `betas`                           | [`SdkBeta`](#sdkbeta)`[]`                                                                                | `[]`                                               | Habilite características beta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `canUseTool`                      | [`CanUseTool`](#canusetool)                                                                              | `undefined`                                        | Función de permiso personalizado para el uso de herramientas                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `continue`                        | `boolean`                                                                                                | `false`                                            | Continúe la conversación más reciente                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `cwd`                             | `string`                                                                                                 | `process.cwd()`                                    | Directorio de trabajo actual                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `debug`                           | `boolean`                                                                                                | `false`                                            | Habilite el modo de depuración para el proceso de Claude Code                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `debugFile`                       | `string`                                                                                                 | `undefined`                                        | Escriba registros de depuración en una ruta de archivo específica. Habilita implícitamente el modo de depuración                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `disallowedTools`                 | `string[]`                                                                                               | `[]`                                               | Herramientas a negar siempre. Las reglas de negación se verifican primero e anulan `allowedTools` y `permissionMode` (incluyendo `bypassPermissions`)                                                                                                                                                                                                                                                                                                                                                                                                            |
| `effort`                          | `'low' \| 'medium' \| 'high' \| 'xhigh' \| 'max'`                                                        | `'high'`                                           | Controla cuánto esfuerzo pone Claude en su respuesta. Funciona con el pensamiento adaptativo para guiar la profundidad del pensamiento                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `enableFileCheckpointing`         | `boolean`                                                                                                | `false`                                            | Habilite el seguimiento de cambios de archivo para rebobinar. Vea [File checkpointing](/es/agent-sdk/file-checkpointing)                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `env`                             | `Record<string, string \| undefined>`                                                                    | `process.env`                                      | Variables de entorno. Vea [Variables de entorno](/es/env-vars) para variables que la CLI subyacente lee, y [Manejar respuestas de API lentas o estancadas](#handle-slow-or-stalled-api-responses) para variables relacionadas con tiempos de espera. Establezca `CLAUDE_AGENT_SDK_CLIENT_APP` para identificar su aplicación en el encabezado User-Agent                                                                                                                                                                                                         |
| `executable`                      | `'bun' \| 'deno' \| 'node'`                                                                              | Detectado automáticamente                          | Tiempo de ejecución de JavaScript a usar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `executableArgs`                  | `string[]`                                                                                               | `[]`                                               | Argumentos a pasar al ejecutable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `extraArgs`                       | `Record<string, string \| null>`                                                                         | `{}`                                               | Argumentos adicionales                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `fallbackModel`                   | `string`                                                                                                 | `undefined`                                        | Modelo a usar si el principal falla                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `forkSession`                     | `boolean`                                                                                                | `false`                                            | Cuando se reanuda con `resume`, bifurque a un nuevo ID de sesión en lugar de continuar la sesión original                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `hooks`                           | `Partial<Record<`[`HookEvent`](#hookevent)`, `[`HookCallbackMatcher`](#hookcallbackmatcher)`[]>>`        | `{}`                                               | Devoluciones de llamada de hooks para eventos                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `includeHookEvents`               | `boolean`                                                                                                | `false`                                            | Incluya eventos del ciclo de vida de hooks en la transmisión de mensajes como [`SDKHookStartedMessage`](#sdkhookstartedmessage), [`SDKHookProgressMessage`](#sdkhookprogressmessage), y [`SDKHookResponseMessage`](#sdkhookresponsemessage)                                                                                                                                                                                                                                                                                                                      |
| `includePartialMessages`          | `boolean`                                                                                                | `false`                                            | Incluya eventos de mensaje parcial                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `maxBudgetUsd`                    | `number`                                                                                                 | `undefined`                                        | Detenga la consulta cuando la estimación de costo del lado del cliente alcance este valor en USD. Comparado con la misma estimación que `total_cost_usd`; vea [Rastrear costo y uso](/es/agent-sdk/cost-tracking) para advertencias de precisión                                                                                                                                                                                                                                                                                                                 |
| `maxThinkingTokens`               | `number`                                                                                                 | `undefined`                                        | *Deprecado:* Use `thinking` en su lugar. Tokens máximos para el proceso de pensamiento                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `maxTurns`                        | `number`                                                                                                 | `undefined`                                        | Número máximo de turnos agentes (viajes de ronda de uso de herramientas)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `mcpServers`                      | `Record<string, [`McpServerConfig`](#mcpserverconfig)>`                                                  | `{}`                                               | Configuraciones de servidor MCP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `model`                           | `string`                                                                                                 | Predeterminado de CLI                              | Modelo Claude a usar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `outputFormat`                    | `{ type: 'json_schema', schema: JSONSchema }`                                                            | `undefined`                                        | Defina el formato de salida para los resultados del agente. Vea [Structured outputs](/es/agent-sdk/structured-outputs) para detalles                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `outputStyle`                     | `string`                                                                                                 | `undefined`                                        | Nombre de un [estilo de salida](/es/output-styles) para activar para la sesión. El estilo debe existir en una ubicación `settingSources` cargada, como `.claude/output-styles/`. Vea [Activar un estilo de salida](/es/agent-sdk/modifying-system-prompts#activate-an-output-style)                                                                                                                                                                                                                                                                              |
| `pathToClaudeCodeExecutable`      | `string`                                                                                                 | Auto-resuelto desde el binario nativo incluido     | Ruta al ejecutable de Claude Code. Solo se necesita si las dependencias opcionales se omitieron durante la instalación o su plataforma no está en el conjunto compatible                                                                                                                                                                                                                                                                                                                                                                                         |
| `permissionMode`                  | [`PermissionMode`](#permissionmode)                                                                      | `'default'`                                        | Modo de permiso para la sesión                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `permissionPromptToolName`        | `string`                                                                                                 | `undefined`                                        | Nombre de herramienta MCP para solicitudes de permiso                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `persistSession`                  | `boolean`                                                                                                | `true`                                             | Cuando es `false`, deshabilita la persistencia de sesión en disco. Las sesiones no se pueden reanudar más tarde                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `plugins`                         | [`SdkPluginConfig`](#sdkpluginconfig)`[]`                                                                | `[]`                                               | Cargue plugins personalizados desde rutas locales. Vea [Plugins](/es/agent-sdk/plugins) para detalles                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `promptSuggestions`               | `boolean`                                                                                                | `false`                                            | Habilite sugerencias de mensaje. Emite un mensaje `prompt_suggestion` después de cada turno con un mensaje de usuario predicho siguiente                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `resume`                          | `string`                                                                                                 | `undefined`                                        | ID de sesión a reanudar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `resumeSessionAt`                 | `string`                                                                                                 | `undefined`                                        | Reanude la sesión en un UUID de mensaje específico                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `sandbox`                         | [`SandboxSettings`](#sandboxsettings)                                                                    | `undefined`                                        | Configure el comportamiento de sandbox mediante programación. Vea [Sandbox settings](#sandboxsettings) para detalles                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `sessionId`                       | `string`                                                                                                 | Auto-generado                                      | Use un UUID específico para la sesión en lugar de generar uno automáticamente                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `sessionStore`                    | [`SessionStore`](/es/agent-sdk/session-storage#the-sessionstore-interface)                               | `undefined`                                        | Refleje transcripciones de sesión en un backend externo para que cualquier host pueda reanudarlas. Vea [Persistir sesiones en almacenamiento externo](/es/agent-sdk/session-storage)                                                                                                                                                                                                                                                                                                                                                                             |
| `settings`                        | `string \| Settings`                                                                                     | `undefined`                                        | Objeto de [configuración](/es/settings) en línea o ruta a un archivo de configuración. Completa la capa de configuración de marca en el [orden de precedencia](/es/settings#settings-precedence). Cambie en tiempo de ejecución con [`applyFlagSettings()`](#applyflagsettings)                                                                                                                                                                                                                                                                                  |
| `settingSources`                  | [`SettingSource`](#settingsource)`[]`                                                                    | Valores predeterminados de CLI (todas las fuentes) | Controle qué configuración del sistema de archivos cargar. Pase `[]` para deshabilitar la configuración de usuario, proyecto y local. La configuración de política administrada se carga independientemente. Vea [Usar características de Claude Code](/es/agent-sdk/claude-code-features#what-settingsources-does-not-control)                                                                                                                                                                                                                                  |
| `skills`                          | `string[] \| 'all'`                                                                                      | `undefined`                                        | Skills disponibles para la sesión. Pase `'all'` para habilitar cada skill descubierto, o una lista de nombres de skills. Cuando se establece, el SDK habilita la herramienta Skill automáticamente sin enumerarla en `allowedTools`. Vea [Skills](/es/agent-sdk/skills)                                                                                                                                                                                                                                                                                          |
| `spawnClaudeCodeProcess`          | `(options: SpawnOptions) => SpawnedProcess`                                                              | `undefined`                                        | Función personalizada para generar el proceso de Claude Code. Use para ejecutar Claude Code en máquinas virtuales, contenedores o entornos remotos                                                                                                                                                                                                                                                                                                                                                                                                               |
| `stderr`                          | `(data: string) => void`                                                                                 | `undefined`                                        | Devolución de llamada para salida de stderr                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `strictMcpConfig`                 | `boolean`                                                                                                | `false`                                            | Aplique validación MCP estricta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `systemPrompt`                    | `string \| { type: 'preset'; preset: 'claude_code'; append?: string; excludeDynamicSections?: boolean }` | `undefined` (mensaje mínimo)                       | Configuración de mensaje del sistema. Pase una cadena para un mensaje personalizado, o `{ type: 'preset', preset: 'claude_code' }` para usar el mensaje del sistema de Claude Code. Cuando use la forma de objeto preestablecido, agregue `append` para extenderlo con instrucciones adicionales, y establezca `excludeDynamicSections: true` para mover el contexto por sesión al primer mensaje de usuario para [mejor reutilización de caché de mensaje en máquinas](/es/agent-sdk/modifying-system-prompts#improve-prompt-caching-across-users-and-machines) |
| `thinking`                        | [`ThinkingConfig`](#thinkingconfig)                                                                      | `{ type: 'adaptive' }` para modelos compatibles    | Controla el comportamiento de pensamiento/razonamiento de Claude. Vea [`ThinkingConfig`](#thinkingconfig) para opciones                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `toolConfig`                      | [`ToolConfig`](#toolconfig)                                                                              | `undefined`                                        | Configuración para el comportamiento de herramientas integradas. Vea [`ToolConfig`](#toolconfig) para detalles                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `tools`                           | `string[] \| { type: 'preset'; preset: 'claude_code' }`                                                  | `undefined`                                        | Configuración de herramientas. Pase una matriz de nombres de herramientas o use el preestablecido para obtener las herramientas predeterminadas de Claude Code                                                                                                                                                                                                                                                                                                                                                                                                   |

#### Manejar respuestas de API lentas o estancadas

El subproceso CLI lee varias variables de entorno que controlan los tiempos de espera de API y la detección de estancamiento. Páselas a través de la opción `env`:

```typescript theme={null}
const result = query({
  prompt: "Analyze this code",
  options: {
    env: {
      ...process.env,
      API_TIMEOUT_MS: "120000",
      CLAUDE_CODE_MAX_RETRIES: "2",
      CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS: "120000",
    },
  },
});
```

* `API_TIMEOUT_MS`: tiempo de espera por solicitud en el cliente de Anthropic, en milisegundos. Predeterminado `600000`. Se aplica al bucle principal y a todos los subagentes.
* `CLAUDE_CODE_MAX_RETRIES`: máximo de reintentos de API. Predeterminado `10`. Cada reintento obtiene su propia ventana `API_TIMEOUT_MS`, por lo que el tiempo de pared en el peor caso es aproximadamente `API_TIMEOUT_MS × (CLAUDE_CODE_MAX_RETRIES + 1)` más retroceso.
* `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS`: perro guardián de estancamiento para subagentes lanzados con `run_in_background`. Predeterminado `600000`. Se reinicia en cada evento de transmisión; en caso de estancamiento, aborta el subagente, marca la tarea como fallida y expone el error al padre con cualquier resultado parcial. No se aplica a subagentes síncronos.
* `CLAUDE_ENABLE_STREAM_WATCHDOG=1` con `CLAUDE_STREAM_IDLE_TIMEOUT_MS`: aborta la solicitud cuando los encabezados han llegado pero el cuerpo de respuesta deja de transmitirse. Desactivado de forma predeterminada. `CLAUDE_STREAM_IDLE_TIMEOUT_MS` tiene un valor predeterminado de `300000` y se fija a ese mínimo. La solicitud abortada pasa por la ruta de reintento normal.

### Objeto `Query`

Interfaz devuelta por la función `query()`.

```typescript theme={null}
interface Query extends AsyncGenerator<SDKMessage, void> {
  interrupt(): Promise<void>;
  rewindFiles(
    userMessageId: string,
    options?: { dryRun?: boolean }
  ): Promise<RewindFilesResult>;
  setPermissionMode(mode: PermissionMode): Promise<void>;
  setModel(model?: string): Promise<void>;
  setMaxThinkingTokens(maxThinkingTokens: number | null): Promise<void>;
  applyFlagSettings(settings: { [K in keyof Settings]?: Settings[K] | null }): Promise<void>;
  initializationResult(): Promise<SDKControlInitializeResponse>;
  supportedCommands(): Promise<SlashCommand[]>;
  supportedModels(): Promise<ModelInfo[]>;
  supportedAgents(): Promise<AgentInfo[]>;
  mcpServerStatus(): Promise<McpServerStatus[]>;
  accountInfo(): Promise<AccountInfo>;
  reconnectMcpServer(serverName: string): Promise<void>;
  toggleMcpServer(serverName: string, enabled: boolean): Promise<void>;
  setMcpServers(servers: Record<string, McpServerConfig>): Promise<McpSetServersResult>;
  streamInput(stream: AsyncIterable<SDKUserMessage>): Promise<void>;
  stopTask(taskId: string): Promise<void>;
  close(): void;
}
```

#### Métodos

| Método                                 | Descripción                                                                                                                                                                                                                                     |
| :------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `interrupt()`                          | Interrumpe la consulta (solo disponible en modo de entrada de transmisión)                                                                                                                                                                      |
| `rewindFiles(userMessageId, options?)` | Restaura archivos a su estado en el mensaje de usuario especificado. Pase `{ dryRun: true }` para obtener una vista previa de los cambios. Requiere `enableFileCheckpointing: true`. Vea [File checkpointing](/es/agent-sdk/file-checkpointing) |
| `setPermissionMode()`                  | Cambia el modo de permiso (solo disponible en modo de entrada de transmisión)                                                                                                                                                                   |
| `setModel()`                           | Cambia el modelo (solo disponible en modo de entrada de transmisión)                                                                                                                                                                            |
| `setMaxThinkingTokens()`               | *Deprecado:* Use la opción `thinking` en su lugar. Cambia los tokens de pensamiento máximos                                                                                                                                                     |
| `applyFlagSettings(settings)`          | Fusiona la configuración en la capa de configuración de marca de la sesión en tiempo de ejecución (solo disponible en modo de entrada de transmisión). Vea [`applyFlagSettings()`](#applyflagsettings)                                          |
| `initializationResult()`               | Devuelve el resultado de inicialización completo incluyendo comandos compatibles, modelos, información de cuenta y configuración de estilo de salida                                                                                            |
| `supportedCommands()`                  | Devuelve comandos slash disponibles                                                                                                                                                                                                             |
| `supportedModels()`                    | Devuelve modelos disponibles con información de visualización                                                                                                                                                                                   |
| `supportedAgents()`                    | Devuelve subagentes disponibles como [`AgentInfo`](#agentinfo)`[]`                                                                                                                                                                              |
| `mcpServerStatus()`                    | Devuelve el estado de los servidores MCP conectados                                                                                                                                                                                             |
| `accountInfo()`                        | Devuelve información de cuenta                                                                                                                                                                                                                  |
| `reconnectMcpServer(serverName)`       | Reconecte un servidor MCP por nombre                                                                                                                                                                                                            |
| `toggleMcpServer(serverName, enabled)` | Habilite o deshabilite un servidor MCP por nombre                                                                                                                                                                                               |
| `setMcpServers(servers)`               | Reemplace dinámicamente el conjunto de servidores MCP para esta sesión. Devuelve información sobre qué servidores se agregaron, eliminaron y cualquier error                                                                                    |
| `streamInput(stream)`                  | Transmita mensajes de entrada a la consulta para conversaciones de múltiples turnos                                                                                                                                                             |
| `stopTask(taskId)`                     | Detenga una tarea de fondo en ejecución por ID                                                                                                                                                                                                  |
| `close()`                              | Cierre la consulta y termine el proceso subyacente. Finaliza forzadamente la consulta y limpia todos los recursos                                                                                                                               |

#### `applyFlagSettings()`

Cambia cualquier [configuración](/es/settings) en una sesión en ejecución sin reiniciar la consulta. Úselo cuando una configuración que no tiene un setter dedicado necesite cambiar a mitad de sesión, como restringir `permissions` después de que el agente lea entrada no confiable. `setModel()` y `setPermissionMode()` son setters dedicados para esas dos claves; `applyFlagSettings()` es la forma general que acepta cualquier subconjunto de las claves de configuración, y pasar `model` aquí se comporta igual que `setModel()`.

Los valores se escriben en la capa de configuración de marca, la misma capa que la opción `settings` en línea de `query()` completa al inicio. La configuración de marca se encuentra cerca de la parte superior del [orden de precedencia de configuración](/es/settings#settings-precedence): anulan la configuración de usuario, proyecto y local, y solo la configuración de política administrada puede anularlas. Esta es la misma capa que la [sección de precedencia en la página](#settings-precedence) llama opciones programáticas.

Las llamadas sucesivas fusionan superficialmente las claves de nivel superior. Una segunda llamada con `{ permissions: {...} }` reemplaza el objeto `permissions` completo de la llamada anterior en lugar de fusionarse profundamente en él. Para borrar una clave de la capa de marca y recurrir a fuentes de menor precedencia, pase `null` para esa clave. Pasar `undefined` no tiene efecto porque la serialización JSON lo elimina.

Solo disponible en modo de entrada de transmisión, la misma restricción que `setModel()` y `setPermissionMode()`.

El ejemplo a continuación cambia el modelo activo a mitad de sesión, luego borra la anulación para que el modelo recurra a lo que especifique la configuración del usuario o proyecto.

```typescript theme={null}
const q = query({ prompt: messageStream });

// Anule el modelo para el resto de la sesión
await q.applyFlagSettings({ model: "claude-opus-4-6" });

// Más tarde: borre la anulación y recurra a la configuración de menor precedencia
await q.applyFlagSettings({ model: null });
```

<Note>
  `applyFlagSettings()` es solo TypeScript. El SDK de Python no expone un método equivalente.
</Note>

### `WarmQuery`

Identificador devuelto por [`startup()`](#startup). El subproceso ya está generado e inicializado, por lo que llamar a `query()` en este identificador escribe el mensaje directamente en un proceso listo sin latencia de inicio.

```typescript theme={null}
interface WarmQuery extends AsyncDisposable {
  query(prompt: string | AsyncIterable<SDKUserMessage>): Query;
  close(): void;
}
```

#### Métodos

| Método          | Descripción                                                                                                                      |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| `query(prompt)` | Envíe un mensaje al subproceso precalentado y devuelva un [`Query`](#query-object). Solo se puede llamar una vez por `WarmQuery` |
| `close()`       | Cierre el subproceso sin enviar un mensaje. Use esto para descartar una consulta cálida que ya no es necesaria                   |

`WarmQuery` implementa `AsyncDisposable`, por lo que se puede usar con `await using` para limpieza automática.

### `SDKControlInitializeResponse`

Tipo de retorno de `initializationResult()`. Contiene datos de inicialización de sesión.

```typescript theme={null}
type SDKControlInitializeResponse = {
  commands: SlashCommand[];
  agents: AgentInfo[];
  output_style: string;
  available_output_styles: string[];
  models: ModelInfo[];
  account: AccountInfo;
  fast_mode_state?: "off" | "cooldown" | "on";
};
```

### `AgentDefinition`

Configuración para un subagente definido mediante programación.

```typescript theme={null}
type AgentDefinition = {
  description: string;
  tools?: string[];
  disallowedTools?: string[];
  prompt: string;
  model?: string;
  mcpServers?: AgentMcpServerSpec[];
  skills?: string[];
  initialPrompt?: string;
  maxTurns?: number;
  background?: boolean;
  memory?: "user" | "project" | "local";
  effort?: "low" | "medium" | "high" | "xhigh" | "max" | number;
  permissionMode?: PermissionMode;
  criticalSystemReminder_EXPERIMENTAL?: string;
};
```

| Campo                                 | Requerido | Descripción                                                                                                                                                                                                    |
| :------------------------------------ | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `description`                         | Sí        | Descripción en lenguaje natural de cuándo usar este agente                                                                                                                                                     |
| `tools`                               | No        | Matriz de nombres de herramientas permitidas. Si se omite, hereda todas las herramientas del padre. Para precargar Skills en el contexto del agente, use el campo `skills` en lugar de enumerar `'Skill'` aquí |
| `disallowedTools`                     | No        | Matriz de nombres de herramientas a desautorizar explícitamente para este agente                                                                                                                               |
| `prompt`                              | Sí        | El mensaje del sistema del agente                                                                                                                                                                              |
| `model`                               | No        | Anulación de modelo para este agente. Acepta un alias como `'sonnet'`, `'opus'`, `'haiku'`, `'inherit'`, o un ID de modelo completo. Si se omite o es `'inherit'`, usa el modelo principal                     |
| `mcpServers`                          | No        | Especificaciones de servidor MCP para este agente                                                                                                                                                              |
| `skills`                              | No        | Matriz de nombres de skills a precargar en el contexto del agente                                                                                                                                              |
| `initialPrompt`                       | No        | Auto-enviado como el primer turno de usuario cuando este agente se ejecuta como el agente del hilo principal                                                                                                   |
| `maxTurns`                            | No        | Número máximo de turnos agentes (viajes de ronda de API) antes de detener                                                                                                                                      |
| `background`                          | No        | Ejecute este agente como una tarea de fondo no bloqueante cuando se invoque                                                                                                                                    |
| `memory`                              | No        | Fuente de memoria para este agente: `'user'`, `'project'`, o `'local'`                                                                                                                                         |
| `effort`                              | No        | Nivel de esfuerzo de razonamiento para este agente. Acepta un nivel nombrado o un entero                                                                                                                       |
| `permissionMode`                      | No        | Modo de permiso para la ejecución de herramientas dentro de este agente. Vea [`PermissionMode`](#permissionmode)                                                                                               |
| `criticalSystemReminder_EXPERIMENTAL` | No        | Experimental: Recordatorio crítico agregado al mensaje del sistema                                                                                                                                             |

### `AgentMcpServerSpec`

Especifica servidores MCP disponibles para un subagente. Puede ser un nombre de servidor (cadena que hace referencia a un servidor de la configuración `mcpServers` del padre) o una configuración de servidor en línea que mapea nombres de servidor a configuraciones.

```typescript theme={null}
type AgentMcpServerSpec = string | Record<string, McpServerConfigForProcessTransport>;
```

Donde `McpServerConfigForProcessTransport` es `McpStdioServerConfig | McpSSEServerConfig | McpHttpServerConfig | McpSdkServerConfig`.

### `SettingSource`

Controla qué fuentes de configuración basadas en el sistema de archivos carga el SDK.

```typescript theme={null}
type SettingSource = "user" | "project" | "local";
```

| Valor       | Descripción                                                   | Ubicación                     |
| :---------- | :------------------------------------------------------------ | :---------------------------- |
| `'user'`    | Configuración global del usuario                              | `~/.claude/settings.json`     |
| `'project'` | Configuración de proyecto compartida (controlada por versión) | `.claude/settings.json`       |
| `'local'`   | Configuración de proyecto local (gitignored)                  | `.claude/settings.local.json` |

#### Comportamiento predeterminado

Cuando `settingSources` se omite o es `undefined`, `query()` carga la misma configuración del sistema de archivos que la CLI de Claude Code: usuario, proyecto y local. La configuración de política administrada se carga en todos los casos. Vea [Qué settingSources no controla](/es/agent-sdk/claude-code-features#what-settingsources-does-not-control) para entradas que se leen independientemente de esta opción, y cómo deshabilitarlas.

#### Por qué usar settingSources

**Deshabilitar configuración del sistema de archivos:**

```typescript theme={null}
// No cargue la configuración de usuario, proyecto o local desde el disco
const result = query({
  prompt: "Analyze this code",
  options: { settingSources: [] }
});
```

**Cargue toda la configuración del sistema de archivos explícitamente:**

```typescript theme={null}
const result = query({
  prompt: "Analyze this code",
  options: {
    settingSources: ["user", "project", "local"] // Cargue toda la configuración
  }
});
```

**Cargue solo fuentes de configuración específicas:**

```typescript theme={null}
// Cargue solo la configuración del proyecto, ignore usuario y local
const result = query({
  prompt: "Run CI checks",
  options: {
    settingSources: ["project"] // Solo .claude/settings.json
  }
});
```

**Entornos de prueba e IC:**

```typescript theme={null}
// Asegure un comportamiento consistente en IC excluyendo la configuración local
const result = query({
  prompt: "Run tests",
  options: {
    settingSources: ["project"], // Solo configuración compartida del equipo
    permissionMode: "bypassPermissions"
  }
});
```

**Aplicaciones solo SDK:**

```typescript theme={null}
// Defina todo mediante programación.
// Pase [] para optar por no usar fuentes de configuración del sistema de archivos.
const result = query({
  prompt: "Review this PR",
  options: {
    settingSources: [],
    agents: {
      /* ... */
    },
    mcpServers: {
      /* ... */
    },
    allowedTools: ["Read", "Grep", "Glob"]
  }
});
```

**Cargando instrucciones de proyecto CLAUDE.md:**

```typescript theme={null}
// Cargue la configuración del proyecto para incluir archivos CLAUDE.md
const result = query({
  prompt: "Add a new feature following project conventions",
  options: {
    systemPrompt: {
      type: "preset",
      preset: "claude_code" // Use el mensaje del sistema de Claude Code
    },
    settingSources: ["project"], // Carga CLAUDE.md del directorio del proyecto
    allowedTools: ["Read", "Write", "Edit"]
  }
});
```

#### Precedencia de configuración

Cuando se cargan múltiples fuentes, la configuración se fusiona con esta precedencia (mayor a menor):

1. Configuración local (`.claude/settings.local.json`)
2. Configuración del proyecto (`.claude/settings.json`)
3. Configuración del usuario (`~/.claude/settings.json`)

Las opciones programáticas como `agents`, `allowedTools` y `settings` anulan la configuración del sistema de archivos de usuario, proyecto y local. La configuración de política administrada tiene precedencia sobre las opciones programáticas.

### `PermissionMode`

```typescript theme={null}
type PermissionMode =
  | "default" // Comportamiento de permiso estándar
  | "acceptEdits" // Auto-aceptar ediciones de archivo
  | "bypassPermissions" // Omitir todas las verificaciones de permiso
  | "plan" // Modo de planificación - solo herramientas de lectura
  | "dontAsk" // No solicitar permisos, negar si no está preaprobado
  | "auto"; // Usar un clasificador de modelo para aprobar o negar cada llamada de herramienta
```

### `CanUseTool`

Tipo de función de permiso personalizado para controlar el uso de herramientas.

```typescript theme={null}
type CanUseTool = (
  toolName: string,
  input: Record<string, unknown>,
  options: {
    signal: AbortSignal;
    suggestions?: PermissionUpdate[];
    blockedPath?: string;
    decisionReason?: string;
    toolUseID: string;
    agentID?: string;
  }
) => Promise<PermissionResult>;
```

| Opción           | Tipo                                        | Descripción                                                                                                                                                                                                                                                                                                                                                      |
| :--------------- | :------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `signal`         | `AbortSignal`                               | Señalizado si la operación debe abortarse                                                                                                                                                                                                                                                                                                                        |
| `suggestions`    | [`PermissionUpdate`](#permissionupdate)`[]` | Actualizaciones de permiso sugeridas para que el usuario no sea solicitado nuevamente para esta herramienta. Los mensajes de Bash incluyen una sugerencia con el destino `localSettings` [destination](#permissionupdatedestination), por lo que devolverlo en `updatedPermissions` escribe la regla en `.claude/settings.local.json` y persiste entre sesiones. |
| `blockedPath`    | `string`                                    | La ruta de archivo que activó la solicitud de permiso, si corresponde                                                                                                                                                                                                                                                                                            |
| `decisionReason` | `string`                                    | Explica por qué se activó esta solicitud de permiso                                                                                                                                                                                                                                                                                                              |
| `toolUseID`      | `string`                                    | Identificador único para esta llamada de herramienta específica dentro del mensaje del asistente                                                                                                                                                                                                                                                                 |
| `agentID`        | `string`                                    | Si se ejecuta dentro de un sub-agente, el ID del sub-agente                                                                                                                                                                                                                                                                                                      |

### `PermissionResult`

Resultado de una verificación de permiso.

```typescript theme={null}
type PermissionResult =
  | {
      behavior: "allow";
      updatedInput?: Record<string, unknown>;
      updatedPermissions?: PermissionUpdate[];
      toolUseID?: string;
    }
  | {
      behavior: "deny";
      message: string;
      interrupt?: boolean;
      toolUseID?: string;
    };
```

### `ToolConfig`

Configuración para el comportamiento de herramientas integradas.

```typescript theme={null}
type ToolConfig = {
  askUserQuestion?: {
    previewFormat?: "markdown" | "html";
  };
};
```

| Campo                           | Tipo                   | Descripción                                                                                                                                                                                                   |
| :------------------------------ | :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `askUserQuestion.previewFormat` | `'markdown' \| 'html'` | Opte por el campo `preview` en las opciones de [`AskUserQuestion`](/es/agent-sdk/user-input#question-format) y establezca su formato de contenido. Cuando no está establecido, Claude no emite vistas previas |

### `McpServerConfig`

Configuración para servidores MCP.

```typescript theme={null}
type McpServerConfig =
  | McpStdioServerConfig
  | McpSSEServerConfig
  | McpHttpServerConfig
  | McpSdkServerConfigWithInstance;
```

#### `McpStdioServerConfig`

```typescript theme={null}
type McpStdioServerConfig = {
  type?: "stdio";
  command: string;
  args?: string[];
  env?: Record<string, string>;
};
```

#### `McpSSEServerConfig`

```typescript theme={null}
type McpSSEServerConfig = {
  type: "sse";
  url: string;
  headers?: Record<string, string>;
};
```

#### `McpHttpServerConfig`

```typescript theme={null}
type McpHttpServerConfig = {
  type: "http";
  url: string;
  headers?: Record<string, string>;
};
```

#### `McpSdkServerConfigWithInstance`

```typescript theme={null}
type McpSdkServerConfigWithInstance = {
  type: "sdk";
  name: string;
  instance: McpServer;
};
```

#### `McpClaudeAIProxyServerConfig`

```typescript theme={null}
type McpClaudeAIProxyServerConfig = {
  type: "claudeai-proxy";
  url: string;
  id: string;
};
```

### `SdkPluginConfig`

Configuración para cargar plugins en el SDK.

```typescript theme={null}
type SdkPluginConfig = {
  type: "local";
  path: string;
};
```

| Campo  | Tipo      | Descripción                                                       |
| :----- | :-------- | :---------------------------------------------------------------- |
| `type` | `'local'` | Debe ser `'local'` (actualmente solo se soportan plugins locales) |
| `path` | `string`  | Ruta absoluta o relativa al directorio del plugin                 |

**Ejemplo:**

```typescript theme={null}
plugins: [
  { type: "local", path: "./my-plugin" },
  { type: "local", path: "/absolute/path/to/plugin" }
];
```

Para información completa sobre la creación y uso de plugins, vea [Plugins](/es/agent-sdk/plugins).

## Tipos de Mensaje

### `SDKMessage`

Tipo de unión de todos los mensajes posibles devueltos por la consulta.

```typescript theme={null}
type SDKMessage =
  | SDKAssistantMessage
  | SDKUserMessage
  | SDKUserMessageReplay
  | SDKResultMessage
  | SDKSystemMessage
  | SDKPartialAssistantMessage
  | SDKCompactBoundaryMessage
  | SDKStatusMessage
  | SDKLocalCommandOutputMessage
  | SDKHookStartedMessage
  | SDKHookProgressMessage
  | SDKHookResponseMessage
  | SDKPluginInstallMessage
  | SDKToolProgressMessage
  | SDKAuthStatusMessage
  | SDKTaskNotificationMessage
  | SDKTaskStartedMessage
  | SDKTaskProgressMessage
  | SDKTaskUpdatedMessage
  | SDKFilesPersistedEvent
  | SDKToolUseSummaryMessage
  | SDKRateLimitEvent
  | SDKPermissionDeniedMessage
  | SDKPromptSuggestionMessage;
```

### `SDKAssistantMessage`

Mensaje de respuesta del asistente.

```typescript theme={null}
type SDKAssistantMessage = {
  type: "assistant";
  uuid: UUID;
  session_id: string;
  message: BetaMessage; // Del SDK de Anthropic
  parent_tool_use_id: string | null;
  error?: SDKAssistantMessageError;
};
```

El campo `message` es un [`BetaMessage`](https://platform.claude.com/docs/es/api/messages/create) del SDK de Anthropic. Incluye campos como `id`, `content`, `model`, `stop_reason` y `usage`.

`SDKAssistantMessageError` es uno de: `'authentication_failed'`, `'oauth_org_not_allowed'`, `'billing_error'`, `'rate_limit'`, `'invalid_request'`, `'server_error'`, `'max_output_tokens'`, o `'unknown'`.

### `SDKUserMessage`

Mensaje de entrada del usuario.

```typescript theme={null}
type SDKUserMessage = {
  type: "user";
  uuid?: UUID;
  session_id: string;
  message: MessageParam; // Del SDK de Anthropic
  parent_tool_use_id: string | null;
  isSynthetic?: boolean;
  shouldQuery?: boolean;
  tool_use_result?: unknown;
  origin?: SDKMessageOrigin;
};
```

Establezca `shouldQuery` en `false` para añadir el mensaje a la transcripción sin activar un turno del asistente. El mensaje se mantiene y se fusiona en el siguiente mensaje de usuario que sí activa un turno. Use esto para inyectar contexto, como la salida de un comando que ejecutó fuera de banda, sin gastar una llamada de modelo en él.

### `SDKUserMessageReplay`

Mensaje de usuario reproducido con UUID requerido.

```typescript theme={null}
type SDKUserMessageReplay = {
  type: "user";
  uuid: UUID;
  session_id: string;
  message: MessageParam;
  parent_tool_use_id: string | null;
  isSynthetic?: boolean;
  tool_use_result?: unknown;
  origin?: SDKMessageOrigin;
  isReplay: true;
};
```

### `SDKResultMessage`

Mensaje de resultado final.

```typescript theme={null}
type SDKResultMessage =
  | {
      type: "result";
      subtype: "success";
      uuid: UUID;
      session_id: string;
      duration_ms: number;
      duration_api_ms: number;
      is_error: boolean;
      num_turns: number;
      result: string;
      stop_reason: string | null;
      total_cost_usd: number;
      usage: NonNullableUsage;
      modelUsage: { [modelName: string]: ModelUsage };
      permission_denials: SDKPermissionDenial[];
      structured_output?: unknown;
      deferred_tool_use?: { id: string; name: string; input: Record<string, unknown> };
      origin?: SDKMessageOrigin;
    }
  | {
      type: "result";
      subtype:
        | "error_max_turns"
        | "error_during_execution"
        | "error_max_budget_usd"
        | "error_max_structured_output_retries";
      uuid: UUID;
      session_id: string;
      duration_ms: number;
      duration_api_ms: number;
      is_error: boolean;
      num_turns: number;
      stop_reason: string | null;
      total_cost_usd: number;
      usage: NonNullableUsage;
      modelUsage: { [modelName: string]: ModelUsage };
      permission_denials: SDKPermissionDenial[];
      errors: string[];
      origin?: SDKMessageOrigin;
    };
```

El campo `origin` reenvía el [`SDKMessageOrigin`](#sdkmessageorigin) del mensaje de usuario que activó este resultado. Cuando una tarea de fondo finaliza y el SDK inyecta un turno de seguimiento sintético, el `SDKResultMessage` resultante lleva `origin: { kind: "task-notification" }`. Verifique este campo para distinguir los resultados que responden a su solicitud de los resultados emitidos para seguimientos de tareas de fondo, para que pueda enrutar o suprimir estos últimos. El campo está ausente para los resultados emitidos antes de cualquier turno de usuario, como errores de inicio.

Cuando un hook `PreToolUse` devuelve `permissionDecision: "defer"`, el resultado tiene `stop_reason: "tool_deferred"` y `deferred_tool_use` lleva el `id`, `name` e `input` de la herramienta pendiente. Lea este campo para mostrar la solicitud en su propia interfaz de usuario, luego reanude con el mismo `session_id` para continuar. Consulte [Diferir una llamada de herramienta para más tarde](/es/hooks#defer-a-tool-call-for-later) para el viaje completo.

### `SDKSystemMessage`

Mensaje de inicialización del sistema.

```typescript theme={null}
type SDKSystemMessage = {
  type: "system";
  subtype: "init";
  uuid: UUID;
  session_id: string;
  agents?: string[];
  apiKeySource: ApiKeySource;
  betas?: string[];
  claude_code_version: string;
  cwd: string;
  tools: string[];
  mcp_servers: {
    name: string;
    status: string;
  }[];
  model: string;
  permissionMode: PermissionMode;
  slash_commands: string[];
  output_style: string;
  skills: string[];
  plugins: { name: string; path: string }[];
};
```

### `SDKPartialAssistantMessage`

Mensaje parcial de transmisión (solo cuando `includePartialMessages` es true).

```typescript theme={null}
type SDKPartialAssistantMessage = {
  type: "stream_event";
  event: BetaRawMessageStreamEvent; // Del SDK de Anthropic
  parent_tool_use_id: string | null;
  uuid: UUID;
  session_id: string;
};
```

### `SDKCompactBoundaryMessage`

Mensaje que indica un límite de compactación de conversación.

```typescript theme={null}
type SDKCompactBoundaryMessage = {
  type: "system";
  subtype: "compact_boundary";
  uuid: UUID;
  session_id: string;
  compact_metadata: {
    trigger: "manual" | "auto";
    pre_tokens: number;
  };
};
```

### `SDKPluginInstallMessage`

Evento de progreso de instalación de plugin. Se emite cuando [`CLAUDE_CODE_SYNC_PLUGIN_INSTALL`](/es/env-vars) está establecido, para que su aplicación Agent SDK pueda rastrear la instalación de plugins del mercado antes del primer turno. Los estados `started` y `completed` cierran la instalación general. Los estados `installed` y `failed` reportan mercados individuales e incluyen `name`.

```typescript theme={null}
type SDKPluginInstallMessage = {
  type: "system";
  subtype: "plugin_install";
  status: "started" | "installed" | "failed" | "completed";
  name?: string;
  error?: string;
  uuid: UUID;
  session_id: string;
};
```

### `SDKPermissionDeniedMessage`

Evento de transmisión emitido cuando el sistema de permisos deniega automáticamente una llamada de herramienta sin un aviso interactivo. Úselo para renderizar la denegación en su interfaz de usuario a medida que sucede, en lugar de solo observar el resultado de la herramienta `is_error` que sigue. La ruta de solicitud interactiva llega a su aplicación por separado a través de la devolución de llamada [`canUseTool`](#canusetool). Las denegaciones emitidas por un hook `PreToolUse` no se reportan a través de este evento.

Este evento requiere Claude Code v2.1.136 o posterior.

```typescript theme={null}
type SDKPermissionDeniedMessage = {
  type: "system";
  subtype: "permission_denied";
  tool_name: string;
  tool_use_id: string;
  agent_id?: string;
  decision_reason_type?: string;
  decision_reason?: string;
  message: string;
  uuid: UUID;
  session_id: string;
};
```

| Campo                  | Tipo     | Descripción                                                                                                                                           |
| ---------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tool_name`            | `string` | Nombre de la herramienta que fue denegada                                                                                                             |
| `tool_use_id`          | `string` | ID del bloque `tool_use` que esta denegación responde                                                                                                 |
| `agent_id`             | `string` | ID del subagente cuando la llamada denegada se originó dentro de un subagente. Refleja el campo en `can_use_tool` para enrutamiento del lado del host |
| `decision_reason_type` | `string` | Discriminador para el componente que decidió, como `"rule"`, `"mode"`, `"classifier"`, o `"asyncAgent"`                                               |
| `decision_reason`      | `string` | Razón legible por humanos del componente que decide, cuando está disponible                                                                           |
| `message`              | `string` | Mensaje de rechazo devuelto al modelo en el `tool_result`                                                                                             |

### `SDKPermissionDenial`

Información sobre un uso de herramienta denegado.

```typescript theme={null}
type SDKPermissionDenial = {
  tool_name: string;
  tool_use_id: string;
  tool_input: Record<string, unknown>;
};
```

### `SDKMessageOrigin`

Procedencia de un mensaje con rol de usuario. Esto aparece como `origin` en [`SDKUserMessage`](#sdkusermessage) y se reenvía al [`SDKResultMessage`](#sdkresultmessage) correspondiente para que pueda saber qué activó un turno determinado.

```typescript theme={null}
type SDKMessageOrigin =
  | { kind: "human" }
  | { kind: "channel"; server: string }
  | { kind: "peer"; from: string; name?: string }
  | { kind: "task-notification" }
  | { kind: "coordinator" };
```

| `kind`              | Significado                                                                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `human`             | Entrada directa del usuario final. En mensajes de usuario, una `origin` ausente también significa entrada humana.                                                        |
| `channel`           | Mensaje que llega en un [canal](/es/channels). `server` es el nombre del servidor MCP de origen.                                                                         |
| `peer`              | Mensaje de otra sesión de agente a través de `SendMessage`. `from` es la dirección del remitente; `name` es el nombre para mostrar del remitente cuando está disponible. |
| `task-notification` | Turno sintético inyectado después de que finalizó una tarea de fondo. Consulte [`SDKTaskNotificationMessage`](#sdktasknotificationmessage).                              |
| `coordinator`       | Mensaje de un coordinador de equipo en un [equipo de agentes](/es/agent-teams).                                                                                          |

## Tipos de Hook

Para una guía completa sobre el uso de hooks con ejemplos y patrones comunes, vea la [guía de Hooks](/es/agent-sdk/hooks).

### `HookEvent`

Eventos de hook disponibles.

```typescript theme={null}
type HookEvent =
  | "PreToolUse"
  | "PostToolUse"
  | "PostToolUseFailure"
  | "PostToolBatch"
  | "Notification"
  | "UserPromptSubmit"
  | "SessionStart"
  | "SessionEnd"
  | "Stop"
  | "SubagentStart"
  | "SubagentStop"
  | "PreCompact"
  | "PermissionRequest"
  | "Setup"
  | "TeammateIdle"
  | "TaskCompleted"
  | "ConfigChange"
  | "WorktreeCreate"
  | "WorktreeRemove";
```

### `HookCallback`

Tipo de función de devolución de llamada de hook.

```typescript theme={null}
type HookCallback = (
  input: HookInput, // Unión de todos los tipos de entrada de hook
  toolUseID: string | undefined,
  options: { signal: AbortSignal }
) => Promise<HookJSONOutput>;
```

### `HookCallbackMatcher`

Configuración de hook con coincidencia opcional.

```typescript theme={null}
interface HookCallbackMatcher {
  matcher?: string;
  hooks: HookCallback[];
  timeout?: number; // Tiempo de espera en segundos para todos los hooks en este coincididor
}
```

### `HookInput`

Tipo de unión de todos los tipos de entrada de hook.

```typescript theme={null}
type HookInput =
  | PreToolUseHookInput
  | PostToolUseHookInput
  | PostToolUseFailureHookInput
  | PostToolBatchHookInput
  | NotificationHookInput
  | UserPromptSubmitHookInput
  | SessionStartHookInput
  | SessionEndHookInput
  | StopHookInput
  | SubagentStartHookInput
  | SubagentStopHookInput
  | PreCompactHookInput
  | PermissionRequestHookInput
  | SetupHookInput
  | TeammateIdleHookInput
  | TaskCompletedHookInput
  | ConfigChangeHookInput
  | WorktreeCreateHookInput
  | WorktreeRemoveHookInput;
```

### `BaseHookInput`

Interfaz base que todos los tipos de entrada de hook extienden.

```typescript theme={null}
type BaseHookInput = {
  session_id: string;
  transcript_path: string;
  cwd: string;
  permission_mode?: string;
  effort?: { level: string };
  agent_id?: string;
  agent_type?: string;
};
```

#### `PreToolUseHookInput`

```typescript theme={null}
type PreToolUseHookInput = BaseHookInput & {
  hook_event_name: "PreToolUse";
  tool_name: string;
  tool_input: unknown;
  tool_use_id: string;
};
```

#### `PostToolUseHookInput`

```typescript theme={null}
type PostToolUseHookInput = BaseHookInput & {
  hook_event_name: "PostToolUse";
  tool_name: string;
  tool_input: unknown;
  tool_response: unknown;
  tool_use_id: string;
  duration_ms?: number;
};
```

#### `PostToolUseFailureHookInput`

```typescript theme={null}
type PostToolUseFailureHookInput = BaseHookInput & {
  hook_event_name: "PostToolUseFailure";
  tool_name: string;
  tool_input: unknown;
  tool_use_id: string;
  error: string;
  is_interrupt?: boolean;
  duration_ms?: number;
};
```

#### `PostToolBatchHookInput`

Se activa una vez después de que cada llamada de herramienta en un lote se haya resuelto, antes de la siguiente solicitud del modelo. `tool_response` lleva el contenido serializado de `tool_result` que el modelo ve; la forma difiere del objeto `Output` estructurado de `PostToolUseHookInput`.

```typescript theme={null}
type PostToolBatchHookInput = BaseHookInput & {
  hook_event_name: "PostToolBatch";
  tool_calls: PostToolBatchToolCall[];
};

type PostToolBatchToolCall = {
  tool_name: string;
  tool_input: unknown;
  tool_use_id: string;
  tool_response?: unknown;
};
```

#### `NotificationHookInput`

```typescript theme={null}
type NotificationHookInput = BaseHookInput & {
  hook_event_name: "Notification";
  message: string;
  title?: string;
  notification_type: string;
};
```

#### `UserPromptSubmitHookInput`

```typescript theme={null}
type UserPromptSubmitHookInput = BaseHookInput & {
  hook_event_name: "UserPromptSubmit";
  prompt: string;
};
```

#### `SessionStartHookInput`

```typescript theme={null}
type SessionStartHookInput = BaseHookInput & {
  hook_event_name: "SessionStart";
  source: "startup" | "resume" | "clear" | "compact";
  agent_type?: string;
  model?: string;
};
```

#### `SessionEndHookInput`

```typescript theme={null}
type SessionEndHookInput = BaseHookInput & {
  hook_event_name: "SessionEnd";
  reason: ExitReason; // Cadena de matriz EXIT_REASONS
};
```

#### `StopHookInput`

```typescript theme={null}
type StopHookInput = BaseHookInput & {
  hook_event_name: "Stop";
  stop_hook_active: boolean;
  last_assistant_message?: string;
};
```

#### `SubagentStartHookInput`

```typescript theme={null}
type SubagentStartHookInput = BaseHookInput & {
  hook_event_name: "SubagentStart";
  agent_id: string;
  agent_type: string;
};
```

#### `SubagentStopHookInput`

```typescript theme={null}
type SubagentStopHookInput = BaseHookInput & {
  hook_event_name: "SubagentStop";
  stop_hook_active: boolean;
  agent_id: string;
  agent_transcript_path: string;
  agent_type: string;
  last_assistant_message?: string;
};
```

#### `PreCompactHookInput`

```typescript theme={null}
type PreCompactHookInput = BaseHookInput & {
  hook_event_name: "PreCompact";
  trigger: "manual" | "auto";
  custom_instructions: string | null;
};
```

#### `PermissionRequestHookInput`

```typescript theme={null}
type PermissionRequestHookInput = BaseHookInput & {
  hook_event_name: "PermissionRequest";
  tool_name: string;
  tool_input: unknown;
  permission_suggestions?: PermissionUpdate[];
};
```

#### `SetupHookInput`

```typescript theme={null}
type SetupHookInput = BaseHookInput & {
  hook_event_name: "Setup";
  trigger: "init" | "maintenance";
};
```

#### `TeammateIdleHookInput`

```typescript theme={null}
type TeammateIdleHookInput = BaseHookInput & {
  hook_event_name: "TeammateIdle";
  teammate_name: string;
  team_name: string;
};
```

#### `TaskCompletedHookInput`

```typescript theme={null}
type TaskCompletedHookInput = BaseHookInput & {
  hook_event_name: "TaskCompleted";
  task_id: string;
  task_subject: string;
  task_description?: string;
  teammate_name?: string;
  team_name?: string;
};
```

#### `ConfigChangeHookInput`

```typescript theme={null}
type ConfigChangeHookInput = BaseHookInput & {
  hook_event_name: "ConfigChange";
  source:
    | "user_settings"
    | "project_settings"
    | "local_settings"
    | "policy_settings"
    | "skills";
  file_path?: string;
};
```

#### `WorktreeCreateHookInput`

```typescript theme={null}
type WorktreeCreateHookInput = BaseHookInput & {
  hook_event_name: "WorktreeCreate";
  name: string;
};
```

#### `WorktreeRemoveHookInput`

```typescript theme={null}
type WorktreeRemoveHookInput = BaseHookInput & {
  hook_event_name: "WorktreeRemove";
  worktree_path: string;
};
```

### `HookJSONOutput`

Valor de retorno de hook.

```typescript theme={null}
type HookJSONOutput = AsyncHookJSONOutput | SyncHookJSONOutput;
```

#### `AsyncHookJSONOutput`

```typescript theme={null}
type AsyncHookJSONOutput = {
  async: true;
  asyncTimeout?: number;
};
```

#### `SyncHookJSONOutput`

```typescript theme={null}
type SyncHookJSONOutput = {
  continue?: boolean;
  suppressOutput?: boolean;
  stopReason?: string;
  decision?: "approve" | "block";
  systemMessage?: string;
  reason?: string;
  hookSpecificOutput?:
    | {
        hookEventName: "PreToolUse";
        permissionDecision?: "allow" | "deny" | "ask" | "defer";
        permissionDecisionReason?: string;
        updatedInput?: Record<string, unknown>;
        additionalContext?: string;
      }
    | {
        hookEventName: "UserPromptSubmit";
        additionalContext?: string;
      }
    | {
        hookEventName: "SessionStart";
        additionalContext?: string;
      }
    | {
        hookEventName: "Setup";
        additionalContext?: string;
      }
    | {
        hookEventName: "SubagentStart";
        additionalContext?: string;
      }
    | {
        hookEventName: "PostToolUse";
        additionalContext?: string;
        updatedToolOutput?: unknown;
        /** @deprecated Use `updatedToolOutput`, which works for all tools. */
        updatedMCPToolOutput?: unknown;
      }
    | {
        hookEventName: "PostToolUseFailure";
        additionalContext?: string;
      }
    | {
        hookEventName: "PostToolBatch";
        additionalContext?: string;
      }
    | {
        hookEventName: "Notification";
        additionalContext?: string;
      }
    | {
        hookEventName: "PermissionRequest";
        decision:
          | {
              behavior: "allow";
              updatedInput?: Record<string, unknown>;
              updatedPermissions?: PermissionUpdate[];
            }
          | {
              behavior: "deny";
              message?: string;
              interrupt?: boolean;
            };
      };
};
```

## Tipos de Entrada de Herramienta

Documentación de esquemas de entrada para todas las herramientas integradas de Claude Code. Estos tipos se exportan desde `@anthropic-ai/claude-agent-sdk` y se pueden usar para interacciones de herramientas seguras de tipos.

### `ToolInputSchemas`

Unión de todos los tipos de entrada de herramienta, exportados desde `@anthropic-ai/claude-agent-sdk`.

```typescript theme={null}
type ToolInputSchemas =
  | AgentInput
  | AskUserQuestionInput
  | BashInput
  | TaskOutputInput
  | EnterWorktreeInput
  | ExitPlanModeInput
  | FileEditInput
  | FileReadInput
  | FileWriteInput
  | GlobInput
  | GrepInput
  | ListMcpResourcesInput
  | McpInput
  | MonitorInput
  | NotebookEditInput
  | ReadMcpResourceInput
  | SubscribeMcpResourceInput
  | SubscribePollingInput
  | TaskCreateInput
  | TaskGetInput
  | TaskListInput
  | TaskStopInput
  | TaskUpdateInput
  | TodoWriteInput
  | UnsubscribeMcpResourceInput
  | UnsubscribePollingInput
  | WebFetchInput
  | WebSearchInput;
```

### Agent

**Nombre de herramienta:** `Agent` (anteriormente `Task`, que aún se acepta como alias)

```typescript theme={null}
type AgentInput = {
  description: string;
  prompt: string;
  subagent_type: string;
  model?: "sonnet" | "opus" | "haiku";
  resume?: string;
  run_in_background?: boolean;
  max_turns?: number;
  name?: string;
  team_name?: string;
  mode?: "acceptEdits" | "bypassPermissions" | "default" | "dontAsk" | "plan";
  isolation?: "worktree";
};
```

Lanza un nuevo agente para manejar tareas complejas de múltiples pasos de forma autónoma.

### AskUserQuestion

**Nombre de herramienta:** `AskUserQuestion`

```typescript theme={null}
type AskUserQuestionInput = {
  questions: Array<{
    question: string;
    header: string;
    options: Array<{ label: string; description: string; preview?: string }>;
    multiSelect: boolean;
  }>;
};
```

Hace preguntas aclaratorias al usuario durante la ejecución. Vea [Manejar aprobaciones e entrada del usuario](/es/agent-sdk/user-input#handle-clarifying-questions) para detalles de uso.

### Bash

**Nombre de herramienta:** `Bash`

```typescript theme={null}
type BashInput = {
  command: string;
  timeout?: number;
  description?: string;
  run_in_background?: boolean;
  dangerouslyDisableSandbox?: boolean;
};
```

Ejecuta comandos bash en una sesión de shell persistente con tiempo de espera opcional y ejecución en segundo plano.

### Monitor

**Nombre de herramienta:** `Monitor`

```typescript theme={null}
type MonitorInput = {
  command: string;
  description: string;
  timeout_ms?: number;
  persistent?: boolean;
};
```

Ejecuta un script de fondo y entrega cada línea de stdout a Claude como un evento para que pueda reaccionar sin sondeo. Establezca `persistent: true` para vigilancias de duración de sesión como colas de registro. Monitor sigue las mismas reglas de permiso que Bash. Vea la [referencia de herramienta Monitor](/es/tools-reference#monitor-tool) para comportamiento y disponibilidad de proveedor.

### TaskOutput

**Nombre de herramienta:** `TaskOutput`

```typescript theme={null}
type TaskOutputInput = {
  task_id: string;
  block: boolean;
  timeout: number;
};
```

Recupera salida de una tarea de fondo en ejecución o completada.

### Edit

**Nombre de herramienta:** `Edit`

```typescript theme={null}
type FileEditInput = {
  file_path: string;
  old_string: string;
  new_string: string;
  replace_all?: boolean;
};
```

Realiza reemplazos de cadena exactos en archivos.

### Read

**Nombre de herramienta:** `Read`

```typescript theme={null}
type FileReadInput = {
  file_path: string;
  offset?: number;
  limit?: number;
  pages?: string;
};
```

Lee archivos del sistema de archivos local, incluyendo texto, imágenes, PDFs y cuadernos Jupyter. Use `pages` para rangos de páginas PDF (por ejemplo, `"1-5"`).

### Write

**Nombre de herramienta:** `Write`

```typescript theme={null}
type FileWriteInput = {
  file_path: string;
  content: string;
};
```

Escribe un archivo en el sistema de archivos local, sobrescribiendo si existe.

### Glob

**Nombre de herramienta:** `Glob`

```typescript theme={null}
type GlobInput = {
  pattern: string;
  path?: string;
};
```

Coincidencia de patrón de archivo rápida que funciona con cualquier tamaño de base de código.

### Grep

**Nombre de herramienta:** `Grep`

```typescript theme={null}
type GrepInput = {
  pattern: string;
  path?: string;
  glob?: string;
  type?: string;
  output_mode?: "content" | "files_with_matches" | "count";
  "-i"?: boolean;
  "-n"?: boolean;
  "-B"?: number;
  "-A"?: number;
  "-C"?: number;
  context?: number;
  head_limit?: number;
  offset?: number;
  multiline?: boolean;
};
```

Herramienta de búsqueda poderosa construida en ripgrep con soporte de expresiones regulares.

### TaskStop

**Nombre de herramienta:** `TaskStop`

```typescript theme={null}
type TaskStopInput = {
  task_id?: string;
  shell_id?: string; // Deprecado: use task_id
};
```

Detiene una tarea de fondo en ejecución o shell por ID.

### NotebookEdit

**Nombre de herramienta:** `NotebookEdit`

```typescript theme={null}
type NotebookEditInput = {
  notebook_path: string;
  cell_id?: string;
  new_source: string;
  cell_type?: "code" | "markdown";
  edit_mode?: "replace" | "insert" | "delete";
};
```

Edita celdas en archivos de cuaderno Jupyter.

### WebFetch

**Nombre de herramienta:** `WebFetch`

```typescript theme={null}
type WebFetchInput = {
  url: string;
  prompt: string;
};
```

Obtiene contenido de una URL y lo procesa con un modelo de IA.

### WebSearch

**Nombre de herramienta:** `WebSearch`

```typescript theme={null}
type WebSearchInput = {
  query: string;
  allowed_domains?: string[];
  blocked_domains?: string[];
};
```

Busca en la web y devuelve resultados formateados.

### TodoWrite

**Nombre de herramienta:** `TodoWrite`

```typescript theme={null}
type TodoWriteInput = {
  todos: Array<{
    content: string;
    status: "pending" | "in_progress" | "completed";
    activeForm: string;
  }>;
};
```

Crea y gestiona una lista de tareas estructurada para rastrear el progreso.

<Note>
  `TodoWrite` está deprecado y se eliminará en una versión futura. Use `TaskCreate`, `TaskGet`, `TaskUpdate` y `TaskList` en su lugar. Establezca `CLAUDE_CODE_ENABLE_TASKS=1` para optar por participar. Vea [Migrar a herramientas Task](/es/agent-sdk/todo-tracking#migrate-to-task-tools) para cómo monitorear cambios de código.
</Note>

### TaskCreate

**Nombre de herramienta:** `TaskCreate`

```typescript theme={null}
type TaskCreateInput = {
  subject: string;
  description: string;
  activeForm?: string;
  metadata?: Record<string, unknown>;
};
```

Crea una única tarea y devuelve su ID asignado.

### TaskUpdate

**Nombre de herramienta:** `TaskUpdate`

```typescript theme={null}
type TaskUpdateInput = {
  taskId: string;
  status?: "pending" | "in_progress" | "completed" | "deleted";
  subject?: string;
  description?: string;
  activeForm?: string;
  addBlocks?: string[];
  addBlockedBy?: string[];
  owner?: string;
  metadata?: Record<string, unknown>;
};
```

Parcha una tarea por ID. Establezca `status` a `"deleted"` para eliminarla.

### TaskGet

**Nombre de herramienta:** `TaskGet`

```typescript theme={null}
type TaskGetInput = {
  taskId: string;
};
```

Devuelve detalles completos para una tarea, o `null` cuando el ID no se encuentra.

### TaskList

**Nombre de herramienta:** `TaskList`

```typescript theme={null}
type TaskListInput = {};
```

Devuelve una instantánea de todas las tareas en la lista actual.

### ExitPlanMode

**Nombre de herramienta:** `ExitPlanMode`

```typescript theme={null}
type ExitPlanModeInput = {
  allowedPrompts?: Array<{
    tool: "Bash";
    prompt: string;
  }>;
};
```

Sale del modo de planificación. Opcionalmente especifica permisos basados en mensajes necesarios para implementar el plan.

### ListMcpResources

**Nombre de herramienta:** `ListMcpResources`

```typescript theme={null}
type ListMcpResourcesInput = {
  server?: string;
};
```

Enumera recursos MCP disponibles de servidores conectados.

### ReadMcpResource

**Nombre de herramienta:** `ReadMcpResource`

```typescript theme={null}
type ReadMcpResourceInput = {
  server: string;
  uri: string;
};
```

Lee un recurso MCP específico de un servidor.

### EnterWorktree

**Nombre de herramienta:** `EnterWorktree`

```typescript theme={null}
type EnterWorktreeInput = {
  name?: string;
  path?: string;
};
```

Crea e ingresa a un worktree git temporal para trabajo aislado. Pase `path` para cambiar a un worktree existente del repositorio actual en lugar de crear uno nuevo. `name` y `path` son mutuamente excluyentes.

## Tipos de Salida de Herramienta

Documentación de esquemas de salida para todas las herramientas integradas de Claude Code. Estos tipos se exportan desde `@anthropic-ai/claude-agent-sdk` y representan los datos de respuesta reales devueltos por cada herramienta.

### `ToolOutputSchemas`

Unión de todos los tipos de salida de herramienta.

```typescript theme={null}
type ToolOutputSchemas =
  | AgentOutput
  | AskUserQuestionOutput
  | BashOutput
  | EnterWorktreeOutput
  | ExitPlanModeOutput
  | FileEditOutput
  | FileReadOutput
  | FileWriteOutput
  | GlobOutput
  | GrepOutput
  | ListMcpResourcesOutput
  | MonitorOutput
  | NotebookEditOutput
  | ReadMcpResourceOutput
  | TaskCreateOutput
  | TaskGetOutput
  | TaskListOutput
  | TaskStopOutput
  | TaskUpdateOutput
  | TodoWriteOutput
  | WebFetchOutput
  | WebSearchOutput;
```

### Agent

**Nombre de herramienta:** `Agent` (anteriormente `Task`, que aún se acepta como alias)

```typescript theme={null}
type AgentOutput =
  | {
      status: "completed";
      agentId: string;
      content: Array<{ type: "text"; text: string }>;
      totalToolUseCount: number;
      totalDurationMs: number;
      totalTokens: number;
      usage: {
        input_tokens: number;
        output_tokens: number;
        cache_creation_input_tokens: number | null;
        cache_read_input_tokens: number | null;
        server_tool_use: {
          web_search_requests: number;
          web_fetch_requests: number;
        } | null;
        service_tier: ("standard" | "priority" | "batch") | null;
        cache_creation: {
          ephemeral_1h_input_tokens: number;
          ephemeral_5m_input_tokens: number;
        } | null;
      };
      prompt: string;
    }
  | {
      status: "async_launched";
      agentId: string;
      description: string;
      prompt: string;
      outputFile: string;
      canReadOutputFile?: boolean;
    }
  | {
      status: "sub_agent_entered";
      description: string;
      message: string;
    };
```

Devuelve el resultado del subagente. Discriminado en el campo `status`: `"completed"` para tareas terminadas, `"async_launched"` para tareas de fondo, y `"sub_agent_entered"` para subagentes interactivos.

### AskUserQuestion

**Nombre de herramienta:** `AskUserQuestion`

```typescript theme={null}
type AskUserQuestionOutput = {
  questions: Array<{
    question: string;
    header: string;
    options: Array<{ label: string; description: string; preview?: string }>;
    multiSelect: boolean;
  }>;
  answers: Record<string, string>;
};
```

Devuelve las preguntas hechas y las respuestas del usuario.

### Bash

**Nombre de herramienta:** `Bash`

```typescript theme={null}
type BashOutput = {
  stdout: string;
  stderr: string;
  rawOutputPath?: string;
  interrupted: boolean;
  isImage?: boolean;
  backgroundTaskId?: string;
  backgroundedByUser?: boolean;
  dangerouslyDisableSandbox?: boolean;
  returnCodeInterpretation?: string;
  structuredContent?: unknown[];
  persistedOutputPath?: string;
  persistedOutputSize?: number;
};
```

Devuelve la salida del comando con stdout/stderr divididos. Los comandos de fondo incluyen un `backgroundTaskId`.

### Monitor

**Nombre de herramienta:** `Monitor`

```typescript theme={null}
type MonitorOutput = {
  taskId: string;
  timeoutMs: number;
  persistent?: boolean;
};
```

Devuelve el ID de tarea de fondo para el monitor en ejecución. Use este ID con `TaskStop` para cancelar la vigilancia temprano.

### Edit

**Nombre de herramienta:** `Edit`

```typescript theme={null}
type FileEditOutput = {
  filePath: string;
  oldString: string;
  newString: string;
  originalFile: string;
  structuredPatch: Array<{
    oldStart: number;
    oldLines: number;
    newStart: number;
    newLines: number;
    lines: string[];
  }>;
  userModified: boolean;
  replaceAll: boolean;
  gitDiff?: {
    filename: string;
    status: "modified" | "added";
    additions: number;
    deletions: number;
    changes: number;
    patch: string;
  };
};
```

Devuelve el diff estructurado de la operación de edición.

### Read

**Nombre de herramienta:** `Read`

```typescript theme={null}
type FileReadOutput =
  | {
      type: "text";
      file: {
        filePath: string;
        content: string;
        numLines: number;
        startLine: number;
        totalLines: number;
      };
    }
  | {
      type: "image";
      file: {
        base64: string;
        type: "image/jpeg" | "image/png" | "image/gif" | "image/webp";
        originalSize: number;
        dimensions?: {
          originalWidth?: number;
          originalHeight?: number;
          displayWidth?: number;
          displayHeight?: number;
        };
      };
    }
  | {
      type: "notebook";
      file: {
        filePath: string;
        cells: unknown[];
      };
    }
  | {
      type: "pdf";
      file: {
        filePath: string;
        base64: string;
        originalSize: number;
      };
    }
  | {
      type: "parts";
      file: {
        filePath: string;
        originalSize: number;
        count: number;
        outputDir: string;
      };
    };
```

Devuelve el contenido del archivo en un formato apropiado para el tipo de archivo. Discriminado en el campo `type`.

### Write

**Nombre de herramienta:** `Write`

```typescript theme={null}
type FileWriteOutput = {
  type: "create" | "update";
  filePath: string;
  content: string;
  structuredPatch: Array<{
    oldStart: number;
    oldLines: number;
    newStart: number;
    newLines: number;
    lines: string[];
  }>;
  originalFile: string | null;
  gitDiff?: {
    filename: string;
    status: "modified" | "added";
    additions: number;
    deletions: number;
    changes: number;
    patch: string;
  };
};
```

Devuelve el resultado de escritura con información de diff estructurado.

### Glob

**Nombre de herramienta:** `Glob`

```typescript theme={null}
type GlobOutput = {
  durationMs: number;
  numFiles: number;
  filenames: string[];
  truncated: boolean;
};
```

Devuelve rutas de archivo que coinciden con el patrón glob, ordenadas por hora de modificación.

### Grep

**Nombre de herramienta:** `Grep`

```typescript theme={null}
type GrepOutput = {
  mode?: "content" | "files_with_matches" | "count";
  numFiles: number;
  filenames: string[];
  content?: string;
  numLines?: number;
  numMatches?: number;
  appliedLimit?: number;
  appliedOffset?: number;
};
```

Devuelve resultados de búsqueda. La forma varía por `mode`: lista de archivos, contenido con coincidencias o conteos de coincidencias.

### TaskStop

**Nombre de herramienta:** `TaskStop`

```typescript theme={null}
type TaskStopOutput = {
  message: string;
  task_id: string;
  task_type: string;
  command?: string;
};
```

Devuelve confirmación después de detener la tarea de fondo.

### NotebookEdit

**Nombre de herramienta:** `NotebookEdit`

```typescript theme={null}
type NotebookEditOutput = {
  new_source: string;
  cell_id?: string;
  cell_type: "code" | "markdown";
  language: string;
  edit_mode: string;
  error?: string;
  notebook_path: string;
  original_file: string;
  updated_file: string;
};
```

Devuelve el resultado de la edición del cuaderno con contenido de archivo original y actualizado.

### WebFetch

**Nombre de herramienta:** `WebFetch`

```typescript theme={null}
type WebFetchOutput = {
  bytes: number;
  code: number;
  codeText: string;
  result: string;
  durationMs: number;
  url: string;
};
```

Devuelve el contenido obtenido con estado HTTP y metadatos.

### WebSearch

**Nombre de herramienta:** `WebSearch`

```typescript theme={null}
type WebSearchOutput = {
  query: string;
  results: Array<
    | {
        tool_use_id: string;
        content: Array<{ title: string; url: string }>;
      }
    | string
  >;
  durationSeconds: number;
};
```

Devuelve resultados de búsqueda de la web.

### TodoWrite

**Nombre de herramienta:** `TodoWrite`

```typescript theme={null}
type TodoWriteOutput = {
  oldTodos: Array<{
    content: string;
    status: "pending" | "in_progress" | "completed";
    activeForm: string;
  }>;
  newTodos: Array<{
    content: string;
    status: "pending" | "in_progress" | "completed";
    activeForm: string;
  }>;
};
```

Devuelve las listas de tareas anteriores y actualizadas.

<Note>
  `TodoWrite` está deprecado y se eliminará en una versión futura. Use `TaskCreate`, `TaskGet`, `TaskUpdate`, y `TaskList` en su lugar. Establezca `CLAUDE_CODE_ENABLE_TASKS=1` para optar por participar. Consulte [Migrar a herramientas de tareas](/es/agent-sdk/todo-tracking#migrate-to-task-tools) para ver cómo monitorear cambios de código.
</Note>

### TaskCreate

**Nombre de herramienta:** `TaskCreate`

```typescript theme={null}
type TaskCreateOutput = {
  task: {
    id: string;
    subject: string;
  };
};
```

Devuelve la tarea creada con su ID asignado.

### TaskUpdate

**Nombre de herramienta:** `TaskUpdate`

```typescript theme={null}
type TaskUpdateOutput = {
  success: boolean;
  taskId: string;
  updatedFields: string[];
  error?: string;
  statusChange?: {
    from: string;
    to: string;
  };
};
```

Devuelve el resultado de la actualización, incluyendo qué campos cambiaron.

### TaskGet

**Nombre de herramienta:** `TaskGet`

```typescript theme={null}
type TaskGetOutput = {
  task: {
    id: string;
    subject: string;
    description: string;
    status: "pending" | "in_progress" | "completed";
    blocks: string[];
    blockedBy: string[];
  } | null;
};
```

Devuelve el registro de tarea completo, o `null` cuando el ID no se encuentra.

### TaskList

**Nombre de herramienta:** `TaskList`

```typescript theme={null}
type TaskListOutput = {
  tasks: Array<{
    id: string;
    subject: string;
    status: "pending" | "in_progress" | "completed";
    owner?: string;
    blockedBy: string[];
  }>;
};
```

Devuelve una instantánea de todas las tareas en la lista actual.

### ExitPlanMode

**Nombre de herramienta:** `ExitPlanMode`

```typescript theme={null}
type ExitPlanModeOutput = {
  plan: string | null;
  isAgent: boolean;
  filePath?: string;
  hasTaskTool?: boolean;
  awaitingLeaderApproval?: boolean;
  requestId?: string;
};
```

Devuelve el estado del plan después de salir del modo de planificación.

### ListMcpResources

**Nombre de herramienta:** `ListMcpResources`

```typescript theme={null}
type ListMcpResourcesOutput = Array<{
  uri: string;
  name: string;
  mimeType?: string;
  description?: string;
  server: string;
}>;
```

Devuelve una matriz de recursos MCP disponibles.

### ReadMcpResource

**Nombre de herramienta:** `ReadMcpResource`

```typescript theme={null}
type ReadMcpResourceOutput = {
  contents: Array<{
    uri: string;
    mimeType?: string;
    text?: string;
  }>;
};
```

Devuelve el contenido del recurso MCP solicitado.

### EnterWorktree

**Nombre de herramienta:** `EnterWorktree`

```typescript theme={null}
type EnterWorktreeOutput = {
  worktreePath: string;
  worktreeBranch?: string;
  message: string;
};
```

Devuelve información sobre el worktree git.

## Tipos de Permiso

### `PermissionUpdate`

Operaciones para actualizar permisos.

```typescript theme={null}
type PermissionUpdate =
  | {
      type: "addRules";
      rules: PermissionRuleValue[];
      behavior: PermissionBehavior;
      destination: PermissionUpdateDestination;
    }
  | {
      type: "replaceRules";
      rules: PermissionRuleValue[];
      behavior: PermissionBehavior;
      destination: PermissionUpdateDestination;
    }
  | {
      type: "removeRules";
      rules: PermissionRuleValue[];
      behavior: PermissionBehavior;
      destination: PermissionUpdateDestination;
    }
  | {
      type: "setMode";
      mode: PermissionMode;
      destination: PermissionUpdateDestination;
    }
  | {
      type: "addDirectories";
      directories: string[];
      destination: PermissionUpdateDestination;
    }
  | {
      type: "removeDirectories";
      directories: string[];
      destination: PermissionUpdateDestination;
    };
```

### `PermissionBehavior`

```typescript theme={null}
type PermissionBehavior = "allow" | "deny" | "ask";
```

### `PermissionUpdateDestination`

```typescript theme={null}
type PermissionUpdateDestination =
  | "userSettings" // Configuración global del usuario
  | "projectSettings" // Configuración del proyecto por directorio
  | "localSettings" // Configuración local gitignored
  | "session" // Solo sesión actual
  | "cliArg"; // Argumento CLI
```

### `PermissionRuleValue`

```typescript theme={null}
type PermissionRuleValue = {
  toolName: string;
  ruleContent?: string;
};
```

## Otros Tipos

### `ApiKeySource`

```typescript theme={null}
type ApiKeySource = "user" | "project" | "org" | "temporary" | "oauth";
```

### `SdkBeta`

Características beta disponibles que se pueden habilitar a través de la opción `betas`. Vea [Encabezados Beta](https://platform.claude.com/docs/es/api/beta-headers) para más información.

```typescript theme={null}
type SdkBeta = "context-1m-2025-08-07";
```

<Warning>
  La beta `context-1m-2025-08-07` se retiró a partir del 30 de abril de 2026. Pasar este valor con Claude Sonnet 4.5 o Sonnet 4 no tiene efecto, y las solicitudes que excedan la ventana de contexto estándar de 200k tokens devuelven un error. Para usar una ventana de contexto de 1M tokens, migre a [Claude Sonnet 4.6, Claude Opus 4.6, o Claude Opus 4.7](https://platform.claude.com/docs/es/about-claude/models/overview), que incluyen contexto de 1M a precios estándar sin encabezado beta requerido.
</Warning>

### `SlashCommand`

Información sobre un comando slash disponible.

```typescript theme={null}
type SlashCommand = {
  name: string;
  description: string;
  argumentHint: string;
  aliases?: string[];
};
```

### `ModelInfo`

Información sobre un modelo disponible.

```typescript theme={null}
type ModelInfo = {
  value: string;
  displayName: string;
  description: string;
  supportsEffort?: boolean;
  supportedEffortLevels?: ("low" | "medium" | "high" | "xhigh" | "max")[];
  supportsAdaptiveThinking?: boolean;
  supportsFastMode?: boolean;
};
```

### `AgentInfo`

Información sobre un subagente disponible que se puede invocar a través de la herramienta Agent.

```typescript theme={null}
type AgentInfo = {
  name: string;
  description: string;
  model?: string;
};
```

| Campo         | Tipo                  | Descripción                                                                     |
| :------------ | :-------------------- | :------------------------------------------------------------------------------ |
| `name`        | `string`              | Identificador de tipo de agente (por ejemplo, `"Explore"`, `"general-purpose"`) |
| `description` | `string`              | Descripción de cuándo usar este agente                                          |
| `model`       | `string \| undefined` | Alias de modelo que usa este agente. Si se omite, hereda el modelo del padre    |

### `McpServerStatus`

Estado de un servidor MCP conectado.

```typescript theme={null}
type McpServerStatus = {
  name: string;
  status: "connected" | "failed" | "needs-auth" | "pending" | "disabled";
  serverInfo?: {
    name: string;
    version: string;
  };
  error?: string;
  config?: McpServerStatusConfig;
  scope?: string;
  tools?: {
    name: string;
    description?: string;
    annotations?: {
      readOnly?: boolean;
      destructive?: boolean;
      openWorld?: boolean;
    };
  }[];
};
```

### `McpServerStatusConfig`

La configuración de un servidor MCP como se reporta por `mcpServerStatus()`. Esta es la unión de todos los tipos de transporte de servidor MCP.

```typescript theme={null}
type McpServerStatusConfig =
  | McpStdioServerConfig
  | McpSSEServerConfig
  | McpHttpServerConfig
  | McpSdkServerConfig
  | McpClaudeAIProxyServerConfig;
```

Vea [`McpServerConfig`](#mcpserverconfig) para detalles sobre cada tipo de transporte.

### `AccountInfo`

Información de cuenta para el usuario autenticado.

```typescript theme={null}
type AccountInfo = {
  email?: string;
  organization?: string;
  subscriptionType?: string;
  tokenSource?: string;
  apiKeySource?: string;
};
```

### `ModelUsage`

Estadísticas de uso por modelo devueltas en mensajes de resultado. El valor `costUSD` es una estimación del lado del cliente. Vea [Rastrear costo y uso](/es/agent-sdk/cost-tracking) para advertencias de facturación.

```typescript theme={null}
type ModelUsage = {
  inputTokens: number;
  outputTokens: number;
  cacheReadInputTokens: number;
  cacheCreationInputTokens: number;
  webSearchRequests: number;
  costUSD: number;
  contextWindow: number;
  maxOutputTokens: number;
};
```

### `ConfigScope`

```typescript theme={null}
type ConfigScope = "local" | "user" | "project";
```

### `NonNullableUsage`

Una versión de [`Usage`](#usage) con todos los campos anulables hechos no anulables.

```typescript theme={null}
type NonNullableUsage = {
  [K in keyof Usage]: NonNullable<Usage[K]>;
};
```

### `Usage`

Estadísticas de uso de tokens (desde `@anthropic-ai/sdk`).

```typescript theme={null}
type Usage = {
  input_tokens: number | null;
  output_tokens: number | null;
  cache_creation_input_tokens?: number | null;
  cache_read_input_tokens?: number | null;
};
```

### `CallToolResult`

Tipo de resultado de herramienta MCP (desde `@modelcontextprotocol/sdk/types.js`). `structuredContent` es un objeto JSON que se puede devolver junto con `content`, incluyendo bloques de imagen. Vea [Devolver datos estructurados](/es/agent-sdk/custom-tools#return-structured-data).

```typescript theme={null}
type CallToolResult = {
  content: Array<{
    type: "text" | "image" | "resource";
    // Los campos adicionales varían por tipo
  }>;
  structuredContent?: Record<string, unknown>;
  isError?: boolean;
};
```

### `ThinkingConfig`

Controla el comportamiento de pensamiento/razonamiento de Claude. Tiene precedencia sobre el `maxThinkingTokens` deprecado.

```typescript theme={null}
type ThinkingConfig =
  | { type: "adaptive" } // El modelo determina cuándo y cuánto razonar (Opus 4.6+)
  | { type: "enabled"; budgetTokens?: number } // Presupuesto de token de pensamiento fijo
  | { type: "disabled" }; // Sin pensamiento extendido
```

### `SpawnedProcess`

Interfaz para generación de proceso personalizado (usada con la opción `spawnClaudeCodeProcess`). `ChildProcess` ya satisface esta interfaz.

```typescript theme={null}
interface SpawnedProcess {
  stdin: Writable;
  stdout: Readable;
  readonly killed: boolean;
  readonly exitCode: number | null;
  kill(signal: NodeJS.Signals): boolean;
  on(
    event: "exit",
    listener: (code: number | null, signal: NodeJS.Signals | null) => void
  ): void;
  on(event: "error", listener: (error: Error) => void): void;
  once(
    event: "exit",
    listener: (code: number | null, signal: NodeJS.Signals | null) => void
  ): void;
  once(event: "error", listener: (error: Error) => void): void;
  off(
    event: "exit",
    listener: (code: number | null, signal: NodeJS.Signals | null) => void
  ): void;
  off(event: "error", listener: (error: Error) => void): void;
}
```

### `SpawnOptions`

Opciones pasadas a la función de generación personalizada.

```typescript theme={null}
interface SpawnOptions {
  command: string;
  args: string[];
  cwd?: string;
  env: Record<string, string | undefined>;
  signal: AbortSignal;
}
```

### `McpSetServersResult`

Resultado de una operación `setMcpServers()`.

```typescript theme={null}
type McpSetServersResult = {
  added: string[];
  removed: string[];
  errors: Record<string, string>;
};
```

### `RewindFilesResult`

Resultado de una operación `rewindFiles()`.

```typescript theme={null}
type RewindFilesResult = {
  canRewind: boolean;
  error?: string;
  filesChanged?: string[];
  insertions?: number;
  deletions?: number;
};
```

### `SDKStatusMessage`

Mensaje de actualización de estado (por ejemplo, compactación).

```typescript theme={null}
type SDKStatusMessage = {
  type: "system";
  subtype: "status";
  status: "compacting" | null;
  permissionMode?: PermissionMode;
  uuid: UUID;
  session_id: string;
};
```

### `SDKTaskNotificationMessage`

Notificación cuando una tarea de fondo se completa, falla o se detiene. Las tareas de fondo incluyen comandos Bash `run_in_background`, vigilancias [Monitor](#monitor) y subagentes de fondo.

```typescript theme={null}
type SDKTaskNotificationMessage = {
  type: "system";
  subtype: "task_notification";
  task_id: string;
  tool_use_id?: string;
  status: "completed" | "failed" | "stopped";
  output_file: string;
  summary: string;
  usage?: {
    total_tokens: number;
    tool_uses: number;
    duration_ms: number;
  };
  uuid: UUID;
  session_id: string;
};
```

### `SDKToolUseSummaryMessage`

Resumen del uso de herramientas en una conversación.

```typescript theme={null}
type SDKToolUseSummaryMessage = {
  type: "tool_use_summary";
  summary: string;
  preceding_tool_use_ids: string[];
  uuid: UUID;
  session_id: string;
};
```

### `SDKHookStartedMessage`

Se emite cuando un hook comienza a ejecutarse.

```typescript theme={null}
type SDKHookStartedMessage = {
  type: "system";
  subtype: "hook_started";
  hook_id: string;
  hook_name: string;
  hook_event: string;
  uuid: UUID;
  session_id: string;
};
```

### `SDKHookProgressMessage`

Se emite mientras un hook se está ejecutando, con salida de stdout/stderr.

```typescript theme={null}
type SDKHookProgressMessage = {
  type: "system";
  subtype: "hook_progress";
  hook_id: string;
  hook_name: string;
  hook_event: string;
  stdout: string;
  stderr: string;
  output: string;
  uuid: UUID;
  session_id: string;
};
```

### `SDKHookResponseMessage`

Se emite cuando un hook termina de ejecutarse.

```typescript theme={null}
type SDKHookResponseMessage = {
  type: "system";
  subtype: "hook_response";
  hook_id: string;
  hook_name: string;
  hook_event: string;
  output: string;
  stdout: string;
  stderr: string;
  exit_code?: number;
  outcome: "success" | "error" | "cancelled";
  uuid: UUID;
  session_id: string;
};
```

### `SDKToolProgressMessage`

Se emite periódicamente mientras se ejecuta una herramienta para indicar progreso.

```typescript theme={null}
type SDKToolProgressMessage = {
  type: "tool_progress";
  tool_use_id: string;
  tool_name: string;
  parent_tool_use_id: string | null;
  elapsed_time_seconds: number;
  task_id?: string;
  uuid: UUID;
  session_id: string;
};
```

### `SDKAuthStatusMessage`

Se emite durante flujos de autenticación.

```typescript theme={null}
type SDKAuthStatusMessage = {
  type: "auth_status";
  isAuthenticating: boolean;
  output: string[];
  error?: string;
  uuid: UUID;
  session_id: string;
};
```

### `SDKTaskStartedMessage`

Se emite cuando comienza una tarea de fondo. El campo `task_type` es `"local_bash"` para comandos Bash de fondo y vigilancias [Monitor](#monitor), `"local_agent"` para subagentes, o `"remote_agent"`.

```typescript theme={null}
type SDKTaskStartedMessage = {
  type: "system";
  subtype: "task_started";
  task_id: string;
  tool_use_id?: string;
  description: string;
  task_type?: string;
  uuid: UUID;
  session_id: string;
};
```

### `SDKTaskProgressMessage`

Se emite periódicamente mientras se ejecuta una tarea de fondo.

```typescript theme={null}
type SDKTaskProgressMessage = {
  type: "system";
  subtype: "task_progress";
  task_id: string;
  tool_use_id?: string;
  description: string;
  usage: {
    total_tokens: number;
    tool_uses: number;
    duration_ms: number;
  };
  last_tool_name?: string;
  uuid: UUID;
  session_id: string;
};
```

### `SDKTaskUpdatedMessage`

Se emite cuando el estado de una tarea de fondo cambia, como cuando transiciona de `running` a `completed`. Combine `patch` en su mapa de tareas local con clave `task_id`. El campo `end_time` es una marca de tiempo de época Unix en milisegundos, comparable con `Date.now()`.

```typescript theme={null}
type SDKTaskUpdatedMessage = {
  type: "system";
  subtype: "task_updated";
  task_id: string;
  patch: {
    status?: "pending" | "running" | "completed" | "failed" | "killed";
    description?: string;
    end_time?: number;
    total_paused_ms?: number;
    error?: string;
    is_backgrounded?: boolean;
  };
  uuid: UUID;
  session_id: string;
};
```

### `SDKFilesPersistedEvent`

Se emite cuando los puntos de control de archivo se persisten en el disco.

```typescript theme={null}
type SDKFilesPersistedEvent = {
  type: "system";
  subtype: "files_persisted";
  files: { filename: string; file_id: string }[];
  failed: { filename: string; error: string }[];
  processed_at: string;
  uuid: UUID;
  session_id: string;
};
```

### `SDKRateLimitEvent`

Se emite cuando la sesión encuentra un límite de velocidad.

```typescript theme={null}
type SDKRateLimitEvent = {
  type: "rate_limit_event";
  rate_limit_info: {
    status: "allowed" | "allowed_warning" | "rejected";
    resetsAt?: number;
    utilization?: number;
  };
  uuid: UUID;
  session_id: string;
};
```

### `SDKLocalCommandOutputMessage`

Salida de un comando slash local (por ejemplo, `/voice` o `/usage`). Se muestra como texto de estilo asistente en la transcripción.

```typescript theme={null}
type SDKLocalCommandOutputMessage = {
  type: "system";
  subtype: "local_command_output";
  content: string;
  uuid: UUID;
  session_id: string;
};
```

### `SDKPromptSuggestionMessage`

Se emite después de cada turno cuando `promptSuggestions` está habilitado. Contiene un mensaje de usuario predicho siguiente.

```typescript theme={null}
type SDKPromptSuggestionMessage = {
  type: "prompt_suggestion";
  suggestion: string;
  uuid: UUID;
  session_id: string;
};
```

### `AbortError`

Clase de error personalizado para operaciones de aborto.

```typescript theme={null}
class AbortError extends Error {}
```

## Configuración de Sandbox

### `SandboxSettings`

Configuración para el comportamiento de sandbox. Use esto para habilitar el sandboxing de comandos y configurar restricciones de red mediante programación.

```typescript theme={null}
type SandboxSettings = {
  enabled?: boolean;
  autoAllowBashIfSandboxed?: boolean;
  excludedCommands?: string[];
  allowUnsandboxedCommands?: boolean;
  network?: SandboxNetworkConfig;
  filesystem?: SandboxFilesystemConfig;
  ignoreViolations?: Record<string, string[]>;
  enableWeakerNestedSandbox?: boolean;
  ripgrep?: { command: string; args?: string[] };
};
```

| Propiedad                   | Tipo                                                  | Predeterminado | Descripción                                                                                                                                                                                                                                                       |
| :-------------------------- | :---------------------------------------------------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                   | `boolean`                                             | `false`        | Habilite el modo sandbox para la ejecución de comandos                                                                                                                                                                                                            |
| `autoAllowBashIfSandboxed`  | `boolean`                                             | `true`         | Auto-apruebe comandos bash cuando el sandbox está habilitado                                                                                                                                                                                                      |
| `excludedCommands`          | `string[]`                                            | `[]`           | Comandos que siempre omiten restricciones de sandbox (por ejemplo, `['docker']`). Estos se ejecutan sin sandbox automáticamente sin participación del modelo                                                                                                      |
| `allowUnsandboxedCommands`  | `boolean`                                             | `true`         | Permita que el modelo solicite ejecutar comandos fuera del sandbox. Cuando es `true`, el modelo puede establecer `dangerouslyDisableSandbox` en la entrada de herramienta, que se vuelve al [sistema de permisos](#permissions-fallback-for-unsandboxed-commands) |
| `network`                   | [`SandboxNetworkConfig`](#sandboxnetworkconfig)       | `undefined`    | Configuración de sandbox específica de red                                                                                                                                                                                                                        |
| `filesystem`                | [`SandboxFilesystemConfig`](#sandboxfilesystemconfig) | `undefined`    | Configuración de sandbox específica del sistema de archivos para restricciones de lectura/escritura                                                                                                                                                               |
| `ignoreViolations`          | `Record<string, string[]>`                            | `undefined`    | Mapa de categorías de violación a patrones a ignorar (por ejemplo, `{ file: ['/tmp/*'], network: ['localhost'] }`)                                                                                                                                                |
| `enableWeakerNestedSandbox` | `boolean`                                             | `false`        | Habilite un sandbox anidado más débil para compatibilidad                                                                                                                                                                                                         |
| `ripgrep`                   | `{ command: string; args?: string[] }`                | `undefined`    | Configuración de binario ripgrep personalizado para entornos sandbox                                                                                                                                                                                              |

#### Ejemplo de uso

```typescript theme={null}
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Build and test my project",
  options: {
    sandbox: {
      enabled: true,
      autoAllowBashIfSandboxed: true,
      network: {
        allowLocalBinding: true
      }
    }
  }
})) {
  if ("result" in message) console.log(message.result);
}
```

<Warning>
  **Seguridad de socket Unix:** La opción `allowUnixSockets` puede otorgar acceso a servicios del sistema poderosos. Por ejemplo, permitir `/var/run/docker.sock` efectivamente otorga acceso completo al sistema host a través de la API de Docker, omitiendo el aislamiento de sandbox. Solo permita sockets Unix que sean estrictamente necesarios y comprenda las implicaciones de seguridad de cada uno.
</Warning>

### `SandboxNetworkConfig`

Configuración específica de red para el modo sandbox.

```typescript theme={null}
type SandboxNetworkConfig = {
  allowedDomains?: string[];
  deniedDomains?: string[];
  allowManagedDomainsOnly?: boolean;
  allowLocalBinding?: boolean;
  allowUnixSockets?: string[];
  allowAllUnixSockets?: boolean;
  httpProxyPort?: number;
  socksProxyPort?: number;
};
```

| Propiedad                 | Tipo       | Predeterminado | Descripción                                                                                                    |
| :------------------------ | :--------- | :------------- | :------------------------------------------------------------------------------------------------------------- |
| `allowedDomains`          | `string[]` | `[]`           | Nombres de dominio a los que los procesos en sandbox pueden acceder                                            |
| `deniedDomains`           | `string[]` | `[]`           | Nombres de dominio a los que los procesos en sandbox no pueden acceder. Tiene prioridad sobre `allowedDomains` |
| `allowManagedDomainsOnly` | `boolean`  | `false`        | Restrinja el acceso de red solo a los dominios en `allowedDomains`                                             |
| `allowLocalBinding`       | `boolean`  | `false`        | Permita que los procesos se vinculen a puertos locales (por ejemplo, para servidores de desarrollo)            |
| `allowUnixSockets`        | `string[]` | `[]`           | Rutas de socket Unix a las que los procesos pueden acceder (por ejemplo, socket de Docker)                     |
| `allowAllUnixSockets`     | `boolean`  | `false`        | Permita el acceso a todos los sockets Unix                                                                     |
| `httpProxyPort`           | `number`   | `undefined`    | Puerto proxy HTTP para solicitudes de red                                                                      |
| `socksProxyPort`          | `number`   | `undefined`    | Puerto proxy SOCKS para solicitudes de red                                                                     |

<Note>
  El proxy de sandbox integrado aplica `allowedDomains` basándose en el nombre de host solicitado y no termina ni inspecciona el tráfico TLS, por lo que técnicas como [domain fronting](https://en.wikipedia.org/wiki/Domain_fronting) potencialmente pueden omitirlo. Consulte [Limitaciones de seguridad de sandboxing](/es/sandboxing#security-limitations) para obtener detalles y [Implementación segura](/es/agent-sdk/secure-deployment#traffic-forwarding) para configurar un proxy que termine TLS.
</Note>

### `SandboxFilesystemConfig`

Configuración específica del sistema de archivos para el modo sandbox.

```typescript theme={null}
type SandboxFilesystemConfig = {
  allowWrite?: string[];
  denyWrite?: string[];
  denyRead?: string[];
};
```

| Propiedad    | Tipo       | Predeterminado | Descripción                                                     |
| :----------- | :--------- | :------------- | :-------------------------------------------------------------- |
| `allowWrite` | `string[]` | `[]`           | Patrones de ruta de archivo para permitir acceso de escritura a |
| `denyWrite`  | `string[]` | `[]`           | Patrones de ruta de archivo para negar acceso de escritura a    |
| `denyRead`   | `string[]` | `[]`           | Patrones de ruta de archivo para negar acceso de lectura a      |

### Fallback de Permisos para Comandos Sin Sandbox

Cuando `allowUnsandboxedCommands` está habilitado, el modelo puede solicitar ejecutar comandos fuera del sandbox estableciendo `dangerouslyDisableSandbox: true` en la entrada de herramienta. Estas solicitudes se vuelven al sistema de permisos existente, lo que significa que se invoca su controlador `canUseTool`, permitiéndole implementar lógica de autorización personalizada.

<Note>
  **`excludedCommands` vs `allowUnsandboxedCommands`:**

  * `excludedCommands`: Una lista estática de comandos que siempre omiten el sandbox automáticamente (por ejemplo, `['docker']`). El modelo no tiene control sobre esto.
  * `allowUnsandboxedCommands`: Permite que el modelo decida en tiempo de ejecución si solicitar ejecución sin sandbox estableciendo `dangerouslyDisableSandbox: true` en la entrada de herramienta.
</Note>

```typescript theme={null}
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Deploy my application",
  options: {
    sandbox: {
      enabled: true,
      allowUnsandboxedCommands: true // El modelo puede solicitar ejecución sin sandbox
    },
    permissionMode: "default",
    canUseTool: async (tool, input) => {
      // Verifique si el modelo está solicitando omitir el sandbox
      if (tool === "Bash" && input.dangerouslyDisableSandbox) {
        // El modelo está solicitando ejecutar este comando fuera del sandbox
        console.log(`Unsandboxed command requested: ${input.command}`);

        if (isCommandAuthorized(input.command)) {
          return { behavior: "allow" as const, updatedInput: input };
        }
        return {
          behavior: "deny" as const,
          message: "Command not authorized for unsandboxed execution"
        };
      }
      return { behavior: "allow" as const, updatedInput: input };
    }
  }
})) {
  if ("result" in message) console.log(message.result);
}
```

Este patrón le permite:

* **Auditar solicitudes del modelo:** Registre cuándo el modelo solicita ejecución sin sandbox
* **Implementar listas de permitidos:** Solo permita comandos específicos para ejecutarse sin sandbox
* **Agregar flujos de trabajo de aprobación:** Requiera autorización explícita para operaciones privilegiadas

<Warning>
  Los comandos que se ejecutan con `dangerouslyDisableSandbox: true` tienen acceso completo al sistema. Asegúrese de que su controlador `canUseTool` valide estas solicitudes cuidadosamente.

  Si `permissionMode` se establece en `bypassPermissions` y `allowUnsandboxedCommands` está habilitado, el modelo puede ejecutar autónomamente comandos fuera del sandbox sin solicitudes de aprobación. Esta combinación efectivamente permite que el modelo escape del aislamiento de sandbox silenciosamente.
</Warning>

## Ver también

* [Descripción general del SDK](/es/agent-sdk/overview) - Conceptos generales del SDK
* [Referencia del SDK de Python](/es/agent-sdk/python) - Documentación del SDK de Python
* [Referencia de CLI](/es/cli-reference) - Interfaz de línea de comandos
* [Flujos de trabajo comunes](/es/common-workflows) - Guías paso a paso
