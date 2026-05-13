# Prompt Patterns

## Campos base

- Target tool.
- Task.
- Context.
- Inputs.
- Output format.
- Constraints.
- Forbidden actions.
- Success criteria.
- Stop conditions.

## Claude Code / coding agents

Incluir:

- starting state;
- target state;
- file scope;
- allowed tools/actions;
- forbidden actions;
- approval gates;
- verification;
- stop conditions.

Evitar tareas globales sin ruta.

## ChatGPT / general LLM

Usar instruccion compacta, output contract y limite de longitud si importa.

## Reasoning models

Instrucciones cortas. No pedir chain-of-thought visible.

## Browser / computer-use agents

Describir outcome, restricciones y acciones irreversibles que requieren permiso.

## Image / video AI

Separar sujeto, estilo, composicion, luz, movimiento, ratio y negativos.

## Prompts peligrosos

- Simular multiples expertos sin mecanismo real.
- Pedir razonamiento oculto visible.
- Pedir ejecutar compras, envios o cambios sin confirmacion.
- Mezclar muchas tareas independientes en una sola.
