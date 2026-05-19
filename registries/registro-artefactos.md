# Registro de artefactos

Este registro lista archivos, carpetas, outputs, scripts o documentos operativos creados o modificados por agentes.

## Formato

```text
### YYYY-MM-DD - ruta
- Area:
- Agente:
- Tipo:
- Motivo:
- Estado:
- Reemplaza a:
- Accion recomendada:
- Riesgo:
```

## Entradas

### 2026-05-12 - rol de migracion Claude Code
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: rol/protocolo/skill/command
- Motivo: crear la autoridad operativa que migrara el sistema legacy al sistema v2 usando primitivas oficiales de Claude Code.
- Estado: vigente
- Reemplaza a: migraciones manuales sin criterio unificado.
- Accion recomendada: usar antes de mover cualquier pieza legacy.
- Riesgo: bajo; no incluye secretos ni datos de clientes.

### 2026-05-12 - planning/plan-maestro-migracion.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: plan maestro / backlog
- Motivo: organizar la migracion completa para que Rodrigo entienda que se hara, por que se hara y como se comprobara, siguiendo Claude Code y considerando la complejidad del sistema legacy.
- Estado: vigente
- Reemplaza a: avance por intuicion o por tareas sueltas sin secuencia global.
- Accion recomendada: usar como mapa de ruta en cada sesion de migracion y actualizar backlog al cerrar fases.
- Riesgo: bajo; documento operativo sin secretos ni datos privados de clientes.

### 2026-05-12 - planning/inventario-legacy.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: inventario de migracion
- Motivo: completar P0-001 mapeando el sistema legacy por areas, responsabilidades, riesgos y destino Claude Code probable.
- Estado: vigente
- Reemplaza a: lectura informal del legacy sin mapa operativo.
- Accion recomendada: usar como entrada para P0-002 auditoria de scripts con secretos historicos.
- Riesgo: bajo; no contiene secretos ni valores de credenciales.

### 2026-05-12 - planning/auditoria-scripts-sensibles.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: auditoria de seguridad / scripts
- Motivo: completar P0-002 detectando scripts legacy con credenciales hardcodeadas, OAuth, tokens, escrituras de `.env`, servicios externos o riesgo de produccion.
- Estado: vigente
- Reemplaza a: sospecha informal sobre scripts sensibles.
- Accion recomendada: ejecutar P0-003 `gestion-secretos` antes de migrar cualquier script S3/S4.
- Riesgo: bajo como documento; no contiene valores secretos.

### 2026-05-12 - protocols/gestion-accesos.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: protocolo / regla
- Motivo: completar P0-003 migrando el protocolo canonico legacy de gestion de secretos al sistema v2 adaptado a Claude Code, scripts, MCP, hooks y registros.
- Estado: vigente
- Reemplaza a: dependencia del protocolo legacy `sistema/protocolos/gestion-secretos.md` como unica fuente.
- Accion recomendada: usar antes de migrar scripts, conectores, MCP o cualquier acceso S2/S3/S4.
- Riesgo: bajo; no contiene valores secretos.

### 2026-05-12 - protocols/control-artefactos.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: protocolo / regla
- Motivo: completar P0-004 migrando el protocolo canonico legacy de control de artefactos al sistema v2, adaptado a GitHub, `.claude/`, outputs ignorados, manifests y registros.
- Estado: vigente
- Reemplaza a: dependencia del protocolo legacy `sistema/protocolos/control-artefactos.md` como unica fuente.
- Accion recomendada: usar antes de crear, modificar, mover, archivar o eliminar archivos/carpetas relevantes.
- Riesgo: bajo; protocolo sin datos privados ni secretos.

### 2026-05-12 - protocols/activos-criticos.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: protocolo / regla
- Motivo: completar P0-005 migrando el protocolo canonico legacy de activos criticos al sistema v2, con niveles A/B/C/D, Orden de Cambio, fuentes de verdad, diagnostico por capas y relacion con Claude Code.
- Estado: vigente
- Reemplaza a: dependencia del protocolo legacy `sistema/protocolos/activos-criticos.md` como unica fuente.
- Accion recomendada: usar antes de tocar produccion, datos vivos, fuentes de verdad, scripts externos, MCP, Ads, WordPress, WooCommerce, hosting, DNS o accesos.
- Riesgo: bajo; protocolo sin datos privados ni secretos.

### 2026-05-12 - protocols/cierre-humano.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: protocolo / regla
- Motivo: completar P0-006 migrando el protocolo canonico legacy de cierre humano al sistema v2 para que cada tarea cierre con explicacion clara, estado, riesgos y siguiente paso.
- Estado: vigente
- Reemplaza a: dependencia del protocolo legacy `sistema/protocolos/cierre-humano.md` como unica fuente.
- Accion recomendada: usar al cerrar cualquier tarea con trabajo detras, cambios, riesgos, commits, registros, scripts o migracion.
- Riesgo: bajo; protocolo sin datos privados ni secretos.

### 2026-05-12 - .claude/hooks/block-sensitive-data.py
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: hook de seguridad / configuracion Claude Code
- Motivo: completar P0-007 creando un hook `PreToolUse` que bloquea escrituras o comandos con rutas o valores sensibles antes de que se ejecuten.
- Estado: vigente
- Reemplaza a: proteccion manual basada solo en `.gitignore` y protocolo escrito.
- Accion recomendada: ejecutar `python .claude/hooks/block-sensitive-data.py --self-test` despues de modificar el hook o `.claude/settings.json`.
- Riesgo: bajo; el script contiene patrones defensivos y datos de prueba construidos sin valores reales.

### 2026-05-12 - quality/diagnostico-calidad.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: diagnostico de calidad / matriz de causas raiz
- Motivo: completar P1-001 identificando por que los outputs pueden carecer de calidad, criterio o acertividad y que piezas v2 deben corregirlo.
- Estado: vigente
- Reemplaza a: diagnostico informal de baja calidad sin matriz accionable.
- Accion recomendada: usar como base directa de P1-002 `quality/criterios-output.md`.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - quality/criterios-output.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: criterios de calidad / contratos de salida
- Motivo: completar P1-002 creando contratos verificables para auditorias, SEO, informes, proximos pasos, CRO, SEM, Social, Web, Copy y Agencia.
- Estado: vigente
- Reemplaza a: criterios dispersos en prompts legacy sin aceptacion estandarizada por entregable.
- Accion recomendada: usar como fuente obligatoria al migrar skills y lideres operativos.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/skills/client-audit/
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: skill operativa Claude Code
- Motivo: completar P1-003 migrando `client-audit` como skill bajo demanda con plantilla y checklist de calidad.
- Estado: vigente
- Reemplaza a: `.agents/skills/client-audit/SKILL.md` como prompt legacy directo.
- Accion recomendada: usar como primera skill piloto para auditorias de cliente antes de migrar Lider Clientes.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/skills/seo-audit/
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: skill operativa Claude Code
- Motivo: completar P1-004 migrando `seo-audit` como skill bajo demanda con evidencia, jerarquia de fuentes, plantilla y checklist de revision.
- Estado: vigente
- Reemplaza a: `.agents/skills/seo-audit/SKILL.md` como prompt legacy directo.
- Accion recomendada: usar como skill piloto para auditorias SEO antes de migrar Lider SEO.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/agents/docente.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: subagent Claude Code / aprendizaje operativo
- Motivo: completar P1-005 migrando El Docente como rol read-only para convertir fallos y correcciones en criterio examinable.
- Estado: vigente
- Reemplaza a: `agents/docente/docente.md` como prompt legacy directo.
- Accion recomendada: usar despues de outputs rechazados, correcciones de Rodrigo o fallos de criterio repetibles.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/agents/leader-clientes.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: subagent Claude Code / orquestacion de clientes
- Motivo: completar P2-001 creando Lider Clientes v2 como orquestador ligero, read-only y alineado con skills/reglas/contratos de calidad.
- Estado: vigente
- Reemplaza a: `agents/leader-clients.md` como prompt legacy directo.
- Accion recomendada: usar al mencionar un cliente, revisar estado, priorizar proximos pasos o enrutar trabajo hacia `client-audit`/`seo-audit`.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/agents/leader-agencia.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: subagent Claude Code / orquestacion interna
- Motivo: completar P2-002 creando Lider Agencia v2 como orquestador ligero y read-only para trabajo interno de E-SELEC.
- Estado: vigente
- Reemplaza a: `agents/agency/leader-agency.md` como prompt legacy directo.
- Accion recomendada: usar con modo agencia, tareas internas, captacion, reputacion, onboarding, retencion, finanzas y operaciones internas.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/commands/alertas-pendientes.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: command Claude Code / workflow recurrente
- Motivo: completar P2-003 convirtiendo `LOOP: alertas-pendientes` en command invocable con lectura consolidada y escritura opcional.
- Estado: vigente
- Reemplaza a: seccion `LOOP 3 - Alertas Pendientes` de `agents/loops/leader-loops.md`.
- Accion recomendada: usar para revisar mensajes pendientes antes de reuniones, cierres semanales o decisiones de prioridad.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - .claude/commands/auditoria-semanal.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: command Claude Code / workflow recurrente
- Motivo: completar P2-004 convirtiendo `LOOP: auditoria-semanal` en command invocable para detectar bloqueos, estancamientos y tareas atascadas.
- Estado: vigente
- Reemplaza a: seccion `LOOP 1 - Auditoria Semanal` de `agents/loops/leader-loops.md`.
- Accion recomendada: usar al inicio de semana o antes de planificar prioridades de clientes.
- Riesgo: bajo; no contiene secretos ni datos privados.

