# Mensajes entre agentes - La Bottega del Gusto
> Canal de comunicacion interna entre agentes. El lider lo lee despues de cada ejecucion.
> Los mensajes NO se borran: se marcan como pendiente, leido o ejecutado.

## Formato de mensaje
```
---
DE: [agente origen]
PARA: [agente destino / lider]
TIPO: alerta | oportunidad | dependencia | info
FECHA: YYYY-MM-DD
ESTADO: pendiente | leido | ejecutado
MENSAJE: [descripcion del hallazgo]
ACCION SUGERIDA: [que deberia hacer el destinatario]
RESOLUCION: [si aplica]
---
```

---

## Mensajes

---
DE: Agente WEB
PARA: Lider Clientes
TIPO: alerta
FECHA: 2026-04-27
ESTADO: pendiente
MENSAJE: Crawler defensivo inicial detecto 2 hallazgos altos y 4 medios en la superficie publica: falta HSTS, usuarios REST enumerables, author enumeration, XML-RPC activo y headers incompletos. Tambien detecto secretos locales redactados en scripts/config, por lo que hay que migrar a `.env` y rotar claves tras actualizar conectores.
ACCION SUGERIDA: Priorizar hardening: revocar token temporal Hostinger, rotar `eselec-api`/claves expuestas, ocultar usuarios REST, bloquear author enumeration/XML-RPC si no se usan, aplicar headers y re-ejecutar `scripts/security_crawler.py`.
RESOLUCION: Parcial 2026-04-28: secretos locales migrados a `.env`; pendiente rotacion/revocacion de credenciales externas y hardening de produccion.
---

---
DE: Agente WEB
PARA: Lider Clientes
TIPO: alerta
FECHA: 2026-04-27
ESTADO: pendiente
MENSAJE: Auditoria de seguridad post-ajustes detecto hardening pendiente antes de publicar: usuarios administradores enumerables por REST, XML-RPC abierto a POST, headers de seguridad incompletos, readme/license publicos, actualizaciones automaticas desactivadas y clave antigua `eselec-api` pendiente de rotar.
ACCION SUGERIDA: Antes de go-live, ejecutar plan de hardening con confirmacion de Rodrigo: rotar/revocar `eselec-api`, ocultar usuarios REST, aplicar headers, bloquear XML-RPC si no se usa, bloquear readme/license y revisar origen de `automatic_updater_disabled`.
RESOLUCION: Pendiente de autorizacion para cambios en produccion.
---

---
DE: Agente WEB
PARA: Lider Clientes
TIPO: alerta
FECHA: 2026-04-26
ESTADO: pendiente
MENSAJE: Envia.es esta activo en la zona Madrid, pero no devuelve tarifas reales. La recogida fuera de Madrid ya fue corregida y la tienda tiene un fallback operativo `Entrega en Madrid` a 5,90 EUR, pero Envia real sigue pendiente antes de go-live.
ACCION SUGERIDA: Revisar credenciales, direccion de origen, paquetes, carriers/cobertura Madrid y respuesta del plugin Envia. Mantener fallback solo como solucion temporal.
RESOLUCION: Parcial 2026-04-26: fuera de Madrid ya no aparecen metodos; Madrid muestra recogida gratis + entrega 5,90 EUR. Pendiente resolver tarifa Envia real.
---

---
DE: Agente WEB
PARA: Lider Clientes
TIPO: dependencia
FECHA: 2026-03-19
ESTADO: pendiente
MENSAJE: La tienda puede operar de forma limitada con transferencia y pago en tienda/recogida, pero falta una pasarela de tarjeta real para vender con normalidad.
ACCION SUGERIDA: Contactar con Camila para conectar WooPayments/Stripe/Bizum y completar una prueba de compra real.
RESOLUCION: Parcial 2026-04-26: transferencia y pago en tienda estan activos; tarjeta sigue pendiente porque WooPayments no tiene cuenta conectada.
---

---
DE: Agente WEB
PARA: Lider Clientes
TIPO: dependencia
FECHA: 2026-03-19
ESTADO: pendiente
MENSAJE: El catalogo real publicado tiene 170 productos; 82 siguen sin imagen. Sin fotos, el catalogo no esta listo para publicar con buena conversion.
ACCION SUGERIDA: Solicitar a Camila imagenes de los productos mas vendidos o acceso a proveedores. Priorizar los 20 productos con mayor probabilidad de venta.
RESOLUCION: Corregido 2026-04-26: el conector anterior solo leia la primera pagina de 100 productos. La cifra real publicada es 170 productos.
---

---
DE: Agente Reports
PARA: Lider Clientes
TIPO: alerta
FECHA: 2026-03-19
ESTADO: pendiente
MENSAJE: El contrato actual podria no cubrir el alcance completo de e-commerce: WooCommerce, pasarelas, catalogo, logistica, SEO y soporte tecnico.
ACCION SUGERIDA: Preparar propuesta o ajuste de contrato antes de extender el alcance mensual. Estimado historico: 550-600 EUR/mes.
---

---
DE: Sistema
PARA: Lider Clientes
TIPO: alerta
FECHA: 2026-04-26
ESTADO: pendiente
MENSAJE: Se detecto una application password de WordPress guardada en texto plano dentro del GAS local. El archivo local fue limpiado, pero la clave debe considerarse expuesta.
ACCION SUGERIDA: Rotar/revocar la application password antigua de `eselec-api` si sigue activa y usar variables seguras (`PropertiesService`) en cualquier despliegue GAS.
RESOLUCION: Parcial 2026-04-26: secreto eliminado del archivo local `outputs/desarrollo/gas_formulario/Code.gs`.
---
