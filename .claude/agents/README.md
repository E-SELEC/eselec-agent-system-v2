# Agentes Claude

Aqui viviran los subagents nativos cuando se migren.

No migrar prompts antiguos en bloque. Cada agente debe tener:

- Proposito unico.
- Herramientas necesarias.
- Inputs esperados.
- Criterios de parada.
- Formato de salida.
- Riesgos y permisos.

Agentes activos:

- `arquitecto-migracion-claude`: audita y planifica la migracion legacy -> v2.
- `docente`: convierte correcciones y fallos de calidad en criterio operativo examinable.
- `leader-clientes`: orquesta trabajo de clientes, prioriza y elige skills/subagents sin ejecutar produccion.
- `leader-agencia`: orquesta trabajo interno de E-SELEC sin mezclarlo con clientes.
- `seo-leader`: coordina SEO tecnico, organico, local, AI SEO y validacion web.
- `cro-leader`: coordina conversion, formularios, tests, onboarding, popups y paywalls.
- `sem-leader`: coordina paid media, tracking, audiencias, presupuestos y creatividad.
- `social-leader`: coordina estrategia, contenido y comunidad social.
- `reports-leader`: coordina informes, alertas y proximos pasos de cliente.
- `web-leader`: coordina arquitectura, diseño, web, WordPress, WooCommerce y feedback visual.
- `seo-tecnico`, `seo-organico`, `seo-local`, `seo-llms`, `seo-web`: especialistas SEO.
- `cro-funnels`, `cro-landing`, `cro-formularios`, `cro-tests`, `cro-uxui`: especialistas CRO.
- `sem-google`, `sem-meta`, `sem-linkedin`, `sem-tiktok`, `sem-analitica`: especialistas SEM/Paid Media.
- `social-estrategia`, `social-contenido`, `social-comunidad`: especialistas Social.
- `reports-cliente`, `reports-alertas`, `reports-proxpasos`: especialistas Reports.
- `web-arquitectura`, `web-diseno`, `web-desarrollo`, `web-implementacion`, `web-mantenimiento`, `web-feedback-loop`: especialistas Web.
- `agency-captacion`, `agency-reputacion`, `agency-onboarding`, `agency-retencion`, `agency-finanzas`: especialistas internos de Agencia.