### 2026-05-12 - planning/piloto-01.md
- Area: sistema E-SELEC v2
- Agente: Codex + Arquitecto
- Tipo: decision operativa / piloto
- Motivo: completar P2-005 definiendo Computer Chamberi como primer cliente piloto para probar operacion v2 sin tocar produccion.
- Estado: vigente
- Reemplaza a: decision informal de cliente piloto.
- Accion recomendada: ejecutar P3-002 migrando estructura minima de `computer-chamberi`.
- Riesgo: bajo; no contiene secretos ni datos privados sensibles.

### 2026-05-12 - clients/computer-chamberi/
- Area: sistema E-SELEC v2 / cliente piloto
- Agente: Codex + Arquitecto
- Tipo: memoria de cliente / migracion minima
- Motivo: completar P3-002 migrando estructura saneada del cliente piloto para probar `leader-clientes`, `client-audit` y `seo-audit`.
- Estado: vigente
- Reemplaza a: dependencia exclusiva de `clients/computer-chamberi/` legacy para pruebas piloto.
- Accion recomendada: ejecutar auditoria piloto en modo diagnostico, sin tocar produccion.
- Riesgo: bajo-medio; contiene resumen operativo de cliente, sin secretos ni outputs pesados.

### 2026-05-12 - planning/resultado-piloto-01.md
- Area: sistema E-SELEC v2 / cliente piloto
- Agente: Codex + Arquitecto
- Tipo: resultado de prueba en seco
- Motivo: documentar la primera prueba de `client-audit` y `seo-audit` sobre `computer-chamberi` sin usar herramientas vivas ni tocar produccion.
- Estado: vigente
- Reemplaza a: ausencia de prueba operativa del sistema v2 con cliente real.
- Accion recomendada: verificar medicion viva antes de convertir el diagnostico SEO en auditoria final.
- Riesgo: bajo; no contiene secretos ni outputs pesados.

### 2026-05-12 - .claude/skills/verificacion-medicion/
- Area: sistema E-SELEC v2 / calidad de datos
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code
- Motivo: crear un procedimiento reusable para comprobar fuentes de medicion antes de auditorias, informes o decisiones.
- Estado: vigente
- Reemplaza a: verificacion manual e inconsistente de GA4/GSC/SEMrush/GBP/Ads.
- Accion recomendada: usar antes de auditorias SEO finales, informes mensuales, CRO y Ads cuando las conclusiones dependan de datos vivos.
- Riesgo: bajo; solo lectura, sin secretos ni produccion.

### 2026-05-12 - .claude/commands/verificar-medicion.md
- Area: sistema E-SELEC v2 / command operativo
- Agente: Codex + Arquitecto
- Tipo: command Claude Code
- Motivo: permitir que Rodrigo invoque la verificacion de medicion de forma directa por cliente y alcance.
- Estado: vigente
- Reemplaza a: ejecucion informal de checks de medicion antes de outputs.
- Accion recomendada: ejecutar `/verificar-medicion [cliente] [alcance]` antes de convertir diagnosticos parciales en entregables finales.
- Riesgo: bajo; command de lectura por defecto con escritura opcional controlada.

### 2026-05-12 - planning/resultado-verificacion-medicion-01.md
- Area: sistema E-SELEC v2 / prueba piloto de medicion
- Agente: Codex + Arquitecto
- Tipo: resultado de prueba en seco
- Motivo: probar la nueva skill `verificacion-medicion` con `computer-chamberi` antes de auditoria SEO final.
- Estado: vigente
- Reemplaza a: decision implicita sobre suficiencia de datos.
- Accion recomendada: verificar GSC + SEMrush para subir la medicion de Nivel 1 a Nivel 2/3.
- Riesgo: bajo; no contiene secretos ni datos vivos exportados.

### 2026-05-12 - clients/computer-chamberi/outputs/evidencia-seo-2026-05-12.md
- Area: cliente piloto / Computer Chamberi
- Agente: Codex + Arquitecto
- Tipo: output saneado de evidencia SEO
- Motivo: extraer evidencia minima desde outputs legacy recientes sin copiar exports brutos ni secretos.
- Estado: vigente
- Reemplaza a: dependencia de leer outputs legacy completos para cada auditoria v2.
- Accion recomendada: usar como base de auditoria SEO parcial fuerte y revalidar GSC/SEMrush antes de entregar al cliente.
- Riesgo: medio si se usa como dato final sin revalidar unidades; bajo como evidencia interna.

### 2026-05-12 - .gitignore excepcion evidencia-*.md
- Area: sistema E-SELEC v2 / control de artefactos
- Agente: Codex + Arquitecto
- Tipo: configuracion de repositorio
- Motivo: permitir versionar outputs saneados `evidencia-*.md` sin abrir la puerta a exports pesados ni artefactos brutos de cliente.
- Estado: vigente
- Reemplaza a: regla demasiado amplia que impedia subir evidencia saneada citada por manifests.
- Accion recomendada: mantener la excepcion solo para paquetes saneados; no versionar exports brutos.
- Riesgo: bajo-medio si se usa mal el prefijo; revisar contenido antes de commit.

### 2026-05-12 - planning/resultado-seo-audit-piloto-02.md
- Area: sistema E-SELEC v2 / prueba seo-audit
- Agente: Codex + Arquitecto
- Tipo: resultado de prueba en seco
- Motivo: probar `seo-audit` con evidencia SEO saneada de Computer Chamberi y comprobar que el output queda parcial fuerte, no final.
- Estado: vigente
- Reemplaza a: diagnostico SEO piloto sin evidencia suficiente.
- Accion recomendada: usar como referencia de calidad para futuras auditorias SEO v2; no entregar al cliente sin revalidar fuentes vivas.
- Riesgo: bajo-medio; contiene datos SEO resumidos, sin secretos ni exports brutos.

### 2026-05-12 - .claude/skills/ingesta-evidencia/
- Area: sistema E-SELEC v2 / seguridad de datos
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code
- Motivo: crear un procedimiento para sanear exports, datos vivos, capturas y outputs legacy antes de usarlos o versionarlos.
- Estado: vigente
- Reemplaza a: ingestion manual no estandarizada de evidencia.
- Accion recomendada: usar antes de `verificacion-medicion`, auditorias, informes o cualquier evidencia nueva.
- Riesgo: bajo; procedimiento de saneamiento sin secretos ni produccion.

### 2026-05-12 - .claude/commands/ingestar-evidencia.md
- Area: sistema E-SELEC v2 / command operativo
- Agente: Codex + Arquitecto
- Tipo: command Claude Code
- Motivo: permitir invocar la ingesta segura de evidencia por cliente y fuente.
- Estado: vigente
- Reemplaza a: instrucciones dispersas para convertir exports en evidencia.
- Accion recomendada: usar `/ingestar-evidencia [cliente] [fuente]` antes de guardar `evidencia-*.md`.
- Riesgo: bajo; command de saneamiento, sin produccion.

### 2026-05-12 - agency/ estructura v2
- Area: agencia E-SELEC
- Agente: Codex + Arquitecto
- Tipo: memoria interna / migracion saneada
- Motivo: completar P3-001 migrando contexto, marca, preferencias, loops, mensajes, historial y manifest de agencia a v2.
- Estado: vigente
- Reemplaza a: dependencia directa de `agency/` legacy para trabajo interno.
- Accion recomendada: usar `agency/` v2 con `leader-agencia`; no volver a copiar legacy completo.
- Riesgo: bajo-medio; contiene memoria interna saneada, sin secretos ni PII innecesaria.

### 2026-05-13 - .claude/skills/analytics-tracking/
- Area: sistema E-SELEC v2 / medicion
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `analytics-tracking` como skill v2 para auditar y disenar GA4/GTM/eventos/conversiones sin tocar produccion.
- Estado: vigente
- Reemplaza a: `.agents/skills/analytics-tracking/` como skill legacy directa.
- Accion recomendada: usar antes de informes, CRO, Ads o cambios de medicion.
- Riesgo: bajo-medio; puede derivar en cambios de produccion, pero la skill bloquea implementacion sin Orden de Cambio.

### 2026-05-13 - .claude/skills/site-architecture/
- Area: sistema E-SELEC v2 / web y SEO
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `site-architecture` como skill v2 para disenar arquitectura, URLs, navegacion, enlazado interno y redirecciones sin tocar produccion.
- Estado: vigente
- Reemplaza a: `.agents/skills/site-architecture/` como skill legacy directa.
- Accion recomendada: usar antes de redisenos, cambios de menu, cambios de URLs, planes SEO de estructura o briefs web.
- Riesgo: medio; puede derivar en cambios de produccion y SEO, pero la skill bloquea implementacion sin inventario, plan 301 y Orden de Cambio.

### 2026-05-13 - .claude/skills/schema-markup/
- Area: sistema E-SELEC v2 / SEO tecnico
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `schema-markup` como skill v2 para auditar y disenar datos estructurados JSON-LD seguros y validables.
- Estado: vigente
- Reemplaza a: `.agents/skills/schema-markup/` como skill legacy directa.
- Accion recomendada: usar despues de `seo-audit` o `site-architecture` cuando haya paginas, breadcrumbs, negocio local, producto o FAQs que requieran datos estructurados.
- Riesgo: medio; puede derivar en cambios de produccion o schema enganoso, pero la skill bloquea contenido no visible, duplicados y publicacion sin Orden de Cambio.

