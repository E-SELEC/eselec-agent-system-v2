# Cliente: La Bottega del Gusto
**Última actualización:** 2026-04-26
**Gestor:** E-SELEC

---

## Snapshot técnico real — 2026-04-26
- WordPress/WooCommerce operativo vía API con usuario Codex separado (`eselec-codex`).
- URL pública, `site_url` y `home_url` corregidas a `https://bottegadelgustomadrid.com`.
- LiteSpeed Cache desactivado por Rodrigo; portada responde sin `X-LiteSpeed-Cache` y Hostinger CDN en estado `DYNAMIC`.
- Rank Math/Elementor: eliminadas URLs internas `http://bottegadelgustomadrid.com` en la home (página 576) y en el autor principal.
- `noindex`/`nofollow` en home y tienda confirmado como intencional hasta publicar la web; no corregir antes del go-live.
- WooCommerce: 170 productos publicados, 75 sin imagen, 0 sin precio (revalidado 2026-04-27).
- Envia: método `envia_shipping` activo en zona Madrid; mientras no devuelve tarifa, queda fallback operativo `Entrega en Madrid` a 5,90 EUR + `Recogida gratuita en tienda`.
- Checkout: T&C asignado a pagina `Terminos y Condiciones` (ID 3889); transferencia y pago en tienda activos; pago en tienda limitado a recogida.
- Categorias: `Quesos Italianos` operativo con 46 productos; `Bebidas`, `Dulces`, `Conservas` y `Ofertas` siguen vacias por falta de productos claros publicados.
- IVA/impuestos: clases creadas pero sin tasas configuradas. Envia no gestiona IVA; pendiente confirmación fiscal de Camila/gestoría.

**Nota de vigencia:** este snapshot sustituye cualquier dato histórico inferior que diga "170 productos", "e-commerce no operativo" o "envíos pendientes" como estado actual. Esas secciones se conservan como contexto histórico, pero el estado real de trabajo debe salir de este snapshot, `tasks.md` y `log.md`.

---

## Datos básicos
- **Nombre:** La Bottega del Gusto / Bottega del Gusto | Mercato Italiano Madrid
- **Contacto:** Camila
- **URL:** https://bottegadelgustomadrid.com/
- **Sector:** Alimentación / Gastronomía italiana
- **Tipo de negocio:** Tienda/mercado italiano presencial + e-commerce
- **Ubicación:** C. de San Bernardo, 108, Chamberí, 28015 Madrid
- **Teléfono:** +34 624 14 27 98
- **Horario:** L-S 9:00-21:00 / D 10:00-16:30
- **CMS:** WordPress + Elementor
- **Hosting:** Hostinger (cuenta E-SELEC — eselec.us@gmail.com)
- **Presupuesto mensual:** 550–600 €
- **Redes sociales:** Instagram + Facebook + TikTok
- **Identificación especial:** Negocio de mujer (women-owned, indicado en GMB)

---

## Descripción del negocio
Tienda italiana especializada en Chamberí (Madrid) con más de 800 productos importados directamente de Italia: pastas, salsas, quesos, embutidos, dulces, bebidas, conservas, y productos con denominación de origen (DOP/IGP). Venta presencial en tienda + tienda online en desarrollo. Entrega solo en Madrid (no envíos nacionales por ahora).

Público objetivo: amantes de la gastronomía italiana en Madrid y profesionales del sector (restaurantes, hostelería).

---

## Situación actual del proyecto
**Fase:** E-commerce activo pero incompleto. Optimización web en curso.

- WooCommerce ya instalado ✅
- 170 productos cargados en tienda online (de un catálogo físico de 800+)
- La mayoría de productos **sin imagen** — es la tarea más urgente del catálogo
- No hay pasarela de pago configurada aún — e-commerce no operativo
- GA4, GTM y Search Console: **sin configurar** ❌
- GBP activo ✅ — pero **sin website vinculado** (alerta crítica!)
- Diseño: verde oscuro con colores bandera italiana, logo "Charcutería Italiana"
- Categorías en tienda: Salsas y Conserva, Quesos Italianos, Pastas Italianas, Embutidos Italianos, Bebidas Típicas, Promociones y Ofertas

---

## Objetivos prioritarios (en orden)
1. **Vincular web en GMB** — quick win crítico (actualmente sin website en el perfil)
2. **Hacer el e-commerce operativo** — configurar pagos y envíos (Madrid)
3. **Completar imágenes del catálogo** — 170 productos, la mayoría sin foto
4. **Configurar GA4 + Search Console** — línea base de medición
5. **Optimizar UX/UI y responsive** — especialmente en móvil
6. **SEO local + orgánico + LLMs** — posicionamiento en Madrid (0 keywords actualmente)

---

## Servicios E-SELEC activos
- E-commerce WooCommerce (pagos, envíos, catálogo)
- SEO local, orgánico y LLM SEO
- UX/UI (sitewide)
- Responsive / Core Web Vitals
- CRO (conversión)
- GA4 + Search Console

