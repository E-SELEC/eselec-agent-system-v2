# Memoria de aprendizajes — Stramondo Venezuela

## Qué ha funcionado
- **CPM muy bajo en Venezuela:** $0,32 CPM / $0,001 por ThruPlay / $0,005 CPC — eficiencia publicitaria excepcional. Con poco presupuesto se logra gran alcance.
- **Video de receta (Tiramisú):** Generó 27.718 ThruPlays con solo $24,36 — el formato de receta con producto funciona para awareness B2C.
- **Campaña B2B con WhatsApp:** 6.103 clics WhatsApp a $0,01 por clic / $32,19 gastados — el anuncio B2B con CTA directo a WhatsApp es eficiente para generación de leads.
- **Anuncio 01 "Mejores heladerías":** El más eficiente de los B2B — $0,169/conv, 3,07% tasa. Referencia para creativos futuros.
- **Pivote B2C→B2B confirmado:** La decisión de priorizar el segmento B2B (heladerías, restaurantes, cafeterías) fue correcta — mayor ticket y conversión más clara.
- **Públicos de retargeting de video:** Creados y en proceso de poblarse (25%, 50%, 75% visto). Base para futuras campañas de retargeting.
- **Copiloto de ventas con IA:** System prompt para Carolina con framework de ventas (Voss/Belfort/Cardone), catálogo, perfiles de cliente, matriz cross-sell y playbook de objeciones. Activado con Gemini Pro.
- **Reorganización de outputs/:** Subcarpetas (auditorias/, reportes/, templates/) — mejora la navegación en el proyecto.

## Qué NO ha funcionado
- **Cuello de botella operativo en WhatsApp:** 325 conversaciones iniciadas, Carolina respondió solo 2 (messaging_conversation_replied_7d=2). El problema no son los anuncios — es la capacidad de atención humana.
- **Facebook completamente ignorado:** Solo 2 seguidores — no hay valor en invertir aquí.
- **"Anuncio de Ventas" B2C en borrador:** Lleva tiempo sin publicarse — bloqueo sin resolver.
- **Exclusión de Instagram en Advantage+:** La API no permite excluir Instagram en campañas Advantage+ — requiere cambio manual a Manual Placements en Ads Manager por Rodrigo.
- **Anuncios 02 y 03 sobrefinanciados:** Consumían 64% del presupuesto con peor ROI que el anuncio 01. El anuncio 03 "Gelato inolvidable" pausado.
- **Tracking por ad_id en WhatsApp:** Poco útil porque los clientes ven múltiples anuncios + perfil IG antes de comprar. No confiar en este método para atribución.
- **Tasa de cierre real baja:** 0,6% (1 venta de 168 conversaciones) o 3,2% (1 de 31 atendidas). El problema es operativo, no publicitario.
- **ChatGPT Plus:** No se activó ($20/mes). Carolina usa Gemini Pro (gratuito) como alternativa.

