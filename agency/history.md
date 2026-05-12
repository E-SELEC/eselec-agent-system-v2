# Historial de Aprendizajes - E-SELEC v2

## Estado

- Fecha de migracion v2: 2026-05-12
- Fuente legacy: `agency/history.md`
- Tipo: resumen saneado, no copia completa

## Aprendizajes estructurales

- 2026-03-19: inicio del sistema E-SELEC y definicion modular de servicios.
- 2026-03-28: arquitectura de dos equipos: Clientes y Agencia.
- 2026-03-28: sistema de `context.md`, `log.md` y `mensajes.md` como memoria operativa.
- 2026-03-28: prioridad de tareas: urgente, importante, rutinario.
- 2026-03-28: arquitectura legacy de lideres y subagentes por especialidad.
- 2026-04-04: equipo WEB agregado.
- 2026-04-06: Notion definido como fuente principal de tareas cuando este conectado.
- 2026-04-06: MCP para lectura en tiempo real; scripts para escritura local e integraciones.
- 2026-04-10: separacion SEO/Web: WEB define arquitectura, SEO valida antes de lanzamiento.
- 2026-04-13: manejo de errores unificado.
- 2026-04-13: formato de log estandarizado.
- 2026-04-14: `agency/brand.md` creado como referencia de tono y estructura.
- 2026-05-12: sistema v2 en GitHub creado siguiendo primitivas Claude Code.
- 2026-05-12: piloto Computer Chamberi usado para probar calidad real antes de migrar todo.

## Principio aprendido en migracion v2

No migrar por volumen. Migrar por responsabilidad:

- instrucciones persistentes pequenas;
- reglas modulares;
- skills procedimentales;
- subagents ligeros;
- commands invocables;
- evidencia saneada;
- conectores solo tras auditoria de secretos.
