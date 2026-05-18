# Patron general - Diagnostico de caida SEO en sitio multi-idioma

## Proposito

Este patron conserva el aprendizaje operativo de una sesion real sin convertir
un cliente concreto en regla general del canon.

No contiene nombre de cliente, dominio, rutas reales ni entregables reales.

## Cuando usarlo

Usalo cuando una web multi-idioma pierde trafico organico de forma repentina,
especialmente si:

- cae un grupo completo de keywords de un idioma;
- sube o se mantiene otro idioma;
- la primera hipotesis apunta a algoritmo, pero no hay verificacion tecnica;
- hay sospecha de redirects, canonicals, hreflang, sitemap o URLs duplicadas.

## Error que evita

No cierres un diagnostico diciendo "fue algoritmo" solo porque la caida coincide
con un update de Google.

Un update puede ser contexto, pero la causa operativa puede estar en la web.

## Secuencia correcta

1. Separar contexto externo de causa interna.
   - Contexto externo: update de Google, cambios de SERP, mercado, idioma.
   - Causa interna: cambios tecnicos, URLs, indexacion, redirects, canonicals,
     hreflang, sitemap, contenido o arquitectura.

2. Cruzar datos antes de concluir.
   - GSC: queries, paginas, clics, impresiones, CTR, fechas reales.
   - SEMrush: keywords ganadas/perdidas, competidores, visibilidad estimada.
   - Crawl tecnico: status codes, redirects, canonicals, hreflang, sitemap.

3. Revisar si la caida agrupa un patron.
   - mismo idioma;
   - mismo tipo de pagina;
   - misma carpeta;
   - mismas URLs criticas;
   - mismo template;
   - mismo cambio reciente.

4. Descartar problemas tecnicos basicos antes de estrategia.
   - 301 a si misma;
   - cadena o bucle de redirects;
   - canonical cruzado incorrecto;
   - hreflang ausente o mal armado;
   - sitemap obsoleto o incompleto;
   - URLs basura o duplicadas;
   - paginas importantes fuera del sitemap;
   - paginas indexables marcadas como duplicadas.

5. Solo despues definir plan.
   - detener sangrado tecnico;
   - ordenar arquitectura;
   - reparar senales de idioma;
   - reindexar;
   - medir recuperacion;
   - mejorar contenido.

## Principio SEO aplicado

El SEO tecnico desbloquea el SEO organico.

Si Google no puede rastrear, entender o conservar una URL, el contenido no puede
competir aunque sea bueno.

## Senales de alerta

- "Perdimos ingles, pero ganamos espanol" no prueba algoritmo por si solo.
- "Hay core update" no prueba causa raiz.
- "El contenido debe recuperarse" exige revisar tecnica antes de escribir mas.
- "Canonical al idioma principal" suele ser peligroso si elimina versiones
  idiomaticas validas.
- "Sitemap viejo pero funciona" debe comprobarse, no asumirse.

## Salida esperada

Cuando uses este patron, responde con:

```text
Patron aplicado:
Datos cruzados:
Causa descartada:
Causa probable:
Causa confirmada:
Riesgo si se actua sin corregir:
Primer cambio seguro:
```

## Regla final

Un caso real puede vivir en `clients/[cliente]/`, pero el canon solo debe
guardar patrones generales y anonimos.
