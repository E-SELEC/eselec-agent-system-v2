---
name: site-architecture
description: >
  Audita, disena o reestructura arquitectura web para clientes de E-SELEC:
  mapa de paginas, jerarquia, menus, URLs, breadcrumbs, enlazado interno,
  redirecciones, sitemap visual, hubs SEO, paginas de servicios, categorias,
  landings y riesgos de migracion. Usalo cuando se hable de estructura web,
  sitemap, arquitectura, menu, navegacion, URLs, redirecciones, enlazado
  interno, "que paginas necesito", "como organizo la web" o redisenos.
---

# Site Architecture - E-SELEC

## Proposito

Crear estructuras web que ayuden al usuario, al SEO y a la conversion sin romper lo que ya funciona.

Esta skill no modifica webs. Produce una arquitectura, plan o diagnostico que despues puede pasar a Web, SEO, CRO, tracking o desarrollo con los riesgos claros.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`, contrato Web / arquitectura
8. `protocols/activos-criticos.md`
9. `protocols/control-artefactos.md`
10. `.claude/skills/verificacion-medicion/SKILL.md` si la decision depende de GA4, GSC, SEMrush, GBP o Ads
11. `.claude/skills/ingesta-evidencia/SKILL.md` si vas a usar exports, capturas o outputs legacy
12. `.claude/skills/analytics-tracking/SKILL.md` si el cambio afecta formularios, conversiones o eventos

No inventes paginas, servicios, URLs con trafico, rankings ni conversiones. Si no estan verificados, marcalos como supuesto o pendiente.

## Principios

1. Cada pagina debe tener objetivo, audiencia y siguiente accion.
2. La arquitectura no se decide solo por estetica; se decide por busqueda, negocio, conversion y mantenimiento.
3. Las URLs existentes son activos: no se cambian sin inventario y plan 301.
4. Los menus deben ayudar a elegir, no mostrar todo.
5. Las paginas importantes deben estar a pocos clics de la home.
6. El enlazado interno debe apoyar prioridades SEO y rutas de conversion.
7. WordPress, WooCommerce, formularios, tracking y redirects son produccion: requieren Orden de Cambio antes de tocarse.

## Niveles de arquitectura

- SA3 - validada: inventario de URLs, datos SEO/conversion, CMS, restricciones, mapa nuevo, redirecciones y validacion de riesgo.
- SA2 - plan fuerte: hay contexto, URLs actuales y evidencia parcial; faltan datos vivos o validacion final.
- SA1 - orientativa: hay objetivo y servicios, pero no inventario completo ni medicion.
- SA0 - bloqueada: falta dominio, objetivo, audiencia, servicios o URLs criticas para una reestructura.

Regla:

- SA0 no produce arquitectura final.
- SA1 solo orienta.
- SA2 permite plan interno.
- SA3 permite briefing de implementacion o propuesta al cliente.

## Workflow

### 1. Definir alcance

Clasifica la tarea:

| Alcance | Pregunta central | Riesgo |
|---|---|---|
| Web nueva | Que paginas necesita? | medio |
| Reestructura | Que conservar, mover, fusionar o redirigir? | alto |
| Menu/navegacion | Como encuentra el usuario lo importante? | medio |
| URLs | Que patron sera estable y entendible? | alto |
| Enlazado interno | Que paginas deben recibir autoridad? | medio |
| Migracion/lanzamiento | Como cambiar sin romper SEO/conversion? | alto |

Si es reestructura o migracion, exige inventario de URLs antes de recomendar cambios definitivos.

### 2. Mapear estado actual

Identifica:

- dominio y CMS;
- servicios/productos;
- audiencias;
- paginas existentes;
- paginas con trafico, leads, ventas, rankings o backlinks;
- menus actuales;
- formularios, WhatsApp, llamadas, checkout o reservas;
- tracking y eventos afectados;
- restricciones tecnicas.

Si usas evidencia externa, pasa primero por `ingesta-evidencia` y `verificacion-medicion`.

### 3. Proteger activos

Marca como activos criticos:

- URLs con trafico organico;
- paginas con conversiones;
- paginas con backlinks;
- checkout, carrito, formularios, reservas y WhatsApp;
- paginas indexadas con buen rendimiento;
- reglas de redirects, canonical, noindex, sitemap o robots.

No recomiendes eliminar, mover o renombrar estos activos sin plan 301 y validacion SEO.

### 4. Elegir patron

Usa `references/site-patterns.md` para elegir estructura base:

- negocio local / servicios;
- e-commerce o WooCommerce;
- web corporativa;
- hub SEO / contenido;
- landing de campana;
- hibrido.

Adapta el patron al cliente. No copies un arbol generico.

### 5. Disenar jerarquia

La jerarquia debe incluir:

- home;
- paginas principales;
- subpaginas;
- landings o hubs si aplican;
- paginas legales o de confianza;
- rutas de conversion.

Usa arbol ASCII simple. Evita caracteres especiales para que sea facil de versionar.

### 6. Definir URLs

Cada URL debe ser:

- corta;
- en minusculas;
- con guiones;
- estable;
- alineada con la jerarquia;
- coherente con idioma y mercado.

Si cambia una URL existente, la tabla debe incluir URL actual, URL propuesta y tipo de accion: mantener, crear, fusionar, redirigir, revisar o eliminar.

### 7. Definir navegacion

Especifica:

- header;
- CTA principal;
- menu movil;
- footer;
- breadcrumbs;
- sidebar si aplica;
- enlaces contextuales.

Regla practica: header con 4-7 items principales. Si hay mas, agrupar.

### 8. Disenar enlazado interno

Define:

- paginas hub;
- paginas spoke;
- enlaces desde home;
- enlaces entre servicios y posts;
- enlaces hacia paginas de conversion;
- paginas huerfanas a corregir.

No propongas enlazado solo por cantidad. Cada enlace debe tener razon.

### 9. Revisar riesgos de lanzamiento

Antes de cerrar, responde:

- que se puede implementar sin tocar produccion;
- que requiere Orden de Cambio;
- que requiere SEO antes de publicar;
- que requiere tracking antes/despues;
- que puede afectar conversion o indexacion.

### 10. Preparar output

Usa `templates/arquitectura-web.md`.

Debe incluir:

- objetivo;
- nivel SA0-SA3;
- fuentes;
- estado actual;
- mapa de paginas;
- tabla de URLs;
- navegacion;
- enlazado interno;
- redirecciones/riesgos;
- dependencias;
- siguiente accion unica.

## Bloqueos

Bloquea o marca como parcial si:

- no hay objetivo de la web;
- no hay dominio o cliente claro;
- se pide reestructura sin inventario de URLs;
- se pide cambiar URLs sin plan 301;
- hay WooCommerce, checkout, pagos, formularios o reservas sin Orden de Cambio;
- se desconoce CMS y el plan depende de implementacion tecnica;
- se afirma rendimiento SEO/conversion sin fuente verificada;
- la arquitectura contradice `context.md` o `log.md`.

## Referencias

- `references/site-patterns.md`: patrones compactos por tipo de sitio.
- `templates/arquitectura-web.md`: formato de salida.
- `checklists/revision.md`: revision antes de entregar.
