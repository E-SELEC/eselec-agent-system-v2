# Plan maestro de migracion E-SELEC v2

## Proposito

Este documento organiza la migracion del sistema antiguo E-SELEC al sistema v2 basado en Claude Code.

El objetivo no es mover archivos. El objetivo es construir un sistema que produzca resultados mejores, mas consistentes y mas seguros.

## Explicacion simple para Rodrigo

Tu sistema antiguo tiene valor real: memoria, protocolos, agentes, clientes, skills, scripts y aprendizajes. El problema es que nacio rapido, con muchas piezas mezcladas. Eso puede provocar resultados flojos porque el agente recibe demasiado contexto, contexto contradictorio, instrucciones repetidas, procedimientos mal ubicados o criterios poco verificables.

Claude Code propone separar las responsabilidades:

- Lo que siempre debe saber: `CLAUDE.md` y `AGENTS.md`.
- Lo que aplica por tema o ruta: `.claude/rules/`.
- Lo que es un procedimiento reutilizable: `.claude/skills/`.
- Lo que necesita un trabajador especializado: `.claude/agents/`.
- Lo que se repite como comando: `.claude/commands/`.
- Lo que conecta herramientas externas: `.mcp.json` o scripts saneados.
- Lo que es memoria de cliente: `clients/[cliente]/`.
- Lo que es historico: `legacy/` o archivo externo.

La migracion se hara por capas, con pruebas, no por impulso.

## Principios de la migracion

1. No se migra una carpeta; se migra una responsabilidad.
2. Claude Code es la norma arquitectonica; el sistema antiguo es materia prima.
3. Nada entra al v2 sin proposito, propietario y criterio de calidad.
4. Nada con secretos entra al repo.
5. Las instrucciones largas no van a `CLAUDE.md`; se convierten en rules, skills o subagents.
6. La memoria de cliente nunca se convierte en skill.
7. Los scripts que puedan tocar produccion deben tener dry-run y aprobacion.
8. Todo cambio estructural deja registro.
9. La calidad se prueba; no se presupone.
10. Cada fase debe poder explicarse en lenguaje humano.

## Definicion de sistema correcto

El sistema v2 estara bien cuando:

- Claude sepa que leer segun el tipo de tarea.
- Los agentes no compitan ni se contradigan.
- Las skills sean procedimientos claros y reutilizables.
- Los subagents tengan contexto propio, herramientas acotadas y criterios de salida.
- Los hooks bloqueen acciones peligrosas antes de que ocurran.
- Los comandos permitan repetir workflows sin improvisar.
- Los conectores esten separados de los secretos.
- Los clientes tengan memoria clara, historico y outputs trazables.
- Los resultados tengan criterios de calidad visibles.
- Rodrigo pueda entender que se hizo y por que.

## Fuentes oficiales Claude Code usadas como norma

- `CLAUDE.md` y memoria de proyecto: instrucciones persistentes, concisas y organizadas.
- `.claude/rules/`: reglas modulares para evitar meter todo en contexto global.
- `.claude/skills/<skill>/SKILL.md`: procedimientos bajo demanda con frontmatter y archivos de apoyo.
- `.claude/agents/*.md`: subagents con frontmatter YAML, descripcion clara, herramientas y modelo.
- `.claude/settings.json`: configuracion compartida, permisos y hooks de proyecto.
- `.claude/commands/`: comandos reutilizables para flujos repetibles.
- Hooks: validacion y seguridad en `PreToolUse`, `PostToolUse`, `Stop` y eventos relacionados.
- MCP: herramientas externas compartidas sin secretos en repo.

## Estructura de trabajo

Cada pieza legacy pasara por este embudo:

```text
Inventariar -> Clasificar -> Sanear -> Migrar -> Probar -> Registrar -> Activar
```

Cada fase tiene:

- Objetivo.
- Por que existe.
- Acciones.
- Entregables.
- Criterios de salida.
- Riesgos.