---

## Auditoría SEO — Marzo 2026

### SEMRush
| Métrica | Valor | Notas |
|---------|-------|-------|
| Authority Score | 0 | Sin autoridad de dominio |
| Keywords orgánicas (ES) | 0 | No aparece en top 100 de Google España |
| Tráfico orgánico | 0 | Sin presencia en buscadores |
| Referring Domains | 18 | (SEMRush) |
| Backlinks | 23 | (SEMRush) |
| AI Mentions | 0 | Sin menciones en IA |

**Conclusión SEMRush:** El sitio NO tiene presencia orgánica en Google España. Punto de partida desde cero en SEO.

### Majestic (Fresh Index)
| Métrica | Valor |
|---------|-------|
| Trust Flow | 0 |
| Citation Flow | 5 |
| External Inbound Links | 6 |
| Referring Domains | 2 |

**Conclusión Majestic:** Perfil de enlaces prácticamente inexistente. Ninguna autoridad de enlace.

---

## Investigación de Keywords (España)

### Keywords objetivo principales
| Keyword | Volumen/mes | KD% | Intención | CPC |
|---------|------------|-----|-----------|-----|
| tienda italiana madrid | 480 | 35% | Commercial | €0.14 |
| tienda productos italianos madrid | 260 | 31% | Commercial | — |
| productos italianos madrid | 210 | 43% | Commercial | €0.11 |
| mercado italiano madrid | 170 | 40% | Navigational | €0.10 |
| tienda de productos italianos en madrid | 90 | 27% | Commercial | — |
| tiendas italianas en madrid | 170 | 32% | Commercial | — |
| tienda comida italiana madrid | 50 | 48% | Commercial | — |
| tienda italiana chamberi | 20 | n/a | — | — |

**Potencial total combinado:** ~1.400 búsquedas/mes en el nicho directo
**Quick win:** "tienda de productos italianos en madrid" (KD 27%) — más fácil de posicionar

---

## Competidores identificados

### casaitalia.es (Market Casa Italia)
- **Authority Score:** 8
- **Tráfico orgánico:** 117 visitas/mes
- **Keywords:** 25
- **Ref. Domains:** 72
- **Backlinks:** 116
- **AI mentions:** 34 (citado en Google.com, OpenTable, TripAdvisor)
- **Nota:** Domina "market casa italia - productos italianos en madrid" (590 búsquedas/mes)

**Brecha competitiva:** casaitalia.es tiene 72 dominios de referencia vs 18 de La Bottega. Con el GBP de 4.9⭐ (vs competidores más débiles), La Bottega tiene ventaja en reputación.

---

## Google My Business (GMB)
- **Estado:** Activo ✅
- **Nombre en GMB:** Bottega del Gusto | Mercato Italiano Madrid
- **Puntuación:** ⭐ 4.9 / 5
- **Reseñas:** 117
- **Categoría:** Italian grocery store
- **Dirección:** C. de San Bernardo, 108, Chamberí, 28015 Madrid
- **Teléfono:** +34 624 14 27 98
- **Website en GMB:** ❌ NO VINCULADO — muestra "Add website"
- **Identificación:** Negocio de mujer (women-owned)

**⚠️ ALERTA CRÍTICA:** El GBP no tiene la web vinculada. Esto reduce el tráfico desde Maps y elimina la señal de autoridad hacia la web. Vincular inmediatamente.

---

## Redes Sociales

### Instagram (@bottegadelgusto_madrid)
- **Seguidores:** 1.122
- **Publicaciones:** 289
- **Seguidos:** 115
- **Categoría:** Supermercado
- **Bio:** "La verdadera Italia en Madrid | L-S 9:00-21:00 / D 10:00-16:30 | C. de San Bernardo 108"
- **Estado:** Activo ✅

### Facebook (La Bottega Del Gusto)
- **Me gusta:** 338
- **Hablando de esto:** ~1
- **Categoría:** Grocery Store
- **Estado:** Poca actividad

### TikTok (@bottegadelgusto)
- **Seguidores:** ~30 (cuenta con poca actividad)
- **Estado:** Muy poca presencia

### TripAdvisor
- **Puntuación:** 4.4 / 5
- **Reseñas:** 55

---

## Google Search Console
- **Estado:** ❌ NO CONFIGURADO
- **GA4:** ❌ NO CONFIGURADO
- **GTM:** ❌ NO CONFIGURADO
- **Nota:** Sin datos históricos de rendimiento de búsqueda disponibles. Prioridad urgente configurar antes de iniciar SEO.

---

## Pasarela de pago (recomendación E-SELEC)
**Opción principal: Stripe**
- Mejor integración con WooCommerce
- Comisión: 1,4% + 0,25€ por tarjeta europea
- Soporta Apple Pay y Google Pay automáticamente
- Setup sencillo, UX excelente para el cliente final

