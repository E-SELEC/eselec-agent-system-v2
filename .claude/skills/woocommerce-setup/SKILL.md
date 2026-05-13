---
name: woocommerce-setup
description: >
  Audita, configura o planifica puesta en marcha de tiendas WooCommerce en
  WordPress: pagos, envios, moneda, impuestos, productos, paginas legales,
  checkout, SSL y go-live. Usalo para WooCommerce, tienda online, ecommerce
  WordPress, pagos, envios, productos, setup tienda o auditoria WC.
---

# WooCommerce Setup - E-SELEC

## Proposito

Auditar y planificar tiendas WooCommerce con foco en venta real, seguridad, checkout y trazabilidad.

Esta skill no modifica tienda, pagos, envios, impuestos ni productos sin Orden de Cambio.

## Fuentes obligatorias

Lee contexto de cliente, `clients/[cliente]/log.md`, `clients/[cliente]/mensajes.md`, `protocols/activos-criticos.md`, `protocols/gestion-accesos.md`, `protocols/control-artefactos.md`, `quality/criterios-output.md`, y si aplica `.claude/skills/analytics-tracking/SKILL.md`, `.claude/skills/page-cro/SKILL.md` y `.claude/skills/email-sequence/SKILL.md`.

Necesitas URL, pais, moneda, productos, metodos de pago, envios, impuestos, permisos API y objetivo: auditoria, setup o go-live.

## Niveles

- WC3 - listo: auditoria completa, bloqueantes, plan, comandos/instrucciones y aprobaciones.
- WC2 - fuerte: diagnostico claro, faltan accesos o confirmaciones.
- WC1 - orientativo: guia con datos parciales.
- WC0 - bloqueado: falta cliente, URL o permiso.

## Workflow

1. Confirmar modo: auditoria, guia manual, setup o go-live.
2. Verificar acceso disponible sin exponer secretos.
3. Auditar pasos: conexion, moneda, impuestos, pagos, envios, productos, paginas legales, emails, SSL y checkout.
4. Clasificar bloqueante, requiere atencion, correcto y recomendado.
5. Proponer plan secuencial con Orden de Cambio para cualquier modificacion real.
6. Si se aprueba ejecucion, aplicar solo pasos aprobados y re-auditar.
7. Entregar usando `templates/woocommerce-audit.md`.

## Reglas

- Pagos, envios, impuestos, productos y paginas legales son activos criticos.
- No guardar ni mostrar claves WC, Stripe, PayPal, Redsys, Mercado Pago ni bancarias.
- No activar/desactivar gateways sin aprobacion.
- No publicar productos ni paginas sin aprobacion.
- No declarar go-live hasta pasar checklist.

## Bloqueos

- faltan cliente o URL;
- no hay permiso para auditar;
- se piden cambios en tienda real sin Orden de Cambio;
- faltan datos legales/fiscales para impuestos o pagos;
- hay secretos expuestos en texto o archivos.

## Referencias

- `references/woocommerce-checklist.md`: pasos y bloqueantes.
- `templates/woocommerce-audit.md`: formato de salida.
- `checklists/revision.md`: revision final.