## Fase 0 - Preparacion y seguridad

### Objetivo

Evitar que la migracion arrastre secretos, archivos privados, scripts peligrosos o outputs sensibles.

### Por que importa

Un repo cloud mal preparado puede filtrar claves, datos de clientes o herramientas que modifican produccion.

### Acciones

1. Confirmar que GitHub es privado.
2. Confirmar `.gitignore` de secretos y outputs pesados.
3. Revisar si existe `.env`, tokens, credentials, application passwords o claves en el sistema antiguo.
4. Registrar accesos detectados sin valores reales.
5. Separar scripts en tres categorias:
   - solo lectura
   - escritura local
   - acciones externas sensibles
6. Marcar scripts historicos WordPress/WooCommerce con credenciales embebidas como bloqueados hasta saneamiento.
7. Definir politica de ramas:
   - `main`: estable
   - `migration/*`: trabajos de migracion
   - `audit/*`: auditorias sin cambios operativos
8. Confirmar que no se suben outputs privados ni exports grandes.

### Entregables

- `.gitignore` blindado.
- `registries/registro-accesos.md` actualizado.
- `registries/registro-artefactos.md` actualizado.
- Lista de scripts bloqueados o pendientes de saneamiento.

### Criterio de salida

Se puede trabajar en v2 sin riesgo razonable de subir secretos o activar produccion por accidente.

## Fase 1 - Inventario inteligente del sistema antiguo

### Objetivo

Saber que existe, para que sirve, que se queda, que se reescribe y que se archiva.

### Por que importa

Sin inventario se migra por sensacion. Eso reproduce el mismo desorden en otro repo.

### Acciones

1. Inventariar carpetas:
   - `AGENTS.md`
   - `CLAUDE.md`
   - `.agents/skills/`
   - `agents/`
   - `agency/`
   - `clients/`
   - `scripts/`
   - `sistema/`
   - `outputs/`
2. Para cada archivo relevante registrar:
   - ruta
   - tipo
   - responsabilidad
   - propietario
   - estado
   - riesgo
   - duplicados
   - destino probable en Claude Code
3. Separar material en categorias:
   - regla viva
   - procedimiento
   - agente
   - memoria
   - protocolo
   - script
   - registro
   - historico
   - obsoleto
4. Detectar duplicidades:
   - instrucciones repetidas
   - criterios conflictivos
   - skills que solapan con agentes
   - protocolos duplicados
   - outputs que se tratan como fuente viva
5. Crear backlog de migracion por prioridad.

### Entregables

- `planning/inventario-legacy.md`
- `planning/backlog-migracion.md`
- `registries/registro-migracion.md` con primeras decisiones.

### Criterio de salida

Toda pieza importante tiene una clasificacion y un destino probable.

## Fase 2 - Mapa de responsabilidades Claude Code

### Objetivo

Decidir donde debe vivir cada tipo de conocimiento dentro del sistema v2.

### Por que importa

La calidad baja cuando se mete todo en un prompt gigante o cuando un agente no sabe que fuente debe obedecer.

### Acciones

1. Definir matriz final:
   - `CLAUDE.md`: solo reglas siempre activas.
   - `AGENTS.md`: instrucciones generales compatibles con otros agentes.
   - `.claude/rules/`: reglas por dominio.
   - `.claude/skills/`: procedimientos ejecutables bajo demanda.
   - `.claude/agents/`: trabajadores especializados.
   - `.claude/commands/`: loops o acciones repetibles.
   - `protocols/`: normas operativas humanas y de sistema.
   - `registries/`: trazabilidad.
   - `clients/`: memoria real de cliente.
   - `agency/`: memoria interna.
   - `legacy/`: decisiones historicas o material no activo.
2. Crear ejemplos canonicos para cada destino.
3. Definir que nunca debe ir en cada lugar.
4. Documentar reglas de decision para futuras migraciones.

### Entregables

