---
source_url: https://code.claude.com/docs/es/agent-sdk/todo-tracking
fetched_url: https://code.claude.com/docs/es/agent-sdk/todo-tracking.md
category: SDK de Agente
status: 200
scraped_at: 2026-05-15T14:28:32+00:00
sha256_16: 0e3653094b94127d
sanitized: true
---

> ## Documentation Index
> Fetch the complete documentation index at: https://code.claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Listas de Tareas

> Rastrear y mostrar tareas pendientes utilizando el SDK del Agente Claude para la gestión organizada de tareas

El seguimiento de tareas proporciona una forma estructurada de gestionar tareas y mostrar el progreso a los usuarios. El SDK del Agente Claude incluye funcionalidad de tareas integrada que ayuda a organizar flujos de trabajo complejos y mantener a los usuarios informados sobre la progresión de las tareas.

### Ciclo de Vida de las Tareas

Las tareas siguen un ciclo de vida predecible:

1. **Creadas** como `pending` cuando se identifican las tareas
2. **Activadas** a `in_progress` cuando comienza el trabajo
3. **Completadas** cuando la tarea finaliza exitosamente
4. **Eliminadas** cuando todas las tareas en un grupo se completan

### Cuándo se Utilizan las Tareas

El SDK crea automáticamente tareas para:

* **Tareas complejas de múltiples pasos** que requieren 3 o más acciones distintas
* **Listas de tareas proporcionadas por el usuario** cuando se mencionan múltiples elementos
* **Operaciones no triviales** que se benefician del seguimiento del progreso
* **Solicitudes explícitas** cuando los usuarios piden organización de tareas

## Ejemplos

### Monitoreo de Cambios en Tareas

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  for await (const message of query({
    prompt: "Optimize my React app performance and track progress with todos",
    options: { maxTurns: 15 }
  })) {
    // Todo updates are reflected in the message stream
    if (message.type === "assistant") {
      for (const block of message.message.content) {
        if (block.type === "tool_use" && block.name === "TodoWrite") {
          const todos = block.input.todos;

          console.log("Todo Status Update:");
          todos.forEach((todo, index) => {
            const status =
              todo.status === "completed" ? "✅" : todo.status === "in_progress" ? "🔧" : "❌";
            console.log(`${index + 1}. ${status} ${todo.content}`);
          });
        }
      }
    }
  }
  ```

  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ToolUseBlock

  async for message in query(
      prompt="Optimize my React app performance and track progress with todos",
      options=ClaudeAgentOptions(max_turns=15),
  ):
      # Todo updates are reflected in the message stream
      if isinstance(message, AssistantMessage):
          for block in message.content:
              if isinstance(block, ToolUseBlock) and block.name == "TodoWrite":
                  todos = block.input["todos"]

                  print("Todo Status Update:")
                  for i, todo in enumerate(todos):
                      status = (
                          "✅"
                          if todo["status"] == "completed"
                          else "🔧"
                          if todo["status"] == "in_progress"
                          else "❌"
                      )
                      print(f"{i + 1}. {status} {todo['content']}")
  ```
</CodeGroup>

### Visualización de Progreso en Tiempo Real

<CodeGroup>
  ```typescript TypeScript theme={null}
  import { query } from "@anthropic-ai/claude-agent-sdk";

  class TodoTracker {
    private todos: any[] = [];

    displayProgress() {
      if (this.todos.length === 0) return;

      const completed = this.todos.filter((t) => t.status === "completed").length;
      const inProgress = this.todos.filter((t) => t.status === "in_progress").length;
      const total = this.todos.length;

      console.log(`\nProgress: ${completed}/${total} completed`);
      console.log(`Currently working on: ${inProgress} task(s)\n`);

      this.todos.forEach((todo, index) => {
        const icon =
          todo.status === "completed" ? "✅" : todo.status === "in_progress" ? "🔧" : "❌";
        const text = todo.status === "in_progress" ? todo.activeForm : todo.content;
        console.log(`${index + 1}. ${icon} ${text}`);
      });
    }

    async trackQuery(prompt: string) {
      for await (const message of query({
        prompt,
        options: { maxTurns: 20 }
      })) {
        if (message.type === "assistant") {
          for (const block of message.message.content) {
            if (block.type === "tool_use" && block.name === "TodoWrite") {
              this.todos = block.input.todos;
              this.displayProgress();
            }
          }
        }
      }
    }
  }

  // Usage
  const tracker = new TodoTracker();
  await tracker.trackQuery("Build a complete authentication system with todos");
  ```

  ```python Python theme={null}
  from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, ToolUseBlock
  from typing import List, Dict


  class TodoTracker:
      def __init__(self):
          self.todos: List[Dict] = []

      def display_progress(self):
          if not self.todos:
              return

          completed = len([t for t in self.todos if t["status"] == "completed"])
          in_progress = len([t for t in self.todos if t["status"] == "in_progress"])
          total = len(self.todos)

          print(f"\nProgress: {completed}/{total} completed")
          print(f"Currently working on: {in_progress} task(s)\n")

          for i, todo in enumerate(self.todos):
              icon = (
                  "✅"
                  if todo["status"] == "completed"
                  else "🔧"
                  if todo["status"] == "in_progress"
                  else "❌"
              )
              text = (
                  todo["activeForm"]
                  if todo["status"] == "in_progress"
                  else todo["content"]
              )
              print(f"{i + 1}. {icon} {text}")

      async def track_query(self, prompt: str):
          async for message in query(prompt=prompt, options=ClaudeAgentOptions(max_turns=20)):
              if isinstance(message, AssistantMessage):
                  for block in message.content:
                      if isinstance(block, ToolUseBlock) and block.name == "TodoWrite":
                          self.todos = block.input["todos"]
                          self.display_progress()


  # Usage
  tracker = TodoTracker()
  await tracker.track_query("Build a complete authentication system with todos")
  ```
</CodeGroup>

## Documentación Relacionada

* [Referencia del SDK de TypeScript](/es/agent-sdk/typescript)
* [Referencia del SDK de Python](/es/agent-sdk/python)
* [Modo de Streaming vs Modo Único](/es/agent-sdk/streaming-vs-single-mode)
* [Herramientas Personalizadas](/es/agent-sdk/custom-tools)
