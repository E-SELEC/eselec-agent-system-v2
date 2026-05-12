# Diagnostico de calidad de outputs

## Estado

- ID: P1-001
- Fecha: 2026-05-12
- Responsable: Codex + Arquitecto
- Sistema: E-SELEC Agent System v2
- Estado: vigente

## Fuentes revisadas

### Documentacion Claude Code

- `https://code.claude.com/docs/es/how-claude-code-works`
- `https://code.claude.com/docs/es/best-practices`
- `https://code.claude.com/docs/es/memory`
- `https://code.claude.com/docs/es/context-window`
- `https://code.claude.com/docs/es/sub-agents`
- `https://code.claude.com/docs/es/skills`
- `https://code.claude.com/docs/es/hooks`
- `https://code.claude.com/docs/es/settings`

### Sistema legacy revisado

- `agents/leader-clients.md`
- `agents/seo/leader-seo.md`
- `agents/reports/leader-reports.md`
- `agents/calibracion/calibracion.md`
- `agents/docente/docente.md`
- `agents/docente/docente-seo.md`
- `agency/preferencias-rodrigo.md`
- indice de skills en `.agents/skills/`
- estructura SEO y Reports legacy
- protocolos migrados en P0

## Tesis principal

El problema de calidad no parece ser que el sistema no tenga criterio.

El sistema legacy tiene mucho criterio, pero esta demasiado mezclado, demasiado cargado en contexto activo y poco convertido en verificaciones concretas de salida.

La mejora no debe empezar creando mas agentes. Debe empezar separando:

- instrucciones siempre activas;
- reglas contextuales;
- skills bajo demanda;
- subagents con responsabilidad clara;
- contratos de output verificables;
- aprendizaje calibrado.

## Principios Claude Code aplicados

1. Claude Code trabaja en un bucle de contexto, accion y verificacion. Si falta verificacion, el output puede parecer correcto sin estar probado.
2. La ventana de contexto se degrada cuando se llena de informacion irrelevante. Las reglas largas dentro de un lider reducen consistencia.
3. Las instrucciones persistentes deben ser concisas y especificas. Cuanto mas largas y mezcladas, menos fiables.
4. Las skills deben cargar procedimientos y archivos de apoyo solo cuando hacen falta.
5. Los subagents sirven para aislar investigacion y responsabilidad en contextos separados.
6. La memoria sirve para aprendizajes especificos, no para meter todo el sistema en cada tarea.
7. Los hooks y permisos deben proteger acciones sensibles, pero no sustituyen criterios de calidad.

## Matriz de causas raiz