- `.claude/rules/migracion-claude-code.md`
- `protocols/migracion-claude-code.md`
- `planning/mapa-responsabilidades.md`

### Criterio de salida

Ante cualquier archivo legacy, el sistema puede decidir su destino correcto sin improvisar.

## Fase 3 - Limpieza de instrucciones globales

### Objetivo

Convertir las instrucciones globales en un nucleo pequeno, claro y obedecible.

### Por que importa

Claude Code advierte que instrucciones largas consumen contexto y reducen adherencia. Si todo esta siempre activo, nada pesa de verdad.

### Acciones

1. Revisar `AGENTS.md` legacy.
2. Extraer solo reglas siempre activas.
3. Crear o ajustar `CLAUDE.md` v2 con importacion a `@AGENTS.md`.
4. Mover instrucciones largas a:
   - rules
   - skills
   - protocols
   - commands
5. Eliminar contradicciones.
6. Crear checklist de adherencia.

### Entregables

- `CLAUDE.md`
- `AGENTS.md`
- `.claude/rules/core.md`
- `planning/auditoria-instrucciones-globales.md`

### Criterio de salida

Un agente nuevo puede iniciar en v2 sin leer un manual gigante y aun asi actuar correctamente.

## Fase 4 - Protocolos criticos

### Objetivo

Migrar primero los protocolos que evitan dano: secretos, activos criticos, artefactos y cierre.

### Por que importa

Antes de automatizar calidad, hay que blindar seguridad.

### Acciones

1. Auditar protocolos legacy:
   - activos criticos
   - control de artefactos
   - gestion de secretos
   - El Escolta
   - El Fenix
   - cierre humano
   - El Arquitecto
   - El Docente
2. Detectar duplicados entre `agency/protocolos/` y `sistema/protocolos/`.
3. Elegir fuente canonica.
4. Reescribir protocolos en v2 con:
   - objetivo
   - cuando se activa
   - pasos
   - salida esperada
   - bloqueo
   - registro
5. Definir que parte sera regla y que parte sera hook.

### Entregables

- `protocols/activos-criticos.md`
- `protocols/control-artefactos.md`
- `protocols/gestion-secretos.md`
- `protocols/cierre-humano.md`
- `protocols/el-escolta.md`
- `protocols/el-fenix.md`
- reglas relacionadas en `.claude/rules/`

### Criterio de salida

El sistema sabe cuando debe parar, pedir aprobacion, registrar o bloquear.

## Fase 5 - Hooks de seguridad y cierre

### Objetivo

Convertir reglas criticas en controles automaticos.

### Por que importa

Las reglas importantes no deben depender de que el agente se acuerde. Claude Code permite hooks para interceptar acciones.

### Acciones

1. Disenar hooks iniciales:
   - bloquear lectura de `.env`
   - bloquear escritura de secretos
   - alertar si se editan scripts sensibles
   - exigir registro si se crean/modifican outputs
   - ejecutar guard antes de cierre
2. Implementar hooks como scripts pequeños.
3. Conectarlos en `.claude/settings.json`.
4. Probar con casos controlados.
5. Documentar como se desbloquea un falso positivo.

### Entregables

- `.claude/hooks/block-secrets.*`
- `.claude/hooks/check-artifacts.*`
- `.claude/hooks/check-critical-assets.*`
- `.claude/hooks/closing-guard.*`
- `.claude/settings.json` actualizado.

### Criterio de salida

El sistema bloquea o avisa antes de acciones peligrosas basicas.

## Fase 6 - Skills operativas

### Objetivo

Convertir procedimientos repetibles en skills limpias.

### Por que importa

Una skill se carga bajo demanda. Eso reduce contexto y mejora precision.

### Acciones

1. Auditar `.agents/skills/` legacy.
2. Clasificar skills:
   - migrar tal cual
   - reescribir
   - fusionar
   - archivar
3. Para cada skill:
   - crear `SKILL.md`
   - definir `description`
   - limitar herramientas si aplica
   - mover referencias largas a archivos de apoyo
   - agregar ejemplos si el output es subjetivo
   - agregar scripts de validacion si aplica
