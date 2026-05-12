# Commands

Comandos reutilizables para flujos iniciados por Rodrigo.

Primer comando:

- `migrar-pieza.md`: evalua una pieza legacy antes de migrarla.
- `alertas-pendientes.md`: consolida mensajes pendientes de clientes y agencia.
- `auditoria-semanal.md`: revisa avance semanal, bloqueos y tareas atascadas.
- `verificar-medicion.md`: comprueba fuentes de medicion antes de auditorias, informes o decisiones.
- `ingestar-evidencia.md`: sanea exports o datos vivos antes de guardarlos en v2.
- `auditar-tracking.md`: audita o disena medicion GA4/GTM/eventos sin tocar produccion.
- `plan-arquitectura-web.md`: disena mapa de paginas, URLs, navegacion, enlazado interno y redirects sin tocar produccion.
- `auditar-schema.md`: audita o disena schema JSON-LD validable sin tocar produccion.

Los loops antiguos de E-SELEC no se copian aqui automaticamente. Cada loop debe convertirse en command, scheduled task o workflow solo despues de revisar riesgo, inputs y outputs.
