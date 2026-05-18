# Tareas activas - La Bottega del Gusto
> Actualizado manualmente por Codex el: 2026-05-03
> Fuente principal: log.md + evaluacion de codigo web del 2026-05-03 + auditorias WooCommerce/API.
> Nota: la sincronizacion Notion previa era del 2026-04-06 y quedo desactualizada.

---

## Estado real resumido

- WooCommerce operativo via API con usuario Codex separado.
- Catalogo real actual: 170 productos publicados, 0 sin precio, 82 sin imagen.
- Checkout operativo de forma parcial: transferencia bancaria + pago en tienda/recogida.
- Envio Madrid operativo con fallback `Entrega en Madrid` a 5,90 EUR + `Recogida gratuita en tienda`.
- Categoria `Quesos Italianos` operativa con 46 productos.
- Envia.es esta activo, pero todavia no devuelve tarifas reales.
- `noindex`/`nofollow` en home y tienda es intencional hasta publicar la web.
- Rodrigo limpio el CSS manual problemático del widget; Codex verifico que ya no aparecen `bdg-*`, `bdg-cards` ni `block-13` en la web viva.
- Queda `block-18` vacio y `block-16` inactivo con CSS viejo; no reactivar sin Orden de Cambio.
- `/tienda/` esta estabilizada de nuevo como archivo WooCommerce mediante rewrite y muestra 9 productos. No seguir forzando 12 productos por pagina desde REST/Customizer hasta decidir una estrategia factory/staging.

---

## Hecho

- [x] Crear usuario API separado para Codex (`eselec-codex`).
- [x] Corregir `site_url` y `home_url` a HTTPS.
- [x] Eliminar referencias internas HTTP en home/Elementor/autor principal.
- [x] Desactivar/validar ausencia de cache LiteSpeed en frontend.
- [x] Corregir formato de moneda a Espana: `1.234,56 EUR`.
- [x] Limitar envio a Espana y cliente por defecto a base de tienda.
- [x] Desactivar recogida global fuera de Madrid.
- [x] Crear fallback visible `Entrega en Madrid` a 5,90 EUR.
- [x] Crear/activar `Recogida gratuita en tienda` dentro de zona Madrid.
- [x] Restringir pago en tienda solo a recogida.
- [x] Crear pagina `Terminos y Condiciones` y asignarla a WooCommerce.
- [x] Reasignar productos evidentes a `Quesos Italianos`.
- [x] Verificar que Barcelona/Valencia no muestran metodos de envio.
- [x] Reorganizar carpeta `outputs/` por tipo de entregable.
- [x] Eliminar credencial WordPress en texto plano del GAS local.
- [x] Limpiar CSS manual `bdg-*` de widgets WooCommerce (ejecutado por Rodrigo, verificado por Codex).
- [x] Retirar de la sidebar WooCommerce activa los bloques vacios `block-12` y `block-18` sin borrarlos; quedaron en widgets inactivos.
- [x] Retirar `block-15` de la sidebar WooCommerce activa; era filtro nativo, pero seguia cargandose tambien en carrito/checkout por la estructura de Astra.
- [x] Separar layout WooCommerce: tienda conserva sidebar izquierda; carrito, checkout y mi cuenta quedan sin sidebar para evitar contaminacion visual en flujos de conversion.
- [x] Crear pagina borrador `Tienda Test Bottega` (ID 4401) con shortcode oficial WooCommerce: 12 productos, 4 columnas y paginacion, sin tocar la tienda actual.
- [x] Aplicar diseno inicial encapsulado a `Tienda Test Bottega`: hero, franja Italia, cards WooCommerce, botones, paginacion y responsive, sin afectar `/tienda/`, carrito ni checkout.

---

## Urgente antes de go-live