## Preferencias del cliente
- **Contacto principal:** Toni Di Benedetto (dueño). Carolina gestiona WhatsApp y atención al cliente.
- **Sin website:** Todo el funnel es Instagram → WhatsApp → venta. No hay web ni e-commerce.
- **Canal de conversión:** WhatsApp Business (+58 422-8027745) es el único punto de cierre.
- **Catálogo:** Accesible vía WhatsApp (https://wa.me/c/584228027745). No hay catálogo web.
- **Acceso Meta Ads:** Solo desde Chrome perfil "E-SELEC" de Rodrigo.
- **Presupuesto activo:** $2 USD/día (puede aumentar — el CPM lo justifica).
- **Mercado Venezuela:** CPM ultra bajo — escalar presupuesto es rentable si se resuelve el cuello de botella operativo.
- **Tono:** Especializado para profesionales del sector (heladería/repostería/cocina italiana).

## Insights de negocio
- **Producto estrella:** Farci de Pistacho (pasta de pistacho en 2 texturas: espesa para rellenos/toppings, fluida para gelato). Toda comunicación gira alrededor de él.
- **Segmento B2B más rentable:** Heladerías, restaurantes, cafeterías — mayor ticket y conversión más predecible que B2C.
- **Preguntas frecuentes reales de leads:** Ubicación (no tienen tienda física), delivery, cantidades, rendimiento, textura Farci, catálogo de sabores.
- **Delivery:** Gratis en Caracas (entrega al día siguiente) / $10 por bulto al interior (3-7 días hábiles).
- **8 familias de productos:** La comunicación debe incluirlas todas, no solo el Farci — hipótesis validada con el chat template v2.
- **Distribuidora oficial:** Stramondo es distribuidor venezolano oficial de Stramondo srl (Italia) — credencial de autoridad importante.
- **Audiencia total:** 17,5M–20,6M personas en Venezuela (Advantage+) — mercado amplio para awareness.
- **ROAS estimado:** 8,7x según reporte ejecutivo (basado en 1 venta de $280 / $32 gastados).

## Reglas operativas aprendidas
- **Acceso Meta Ads:** Solo desde Chrome perfil "E-SELEC" — nunca desde otro perfil.
- **Meta Ads Account ID:** act_936709065437591 / Meta Business ID: 928766489870829.
- **Exclusión de Instagram:** No se puede hacer vía API en Advantage+ — debe hacerlo Rodrigo manualmente en Ads Manager cambiando a Manual Placements.
- **Cambios pendientes siempre visibles:** Verificar en Ads Manager si hay "cambios pendientes de publicar" antes de analizar resultados.
- **Chat template:** Cambiarlo requiere editar el anuncio en Meta Ads Manager → Campaña B2B → editar anuncio → mensaje de bienvenida. Lo hace Carolina.
- **Atribución WhatsApp:** No usar ad_id para atribución — los clientes ven múltiples touchpoints antes de comprar.
- **Escalar presupuesto:** Solo después de resolver el cuello de botella operativo (capacidad de respuesta de Carolina).
- **Público retargeting:** Poblar primero a >1.000 personas antes de lanzar campañas de retargeting.

## Próximas hipótesis a probar
- **Chat template WhatsApp v2 (mixto B2B+B2C):** 5 botones que cubren todos los segmentos + pregunta de cierre en cada respuesta. Si Carolina lo implementa, debería mejorar la tasa de atención de conversaciones.
- **Copiloto Gemini Pro con Carolina:** Si lo adopta con el SLA de 30 min establecido, la tasa de cierre debería pasar de 0,6% a al menos 3-5%.
- **Aumentar presupuesto a $5/día:** Con el CPM actual, triplicaría el alcance. Hipótesis: si el cuello de botella operativo está resuelto, el ROAS debería mantenerse.
- **Video B2B específico:** Una campaña separada para distribuidores/restaurantes con creativos B2B debería tener mejor tasa de cierre que reutilizar creativos B2C.
- **Excluir Instagram en Manual Placements:** Si se excluye Instagram y se concentra todo en Facebook, el CPC debería bajar (hipótesis basada en datos del sector).

## Historial de versiones
- [2026-04-21] Memory.md creado. Extraído de context.md (2026-03-27), log.md (sesiones mar-abr 2026) y tasks.md.

## Aprendizajes 2026-05-11
- El token de Meta Ads expiró el 2026-05-01 y bloqueó el chequeo de campañas del 2026-05-11. Antes de auditar Stramondo por API, validar token con el conector.
- El token efectivo se carga desde .env mediante config.py. scripts/refresh_meta_token.py fue corregido para actualizar .env, no config.py.
- Corrección de lectura Meta Ads: la campaña B2B está configurada para maximizar clics en el enlace hacia destinos de mensajes. Los eventos `messaging_*` de la API no deben tratarse como conversiones/repuestas reales sin validación en WhatsApp Business.
- Tras renovar token, la campaña principal B2B aparece PAUSED. Últimos 30 días: $175.38 gastados, 29.858 link clicks, CPC link click aprox. $0.0059, CTR 5.40%, CPM $0.31.
- Instagram medido por link click no es 6.4x peor: Facebook tuvo CPC aprox. $0.0057 e Instagram $0.0068. La exclusión de Instagram debe decidirse por calidad real del lead, no por eventos `messaging_*`.
