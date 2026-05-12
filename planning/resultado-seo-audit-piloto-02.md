# Resultado seo-audit piloto 02 - Computer Chamberi

## Estado

- Fecha: 2026-05-12
- Cliente: `computer-chamberi`
- Dominio: `https://www.computerchamberi.com/`
- Skill usada: `.claude/skills/seo-audit/`
- Nivel de datos: parcial fuerte
- Fuentes usadas: contexto v2, log v2, memoria v2, mensajes v2, `evidencia-seo-2026-05-12.md`, auditoria on-page legacy estatica
- Produccion tocada: no
- Herramientas vivas usadas: no
- Estado: prueba de sistema, no entregable final al cliente

# Auditoria SEO: Computer Chamberi

**Fecha:** 2026-05-12
**Nivel de datos:** parcial fuerte
**Fuentes usadas:** GSC legacy resumido, SEMrush legacy resumido, auditoria on-page estatica legacy, context, log, memoria
**Alcance:** dominio completo con foco en caida organica, CTR, homepage y paginas de servicio

## 1. Resumen ejecutivo

Computer Chamberi tiene una base SEO real: marca posicionada, volumen alto de impresiones, oportunidad clara en CTR y demanda en clusters como Xiaomi, Amazfit y GoPro. El problema dominante no es falta de ideas, sino riesgo de decidir con datos no revalidados: los outputs legacy recientes apuntan a caida organica, CTR bajo y alta dependencia de homepage, pero hay que confirmar periodo y unidades en GSC antes de ejecutar.

Decision recomendada: tratar esta auditoria como parcial fuerte. Preparar cambios, pero no tocar titles/metas, contenido, schema, WordPress ni homepage hasta revalidar GSC/SEMrush y abrir Orden de Cambio.

## 2. Top 3 problemas prioritarios

| Prioridad | Problema | Evidencia | Impacto | Esfuerzo | Fix recomendado |
|---|---|---|---|---|---|
| 1 | Caida organica sin causa confirmada | SEMrush legacy reporta trafico estimado de 4.200/mes a 3.200/mes (-24%) y GSC agregado muestra posicion media empeorando de 9,6 a 10,1 | alto | bajo | Revalidar GSC por fechas y paginas, cruzar con SEMrush actual antes de diagnosticar causa |
| 2 | CTR bajo sobre volumen alto de impresiones | GSC legacy agregado declara 637.000 impresiones/3 meses, CTR medio 1%; homepage con CTR bajo y gran dependencia de trafico | alto | bajo-medio | Validar top URLs en GSC, revisar title/meta actuales y preparar Orden de Cambio para top 5 |
| 3 | Trafico demasiado concentrado y clusters infraexplotados | SEMrush legacy reporta homepage con 86.9% del trafico estimado; evidencia legacy muestra demanda en Amazfit, Xiaomi y GoPro | alto | medio | Reforzar paginas de servicio e interlinking tras validar medicion y ausencia de bloqueo tecnico |

## 3. Hallazgos tecnicos

| Area | Estado | Evidencia | Accion |
|---|---|---|---|
| Crawlability | parcial ok | auditoria estatica: status 200, robots meta `follow,index` | Confirmar con crawl/render antes de cambios masivos |
| Indexacion | riesgo | SEMrush legacy reporta 240 paginas organicas; GSC legacy analiza muchas URLs, pero no hay consulta viva | Revalidar cobertura/indexacion en GSC |
| Sitemap/robots | riesgo | auditoria estatica detecta robots.txt y sitemap.xml, pero sitemap reporta 4 URLs y 20 reglas Disallow | Revisar sitemap real y cobertura antes de arquitectura |
| Canonicals/redirecciones | parcial ok | canonical homepage apunta a `https://www.computerchamberi.com/` | Revisar canonicals de paginas prioritarias |
| Core Web Vitals | no verificado | no hay PageSpeed/CWV en v2 | Ejecutar PageSpeed/CrUX antes de priorizar performance |
| Mobile/render | parcial | viewport presente, pero auditoria fue por requests | Revisar render mobile real antes de UX/CRO |
| Schema | parcial, no final | auditoria estatica detecta LocalBusiness, FAQPage y otros; recomienda BreadcrumbList/WebPage | No afirmar ausencia; verificar con render o Rich Results Test |

## 4. Hallazgos on-page y contenido

