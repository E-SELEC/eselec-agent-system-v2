---
source_url: https://code.claude.com/docs/es/agent-sdk/claude-code-features
fetched_url: https://code.claude.com/docs/es/agent-sdk/claude-code-features.md
category: SDK de Agente
status: 200
scraped_at: 2026-05-15T14:28:26+00:00
sha256_16: dd71ec70248aab81
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Usar características de Claude Code en el SDK

> Cargue instrucciones de proyecto, skills, hooks y otras características de Claude Code en sus agentes SDK.

El Agent SDK se basa en la misma base que Claude Code, lo que significa que sus agentes SDK tienen acceso a las mismas características basadas en el sistema de archivos: instrucciones de proyecto (`CLAUDE.md` y reglas), skills, hooks y más.

Cuando omite `settingSources`, `query()` lee la misma configuración del sistema de archivos que la CLI de Claude Code: configuración de usuario, proyecto y local, archivos `CLAUDE.md` y skills, agentes y comandos en `.claude/`. Para ejecutar sin estos, pase `settingSources: []`, lo que limita el agente a lo que configure programáticamente. La configuración de políticas administradas y la configuración global `~/.claude.json` se leen independientemente de esta opción. Consulte [Qué settingSources no controla](#what-settingsources-does-not-control).

Para una descripción conceptual de lo que hace cada característica y cuándo usarla, consulte [Extender Claude Code](/es/features-overview).

## Controlar la configuración del sistema de archivos con settingSources

La opción de fuentes de configuración ([`setting_sources`](/es/agent-sdk/python#claudeagentoptions) en Python, [`settingSources`](/es/agent-sdk/typescript#settingsource) en TypeScript) controla qué configuración basada en el sistema de archivos carga el SDK. Pase una lista explícita para optar por fuentes específicas, o pase una matriz vacía para deshabilitar la configuración de usuario, proyecto y local.

Este ejemplo carga tanto la configuración a nivel de usuario como a nivel de proyecto estableciendo `settingSources` en `["user", "project"]`:

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ResultMessage

  async for message in query(
      prompt="Help me refactor the auth module",
      options=ClaudeAgentOptions(
          # "user" loads from ~/.claude/, "project" loads from ./.claude/ in cwd.
          # Together they give the agent access to CLAUDE.md, skills, hooks, and
          # permissions from both locations.
          setting_sources=["user", "project"],
          allowed_tools=["Read", "Edit", "Bash"],
      ),
  ):
      if isinstance(message, AssistantMessage):
          for block in message.content:
              if hasattr(block, "text"):
                  print(block.text)
      if isinstance(message, ResultMessage) and message.subtype == "success":
          print(f"\nResult: {message.result}")
  ```

  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  for await (const message of query({
    prompt: "Help me refactor the auth module",
    options: {
      // "user" loads from ~/.claude/, "project" loads from ./.claude/ in cwd.
      // Together they give the agent access to CLAUDE.md, skills, hooks, and
      // permissions from both locations.
      settingSources: ["user", "project"],
      allowedTools: ["Read", "Edit", "Bash"]
    }
  })) {
    if (message.type === "assistant") {
      for (const block of message.message.content) {
        if (block.type === "text") console.log(block.text);
      }
    }
    if (message.type === "result" && message.subtype === "success") {
      console.log(`\nResult: ${message.result}`);
    }
  }
  ```
</CodeGroup>

Cada fuente carga la configuración desde una ubicación específica, donde `<cwd>` es el directorio de trabajo que pasa a través de la opción `cwd`, o el directorio actual del proceso si no está establecido. Para la definición de tipo completa, consulte [`SettingSource`](/es/agent-sdk/typescript#settingsource) (TypeScript) o [`SettingSource`](/es/agent-sdk/python#settingsource) (Python).

| Fuente      | Qué carga                                                                                                           | Ubicación                                                                                                                                                                        |
| :---------- | :------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"project"` | CLAUDE.md del proyecto, `.claude/rules/*.md`, skills del proyecto, hooks del proyecto, `settings.json` del proyecto | `<cwd>/.claude/` para `settings.json` y hooks; `<cwd>` y cada directorio padre para CLAUDE.md y rules; `<cwd>` y cada directorio padre hasta la raíz del repositorio para skills |
| `"user"`    | CLAUDE.md del usuario, `~/.claude/rules/*.md`, skills del usuario, configuración del usuario                        | `~/.claude/`                                                                                                                                                                     |
| `"local"`   | CLAUDE.local.md, `.claude/settings.local.json`                                                                      | `<cwd>/.claude/` para `settings.local.json`; `<cwd>` y cada directorio padre para CLAUDE.local.md                                                                                |

Omitir `settingSources` es equivalente a `["user", "project", "local"]`.

La opción `cwd` determina dónde busca el SDK las entradas a nivel de proyecto. CLAUDE.md y rules se cargan desde `<cwd>` y desde cada directorio padre. Skills se cargan desde `<cwd>` y desde cada directorio padre hasta la raíz del repositorio. `settings.json` del proyecto y hooks se cargan solo desde `<cwd>/.claude/` sin fallback de directorio padre.

### Qué settingSources no controla

`settingSources` cubre la configuración de usuario, proyecto y local. Algunas entradas se leen independientemente de su valor:

| Entrada                                                      | Comportamiento                                             | Para deshabilitar                                                                                         |
| :----------------------------------------------------------- | :--------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| Configuración de políticas administradas                     | Siempre se carga cuando está presente en el host           | Elimine el archivo de configuración administrada                                                          |
| Configuración global `~/.claude.json`                        | Siempre se lee                                             | Reubique con `CLAUDE_CONFIG_DIR` en `env`                                                                 |
| Memoria automática en `~/.claude/projects/<project>/memory/` | Se carga de forma predeterminada en el mensaje del sistema | Establezca `autoMemoryEnabled: false` en la configuración, o `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` en `env` |

<Warning>
  No confíe en las opciones predeterminadas de `query()` para el aislamiento multiinquilino. Debido a que las entradas anteriores se leen independientemente de `settingSources`, un proceso SDK puede recopilar configuración a nivel de host y memoria por directorio. Para implementaciones multiinquilino, ejecute cada inquilino en su propio sistema de archivos y establezca `settingSources: []` más `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` en `env`. Consulte [Implementación segura](/es/agent-sdk/secure-deployment).
</Warning>

## Instrucciones de proyecto (CLAUDE.md y reglas)

Los archivos `CLAUDE.md` y los archivos `.claude/rules/*.md` proporcionan a su agente contexto persistente sobre su proyecto: convenciones de codificación, comandos de compilación, decisiones de arquitectura e instrucciones. Cuando `settingSources` incluye `"project"` (como en el ejemplo anterior), el SDK carga estos archivos en el contexto al inicio de la sesión. El agente luego sigue sus convenciones de proyecto sin que tenga que repetirlas en cada mensaje.

### Ubicaciones de carga de CLAUDE.md

| Nivel                        | Ubicación                                                                  | Cuándo se carga                                                                                             |
| :--------------------------- | :------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- |
| Proyecto (raíz)              | `<cwd>/CLAUDE.md` o `<cwd>/.claude/CLAUDE.md`                              | `settingSources` incluye `"project"`                                                                        |
| Reglas del proyecto          | `<cwd>/.claude/rules/*.md` y `.claude/rules/*.md` en cada directorio padre | `settingSources` incluye `"project"`                                                                        |
| Proyecto (directorios padre) | Archivos `CLAUDE.md` en directorios por encima de `cwd`                    | `settingSources` incluye `"project"`, se carga al inicio de la sesión                                       |
| Proyecto (directorios hijo)  | Archivos `CLAUDE.md` en subdirectorios de `cwd`                            | `settingSources` incluye `"project"`, se carga bajo demanda cuando el agente lee un archivo en ese subárbol |
| Local                        | `<cwd>/CLAUDE.local.md` y `CLAUDE.local.md` en cada directorio padre       | `settingSources` incluye `"local"`                                                                          |
| Usuario                      | `~/.claude/CLAUDE.md`                                                      | `settingSources` incluye `"user"`                                                                           |
| Reglas del usuario           | `~/.claude/rules/*.md`                                                     | `settingSources` incluye `"user"`                                                                           |

Todos los niveles son aditivos: si existen archivos `CLAUDE.md` tanto de proyecto como de usuario, el agente ve ambos. No hay una regla de precedencia dura entre niveles; si las instrucciones entran en conflicto, el resultado depende de cómo Claude las interprete. Escriba reglas que no entren en conflicto, o indique la precedencia explícitamente en el archivo más específico ("Estas instrucciones de proyecto anulan cualquier valor predeterminado conflictivo a nivel de usuario").

<Tip>
  También puede inyectar contexto directamente a través de `systemPrompt` sin usar archivos `CLAUDE.md`. Consulte [Modificar mensajes del sistema](/es/agent-sdk/modifying-system-prompts). Use `CLAUDE.md` cuando desee que el mismo contexto se comparta entre sesiones interactivas de Claude Code y sus agentes SDK.
</Tip>

Para saber cómo estructurar y organizar el contenido de `CLAUDE.md`, consulte [Administrar la memoria de Claude](/es/memory).

## Skills

Los skills son archivos markdown que proporcionan a su agente conocimiento especializado y flujos de trabajo invocables. A diferencia de `CLAUDE.md` (que se carga cada sesión), los skills se cargan bajo demanda. El agente recibe descripciones de skills al inicio y carga el contenido completo cuando es relevante.

Los skills se descubren desde el sistema de archivos a través de `settingSources`. Cuando la opción `skills` en `query()` se omite, los skills de usuario y proyecto descubiertos se habilitan y la herramienta Skill está disponible, coincidiendo con el comportamiento de CLI. Para controlar qué skills están habilitados, pase `skills` como `"all"`, una lista de nombres de skills, o `[]` para deshabilitar todos. El SDK habilita la herramienta Skill automáticamente cuando `skills` está configurado, por lo que no necesita agregarla a `allowedTools`.

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage

  # Skills in .claude/skills/ are discovered automatically
  # when settingSources includes "project"
  async for message in query(
      prompt="Review this PR using our code review checklist",
      options=ClaudeAgentOptions(
          setting_sources=["user", "project"],
          skills="all",
          allowed_tools=["Read", "Grep", "Glob"],
      ),
  ):
      if isinstance(message, ResultMessage) and message.subtype == "success":
          print(message.result)
  ```

  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  // Skills in .claude/skills/ are discovered automatically
  // when settingSources includes "project"
  for await (const message of query({
    prompt: "Review this PR using our code review checklist",
    options: {
      settingSources: ["user", "project"],
      skills: "all",
      allowedTools: ["Read", "Grep", "Glob"]
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```
</CodeGroup>

<Note>
  Los skills deben crearse como artefactos del sistema de archivos (`.claude/skills/<name>/SKILL.md`). El SDK no tiene una API programática para registrar skills. Consulte [Agent Skills en el SDK](/es/agent-sdk/skills) para obtener detalles completos.
</Note>

Para obtener más información sobre cómo crear y usar skills, consulte [Agent Skills en el SDK](/es/agent-sdk/skills).

## Hooks

El SDK admite dos formas de definir hooks, y se ejecutan lado a lado:

* **Hooks del sistema de archivos:** comandos de shell definidos en `settings.json`, cargados cuando `settingSources` incluye la fuente relevante. Estos son los mismos hooks que configuraría para [sesiones interactivas de Claude Code](/es/hooks-guide).
* **Hooks programáticos:** funciones de devolución de llamada pasadas directamente a `query()`. Se ejecutan en el proceso de su aplicación y pueden devolver decisiones estructuradas. Consulte [Controlar la ejecución con hooks](/es/agent-sdk/hooks).

Ambos tipos se ejecutan durante el mismo ciclo de vida del hook. Si ya tiene hooks en el `.claude/settings.json` de su proyecto y establece `settingSources: ["project"]`, esos hooks se ejecutan automáticamente en el SDK sin configuración adicional.

Las devoluciones de llamada de hooks reciben la entrada de la herramienta y devuelven un diccionario de decisión. Devolver `{}` (un diccionario vacío) significa permitir que la herramienta continúe. Devolver `{"decision": "block", "reason": "..."}` previene la ejecución y la razón se envía a Claude como el resultado de la herramienta. Consulte la [guía de hooks](/es/agent-sdk/hooks) para la firma de devolución de llamada completa y los tipos de retorno.

<CodeGroup>
  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, HookMatcher, ResultMessage


  # PreToolUse hook callback. Positional args:
  #   input_data: HookInput dict with tool_name, tool_input, hook_event_name
  #   tool_use_id: str | None, the ID of the tool call being intercepted
  #   context: HookContext, carries session metadata
  async def audit_bash(input_data, tool_use_id, context):
      command = input_data.get("tool_input", {}).get("command", "")
      if "rm -rf" in command:
          return {"decision": "block", "reason": "Destructive command blocked"}
      return {}  # Empty dict: allow the tool to proceed


  # Filesystem hooks from .claude/settings.json run automatically
  # when settingSources loads them. You can also add programmatic hooks:
  async for message in query(
      prompt="Refactor the auth module",
      options=ClaudeAgentOptions(
          setting_sources=["project"],  # Loads hooks from .claude/settings.json
          hooks={
              "PreToolUse": [
                  HookMatcher(matcher="Bash", hooks=[audit_bash]),
              ]
          },
      ),
  ):
      if isinstance(message, ResultMessage) and message.subtype == "success":
          print(message.result)
  ```

  ```typescript TypeScript theme={null}
  import { query, type HookInput, type HookJSONOutput } from "@anthropic-ai/claude-agent-sdk";

  // PreToolUse hook callback. HookInput is a discriminated union on
  // hook_event_name, so narrowing on it gives TypeScript the right
  // tool_input shape for this event.
  const auditBash = async (input: HookInput): Promise<HookJSONOutput> => {
    if (input.hook_event_name !== "PreToolUse") return {};
    const toolInput = input.tool_input as { command?: string };
    if (toolInput.command?.includes("rm -rf")) {
      return { decision: "block", reason: "Destructive command blocked" };
    }
    return {}; // Empty object: allow the tool to proceed
  };

  // Filesystem hooks from .claude/settings.json run automatically
  // when settingSources loads them. You can also add programmatic hooks:
  for await (const message of query({
    prompt: "Refactor the auth module",
    options: {
      settingSources: ["project"], // Loads hooks from .claude/settings.json
      hooks: {
        PreToolUse: [{ matcher: "Bash", hooks: [auditBash] }]
      }
    }
  })) {
    if (message.type === "result" && message.subtype === "success") {
      console.log(message.result);
    }
  }
  ```
</CodeGroup>

### Cuándo usar qué tipo de hook

| Tipo de hook                                            | Mejor para                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sistema de archivos** (`settings.json`)               | Compartir hooks entre sesiones CLI y SDK. Admite `"command"` (scripts de shell), `"http"` (POST a un punto final), `"mcp_tool"` (llamar a la herramienta de un servidor MCP conectado), `"prompt"` (LLM evalúa un mensaje), y `"agent"` (genera un agente verificador). Se ejecutan en el agente principal y en cualquier subagenteque genere. |
| **Programático** (devoluciones de llamada en `query()`) | Lógica específica de la aplicación; devolver decisiones estructuradas; integración en proceso. Limitado a la sesión principal únicamente.                                                                                                                                                                                                      |

<Note>
  El SDK de TypeScript admite eventos de hook adicionales más allá de Python, incluidos `SessionStart`, `SessionEnd`, `TeammateIdle` y `TaskCompleted`. Consulte la [guía de hooks](/es/agent-sdk/hooks) para la tabla de compatibilidad de eventos completa.
</Note>

Para obtener detalles completos sobre hooks programáticos, consulte [Controlar la ejecución con hooks](/es/agent-sdk/hooks). Para la sintaxis de hooks del sistema de archivos, consulte [Hooks](/es/hooks).

## Elegir la característica correcta

El Agent SDK le proporciona acceso a varias formas de extender el comportamiento de su agente. Si no está seguro de cuál usar, esta tabla asigna objetivos comunes al enfoque correcto.

| Desea...                                                                                                          | Usar                                                     | Superficie del SDK                                                                                                                                                                                                   |
| :---------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Establecer convenciones de proyecto que su agente siempre sigue                                                   | [CLAUDE.md](/es/memory)                                  | `settingSources: ["project"]` lo carga automáticamente                                                                                                                                                               |
| Proporcionar al agente material de referencia que carga cuando es relevante                                       | [Skills](/es/agent-sdk/skills)                           | opción `settingSources` + `skills`                                                                                                                                                                                   |
| Ejecutar un flujo de trabajo reutilizable (desplegar, revisar, lanzar)                                            | [Skills invocables por el usuario](/es/agent-sdk/skills) | opción `settingSources` + `skills`                                                                                                                                                                                   |
| Delegar una subtarea aislada a un contexto nuevo (investigación, revisión)                                        | [Subagentos](/es/agent-sdk/subagents)                    | parámetro `agents` + `allowedTools: ["Agent"]`                                                                                                                                                                       |
| Coordinar múltiples instancias de Claude Code con listas de tareas compartidas y mensajería directa entre agentes | [Equipos de agentes](/es/agent-teams)                    | No se configura directamente a través de opciones del SDK. Los equipos de agentes son una característica CLI donde una sesión actúa como el líder del equipo, coordinando el trabajo entre compañeros independientes |
| Ejecutar lógica determinista en llamadas de herramientas (auditoría, bloqueo, transformación)                     | [Hooks](/es/agent-sdk/hooks)                             | parámetro `hooks` con devoluciones de llamada, o scripts de shell cargados a través de `settingSources`                                                                                                              |
| Proporcionar a Claude acceso a herramientas estructuradas a un servicio externo                                   | [MCP](/es/agent-sdk/mcp)                                 | parámetro `mcpServers`                                                                                                                                                                                               |

<Tip>
  **Subagentos versus equipos de agentes:** Los subagentos son efímeros y aislados: conversación nueva, una tarea, resumen devuelto al padre. Los equipos de agentes coordinan múltiples instancias independientes de Claude Code que comparten una lista de tareas y se envían mensajes directamente entre sí. Los equipos de agentes son una característica CLI. Consulte [Qué heredan los subagentos](/es/agent-sdk/subagents#what-subagents-inherit) y la [comparación de equipos de agentes](/es/agent-teams#compare-with-subagents) para obtener detalles.
</Tip>

Cada característica que habilita se suma a la ventana de contexto de su agente. Para costos por característica y cómo se superponen estas características, consulte [Extender Claude Code](/es/features-overview#understand-context-costs).

## Recursos relacionados

* [Extender Claude Code](/es/features-overview): Descripción conceptual de todas las características de extensión, con tablas de comparación y análisis de costos de contexto
* [Skills en el SDK](/es/agent-sdk/skills): Guía completa para usar skills programáticamente
* [Subagentos](/es/agent-sdk/subagents): Defina e invoque subagentos para subtareas aisladas
* [Hooks](/es/agent-sdk/hooks): Intercepte y controle el comportamiento del agente en puntos de ejecución clave
* [Permisos](/es/agent-sdk/permissions): Controle el acceso a herramientas con modos, reglas y devoluciones de llamada
* [Mensajes del sistema](/es/agent-sdk/modifying-system-prompts): Inyecte contexto sin archivos CLAUDE.md