- [ ] Rotar o revocar token/API temporal de Hostinger usado para Bottega.
- [ ] Conectar pasarela de tarjeta real: WooPayments conectado o Stripe/Bizum con credenciales de Camila.
- [ ] Resolver Envia.es real: revisar credenciales, origen, paquetes, carriers/cobertura Madrid y por que no devuelve tarifas.
- [ ] Rotar la application password antigua que aparecia en `outputs/desarrollo/gas_formulario/Code.gs`.
- [ ] Subir imagenes reales a los 47 productos sin imagen, empezando por los mas vendidos.
- [ ] Configurar IVA/impuestos solo tras confirmacion fiscal de Camila/gestoria.
- [ ] Hacer prueba E2E de compra real: carrito, checkout, pago, email, estado de pedido y cancelacion/reembolso si aplica.

---

## Importante

- [ ] Configurar/validar GA4 + GTM con eventos de e-commerce, WhatsApp, llamada y formulario.
- [ ] Configurar Search Console + sitemap cuando se retire el `noindex`.
- [ ] Vincular web en Google Business Profile si sigue pendiente.
- [ ] Revisar plantillas WooCommerce obsoletas de Royal Elementor Addons con backup previo.
- [ ] Resolver `automatic_updater_disabled` con backup/Hostinger antes de activar updates automaticos.
- [ ] Enlazar paginas legales en footer: Aviso Legal, Privacidad, Devoluciones, Terminos y Condiciones.
- [ ] Revisar color base de emails WooCommerce para alinearlo con la marca.
- [ ] Definir estrategia factory para la tienda: staging o snapshot limpio, conservar configuracion WooCommerce/Envia/pagos, y eliminar dependencias raras de rewrite/Elementor solo con rollback claro.

---

## Rutina / siguiente fase

- [ ] Preparar Orden de Cambio para una capa visual Bottega controlada, cargada solo en tienda/categorias y sin afectar carrito/checkout.
- [ ] Validar visualmente tienda, carrito, checkout y movil despues de la limpieza de widgets.
- [ ] Decidir si se quiere reconstruir la sidebar de tienda con widgets utiles desde cero, manteniendo carrito/checkout/mi cuenta sin sidebar.
- [ ] Posponer ajuste de 12 productos por pagina hasta tener acceso de archivo/staging; el intento por opciones REST dejo el loop vacio y fue estabilizado de vuelta a 9 productos.
- [ ] Revisar visualmente `Tienda Test Bottega` version inline resistente: si el diseno convence, convertirlo en implementacion dinamica estable mediante plugin/snippet/template controlado antes de reemplazar `/tienda/`.
- [ ] Completar categorias vacias solo cuando existan productos claros publicados: Bebidas, Dulces, Conservas, Ofertas.
- [ ] Optimizar titles/metas/headings de categorias principales.
- [ ] Implementar schema LocalBusiness, Product, BreadcrumbList y FAQPage.
- [ ] Crear paginas locales: tienda italiana Madrid, mercado italiano Chamberi, productos italianos Madrid.
- [ ] Mejorar UX/UI movil de tienda, carrito y checkout tras estabilizar pagos/envios.
- [ ] Preparar propuesta comercial/alcance nuevo si el e-commerce no esta cubierto por contrato actual.

---

## Archivos de referencia vivos

- `outputs/auditorias/evaluacion-codigo-web-2026-05-03.md`
- `outputs/auditorias/puesta-operativa-woocommerce-2026-04-26.md`
- `outputs/auditorias/estabilidad-catalogo-woocommerce-2026-04-26.md`
- `outputs/auditorias/checkout-envia-audit-2026-04-26.md`
- `outputs/guias/2026-04-17_guia-pasarela-pago.md`
- `outputs/guias/2026-04-17_guia-analitica.md`

## Archivos que NO deben usarse como base actual

- `outputs/desarrollo/eselec-bottega-shop.zip` y carpeta `outputs/desarrollo/eselec-bottega-shop/`: plugin obsoleto; no instalar sin nueva Orden de Cambio.
- `outputs/desarrollo/redesign-bottega-2026/custom-css-tienda.css`: CSS historico; no pegar en WordPress ni usar como fuente viva.
- `outputs/desarrollo/redesign-bottega-2026/mockup-tienda.html` y `sidebar.html`: mockups historicos; conservar solo como referencia de exploracion.