**Opción secundaria: Bizum**
- Muy popular en España, especialmente en móvil
- Integrable vía plugin WooCommerce (Aplazame, Sipay, o TPV virtual bancario)
- Ideal para el público español que prefiere no usar tarjeta online

**No recomendado como principal: PayPal**
- Comisiones más altas (3,4% + 0,35€)

**Decisión pendiente de confirmar con Camila.**

---

## Envíos
- **Zona:** Madrid ciudad únicamente (no envíos nacionales de momento)
- **Tarifas:** Por definir con Camila (tarifa plana, gratis desde X€, por peso)
- **Recogida en tienda:** Por confirmar si se habilita

---

## Canales de conversión
- **Tienda online** (WooCommerce) — objetivo principal
- **WhatsApp** — contacto directo
- **Visita presencial** — tienda en Chamberí
- **GBP** — fuente de tráfico local (4.9⭐ 117 reseñas)

---

## Stack técnico
- CMS: WordPress + Elementor
- E-commerce: WooCommerce ✅ (instalado, sin pago configurado)
- Hosting: Hostinger (cuenta E-SELEC)
- Analytics: GA4 + GTM — ❌ pendiente
- Search Console — ❌ pendiente
- Schema: LocalBusiness + Product + BreadcrumbList (pendiente)

---

## Tono y comunicación
- Sofisticado pero cercano — pasión por la gastronomía italiana auténtica
- Evocador: calidad artesanal, origen, tradición italiana
- Local: referencias a Chamberí y Madrid
- CTA directo: comprar online o visitar la tienda

---

## Plan de acción — Año 1 (Prioridades)

### Semana 1 (Quick wins inmediatos)
1. **Vincular web bottegadelgustomadrid.com en GMB** — 10 min, impacto inmediato en Maps
2. **Instalar GA4 + GTM + Search Console** — línea base para medir todo lo que sigue
3. **Completar horas de apertura en GMB** — asegurar que son correctas

### Mes 1–2 (Fundamentos)
4. **Configurar Stripe** — hacer el e-commerce operativo
5. **Fotografiar los 170 productos** — sin imagen no hay conversión
6. **Optimizar GBP** — fotos, descripción, categorías adicionales

### Mes 2–4 (SEO base)
7. **Crear páginas de categoría optimizadas** — una por categoría de producto (pasta, quesos, embutidos...)
8. **Optimizar homepage** — targeting "tienda italiana madrid" (480/mes, KD 35%)
9. **Schema LocalBusiness** — ayuda inmediata al CTR en resultados locales
10. **Link building inicial** — directorios de alimentación, blogs gastronómicos italianos en España

---

## Historial del proyecto
| Fecha | Acción |
|---|---|
| 2026-03-23 | Context.md creado. WooCommerce instalado, 170 productos sin imagen, sin pasarela de pago. |
| 2026-03-23 | GBP activo confirmado. GA4 y Search Console pendientes. |
| 2026-03-27 | Auditoría completa: SEMRush (0 keywords, AS 0), Majestic (TF 0, CF 5), GMB (4.9⭐ 117 reseñas, web no vinculada), Instagram (1.122 seguidores, 289 posts), Facebook (338 likes), TripAdvisor (4.4⭐ 55 reseñas). |

---

## Integraciones
| Servicio | ID / URL | Estado |
|---|---|---|
| GA4 | Pendiente configurar | ❌ No instalado |
| GTM | Pendiente configurar | ❌ No instalado |
| GSC | bottegadelgustomadrid.com | ❌ No configurado |
| GBP | Activo (sin web vinculada) | ⚠️ Requiere vincular URL |
| Meta Ads | No aplica | — |

---

## Notas para los agentes
- **Quick win #1:** Vincular bottegadelgustomadrid.com en el GBP — está sin website
- **Quick win #2:** Instalar GA4 + GSC antes de empezar cualquier SEO
- **SEO parte desde cero** — 0 keywords en top 100, 0 backlinks de calidad
- **Reputación excelente:** 4.9⭐ 117 reseñas GMB + 4.4⭐ 55 en TripAdvisor — explotar en contenido
- **Instagram activo:** 1.122 seguidores, 289 posts — base social para crecer
- **Keyword estrella:** "tienda italiana madrid" (480/mes, KD 35%) — objetivo principal Mes 2-3
- **Competidor clave:** casaitalia.es (Market Casa Italia) — 117 tráfico/mes, 72 ref domains
- Entrega solo Madrid — no mencionar envíos nacionales en ningún contenido
- El catálogo físico son 800+ productos pero online hay 170 — priorizar los más vendidos con foto primero
- Siempre mencionar autenticidad italiana, DOP/IGP y la ubicación en Chamberí como diferenciadores
- Contacto del cliente: Camila
- Negocio de mujer (women-owned) — diferenciador para comunicación y posibles menciones en medios

---

Memoria de aprendizajes: ver memory.md
