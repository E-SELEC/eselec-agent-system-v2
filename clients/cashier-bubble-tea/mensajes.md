# Mensajes entre agentes — Chashier Bubble Tea
> Canal de comunicación interna entre agentes. El líder lo lee después de cada ejecución.
> Los mensajes NO se borran — se marcan como [LEÍDO] o [EJECUTADO].

## Formato de mensaje
```
---
DE: [agente origen]
PARA: [agente destino / líder]
TIPO: alerta | oportunidad | dependencia | info
FECHA: YYYY-MM-DD
ESTADO: pendiente | leído | ejecutado
MENSAJE: [descripción del hallazgo]
ACCIÓN SUGERIDA: [qué debería hacer el destinatario]
---
```

---

## Mensajes

---
DE: Agente SEO Orgánico
PARA: Líder Clientes
TIPO: alerta
FECHA: 2026-03-28
ESTADO: pendiente
MENSAJE: "té de burbujas" posiciona en 4.4 en GSC pero tiene 0 clicks con 26.055 impresiones/mes. El title/meta no está optimizado para esa query. Es la corrección de mayor impacto/esfuerzo del cliente.
ACCIÓN SUGERIDA: Optimizar title y meta description de la página que posiciona para "té de burbujas" antes de cualquier otra acción SEO.
---

---
DE: Agente SEO Técnico
PARA: Líder Clientes
TIPO: alerta
FECHA: 2026-03-28
ESTADO: ejecutado
MENSAJE: Backlinks tóxicos detectados — Trust Flow Majestic = 0. 63% de dominios provienen de Singapur (posibles PBNs). Riesgo de penalización algorítmica o manual.
ACCIÓN SUGERIDA: Preparar archivo disavow con los dominios sospechosos y subirlo a Google Search Console.
---

---
DE: Agente SEO Técnico
PARA: Líder Clientes
TIPO: alerta
FECHA: 2026-03-28
ESTADO: ejecutado
MENSAJE: Canonical conflict activo — Google elige canonical diferente al configurado en 1 página. Puede estar dañando la indexación de esa URL.
ACCIÓN SUGERIDA: Identificar la página afectada en GSC (Coverage > Duplicate > alternate page with proper canonical tag) y corregir el canonical manualmente.
---

---
DE: Agente SEO Técnico
PARA: Líder Clientes
TIPO: alerta
FECHA: 2026-03-28
ESTADO: ejecutado
MENSAJE: Core Web Vitals sin datos para móvil ni escritorio en GSC. Posible bloqueo de rastreo de recursos o problema con el plugin Seraphinite Accelerator.
ACCIÓN SUGERIDA: Revisar si Seraphinite está bloqueando el rastreo de CSS/JS que Google necesita para calcular CWV. Verificar en robots.txt y en el informe de Core Web Vitals de GSC.
---

---
DE: SEO Técnico
PARA: SEO Orgánico
TIPO: dependencia
FECHA: 2026-04-20
ESTADO: pendiente
MENSAJE: No activar optimización On-Page hasta que canonical conflict esté corregido y verificado en GSC. Primera prioridad On-Page: title/meta de /todo-lo-que-necesitas-saber-del-bubble-tea-o-te-de-burbujas/ para capturar "té de burbujas" (2.900 búsquedas/mes, pos. 21).
ACCIÓN SUGERIDA: Esperar confirmación del Líder SEO antes de activar seo-organico.md.
---

---
DE: SEO Técnico
PARA: Líder WEB / Diseño
TIPO: info
FECHA: 2026-04-20
ESTADO: pendiente
MENSAJE: Seraphinite Accelerator puede cachear versiones antiguas de páginas. Cualquier cambio visual debe ir seguido de un vaciado de caché de Seraphinite.
ACCIÓN SUGERIDA: Vaciar caché de Seraphinite tras cualquier cambio visual para asegurar que Googlebot y usuarios ven la versión actualizada.
---

---
DE: Agente Reports
PARA: Líder Clientes
TIPO: oportunidad
FECHA: 2026-03-27
ESTADO: pendiente
MENSAJE: Informe de resultados 2 años generado (outputs/Informe_Resultados_2Anos_Chashier_v2.docx). Gemma ha confirmado que quiere continuar. Momento óptimo para presentar propuesta Año 3.
ACCIÓN SUGERIDA: Enviar informe a Gemma y preparar propuesta de renovación Año 3 con nuevos objetivos (CTR, orgánico, email marketing).
---
