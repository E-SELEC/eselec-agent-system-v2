---
name: prompt-master
description: >
  Crea, corrige u optimiza prompts para Claude Code, ChatGPT, OpenAI, Gemini,
  Cursor, v0, Midjourney, DALL-E, Kling, browser agents, coding agents y otras
  herramientas IA. Usalo cuando el usuario pida un prompt, mejorar un prompt,
  adaptar instrucciones o convertir una idea en un prompt listo para usar.
---

# Prompt Master - E-SELEC

## Proposito

Convertir una idea imprecisa en un prompt claro, acotado y listo para pegar en la herramienta correcta.

Esta skill produce prompts. No ejecuta automaticamente la herramienta destino.

## Fuentes obligatorias

Lee el pedido del usuario, contexto de agencia o cliente si aplica, `quality/criterios-output.md`, y la referencia de patrones si el target es ambiguo.

Necesitas target tool, tarea, input, output esperado, restricciones, criterios de exito y acciones prohibidas.

## Niveles

- PMT3 - listo: prompt listo para pegar, target claro, restricciones, output contract y stop conditions si aplica.
- PMT2 - fuerte: prompt util, faltan ejemplos o criterios finos.
- PMT1 - orientativo: prompt base con contexto parcial.
- PMT0 - bloqueado: falta target tool o tarea concreta.

## Workflow

1. Confirmar herramienta destino. Si es ambigua, preguntar.
2. Extraer tarea, contexto, inputs, formato de salida, restricciones y criterios de exito.
3. Elegir patron de `references/prompt-patterns.md`.
4. Incluir limites y acciones prohibidas, sobre todo para agentes con herramientas.
5. Evitar pedir chain-of-thought visible o tecnicas que simulan procesos inexistentes.
6. Entregar un solo prompt copiable usando `templates/prompt-output.md`.

## Reglas

- No mas de 3 preguntas antes de producir una version.
- No explicar teoria salvo que Rodrigo lo pida.
- No incluir instrucciones de razonamiento visible.
- Para agentes de codigo, incluir alcance, archivos, stop conditions y aprobaciones.
- Para browser/computer-use, incluir "no comprar, no enviar, no confirmar" salvo aprobacion.

## Bloqueos

- target tool desconocida y no se puede inferir;
- la tarea es demasiado amplia para un prompt unico;
- el prompt ejecutaria acciones sensibles sin permisos;
- faltan inputs esenciales.

## Referencias

- `references/prompt-patterns.md`: patrones por herramienta.
- `templates/prompt-output.md`: formato de salida.
- `checklists/revision.md`: revision final.