4. Priorizar skills:
   - `client-audit`
   - `folder-cleanup`
   - `seo-audit`
   - `site-architecture`
   - `analytics-tracking`
   - `copywriting`
   - `humanizalo`
   - `woocommerce-setup`
5. Probar cada skill con una tarea real o simulada.

### Entregables

- `.claude/skills/[skill]/SKILL.md`
- referencias en subcarpetas
- ejemplos de salida
- registros de migracion

### Criterio de salida

Cada skill tiene activador claro, procedimiento conciso y prueba de calidad.

## Fase 7 - Subagents nativos

### Objetivo

Convertir lideres y especialistas en subagents cuando realmente necesiten contexto propio.

### Por que importa

Los subagents preservan contexto, acotan herramientas y especializan criterio. Pero crear demasiados subagents sin necesidad vuelve el sistema complejo.

### Acciones

1. Auditar `agents/` legacy.
2. Separar:
   - lideres
   - especialistas
   - docentes
   - entidades de sistema
   - referencias
3. Decidir cuales son subagents reales:
   - Lider Clientes
   - Lider Agencia
   - Arquitecto Migracion
   - Docente
   - Fenix
   - SEO, CRO, SEM, Social, Reports, Web solo si requieren contexto aislado
4. Crear cada subagent con:
   - `name`
   - `description`
   - `tools`
   - `model`
   - `permissionMode`
   - `maxTurns`
   - `skills`
   - cuerpo markdown claro
5. Evitar que subagents hereden herramientas innecesarias.
6. Crear pruebas de delegacion.

### Entregables

- `.claude/agents/leader-clientes.md`
- `.claude/agents/leader-agencia.md`
- `.claude/agents/docente.md`
- `.claude/agents/fenix.md`
- especialistas por prioridad

### Criterio de salida

Cada subagent hace una cosa mejor que el hilo principal y devuelve una salida clara.

## Fase 8 - Comandos y loops

### Objetivo

Convertir acciones repetibles en comandos o automatizaciones.

### Por que importa

Los loops antiguos son utiles, pero deben separarse entre comandos manuales, scheduled tasks y workflows automatizados.

### Acciones

1. Auditar loops legacy:
   - auditoria semanal
   - informe mensual
   - alertas pendientes
   - meta ads semanal
   - arquitecto diario
   - arquitecto semanal
2. Clasificar cada loop:
   - comando manual
   - scheduled task
   - automation externa
   - no migrar
3. Crear commands:
   - `.claude/commands/auditoria-semanal.md`
   - `.claude/commands/informe-mensual.md`
   - `.claude/commands/alertas-pendientes.md`
4. Definir inputs, outputs y registros.
5. Probar sin tocar produccion.

### Entregables

- comandos en `.claude/commands/`
- registro de ejecuciones
- checklist de salida

### Criterio de salida

Rodrigo puede pedir un flujo por nombre y el sistema sabe que hacer, que leer y que entregar.

## Fase 9 - MCP, conectores y scripts

### Objetivo

Ordenar herramientas externas y scripts sin mezclar secretos ni acciones peligrosas.

### Por que importa

Los conectores dan datos vivos. Pero mal gobernados pueden modificar produccion o filtrar accesos.

### Acciones

1. Auditar scripts:
   - Notion
   - Drive
   - GA4
   - GSC
   - GBP
   - Meta Ads
   - WooCommerce
   - WordPress
   - Kling
2. Clasificar:
   - lectura segura
   - escritura local
   - produccion sensible
3. Crear normas:
   - no interactivo
   - dry-run por defecto
   - logs sin secretos
   - outputs registrados
   - errores comprensibles
4. Definir que va por MCP y que va por script.
5. Crear `.mcp.example.json` si procede.
6. No crear `.mcp.json` real con secretos.

### Entregables

