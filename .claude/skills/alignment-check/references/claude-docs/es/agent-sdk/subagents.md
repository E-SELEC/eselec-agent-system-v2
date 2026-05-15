---
source_url: https://code.claude.com/docs/es/agent-sdk/subagents
fetched_url: https://code.claude.com/docs/es/agent-sdk/subagents.md
category: SDK de Agente
status: 200
scraped_at: 2026-05-15T14:28:31+00:00
sha256_16: cf0a7ead29753ca7
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Subagentes en el SDK

> Define e invoque subagentes para aislar contexto, ejecutar tareas en paralelo y aplicar instrucciones especializadas en sus aplicaciones Claude Agent SDK.

Los subagentes son instancias de agente separadas que su agente principal puede generar para manejar subtareas enfocadas.
Utilice subagentes para aislar contexto para subtareas enfocadas, ejecutar múltiples análisis en paralelo y aplicar instrucciones especializadas sin sobrecargar el prompt del agente principal.

Esta guía explica cómo definir y usar subagentes en el SDK utilizando el parámetro `agents`.

## Descripción general

Puede crear subagentes de tres formas:

* **Programáticamente**: use el parámetro `agents` en sus opciones `query()` ([TypeScript](/es/agent-sdk/typescript#agentdefinition), [Python](/es/agent-sdk/python#agentdefinition))
* **Basado en sistema de archivos**: defina agentes como archivos markdown en directorios `.claude/agents/` (consulte [definición de subagentes como archivos](/es/sub-agents))
* **Propósito general integrado**: Claude puede invocar el subagente integrado `general-purpose` en cualquier momento a través de la herramienta Agent sin que usted defina nada

Esta guía se enfoca en el enfoque programático, que se recomienda para aplicaciones SDK.

Cuando define subagentes, Claude determina si invocarlos en función del campo `description` de cada subagente. Escriba descripciones claras que expliquen cuándo se debe usar el subagente, y Claude delegará automáticamente las tareas apropiadas. También puede solicitar explícitamente un subagente por nombre en su prompt (por ejemplo, "Usa el agente code-reviewer para...").

## Beneficios de usar subagentes

### Aislamiento de contexto

Cada subagente se ejecuta en su propia conversación nueva. Las llamadas a herramientas intermedias y los resultados permanecen dentro del subagente; solo su mensaje final regresa al padre. Consulte [Qué heredan los subagentes](#what-subagents-inherit) para ver exactamente qué hay en el contexto del subagente.

**Ejemplo:** un subagente `research-assistant` puede explorar docenas de archivos sin que ninguno de ese contenido se acumule en la conversación principal. El padre recibe un resumen conciso, no cada archivo que leyó el subagente.

### Paralelización

Múltiples subagentes pueden ejecutarse simultáneamente, acelerando dramáticamente flujos de trabajo complejos.

**Ejemplo:** durante una revisión de código, puede ejecutar los subagentes `style-checker`, `security-scanner` y `test-coverage` simultáneamente, reduciendo el tiempo de revisión de minutos a segundos.

### Instrucciones y conocimiento especializados

Cada subagente puede tener prompts de sistema personalizados con experiencia específica, mejores prácticas y restricciones.

**Ejemplo:** un subagente `database-migration` puede tener conocimiento detallado sobre mejores prácticas de SQL, estrategias de reversión y verificaciones de integridad de datos que serían ruido innecesario en las instrucciones del agente principal.

### Restricciones de herramientas

Los subagentes pueden limitarse a herramientas específicas, reduciendo el riesgo de acciones no intencionadas.

**Ejemplo:** un subagente `doc-reviewer` podría tener acceso solo a las herramientas Read y Grep, asegurando que pueda analizar pero nunca modifique accidentalmente sus archivos de documentación.

## Creación de subagentes

### Definición programática (recomendada)

Defina subagentes directamente en su código utilizando el parámetro `agents`. Este ejemplo crea dos subagentes: un revisor de código con acceso de solo lectura y un ejecutor de pruebas que puede ejecutar comandos. La herramienta `Agent` debe incluirse en `allowedTools` ya que Claude invoca subagentes a través de la herramienta Agent.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition


  async def main():
      async for message in query(
          prompt="Review the authentication module for security issues",
          options=ClaudeAgentOptions(
              # Agent tool is required for subagent invocation
              allowed_tools=["Read", "Grep", "Glob", "Agent"],
              agents={
                  "code-reviewer": AgentDefinition(
                      # description tells Claude when to use this subagent
                      description="Expert code review specialist. Use for quality, security, and maintainability reviews.",
                      # prompt defines the subagent's behavior and expertise
                      prompt="""You are a code review specialist with expertise in security, performance, and best practices.

  When reviewing code:
  - Identify security vulnerabilities
  - Check for performance issues
  - Verify adherence to coding standards
  - Suggest specific improvements

  Be thorough but concise in your feedback.""",
                      # tools restricts what the subagent can do (read-only here)
                      tools=["Read", "Grep", "Glob"],
                      # model overrides the default model for this subagent
                      model="sonnet",
                  ),
                  "test-runner": AgentDefinition(
                      description="Runs and analyzes test suites. Use for test execution and coverage analysis.",
                      prompt="""You are a test execution specialist. Run tests and provide clear analysis of results.

  Focus on:
  - Running test commands
  - Analyzing test output
  - Identifying failing tests
  - Suggesting fixes for failures""",
                      # Bash access lets this subagent run test commands
                      tools=["Bash", "Read", "Grep"],
                  ),
              },
          ),
      ):
          if hasattr(message, "result"):
              print(message.result)


  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  for await (const message of query({
    prompt: "Review the authentication module for security issues",
    options: {
      // Agent tool is required for subagent invocation
      allowedTools: ["Read", "Grep", "Glob", "Agent"],
      agents: {
        "code-reviewer": {
          // description tells Claude when to use this subagent
          description:
            "Expert code review specialist. Use for quality, security, and maintainability reviews.",
          // prompt defines the subagent's behavior and expertise
          prompt: `You are a code review specialist with expertise in security, performance, and best practices.

  When reviewing code:
  - Identify security vulnerabilities
  - Check for performance issues
  - Verify adherence to coding standards
  - Suggest specific improvements

  Be thorough but concise in your feedback.`,
          // tools restricts what the subagent can do (read-only here)
          tools: ["Read", "Grep", "Glob"],
          // model overrides the default model for this subagent
          model: "sonnet"
        },
        "test-runner": {
          description:
            "Runs and analyzes test suites. Use for test execution and coverage analysis.",
          prompt: `You are a test execution specialist. Run tests and provide clear analysis of results.

  Focus on:
  - Running test commands
  - Analyzing test output
  - Identifying failing tests
  - Suggesting fixes for failures`,
          // Bash access lets this subagent run test commands
          tools: ["Bash", "Read", "Grep"]
        }
      }
    }
  })) {
    if ("result" in message) console.log(message.result);
  }
  ```
</CodeGroup>

### Configuración de AgentDefinition

| Campo             | Tipo                                                        | Requerido | Descripción                                                                                                                                                                         |
| :---------------- | :---------------------------------------------------------- | :-------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `description`     | `string`                                                    | Sí        | Descripción en lenguaje natural de cuándo usar este agente                                                                                                                          |
| `prompt`          | `string`                                                    | Sí        | El prompt del sistema del agente que define su rol y comportamiento                                                                                                                 |
| `tools`           | `string[]`                                                  | No        | Matriz de nombres de herramientas permitidas. Si se omite, hereda todas las herramientas                                                                                            |
| `disallowedTools` | `string[]`                                                  | No        | Matriz de nombres de herramientas a eliminar del conjunto de herramientas del agente                                                                                                |
| `model`           | `string`                                                    | No        | Anulación de modelo para este agente. Acepta un alias como `'sonnet'`, `'opus'`, `'haiku'`, `'inherit'`, o un ID de modelo completo. Por defecto es el modelo principal si se omite |
| `skills`          | `string[]`                                                  | No        | Lista de nombres de skills a precargar en el contexto del agente al inicio. Los skills no listados permanecen invocables a través de la herramienta Skill                           |
| `memory`          | `'user' \| 'project' \| 'local'`                            | No        | Fuente de memoria para este agente                                                                                                                                                  |
| `mcpServers`      | `(string \| object)[]`                                      | No        | Servidores MCP disponibles para este agente, por nombre o configuración en línea                                                                                                    |
| `maxTurns`        | `number`                                                    | No        | Número máximo de turnos de agente antes de que el agente se detenga                                                                                                                 |
| `background`      | `boolean`                                                   | No        | Ejecutar este agente como una tarea de fondo no bloqueante cuando se invoca                                                                                                         |
| `effort`          | `'low' \| 'medium' \| 'high' \| 'xhigh' \| 'max' \| number` | No        | Nivel de esfuerzo de razonamiento para este agente                                                                                                                                  |
| `permissionMode`  | `PermissionMode`                                            | No        | Modo de permiso para la ejecución de herramientas dentro de este agente                                                                                                             |

En el SDK de Python, estos nombres de campo usan camelCase para coincidir con el formato de cable. Consulte la referencia [`AgentDefinition`](/es/agent-sdk/python#agentdefinition) para obtener detalles.

<Note>
  Los subagentes no pueden generar sus propios subagentes. No incluya `Agent` en la matriz `tools` de un subagente.
</Note>

### Definición basada en sistema de archivos (alternativa)

También puede definir subagentes como archivos markdown en directorios `.claude/agents/`. Consulte la [documentación de subagentes de Claude Code](/es/sub-agents) para obtener detalles sobre este enfoque. Los agentes definidos programáticamente tienen prioridad sobre los agentes basados en sistema de archivos con el mismo nombre.

<Note>
  Incluso sin definir subagentes personalizados, Claude puede generar el subagente integrado `general-purpose` cuando `Agent` está en su `allowedTools`. Esto es útil para delegar tareas de investigación o exploración sin crear agentes especializados.
</Note>

## Qué heredan los subagentes

La ventana de contexto de un subagente comienza nueva (sin conversación padre) pero no está vacía. El único canal del padre al subagente es la cadena de prompt de la herramienta Agent, así que incluya cualquier ruta de archivo, mensaje de error o decisión que el subagente necesite directamente en ese prompt.

| El subagente recibe                                                                         | El subagente no recibe                                                              |
| :------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------- |
| Su propio prompt del sistema (`AgentDefinition.prompt`) y el prompt de la herramienta Agent | El historial de conversación del padre o resultados de herramientas                 |
| CLAUDE.md del proyecto (cargado a través de `settingSources`)                               | Contenido de skill precargado, a menos que esté listado en `AgentDefinition.skills` |
| Definiciones de herramientas (heredadas del padre, o el subconjunto en `tools`)             | El prompt del sistema del padre                                                     |

<Note>
  El padre recibe el mensaje final del subagente textualmente como el resultado de la herramienta Agent, pero puede resumirlo en su propia respuesta. Para preservar la salida del subagente textualmente en la respuesta visible para el usuario, incluya una instrucción para hacerlo en el prompt u opción `systemPrompt` que pase a la llamada `query()` **principal**.
</Note>

## Invocación de subagentes

### Invocación automática

Claude decide automáticamente cuándo invocar subagentes en función de la tarea y la `description` de cada subagente. Por ejemplo, si define un subagente `performance-optimizer` con la descripción "Especialista en optimización de rendimiento para ajuste de consultas", Claude lo invocará cuando su prompt mencione optimizar consultas.

Escriba descripciones claras y específicas para que Claude pueda hacer coincidir tareas con el subagente correcto.

### Invocación explícita

Para garantizar que Claude use un subagente específico, mencione su nombre en su prompt:

```text theme={null}
"Use the code-reviewer agent to check the authentication module"
```

Esto omite la coincidencia automática e invoca directamente el subagente nombrado.

### Configuración dinámica de agentes

Puede crear definiciones de agentes dinámicamente en función de condiciones en tiempo de ejecución. Este ejemplo crea un revisor de seguridad con diferentes niveles de rigor, utilizando un modelo más potente para revisiones estrictas.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition


  # Factory function that returns an AgentDefinition
  # This pattern lets you customize agents based on runtime conditions
  def create_security_agent(security_level: str) -> AgentDefinition:
      is_strict = security_level == "strict"
      return AgentDefinition(
          description="Security code reviewer",
          # Customize the prompt based on strictness level
          prompt=f"You are a {'strict' if is_strict else 'balanced'} security reviewer...",
          tools=["Read", "Grep", "Glob"],
          # Key insight: use a more capable model for high-stakes reviews
          model="opus" if is_strict else "sonnet",
      )


  async def main():
      # The agent is created at query time, so each request can use different settings
      async for message in query(
          prompt="Review this PR for security issues",
          options=ClaudeAgentOptions(
              allowed_tools=["Read", "Grep", "Glob", "Agent"],
              agents={
                  # Call the factory with your desired configuration
                  "security-reviewer": create_security_agent("strict")
              },
          ),
      ):
          if hasattr(message, "result"):
              print(message.result)


  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import { query, type AgentDefinition } from "@anthropic-ai/claude-agent-sdk";

  // Factory function that returns an AgentDefinition
  // This pattern lets you customize agents based on runtime conditions
  function createSecurityAgent(securityLevel: "basic" | "strict"): AgentDefinition {
    const isStrict = securityLevel === "strict";
    return {
      description: "Security code reviewer",
      // Customize the prompt based on strictness level
      prompt: `You are a ${isStrict ? "strict" : "balanced"} security reviewer...`,
      tools: ["Read", "Grep", "Glob"],
      // Key insight: use a more capable model for high-stakes reviews
      model: isStrict ? "opus" : "sonnet"
    };
  }

  // The agent is created at query time, so each request can use different settings
  for await (const message of query({
    prompt: "Review this PR for security issues",
    options: {
      allowedTools: ["Read", "Grep", "Glob", "Agent"],
      agents: {
        // Call the factory with your desired configuration
        "security-reviewer": createSecurityAgent("strict")
      }
    }
  })) {
    if ("result" in message) console.log(message.result);
  }
  ```
</CodeGroup>

## Detección de invocación de subagentes

Los subagentes se invocan a través de la herramienta Agent. Para detectar cuándo se invoca un subagente, busque bloques `tool_use` donde `name` sea `"Agent"`. Los mensajes desde dentro del contexto de un subagente incluyen un campo `parent_tool_use_id`.

<Note>
  El nombre de la herramienta se cambió de `"Task"` a `"Agent"` en Claude Code v2.1.63. Los lanzamientos actuales del SDK emiten `"Agent"` en bloques `tool_use` pero aún usan `"Task"` en la lista de herramientas `system:init` y en `result.permission_denials[].tool_name`. Verificar ambos valores en `block.name` asegura compatibilidad entre versiones del SDK.
</Note>

Este ejemplo itera a través de mensajes transmitidos, registrando cuándo se invoca un subagente y cuándo los mensajes posteriores se originan dentro del contexto de ejecución de ese subagente.

<Note>
  La estructura del mensaje difiere entre SDKs. En Python, los bloques de contenido se acceden directamente a través de `message.content`. En TypeScript, `SDKAssistantMessage` envuelve el mensaje de la API de Claude, por lo que el contenido se accede a través de `message.message.content`.
</Note>

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition


  async def main():
      async for message in query(
          prompt="Use the code-reviewer agent to review this codebase",
          options=ClaudeAgentOptions(
              allowed_tools=["Read", "Glob", "Grep", "Agent"],
              agents={
                  "code-reviewer": AgentDefinition(
                      description="Expert code reviewer.",
                      prompt="Analyze code quality and suggest improvements.",
                      tools=["Read", "Glob", "Grep"],
                  )
              },
          ),
      ):
          # Check for subagent invocation. Match both names: older SDK
          # versions emitted "Task", current versions emit "Agent".
          if hasattr(message, "content") and message.content:
              for block in message.content:
                  if getattr(block, "type", None) == "tool_use" and block.name in (
                      "Task",
                      "Agent",
                  ):
                      print(f"Subagent invoked: {block.input.get('subagent_type')}")

          # Check if this message is from within a subagent's context
          if hasattr(message, "parent_tool_use_id") and message.parent_tool_use_id:
              print("  (running inside subagent)")

          if hasattr(message, "result"):
              print(message.result)


  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  for await (const message of query({
    prompt: "Use the code-reviewer agent to review this codebase",
    options: {
      allowedTools: ["Read", "Glob", "Grep", "Agent"],
      agents: {
        "code-reviewer": {
          description: "Expert code reviewer.",
          prompt: "Analyze code quality and suggest improvements.",
          tools: ["Read", "Glob", "Grep"]
        }
      }
    }
  })) {
    const msg = message as any;

    // Check for subagent invocation. Match both names: older SDK versions
    // emitted "Task", current versions emit "Agent".
    for (const block of msg.message?.content ?? []) {
      if (block.type === "tool_use" && (block.name === "Task" || block.name === "Agent")) {
        console.log(`Subagent invoked: ${block.input.subagent_type}`);
      }
    }

    // Check if this message is from within a subagent's context
    if (msg.parent_tool_use_id) {
      console.log("  (running inside subagent)");
    }

    if ("result" in message) {
      console.log(message.result);
    }
  }
  ```
</CodeGroup>

## Reanudación de subagentes

Los subagentes pueden reanudarse para continuar donde se detuvieron. Los subagentes reanudados retienen su historial de conversación completo, incluidas todas las llamadas a herramientas anteriores, resultados y razonamiento. El subagente continúa exactamente donde se detuvo en lugar de comenzar de nuevo.

Cuando un subagente se completa, Claude recibe su ID de agente en el resultado de la herramienta Agent. Para reanudar un subagente programáticamente:

1. **Capture el ID de sesión**: Extraiga `session_id` de los mensajes durante la primera consulta
2. **Extraiga el ID del agente**: Analice `agentId` del contenido del mensaje
3. **Reanude la sesión**: Pase `resume: sessionId` en las opciones de la segunda consulta e incluya el ID del agente en su prompt

<Note>
  Debe reanudar la misma sesión para acceder a la transcripción del subagente. Cada llamada `query()` inicia una nueva sesión por defecto, así que pase `resume: sessionId` para continuar en la misma sesión.

  Si está usando un agente personalizado (no uno integrado), también necesita pasar la misma definición de agente en el parámetro `agents` para ambas consultas.
</Note>

El ejemplo a continuación demuestra este flujo: la primera consulta ejecuta un subagente y captura el ID de sesión e ID de agente, luego la segunda consulta reanuda la sesión para hacer una pregunta de seguimiento que requiere contexto del primer análisis.

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query, type SDKMessage } from "@anthropic-ai/claude-agent-sdk";

  // Helper to extract agentId from message content
  // Stringify to avoid traversing different block types (TextBlock, ToolResultBlock, etc.)
  function extractAgentId(message: SDKMessage): string | undefined {
    if (!("message" in message)) return undefined;
    // Stringify the content so we can search it without traversing nested blocks
    const content = JSON.stringify(message.message.content);
    const match = content.match(/agentId:\s*([a-f0-9-]+)/);
    return match?.[1];
  }

  let agentId: string | undefined;
  let sessionId: string | undefined;

  // First invocation - use the Explore agent to find API endpoints
  for await (const message of query({
    prompt: "Use the Explore agent to find all API endpoints in this codebase",
    options: { allowedTools: ["Read", "Grep", "Glob", "Agent"] }
  })) {
    // Capture session_id from ResultMessage (needed to resume this session)
    if ("session_id" in message) sessionId = message.session_id;
    // Search message content for the agentId (appears in Agent tool results)
    const extractedId = extractAgentId(message);
    if (extractedId) agentId = extractedId;
    // Print the final result
    if ("result" in message) console.log(message.result);
  }

  // Second invocation - resume and ask follow-up
  if (agentId && sessionId) {
    for await (const message of query({
      prompt: `Resume agent ${agentId} and list the top 3 most complex endpoints`,
      options: { allowedTools: ["Read", "Grep", "Glob", "Agent"], resume: sessionId }
    })) {
      if ("result" in message) console.log(message.result);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  import json
  import re
  from claude_agent_sdk import query, ClaudeAgentOptions


  def extract_agent_id(text: str) -> str | None:
      """Extract agentId from Agent tool result text."""
      match = re.search(r"agentId:\s*([a-f0-9-]+)", text)
      return match.group(1) if match else None


  async def main():
      agent_id = None
      session_id = None

      # First invocation - use the Explore agent to find API endpoints
      async for message in query(
          prompt="Use the Explore agent to find all API endpoints in this codebase",
          options=ClaudeAgentOptions(allowed_tools=["Read", "Grep", "Glob", "Agent"]),
      ):
          # Capture session_id from ResultMessage (needed to resume this session)
          if hasattr(message, "session_id"):
              session_id = message.session_id
          # Search message content for the agentId (appears in Agent tool results)
          if hasattr(message, "content"):
              # Stringify the content so we can search it without traversing nested blocks
              content_str = json.dumps(message.content, default=str)
              extracted = extract_agent_id(content_str)
              if extracted:
                  agent_id = extracted
          # Print the final result
          if hasattr(message, "result"):
              print(message.result)

      # Second invocation - resume and ask follow-up
      if agent_id and session_id:
          async for message in query(
              prompt=f"Resume agent {agent_id} and list the top 3 most complex endpoints",
              options=ClaudeAgentOptions(
                  allowed_tools=["Read", "Grep", "Glob", "Agent"], resume=session_id
              ),
          ):
              if hasattr(message, "result"):
                  print(message.result)


  asyncio.run(main())
  ```
</CodeGroup>

Las transcripciones de subagentes persisten independientemente de la conversación principal:

* **Compactación de conversación principal**: Cuando la conversación principal se compacta, las transcripciones de subagentes no se ven afectadas. Se almacenan en archivos separados.
* **Persistencia de sesión**: Las transcripciones de subagentes persisten dentro de su sesión. Puede reanudar un subagente después de reiniciar Claude Code reanudando la misma sesión.
* **Limpieza automática**: Las transcripciones se limpian en función de la configuración `cleanupPeriodDays` (predeterminado: 30 días).

## Restricciones de herramientas

Los subagentes pueden tener acceso restringido a herramientas a través del campo `tools`:

* **Omitir el campo**: el agente hereda todas las herramientas disponibles (predeterminado)
* **Especificar herramientas**: el agente solo puede usar las herramientas listadas

Este ejemplo crea un agente de análisis de solo lectura que puede examinar código pero no puede modificar archivos ni ejecutar comandos.

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, AgentDefinition


  async def main():
      async for message in query(
          prompt="Analyze the architecture of this codebase",
          options=ClaudeAgentOptions(
              allowed_tools=["Read", "Grep", "Glob", "Agent"],
              agents={
                  "code-analyzer": AgentDefinition(
                      description="Static code analysis and architecture review",
                      prompt="""You are a code architecture analyst. Analyze code structure,
  identify patterns, and suggest improvements without making changes.""",
                      # Read-only tools: no Edit, Write, or Bash access
                      tools=["Read", "Grep", "Glob"],
                  )
              },
          ),
      ):
          if hasattr(message, "result"):
              print(message.result)


  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  for await (const message of query({
    prompt: "Analyze the architecture of this codebase",
    options: {
      allowedTools: ["Read", "Grep", "Glob", "Agent"],
      agents: {
        "code-analyzer": {
          description: "Static code analysis and architecture review",
          prompt: `You are a code architecture analyst. Analyze code structure,
  identify patterns, and suggest improvements without making changes.`,
          // Read-only tools: no Edit, Write, or Bash access
          tools: ["Read", "Grep", "Glob"]
        }
      }
    }
  })) {
    if ("result" in message) console.log(message.result);
  }
  ```
</CodeGroup>

### Combinaciones comunes de herramientas

| Caso de uso              | Herramientas                            | Descripción                                                      |
| :----------------------- | :-------------------------------------- | :--------------------------------------------------------------- |
| Análisis de solo lectura | `Read`, `Grep`, `Glob`                  | Puede examinar código pero no modificar ni ejecutar              |
| Ejecución de pruebas     | `Bash`, `Read`, `Grep`                  | Puede ejecutar comandos y analizar salida                        |
| Modificación de código   | `Read`, `Edit`, `Write`, `Grep`, `Glob` | Acceso completo de lectura/escritura sin ejecución de comandos   |
| Acceso completo          | Todas las herramientas                  | Hereda todas las herramientas del padre (omita el campo `tools`) |

## Solución de problemas

### Claude no delega a subagentes

Si Claude completa tareas directamente en lugar de delegar a su subagente:

1. **Incluya la herramienta Agent**: los subagentes se invocan a través de la herramienta Agent, por lo que debe estar en `allowedTools`
2. **Use prompting explícito**: mencione el subagente por nombre en su prompt (por ejemplo, "Usa el agente code-reviewer para...")
3. **Escriba una descripción clara**: explique exactamente cuándo se debe usar el subagente para que Claude pueda hacer coincidir las tareas apropiadamente

### Agentes basados en sistema de archivos no se cargan

Los agentes definidos en `.claude/agents/` se cargan solo al inicio. Si crea un nuevo archivo de agente mientras Claude Code está en ejecución, reinicie la sesión para cargarlo.

### Windows: fallos de prompt largo

En Windows, los subagentes con prompts muy largos pueden fallar debido a límites de longitud de línea de comandos (8191 caracteres). Mantenga los prompts concisos o use agentes basados en sistema de archivos para instrucciones complejas.

## Documentación relacionada

* [Subagentes de Claude Code](/es/sub-agents): documentación completa de subagentes incluyendo definiciones basadas en sistema de archivos
* [Descripción general del SDK](/es/agent-sdk/overview): introducción al Claude Agent SDK
