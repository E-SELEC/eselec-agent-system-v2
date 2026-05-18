# Memoria de aprendizajes — Chashier Bubble Tea & Coffee

## Qué ha funcionado
- **Tráfico orgánico SEO:** +193% YoY (de ~3.000 a 9.300 visitas/mes estimadas SEMRush). La estrategia de contenido y SEO orgánico ha dado resultados claros.
- **SEO Local GMB:** Mantenimiento constante. GMB en 4.9⭐ con 331 reseñas — uno de los activos más fuertes del cliente.
- **Impresiones x20 en 18 meses** (GSC): la base de visibilidad creció enormemente aunque el CTR no acompañó.
- **AI Search:** 19 menciones en resultados de IA (ChatGPT: 6, AI Overview: 4, Gemini: 2) — presencia incipiente pero real.
- **Conector WordPress REST API:** Application Passwords configuradas en functions.php de Astra, Rank Math integrado en REST API, permite edición programática de metadatos y schemas.
- **Schema FoodEstablishment** implementado en homepage y verificado en frontend.
- **Canonical homepage fijado** — resolvió conflicto detectado en GSC.
- **Títulos/metas del blog optimizados:** Post "Qué es el té de burbujas" corregido con focus keyword correcto.
- **Timestamps de posts actualizados** para señales de frescura.

## Qué NO ha funcionado
- **CTR crítico:** A pesar de las impresiones creciendo, el CTR bajó a 0.2% (256 clics / 128.000 impresiones en 3 meses). Clicks en tendencia bajista desde pico de mar 2025.
- **Backlinks de baja calidad:** 63% de los 80 dominios referenciados provienen de Singapur (posibles PBNs). Trust Flow Majestic = 0. La estrategia de link building anterior generó backlinks que pueden ser contraproducentes.
- **Bots de captación de tráfico:** Discontinuados por presupuesto — no escalan ni son sostenibles.
- **"Té de burbujas" sin optimizar:** 2.900 búsquedas/mes pero posición 21 — la URL del blog no está atacando bien esta keyword de alto volumen.
- **Páginas con noindex:** Detectadas en GSC en nov 2024 y ago 2025 — error técnico que limitó la indexación.
- **GA4:** Estado desconocido — no se puede medir conversiones reales desde web.

## Preferencias del cliente
- **Contacto:** Gemma Ye (dueña) — relación directa con Rodrigo.
- **Relación activa y de confianza:** Gemma ha confirmado que quiere continuar en Año 3.
- **Comunicación:** WhatsApp como canal habitual (ver resumen WhatsApp en outputs de informes).
- **Presupuesto:** Actualmente 300€/mes. Hosting y dominio asumidos por Rodrigo (pendiente regularizar en propuesta Año 3).
- **Servicios no contratados:** Google Ads y Meta Ads — solo a demanda.
- **Decisiones de marketing:** Confía en E-SELEC — no es un cliente que interfiera mucho.

## Insights de negocio
- **Estacionalidad:** Pico de tráfico en primavera (marzo-mayo). Caída en verano (julio-agosto) y dic-ene. Los informes deben reflejar esto para no alarmar al cliente.
- **Competidor líder inalcanzable a corto plazo:** coco-tea.es con 44.800 visitas/mes. El objetivo realista es superar a momobubbletea.com (6.300/mes) a 12 meses.
- **Mercado mixto:** Local físico en Chamberí + delivery (Glovo, Uber Eats, Just Eat) — el SEO debe atacar intent transaccional y local simultáneamente.
- **Posicionamiento diferencial:** Autenticidad taiwanesa, +12 variedades de bubble tea personalizables con toppings.
- **Delivery activo en 3 plataformas:** tener en cuenta que el cliente convierte tanto en tienda como online.
- **Público objetivo:** Jóvenes y adultos interesados en tendencias foodie/cultura asiática en Chamberí y Madrid.

## Reglas operativas aprendidas
- **Nombre correcto del cliente es "Chashier"** (no "Cashier") — la carpeta del sistema tiene typo.
- **Hosting/dominio en manos de Rodrigo** — cualquier propuesta económica nueva debe incluir la regularización de este coste.
- **GA4 y GBP:** Estado desconocido — verificar antes de generar informes de tráfico.
- **Acceso GSC:** vía cuenta chashier.es@gmail.com.
- **Conector WordPress activo:** Application Passwords en functions.php, Rank Math integrado — usar wp_connector para ediciones programáticas.
- **Antes de cualquier trabajo nuevo:** verificar si el informe de resultados del período ya existe en outputs/.
- **Aprobación requerida antes de crear páginas en WordPress:** el output de contenido ya está en outputs/ pero requiere aprobación de Rodrigo antes de publicar (ver log 2026-04-20).
- **Disavow backlinks tóxicos:** requiere export previo de SEMRush — no ejecutar sin ese archivo.
- **Seraphinite Accelerator** puede estar afectando Core Web Vitals — revisar antes de cualquier auditoría CWV.

## Próximas hipótesis a probar
- **Crear página /te-de-burbujas/** (2.900 búsquedas/mes, pos 21): si se crea con contenido optimizado, debería entrar en top 5 y generar +200 visitas/mes adicionales. Contenido ya preparado en outputs/seo-organico-2026-04-20.md.
- **Crear página /bubble-tea-madrid/** (1.600 búsquedas/mes, pos 5): con contenido localizado debería consolidar posición y atraer tráfico transaccional.
- **Disavow backlinks tóxicos:** si el Trust Flow sube de 0, debería mejorar la autoridad percibida y el ranking de keywords competitivas.
- **Optimizar CTR:** mejoras de title/description en páginas principales — hipótesis: el CTR bajo (0.2%) se puede triplicar con mejor copy en snippets.
- **Propuesta Año 3:** incluir regularización hosting/dominio + posiblemente email marketing como nuevo servicio.

## Historial de versiones
- [2026-04-21] Memory.md creado. Extraído de context.md (2026-03-26), log.md (sesiones mar-abr 2026) y tasks.md (2026-04-06).
