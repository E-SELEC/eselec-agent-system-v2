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

