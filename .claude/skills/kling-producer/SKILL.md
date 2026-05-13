---
name: kling-producer
description: >
  Produce briefs, prompts y planes para videos con Kling AI, DALL-E o imagen de
  referencia: image-to-video, text-to-video, motion control, lip sync, clips para
  redes, anuncios, web o piezas creativas. Usalo cuando se pida crear video,
  producir clip, Kling, prompt de video, imagen a video o video AI.
---

# Kling Producer - E-SELEC

## Proposito

Convertir una idea visual en un plan de produccion AI con prompt de imagen, prompt de video, parametros, coste estimado y pasos seguros.

Esta skill no ejecuta Kling ni consume creditos sin aprobacion explicita.

## Fuentes obligatorias

Lee el brief del usuario, contexto de agencia o cliente si aplica, `quality/criterios-output.md`, y `protocols/activos-criticos.md` si hay ejecucion real, imagen de cliente, marca o publicacion.

Necesitas sujeto, destino, mood, estilo, movimiento, ratio, duracion, imagen de referencia si existe y restricciones de marca.

## Niveles

- KP3 - listo: prompt de imagen/video, parametros, negativos, coste, riesgos y pasos.
- KP2 - fuerte: prompts listos, faltan imagen final o coste exacto.
- KP1 - orientativo: direccion visual con contexto parcial.
- KP0 - bloqueado: falta sujeto, destino o permiso para usar imagen.

## Workflow

1. Confirmar sujeto, destino, mood, estilo, movimiento y audio.
2. Si hay imagen propia, revisar aptitud: resolucion, ratio, luz, sujeto y permisos.
3. Elegir modo: image2video, text2video, motion-control o lip-sync.
4. Crear prompt de imagen si hace falta.
5. Crear prompt Kling, negative prompt y parametros.
6. Estimar coste/creditos y recomendar prueba segura.
7. Entregar usando `templates/video-production-plan.md`.

## Reglas

- No usar `--execute` ni abrir ejecucion real sin aprobacion explicita.
- Empezar por prueba corta cuando haya coste.
- No usar imagen de tercero sin permiso.
- No prometer resultado perfecto: video AI requiere iteracion.
- Marcar limitaciones de imagen, marca, derechos o coste.

## Bloqueos

- falta sujeto o destino;
- imagen sin permiso o con calidad insuficiente y el usuario no acepta riesgo;
- se pide ejecutar sin aprobar coste;
- contenido o marca requiere aprobacion previa.

## Referencias

- `references/kling-patterns.md`: modos, parametros y prompts.
- `templates/video-production-plan.md`: formato de salida.
- `checklists/revision.md`: revision final.