### 2026-05-13 - .claude/skills/ai-seo/
- Area: sistema E-SELEC v2 / AI search
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `ai-seo` como skill v2 para auditar visibilidad AI y planificar contenido citable con evidencia.
- Estado: vigente
- Reemplaza a: `.agents/skills/ai-seo/` como skill legacy directa.
- Accion recomendada: usar para AI Search / LLM SEO despues de revisar fundamentos SEO, schema y arquitectura.
- Riesgo: medio; puede generar promesas falsas o cambios de crawling si no se exige evidencia y Orden de Cambio.

### 2026-05-13 - .claude/skills/content-strategy/
- Area: sistema E-SELEC v2 / contenido
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `content-strategy` como skill v2 para planificar pilares, clusters, temas y calendario editorial priorizado.
- Estado: vigente
- Reemplaza a: `.agents/skills/content-strategy/` como skill legacy directa.
- Accion recomendada: usar despues de SEO/AI SEO o al definir roadmap editorial por cliente.
- Riesgo: bajo-medio; puede generar contenido generico si no se exige evidencia y conexion con servicios reales.

### 2026-05-13 - .claude/skills/copywriting/
- Area: sistema E-SELEC v2 / copy comercial
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `copywriting` como skill v2 para escribir copy claro, especifico y verificable.
- Estado: vigente
- Reemplaza a: `.agents/skills/copywriting/` como skill legacy directa.
- Accion recomendada: usar despues de estrategia, CRO o briefing cuando haga falta texto final o variantes de copy.
- Riesgo: bajo-medio; puede inventar claims si no se exige prueba, por eso queda bloqueado sin oferta, audiencia y accion primaria.

### 2026-05-13 - .claude/skills/copy-editing/
- Area: sistema E-SELEC v2 / revision de copy
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `copy-editing` como skill v2 para revisar copy existente y pulirlo sin cambiar el mensaje central.
- Estado: vigente
- Reemplaza a: `.agents/skills/copy-editing/` como skill legacy directa.
- Accion recomendada: usar despues de `copywriting` o antes de entregar textos al cliente/publicar.
- Riesgo: bajo-medio; puede mantener claims sin prueba si no se revisan fuentes, por eso clasifica claims y bloquea publicacion sin aprobacion.

### 2026-05-13 - .claude/skills/page-cro/
- Area: sistema E-SELEC v2 / CRO
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `page-cro` como skill v2 para auditar paginas completas y priorizar mejoras de conversion.
- Estado: vigente
- Reemplaza a: `.agents/skills/page-cro/` como skill legacy directa.
- Accion recomendada: usar antes de reescribir, rediseniar o testear paginas de marketing.
- Riesgo: medio; puede proponer cambios de produccion o tests sin datos si no se exige medicion y Orden de Cambio.

### 2026-05-13 - .claude/skills/form-cro/
- Area: sistema E-SELEC v2 / CRO
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `form-cro` como skill v2 para auditar formularios, campos, errores, privacidad, mobile y medicion sin tocar produccion.
- Estado: vigente
- Reemplaza a: `.agents/skills/form-cro/` como skill legacy directa.
- Accion recomendada: usar despues de revisar la pagina o cuando el cuello de botella sea el formulario.
- Riesgo: medio; puede afectar CRM, tracking o captacion de datos si se ejecutan cambios sin Orden de Cambio.

### 2026-05-13 - .claude/skills/ab-test-setup/
- Area: sistema E-SELEC v2 / CRO y experimentacion
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `ab-test-setup` como skill v2 para convertir hipotesis en experimentos medibles, viables y con criterio de decision.
- Estado: vigente
- Reemplaza a: `.agents/skills/ab-test-setup/` como skill legacy directa.
- Accion recomendada: usar cuando una recomendacion CRO requiera prueba y existan datos/trafico suficientes.
- Riesgo: medio; puede producir decisiones falsas si se ignoran muestra, baseline, tracking o duracion minima.

### 2026-05-13 - .claude/skills/signup-flow-cro/
- Area: sistema E-SELEC v2 / CRO
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `signup-flow-cro` como skill v2 para auditar registros, altas de cuenta y trials sin tocar produccion.
- Estado: vigente
- Reemplaza a: `.agents/skills/signup-flow-cro/` como skill legacy directa.
- Accion recomendada: usar antes de cambiar flujos de registro, trials, auth, SSO, verificacion o pasos de alta.
- Riesgo: medio; puede afectar auth, pagos, email, CRM o producto si se ejecuta sin Orden de Cambio.

### 2026-05-13 - .claude/skills/onboarding-cro/
- Area: sistema E-SELEC v2 / CRO y activacion
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `onboarding-cro` como skill v2 para auditar activacion, primer valor y onboarding post-signup sin tocar produccion.
- Estado: vigente
- Reemplaza a: `.agents/skills/onboarding-cro/` como skill legacy directa.
- Accion recomendada: usar cuando usuarios se registran pero no llegan a valor, setup o retencion temprana.
- Riesgo: medio; puede afectar producto, emails, tracking o datos de usuario si se ejecuta sin Orden de Cambio.

### 2026-05-13 - .claude/skills/popup-cro/
- Area: sistema E-SELEC v2 / CRO
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `popup-cro` como skill v2 para auditar popups, modals, overlays y banners sin danar UX, SEO movil ni privacidad.
- Estado: vigente
- Reemplaza a: `.agents/skills/popup-cro/` como skill legacy directa.
- Accion recomendada: usar antes de crear, cambiar o probar popups, banners, exit intent o lead capture overlays.
- Riesgo: medio; puede afectar UX, privacidad, SEO movil, scripts y conversiones si se ejecuta sin Orden de Cambio.

### 2026-05-13 - .claude/skills/paywall-upgrade-cro/
- Area: sistema E-SELEC v2 / CRO y monetizacion
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `paywall-upgrade-cro` como skill v2 para auditar paywalls, upsells y upgrades con guardrails de revenue, confianza y churn.
- Estado: vigente
- Reemplaza a: `.agents/skills/paywall-upgrade-cro/` como skill legacy directa.
- Accion recomendada: usar antes de modificar paywalls, feature gates, trial expiration, usage limits, pricing in-app o upsell modals.
- Riesgo: medio-alto; puede afectar pricing, checkout, billing, producto, revenue o confianza si se ejecuta sin Orden de Cambio.

### 2026-05-13 - .claude/skills/paid-ads/
- Area: sistema E-SELEC v2 / SEM y paid media
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `paid-ads` como skill v2 para planificar o auditar campanas pagadas con tracking, presupuesto, estructura y riesgos.
- Estado: vigente
- Reemplaza a: `.agents/skills/paid-ads/` como skill legacy directa.
- Accion recomendada: usar antes de lanzar, reestructurar, escalar, pausar o invertir en campanas pagadas.
- Riesgo: alto; puede afectar gasto, conversiones, pixels, billing y cuentas publicitarias si se ejecuta sin Orden de Cambio.

### 2026-05-13 - .claude/skills/ad-creative/
- Area: sistema E-SELEC v2 / creatividad publicitaria
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `ad-creative` como skill v2 para generar o iterar anuncios con limites de plataforma, claims verificables y plan de test.
- Estado: vigente
- Reemplaza a: `.agents/skills/ad-creative/` como skill legacy directa.
- Accion recomendada: usar despues de definir campana con `paid-ads` o cuando haga falta creatividad validada para Ads.
- Riesgo: medio; puede crear claims falsos, anuncios fuera de specs o piezas no aprobables si no valida plataforma y fuentes.

### 2026-05-13 - .claude/skills/social-content/
- Area: sistema E-SELEC v2 / social
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `social-content` como skill v2 para crear piezas, calendarios y repurposing por canal, audiencia, tono y objetivo.
- Estado: vigente
- Reemplaza a: `.agents/skills/social-content/` como skill legacy directa.
- Accion recomendada: usar para contenido social despues de definir objetivo y tono; no publicar sin aprobacion.
- Riesgo: medio; puede publicar claims, tono incorrecto o contenido visible no aprobado si se ejecuta sin Orden de Cambio.

### 2026-05-13 - .claude/skills/programmatic-seo/
- Area: sistema E-SELEC v2 / SEO
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `programmatic-seo` como skill v2 para planificar paginas SEO a escala con datos, template, arquitectura e indexacion.
- Estado: vigente
- Reemplaza a: `.agents/skills/programmatic-seo/` como skill legacy directa.
- Accion recomendada: usar antes de crear paginas a escala, directorios, location pages, integraciones o comparativas masivas.
- Riesgo: alto; puede afectar indexacion, crawl budget, arquitectura y reputacion SEO si se ejecuta sin Orden de Cambio.

### 2026-05-13 - .claude/skills/competitor-alternatives/
- Area: sistema E-SELEC v2 / SEO y sales enablement
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `competitor-alternatives` como skill v2 para planificar paginas comparativas honestas, verificables y posicionables.
- Estado: vigente
- Reemplaza a: `.agents/skills/competitor-alternatives/` como skill legacy directa.
- Accion recomendada: usar para alternatives/vs pages solo con fuentes fechadas y revision comercial/legal cuando aplique.
- Riesgo: medio-alto; puede afectar marca, legal, SEO y confianza si se publican datos falsos.

