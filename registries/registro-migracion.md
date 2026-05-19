# Registro de migracion

Este registro documenta decisiones de migracion desde el sistema legacy E-SELEC al sistema v2.

## Formato

```text
### YYYY-MM-DD - pieza legacy
- Responsable:
- Tipo:
- Responsabilidad real:
- Destino Claude Code:
- Decision: conservar | fusionar | reescribir | archivar | no migrar
- Motivo:
- Riesgo:
- Prueba de calidad:
- Estado:
- Commit:
```

## Entradas

### 2026-05-12 - rol arquitecto-migracion-claude
- Responsable: Codex + Arquitecto
- Tipo: subagent / protocolo / skill / command
- Responsabilidad real: crear el rol que gobernara la migracion del sistema legacy al sistema v2 siguiendo Claude Code.
- Destino Claude Code: `.claude/agents/`, `.claude/rules/`, `.claude/skills/`, `.claude/commands/`, `protocols/`
- Decision: conservar
- Motivo: el sistema necesita una autoridad de migracion que evite copiar desorden y diagnostique problemas de calidad como fallos de arquitectura, no solo como fallos del modelo.
- Riesgo: bajo; no migra datos de clientes ni secretos.
- Prueba de calidad: existe mapa de decision, formato de dictamen, checklist de calidad y registro obligatorio.
- Estado: implementado
- Commit: este mismo cambio; consultar `git log --oneline` para el hash final.

