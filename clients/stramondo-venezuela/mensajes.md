# Mensajes entre agentes â€” Stramondo Venezuela
> Canal de comunicaciÃ³n interna entre agentes. El lÃ­der lo lee despuÃ©s de cada ejecuciÃ³n.
> Los mensajes NO se borran â€” se marcan como [LEÃDO] o [EJECUTADO].

## Formato de mensaje
```
---
DE: [agente origen]
PARA: [agente destino / lÃ­der]
TIPO: alerta | oportunidad | dependencia | info
FECHA: YYYY-MM-DD
ESTADO: pendiente | leÃ­do | ejecutado
MENSAJE: [descripciÃ³n del hallazgo]
ACCIÃ“N SUGERIDA: [quÃ© deberÃ­a hacer el destinatario]
---
```

---

## Mensajes

---
DE: Agente SEM
PARA: LÃ­der Clientes
TIPO: oportunidad
FECHA: 2026-03-28
ESTADO: ejecutado
MENSAJE: CampaÃ±a B2C activa logra $0,001/ThruPlay (benchmark referencia: <$0,02) â€” rendimiento excepcional. Con $5/dÃ­a en lugar de $2/dÃ­a se triplicarÃ­a el alcance sin cambiar creativos.
ACCIÃ“N SUGERIDA: Proponer a Carolina aumentar presupuesto a $5/dÃ­a aprovechando el CPM bajo actual en Venezuela.
RESOLUCIÃ“N: Pivote confirmado B2Câ†’B2B en abril 2026. B2C desactivada. Escalar presupuesto B2B pendiente de verificar adopciÃ³n del copiloto primero.
---

---
DE: Agente SEM
PARA: LÃ­der Clientes
TIPO: dependencia
FECHA: 2026-03-28
ESTADO: ejecutado
MENSAJE: "Anuncio de Ventas" lleva en borrador desde la auditorÃ­a. EstÃ¡ listo para publicar pero requiere aprobaciÃ³n de Rodrigo.
ACCIÃ“N SUGERIDA: Revisar el anuncio en Meta Ads (cuenta 936709065437591) y publicarlo si estÃ¡ correcto.
RESOLUCIÃ“N: CampaÃ±a B2B lanzada con 5 anuncios activos (19 abr). Anuncio 03 pausado por bajo rendimiento.
---

---
DE: Agente SEM
PARA: LÃ­der Clientes
TIPO: alerta
FECHA: 2026-03-28
ESTADO: ejecutado
MENSAJE: CampaÃ±a de Mensajes desactivada â€” el chat template estÃ¡ diseÃ±ado pero no hay configuraciÃ³n en la campaÃ±a. El flujo WhatsAppâ†’conversiÃ³n no estÃ¡ activo.
ACCIÃ“N SUGERIDA: Reactivar la CampaÃ±a de Mensajes con el editor de chats ya aprobado (5 preguntas + respuestas automÃ¡ticas).
RESOLUCIÃ“N: CampaÃ±a B2B activa. Chat template v2 diseÃ±ado (outputs/templates/chat-template-whatsapp-v2.md) â€” pendiente implementaciÃ³n manual por Carolina en Ads Manager.
---

---
DE: Agente SEM
PARA: LÃ­der Clientes
TIPO: alerta
FECHA: 2026-04-19
ESTADO: pendiente
MENSAJE: CRÃTICO â€” De 325 conversaciones WhatsApp iniciadas desde los anuncios, Carolina respondiÃ³ solo 2 (messaging_conversation_replied_7d=2). Tasa de respuesta: 0,6%. El cuello de botella es operativo, no publicitario.
ACCIÃ“N SUGERIDA: Verificar que Carolina estÃ¡ usando el copiloto Gemini Pro. Confirmar si el sistema de etiquetas WhatsApp Business estÃ¡ configurado. Evaluar si hay problema tÃ©cnico (mÃ³vil, conexiÃ³n) o de adopciÃ³n.
---

---
DE: Agente SEM
PARA: LÃ­der Clientes
TIPO: dependencia
FECHA: 2026-04-19
ESTADO: pendiente
MENSAJE: ExclusiÃ³n de Instagram en Ads Manager bloqueada â€” la campaÃ±a usa Advantage+ que impide cambios de placement vÃ­a API. Requiere acciÃ³n manual de Rodrigo en la interfaz web de Ads Manager.
ACCIÃ“N SUGERIDA: Rodrigo entra a Ads Manager â†’ CampaÃ±a B2B â†’ Conjunto de anuncios â†’ Placements â†’ cambiar de Advantage+ a Manual â†’ desmarcar Instagram.
---

---
DE: Agente SEM
PARA: LÃ­der Clientes
TIPO: dependencia
FECHA: 2026-04-19
ESTADO: pendiente
MENSAJE: Chat template WhatsApp v2 diseÃ±ado pero no implementado. Carolina debe entrar en Meta Ads Manager y reemplazar el mensaje de bienvenida actual con el template v2 (5 botones B2B+B2C).
ACCIÃ“N SUGERIDA: Enviar a Carolina el archivo outputs/templates/chat-template-whatsapp-v2.md con instrucciones de implementaciÃ³n.
---

---
DE: Agente SEM
PARA: Líder Clientes
TIPO: dependencia
FECHA: 2026-05-11
ESTADO: ejecutado
MENSAJE: No se pudo chequear Meta Ads con datos actuales porque el token de la Marketing API expiró el 2026-05-01. El último dato fiable era la auditoría del 2026-04-24.
ACCIÓN SUGERIDA: Renovar token con python scripts/refresh_meta_token.py y volver a ejecutar python scripts/meta_ads_connector.py stramondo-venezuela --json --campanas --anuncios --publicos.
RESOLUCIÓN: Token renovado y chequeo ejecutado el 2026-05-11. Output: outputs/auditorias/meta-ads-chequeo-11mayo2026.md.
---

---
DE: Agente SEM
PARA: Líder Clientes
TIPO: alerta
FECHA: 2026-05-11
ESTADO: ejecutado
MENSAJE: Corrección de lectura: la campaña principal Stramondo | B2B | Clics al enlace | Abril 2026 aparece PAUSED y está configurada para maximizar clics en el enlace hacia destinos de mensajes. Los 874 eventos `messaging_conversation_started_7d` no deben tratarse como conversiones reales ni los 3 `messaging_conversation_replied_7d` como prueba suficiente de respuestas humanas.
ACCIÓN SUGERIDA: Evaluar la campaña por link clicks, CPC, CTR y calidad real de leads validada en WhatsApp Business. No usar eventos `messaging_*` como métrica principal sin validación manual.
RESOLUCIÓN: Reporte 2026-05-11 corregido para reflejar clics al enlace como resultado primario.
---