### 2026-05-13 - eselec-agent-system-v2/.claude/skills/cold-email/
- Area: sistema E-SELEC v2 / ventas
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `cold-email` para escribir outreach frio humano, breve y verificable sin enviar emails.
- Estado: vigente
- Reemplaza a: `.agents/skills/cold-email/` como skill legacy directa.
- Accion recomendada: usar para borradores de prospeccion; cualquier envio real requiere Orden de Cambio.
- Riesgo: medio-alto; puede afectar reputacion y cumplimiento si se envia sin aprobacion.

### 2026-05-13 - eselec-agent-system-v2/.claude/skills/email-sequence/
- Area: sistema E-SELEC v2 / lifecycle email
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `email-sequence` para disenar secuencias con trigger, consentimiento, cadencia, salida y metricas.
- Estado: vigente
- Reemplaza a: `.agents/skills/email-sequence/` como skill legacy directa.
- Accion recomendada: usar para planificar sequences; activar automatizaciones requiere Orden de Cambio.
- Riesgo: medio-alto; puede afectar consentimiento, entregabilidad y experiencia si se ejecuta sin aprobacion.

### 2026-05-13 - eselec-agent-system-v2/.claude/skills/lead-magnets/
- Area: sistema E-SELEC v2 / captacion
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `lead-magnets` para planificar recursos de captacion con gating, entrega, nurture y medicion.
- Estado: vigente
- Reemplaza a: `.agents/skills/lead-magnets/` como skill legacy directa.
- Accion recomendada: usar antes de crear formularios, landings o capturas reales.
- Riesgo: medio; puede captar datos o prometer recursos no entregados si se ejecuta sin control.

### 2026-05-13 - eselec-agent-system-v2/.claude/skills/sales-enablement/
- Area: sistema E-SELEC v2 / ventas
- Agente: Codex + Arquitecto
- Tipo: skill Claude Code + command
- Motivo: migrar `sales-enablement` para crear materiales comerciales por persona, etapa, objecion, prueba y CTA.
- Estado: vigente
- Reemplaza a: `.agents/skills/sales-enablement/` como skill legacy directa.
- Accion recomendada: usar para decks, one-pagers, propuestas y playbooks; envio externo requiere aprobacion.
- Riesgo: medio-alto; puede usar pricing, claims o propuestas no aprobadas si no se revisa.

### 2026-05-13 - .claude/skills/pricing-strategy/ + revops/churn/referral
- Area: sistema E-SELEC v2 / negocio y retencion
- Agente: Codex + Arquitecto
- Tipo: skills Claude Code + commands
- Motivo: migrar `pricing-strategy`, `revops`, `churn-prevention` y `referral-program` como bloque de decisiones sensibles de negocio.
- Estado: vigente
- Reemplaza a: `.agents/skills/pricing-strategy/`, `.agents/skills/revops/`, `.agents/skills/churn-prevention/`, `.agents/skills/referral-program/`.
- Accion recomendada: usar para planes y especificaciones; cualquier cambio real de precios, CRM, billing, programas o pagos requiere Orden de Cambio.
- Riesgo: alto; puede afectar ingresos, pipeline, billing, churn, cumplimiento y confianza si se ejecuta sin aprobacion.

### 2026-05-13 - .claude/skills/launch-strategy/ + free-tool/ideas/psychology/context
- Area: sistema E-SELEC v2 / lanzamiento, crecimiento y posicionamiento
- Agente: Codex + Arquitecto
- Tipo: skills Claude Code + commands
- Motivo: migrar `launch-strategy`, `free-tool-strategy`, `marketing-ideas`, `marketing-psychology` y `product-marketing-context` como bloque de crecimiento y contexto comercial.
- Estado: vigente
- Reemplaza a: `.agents/skills/launch-strategy/`, `.agents/skills/free-tool-strategy/`, `.agents/skills/marketing-ideas/`, `.agents/skills/marketing-psychology/`, `.agents/skills/product-marketing-context/`.
- Accion recomendada: usar para planificar crecimiento, lanzamientos y contexto antes de ejecutar canales reales; escritura de contexto o acciones externas requiere control de artefactos u Orden de Cambio segun aplique.
- Riesgo: medio-alto; puede afectar posicionamiento, marca, captacion, promesas comerciales, privacidad y calidad de outputs si se usa sin fuentes reales.

### 2026-05-13 - .claude/skills/humanizalo/ + prompt-master/kling-producer
- Area: sistema E-SELEC v2 / contenido, prompts y media AI
- Agente: Codex + Arquitecto
- Tipo: skills Claude Code + commands
- Motivo: migrar `humanizalo`, `prompt-master` y `kling-producer` como utilidades de produccion con contratos de calidad y aprobacion antes de ejecucion externa.
- Estado: vigente
- Reemplaza a: `.agents/skills/humanizalo/`, `.agents/skills/prompt-master/`, `.agents/skills/kling-producer/`.
- Accion recomendada: usar para mejorar textos, crear prompts o planificar videos; ejecucion en herramientas externas, consumo de creditos o escritura de outputs requiere aprobacion/control de artefactos.
- Riesgo: medio; puede cambiar sentido de claims, crear instrucciones inseguras o consumir creditos si se usa sin revision.

### 2026-05-13 - .claude/skills/folder-cleanup/ + web-feedback/woocommerce
- Area: sistema E-SELEC v2 / operaciones, web y ecommerce
- Agente: Codex + Arquitecto
- Tipo: skills Claude Code + commands
- Motivo: migrar `folder-cleanup`, `web-feedback-loop` y `woocommerce-setup` como skills operativas con controles estrictos antes de mover archivos, tocar web o modificar WooCommerce.
- Estado: vigente
- Reemplaza a: `.agents/skills/folder-cleanup/`, `.agents/skills/web-feedback-loop/`, `.agents/skills/woocommerce-setup/`.
- Accion recomendada: usar primero en modo auditoria/propuesta; ejecucion real requiere aprobacion, Orden de Cambio o control de artefactos segun el activo afectado.
- Riesgo: alto; puede afectar archivos de cliente, web publicada, checkout, pagos, envios, impuestos, productos, legales y secretos.

### 2026-05-13 - planning/backlog-migracion.md P3-003
- Area: sistema E-SELEC v2 / migracion
- Agente: Codex + Arquitecto
- Tipo: registro / backlog
- Motivo: cerrar formalmente P3-003 tras verificar que todas las skills legacy tienen equivalente en `.claude/skills/`.
- Estado: vigente
- Reemplaza a: estado `en curso` de P3-003.
- Accion recomendada: continuar con P3-004 agentes especialistas y P3-005 conectores/scripts.
- Riesgo: bajo; marca de estado, no cambia comportamiento operativo.

### 2026-05-13 - planning/inventario-agentes-legacy.md
- Area: sistema E-SELEC v2 / migracion de agentes
- Agente: Codex + Arquitecto
- Tipo: inventario / plan
- Motivo: ordenar P3-004 antes de migrar agentes especialistas y evitar copiar referencias/aprendizajes como agentes ejecutables.
- Estado: vigente
- Reemplaza a: ninguno.
- Accion recomendada: usar como mapa de P3-004.
- Riesgo: bajo-medio; si queda desactualizado, el plan de agentes puede desviarse.

### 2026-05-13 - .claude/agents/*-leader.md Equipo Clientes
- Area: sistema E-SELEC v2 / agentes clientes
- Agente: Codex + Arquitecto
- Tipo: subagents Claude Code
- Motivo: migrar lideres SEO, CRO, SEM, Social, Reports y Web como orquestadores v2 con routing a skills y controles de produccion.
- Estado: vigente
- Reemplaza a: `agents/seo/leader-seo.md`, `agents/cro/leader-cro.md`, `agents/sem/leader-sem.md`, `agents/social/leader-social.md`, `agents/reports/leader-reports.md`, `agents/web/leader-web.md`.
- Accion recomendada: usar desde `leader-clientes` para coordinar tareas por area.
- Riesgo: medio; mala ruta puede activar skill incorrecta, pero no ejecutan produccion por defecto.

### 2026-05-13 - .claude/agents/seo-*.md + cro-*.md + sem-*.md
- Area: sistema E-SELEC v2 / agentes clientes
- Agente: Codex + Arquitecto
- Tipo: subagents Claude Code
- Motivo: migrar especialistas SEO, CRO y SEM como agentes v2 breves, conectados a skills y protocolos.
- Estado: vigente
- Reemplaza a: `agents/seo/seo-*.md`, `agents/cro/cro-*.md`, `agents/sem/sem-*.md` como prompts legacy directos.
- Accion recomendada: usar desde los lideres `seo-leader`, `cro-leader` y `sem-leader`.
- Riesgo: medio-alto; influyen prioridades tecnicas, conversion y Ads, pero no ejecutan produccion sin Orden de Cambio.

### 2026-05-13 - .claude/agents/social-*.md + reports-*.md + web-*.md
- Area: sistema E-SELEC v2 / agentes clientes
- Agente: Codex + Arquitecto
- Tipo: subagents Claude Code
- Motivo: migrar especialistas Social, Reports y Web como agentes v2 breves, conectados a skills y protocolos.
- Estado: vigente
- Reemplaza a: `agents/social/social-*.md`, `agents/reports/reports-*.md`, `agents/web/web-*.md` como prompts legacy directos.
- Accion recomendada: usar desde los lideres `social-leader`, `reports-leader` y `web-leader`.
- Riesgo: medio-alto; afecta comunicacion publica, informes y web, pero no ejecuta produccion sin aprobacion.

