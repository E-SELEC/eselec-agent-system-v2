---
name: copywriting
description: >
  Escribe, reescribe o mejora copy comercial para clientes de E-SELEC:
  homepages, landing pages, paginas de servicio, heroes, titulares,
  subtitulares, CTAs, value proposition, secciones de beneficios, FAQs,
  anuncios base, textos web, above the fold, pricing, about, producto,
  mensajes de conversion y copy para SEO/AI SEO. Usalo cuando se pida escribir
  copy, mejorar textos, hacer una pagina mas persuasiva, crear titulares,
  CTAs, propuesta de valor o transformar estrategia/brief en texto final.
---

# Copywriting - E-SELEC

## Proposito

Crear copy claro, especifico y accionable que ayude a convertir sin inventar pruebas ni sonar generico.

Esta skill escribe texto final o borradores fuertes. Si el problema es estrategia de pagina, usar `page-cro` o `site-architecture` antes.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`, contrato Copy / contenido
8. `agency/brand.md` si el entregable lleva marca E-SELEC
9. `agency/preferencias-rodrigo.md` si existe en v2
10. `.claude/skills/content-strategy/SKILL.md` si el copy viene de estrategia editorial
11. `.claude/skills/seo-audit/SKILL.md` si hay intencion SEO
12. `.claude/skills/ai-seo/SKILL.md` si debe ser citable o extractable

No uses claims, cifras, testimonios, precios, garantias, certificaciones ni resultados si no aparecen en las fuentes.

## Principios

1. Claridad antes que ingenio.
2. Beneficio antes que feature.
3. Especificidad antes que frases comodin.
4. Voz del cliente antes que lenguaje interno.
5. Una seccion, una idea.
6. CTA alineado con el objetivo real.
7. Honestidad antes que exageracion.

## Niveles de copy

- CW3 - listo: objetivo, audiencia, oferta, tono, pruebas y restricciones claras; copy revisado con CTA y estructura.
- CW2 - borrador fuerte: falta alguna prueba o dato, pero el texto es usable internamente.
- CW1 - exploratorio: falta informacion relevante; sirve para elegir direccion.
- CW0 - bloqueado: falta oferta, audiencia, objetivo o hay claims no verificables.

Regla:

- CW0 no produce copy final.
- CW1 debe marcarse como exploratorio.
- CW2 puede pasar a revision.
- CW3 puede entregarse o implementarse con aprobacion si toca produccion.

## Workflow

### 1. Definir objetivo

Identifica:

- tipo de pieza: home, landing, servicio, producto, anuncio, seccion, CTA;
- accion primaria;
- audiencia;
- etapa de compra;
- fuente de trafico;
- idioma;
- tono;
- restriccion de longitud o formato.

Si no hay accion primaria, no escribas CTA definitivo.

### 2. Extraer materia prima

Busca:

- oferta;
- problema;
- resultado deseado;
- diferenciador;
- prueba;
- objeciones;
- lenguaje del cliente;
- competidores o alternativas;
- restricciones legales/sectoriales.

Si falta prueba, no la inventes: usa copy sin prueba o marca "prueba pendiente".

### 3. Elegir estructura

Usa `references/copy-frameworks.md`.

Estructuras comunes:

- Hero: headline, subheadline, CTA, prueba breve.
- Landing: problema, solucion, beneficios, prueba, FAQ, CTA.
- Servicio: problema, solucion, proceso, confianza, CTA.
- Producto: resultado, features-beneficios, comparativa, prueba, CTA.
- About: historia, creencia, beneficio para cliente, confianza, CTA.

### 4. Escribir con control de calidad

Evita:

- "soluciones integrales";
- "innovador";
- "a medida" sin explicar;
- "lideres";
- "expertos" sin prueba;
- "potencia tu negocio";
- "en el mundo digital actual";
- claims absolutos;
- exclamaciones innecesarias.

Prefiere:

- verbo concreto;
- resultado visible;
- condicion real;
- prueba disponible;
- CTA especifico.

### 5. Preparar variantes

Cuando el texto sea importante, da:

- version principal;
- 2 alternativas de titular;
- 2 alternativas de CTA;
- razon breve de cada decision.

### 6. Revisar tono humano

Lee `references/style-rules.md`.

El texto debe sonar natural, no inflado ni robotico.

### 7. Preparar output

Usa `templates/copy-output.md`.

Debe incluir:

- nivel CW0-CW3;
- objetivo;
- audiencia;
- fuentes/pruebas;
- copy final;
- variantes;
- notas de uso;
- riesgos o datos faltantes;
- siguiente accion unica.

## Bloqueos

Bloquea o marca como parcial si:

- no hay oferta;
- no hay audiencia;
- no hay accion primaria;
- se piden claims no verificables;
- se piden datos legales/salud/finanzas sin fuente;
- contradice brand/context/log;
- se quiere publicar en web/ads/email sin aprobacion.

## Referencias

- `references/copy-frameworks.md`: estructuras y formulas.
- `references/style-rules.md`: reglas de estilo y anti-frases genericas.
- `templates/copy-output.md`: formato de salida.
- `checklists/revision.md`: revision final.