| ID | Causa raiz | Sintoma en legacy | Impacto en outputs | Decision v2 | Accion |
|---|---|---|---|---|---|
| Q-001 | Contexto activo demasiado grande | `agents/leader-clients.md` mezcla routing, protocolos, playbooks, aprobaciones, prioridad, cierre, errores y reglas universales en un solo archivo largo | El agente puede perder reglas clave, priorizar instrucciones secundarias o responder con criterio irregular | Reescribir, no copiar | Mantener `CLAUDE.md` pequeno, mover reglas a `.claude/rules/`, procedimientos a skills y comandos |
| Q-002 | Criterio sin contrato de salida | Hay principios buenos, pero no siempre hay definicion de "output aprobado" por tipo de entregable | Informes, auditorias o planes pueden sonar bien pero carecer de profundidad, evidencia o utilidad | Crear | P1-002 debe crear criterios de output por servicio |
| Q-003 | Verificacion insuficiente | Muchos prompts dicen "verifica" o "no inventes", pero no exigen prueba final estructurada | Outputs sin datos, sin fuente, sin comparacion contra objetivo o sin pass/fail | Crear gates | Cada skill migrada debe incluir checklist de verificacion y condiciones de bloqueo |
| Q-004 | Sub-agentes no nativos | Los sub-agentes legacy son archivos markdown, no subagents Claude Code con contexto, herramientas y responsabilidad aislada | Se hereda demasiado contexto del lider y se diluye la especializacion | Reestructurar | Migrar solo roles utiles a `.claude/agents/` con scope, tools y entregable claro |
| Q-005 | Skills desconectadas del flujo | Hay muchas skills valiosas, pero el flujo legacy depende de que el agente recuerde leerlas | La ejecucion puede saltarse metodologia especializada | Reempaquetar | Migrar primero skills de alto impacto y activacion clara: `client-audit`, `seo-audit` |
| Q-006 | Memoria de cliente no integrada de forma consistente | AGENTS exige leer `memory.md`, pero el lider legacy enumera `context.md`, `log.md`, `mensajes.md`, `tasks.md` y no siempre incluye memoria | Se repiten errores de tono, preferencias y aprendizajes por cliente | Corregir | Lider Clientes v2 debe tener lectura obligatoria de `memory.md` antes de outputs |
| Q-007 | Aprendizaje existe, pero no se examina | Calibracion y Docente capturan aprendizajes, pero no siempre crean prueba de conducta futura | El sistema "guarda" informacion sin garantizar que cambia decisiones | Reforzar | Docente v2 debe producir caso de prueba por aprendizaje importante |
| Q-008 | Fuente de verdad dispersa | Notion, context, log, mensajes, conectores y outputs aparecen en varios lugares con jerarquias no siempre operativas | Decisiones basadas en datos parciales o contradictorios | Normalizar | Crear reglas por tipo de dato y gates de "dato parcial" en cada skill |
| Q-009 | Modelo/router usado como sustituto de calidad | Tiering reduce coste, pero no define criterios de aceptacion | Un tier barato puede generar borradores aceptables superficialmente pero flojos para decisiones complejas | Ajustar | Router debe depender de riesgo, evidencia requerida y criterio, no solo tipo general de tarea |
| Q-010 | Demasiadas aprobaciones y excepciones mezcladas | Hay reglas como "nunca ejecutar sin aprobacion" y tambien "elige ejecucion ante duda" | El agente puede bloquearse o ejecutar con inseguridad segun que regla recuerde | Clarificar | Separar modo: diagnostico, propuesta, ejecucion, produccion |
| Q-011 | Outputs no comparados contra ejemplos buenos | No hay biblioteca clara de ejemplos aprobados por Rodrigo por tipo de entregable | El estilo y profundidad varian entre sesiones | Crear | P1 debe crear ejemplos canonicos por servicio despues del primer piloto |
| Q-012 | Riesgo de copiar historico como contexto vivo | Legacy contiene muchos archivos utiles pero tambien historico, duplicados y criterios antiguos | Se puede migrar deuda cognitiva al v2 | Bloquear arrastre | Toda migracion debe pasar por inventario, decision y prueba de calidad |

## Diagnostico por area

### Lider Clientes

Fortalezas:

- tiene razonamiento de prioridad;
- distingue urgente, importante y rutinario;
- incluye datos insuficientes;
- tiene protocolos de seguridad y cierre;
- reconoce conflictos antes de ejecutar.

Riesgos:

- archivo demasiado largo para ser instruccion activa;
- mezcla estrategia, operacion, seguridad, presentacion y playbooks;
- contiene reglas que pueden competir entre si;
- no convierte cada salida en prueba de calidad.

Decision v2:

```text
No copiar como subagent entero.
Extraer responsabilidad central y convertir el resto en rules, commands y skills.
```

### SEO

Fortalezas:

- buen mapa de subespecialidades;
- reglas SEMrush + GSC valiosas;
- principios SEO claros;
- dependencias razonables entre tecnico, organico, local, LLM y web.

Riesgos:

- los archivos son largos y algunos contienen mucha referencia de herramienta;
- falta contrato de output por tipo de auditoria;
- no siempre hay criterio pass/fail de calidad;
- riesgo de hacer SEO con fuente parcial sin marcarlo con suficiente fuerza.

Decision v2:

```text
Migrar primero `seo-audit` como skill verificable.
Luego migrar Lider SEO como subagent ligero.
Dejar SEMrush workflows como referencia bajo demanda, no como contexto siempre activo.
```

### Reports

Fortalezas:

- entiende que un buen informe debe tomar decisiones;
- distingue mensual, alerta y proximos pasos;
- adapta lenguaje al nivel tecnico del cliente.

Riesgos:

