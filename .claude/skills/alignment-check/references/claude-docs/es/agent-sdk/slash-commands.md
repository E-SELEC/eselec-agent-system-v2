---
source_url: https://code.claude.com/docs/es/agent-sdk/slash-commands
fetched_url: https://code.claude.com/docs/es/agent-sdk/slash-commands.md
category: SDK de Agente
status: 200
scraped_at: 2026-05-15T14:28:36+00:00
sha256_16: cdae0a0ddafdf4db
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Slash Commands en el SDK

> Aprenda cómo usar slash commands para controlar sesiones de Claude Code a través del SDK

Los slash commands proporcionan una forma de controlar sesiones de Claude Code con comandos especiales que comienzan con `/`. Estos comandos se pueden enviar a través del SDK para realizar acciones como compactar contexto, listar el uso del contexto o invocar comandos personalizados. Solo los comandos que funcionan sin una terminal interactiva se pueden enviar a través del SDK; el mensaje `system/init` enumera los disponibles en su sesión.

## Descubrimiento de Slash Commands Disponibles

El Claude Agent SDK proporciona información sobre los slash commands disponibles en el mensaje de inicialización del sistema. Acceda a esta información cuando su sesión comience:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  for await (const message of query({
    prompt: "Hello Claude",
    options: { maxTurns: 1 }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      console.log("Available slash commands:", message.slash_commands);
      // Example output: ["/compact", "/context", "/usage"]
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, SystemMessage


  async def main():
      async for message in query(prompt="Hello Claude", options=ClaudeAgentOptions(max_turns=1)):
          if isinstance(message, SystemMessage) and message.subtype == "init":
              print("Available slash commands:", message.data["slash_commands"])
              # Example output: ["/compact", "/context", "/usage"]


  asyncio.run(main())
  ```
</CodeGroup>

## Envío de Slash Commands

Envíe slash commands incluyéndolos en su cadena de prompt, como texto normal:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  // Send a slash command
  for await (const message of query({
    prompt: "/compact",
    options: { maxTurns: 1 }
  })) {
    if (message.type === "result") {
      console.log("Command executed:", message.result);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage


  async def main():
      # Send a slash command
      async for message in query(prompt="/compact", options=ClaudeAgentOptions(max_turns=1)):
          if isinstance(message, ResultMessage):
              print("Command executed:", message.result)


  asyncio.run(main())
  ```
</CodeGroup>

## Slash Commands Comunes

### `/compact` - Compactar Historial de Conversación

El comando `/compact` reduce el tamaño de su historial de conversación resumiendo mensajes antiguos mientras preserva el contexto importante:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  for await (const message of query({
    prompt: "/compact",
    options: { maxTurns: 1 }
  })) {
    if (message.type === "system" && message.subtype === "compact_boundary") {
      console.log("Compaction completed");
      console.log("Pre-compaction tokens:", message.compact_metadata.pre_tokens);
      console.log("Trigger:", message.compact_metadata.trigger);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, SystemMessage


  async def main():
      async for message in query(prompt="/compact", options=ClaudeAgentOptions(max_turns=1)):
          if isinstance(message, SystemMessage) and message.subtype == "compact_boundary":
              print("Compaction completed")
              print("Pre-compaction tokens:", message.data["compact_metadata"]["pre_tokens"])
              print("Trigger:", message.data["compact_metadata"]["trigger"])


  asyncio.run(main())
  ```
</CodeGroup>

### Limpiar la conversación

El comando interactivo `/clear` no está disponible en el SDK. Cada llamada a `query()` ya comienza una conversación nueva, así que para limpiar el contexto, termine la `query()` actual e inicie una nueva. La conversación anterior se mantiene en disco y se puede recuperar pasando su ID de sesión a la [opción `resume`](/es/agent-sdk/sessions#resume-by-id).

## Creación de Slash Commands Personalizados

Además de usar slash commands integrados, puede crear sus propios comandos personalizados que estén disponibles a través del SDK. Los comandos personalizados se definen como archivos markdown en directorios específicos, similar a cómo se configuran los subagentes.

<Note>
  El directorio `.claude/commands/` es el formato heredado. El formato recomendado es `.claude/skills/<name>/SKILL.md`, que admite la misma invocación de slash command (`/name`) más invocación autónoma por Claude. Consulte [Skills](/es/agent-sdk/skills) para el formato actual. La CLI continúa admitiendo ambos formatos, y los ejemplos a continuación siguen siendo precisos para `.claude/commands/`.
</Note>

### Ubicaciones de Archivos

Los slash commands personalizados se almacenan en directorios designados según su alcance:

* **Comandos de proyecto**: `.claude/commands/` - Disponibles solo en el proyecto actual (heredado; prefiera `.claude/skills/`)
* **Comandos personales**: `~/.claude/commands/` - Disponibles en todos sus proyectos (heredado; prefiera `~/.claude/skills/`)

### Formato de Archivo

Cada comando personalizado es un archivo markdown donde:

* El nombre del archivo (sin extensión `.md`) se convierte en el nombre del comando
* El contenido del archivo define qué hace el comando
* El frontmatter YAML opcional proporciona configuración

#### Ejemplo Básico

Cree `.claude/commands/refactor.md`:

```markdown theme={null}
Refactor the selected code to improve readability and maintainability.
Focus on clean code principles and best practices.
```

Esto crea el comando `/refactor` que puede usar a través del SDK.

#### Con Frontmatter

Cree `.claude/commands/security-check.md`:

```markdown theme={null}
---
allowed-tools: Read, Grep, Glob
description: Run security vulnerability scan
model: claude-opus-4-7
---

Analyze the codebase for security vulnerabilities including:
- SQL injection risks
- XSS vulnerabilities
- Exposed credentials
- Insecure configurations
```

### Uso de Comandos Personalizados en el SDK

Una vez definidos en el sistema de archivos, los comandos personalizados están automáticamente disponibles a través del SDK:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  // Use a custom command
  for await (const message of query({
    prompt: "/refactor src/auth/login.ts",
    options: { maxTurns: 3 }
  })) {
    if (message.type === "assistant") {
      console.log("Refactoring suggestions:", message.message);
    }
  }

  // Custom commands appear in the slash_commands list
  for await (const message of query({
    prompt: "Hello",
    options: { maxTurns: 1 }
  })) {
    if (message.type === "system" && message.subtype === "init") {
      // Will include both built-in and custom commands
      console.log("Available commands:", message.slash_commands);
      // Example: ["/compact", "/context", "/usage", "/refactor", "/security-check"]
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, SystemMessage


  async def main():
      # Use a custom command
      async for message in query(
          prompt="/refactor src/auth/login.py", options=ClaudeAgentOptions(max_turns=3)
      ):
          if isinstance(message, AssistantMessage):
              for block in message.content:
                  if hasattr(block, "text"):
                      print("Refactoring suggestions:", block.text)

      # Custom commands appear in the slash_commands list
      async for message in query(prompt="Hello", options=ClaudeAgentOptions(max_turns=1)):
          if isinstance(message, SystemMessage) and message.subtype == "init":
              # Will include both built-in and custom commands
              print("Available commands:", message.data["slash_commands"])
              # Example: ["/compact", "/context", "/usage", "/refactor", "/security-check"]


  asyncio.run(main())
  ```
</CodeGroup>

### Características Avanzadas

#### Argumentos y Placeholders

Los comandos personalizados admiten argumentos dinámicos usando placeholders:

Cree `.claude/commands/fix-issue.md`:

```markdown theme={null}
---
argument-hint: [issue-number] [priority]
description: Fix a GitHub issue
---

Fix issue #$1 with priority $2.
Check the issue description and implement the necessary changes.
```

Úselo en el SDK:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  // Pass arguments to custom command
  for await (const message of query({
    prompt: "/fix-issue 123 high",
    options: { maxTurns: 5 }
  })) {
    // Command will process with $1="123" and $2="high"
    if (message.type === "result") {
      console.log("Issue fixed:", message.result);
    }
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage


  async def main():
      # Pass arguments to custom command
      async for message in query(prompt="/fix-issue 123 high", options=ClaudeAgentOptions(max_turns=5)):
          # Command will process with $1="123" and $2="high"
          if isinstance(message, ResultMessage):
              print("Issue fixed:", message.result)


  asyncio.run(main())
  ```
</CodeGroup>

#### Ejecución de Comandos Bash

Los comandos personalizados pueden ejecutar comandos bash e incluir su salida:

Cree `.claude/commands/git-commit.md`:

```markdown theme={null}
---
allowed-tools: Bash(git add *), Bash(git status *), Bash(git commit *)
description: Create a git commit
---

## Context

- Current status: !`git status`
- Current diff: !`git diff HEAD`

## Task

Create a git commit with appropriate message based on the changes.
```

#### Referencias de Archivos

Incluya contenidos de archivos usando el prefijo `@`:

Cree `.claude/commands/review-config.md`:

```markdown theme={null}
---
description: Review configuration files
---

Review the following configuration files for issues:
- Package config: @package.json
- TypeScript config: @tsconfig.json
- Environment config: @.env

Check for security issues, outdated dependencies, and misconfigurations.
```

### Organización con Espacios de Nombres

Organice comandos en subdirectorios para una mejor estructura:

```bash theme={null}
.claude/commands/
├── frontend/
│   ├── component.md      # Creates /component (project:frontend)
│   └── style-check.md     # Creates /style-check (project:frontend)
├── backend/
│   ├── api-test.md        # Creates /api-test (project:backend)
│   └── db-migrate.md      # Creates /db-migrate (project:backend)
└── review.md              # Creates /review (project)
```

El subdirectorio aparece en la descripción del comando pero no afecta el nombre del comando en sí.

### Ejemplos Prácticos

#### Comando de Revisión de Código

Cree `.claude/commands/code-review.md`:

```markdown theme={null}
---
allowed-tools: Read, Grep, Glob, Bash(git diff *)
description: Comprehensive code review
---

## Changed Files
!`git diff --name-only HEAD~1`

## Detailed Changes
!`git diff HEAD~1`

## Review Checklist

Review the above changes for:
1. Code quality and readability
2. Security vulnerabilities
3. Performance implications
4. Test coverage
5. Documentation completeness

Provide specific, actionable feedback organized by priority.
```

#### Comando de Ejecutor de Pruebas

Cree `.claude/commands/test.md`:

```markdown theme={null}
---
allowed-tools: Bash, Read, Edit
argument-hint: [test-pattern]
description: Run tests with optional pattern
---

Run tests matching pattern: $ARGUMENTS

1. Detect the test framework (Jest, pytest, etc.)
2. Run tests with the provided pattern
3. If tests fail, analyze and fix them
4. Re-run to verify fixes
```

Use estos comandos a través del SDK:

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  // Run code review
  for await (const message of query({
    prompt: "/code-review",
    options: { maxTurns: 3 }
  })) {
    // Process review feedback
  }

  // Run specific tests
  for await (const message of query({
    prompt: "/test auth",
    options: { maxTurns: 5 }
  })) {
    // Handle test results
  }
  ```

  ```python Python theme={null}
  import asyncio
  from claude_agent_sdk import query, ClaudeAgentOptions


  async def main():
      # Run code review
      async for message in query(prompt="/code-review", options=ClaudeAgentOptions(max_turns=3)):
          # Process review feedback
          pass

      # Run specific tests
      async for message in query(prompt="/test auth", options=ClaudeAgentOptions(max_turns=5)):
          # Handle test results
          pass


  asyncio.run(main())
  ```
</CodeGroup>

## Véase También

* [Slash Commands](/es/skills) - Documentación completa de slash commands
* [Subagentes en el SDK](/es/agent-sdk/subagents) - Configuración similar basada en sistema de archivos para subagentes
* [Referencia del SDK de TypeScript](/es/agent-sdk/typescript) - Documentación completa de la API
* [Descripción general del SDK](/es/agent-sdk/overview) - Conceptos generales del SDK
* [Referencia de CLI](/es/cli-reference) - Interfaz de línea de comandos
