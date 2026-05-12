# Event Taxonomy - E-SELEC

## Marketing / Lead Gen

| Evento | Decision que informa | Propiedades |
|---|---|---|
| `cta_clicked` | que CTAs generan intencion | `cta_location`, `cta_text`, `page_location` |
| `form_started` | friccion inicial de formularios | `form_name`, `form_location` |
| `form_submitted` | leads generados | `form_name`, `lead_type`, `service_category` |
| `form_error` | errores de conversion | `form_name`, `error_type` |
| `phone_clicked` | intencion de llamada | `page_location`, `cta_location` |
| `whatsapp_clicked` | intencion por WhatsApp | `page_location`, `cta_location`, `service_category` |
| `email_clicked` | contacto por email | `page_location`, `cta_location` |

## SEO / Contenido

| Evento | Decision que informa | Propiedades |
|---|---|---|
| `internal_link_clicked` | enlaces internos utiles | `link_url`, `link_text`, `location` |
| `resource_downloaded` | valor de recursos | `resource_name`, `resource_type` |
| `scroll_depth` | engagement de contenido | `depth`, `page_location` |
| `site_search` | demanda interna | `search_term`, `results_count` |

## E-commerce / WooCommerce

| Evento | Decision que informa | Propiedades |
|---|---|---|
| `view_item` | interes por producto | `item_id`, `item_name`, `item_category`, `price` |
| `add_to_cart` | intencion de compra | `item_id`, `item_name`, `price`, `quantity` |
| `begin_checkout` | inicio de checkout | `cart_value`, `items_count` |
| `purchase_completed` | ventas reales | `transaction_id`, `value`, `currency`, `items` |
| `purchase_failed` | friccion tecnica | `error_type`, `payment_method` |

## Ads / Paid Media

| Evento | Decision que informa | Propiedades |
|---|---|---|
| `lead_generated` | optimizacion de campanas | `lead_type`, `source`, `medium`, `campaign` |
| `booking_requested` | leads cualificados | `service_category`, `source`, `medium` |
| `quote_requested` | intencion comercial | `service_category`, `estimated_value` |

## Reglas

- Usar eventos recomendados por GA4 cuando existan.
- Mantener nombres en ingles y snake_case.
- No meter ubicacion o pagina en el nombre del evento; usar propiedades.
- No enviar PII.
- Diferenciar evento de conversion: no todo evento debe ser conversion.
