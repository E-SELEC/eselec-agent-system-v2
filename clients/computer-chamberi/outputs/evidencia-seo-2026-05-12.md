# Evidencia SEO saneada - Computer Chamberi

## Estado

- Fecha de creacion: 2026-05-12
- Fuente: outputs legacy de `clients/computer-chamberi/outputs/`
- Uso: soporte para `seo-audit` v2 y `verificacion-medicion`
- Nivel de medicion resultante: 2 - parcial fuerte
- Produccion tocada: no
- Datos vivos consultados en esta sesion: no
- Exports brutos copiados: no

## Fuentes legacy leidas

| Archivo legacy | Fecha | Fuente declarada | Uso en v2 |
|---|---|---|---|
| `auditoria-seo-2026-05-07.md` | 2026-05-07 | SEMrush 3 Espana Desktop | tendencia, paginas, autoridad, competidores |
| `estrategia-seo-2026-05-07.md` | 2026-05-07 | SEMrush + Google Search Console Feb-May 2026 | estrategia, GSC agregado, oportunidades |
| `ctr-audit-2026-05-07.md` | 2026-05-07 | Google Search Console ultimos 91 dias | CTR, paginas prioritarias, patrones |
| `plan-metas-ctr-2026-05-08.md` | 2026-05-08 | auditoria CTR previa | propuestas pendientes, no implementadas |

## Evidencia extraida

### Tendencia organica SEMrush

- Trafico organico estimado Espana: de 4.200/mes a 3.200/mes entre marzo y mayo 2026.
- Variacion estimada: -24%.
- Keywords organicas estimadas: de 2.400 a 2.200.
- Authority Score: 16.
- Referring domains: 1.3K.
- Backlinks: 11.5K aprox.
- Trust Flow legacy/Majestic: 0.

Interpretacion permitida:

- Hay senal suficiente para investigar caida organica y autoridad.
- No afirmar causa definitiva de la caida sin GSC vivo por fechas.

### Concentracion de trafico

- Homepage reportada por SEMrush: 2.800 visitas estimadas, 86.9% del trafico organico estimado.
- La dependencia de homepage es un riesgo SEO y de conversion.

Interpretacion permitida:

- Priorizar distribucion de trafico hacia paginas de servicio es razonable.
- No tocar homepage sin Orden de Cambio y medicion de linea base.

### Datos GSC agregados

El output `estrategia-seo-2026-05-07.md` declara:

- Clics totales 3 meses: 6.280.
- Impresiones totales 3 meses: 637.000.
- CTR medio: 1%.
- Posicion media: 9,6, empeorando hacia 10,1 en el ultimo mes.
- Trafico mensual real aproximado: 2.100 clics/mes.

Interpretacion permitida:

- El problema principal parece ser bajo CTR sobre un volumen alto de impresiones.
- Antes de implementar, comprobar periodo exacto en GSC.

### Oportunidades por pagina/cluster

- Homepage: CTR bajo y volumen alto, reportada con alrededor de 106K impresiones en el periodo usado por la estrategia.
- iPhone 13: 18.720 impresiones y 189 clics en 3 meses, CTR 1%.
- BitLocker: query "bitlocker que es" con 1.706 impresiones y 19 clics.
- MacBook: 11.441 impresiones y 255 clics, CTR 2.2%.
- Amazfit: el output de estrategia declara aproximadamente 518 clics en 3 meses entre categoria/post/queries.
- GoPro: `category/reparacion-gopro/` reporta 98 clics, 1.367 impresiones y CTR 7.2%.

Interpretacion permitida:

- CTR y snippets son oportunidades reales.
- Amazfit, Xiaomi y GoPro tienen demanda suficiente para revisar paginas dedicadas o mejoras.

### Auditoria CTR

El output `ctr-audit-2026-05-07.md` declara:

- 111 paginas con mas de 1.000 impresiones/mes y CTR inferior a 3%.
- Top 10 paginas: 261.175 impresiones/mes, CTR promedio 0.4%.
- Ganancia estimada si top 10 suben a 2% CTR: +4.210 clics/mes.

Advertencia:

- La unidad `impresiones/mes` debe verificarse. Otros outputs declaran GSC de ultimos 91 dias, por lo que puede haber normalizacion o inconsistencia de etiqueta.
- No usar estas cifras en un informe externo sin revalidar en GSC.

## Propuestas legacy no implementadas

El archivo `plan-metas-ctr-2026-05-08.md` contiene propuestas de titles/metas para:

- homepage;
- HyperOS Xiaomi;
- categoria reparacion moviles;
- BitLocker;
- teclado portatil;
- iPhone;
- raya verde iPhone;
- Xiaomi;
- pasta termica;
- firmware moviles.

Estado:

- Son propuestas pendientes.
- No hay confirmacion de implementacion.
- No deben ejecutarse sin Orden de Cambio y validacion de title/meta actual.

## Contradicciones o dudas

- El sistema legacy mezcla algunos datos estimados de SEMrush con datos reales de GSC; deben mantenerse separados.
- Existe posible inconsistencia de unidad en CTR audit: `impresiones/mes` vs fuente `ultimos 91 dias`.
- GA4 sigue sin evidencia verificable en v2.
- GBP se describe como fuerte, pero no fue verificado vivo en esta sesion.

## Nivel de medicion actualizado

Despues de leer outputs legacy:

- Nivel anterior: 1 - declarada/orientativa.
- Nivel nuevo: 2 - parcial fuerte.

Motivo:

- Hay evidencia reciente en documentos legacy con fuentes declaradas GSC y SEMrush.
- No hay export bruto ni consulta viva en v2.
- Hay dudas de unidades que bloquean Nivel 3.
- GA4 y GBP siguen pendientes de verificacion.

## Que permite hacer ahora

- Preparar una auditoria SEO parcial fuerte.
- Priorizar hipotesis SEO con cautela.
- Definir checklist para consulta GSC/SEMrush viva.
- Preparar backlog de CTR sin ejecutar cambios.

## Que no permite hacer todavia

- Entregar auditoria SEO final al cliente.
- Afirmar causa exacta de caida organica.
- Presentar estimaciones de clics como promesa.
- Ejecutar cambios de metas, schema, contenido, WordPress o homepage.
- Hacer CRO basado en conversiones GA4.

## Proxima accion unica

Revalidar en GSC las unidades y el periodo de las paginas prioritarias de CTR, y cruzar con SEMrush actual antes de cerrar auditoria SEO final.