| Pagina / seccion | Hallazgo | Evidencia | Accion |
|---|---|---|---|
| Homepage `/` | Dependencia excesiva y CTR bajo | SEMrush legacy: 86.9% del trafico estimado; GSC legacy: homepage con volumen alto y CTR bajo | Validar GSC actual y preparar mejora title/meta + enlazado interno bajo Orden de Cambio |
| Homepage title/meta/H1 | La keyword objetivo exacta no aparece en title/meta/H1 | auditoria on-page estatica 2026-05-07 | Ajustar solo si coincide con estrategia de queries reales, no por keyword stuffing |
| Paginas informacionales | Ranking alto con CTR muy bajo probable por snippet/AI answer | CTR audit legacy: paginas en posiciones 1-5 con CTR 0.1%-0.4% | Reescribir titles para prometer valor adicional, no solo cambiar metas |
| Categorias de servicio | Mal ranking + bajo CTR en categorias clave | CTR audit legacy: reparacion moviles, iPhone, ordenadores, portatiles, Samsung con CTR bajo y posiciones medias/altas | Combinar mejora on-page, contenido e interlinking |
| Xiaomi/Amazfit/GoPro | Demanda organica con margen de crecimiento | evidencia saneada: Xiaomi crece, Amazfit/GoPro muestran clics e intencion | Priorizar mejoras de paginas existentes antes de crear muchas URLs nuevas |

## 5. Autoridad, competencia, local o AI Search

- Autoridad/backlinks: SEMrush/Majestic legacy indican 1.3K referring domains, 11.5K backlinks, Authority Score 16 y Trust Flow 0. Interpretacion: hay volumen, pero la calidad parece baja. No iniciar link building hasta tener plan editorial/local claro.
- Competidores/gaps: legacy detecta competidores como `repararpcmicrocomputer.es`, `doctoresdelpc.com` y `spanishcomputers.com`. Usar para comparar snippets y servicios, no para copiar estructura.
- Local/GBP: contexto/memoria indican GBP fuerte, pero no se verifico vivo en esta sesion. Mantener SEO local como activo, sin tocar GBP.
- AI Search/LLM: no evaluado en esta auditoria.

## 6. Matriz impacto/esfuerzo

| Accion | Impacto | Esfuerzo | Orden | Dependencia |
|---|---|---|---|---|
| Revalidar GSC por periodo, unidades y top URLs | alto | bajo | 1 | acceso GSC aprobado |
| Cruzar SEMrush actual con GSC | alto | bajo-medio | 2 | acceso SEMrush/export |
| Validar title/meta actuales de top 5 paginas | alto | bajo | 3 | WordPress solo lectura o navegador |
| Preparar Orden de Cambio para metas top 5 | alto | bajo | 4 | aprobacion Rodrigo |
| Revisar sitemap/cobertura y render mobile | medio-alto | medio | 5 | crawl/render/PageSpeed |
| Mejorar paginas Amazfit/GoPro/Xiaomi | alto | medio | 6 | medicion validada + no bloqueo tecnico |
| Plan de autoridad local/editorial | medio-alto | alto | 7 | diagnostico autoridad confirmado |

## 7. Plan de accion priorizado

### Ahora

1. Revalidar GSC: confirmar si las cifras de impresiones son mensuales o de 91 dias, y exportar top URLs/queries saneado.
2. Revalidar SEMrush: confirmar tendencia actual y competidores.
3. No ejecutar ningun cambio en WordPress todavia.

### Proximos 7 dias

1. Preparar cambio controlado para top 5 titles/metas solo despues de validar title/meta actual.
2. Revisar sitemap/cobertura y render mobile.
3. Priorizar homepage, `reparacion-moviles`, BitLocker, teclado portatil y una pagina de servicio segun GSC validado.

### Proximos 30 dias

1. Expandir o mejorar paginas de servicio con demanda confirmada: Amazfit, GoPro, Xiaomi.
2. Fortalecer enlazado interno desde homepage hacia paginas de servicio.
3. Definir plan de autoridad editorial/local si se confirma baja calidad de backlinks.

## 8. Datos faltantes y como obtenerlos

| Dato faltante | Por que importa | Como obtenerlo |
|---|---|---|
| GSC vivo por fechas y top URLs | confirma caida, CTR y unidades | export saneado o acceso aprobado |
| SEMrush actual | confirma si la caida sigue activa | export o captura verificada |
| GA4/eventos/conversiones | necesario para hablar de leads/CRO | verificar propiedad/eventos sin copiar secretos |
| PageSpeed/Core Web Vitals | necesario para priorizar performance | PageSpeed/CrUX |
| Render/schema validado | evita conclusiones falsas sobre schema | navegador renderizado o Rich Results Test |
| GBP vivo | necesario para SEO local final | acceso/captura aprobada |

## Estado de la auditoria

Parcial fuerte.

Puede usarse para priorizar trabajo interno y preparar el siguiente paso. No debe entregarse como auditoria final al cliente ni usarse para ejecutar cambios de produccion.

## Siguiente paso

Revalidar GSC y SEMrush con periodo claro. Si Rodrigo aprueba, convertir el top 5 de CTR en una Orden de Cambio separada antes de tocar WordPress.

## Revision de calidad

- Nivel de calidad estimado: 3 como prueba interna.
- Motivo: usa evidencia, declara limites, separa fuentes, prioriza y bloquea produccion.
- Limite principal: no usa fuentes vivas; por eso no es auditoria final.
