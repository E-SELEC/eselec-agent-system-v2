# Memoria de aprendizajes — La Bottega del Gusto

## Qué ha funcionado
- **GBP con reputación excelente:** 4.9⭐ con 117 reseñas GMB + 4.4⭐ en TripAdvisor — activo diferencial clave frente a competidores con peor reputación.
- **Instagram activo:** 1.122 seguidores, 289 posts — base social orgánica ya construida. Categoría correcta como "Supermercado".
- **WooCommerce instalado y configurado:** Se logró activar la base del e-commerce (BACS/BBVA, COD, zonas de envío Madrid, emails transaccionales, páginas legales) con datos reales de Camila.
- **Application Passwords WordPress:** Configuradas vía functions.php del tema Astra, usuario eselec-api creado. El wp_connector.py funciona y está operativo.
- **Entregables generados para implementación directa:** schema markup JSON-LD listo para pegar (LocalBusiness, BreadcrumbList, FAQPage), instrucciones WooCommerce completas, guía Stripe+Bizum, guía GA4+GTM+GSC, checklist go-live.
- **Formulario Google Apps Script:** Desplegado y completado por Camila — datos reales obtenidos (Marketitalia España SL / B75792119).
- **Metodología de cuestionario cliente:** El formulario GAS v4 funcionó para desbloquear datos fiscales y de configuración sin llamadas.

## Qué NO ha funcionado
- **Bloqueadores del cliente (Camila):** La pasarela de pago (Stripe/Bizum), las imágenes de los 170 productos, el email de Envia.com y el logo para emails siguen pendientes de Camila. El ritmo de avance depende de su disponibilidad.
- **GA4, GTM y Search Console:** Sin configurar — no hay ninguna línea base de medición. Todo trabajo SEO se hace sin datos de referencia.
- **GBP sin web vinculada (al inicio):** Era el quick win más crítico — alerta detectada en auditoría inicial. Pendiente confirmar si ya se vinculó.
- **E-commerce no operativo:** A pesar de WooCommerce instalado, sin pasarela de pago el e-commerce no genera ingresos todavía.
- **Facebook y TikTok ignorados:** Facebook (338 likes) y TikTok (30 seguidores) prácticamente inactivos — decisión correcta de no invertir recursos ahí por ahora.
- **170 productos sin imagen:** Sin fotos no hay conversión en e-commerce — bloqueador principal del catálogo.

## Preferencias del cliente
- **Contacto:** Camila — propietaria, responde a cuestionarios estructurados (formulario GAS probado).
- **Negocio de mujer (women-owned):** Identificación especial en GMB — diferenciador para comunicación y posibles menciones en medios.
- **Tono de la marca:** Sofisticado pero cercano. Evocador de calidad artesanal, origen italiano, tradición. CTA directo: comprar online o visitar tienda.
- **Zona de entrega:** Solo Madrid ciudad (no envíos nacionales) — nunca mencionar envíos nacionales en ningún contenido.
- **Presupuesto:** 550-600€/mes — cliente de ticket medio-alto para E-SELEC.
- **Identificación fiscal:** Marketitalia España SL / B75792119 — datos reales obtenidos y operativos.

## Insights de negocio
- **Catálogo físico vs online:** 800+ productos físicos, 170 cargados online sin imagen — la brecha entre catálogo real y tienda online es enorme. Priorizar los más vendidos.
- **Competidor clave:** casaitalia.es (Market Casa Italia) — 72 ref domains vs 18 de La Bottega, pero La Bottega tiene mejor reputación (4.9⭐ vs competidores más débiles).
- **Keyword estrella:** "tienda italiana madrid" (480/mes, KD 35%) — objetivo principal mes 2-3 de SEO.
- **Quick win de mayor impacto:** "tienda de productos italianos en madrid" (KD 27%) — más fácil de posicionar.
- **Potencial total del nicho:** ~1.400 búsquedas/mes combinadas — mercado pequeño pero muy específico y con alta intención de compra.
- **SEO parte desde cero:** 0 keywords en top 100, Authority Score 0, Trust Flow 0 — todo está por construir.
- **Público dual:** Consumidores finales amantes de gastronomía italiana + profesionales (restaurantes, hostelería).
- **Diferenciadores clave:** Productos DOP/IGP, 800+ referencias, importación directa de Italia, ubicación en Chamberí.

