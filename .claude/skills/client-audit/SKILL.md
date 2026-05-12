---
name: client-audit
description: >
  Audita un cliente de E-SELEC, revisa su estado digital, resume que se ha
  hecho, detecta bloqueos y define la proxima prioridad logica. Usalo cuando
  el usuario diga "audita a [cliente]", "como esta [cliente]", "revisa
  [cliente]", "que necesita [cliente]", "actualiza el contexto de [cliente]" o
  mencione un cliente sin tarea especifica.
---

# Client Audit - E-SELEC

## Proposito

Entender el estado real de un cliente y decidir una sola proxima prioridad logica.

Esta skill no existe para generar listas largas. Existe para crear una foto util del cliente:

- que sabemos;
- que se hizo;
- que falta;
- que esta bloqueado;
- que conviene hacer primero.

## Fuentes obligatorias

Antes de auditar un cliente existente, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/log.md`
3. `clients/[cliente]/mensajes.md`
4. `clients/[cliente]/tasks.md` si existe
5. `clients/[cliente]/memory.md` si existe
6. `quality/criterios-output.md`, Contrato 1 - Auditoria de cliente

Si el cliente no existe o no hay `context.md`, no inventes. Pregunta si se debe crear el cliente o hacer una auditoria orientativa.

## Nivel de datos

Clasifica la auditoria antes de escribir conclusiones:

- Nivel 3 - completo: contexto actualizado + historial + tareas + datos vivos relevantes.
- Nivel 2 - parcial: contexto e historial, pero faltan conectores o metricas.
- Nivel 1 - minimo: solo contexto basico o informacion incompleta.
- Nivel 0 - bloqueado: falta contexto minimo para decidir.

Regla:

- Nivel 0 no produce auditoria final.
- Nivel 1 produce diagnostico orientativo.
- Nivel 2 produce auditoria parcial.
- Nivel 3 produce auditoria completa.

## Workflow

### 1. Identificar el alcance

Determina:

- cliente;
- objetivo de la auditoria;
- si Rodrigo quiere solo lectura o tambien actualizar archivos;
- si el output debe quedar en chat o guardarse en `clients/[cliente]/outputs/`.

### 2. Leer memoria operativa

No saltes `memory.md` si existe. La memoria contiene preferencias, aprendizajes y cosas que ya funcionaron o fallaron.

Si `memory.md` contradice `context.md`, marca la contradiccion y no decidas solo.

### 3. Reconstruir estado actual

Extrae:

- negocio y oferta;
- servicios activos;
- fase del proyecto;
- web, redes, GBP, tracking y canales;
- ultimas acciones reales desde `log.md`;
- mensajes pendientes;
- tareas abiertas;
- aprendizajes de memoria;
- bloqueos.

### 4. Detectar prioridad

Prioriza en este orden:

1. Urgente: el cliente puede notarlo antes que nosotros.
2. Importante: tiene coste acumulativo si se retrasa.
3. Rutinario: puede esperar sin impacto relevante.

Despues cruza impacto/esfuerzo:

- impacto alto + esfuerzo bajo;
- impacto alto + esfuerzo alto;
- impacto medio + esfuerzo bajo;
- resto como pendiente.

### 5. Decidir si hacen falta datos vivos

No abras herramientas externas por defecto.

Usa fuentes vivas solo si cambian la decision:

- GA4/GSC para trafico, conversion o SEO;
- GBP para SEO local;
- Ads para campanas activas;
- WordPress/WooCommerce para estado tecnico o tienda;
- Notion para tareas si `tasks.md` parece desactualizado.

Si faltan accesos, entrega como parcial y explica que dato falta.

### 6. Generar output

Usa `templates/auditoria-cliente.md`.

Reglas:

- maximo 5 hallazgos;
- una sola proxima prioridad;
- no repetir tareas ya cerradas en `log.md`;
- no convertir oportunidades no contratadas en tareas;
- marcar datos pendientes;
- explicar limites.

### 7. Revisar antes de entregar

Usa `checklists/revision.md`.

El output minimo aceptable es nivel 2. El estandar E-SELEC es nivel 3.

### 8. Actualizar sistema solo si corresponde

No modifiques archivos por defecto.

Puedes actualizar archivos cuando:

- Rodrigo lo pidio explicitamente;
- el alcance aprobado incluye actualizar contexto/tareas;
- los cambios son de solo documentacion interna;
- aplicaste `protocols/control-artefactos.md`.

Si actualizas:

- `context.md`: registrar que campos cambiaron;
- `tasks.md`: solo proximas tareas relevantes de 7-14 dias;
- output guardado: actualizar `clients/[cliente]/outputs/manifest.md`;
- `log.md`: registrar cierre de sesion.

Para Notion, usa MCP si esta disponible. Si no esta disponible, deja instruccion clara de sincronizacion pendiente.

## Bloqueos

Detente si:

- no existe contexto minimo;
- hay contradiccion que cambia la prioridad;
- la tarea exige modificar produccion;
- se necesita acceso sensible no disponible;
- el usuario pide actualizar una fuente de verdad pero no esta claro cual prevalece.

## Archivos de apoyo

- `templates/auditoria-cliente.md`: formato de salida.
- `checklists/revision.md`: revision antes de entregar.