### 2026-05-12 - decision de prioridad P0 seguridad/protocolos
- Responsable: Codex + Arquitecto
- Tipo: decision de migracion
- Responsabilidad real: ordenar la primera fase de trabajo despues del plan maestro.
- Destino Claude Code: `planning/backlog-migracion.md`, `planning/sprint-00-seguridad-protocolos.md`
- Decision: conservar
- Motivo: antes de mejorar outputs SEO/informes hay que blindar secretos, artefactos, activos criticos y cierre para no migrar riesgos al sistema v2.
- Riesgo: bajo; decision organizativa sin datos privados.
- Prueba de calidad: P0 tiene sprint propio, criterios de salida y backlog marcado.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-001 inventario legacy inicial
- Responsable: Codex + Arquitecto
- Tipo: inventario de migracion
- Responsabilidad real: mapear el sistema legacy por areas, responsabilidades, riesgos y destino Claude Code probable antes de migrar piezas.
- Destino Claude Code: `planning/inventario-legacy.md`
- Decision: conservar
- Motivo: evita migrar por carpetas completas y crea base para P0-002 y protocolos criticos.
- Riesgo: bajo; no contiene secretos ni valores de credenciales.
- Prueba de calidad: incluye resumen cuantitativo, mapa de destinos Claude Code, clasificacion por carpetas, riesgos y siguiente accion.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-002 auditoria scripts con secretos historicos
- Responsable: Codex + Arquitecto
- Tipo: auditoria de seguridad
- Responsabilidad real: detectar scripts legacy que no deben migrarse al v2 sin saneamiento por credenciales hardcodeadas, OAuth, tokens, `.env`, servicios externos o produccion.
- Destino Claude Code: `planning/auditoria-scripts-sensibles.md`, `registries/registro-accesos.md`
- Decision: conservar
- Motivo: bloquea la migracion insegura de scripts y prepara P0-003 gestion-secretos.
- Riesgo: bajo; no contiene valores de secretos.
- Prueba de calidad: clasifica scripts bloqueados, alto riesgo, revisables y bajo riesgo; define acciones antes de migrar.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-003 protocolo gestion-secretos
- Responsable: Codex + Arquitecto
- Tipo: protocolo de seguridad
- Responsabilidad real: definir como se clasifican, registran, bloquean y rotan secretos/accesos en el sistema v2.
- Destino Claude Code: `protocols/gestion-accesos.md`, `.claude/rules/gestion-accesos.md`
- Decision: reescribir
- Motivo: adaptar el protocolo canonico legacy a la estructura Claude Code y a los hallazgos P0-002.
- Riesgo: bajo; no contiene valores de secretos.
- Prueba de calidad: incluye clasificacion S1-S4, ubicaciones permitidas, flujo operativo, politica para scripts, MCP y requisitos para hook P0-007.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-004 protocolo control-artefactos
- Responsable: Codex + Arquitecto
- Tipo: protocolo de trazabilidad
- Responsabilidad real: definir como se crean, ubican, registran y cierran artefactos en el sistema v2.
- Destino Claude Code: `protocols/control-artefactos.md`, `.claude/rules/control-artefactos.md`
- Decision: reescribir
- Motivo: adaptar el protocolo canonico legacy a la estructura v2, GitHub, `.claude/`, manifests, outputs ignorados y registros.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: incluye definicion de artefacto, registros, campos obligatorios, politica de repo, prohibiciones, cierre y checklist antes de commit.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-005 protocolo activos-criticos
- Responsable: Codex + Arquitecto
- Tipo: protocolo de seguridad operacional
- Responsabilidad real: definir como clasificar y aprobar acciones que puedan afectar produccion, datos, fuentes de verdad, integraciones o accesos.
- Destino Claude Code: `protocols/activos-criticos.md`, `.claude/rules/activos-criticos.md`
- Decision: reescribir
- Motivo: adaptar el protocolo canonico legacy a la estructura v2, Claude Code, scripts, MCP, subagents y fuentes de verdad.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: incluye niveles A/B/C/D, Orden corta/completa, diagnostico por capas, anti-restore, fuentes de verdad, condiciones de parada y checklist.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-006 protocolo cierre-humano
- Responsable: Codex + Arquitecto
- Tipo: protocolo de cierre / comunicacion operativa
- Responsabilidad real: definir como explicar a Rodrigo, al cierre de cada tarea, que se pidio, que se hizo, que cambio, que no se toco, que se encontro, estado y siguiente paso.
- Destino Claude Code: `protocols/cierre-humano.md`, `.claude/rules/cierre-humano.md`
- Decision: reescribir
- Motivo: adaptar el protocolo canonico legacy a la estructura v2 y al flujo de migracion con backlog, commits, registros y El Escolta.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: incluye cierre normal, cierre corto, checklist de migracion, tono obligatorio, relacion con Claude Code, El Escolta y otros protocolos.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P0-007 hook bloqueo de datos sensibles
- Responsable: Codex + Arquitecto
- Tipo: hook de seguridad
- Responsabilidad real: bloquear antes de ejecutar una herramienta los intentos de escribir, mover, versionar o introducir datos sensibles en archivos o comandos.
- Destino Claude Code: `.claude/hooks/block-sensitive-data.py`, `.claude/settings.json`
- Decision: conservar con adaptacion
- Motivo: Claude Code permite hooks `PreToolUse` con decision `deny`; este control convierte el protocolo de accesos sensibles en una barrera automatica.
- Riesgo: bajo; no contiene secretos reales y solo usa patrones defensivos.
- Prueba de calidad: autoprueba del hook, JSON valido de settings, busqueda defensiva de patrones sensibles y `git diff --check`.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P1-001 diagnostico de calidad de outputs
- Responsable: Codex + Arquitecto
- Tipo: diagnostico de calidad / matriz de causas raiz
- Responsabilidad real: explicar por que los outputs pueden salir flojos aunque el legacy tenga criterios y agentes, y definir decisiones de migracion para corregirlo.
- Destino Claude Code: `quality/diagnostico-calidad.md`, `quality/README.md`
- Decision: crear
- Motivo: antes de migrar skills o agentes de SEO/informes, el sistema necesita saber que problema de calidad esta corrigiendo.
- Riesgo: bajo; documento de arquitectura sin secretos ni datos privados.
- Prueba de calidad: cruza documentacion Claude Code, estructura legacy, matriz de causas, diagnostico por area y acciones P1.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P1-002 criterios de output por servicio
- Responsable: Codex + Arquitecto
- Tipo: criterios de calidad / contratos de salida
- Responsabilidad real: definir que debe cumplir cada tipo de entregable para considerarse bueno, parcial o bloqueado.
- Destino Claude Code: `quality/criterios-output.md`
- Decision: crear
- Motivo: corregir la causa Q-002 y Q-003 del diagnostico de calidad: criterio sin contrato y verificacion insuficiente.
- Riesgo: bajo; documento operativo sin secretos ni datos privados.
- Prueba de calidad: incluye criterios universales, escala 0-4, contratos por servicio, bloqueos y checklist final.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P1-003 skill client-audit
- Responsable: Codex + Arquitecto
- Tipo: skill operativa Claude Code
- Responsabilidad real: auditar un cliente existente o nuevo, reconstruir estado real y definir una proxima prioridad verificable.
- Destino Claude Code: `.claude/skills/client-audit/`
- Decision: reescribir
- Motivo: adaptar la skill legacy a Claude Code con instrucciones compactas, archivos de apoyo, contrato de salida y checklist.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: incluye `SKILL.md`, plantilla de auditoria, checklist de revision, bloqueos y relacion con `quality/criterios-output.md`.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P1-004 skill seo-audit
- Responsable: Codex + Arquitecto
- Tipo: skill operativa Claude Code
- Responsabilidad real: diagnosticar problemas SEO con evidencia, fuentes jerarquizadas y plan priorizado.
- Destino Claude Code: `.claude/skills/seo-audit/`
- Decision: reescribir
- Motivo: adaptar la skill legacy y criterios SEO del sistema a una skill compacta con plantilla y checklist, evitando auditorias genericas.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: incluye nivel de datos SEO, jerarquia GSC/SEMrush/render/contexto, bloqueo por datos faltantes, schema seguro, plantilla y checklist.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P1-005 subagent docente
- Responsable: Codex + Arquitecto
- Tipo: subagent Claude Code / aprendizaje operativo
- Responsabilidad real: convertir correcciones, rechazos y fallos de calidad en criterio operativo con prueba de conducta futura.
- Destino Claude Code: `.claude/agents/docente.md`
- Decision: reescribir
- Motivo: adaptar El Docente legacy a un subagent nativo, read-only, con contexto aislado y formato de capacitacion.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: frontmatter de subagent, tools read-only, workflow observa-diagnostica-formula-ensena-examina y formato de salida.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P2-001 subagent leader-clientes
- Responsable: Codex + Arquitecto
- Tipo: subagent Claude Code / orquestacion de clientes
- Responsabilidad real: leer estado de cliente, priorizar, detectar riesgos y enrutar hacia skills/subagents/commands correctos.
- Destino Claude Code: `.claude/agents/leader-clientes.md`
- Decision: reescribir
- Motivo: sustituir el lider legacy largo por un orquestador ligero que delega procedimientos en skills, reglas y contratos de calidad.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: frontmatter de subagent, tools read-only, lectura obligatoria, modos, priorizacion, routing, bloqueos y formato de salida.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P2-002 subagent leader-agencia
- Responsable: Codex + Arquitecto
- Tipo: subagent Claude Code / orquestacion interna
- Responsabilidad real: coordinar captacion, reputacion, onboarding, retencion, finanzas y operaciones internas de E-SELEC sin mezclarlo con clientes.
- Destino Claude Code: `.claude/agents/leader-agencia.md`
- Decision: reescribir
- Motivo: sustituir el lider legacy repetitivo por un orquestador ligero que aplica protocolos y contratos sin duplicarlos.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: frontmatter de subagent, tools read-only, lectura obligatoria, routing interno, separacion agencia/cliente, bloqueos y formato de salida.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P2-003 command alertas-pendientes
- Responsable: Codex + Arquitecto
- Tipo: command Claude Code / workflow recurrente
- Responsabilidad real: consolidar mensajes pendientes de clientes y agencia, clasificarlos y proponer siguiente accion.
- Destino Claude Code: `.claude/commands/alertas-pendientes.md`
- Decision: reescribir
- Motivo: convertir el loop legacy en command invocable, con modo solo lectura por defecto y escritura opcional controlada.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: define uso, lectura, clasificacion, salida, escritura opcional, no duplicacion y criterio de exito.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P2-004 command auditoria-semanal
- Responsable: Codex + Arquitecto
- Tipo: command Claude Code / workflow recurrente
- Responsabilidad real: revisar avance semanal de clientes, detectar estancamientos, mensajes pendientes, tareas criticas e incidencias de datos.
- Destino Claude Code: `.claude/commands/auditoria-semanal.md`
- Decision: reescribir
- Motivo: convertir el loop legacy en command invocable, con lectura por defecto y escritura opcional para evitar outputs innecesarios.
- Riesgo: bajo; no contiene secretos ni datos privados.
- Prueba de calidad: define uso, lectura, detecciones, clasificacion, salida, escritura opcional y criterio de exito.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P2-005 cliente piloto
- Responsable: Codex + Arquitecto
- Tipo: decision de piloto
- Responsabilidad real: elegir el primer cliente para probar el sistema v2 operativo sin tocar produccion.
- Destino Claude Code: `planning/piloto-01.md`
- Decision: crear
- Motivo: Computer Chamberi permite probar `leader-clientes`, `client-audit`, `seo-audit` y criterios de calidad con menor riesgo que WooCommerce o Ads.
- Riesgo: bajo; documento de planificacion sin secretos ni datos privados sensibles.
- Prueba de calidad: incluye razones de seleccion, descartes, alcance, no-alcance, riesgos y siguiente paso.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P3-002 cliente piloto computer-chamberi
- Responsable: Codex + Arquitecto
- Tipo: migracion minima de cliente
- Responsabilidad real: crear estructura v2 saneada para el cliente piloto sin copiar outputs pesados ni secretos.
- Destino Claude Code: `clients/computer-chamberi/`
- Decision: reescribir/resumir
- Motivo: probar operacion v2 con cliente real y riesgo controlado antes de migrar mas clientes.
- Riesgo: bajo-medio; contiene resumen operativo de cliente, sin secretos ni exports brutos.
- Prueba de calidad: estructura minima creada, mensajes saneados, manifest de outputs historicos, no se copian archivos pesados.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P1-006 verificacion-medicion
- Responsable: Codex + Arquitecto
- Tipo: skill + command Claude Code / calidad de datos
- Responsabilidad real: comprobar fuentes de medicion antes de auditorias, informes o decisiones para evitar outputs con conclusiones prematuras.
- Destino Claude Code: `.claude/skills/verificacion-medicion/` y `.claude/commands/verificar-medicion.md`
- Decision: crear
- Motivo: el piloto de Computer Chamberi mostro que `seo-audit` queda en nivel 2 si no existe una comprobacion previa de GSC/SEMrush/GA4.
- Riesgo: bajo; procedimiento de solo lectura, sin secretos ni produccion.
- Prueba de calidad: skill con nivel de medicion 0-3, plantilla, checklist, command invocable y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - prueba verificacion medicion computer-chamberi
- Responsable: Codex + Arquitecto
- Tipo: prueba de sistema / calidad de datos
- Responsabilidad real: validar que `verificacion-medicion` detecta insuficiencia de fuentes vivas antes de una auditoria SEO final.
- Destino Claude Code: `planning/resultado-verificacion-medicion-01.md`
- Decision: crear resultado de prueba
- Motivo: evitar que el sistema confunda contexto SEO legacy con medicion viva verificada.
- Riesgo: bajo; no contiene secretos ni exports de herramientas.
- Prueba de calidad: clasifica medicion en Nivel 1, declara fuentes revisadas, limites y proxima accion unica.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - evidencia SEO saneada computer-chamberi
- Responsable: Codex + Arquitecto
- Tipo: output cliente v2 / evidencia migrada
- Responsabilidad real: extraer datos minimos utiles desde auditorias legacy recientes para permitir auditoria SEO parcial fuerte sin copiar outputs completos.
- Destino Claude Code: `clients/computer-chamberi/outputs/evidencia-seo-2026-05-12.md`
- Decision: resumir/sanear
- Motivo: subir la medicion SEO de Nivel 1 a Nivel 2 usando evidencia legacy reciente con fuentes declaradas GSC/SEMrush.
- Riesgo: medio si se usa como dato final sin revalidar unidades; bajo como evidencia interna.
- Prueba de calidad: separa SEMrush/GSC, declara contradicciones de unidades, limita conclusiones permitidas y prohibe ejecucion sin Orden de Cambio.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - seo-audit piloto 02 computer-chamberi
- Responsable: Codex + Arquitecto
- Tipo: prueba de skill / auditoria SEO parcial
- Responsabilidad real: comprobar que `seo-audit` produce un diagnostico priorizado, con evidencia y limites claros, sin convertir datos parciales en output final.
- Destino Claude Code: `planning/resultado-seo-audit-piloto-02.md`
- Decision: crear prueba
- Motivo: validar la mejora de calidad despues de anadir `verificacion-medicion` y evidencia SEO saneada.
- Riesgo: bajo-medio; contiene resumen SEO interno, sin secretos ni produccion.
- Prueba de calidad: nivel parcial fuerte, top 3 priorizado, tecnico antes de contenido, schema no sobrediagnosticado y produccion bloqueada.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P1-007 ingesta-evidencia
- Responsable: Codex + Arquitecto
- Tipo: skill + command Claude Code / seguridad de datos
- Responsabilidad real: convertir exports, capturas, datos vivos u outputs legacy en evidencia saneada antes de usarlos en auditorias, informes o GitHub.
- Destino Claude Code: `.claude/skills/ingesta-evidencia/` y `.claude/commands/ingestar-evidencia.md`
- Decision: crear
- Motivo: el piloto demostro que se necesita una forma repetible de subir evidencia de Nivel 2/3 sin copiar dumps ni secretos.
- Riesgo: bajo; procedimiento de saneamiento, sin produccion.
- Prueba de calidad: define niveles E0/E1/E2/E3, plantilla, checklist, command, contrato de output y bloqueo de secretos/PII.
- Estado: implementado
- Commit: pendiente