## Reglas operativas aprendidas
- **Astra editor manda sobre el contenedor visual de paginas test:** El 2026-05-03 Rodrigo enderezo `Tienda Test Bottega` desde el editor de pagina > icono Astra > Contenedor, dejando la pagina en modo visual correcto con `site-content-layout=page-builder`, `site-content-style=unboxed`, `ast-site-content-layout=default` y `site-sidebar-layout=default`. No confundir `ast-site-content-layout=full-width-container` con la solucion: en este caso la combinacion estable fue page-builder + sin caja desde UI. Antes de pelear con CSS/HTML en paginas Astra, verificar y fijar primero estos ajustes desde el panel de Astra.
- **Tienda Bottega depende de rewrite para verse como archivo:** El 2026-05-03 se confirmo que `/tienda/` necesita una regla `tienda/?$ => index.php?post_type=product` para comportarse como archivo WooCommerce. Si esa regla falta, WordPress trata `/tienda/` como pagina singular `page-id-687` y puede mostrar un loop vacio. No limpiar metadata de Tienda ni tocar rewrite sin verificar body class `post-type-archive-product` despues.
- **No forzar productos por pagina via opciones REST:** El 2026-05-03 Astra tenia `shop-no-of-products=12`, pero el frontend seguia en 9. Intentar forzar `woocommerce_catalog_columns/rows` desde `wc-admin/options` dejo el loop vacio; se restauro visibilidad via rewrite. Para cambiar a 12, usar acceso de archivo/staging y un filtro controlado `loop_shop_per_page`, o resolver primero la dependencia de rewrite en un entorno seguro.
- **Evaluacion de codigo web 2026-05-03:** home y tienda responden `DYNAMIC`, por lo que el problema actual no apunta a cache HTML vieja. La capa conflictiva esta en widgets activos de `astra-woo-shop-sidebar`: `block-13` contiene sidebar/busqueda/categorias manuales `bdg-*` y `block-18` contiene CSS `bdg-cards` con reglas globales para cards WooCommerce. Astra declara que esa sidebar se usa tambien en carrito, checkout y mi cuenta, asi que cualquier CSS ahi puede contaminar flujos de venta. No limpiar sin Orden de Cambio.
- **Productos WooCommerce siempre paginados:** el Store API publico marca 170 productos publicados y 2 paginas. El comando interno `wc-products` puede devolver solo 100 si no se pagina, asi que no usar esa cifra como total real sin revisar cabeceras `X-WP-Total` o paginar.
- **Acceso Codex separado:** Desde 2026-04-26 Codex usa el usuario WordPress `eselec-codex` con application password propia y WooCommerce via `wc_auth=wp_app_password` en `scripts/wp_connector.py`. Claude/otros agentes deben usar su propio usuario/API separado.
- **Noindex intencional pre-lanzamiento:** Rodrigo confirmó el 2026-04-26 que el `noindex`/`nofollow` en home y tienda es deliberado hasta finalizar y publicar la web. No corregirlo como error antes del go-live.
- **Envia activo, IVA separado:** Envia ya está activo como método `envia_shipping` en la zona Madrid. No confundir con impuestos: Envia resuelve logística/envíos; IVA se configura en WooCommerce con tasas y clases de producto, pendiente de confirmación fiscal de Camila/gestoría.
- **Fallback operativo de entrega Madrid:** Desde 2026-04-26, mientras Envia no devuelve tarifas, la zona Madrid tiene `Recogida gratuita en tienda` y `Entrega en Madrid` a 5,90 EUR. La recogida global sin ubicaciones quedo desactivada para no aparecer fuera de Madrid.
- **T&C correcto:** WooCommerce usa la pagina `Terminos y Condiciones` ID 3889. No volver a asignar `Politica de Devoluciones` como T&C.
- **Categoria Quesos operativa:** `Quesos Italianos` ya contiene 46 productos evidentes de queso. `Bebidas`, `Dulces`, `Conservas` y `Ofertas` siguen vacias porque el catalogo publicado actual no contiene productos claros para esas categorias.
- **HTTPS interno corregido:** El 2026-04-26 se corrigieron `home_url`, URL del autor y URLs internas de Elementor/home de HTTP a HTTPS. Si reaparece el aviso de Rank Math, revisar primero Ajustes Generales (`home`) y `_elementor_data` de la página 576.
- **Cambios Elementor no visibles:** El 2026-04-26 se detecto que el HTML no estaba cacheado (`x-hcdn-cache-status: DYNAMIC`), pero los CSS/JS estaticos de Hostinger CDN tenian `max-age=604800` (7 dias). Se limpio cache Elementor via `/wp-json/elementor/v1/cache` y se cambio `elementor_css_print_method` a `internal` para desarrollo, evitando depender de archivos `/uploads/elementor/css/post-*.css` cacheados. Al go-live, evaluar volver a `external` + purga CDN para rendimiento.
- **Customizer tienda pisado por CSS manual:** El 2026-04-26 se detecto que la tienda tenia un widget manual `block-16` en `astra-woo-shop-sidebar` con `<style id="bdg-cards">` y muchas reglas `!important` + JS inline, bloqueando cambios hechos desde `Apariencia > Personalizar > WooCommerce`. Se movio `block-16` a widgets inactivos. Si Rodrigo edita desde Customizer, no reactivar ese bloque salvo que se quiera volver al CSS custom.
- **Lineas divisorias tienda:** Las lineas vertical/horizontal vistas en tienda venian de bordes por defecto de Astra (`#secondary` con sidebar izquierda y `.ast-archive-description` vacia). Se ocultaron solo en archivo de tienda con CSS puntual dentro de `block-13`.
- **Layout tienda con sidebar:** El 2026-04-27 se ajusto la tienda para que la sidebar tenga ancho fijo razonable y el grid de productos no quede empujado a la derecha. CSS en `block-13`: 4 columnas en desktop, 5 columnas en pantallas anchas (>=1800px), 3 columnas en desktop estrecho, 2 tablet y 1 movil.
- **Mobile tienda:** El 2026-04-27 se aplico CSS mobile-first en `block-13`: en movil el catalogo/productos aparece antes que la sidebar, las cards son compactas, el selector de orden ocupa ancho completo, el grid usa 2 columnas cuando cabe y 1 columna en pantallas muy estrechas. La sidebar/filtros baja debajo del catalogo y solo deja visible busqueda para reducir friccion.
- **Plugin tienda propia recomendado:** Debido a friccion continua con Astra/Customizer/widgets/CSS manual, el 2026-04-27 se creo el plugin instalable `E-SELEC Bottega Shop` en `outputs/desarrollo/eselec-bottega-shop.zip`. Renderiza una tienda independiente mediante shortcode `[eselec_bottega_shop per_page="20"]`, con filtros dinamicos, grid responsive, add-to-cart WooCommerce y sin depender del archivo nativo de Astra.
- **Reversion tienda nativa:** El 2026-04-27 se retiro de `block-13` el CSS reciente de layout/mobile/divisorias y se dejo activo `block-18` como bloque visual de cards (`bdg-cards`). `block-16` queda inactivo para no duplicar el mismo CSS. Tambien se restauro la regla de permalink de `/tienda/` para que vuelva a cargar el archivo de productos; si desaparecen productos otra vez, revisar primero `rewrite_rules` antes de tocar WooCommerce/Envia.
- **Hostinger cache stale puede simular web rota:** El 2026-04-27, tras restores de Hostinger, se confirmo que Elementor/home seguia correcta pero la raiz `/` podia servir HTML viejo desde Hostinger/LiteSpeed/CDN (`x-hcdn-cache-status: HIT`, `X-LiteSpeed-Cache: hit`, Astra 4.11.12). Antes de restaurar archivos/base de datos por problemas visuales, ejecutar `python scripts/hostinger_connector.py audit --domain bottegadelgustomadrid.com` y purgar hPanel Cache Manager/CDN si aparece cache stale.
- **Hostinger API temporal validada:** La API publica permite listar sitio/dominio/hosting (`u594903472`, root `/home/u594903472/domains/bottegadelgustomadrid.com/public_html`), pero no expone endpoint oficial verificado para purgar Cache Manager/CDN. La purga sigue siendo manual desde hPanel salvo que Hostinger publique endpoint o se active una integracion/plugin especifico con aprobacion.
- **Conteo catalogo real:** El conector anterior leia solo la primera pagina de 100 productos. Tras paginar WooCommerce correctamente, el catalogo real es 170 productos publicados, 0 sin precio y 82 sin imagen.
- **Camila es el cuello de botella principal:** decisiones de pasarela de pago, imágenes, datos fiscales, email Envia.com y logo dependen de ella. Planificar con margen de espera.
- **Hosting en cuenta E-SELEC (Hostinger):** eselec.us@gmail.com — tener en cuenta en cualquier acceso técnico.
- **wp_connector.py activo:** Codex usa `eselec-codex` con App Password propia. El usuario `eselec-api` queda como acceso legado/otros agentes.
- **Email receptor de pedidos:** labottegadelgusto.madrid@gmail.com.
- **Envíos:** Zona Madrid con Envia activo (`envia_shipping`) + recogida gratuita en tienda. No comunicar envíos nacionales.
- **Zona de entrega:** Solo Madrid ciudad — regla estricta de comunicación.
- **Siempre mencionar:** autenticidad italiana, DOP/IGP, ubicación en Chamberí como diferenciadores.
- **Footer legal:** Enlazar Aviso Legal (ID 3427), Privacidad (ID 3428), Devoluciones (ID 3429) — páginas ya creadas y publicadas.

## Próximas hipótesis a probar
- **Vincular web en GBP:** Si se vincula bottegadelgustomadrid.com en el perfil de Google Business, debería aumentar inmediatamente el tráfico desde Maps y la señal de autoridad hacia la web.
- **Activar Stripe:** Con pasarela de pago activa, el e-commerce empezará a convertir visitas en ingresos — primera validación real del canal online.
- **Schema LocalBusiness en homepage:** Debería mejorar CTR en resultados locales desde el momento de implementación.
- **Fotografiar productos más vendidos primero:** Hipótesis: los 20 productos más populares con foto buena generarán el 80% de las ventas online.
- **Ranking "tienda italiana madrid":** Con contenido optimizado en homepage y backlinks iniciales en directorios gastronómicos, debería entrar en top 10 en 3-4 meses.

## Historial de versiones
- [2026-04-21] Memory.md creado. Extraído de context.md (2026-03-27), log.md (sesiones mar-abr 2026) y tasks.md (2026-04-06).