### 2026-05-13 - .claude/agents/agency-*.md
- Area: sistema E-SELEC v2 / agentes agencia
- Agente: Codex + Arquitecto
- Tipo: subagents Claude Code
- Motivo: migrar especialistas internos de captacion, reputacion, onboarding, retencion y finanzas.
- Estado: vigente
- Reemplaza a: `agents/agency/agency-*.md` como prompts legacy directos.
- Accion recomendada: usar desde `leader-agencia`.
- Riesgo: medio; afecta decisiones internas de negocio, captacion y pricing, pero no ejecuta acciones externas sin aprobacion.

### 2026-05-13 - .claude/agents/gobernanza-y-loops
- Area: sistema E-SELEC v2 / gobernanza
- Agente: Codex + Arquitecto
- Tipo: subagents Claude Code
- Motivo: migrar roles legacy de conciencia organizacional, regeneracion estructural, aprendizaje de Rodrigo y ciclos recurrentes.
- Estado: vigente
- Reemplaza a: `agents/arquitecto/arquitecto.md`, `agents/fenix/fenix.md`, `agents/calibracion/calibracion.md`, `agents/loops/leader-loops.md`.
- Accion recomendada: usar desde `leader-clientes`, `leader-agencia` y comandos LOOP.
- Riesgo: medio; afecta arquitectura, memoria y loops, pero no ejecuta produccion sin aprobacion.

### 2026-05-13 - planning/inventario-conectores-scripts.md
- Area: sistema E-SELEC v2 / conectores
- Agente: Codex + Arquitecto
- Tipo: inventario de migracion
- Motivo: iniciar P3-005 separando scripts migrables, deferidos y bloqueados antes de copiar codigo con accesos.
- Estado: vigente
- Reemplaza a: lectura dispersa de `planning/auditoria-scripts-sensibles.md` para P3-005.
- Accion recomendada: usar como mapa de decisiones para migrar scripts v2.
- Riesgo: bajo-medio; documento de control que evita mover conectores sensibles sin saneamiento.

### 2026-05-13 - scripts/protocol_guard.py + .mcp.example.json
- Area: sistema E-SELEC v2 / scripts y MCP
- Agente: Codex + Arquitecto
- Tipo: script defensivo / configuracion de ejemplo
- Motivo: migrar el guard de cierre adaptado a rutas v2 y crear ejemplo MCP seguro sin valores reales.
- Estado: vigente
- Archivos creados/modificados: `scripts/protocol_guard.py`, `.mcp.example.json`, `.gitignore`, `scripts/README.md`, `registries/registro-migracion.md`, `registries/registro-artefactos.md`.
- Reemplaza a: uso del guard legacy para cierres del repo v2.
- Accion recomendada: ejecutar `python scripts/protocol_guard.py` antes de cerrar tareas con cambios en v2.
- Riesgo: medio; revisa archivos y escribe reporte local ignorado, sin conectar servicios externos.

### 2026-05-13 - planning/cierre-migracion-v2.md
- Area: sistema E-SELEC v2 / cierre operativo
- Agente: Codex + Arquitecto
- Tipo: manual de arranque / cierre de migracion
- Motivo: dejar una guia clara de estado final, arranque, reglas no negociables y conectores deferidos.
- Estado: vigente
- Archivos creados/modificados: `planning/cierre-migracion-v2.md`, `README.md`, `registries/registro-migracion.md`, `registries/registro-artefactos.md`.
- Reemplaza a: cierre disperso en logs y backlog.
- Accion recomendada: leer antes de iniciar trabajo real en v2.
- Riesgo: bajo; documento operativo sin accesos ni produccion.

### 2026-05-13 - planning/validacion-operativa-v2.md
- Area: sistema E-SELEC v2 / validacion
- Agente: Codex + Arquitecto
- Tipo: validacion operativa
- Motivo: comprobar que backlog, agentes, skills, commands, protocolos y guard quedan listos para primer uso operativo.
- Estado: vigente
- Archivos creados/modificados: `planning/validacion-operativa-v2.md`, `planning/cierre-migracion-v2.md`, `planning/inventario-agentes-legacy.md`, `.claude/agents/arquitecto-migracion-claude.md`, `registries/registro-migracion.md`, `registries/registro-artefactos.md`.
- Reemplaza a: ninguno.
- Accion recomendada: usar como evidencia de que v2 esta listo para operar.
- Riesgo: bajo; validacion y ajuste de frontmatter sin produccion.

### 2026-05-13 - planning/sprint-01-operacion-v2.md
- Area: sistema E-SELEC v2 / operacion
- Agente: Codex + Arquitecto
- Tipo: sprint operativo
- Motivo: definir el primer ciclo de uso real del sistema v2 despues de cerrar migracion.
- Estado: vigente
- Archivos creados/modificados: `planning/sprint-01-operacion-v2.md`, `README.md`, `registries/registro-migracion.md`, `registries/registro-artefactos.md`.
- Reemplaza a: ninguno.
- Accion recomendada: ejecutar O1-001 con `computer-chamberi` antes de activar otros clientes.
- Riesgo: bajo; plan de lectura y priorizacion, sin produccion ni accesos.

### 2026-05-13 - clients/computer-chamberi/outputs/auditoria-arranque-v2-2026-05-13.md
- Area: cliente computer-chamberi / arranque operativo v2
- Agente: Codex + leader-clientes
- Tipo: auditoria de cliente
- Motivo: ejecutar O1-001 en modo lectura para probar primer arranque real del sistema v2.
- Estado: vigente
- Archivos creados/modificados: `clients/computer-chamberi/outputs/auditoria-arranque-v2-2026-05-13.md`, `clients/computer-chamberi/outputs/manifest.md`, `clients/computer-chamberi/log.md`, `planning/sprint-01-operacion-v2.md`.
- Reemplaza a: ninguno.
- Accion recomendada: usar como punto de partida para verificacion de medicion segura.
- Riesgo: bajo; no toca produccion ni accesos, diagnostico parcial fuerte.

### 2026-05-13 - agency/outputs/arranque-agencia-v2-2026-05-13.md
- Area: agencia E-SELEC / arranque operativo v2
- Agente: Codex + leader-agencia
- Tipo: output interno de agencia
- Motivo: ejecutar O1-002 en modo lectura para probar el primer arranque interno de Agencia y detectar prioridad operativa sin mezclar clientes.
- Estado: vigente
- Archivos creados/modificados: `agency/outputs/arranque-agencia-v2-2026-05-13.md`, `agency/outputs/manifest.md`, `agency/log.md`, `planning/sprint-01-operacion-v2.md`.
- Reemplaza a: ninguno.
- Accion recomendada: actualizar `agency/context.md` para reflejar estado post-migracion y luego ejecutar O1-003 en modo lectura.
- Riesgo: bajo; no toca produccion, conectores, accesos ni datos vivos.

### 2026-05-13 - agency/context.md actualizacion post-O1-002
- Area: agencia E-SELEC / contexto operativo
- Agente: Codex + Arquitecto
- Tipo: fuente de verdad interna
- Motivo: corregir el contexto interno tras O1-002 para que Agencia deje de priorizar migracion base ya cerrada y pase a Sprint 01 operativo.
- Estado: vigente
- Archivos creados/modificados: `agency/context.md`, `agency/log.md`, `registries/registro-artefactos.md`.
- Reemplaza a: estado interno que marcaba areas, skills y agentes como pendientes de migracion.
- Accion recomendada: usar este contexto antes de O1-003 y decisiones internas de Agencia.
- Riesgo: bajo; documentacion interna sin produccion ni accesos.

### 2026-05-13 - agency/outputs/resumen-semanal-2026-05-13.md
- Area: agencia E-SELEC / loops
- Agente: Codex + loops-leader
- Tipo: output interno de auditoria semanal
- Motivo: ejecutar O1-003 en modo lectura para comprobar estado multi-cliente v2 sin modificar archivos de cliente ni tocar produccion.
- Estado: vigente
- Archivos creados/modificados: `agency/outputs/resumen-semanal-2026-05-13.md`, `agency/outputs/manifest.md`, `agency/log.md`, `agency/loops-activos.md`, `planning/sprint-01-operacion-v2.md`, `registries/registro-artefactos.md`.
- Reemplaza a: ninguno.
- Accion recomendada: usar para decidir O1-004 Calibracion y no migrar mas clientes hasta cerrar el sprint.
- Riesgo: bajo; output interno, sin datos vivos, accesos ni produccion.

### 2026-05-13 - agency/outputs/calibracion-o1-004-2026-05-13.md
- Area: agencia E-SELEC / calibracion
- Agente: Codex + calibracion
- Tipo: output interno de prueba de calibracion
- Motivo: ejecutar O1-004 para verificar que Calibracion distingue duplicados, preferencias nuevas y escritura pendiente de aprobacion.
- Estado: vigente
- Archivos creados/modificados: `agency/outputs/calibracion-o1-004-2026-05-13.md`, `agency/outputs/manifest.md`, `agency/log.md`, `planning/sprint-01-operacion-v2.md`, `registries/registro-artefactos.md`.
- Reemplaza a: ninguno.
- Accion recomendada: pedir aprobacion antes de escribir la preferencia propuesta en `agency/preferencias-rodrigo.md`.
- Riesgo: bajo; no modifica memoria permanente, produccion ni accesos.