- `scripts/README.md` ampliado
- `scripts/[conector].py` saneados
- `.mcp.example.json`
- `registries/registro-accesos.md`

### Criterio de salida

El sistema sabe obtener datos vivos sin comprometer secretos ni alterar activos reales sin permiso.

## Fase 10 - Migracion de clientes

### Objetivo

Migrar memoria y estructura de clientes sin perder historico ni mezclar datos.

### Por que importa

La memoria de cliente es una de las partes mas valiosas del sistema antiguo.

### Acciones

1. Revisar plantilla v2 de cliente.
2. Para cada cliente activo:
   - auditar `context.md`
   - auditar `memory.md`
   - auditar `log.md`
   - auditar `mensajes.md`
   - auditar `tasks.md`
   - auditar `outputs/manifest.md`
3. Separar:
   - informacion vigente
   - historico
   - tareas abiertas
   - mensajes pendientes
   - datos obsoletos
4. Crear cliente piloto.
5. Probar una tarea real con el nuevo flujo.
6. Solo despues migrar el resto.

### Entregables

- `clients/[cliente]/` en v2
- manifests actualizados
- registro de migracion por cliente

### Criterio de salida

El nuevo flujo puede trabajar con un cliente sin repetir trabajo viejo ni perder memoria.

## Fase 11 - Migracion de agencia

### Objetivo

Migrar el trabajo interno de E-SELEC como negocio.

### Por que importa

El sistema no solo trabaja para clientes; tambien debe ayudar a captar, vender, organizar y mejorar E-SELEC.

### Acciones

1. Migrar `agency/context.md`.
2. Migrar `agency/brand.md`.
3. Migrar `agency/preferencias-rodrigo.md` como regla o memoria local segun sensibilidad.
4. Migrar `agency/log.md`.
5. Migrar `agency/mensajes.md`.
6. Separar outputs de estrategia, captacion y propuestas.
7. Crear commands internos si procede.

### Entregables

- `agency/context.md`
- `agency/brand.md`
- `agency/log.md`
- `agency/mensajes.md`
- comandos de captacion o reporting interno

### Criterio de salida

El modo agencia funciona en v2 sin depender del legacy.

## Fase 12 - Docente, Arquitecto y Fenix

### Objetivo

Convertir las entidades estructurales en un sistema de aprendizaje y mejora continua.

### Por que importa

Tu problema de calidad no se arregla solo con prompts. Se arregla haciendo que el sistema aprenda de errores, aprobaciones y correcciones.

### Acciones

1. Definir Arquitecto:
   - observa estructura
   - detecta fallos de proceso
   - propone cambios
2. Definir Docente:
   - convierte fuentes y correcciones en criterio
   - crea evaluaciones
   - evita duplicar conocimiento
3. Definir Fenix:
   - conecta piezas cuando cambia la estructura
   - evita cabos sueltos
4. Crear subagents o rules segun corresponda.
5. Crear ciclo de aprendizaje:
   - correccion de Rodrigo
   - diagnostico
   - actualizacion de skill/rule
   - prueba
   - registro

### Entregables

- `.claude/agents/docente.md`
- `.claude/agents/fenix.md`
- `.claude/agents/arquitecto.md`
- `registries/registro-aprendizajes.md`

### Criterio de salida

Cuando Rodrigo corrija algo, el sistema sabe donde convertirlo en mejora permanente.

## Fase 13 - Sistema de calidad y evaluaciones

### Objetivo

Crear pruebas para evitar outputs mediocres.

### Por que importa

La calidad no puede depender de "esta vez el modelo estuvo inspirado".

### Acciones

1. Definir criterios por tipo de output:
   - auditoria SEO
   - informe mensual
   - copy
   - estrategia
   - captacion
   - web/CRO
   - contenido social
2. Crear ejemplos buenos y malos.
3. Crear checklists de evaluacion.
4. Crear matriz de causas de baja calidad:
   - falta contexto
   - contexto contradictorio
   - datos incompletos
   - skill incorrecta
   - agente incorrecto
   - modelo insuficiente
   - output sin ejemplo
   - fuente de verdad equivocada