### 2026-05-12 - P3-001 estructura agencia
- Responsable: Codex + Arquitecto
- Tipo: migracion agencia / memoria operativa
- Responsabilidad real: crear snapshot v2 saneado de identidad, marca, preferencias, loops, mensajes e historial interno de E-SELEC.
- Destino Claude Code: `agency/`
- Decision: resumir/sanear
- Motivo: permitir que `leader-agencia` trabaje con contexto v2 sin depender de archivos legacy largos o con datos innecesarios.
- Riesgo: bajo-medio; contiene memoria interna, sin secretos ni PII innecesaria.
- Prueba de calidad: separa contexto, marca, preferencias, mensajes, loops, historial y manifest; marca pendientes y fuentes legacy.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 analytics-tracking
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / medicion
- Responsabilidad real: auditar o disenar tracking GA4/GTM/eventos/conversiones con criterios de privacidad, decision y validacion.
- Destino Claude Code: `.claude/skills/analytics-tracking/` y `.claude/commands/auditar-tracking.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy prioritaria que desbloquea informes, CRO, Ads y SEO final con medicion confiable.
- Riesgo: bajo-medio; procedimiento puede derivar en produccion, pero queda bloqueado por Orden de Cambio.
- Prueba de calidad: SKILL con niveles T0-T3, referencias compactas, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 site-architecture
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / arquitectura web
- Responsabilidad real: disenar o auditar mapa de paginas, URLs, menus, breadcrumbs, enlazado interno y redirecciones sin tocar produccion.
- Destino Claude Code: `.claude/skills/site-architecture/` y `.claude/commands/plan-arquitectura-web.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy prioritaria para ordenar SEO/Web/CRO antes de cambios en paginas, menus o URLs.
- Riesgo: medio; puede derivar en cambios de produccion y perdida SEO si se ejecuta mal, por eso bloquea implementacion sin Orden de Cambio.
- Prueba de calidad: SKILL con niveles SA0-SA3, patrones compactos, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 schema-markup
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / SEO tecnico
- Responsabilidad real: auditar, disenar o corregir schema JSON-LD basado en contenido visible, validacion y reglas de Google/schema.org.
- Destino Claude Code: `.claude/skills/schema-markup/` y `.claude/commands/auditar-schema.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy y endurecerla para evitar schema generico, duplicado, no validado o basado en contenido inventado.
- Riesgo: medio; puede derivar en cambios de produccion o penalizacion de rich results si se marca contenido falso, por eso bloquea implementacion sin validacion y Orden de Cambio.
- Prueba de calidad: SKILL con niveles SM0-SM3, fuentes oficiales, referencias compactas, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 ai-seo
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / AI search
- Responsabilidad real: auditar visibilidad en respuestas AI y planificar contenido citable con evidencia por query, plataforma y fecha.
- Destino Claude Code: `.claude/skills/ai-seo/` y `.claude/commands/auditar-ai-seo.md`
- Decision: reescribir/adaptar
- Motivo: conservar el enfoque legacy de AI SEO pero eliminar cifras no verificadas, promesas de cita y cambios peligrosos de robots.txt sin Orden de Cambio.
- Riesgo: medio; puede llevar a claims comerciales falsos o cambios de crawling si se ejecuta mal.
- Prueba de calidad: SKILL con niveles AI0-AI3, plantilla, checklist, crawler refs oficiales y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 content-strategy
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / estrategia editorial
- Responsabilidad real: planificar pilares, clusters, temas y calendario editorial priorizado por negocio, SEO, AI SEO y recursos.
- Destino Claude Code: `.claude/skills/content-strategy/` y `.claude/commands/plan-contenido.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy como puente entre auditorias SEO/AI y produccion de contenido accionable.
- Riesgo: bajo-medio; puede producir calendarios genericos si no exige objetivo, audiencia y evidencia.
- Prueba de calidad: SKILL con niveles CS0-CS3, matriz de priorizacion, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 copywriting
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / copy comercial
- Responsabilidad real: escribir o mejorar copy para web, landing, servicios, hero, CTA y value proposition con claims verificables.
- Destino Claude Code: `.claude/skills/copywriting/` y `.claude/commands/escribir-copy.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy endureciendo criterios de prueba, tono, accion primaria y no invencion de claims.
- Riesgo: bajo-medio; puede producir textos genericos o claims riesgosos si no lee contexto y pruebas.
- Prueba de calidad: SKILL con niveles CW0-CW3, frameworks, reglas de estilo, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 copy-editing
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / revision de copy
- Responsabilidad real: revisar y pulir copy existente mediante pasadas de claridad, tono, beneficio, prueba, especificidad, emocion y CTA.
- Destino Claude Code: `.claude/skills/copy-editing/` y `.claude/commands/revisar-copy.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy como filtro de calidad posterior a copywriting y entregables comerciales.
- Riesgo: bajo-medio; puede cambiar demasiado el mensaje o mantener claims falsos si no exige fuente.
- Prueba de calidad: SKILL con niveles CE0-CE3, pasadas de edicion, lenguaje claro, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 page-cro
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / CRO de pagina
- Responsabilidad real: diagnosticar conversion de paginas completas: propuesta de valor, CTA, jerarquia, confianza, objeciones, friccion, mobile y medicion.
- Destino Claude Code: `.claude/skills/page-cro/` y `.claude/commands/auditar-cro-pagina.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy como evaluador de conversion integral, conectado a analytics, copy, arquitectura y formularios.
- Riesgo: medio; puede derivar en cambios de produccion o tests mal planteados si no hay medicion.
- Prueba de calidad: SKILL con niveles PC0-PC3, checklist de pagina, experimentos, plantilla, command y contrato actualizado.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 form-cro
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / CRO de formulario
- Responsabilidad real: diagnosticar friccion de formularios, campos, labels, errores, privacidad, mobile, confianza y medicion.
- Destino Claude Code: `.claude/skills/form-cro/` y `.claude/commands/auditar-formulario.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy como evaluador especializado de formularios, separando cambios accionables de tests y bloqueando produccion sin Orden de Cambio.
- Riesgo: medio; puede derivar en cambios de CRM, formularios, tracking o captacion de PII si no se controla.
- Prueba de calidad: SKILL con niveles FC0-FC3, patrones de formulario, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 ab-test-setup
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / experimentacion CRO
- Responsabilidad real: convertir hipotesis CRO en planes de test con metrica primaria, muestra, duracion, guardrails, QA y criterio de decision.
- Destino Claude Code: `.claude/skills/ab-test-setup/` y `.claude/commands/plan-ab-test.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy evitando experimentos por intuicion, falsos ganadores y tests inviables por falta de trafico o tracking.
- Riesgo: medio; puede llevar a decisiones falsas si no exige baseline, muestra y tracking verificado.
- Prueba de calidad: SKILL con niveles AB0-AB3, referencia de muestra, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 signup-flow-cro
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / CRO de registro
- Responsabilidad real: auditar registros, altas de cuenta y trials: pasos, campos, autenticacion, SSO, recuperacion de cuenta, verificacion, mobile, medicion y handoff a activacion.
- Destino Claude Code: `.claude/skills/signup-flow-cro/` y `.claude/commands/auditar-signup-flow.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy separando signup de formularios generales y de onboarding, para evitar mejoras de alta que degraden activacion posterior.
- Riesgo: medio; puede afectar auth, pagos, email, CRM o producto si se ejecuta sin aprobacion.
- Prueba de calidad: SKILL con niveles SF0-SF3, patrones de signup, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 onboarding-cro
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / CRO de activacion
- Responsabilidad real: auditar onboarding post-signup, activacion, primer valor, empty states, checklists, ayudas, usuarios atascados, medicion y retencion temprana.
- Destino Claude Code: `.claude/skills/onboarding-cro/` y `.claude/commands/auditar-onboarding.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy con criterio de activacion medible y separarla de signup, emails y retencion general.
- Riesgo: medio; puede afectar producto, emails, tracking o datos de usuario si se ejecuta sin Orden de Cambio.
- Prueba de calidad: SKILL con niveles OB0-OB3, patrones de onboarding, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 popup-cro
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / CRO de popup
- Responsabilidad real: auditar popups, modals, overlays, slide-ins y banners: objetivo, oferta, trigger, frecuencia, cierre, mobile, privacidad, accesibilidad, SEO y medicion.
- Destino Claude Code: `.claude/skills/popup-cro/` y `.claude/commands/auditar-popup.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy controlando el riesgo de interrumpir, molestar, afectar SEO movil o capturar datos sin consentimiento.
- Riesgo: medio; puede afectar UX, SEO, privacidad, scripts y conversiones si se ejecuta sin Orden de Cambio.
- Prueba de calidad: SKILL con niveles PU0-PU3, patrones de popup, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 paywall-upgrade-cro
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / CRO de monetizacion in-product
- Responsabilidad real: auditar paywalls, upgrade screens, upsell modals, feature gates, trial expiration y usage limits con guardrails de revenue, confianza y churn.
- Destino Claude Code: `.claude/skills/paywall-upgrade-cro/` y `.claude/commands/auditar-paywall.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy separandola de pricing publico y evitando dark patterns, falsas decisiones de revenue y cambios sensibles de billing.
- Riesgo: medio-alto; puede afectar pricing, checkout, billing, producto, revenue o confianza si se ejecuta sin Orden de Cambio.
- Prueba de calidad: SKILL con niveles PW0-PW3, patrones de paywall, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 paid-ads
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / SEM y paid media
- Responsabilidad real: planificar o auditar campanas pagadas con objetivo, conversion, tracking, presupuesto, plataforma, estructura, audiencias, exclusiones, aprendizaje y riesgos.
- Destino Claude Code: `.claude/skills/paid-ads/` y `.claude/commands/plan-paid-ads.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy separando estrategia de campana de generacion creativa y bloqueando cambios reales de cuentas Ads sin Orden de Cambio.
- Riesgo: alto; puede afectar gasto, conversiones, pixels, billing y cuentas publicitarias si se ejecuta sin aprobacion.
- Prueba de calidad: SKILL con niveles PA0-PA3, guia de plataforma, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 ad-creative
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / creatividad publicitaria
- Responsabilidad real: generar, revisar e iterar headlines, descriptions, primary text, hooks y variaciones de anuncios con limites por plataforma y claims verificables.
- Destino Claude Code: `.claude/skills/ad-creative/` y `.claude/commands/generar-ad-creative.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy para producir creatividad escalable sin mezclarla con estrategia, presupuesto o publicacion en Ads.
- Riesgo: medio; puede crear claims falsos, piezas fuera de politica o anuncios no subibles si no valida plataforma y fuentes.
- Prueba de calidad: SKILL con niveles AC0-AC3, specs de plataforma, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 social-content
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / contenido social
- Responsabilidad real: crear piezas, calendarios y repurposing social por canal, audiencia, tono, objetivo, CTA y medicion.
- Destino Claude Code: `.claude/skills/social-content/` y `.claude/commands/crear-social-content.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy separando distribucion social de estrategia editorial amplia y bloqueando publicacion sin aprobacion.
- Riesgo: medio; puede publicar claims, tono incorrecto o contenido visible no aprobado si se ejecuta sin control.
- Prueba de calidad: SKILL con niveles SC0-SC3, patrones de canal, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 programmatic-seo
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / SEO programatico
- Responsabilidad real: planificar paginas SEO a escala con patron, datos, template, arquitectura, indexacion, schema, tracking y riesgos.
- Destino Claude Code: `.claude/skills/programmatic-seo/` y `.claude/commands/plan-programmatic-seo.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy evitando thin content, doorway pages, indexacion masiva sin control y cambios de CMS/URLs sin Orden de Cambio.
- Riesgo: alto; puede afectar indexacion, crawl budget, arquitectura y reputacion SEO si se ejecuta mal.
- Prueba de calidad: SKILL con niveles PS0-PS3, patrones pSEO, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 competitor-alternatives
- Responsable: Codex + Arquitecto
- Tipo: skill Claude Code / paginas comparativas
- Responsabilidad real: planificar paginas de alternativas, vs pages y comparativas con fuentes fechadas, posicionamiento honesto, SEO y riesgos legales/comerciales.
- Destino Claude Code: `.claude/skills/competitor-alternatives/` y `.claude/commands/plan-competitor-page.md`
- Decision: reescribir/adaptar
- Motivo: migrar la skill legacy sin permitir claims inventados, difamacion o comparativas no verificadas.
- Riesgo: medio-alto; puede afectar marca, legal, SEO y confianza si se publican datos falsos.
- Prueba de calidad: SKILL con niveles CA0-CA3, patrones de comparativa, plantilla, checklist, command y contrato de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 cold-email / email-sequence / lead-magnets / sales-enablement
- Responsable: Codex + Arquitecto
- Tipo: skills Claude Code / ventas y captacion
- Responsabilidad real: migrar prospeccion fria, secuencias lifecycle, recursos de captacion y materiales comerciales con criterios de reputacion, consentimiento, claims y aprobacion.
- Destino Claude Code: `.claude/skills/cold-email/`, `.claude/skills/email-sequence/`, `.claude/skills/lead-magnets/`, `.claude/skills/sales-enablement/` y commands relacionados.
- Decision: reescribir/adaptar
- Motivo: migrar el bloque comercial legacy sin permitir envios, automatizaciones, capturas o propuestas finales sin Orden de Cambio.
- Riesgo: medio-alto; puede afectar reputacion, cumplimiento, relaciones comerciales, pricing y confianza si se ejecuta sin aprobacion.
- Prueba de calidad: skills con niveles CO/ES/LM/SE, referencias compactas, plantillas, checklists, commands y contratos de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 pricing-strategy / revops / churn-prevention / referral-program
- Responsable: Codex + Arquitecto
- Tipo: skills Claude Code / negocio y retencion
- Responsabilidad real: migrar pricing, revenue operations, prevencion de churn y programas de referidos con guardrails de ingresos, CRM, billing, reputacion y aprobacion.
- Destino Claude Code: `.claude/skills/pricing-strategy/`, `.claude/skills/revops/`, `.claude/skills/churn-prevention/`, `.claude/skills/referral-program/` y commands relacionados.
- Decision: reescribir/adaptar
- Motivo: migrar el bloque de negocio sin permitir cambios reales de precios, CRM, billing, cancelaciones, pagos, links o programas sin Orden de Cambio.
- Riesgo: alto; puede afectar ingresos, pipeline, billing, churn, cumplimiento y confianza si se ejecuta sin aprobacion.
- Prueba de calidad: skills con niveles PR/RV/CH/RF, referencias compactas, plantillas, checklists, commands y contratos de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 launch-strategy / free-tool-strategy / marketing-ideas / marketing-psychology / product-marketing-context
- Responsable: Codex + Arquitecto
- Tipo: skills Claude Code / lanzamiento, crecimiento y posicionamiento
- Responsabilidad real: migrar planificacion de lanzamientos, herramientas gratuitas, ideacion de marketing, psicologia aplicada y contexto de product marketing con guardrails de publicacion, claims, contexto y aprobacion.
- Destino Claude Code: `.claude/skills/launch-strategy/`, `.claude/skills/free-tool-strategy/`, `.claude/skills/marketing-ideas/`, `.claude/skills/marketing-psychology/`, `.claude/skills/product-marketing-context/` y commands relacionados.
- Decision: reescribir/adaptar
- Motivo: migrar el bloque de crecimiento sin publicar, activar canales, capturar leads, manipular behavior, inventar contexto ni sobrescribir fuentes vivas sin control de artefactos.
- Riesgo: medio-alto; puede afectar marca, lanzamiento, captacion, confianza, posicionamiento y calidad de outputs si se ejecuta sin contexto real.
- Prueba de calidad: skills con niveles LS/FT/MI/MP/PM, referencias compactas, plantillas, checklists, commands y contratos de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 humanizalo / prompt-master / kling-producer
- Responsable: Codex + Arquitecto
- Tipo: skills Claude Code / contenido, prompts y media AI
- Responsabilidad real: migrar humanizacion de texto, creacion de prompts y produccion de video AI con control de claims, herramienta destino, coste, creditos, permisos y ejecucion segura.
- Destino Claude Code: `.claude/skills/humanizalo/`, `.claude/skills/prompt-master/`, `.claude/skills/kling-producer/` y commands relacionados.
- Decision: reescribir/adaptar
- Motivo: migrar utilidades legacy de produccion sin arrastrar repos embebidos, instrucciones infladas ni ejecucion externa automatica.
- Riesgo: medio; puede alterar claims, generar prompts inseguros o consumir creditos/video assets si se ejecuta sin aprobacion.
- Prueba de calidad: skills con niveles HU/PMT/KP, referencias compactas, plantillas, checklists, commands y contratos de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - P3-003 folder-cleanup / web-feedback-loop / woocommerce-setup
- Responsable: Codex + Arquitecto
- Tipo: skills Claude Code / operaciones, web y ecommerce
- Responsabilidad real: migrar limpieza de carpetas, feedback visual web y auditoria/setup WooCommerce con aprobacion previa para mover archivos, tocar web, modificar tienda, pagos, envios, impuestos o productos.
- Destino Claude Code: `.claude/skills/folder-cleanup/`, `.claude/skills/web-feedback-loop/`, `.claude/skills/woocommerce-setup/` y commands relacionados.
- Decision: reescribir/adaptar
- Motivo: migrar las ultimas skills legacy como procedimientos seguros, separando diagnostico/propuesta de ejecucion real.
- Riesgo: alto; puede afectar archivos de cliente, web publicada, checkout, pagos, envios, legal, productos y datos sensibles si se ejecuta sin control.
- Prueba de calidad: skills con niveles FCU/WFL/WC, referencias compactas, plantillas, checklists, commands y contratos de output.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - Cierre P3-003 skills legacy
- Responsable: Codex + Arquitecto
- Tipo: cierre de fase / inventario de skills
- Resultado: comparadas 40 carpetas legacy en `.agents/skills/` contra `.claude/skills/`; faltantes legacy en v2: 0.
- Extras v2 esperados: `migration-audit`, `ingesta-evidencia`, `verificacion-medicion`.
- Decision: marcar P3-003 como hecho.
- Riesgo residual: las skills migradas son procedimientos v2; aun falta P3-004 para migrar agentes especialistas y P3-005 para conectores/scripts.
- Estado: cerrado
- Commit: pendiente

### 2026-05-13 - P3-004 inventario agentes legacy
- Responsable: Codex + Arquitecto
- Tipo: inventario / plan de migracion de agentes
- Resultado: creado `planning/inventario-agentes-legacy.md` separando agentes migrables, referencias, aprendizajes y orden recomendado.
- Decision: iniciar P3-004 en estado `en curso`.
- Riesgo: medio; migrar agentes sin separar referencias del Docente podria inflar contexto y duplicar conocimiento.
- Estado: implementado
- Commit: `c0d6a8a`

### 2026-05-13 - P3-004 lideres Equipo Clientes
- Responsable: Codex + Arquitecto
- Tipo: subagents Claude Code / lideres de area
- Resultado: creados `seo-leader`, `cro-leader`, `sem-leader`, `social-leader`, `reports-leader` y `web-leader`; actualizado `leader-clientes` para enrutar a agentes reales.
- Decision: migrar lideres de area antes que especialistas para desbloquear routing ordenado.
- Riesgo: medio; son agentes de coordinacion, no ejecutan produccion directa.
- Estado: implementado
- Commit: `c2845bf`

### 2026-05-13 - P3-004 especialistas SEO/CRO/SEM
- Responsable: Codex + Arquitecto
- Tipo: subagents Claude Code / especialistas clientes
- Resultado: creados 15 especialistas v2 para SEO (`seo-*`), CRO (`cro-*`) y SEM (`sem-*`), con rutas a skills migradas y bloqueos de produccion.
- Decision: migrar primero areas con mayor uso operativo y riesgo de calidad en outputs.
- Riesgo: medio-alto; pueden influir decisiones SEO, CRO y Ads, pero no ejecutan cambios reales por defecto.
- Estado: implementado
- Commit: `d9d6f90`

### 2026-05-13 - P3-004 especialistas Social/Reports/Web
- Responsable: Codex + Arquitecto
- Tipo: subagents Claude Code / especialistas clientes
- Resultado: creados 12 especialistas v2 para Social, Reports y Web, con rutas a skills migradas, protocolos y bloqueos de produccion.
- Decision: completar especialistas del Equipo Clientes antes de migrar Equipo Agencia.
- Riesgo: medio-alto; pueden afectar comunicacion publica, informes y web, pero no ejecutan produccion sin aprobacion.
- Estado: implementado
- Commit: `92cde16`

### 2026-05-13 - P3-004 especialistas Equipo Agencia
- Responsable: Codex + Arquitecto
- Tipo: subagents Claude Code / especialistas internos
- Resultado: creados `agency-captacion`, `agency-reputacion`, `agency-onboarding`, `agency-retencion` y `agency-finanzas`; actualizado `leader-agencia`.
- Decision: completar Equipo Agencia despues de Equipo Clientes.
- Riesgo: medio; afectan captacion, reputacion, onboarding, retencion y pricing interno, pero no ejecutan acciones externas por defecto.
- Estado: implementado
- Commit: `e2365f6`

### 2026-05-13 - P3-004 gobernanza y loops
- Responsable: Codex + Arquitecto
- Tipo: subagents Claude Code / gobernanza del sistema
- Resultado: creados `arquitecto`, `fenix`, `calibracion` y `loops-leader`; actualizados `leader-clientes`, `leader-agencia`, README e inventario.
- Decision: migrar estos roles al final porque dependen de que las rutas operativas de clientes y agencia ya existan.
- Riesgo: medio; afectan arquitectura, memoria y loops, pero operan como lectura/criterio y no ejecutan produccion por defecto.
- Estado: implementado
- Commit: `4b35139`

### 2026-05-13 - Cierre P3-004 agentes
- Responsable: Codex + Arquitecto
- Tipo: cierre de backlog / verificacion de inventario
- Resultado: verificados 42 roles legacy migrados a `.claude/agents/`; faltantes esperados: 0; total actual: 46 subagents reales y 47 archivos Markdown incluyendo `README.md`.
- Decision: marcar P3-004 como `hecho` en `planning/backlog-migracion.md`.
- Riesgo: bajo-medio; quedan referencias legacy no migradas como subagents por decision consciente.
- Estado: implementado
- Commit: este mismo cambio; consultar `git log --oneline` para el hash final.

### 2026-05-13 - P3-005 inventario conectores/scripts
- Responsable: Codex + Arquitecto
- Tipo: inventario / saneamiento de scripts
- Resultado: creado `planning/inventario-conectores-scripts.md` y P3-005 marcado como `en curso`.
- Decision: migrar solo `protocol_guard.py` adaptado, `.mcp.example.json` seguro y documentacion; bloquear o deferir conectores con accesos/produccion.
- Riesgo: medio; evita copiar scripts S4 al v2 sin saneamiento.
- Estado: implementado
- Commit: `f90b3cd`

### 2026-05-13 - P3-005 guard v2 y MCP seguro
- Responsable: Codex + Arquitecto
- Tipo: script seguro / configuracion local
- Resultado: creado `scripts/protocol_guard.py`, `.mcp.example.json`; actualizado `.gitignore` y `scripts/README.md`.
- Decision: migrar guard adaptado a rutas v2 y documentar MCP sin valores reales; no copiar conectores S4.
- Riesgo: medio; script defensivo, sin llamadas externas ni escritura fuera de reporte local ignorado.
- Estado: implementado
- Commit: `11c9af8`; ajuste posterior `7d4f6ce`

### 2026-05-13 - Cierre P3-005 conectores/scripts
- Responsable: Codex + Arquitecto
- Tipo: cierre de backlog / saneamiento de conectores
- Resultado: P3-005 marcado como `hecho`; `scripts/protocol_guard.py` probado limpio con repo sin cambios; `.mcp.example.json` seguro; `.mcp.json` ignorado; conectores S4 no copiados.
- Decision: cerrar P3-005 sin migrar conectores productivos legacy; quedan deferidos hasta flujo seguro con dry-run, variables locales y Orden de Cambio.
- Riesgo residual: medio; los conectores reales aun no estan activos en v2, pero el repo queda protegido contra migracion insegura.
- Estado: implementado
- Commit: este mismo cambio; consultar `git log --oneline` para el hash final.

### 2026-05-13 - Cierre operativo migracion v2
- Responsable: Codex + Arquitecto
- Tipo: cierre operativo / manual de arranque
- Resultado: creado `planning/cierre-migracion-v2.md` y actualizado `README.md` con estado final y ruta de arranque.
- Decision: cerrar la migracion base con una guia de uso para evitar que el sistema quede completo pero ambiguo.
- Riesgo residual: bajo; documento operativo sin secretos ni llamadas externas.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - Validacion operativa post-migracion v2
- Responsable: Codex + Arquitecto
- Tipo: validacion / ajuste menor de agente
- Resultado: creado `planning/validacion-operativa-v2.md`; corregido `effort: high` en `.claude/agents/arquitecto-migracion-claude.md`; precisado conteo de agentes.
- Decision: validar el sistema como operable antes de iniciar trabajos reales sobre clientes o agencia.
- Riesgo residual: bajo; ajuste documental y frontmatter, sin produccion ni accesos.
- Estado: implementado
- Commit: pendiente

### 2026-05-13 - Sprint 01 arranque operativo v2
- Responsable: Codex + Arquitecto
- Tipo: plan operativo post-migracion
- Resultado: creado `planning/sprint-01-operacion-v2.md` y enlazado desde `README.md`.
- Decision: separar la migracion cerrada del primer ciclo operativo para evitar seguir acumulando piezas sin probar el sistema.
- Riesgo residual: bajo; plan de trabajo sin produccion ni accesos.
- Estado: implementado
- Commit: pendiente
### 2026-05-18 - fase 2 migracion minima de clientes activos

- Origen legacy: `../clients/cashier-bubble-tea/`, `../clients/la-bottega-del-gusto/`, `../clients/stramondo-venezuela/`.
- Destino Claude Code: `clients/cashier-bubble-tea/`, `clients/la-bottega-del-gusto/`, `clients/stramondo-venezuela/`.
- Tipo: migracion minima de memoria operativa de clientes activos.
- Archivos migrados: `context.md`, `memory.md`, `log.md`, `mensajes.md`, `tasks.md`; en Bottega tambien `brand.md`.
- Outputs historicos: no migrados.
- Cliente inactivo `shogun-motors`: no migrado a `clients/` operativo; permanece como legacy/inactivo salvo decision futura.
- Validacion requerida: ejecutar `scripts/protocol_guard.py` y revisar que cada cliente tenga `outputs/manifest.md`.

### 2026-05-18 - fase 3 auditoria por areas

- Alcance: `.claude/agents/`, `.claude/skills/`, `.claude/commands/`.
- Tipo: auditoria estructural sin cambios operativos.
- Evidencia: 47 agentes, 45 skills con `SKILL.md`, 43 commands, excluyendo README.
- Decision: no replicar `seo-canon` automaticamente en todas las areas.
- Criterio: una skill dedicada resuelve procedimiento; un canon solo aplica cuando hay criterio transversal obligatorio antes de cualquier tarea del area.
- Resultado: SEO queda como patron maduro; Reports es siguiente prioridad por falta de skill dedicada; SEM requiere auditoria propia por riesgo operativo; CRO, Web y Social se mantienen con skills procedurales hasta observar fallos reales.
- Documento: `planning/auditoria-agentes-skills-areas-2026-05-18.md`.
- Validacion: consulta Claude realizada; `scripts/protocol_guard.py` limpio.

### 2026-05-18 - fase 4 skill reports

- Alcance: agentes Reports, contrato de calidad y agentes Reports legacy.
- Tipo: migracion de procedimiento operativo.
- Decision: crear skill `reports`, no canon. Reports necesitaba procedimiento, no una puerta transversal historica como SEO.
- Resultado: creada `.claude/skills/reports/` con `SKILL.md`, `references/fuentes-por-servicio.md` y templates `informe-mensual.md`, `alerta.md`, `proxpasos.md`.
- Agentes conectados: `reports-leader`, `reports-cliente`, `reports-alertas`, `reports-proxpasos`.
- Contaminacion evitada: no se copiaron informes reales de clientes dentro de la skill; solo se migraron reglas generales de reporting.
- Validacion: consulta Claude realizada; validacion manual limpia; `quick_validate.py` bloqueado por dependencia local `PyYAML` ausente.

### 2026-05-18 - fase 5 SEM / Paid Ads

- Alcance: agentes SEM v2, skill `paid-ads`, referencias `platform-guide.md`, SEM legacy y lecciones operativas anonimizadas.
- Tipo: refuerzo de reglas bajo demanda.
- Decision: no crear canon SEM. Reforzar `paid-ads` porque la skill ya existe y el problema era falta de reglas practicas de plataforma, no falta de arquitectura.
- Resultado: `platform-guide.md` ahora incluye bloqueadores por plataforma; creado `platform-rules.md` con reglas de validacion de eventos y metricas; `SKILL.md` enlaza la nueva referencia.
- Contaminacion evitada: no se copiaron nombres, cuentas, campanas ni casos reales de clientes; solo se convirtieron aprendizajes en principios generales.
- Validacion: `scripts/protocol_guard.py` limpio.

### 2026-05-18 - fase 6 limpieza de contaminacion general

- Alcance: `.claude/skills/`, `.claude/agents/`, `.claude/commands/`, `.claude/rules/`, `AGENTS.md`, `agency/`, `planning/`, `registries/`.
- Tipo: saneamiento de frontera cliente/general.
- Decision: limpiar comandos y el loop de Meta Ads; no tocar `agency/`, `planning/` ni `registries/` porque son historia/trazabilidad; no tocar `seo-canon` porque sus coincidencias son ejemplos pedagogicos genericos.
- Resultado: 18 commands cambiaron ejemplos reales por slugs inventados; `loops-leader` dejo de apuntar a un cliente concreto; `commands/README.md` ahora prohibe clientes reales en ejemplos reutilizables.
- Contaminacion evitada: los clientes reales quedan en `/clients` o en registros historicos, no en instrucciones generales de uso.
- Validacion: grep final sin clientes reales en commands/loops reutilizables; `scripts/protocol_guard.py` limpio.

### 2026-05-18 - fase 7 mapa commands-skills-agents

- Alcance: 43 commands, skills referenciadas por commands y skills sin command directo.
- Tipo: auditoria documental de duplicacion.
- Decision: no hay duplicacion rota. Los commands son entradas practicas; las skills son procedimientos; los agents son roles y orquestadores.
- Resultado: creado `planning/mapa-commands-skills-2026-05-18.md`; actualizado `.claude/commands/README.md` con el patron command-skill.
- Evidencia: 0 commands apuntan a skills inexistentes. Las 5 skills sin command directo estan usadas por agentes (`alignment-check`, `client-audit`, `reports`, `seo-audit`, `seo-canon`).
- Validacion: `scripts/protocol_guard.py` limpio.

### 2026-05-18 - fase 8 patron operativo de agentes

- Alcance: patron general para commands, agents, skills, references, templates, canon, clients, planning y registries.
- Tipo: guia de arquitectura operativa.
- Decision: copiar el patron que funciono en SEO, no copiar la estructura SEO completa a todas las areas.
- Resultado: creado `planning/patron-operativo-agentes-v2.md`; enlazado desde `README.md`.
- Criterio: canon solo si hay criterio transversal probado; skill si falta procedimiento; reference si hay conocimiento largo bajo demanda; command si Rodrigo necesita entrada simple.
- Validacion: `scripts/protocol_guard.py` limpio.

### 2026-05-19 - fase 9 auditoria CRO/Web/Social

- Alcance: agentes y skills de CRO, Web y Social.
- Tipo: auditoria estructural y ajuste minimo de routing.
- Decision: no crear canon CRO/Web/Social ahora. Las areas ya tienen skills procedurales con referencias/templates/checklists; se reforzaran solo si outputs reales muestran fallos repetidos.
- Resultado: creado `planning/auditoria-cro-web-social-2026-05-19.md`; corregido `social-leader.md` para enrutar comunidad/crisis a `social-comunidad` en lugar de marcarlo como futuro.
- Contaminacion evitada: no se copiaron ejemplos reales de clientes ni material legacy especifico dentro de skills generales.
- Validacion: `scripts/protocol_guard.py` limpio; grep de routing Social confirma `social-comunidad`.

### 2026-05-19 - fase 11 contaminacion restante y contexto agencia

- Alcance: `.claude/skills`, `.claude/agents`, `.claude/commands`, `.claude/rules`, memoria `agency/`.
- Tipo: auditoria de contaminacion y sincronizacion de memoria interna.
- Decision: no eliminar nombres reales de `agency/`, porque es memoria operativa interna; si mantener las primitivas reutilizables sin clientes reales.
- Resultado: creado `planning/auditoria-contaminacion-restante-2026-05-19.md`; actualizado `agency/context.md` para reflejar que los 4 clientes activos ya existen en v2 con migracion minima; actualizado `agency/log.md`.
- Cliente inactivo: `shogun-motors` permanece solo como historico/inactivo y fuera de loops, informes y tareas.
- Validacion: escaneo `.claude/` sin coincidencias; `scripts/protocol_guard.py` limpio; `git diff --check` limpio.

### 2026-05-19 - fase 12 homologacion Computer Chamberi

- Alcance: cliente piloto `clients/computer-chamberi/`.
- Tipo: homologacion operativa de cliente activo.
- Decision: no reescribir `context.md`; el cliente ya tiene estructura v2 suficiente. Crear output de homologacion, actualizar manifest/log y marcar `client-audit v2` como cubierto.
- Resultado: creado `clients/computer-chamberi/outputs/homologacion-v2-2026-05-19.md`; actualizado `tasks.md` para dejar como siguiente prioridad real la verificacion de medicion y linea base.
- Contaminacion evitada: la conversacion historica de diagnostico SEO permanece dentro del cliente, no en canon ni skills generales.
- Validacion: `scripts/protocol_guard.py` limpio; `git diff --check` limpio; manifest actualizado.

### 2026-05-19 - fase 13 homologacion Chashier Bubble Tea

- Alcance: cliente activo `clients/cashier-bubble-tea/`.
- Tipo: homologacion operativa de cliente activo.
- Decision: no reescribir `context.md` ni borrar mensajes legacy. Sincronizar solo tareas con evidencia fuerte de `log.md` y `memory.md`.
- Resultado: creado `clients/cashier-bubble-tea/outputs/homologacion-v2-2026-05-19.md`; actualizado `tasks.md` para marcar informe de 2 anos como preparado y canonical como fijado en WordPress, manteniendo validacion GSC pendiente.
- Contaminacion evitada: outputs historicos siguen sin copiarse al repo v2; el nuevo output de homologacion queda como artefacto local de cliente.
- Validacion: `scripts/protocol_guard.py` limpio; `git diff --check` limpio; manifest actualizado.

### 2026-05-19 - fase 14 homologacion La Bottega del Gusto

- Alcance: cliente activo sensible `clients/la-bottega-del-gusto/`.
- Tipo: homologacion operativa de cliente activo con WordPress/WooCommerce.
- Decision: no reescribir `tasks.md`, no borrar mensajes y no tocar produccion. Corregir solo el conteo obsoleto de imagenes en `context.md`, porque `log.md`, `tasks.md`, `memory.md` y `mensajes.md` posteriores coinciden en 82 productos sin imagen.
- Resultado: creado `clients/la-bottega-del-gusto/outputs/homologacion-v2-2026-05-19.md`; actualizado manifest/log/planning/registros; Bottega queda homologado con prioridad de go-live y Orden de Cambio antes de operaciones reales.
- Contaminacion evitada: datos reales de Bottega quedan solo dentro del cliente y registros, no en canon, skills ni agentes generales.

### 2026-05-19 - fase 15 homologacion Stramondo Venezuela

- Alcance: cliente activo sensible `clients/stramondo-venezuela/`.
- Tipo: homologacion operativa de cliente activo con Meta Ads.
- Decision: no ejecutar conector Meta Ads, no tocar tokens y no reescribir mensajes. Corregir solo inconsistencias documentales para que `context.md` y `tasks.md` reflejen el ultimo dato confirmado del 2026-05-11: campaña principal B2B `PAUSED` y evaluacion por link clicks/CPC/CTR, no por eventos `messaging_*` como conversiones reales.
- Resultado: creado `clients/stramondo-venezuela/outputs/homologacion-v2-2026-05-19.md`; actualizado manifest/log/tasks/context/planning/registros.
- Contaminacion evitada: datos reales de campaña quedan en `/clients/stramondo-venezuela` y registros, no en skills, agentes ni canon general.

### 2026-05-19 - fase 16 auditoria duplicaciones agents skills commands

- Alcance: `.claude/agents`, `.claude/skills`, `.claude/commands`.
- Tipo: auditoria estructural y ajuste minimo.
- Decision: no consolidar agentes ni borrar artefactos en lote. Corregir solo `seo-leader` porque `seo-tecnico` ya existe y no debe figurar como futuro. Documentar los 40 `openai.yaml` como pendiente-revision antes de una eliminacion ordenada.
- Resultado: creado `planning/auditoria-duplicaciones-agents-skills-commands-2026-05-19.md`; corregido routing SEO.
- Contaminacion evitada: no se mezclaron datos de clientes ni ejemplos reales en primitives generales.

### 2026-05-19 - fase 17 saneamiento openai.yaml

- Alcance: `.claude/skills/*/agents/openai.yaml`.
- Tipo: saneamiento de artefactos no nativos de Claude Code.
- Decision: eliminar los 40 `openai.yaml` porque fueron creados por Codex durante la migracion, no habia consumidor externo conocido y no son una primitiva viva de Claude Code.
- Resultado: creado `planning/saneamiento-openai-yaml-2026-05-19.md`; actualizado `planning/auditoria-duplicaciones-agents-skills-commands-2026-05-19.md` para marcar `DPL-002` como resuelto; eliminados los 40 `openai.yaml`.
- Contaminacion evitada: se retiro metadata externa que podia hacer creer a futuros agentes que habia otra capa de instrucciones aparte de `SKILL.md`.
- Validacion pendiente al cierre de fase: confirmar sin `openai.yaml`, ejecutar `protocol_guard.py`, commit y push.