### 2026-05-13 - planning/conector-seguro-01-gsc-lectura.md
- Area: sistema E-SELEC v2 / conectores
- Agente: Codex + Arquitecto
- Tipo: especificacion de conector seguro
- Motivo: ejecutar O1-005 eligiendo un primer conector a reconstruir sin implementar produccion ni usar credenciales.
- Estado: vigente
- Archivos creados/modificados: `planning/conector-seguro-01-gsc-lectura.md`, `agency/log.md`, `planning/sprint-01-operacion-v2.md`, `registries/registro-artefactos.md`.
- Reemplaza a: decision abierta sobre primer conector post-migracion.
- Accion recomendada: implementar solo con aprobacion, OAuth fuera del repo, dry-run por defecto y registro de accesos antes del primer uso real.
- Riesgo: bajo como especificacion; futuro token OAuth debe tratarse como S4.

### 2026-05-14 - agente de alineacion Claude Code
- Area: sistema E-SELEC v2 / control interno
- Agente: Codex
- Tipo: subagent + skill Claude Code / auditoria de alineacion
- Motivo: crear un control neutral que audite si el repo usa bien las primitivas oficiales de Claude Code sin contaminarse con diagnosticos previos del sistema.
- Estado: vigente
- Archivos creados/modificados: `.claude/agents/alineacion.md`, `.claude/skills/alignment-check/SKILL.md`, `.claude/skills/alignment-check/references/claude-code-spec.md`, `.claude/skills/alignment-check/references/fuentes-claude-code.md`, `.claude/skills/alignment-check/checklists/sistema-completo.md`, `.claude/skills/alignment-check/templates/hallazgo.md`, `.claude/skills/alignment-check/templates/reporte-alineacion.md`, `.claude/settings.json`, `registries/registro-artefactos.md`.
- Reemplaza a: ninguno; convierte la idea del control de alineacion en una pieza auditable y no ejecutora.
- Accion recomendada: usar `alineacion` para generar una matriz aceptar/revisar/posponer antes de borrar commands, fusionar agentes o reducir contexto.
- Riesgo: bajo; no toca produccion, secretos, conectores ni clientes. El agente opera en `permissionMode: plan` y no edita archivos.
- Nota: `.claude/settings.json` queda incluido solo para conservar la correccion local de Claude Code (`defaultMode` invalido a `default`) y permitir que el repo abra sin error.

### 2026-05-15 - biblioteca oficial local para alineacion
- Area: sistema E-SELEC v2 / control interno
- Agente: Codex
- Tipo: fuentes oficiales scrapeadas + reglas de auditoria
- Motivo: hacer que el agente `alineacion` lea documentacion oficial local de Claude Code antes de emitir hallazgos fuertes o recomendar cambios estructurales.
- Estado: vigente
- Archivos creados/modificados: `.claude/agents/alineacion.md`, `.claude/skills/alignment-check/SKILL.md`, `.claude/skills/alignment-check/scripts/scrape_claude_docs.py`, `.claude/skills/alignment-check/references/fuentes-claude-code.md`, `.claude/skills/alignment-check/references/indice-tematico.md`, `.claude/skills/alignment-check/references/claude-code-spec.md`, `.claude/skills/alignment-check/references/claude-docs/`, `.claude/skills/alignment-check/checklists/sistema-completo.md`, `.claude/skills/alignment-check/checklists/observacion-sesion.md`, `.claude/skills/alignment-check/templates/hallazgo.md`, `.claude/skills/alignment-check/templates/reporte-alineacion.md`, `scripts/protocol_guard.py`, `registries/registro-artefactos.md`.
- Reemplaza a: uso de resumen operativo sin biblioteca local completa.
- Accion recomendada: en auditorias profundas, leer `references/claude-docs/manifest.md` e `indice-tematico.md` antes de revisar el repo; para hallazgos altos/criticos, citar fuente local leida.
- Riesgo: bajo-medio; aumenta tamano del repo con copias Markdown oficiales, pero evita dependencia de memoria o reportes previos. No toca produccion, secretos ni conectores. `protocol_guard.py` se ajusta para reconocer carpetas registradas como cobertura de sus archivos hijos.
- Nota: el scraper usa fallback oficial en ingles cuando una URL espanola no entrega Markdown valido; el agente trabaja y responde en espanol.

### 2026-05-15 - evidencia obligatoria en alineacion
- Area: sistema E-SELEC v2 / control interno
- Agente: Codex
- Tipo: ajuste de agente + skill / calidad de auditoria
- Motivo: corregir el fallo detectado en la primera auditoria de `alineacion`, donde se afirmaron conteos sin mostrar evidencia operativa del filesystem.
- Estado: vigente
- Archivos creados/modificados: `.claude/agents/alineacion.md`, `.claude/skills/alignment-check/SKILL.md`, `.claude/skills/alignment-check/checklists/sistema-completo.md`, `.claude/skills/alignment-check/templates/hallazgo.md`, `.claude/skills/alignment-check/templates/reporte-alineacion.md`, `registries/registro-artefactos.md`.
- Reemplaza a: reglas de inventario demasiado debiles que permitian confundir README/reportes con realidad del repo.
- Accion recomendada: en cualquier auditoria futura, exigir `EVIDENCIA OPERATIVA` con comando, resultado y alcance antes de aceptar conteos o ausencias como hechos.
- Riesgo: bajo; solo cambia instrucciones del auditor, no toca produccion, secretos, conectores ni clientes.

### 2026-05-16 - seo-canon legacy docente SEO
- Area: sistema E-SELEC v2 / SEO
- Agente: Codex + criterios de alineacion
- Tipo: skill + referencias historicas intactas
- Motivo: conectar el Docente SEO legacy y su canon operativo al sistema Claude Code v2 sin crear otro agente docente ni resumir el canon que funcionaba bien.
- Estado: vigente
- Archivos creados/modificados: `.claude/skills/seo-canon/`, `.claude/skills/seo-audit/SKILL.md`, `.claude/skills/README.md`, `.claude/agents/README.md`, `.claude/agents/seo-leader.md`, `.claude/agents/seo-organico.md`, `.claude/agents/seo-tecnico.md`, `.claude/agents/seo-local.md`, `.claude/agents/seo-llms.md`, `.claude/agents/seo-web.md`, `registries/registro-artefactos.md`.
- Reemplaza a: agentes SEO v2 que operaban mayormente como routing sin una capa canonica compartida del Docente SEO legacy.
- Accion recomendada: usar `seo-canon` como criterio bajo demanda antes de auditorias SEO profundas, caidas de trafico, arquitectura, migraciones, canibalizacion o reconstruccion de agentes SEO.
- Riesgo: bajo; no toca produccion, secretos, conectores ni datos vivos. Aumenta tamano del repo con referencias historicas, pero preserva rollback y evita reescribir el canon.

### 2026-05-18 - indice completo seo-canon
- Area: sistema E-SELEC v2 / SEO
- Agente: Codex
- Tipo: indice operativo de canon
- Motivo: evitar que los 28 aprendizajes y 5 fuentes del Docente SEO legacy queden copiados pero no operativos dentro de `seo-canon`.
- Estado: vigente
- Archivos creados/modificados: `.claude/skills/seo-canon/references/indice-canon-seo.md`, `.claude/skills/seo-canon/SKILL.md`, `registries/registro-artefactos.md`.
- Reemplaza a: tabla parcial de lectura dentro de `seo-canon/SKILL.md` que no destacaba todos los modulos relevantes para agentes SEO.
- Accion recomendada: antes de tareas SEO profundas o reestructuracion de agentes SEO, consultar `references/indice-canon-seo.md` y declarar que archivos del canon se leyeron. Ajuste M-01 aplicado: `2026-05-09-refuerzo-links-manual-seo.md` queda visible en el indice.
- Riesgo: bajo; no modifica el canon, solo crea mapa de acceso y trazabilidad.

### 2026-05-18 - separacion caso real y canon SEO
- Area: sistema E-SELEC v2 / SEO
- Agente: Codex
- Tipo: saneamiento de canon + reubicacion de evidencia de cliente
- Motivo: evitar que un caso real de cliente viva dentro de una skill general y contamine el funcionamiento del canon SEO.
- Estado: vigente
- Archivos creados/modificados: `.claude/skills/seo-canon/SKILL.md`, `.claude/skills/seo-canon/references/indice-canon-seo.md`, `.claude/skills/seo-canon/references/patrones/patron-diagnostico-caida-seo-multidioma.md`, `clients/computer-chamberi/outputs/conversaciones/diagnostico-seo-2026-05-16.json`, `clients/computer-chamberi/outputs/manifest.md`, `registries/registro-artefactos.md`.
- Reemplaza a: referencia directa desde `seo-canon` a `computer-chamberi-diagnostico-2026-05-16.json`.
- Accion recomendada: mantener los casos reales en `clients/[cliente]/` y convertir solo aprendizajes reutilizables en patrones anonimos dentro de skills generales.
- Riesgo: bajo; no toca produccion, secretos ni conectores. El JSON real se conserva dentro del cliente y el canon queda generalizado.
- Nota adicional: el aprendizaje `2026-05-11-lectura-sistema-completo-previa-reestructuracion.md` queda anonimizado dentro del canon; la version historica con nombres de clientes se conserva fuera de la skill en `legacy/docente-seo-historico-con-clientes/`.