5. Crear protocolo de correccion.

### Entregables

- `quality/criterios-output.md`
- `quality/evaluaciones/`
- `quality/ejemplos/`
- `protocols/correccion-calidad.md`

### Criterio de salida

Cada entregable importante puede evaluarse con criterios visibles.

## Fase 14 - Piloto controlado

### Objetivo

Probar el sistema v2 con una tarea real antes de migrar todo.

### Por que importa

Un sistema puede parecer ordenado y fallar en ejecucion real.

### Acciones

1. Elegir un cliente piloto o una tarea de agencia.
2. Ejecutar una tarea real completa.
3. Comparar output v2 contra output legacy.
4. Medir:
   - calidad
   - criterio
   - contexto usado
   - tiempo
   - errores
   - trazabilidad
5. Corregir estructura.

### Entregables

- `planning/piloto-01.md`
- output generado
- evaluacion de calidad
- cambios estructurales derivados

### Criterio de salida

El piloto demuestra que v2 produce igual o mejor calidad con menos friccion.

## Fase 15 - Migracion progresiva

### Objetivo

Migrar el resto del sistema por prioridad y con control.

### Orden recomendado

1. Protocolos criticos.
2. Fuentes de verdad.
3. Agencia core.
4. Cliente piloto.
5. Skills de mayor uso.
6. Lider Clientes.
7. Lider Agencia.
8. SEO.
9. Reports.
10. Web.
11. CRO.
12. SEM.
13. Social.
14. Loops.
15. Scripts sensibles.
16. Resto de clientes.
17. Historico y archivo.

### Criterio de salida

El sistema legacy deja de ser operativo principal y queda como referencia historica.

## Fase 16 - Operacion continua

### Objetivo

Mantener el sistema limpio despues de migrar.

### Acciones

1. Revision semanal de registros.
2. Revision mensual de skills.
3. Revision mensual de agentes.
4. Revision de hooks tras falsos positivos.
5. Revision de outputs mediocres.
6. Limpieza de legacy.
7. Backups y tags de version.

### Entregables

- `CHANGELOG.md`
- tags de GitHub
- `registries/registro-aprendizajes.md`
- reportes de calidad

### Criterio de salida

El sistema no vuelve a desordenarse con el tiempo.

## Primer bloque de trabajo recomendado

No empezaria migrando agentes. Empezaria asi:

1. Crear `planning/inventario-legacy.md`.
2. Crear `planning/backlog-migracion.md`.
3. Auditar protocolos criticos legacy.
4. Migrar `gestion-secretos`.
5. Migrar `control-artefactos`.
6. Migrar `activos-criticos`.
7. Migrar `cierre-humano`.
8. Crear hooks minimos de bloqueo de secretos.
9. Probar una tarea sencilla de agencia.
10. Elegir cliente piloto.

Decision tomada: empezar por seguridad/protocolos. Al cerrar P0 se abre P1 calidad/criterio para atacar directamente el problema de outputs pobres.

## Preguntas no bloqueantes para Rodrigo

Estas preguntas no impiden empezar, pero ayudan a ordenar prioridades:

1. Que prefieres como cliente piloto: `computer-chamberi`, `cashier-bubble-tea`, `la-bottega-del-gusto` o `stramondo-venezuela`?
2. Prefieres empezar por seguridad/protocolos o por mejorar calidad de outputs SEO?
3. Quieres que GitHub sea solo backup privado o tambien tablero operativo con issues?

## Como usaremos este plan

Cada sesion debe terminar actualizando:

- `planning/backlog-migracion.md`
- `registries/registro-migracion.md`
- `registries/registro-artefactos.md`
- `agency/log.md` del sistema legacy mientras la transicion siga viva

No se da una fase por terminada hasta que su criterio de salida este cumplido.
