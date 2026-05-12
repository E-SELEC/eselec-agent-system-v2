# Checklist de revision - client-audit

Antes de entregar, verifica:

## Datos

- [ ] Lei `context.md`.
- [ ] Lei `log.md`.
- [ ] Lei `mensajes.md`.
- [ ] Lei `tasks.md` si existe.
- [ ] Lei `memory.md` si existe.
- [ ] Declare nivel de datos.
- [ ] Marque datos faltantes.

## Calidad

- [ ] El snapshot del negocio cabe en 1-2 frases.
- [ ] Hay maximo 5 hallazgos principales.
- [ ] Cada hallazgo importante tiene evidencia.
- [ ] No repito tareas ya completadas en log.
- [ ] No convierto servicios no contratados en tareas activas.
- [ ] Hay una sola proxima prioridad.
- [ ] La prioridad tiene impacto, esfuerzo y motivo.

## Riesgo

- [ ] No propongo tocar produccion sin `protocols/activos-criticos.md`.
- [ ] No registro ni pido secretos reales.
- [ ] Si hay contradiccion entre fuentes, la marco y no decido solo.
- [ ] Si el output es parcial, lo digo al inicio o en estado.

## Cierre

- [ ] Digo que cambio si modifique archivos.
- [ ] Registro artefactos si cree o modifique outputs.
- [ ] Dejo un siguiente paso concreto.

