---
name: reports
description: Create client reports, executive summaries, urgent alerts, and next-step roadmaps for E-SELEC. Use when the task is an informe mensual, reporte ejecutivo, resumen de resultados, alerta urgente, comunicacion al cliente, proximos pasos, roadmap mensual, or explanation of what happened and what should happen next.
---

# Reports - E-SELEC

## Proposito

Convertir datos, trabajo ejecutado y hallazgos en comunicacion que ayude al cliente y al sistema a decidir.

Principio central:

```text
Un buen informe toma decisiones.
Un mal informe ocupa espacio.
```

## Modos

Elige un modo antes de escribir:

| Modo | Usalo cuando | Template |
|---|---|---|
| `informe-mensual` | cierre mensual, resumen ejecutivo, resultados por servicio | `templates/informe-mensual.md` |
| `alerta` | caida, bloqueo, dato anomalo, riesgo que requiere accion hoy | `templates/alerta.md` |
| `proxpasos` | roadmap, plan de 7/30 dias, siguiente mes, cierre de auditoria | `templates/proxpasos.md` |

Si la tarea mezcla modos, entrega primero el modo mas urgente:

1. alerta;
2. informe mensual;
3. proximos pasos.

## Fuentes obligatorias

Leer antes de concluir:

- `clients/[cliente]/context.md`
- `clients/[cliente]/memory.md` si existe
- `clients/[cliente]/log.md`
- `clients/[cliente]/mensajes.md`
- `clients/[cliente]/tasks.md` si existe
- `clients/[cliente]/outputs/manifest.md` si existe
- `agency/brand.md` si el output sera visible para cliente
- `quality/criterios-output.md`

Leer segun el servicio activo:

- `references/fuentes-por-servicio.md`
- `.claude/skills/verificacion-medicion/SKILL.md` si la decision depende de datos
- `.claude/skills/analytics-tracking/SKILL.md` si el problema es medicion, GA4/GTM/eventos/conversiones
- `.claude/skills/copy-editing/SKILL.md` y `.claude/skills/humanizalo/SKILL.md` para revision final de claridad

No meter informes reales de clientes dentro de esta skill. Si un informe real deja un aprendizaje reutilizable, convertirlo en patron anonimo antes de moverlo a una referencia.

## Nivel de datos

Clasifica el informe antes de redactar:

| Nivel | Estado | Uso permitido |
|---|---|---|
| R0 | bloqueado | no entregar como informe final |
| R1 | parcial | entregar solo si abre declarando datos faltantes |
| R2 | suficiente | informe valido con fuentes y limites claros |
| R3 | completo | fuentes vivas o exports confiables para todos los servicios activos |

Reglas:

- Sin periodo claro, el informe es R0.
- Sin acciones del mes ni datos, el informe es R0 o R1.
- Si faltan GSC, GA4, GBP, Ads u otra fuente clave, marcar R1 salvo que el alcance no dependa de esa fuente.
- Si hay contradiccion entre `log.md`, datos vivos y contexto, detener y explicar la contradiccion.

## Workflow

### 1. Definir alcance

Identificar:

- cliente;
- periodo;
- audiencia: Rodrigo, equipo interno o cliente final;
- idioma del cliente;
- modo de informe;
- servicios activos.

Si el nivel tecnico del cliente no esta definido, usar lenguaje no tecnico por defecto.

### 2. Reconstruir trabajo y contexto

Separar:

- que se hizo realmente;
- que datos se midieron;
- que quedo pendiente;
- que alertas o dependencias siguen abiertas;
- que no se puede afirmar todavia.

No repetir tareas ya cerradas como si fueran nuevas.

### 3. Verificar medicion

Para cualquier metrica, confirmar:

- fuente;
- fecha o periodo;
- cliente/dominio/cuenta;
- limitacion;
- si es dato real, estimacion, observacion o inferencia.

No usar metricas sin fuente/fecha.

### 4. Traducir datos a negocio

No entregar listas de metricas. Cada dato importante debe responder:

- que paso;
- por que importa;
- que decision permite tomar;
- que se recomienda hacer ahora.

Ejemplo de criterio:

```text
Debil: "CTR aumento 15%".
Mejor: "Mas personas que vieron el resultado hicieron clic; ahora conviene reforzar las paginas que ya estan atrayendo demanda".
```

### 5. Redactar por modo

Usar el template correspondiente:

- `templates/informe-mensual.md`
- `templates/alerta.md`
- `templates/proxpasos.md`

Mantener la salida escaneable. Para clientes no tecnicos, priorizar claridad y accion sobre detalle.

### 6. Revisar antes de entregar

Aplicar:

- criterios universales de `quality/criterios-output.md`;
- Contrato 3 para informe mensual;
- Contrato 4 para proximos pasos;
- Contrato 11 si hubo verificacion de medicion;
- `copy-editing` y `humanizalo` si el texto sera visible para cliente.

## Reglas

- Maximo 3 prioridades en proximos pasos.
- Maximo 3 cifras clave en resumen ejecutivo.
- Una alerta requiere evidencia, impacto y accion inmediata.
- Un informe debe incluir resultados negativos si existen, con contexto.
- Un informe para cliente no tecnico no debe depender de jerga.
- Distinguir siempre trabajo hecho, resultado medido, interpretacion y recomendacion.
- Incluir "queda fuera" cuando ayuda a gestionar expectativas.

## Bloqueos

Detener o marcar como parcial si:

- no hay periodo;
- no hay cliente claro;
- faltan datos que cambian la conclusion;
- una metrica no tiene fuente o fecha;
- se mezclan datos de clientes;
- se promete resultado futuro;
- se quiere contactar al cliente sin aprobacion;
- se pide tocar GA4, GSC, Ads, GBP, CMS, email, CRM o cualquier produccion sin Orden de Cambio.

## Escritura

Por defecto, responder en chat.

Solo escribir archivos si:

- el command usa `--write`;
- Rodrigo lo pide explicitamente;
- o el flujo ya autorizo crear output.

Si escribes:

- guardar en `clients/[cliente]/outputs/`;
- actualizar `clients/[cliente]/outputs/manifest.md`;
- registrar en `clients/[cliente]/log.md`;
- aplicar control de artefactos;
- ejecutar guard antes de cerrar.

## Referencias

- `references/fuentes-por-servicio.md`
- `templates/informe-mensual.md`
- `templates/alerta.md`
- `templates/proxpasos.md`
