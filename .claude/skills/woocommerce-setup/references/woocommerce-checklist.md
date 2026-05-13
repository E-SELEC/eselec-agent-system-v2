# WooCommerce Checklist

## Pasos

| Paso | Area | Bloquea venta |
|---|---|---|
| 0 | conexion y permisos | si |
| 1 | auditoria completa | no |
| 2 | moneda, pais, formato | si, si incorrecto |
| 3 | impuestos | depende del pais |
| 4 | pasarela de pago | si |
| 5 | zonas y metodos de envio | si |
| 6 | productos y categorias | si |
| 7 | paginas legales y emails | depende |
| 8 | checklist go-live | si |

## Bloqueantes go-live

- SSL activo.
- Moneda correcta.
- Al menos un gateway activo y probado.
- Envio configurado o pickup claro.
- Al menos un producto publicado con precio.
- Carrito, checkout y mi cuenta configurados.
- Politicas legales suficientes para el pais.
- Pedido de prueba completado.

## Accesos sensibles

- WooCommerce REST keys.
- Stripe/PayPal/Redsys/Mercado Pago.
- Datos bancarios.
- Admin WordPress.

Registrar solo metadatos de acceso, nunca secretos.

## Modo guia

Si no hay API, entregar rutas wp-admin exactas y esperar confirmacion del usuario.