### 2026-05-18 - fase 1 limpieza de contaminacion
- Area: sistema E-SELEC v2 / migracion
- Agente: Codex + consulta Claude
- Tipo: saneamiento documental
- Motivo: separar referencias operativas reutilizables de historia de migracion con clientes reales.
- Estado: vigente
- Archivos creados/modificados: `planning/conector-seguro-01-gsc-lectura.md`, `planning/sprint-01-operacion-v2.md`, `planning/piloto-01.md`, `registries/registro-artefactos.md`.
- Reemplaza a: ejemplos de GSC con cliente y URL hardcodeados en una especificacion reutilizable; documentos de sprint/piloto sin marca clara de archivo historico.
- Accion recomendada: mantener `planning/` como historial cuando tenga clientes reales; si un documento se vuelve plantilla reutilizable, anonimizar ejemplos.
- Riesgo: bajo; no toca produccion, secretos, conectores ni datos vivos.

### 2026-05-18 - fase 2 migracion minima de clientes activos
- Area: clientes E-SELEC v2 / migracion
- Agente: Codex + consulta Claude
- Tipo: migracion documental minima
- Motivo: completar la presencia de clientes activos legacy dentro de `clients/` sin copiar outputs historicos, secretos ni archivos pesados.
- Estado: vigente
- Archivos creados/modificados: `clients/cashier-bubble-tea/`, `clients/la-bottega-del-gusto/`, `clients/stramondo-venezuela/`, `registries/registro-artefactos.md`.
- Reemplaza a: dependencia de leer esos clientes solo desde `../clients/` legacy.
- Accion recomendada: usar estos clientes en v2 solo tras leer `context.md`, `memory.md`, `log.md`, `mensajes.md`, `tasks.md` y `outputs/manifest.md`; si se necesita un output legacy, extraer evidencia saneada y registrar el nuevo archivo.
- Riesgo: medio; Bottega implica WordPress/WooCommerce y Stramondo Meta Ads, pero esta migracion no toca produccion, credenciales ni conectores.

### 2026-05-18 - fase 3 auditoria por areas
- Area: sistema E-SELEC v2 / agentes y skills
- Agente: Codex + consulta Claude
- Tipo: auditoria documental
- Motivo: determinar que areas pueden operar con skills procedurales y que areas requieren canon o skill dedicada, sin copiar automaticamente el patron SEO a todo el sistema.
- Estado: vigente
- Archivos creados/modificados: `planning/auditoria-agentes-skills-areas-2026-05-18.md`, `registries/registro-artefactos.md`.
- Reemplaza a: idea inicial de replicar `seo-canon` en todas las areas sin comprobar si el problema era de canon, skill dedicada o command wrapper.
- Accion recomendada: empezar por una skill dedicada de Reports, despues auditar SEM por riesgo operativo y luego revisar commands como wrappers finos.
- Riesgo: bajo; solo documenta evidencia y criterio. No toca produccion, secretos, conectores, agentes ni skills operativas.

### 2026-05-18 - fase 4 skill reports
- Area: sistema E-SELEC v2 / Reports
- Agente: Codex + consulta Claude
- Tipo: skill operativa + templates
- Motivo: resolver el gap detectado en Fase 3: Reports tenia agentes y contratos de calidad, pero no una skill dedicada que convirtiera datos, trabajo ejecutado y hallazgos en informes, alertas y proximos pasos.
- Estado: vigente
- Archivos creados/modificados: `.claude/skills/reports/`, `.claude/skills/README.md`, `.claude/agents/reports-leader.md`, `.claude/agents/reports-cliente.md`, `.claude/agents/reports-alertas.md`, `.claude/agents/reports-proxpasos.md`, `.claude/agents/README.md`, `registries/registro-artefactos.md`.
- Reemplaza a: rutas Reports dispersas entre `analytics-tracking`, `copy-editing`, `humanizalo` y `quality/criterios-output.md` sin procedimiento unico.
- Accion recomendada: usar `.claude/skills/reports/SKILL.md` como entrada principal para informe mensual, alerta y proximos pasos; usar `verificacion-medicion` cuando el output dependa de datos.
- Riesgo: bajo; no contiene informes reales de clientes ni toca produccion, secretos, conectores o fuentes vivas.
- Validacion: `quick_validate.py` no pudo ejecutarse por falta de `PyYAML` en el Python local; validacion manual limpia de frontmatter, TODOs, rutas y referencias.

