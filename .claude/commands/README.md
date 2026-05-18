# Commands

Comandos reutilizables para flujos iniciados por Rodrigo.

Los ejemplos de comandos deben usar slugs inventados (`cliente-servicios`, `cliente-ecommerce`, `agencia-demo`). No uses nombres de clientes reales en ejemplos reutilizables.

## Patron command-skill

Un command es una entrada practica: recibe la peticion de Rodrigo, lee contexto del cliente, decide si se responde en chat o se usa `--write`, y aplica manifest/log/protocolos si hay escritura.

Una skill es la fuente del procedimiento especializado. Si un command apunta a una skill, la skill gobierna el criterio principal. No dupliques dentro del command el contenido largo de la skill; deja solo routing, lecturas obligatorias, formato de escritura y reglas de seguridad.

Primer comando:

- `migrar-pieza.md`: evalua una pieza legacy antes de migrarla.
- `alertas-pendientes.md`: consolida mensajes pendientes de clientes y agencia.
- `auditoria-semanal.md`: revisa avance semanal, bloqueos y tareas atascadas.
- `verificar-medicion.md`: comprueba fuentes de medicion antes de auditorias, informes o decisiones.
- `ingestar-evidencia.md`: sanea exports o datos vivos antes de guardarlos en v2.
- `auditar-tracking.md`: audita o disena medicion GA4/GTM/eventos sin tocar produccion.
- `plan-arquitectura-web.md`: disena mapa de paginas, URLs, navegacion, enlazado interno y redirects sin tocar produccion.
- `auditar-schema.md`: audita o disena schema JSON-LD validable sin tocar produccion.
- `auditar-ai-seo.md`: audita visibilidad en respuestas AI y planifica AI SEO con evidencia.
- `plan-contenido.md`: crea estrategia de contenido, pilares, clusters y calendario sin publicar.
- `escribir-copy.md`: escribe o mejora copy comercial sin publicar ni inventar claims.
- `revisar-copy.md`: revisa copy existente con pasadas de claridad, prueba, tono y CTA.
- `auditar-cro-pagina.md`: audita propuesta de valor, CTA, confianza, friccion y medicion de una pagina.
- `auditar-formulario.md`: audita campos, errores, privacidad y medicion de formularios.
- `plan-ab-test.md`: disena experimentos A/B sin implementarlos.
- `auditar-signup-flow.md`: audita registro, alta de cuenta o trial sin tocar produccion.
- `auditar-onboarding.md`: audita activacion y primer valor post-signup sin tocar produccion.
- `auditar-popup.md`: audita popups, modales, overlays y banners sin tocar produccion.
- `auditar-paywall.md`: audita paywalls, upsells y upgrades sin tocar produccion.
- `plan-paid-ads.md`: planifica o audita campanas paid media sin tocar cuentas reales.
- `generar-ad-creative.md`: genera variaciones de anuncios sin subirlas a plataformas.
- `crear-social-content.md`: crea calendario o piezas sociales sin publicar.
- `plan-programmatic-seo.md`: planifica paginas SEO a escala sin publicarlas.
- `plan-competitor-page.md`: planifica paginas comparativas sin publicarlas.
- `escribir-cold-email.md`: escribe cold emails o follow-ups sin enviarlos.
- `plan-email-sequence.md`: disena secuencias lifecycle sin activarlas.
- `plan-lead-magnet.md`: planifica lead magnets sin publicar formularios.
- `crear-sales-enablement.md`: crea materiales comerciales sin enviarlos.
- `plan-pricing.md`: analiza pricing sin cambiar precios reales.
- `plan-revops.md`: disena procesos RevOps sin tocar CRM.
- `plan-churn-prevention.md`: disena retencion sin tocar billing.
- `plan-referral-program.md`: disena referidos/afiliados sin lanzarlos.
- `plan-launch.md`: planifica lanzamientos, betas o releases sin publicarlos.
- `plan-free-tool.md`: planifica herramientas gratuitas sin construirlas ni publicarlas.
- `generar-marketing-ideas.md`: prioriza ideas de marketing sin ejecutar canales.
- `aplicar-psicologia-marketing.md`: revisa activos o flujos con behavioral science etica.
- `crear-product-marketing-context.md`: crea o actualiza contexto de posicionamiento.
- `humanizar-texto.md`: humaniza textos sin cambiar claims ni CTA.
- `crear-prompt.md`: crea prompts listos para una herramienta IA.
- `producir-video-kling.md`: prepara prompts y parametros de video AI sin ejecutar Kling.
- `limpiar-carpeta-cliente.md`: audita carpeta de cliente y propone limpieza segura.
- `revisar-web-visual.md`: revisa pagina web contra referencia visual.
- `auditar-woocommerce.md`: audita tienda WooCommerce y prepara plan de setup.

Los loops antiguos de E-SELEC no se copian aqui automaticamente. Cada loop debe convertirse en command, scheduled task o workflow solo despues de revisar riesgo, inputs y outputs.
