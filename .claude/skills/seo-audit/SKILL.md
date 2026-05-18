---
name: seo-audit
description: >
  Audita, revisa o diagnostica SEO de un sitio. Usalo para SEO tecnico,
  indexacion, caidas de trafico, perdida de rankings, on-page, Core Web
  Vitals, arquitectura SEO, SEO local basico, schema o "mi web no posiciona".
  Para AI Search profundo usa una skill especifica de AI SEO cuando exista.
---

# SEO Audit - E-SELEC

## Proposito

Detectar los problemas SEO que mas afectan visibilidad, trafico o conversion organica, y priorizar correcciones.

Esta skill debe producir una auditoria verificable, no una lista generica de recomendaciones.

## Fuentes obligatorias

Si el cliente existe en el sistema, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/log.md`
3. `clients/[cliente]/memory.md` si existe
4. outputs SEO recientes si existen
5. `.claude/skills/seo-canon/SKILL.md` cuando sea una auditoria profunda, una caida de trafico, arquitectura, migracion, canibalizacion, SEO local, SEO internacional o Rodrigo mencione el canon/Docente SEO
6. `quality/criterios-output.md`, Contrato 2 - Auditoria SEO

Si no hay cliente local, pide o usa:

- dominio o URL;
- tipo de negocio;
- objetivo SEO;
- alcance de la auditoria;
- herramientas disponibles.

## Nivel de datos SEO

Clasifica antes de concluir:

- Nivel 3 - completo: GSC + SEMrush + datos tecnicos/render + contexto.
- Nivel 2 - parcial fuerte: GSC o SEMrush + revision tecnica basica.
- Nivel 1 - orientativo: solo URL/render/manual, sin datos de rendimiento.
- Nivel 0 - bloqueado: no hay dominio/URL o el sitio no puede evaluarse.

Regla:

- Si falta GSC o SEMrush, la auditoria debe decir `Basado en datos parciales`.
- Si no hay datos de rendimiento, no afirmar causas de trafico o ranking como hechos.
- Si solo se revisa una pagina, no concluir sobre todo el dominio.
- Si aplicas el canon SEO, indica que archivo o modulo leiste. No digas que usaste el canon si no lo leiste.

## Jerarquia de fuentes

1. GSC: impresiones, clics, CTR, queries, paginas y fechas reales.
2. SEMrush: visibilidad estimada, competidores, gaps, autoridad, backlinks y dificultad.
3. PageSpeed/Chrome/render: Core Web Vitals, rendimiento, mobile y renderizado.
4. Sitio: robots, sitemap, canonicals, headings, contenido, enlaces, schema.
5. Contexto/log/memoria: objetivos, historial y restricciones.

La prioridad nace del cruce entre datos reales y oportunidad de mercado.

## Orden de analisis

1. Crawlability e indexacion.
2. Fundamentos tecnicos.
3. On-page y arquitectura.
4. Calidad de contenido e intencion.
5. Autoridad, enlaces y competencia.
6. Local/GBP si aplica.
7. LLM/AI search solo como observacion si no es el alcance principal.

Regla SEO:

```text
No propongas contenido si hay bloqueo tecnico critico que impide rastreo, indexacion o medicion.
```

Regla del canon E-SELEC:

```text
web nueva = disenar antes de publicar
web existente = medir, proteger y corregir antes de expandir
```

## Schema

No diagnostiques "no hay schema" usando solo `curl`, `web_fetch` o HTML estatico.

Para schema usa una de estas vias:

- navegador renderizado y selector `script[type="application/ld+json"]`;
- Google Rich Results Test;
- Screaming Frog con renderizado si hay export;
- herramienta equivalente que renderice JavaScript.

Si no puedes verificarlo, escribe:

```text
Schema no verificado con renderizado. No concluyo ausencia.
```

## Workflow

### 1. Definir alcance

Determina:

- dominio o URL;
- cliente;
- objetivo SEO;
- tipo de auditoria: tecnica, on-page, local, perdida de trafico, completa;
- fuentes disponibles;
- si el output se guarda o se entrega en chat.

### 2. Revisar contexto e historial

Busca:

- servicios SEO contratados;
- cambios recientes;
- migraciones;
- problemas tecnicos anteriores;
- keywords o zonas prioritarias;
- outputs previos;
- aprendizajes en memoria.

### 3. Levantar evidencia

Recoge solo evidencia necesaria para decidir.

Ejemplos:

- robots/sitemap/canonicals;
- indexacion esperada vs observada;
- PageSpeed/Core Web Vitals;
- titles/metas/H1;
- estructura de enlaces internos;
- paginas con caida o oportunidad;
- queries con impresiones y bajo CTR;
- competidores y gaps;
- backlinks/autoridad si aplica.

### 4. Priorizar

Cada hallazgo importante debe incluir:

- problema;
- evidencia;
- impacto;
- esfuerzo;
- fix;
- prioridad.

Top 3 primero. El resto va a backlog.

### 5. Generar output

Usa `templates/auditoria-seo.md`.

### 6. Revisar antes de entregar

Usa `checklists/revision.md`.

El minimo aceptable es nivel 2. El estandar E-SELEC es nivel 3.

## Bloqueos

Detente o marca como parcial si:

- no hay dominio o URL;
- el sitio no responde;
- faltan GSC/SEMrush para diagnosticar caidas;
- hay contradiccion entre datos y contexto;
- el fix implica produccion, redirecciones, DNS, WordPress, Ads, GBP o datos vivos;
- se requiere acceso sensible no disponible.

Si hay cambios en produccion, aplica `protocols/activos-criticos.md` antes de proponer ejecucion.

## Archivos de apoyo

- `templates/auditoria-seo.md`: formato de salida.
- `checklists/revision.md`: revision antes de entregar.