- lider muy breve comparado con la complejidad del output;
- no define estructura de evidencia minima;
- no define que graficas, datos o conclusiones son obligatorias;
- puede producir informes bonitos pero poco accionables.

Decision v2:

```text
Crear contrato de informe antes de migrar Reports.
Un informe debe tener datos, lectura de negocio, decision y siguiente accion.
```

### Calibracion y Docente

Fortalezas:

- separan preferencia de Rodrigo, aprendizaje de cliente y criterio operativo;
- evitan guardar ruido;
- Docente exige prueba de aprendizaje.

Riesgos:

- no estan conectados como gate obligatorio despues de un output rechazado;
- pueden quedar como documentos aislados si no modifican skills/reglas;
- Docente SEO esta en fase de aprendizaje desde cero y no debe contaminar agentes reales sin aprobacion.

Decision v2:

```text
Conservar filosofia.
Convertir Calibracion en command o skill.
Convertir Docente en subagent con permisos limitados y pruebas de conducta.
```

## Arquitectura de calidad propuesta

Cada entregable debe pasar por cuatro capas.

### 1. Intake

Antes de ejecutar:

- cliente o area;
- objetivo del output;
- audiencia;
- datos disponibles;
- datos faltantes;
- fuente de verdad;
- nivel de riesgo;
- criterio de exito.

### 2. Ejecucion

Durante la tarea:

- usar solo la skill necesaria;
- cargar referencias bajo demanda;
- limitar contexto a fuentes relevantes;
- separar analisis de redaccion;
- marcar supuestos.

### 3. Verificacion

Antes de entregar:

- comprobar que responde al objetivo;
- comprobar evidencia y fuentes;
- comprobar contradicciones con contexto/log/mensajes;
- comprobar formato esperado;
- comprobar tono y audiencia;
- declarar si es parcial.

### 4. Aprendizaje

Despues del output:

- si Rodrigo corrige, activar Calibracion;
- si el fallo revela criterio, activar Docente;
- si cambia estructura, activar Arquitecto/Fenix;
- registrar aprendizaje solo si cambia conducta futura.

## Reglas P1 para no perder calidad

1. No migrar mas agentes antes de crear criterios de output.
2. No copiar prompts largos como instrucciones siempre activas.
3. No aumentar numero de agentes como solucion primaria.
4. No confiar en el router de modelos como garantia de calidad.
5. No crear informes/auditorias sin checklist de verificacion.
6. No cerrar outputs con datos parciales sin marcar limitacion.
7. No guardar aprendizaje si no cambia conducta futura.
8. No meter documentacion extensa en `CLAUDE.md`.

## Acciones siguientes

### P1-002

Crear `quality/criterios-output.md` con contratos de salida por servicio:

- auditoria cliente;
- auditoria SEO;
- informe mensual;
- proximos pasos;
- contenido/copy;
- CRO;
- SEM;
- web.

Cada contrato debe incluir:

- objetivo;
- inputs minimos;
- fuentes preferidas;
- estructura;
- criterios de aceptacion;
- motivos de bloqueo;
- checklist de revision;
- ejemplo de output bueno o placeholder para ejemplo.

### P1-003

Migrar `client-audit` como skill piloto.

Debe incluir:

- `SKILL.md`;
- plantilla de auditoria;
- checklist de verificacion;
- criterios de dato parcial.

### P1-004

Migrar `seo-audit` como segunda skill.

Debe incluir:

- fuente SEMrush + GSC cuando existan;
- matriz impacto/esfuerzo;
- bloqueo por datos insuficientes;
- formato de output verificable.

### P1-005

Migrar Docente como rol de aprendizaje.

Debe incluir:

- permisos limitados;
- output de capacitacion;
- prueba de conducta futura;
- relacion con Calibracion y Arquitecto.

## Criterio de exito de P1

P1 estara bien si Rodrigo deja de recibir outputs que "suenan correctos" pero no sabe si son buenos.

Un output bueno en v2 debe poder responder:

- que objetivo cumple;
- con que datos se hizo;
- que faltaba;
- que decision recomienda;
- por que esa decision importa;
- como sabemos que no es humo;
- que debe pasar despues.