### 2026-05-18 - fase 5 SEM / Paid Ads
- Area: sistema E-SELEC v2 / SEM
- Agente: Codex + consulta Claude / alineacion
- Tipo: refuerzo de skill y referencias bajo demanda
- Motivo: capturar reglas operativas de paid media sin crear un canon SEM innecesario ni contaminar la skill con casos reales de clientes.
- Estado: vigente
- Archivos creados/modificados: `.claude/skills/paid-ads/SKILL.md`, `.claude/skills/paid-ads/references/platform-guide.md`, `.claude/skills/paid-ads/references/platform-rules.md`, `planning/auditoria-sem-paid-ads-2026-05-18.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Reemplaza a: guia SEM demasiado breve para decisiones de riesgo sobre plataforma, tracking y lectura de eventos.
- Accion recomendada: usar `platform-rules.md` cuando se diagnostiquen campanas, tracking, calidad de leads, eventos de mensajeria, escala de presupuesto o eleccion de plataforma.
- Riesgo: bajo; no toca campanas, cuentas, presupuestos, secretos, conectores ni datos vivos.

### 2026-05-18 - fase 6 limpieza de contaminacion general
- Area: sistema E-SELEC v2 / comandos y loops
- Agente: Codex + consulta Claude / alineacion
- Tipo: saneamiento de ejemplos reutilizables
- Motivo: evitar que clientes reales aparezcan como ejemplos fijos en comandos generales o loops reutilizables.
- Estado: vigente
- Archivos creados/modificados: `.claude/commands/*.md` con ejemplos anonimizados, `.claude/commands/README.md`, `.claude/agents/loops-leader.md`, `planning/auditoria-contaminacion-general-2026-05-18.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Reemplaza a: ejemplos con `computer-chamberi`, `la-bottega-del-gusto`, `cashier-bubble-tea` y `stramondo-venezuela` dentro de commands generales.
- Accion recomendada: mantener nombres reales solo en `clients/`, `agency/`, `planning/` y `registries/` cuando actuen como memoria o trazabilidad; usar slugs inventados en instrucciones reutilizables.
- Riesgo: bajo; solo cambia documentacion operativa y no toca clientes, produccion, secretos ni conectores.

### 2026-05-18 - fase 7 mapa commands-skills-agents
- Area: sistema E-SELEC v2 / commands y skills
- Agente: Codex; consulta Claude intentada pero bloqueada por uso disponible
- Tipo: documentacion de arquitectura operativa
- Motivo: comprobar si habia duplicacion real entre commands, skills y agents, y aclarar que gobierna cada capa.
- Estado: vigente
- Archivos creados/modificados: `.claude/commands/README.md`, `planning/mapa-commands-skills-2026-05-18.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Reemplaza a: ambiguedad sobre si commands y skills duplican responsabilidad.
- Accion recomendada: mantener commands como entradas finas; mantener skills como fuente de procedimiento; mantener agents como roles/orquestadores.
- Riesgo: bajo; solo documentacion, sin produccion, secretos, clientes ni conectores.

### 2026-05-18 - fase 8 patron operativo de agentes
- Area: sistema E-SELEC v2 / arquitectura operativa
- Agente: Codex; consulta Claude no disponible por limite de uso en CLI
- Tipo: guia de decision estructural
- Motivo: explicar como replicar lo que funciono en SEO sin copiar SEO literalmente a todas las areas.
- Estado: vigente
- Archivos creados/modificados: `planning/patron-operativo-agentes-v2.md`, `README.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Reemplaza a: ambiguedad sobre cuando crear canon, skill, reference, command o agente.
- Accion recomendada: usar este patron antes de migrar nuevas piezas legacy o reestructurar areas como CRO, Web o Social.
- Riesgo: bajo; documentacion de arquitectura, sin produccion, secretos, clientes ni conectores.

### 2026-05-19 - fase 9 auditoria CRO/Web/Social
- Area: sistema E-SELEC v2 / CRO, Web y Social
- Agente: Codex + consulta Claude / alineacion
- Tipo: auditoria estructural + ajuste de routing
- Motivo: comprobar si CRO, Web y Social necesitaban canon propio o si bastaban sus skills procedurales actuales.
- Estado: vigente
- Archivos creados/modificados: `.claude/agents/social-leader.md`, `planning/auditoria-cro-web-social-2026-05-19.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Reemplaza a: idea de replicar automaticamente `seo-canon` en CRO, Web y Social.
- Accion recomendada: no crear canon CRO/Web/Social hasta observar fallos reales de output; si aparece un fallo, decidir entre mejorar skill, crear referencia, crear template, crear command o crear canon.
- Riesgo: bajo; no toca clientes, produccion, secretos, conectores ni datos vivos.

### 2026-05-19 - fase 11 contaminacion restante y contexto agencia
- Area: sistema E-SELEC v2 / memoria interna y contaminacion
- Agente: Codex + consulta Claude / alineacion
- Tipo: auditoria documental + sincronizacion de contexto
- Motivo: confirmar que los nombres reales de clientes no viven en primitivas reutilizables y corregir estado obsoleto de clientes migrados en `agency/context.md`.
- Estado: vigente
- Archivos creados/modificados: `agency/context.md`, `agency/log.md`, `planning/auditoria-contaminacion-restante-2026-05-19.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Reemplaza a: estados obsoletos que marcaban clientes activos como pendientes de migrar v2.
- Accion recomendada: permitir nombres reales en `agency/` como memoria interna; mantener `.claude/agents`, `.claude/skills`, `.claude/commands` y `.claude/rules` sin clientes reales salvo que sea una referencia historica justificada.
- Riesgo: bajo; no toca produccion, secretos, conectores ni outputs de clientes.

### 2026-05-19 - fase 12 homologacion Computer Chamberi
- Area: clientes E-SELEC v2 / Computer Chamberi
- Agente: Codex + consulta Claude / alineacion
- Tipo: homologacion de cliente piloto
- Motivo: confirmar que el cliente piloto puede operar en v2 sin reescribir su contexto ni mezclar memoria historica con instrucciones generales.
- Estado: vigente
- Archivos creados/modificados: `clients/computer-chamberi/outputs/homologacion-v2-2026-05-19.md`, `clients/computer-chamberi/outputs/manifest.md`, `clients/computer-chamberi/log.md`, `clients/computer-chamberi/tasks.md`, `planning/homologacion-clientes-activos-2026-05-19.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Reemplaza a: tarea pendiente generica de `client-audit v2` para el cliente piloto.
- Accion recomendada: verificar medicion y linea base SEO/tecnica antes de auditoria SEO final, CRO o informes.
- Riesgo: bajo; solo documentacion interna del cliente, sin produccion, secretos ni conectores.

### 2026-05-19 - fase 13 homologacion Chashier Bubble Tea
- Area: clientes E-SELEC v2 / Chashier Bubble Tea
- Agente: Codex + consulta Claude / alineacion
- Tipo: homologacion de cliente activo
- Motivo: sincronizar tareas del cliente con acciones ya probadas en `log.md` y evitar que futuros agentes repitan trabajo hecho.
- Estado: vigente
- Archivos creados/modificados: `clients/cashier-bubble-tea/outputs/homologacion-v2-2026-05-19.md`, `clients/cashier-bubble-tea/outputs/manifest.md`, `clients/cashier-bubble-tea/log.md`, `clients/cashier-bubble-tea/tasks.md`, `planning/homologacion-clientes-activos-2026-05-19.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Reemplaza a: tareas obsoletas que seguian marcando como pendiente preparar informe de 2 anos y resolver canonical en WordPress.
- Accion recomendada: confirmar envio/uso del informe y preparar propuesta Ano 3; mantener GSC/GA4/GBP, disavow y CWV como pendientes sensibles.
- Riesgo: bajo; solo documentacion interna del cliente, sin produccion, secretos ni conectores.

### 2026-05-19 - fase 14 homologacion La Bottega del Gusto
- Area: clientes E-SELEC v2 / La Bottega del Gusto
- Agente: Codex + consulta Claude / alineacion
- Tipo: homologacion de cliente activo sensible
- Motivo: confirmar que Bottega opera en v2 sin reescribir tareas utiles ni tocar produccion, corrigiendo solo un dato obsoleto de catalogo antes de nuevos trabajos.
- Estado: vigente
- Archivos creados/modificados: `clients/la-bottega-del-gusto/outputs/homologacion-v2-2026-05-19.md`, `clients/la-bottega-del-gusto/outputs/manifest.md`, `clients/la-bottega-del-gusto/context.md`, `clients/la-bottega-del-gusto/log.md`, `planning/homologacion-clientes-activos-2026-05-19.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Reemplaza a: conteo obsoleto de 75 productos sin imagen en `context.md`.
- Accion recomendada: antes de tocar WordPress/WooCommerce, pagos, envios, impuestos, accesos o checkout, abrir Orden de Cambio y cerrar bloqueadores de go-live.
- Riesgo: medio documental; no toca produccion, secretos ni conectores, pero el cliente es operativo y sensible.

### 2026-05-19 - fase 15 homologacion Stramondo Venezuela
- Area: clientes E-SELEC v2 / Stramondo Venezuela
- Agente: Codex + consulta Claude / alineacion
- Tipo: homologacion de cliente activo sensible
- Motivo: corregir inconsistencias documentales sobre Meta Ads para evitar que futuros agentes actuen como si la campaña B2B siguiera activa cuando el ultimo dato confirmado la marca `PAUSED`.
- Estado: vigente
- Archivos creados/modificados: `clients/stramondo-venezuela/outputs/homologacion-v2-2026-05-19.md`, `clients/stramondo-venezuela/outputs/manifest.md`, `clients/stramondo-venezuela/context.md`, `clients/stramondo-venezuela/log.md`, `clients/stramondo-venezuela/tasks.md`, `planning/homologacion-clientes-activos-2026-05-19.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Reemplaza a: cabeceras obsoletas y tabla `Estado de campañas Meta Ads (19 abr 2026)` que marcaba la B2B como activa.
- Accion recomendada: validar estado actual en Ads Manager/API y calidad real de leads en WhatsApp Business antes de reactivar, escalar presupuesto o cambiar placements.
- Riesgo: medio documental; no toca Meta Ads, secretos, tokens, presupuesto ni conectores.

### 2026-05-19 - fase 16 auditoria duplicaciones agents skills commands
- Area: arquitectura E-SELEC v2 / primitives Claude Code
- Agente: Codex + consulta Claude / alineacion
- Tipo: auditoria estructural y ajuste minimo
- Motivo: comprobar si la convivencia agents/skills/commands genera duplicacion operativa o rutas obsoletas.
- Estado: vigente
- Archivos creados/modificados: `.claude/agents/seo-leader.md`, `planning/auditoria-duplicaciones-agents-skills-commands-2026-05-19.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Reemplaza a: referencia obsoleta `futuro seo-tecnico` dentro de `seo-leader`.
- Pendiente-revision: 40 archivos `.claude/skills/*/agents/openai.yaml`; no se eliminan hasta confirmar si alguna herramienta externa los consume.
- Accion recomendada: si no hay consumidor externo de `openai.yaml`, abrir Fase 17 para eliminarlos con inventario y commit propio.
- Riesgo: bajo; no toca clientes, produccion, secretos ni conectores.

### 2026-05-19 - fase 17 saneamiento openai.yaml
- Area: arquitectura E-SELEC v2 / skills Claude Code
- Agente: Codex + consulta Claude / alineacion
- Tipo: saneamiento de artefactos no nativos
- Motivo: retirar 40 archivos `openai.yaml` creados durante la migracion que no son leidos por Claude Code ni tienen referencias internas operativas.
- Estado: vigente
- Archivos creados/modificados: `planning/saneamiento-openai-yaml-2026-05-19.md`, `planning/auditoria-duplicaciones-agents-skills-commands-2026-05-19.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Archivos eliminados: 40 archivos `.claude/skills/*/agents/openai.yaml`.
- Reemplaza a: pendiente-revision `DPL-002`.
- Accion recomendada: no volver a crear metadatos externos dentro de `.claude/skills` salvo que exista consumidor documentado; cada skill debe vivir en `SKILL.md` y referencias bajo demanda.
- Riesgo: bajo; no toca clientes, produccion, secretos, conectores ni outputs.

### 2026-05-19 - fase 18 regla de admision de canon
- Area: arquitectura E-SELEC v2 / gobernanza de canons
- Agente: Codex + consulta Claude / alineacion
- Tipo: regla transversal de calidad
- Motivo: impedir que futuras areas creen canons debiles por analogia con SEO; un canon solo se acepta si tiene fuente primaria, profundidad modular, indice y prueba de criterio.
- Estado: vigente
- Archivos creados/modificados: `.claude/rules/canon-admision.md`, `planning/patron-operativo-agentes-v2.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Fuentes externas revisadas pero no importadas: JSON handoff y PDFs del manual SEO entregados por Rodrigo en Downloads.
- Accion recomendada: antes de proponer canon para SEM, CRO, Reports, Web o Social, aplicar `.claude/rules/canon-admision.md`; si no cumple, reforzar skill/referencia/checklist.
- Riesgo: bajo; no toca clientes, produccion, secretos, conectores ni outputs.

### 2026-05-19 - browser mcp chrome playwright
- Area: integraciones locales E-SELEC v2 / MCP
- Agente: Codex + consulta Claude / alineacion
- Tipo: configuracion ejemplo y protocolo operativo
- Motivo: habilitar un camino seguro para usar Playwright MCP con Chrome controlado por Rodrigo sin crear servidor custom ni guardar sesiones o secretos en el repo.
- Estado: vigente
- Archivos creados/modificados: `.mcp.example.json`, `protocols/browser-mcp.md`, `protocols/README.md`, `registries/registro-artefactos.md`, `registries/registro-migracion.md`.
- Archivo local no versionado: `.mcp.json` con `playwright-chrome` sin secretos.
- Reemplaza a: idea inicial de crear un MCP custom Chrome + Playwright sin necesidad.
- Accion recomendada: iniciar Chrome con `--remote-debugging-port=9222`, reiniciar Claude Code y revisar `/mcp`; aplicar activos criticos antes de acciones sensibles.
- Riesgo: medio operativo si se usa sobre cuentas autenticadas; bajo documental porque no contiene secretos ni crea `.mcp.json` real.
