# Reglas de Plataforma - Paid Ads

Estas reglas se usan cuando una decision de paid media puede cambiar presupuesto, lectura de resultados, tracking, plataforma o expectativas del cliente.

## Principios

- La metrica de plataforma no es automaticamente resultado de negocio.
- Un clic, una visualizacion, una visita, un evento de mensajeria o una conversion modelada no equivalen por si solos a lead cualificado, venta o respuesta real.
- Si el objetivo es conversion, el tracking debe estar verificado antes de recomendar inversion, escala o optimizacion.
- Si los datos de plataforma y GA4/CRM/ventas se contradicen, declara la contradiccion y no elijas una verdad sin evidencia.
- Antes de concluir que "la campana funciona" o "la campana falla", separa la capa del problema: tracking, oferta, landing, creatividad, audiencia, presupuesto, cuenta o atencion comercial.

## Validacion de eventos

| Tipo de senal | Puede indicar | No demuestra por si sola | Validacion recomendada |
|---|---|---|---|
| Link click | Interes inicial o promesa creativa atractiva | Lead, venta, llamada o conversacion real | GA4, CRM, formulario, llamada, WhatsApp o backend |
| Landing page view | Carga de pagina o visita post-click | Intencion de compra ni calidad de trafico | Tasa de conversion, scroll/clicks, formulario, CRM |
| Messaging event | Inicio o intento de contacto segun plataforma | Respuesta humana, lead atendido o venta | Bandeja real, WhatsApp Business, CRM o registro comercial |
| Lead form submit | Captura de datos | Calidad del lead, contacto valido o cierre | CRM, llamadas, email valido, oportunidad o venta |
| Purchase/revenue | Venta atribuida por plataforma | Margen, devoluciones, duplicados o atribucion exacta | Backend, ecommerce, GA4 y conciliacion de ingresos |

## Reglas por plataforma

### Google Ads

- No mezcles objetivos distintos en la misma campana.
- No uses concordancia amplia sin historial, negativas y control de terminos de busqueda.
- Separa Search de Display salvo que exista una razon documentada.
- Si hay keywords que convierten bien en paid, informa a SEO como oportunidad organica.

### Meta Ads

- No trates eventos de mensajeria, clics o engagement como conversion final sin validacion externa.
- La creatividad suele ser una palanca critica; fatiga creativa puede parecer problema de audiencia.
- Si la frecuencia sube y el CTR cae, revisa fatiga antes de culpar solo al algoritmo.
- Si hay campana de conversion, valida Pixel/eventos/dominio antes de recomendar escala.

### LinkedIn Ads

- Solo tiene sentido cuando el cliente es B2B, el ICP es claro y el valor del cliente justifica CPL alto.
- Si el ticket o margen no soporta el CPL probable, recomienda otro canal.
- La segmentacion debe poder expresarse por cargo, funcion, industria, empresa, seniority o cuenta objetivo.

### TikTok Ads

- No recomiendes TikTok si no existe capacidad de producir video nativo de forma recurrente.
- No recicles creatividad de Meta/Instagram sin adaptarla al lenguaje de TikTok.
- El primer diagnostico de bajo rendimiento debe revisar gancho, formato, ritmo, audio y oferta antes de tocar presupuesto.

## Salida minima al diagnosticar

Incluye siempre:

- objetivo real de negocio;
- metrica de plataforma usada;
- fuente externa de validacion, si existe;
- capa probable del problema;
- datos faltantes;
- decision segura: auditar, esperar datos, ajustar plan o pedir Orden de Cambio.
