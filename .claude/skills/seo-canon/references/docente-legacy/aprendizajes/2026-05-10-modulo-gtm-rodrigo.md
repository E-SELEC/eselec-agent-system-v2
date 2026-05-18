# Modulo Google Tag Manager - Rodrigo

- Fecha: 2026-05-10
- Estado: aprendido / pendiente de verificacion viva de enlaces oficiales
- Fuente: `agents/docente/seo/fuentes/2026-05-10-manual-seo-post-neuronwriter.md`
- Alcance: laboratorio del Docente SEO
- Restriccion: no modifica `agents/seo/`

---

## Idea central

Google Tag Manager, o GTM, es una herramienta de gestion de etiquetas.

La explicacion simple:

```text
GA4 mide y analiza datos.
GTM ayuda a enviar esos datos correctamente.
```

GTM no posiciona una web.

```text
GTM no es una herramienta SEO para posicionar.
GTM es una herramienta de medicion.
Sin medicion, el SEO se vuelve intuicion.
```

Relacion correcta:

```text
SEO -> genera trafico
GTM -> mide acciones
GA4 -> analiza comportamiento
CRO -> mejora conversion
```

---

## Lugar en el sistema SEO

GTM conecta con:

1. Diagnostico SEO: validar medicion, comprobar GA4, detectar eventos faltantes
   y duplicidad de etiquetas.
2. SEO On-Page: medir CTAs, formularios, WhatsApp, telefono, scroll e
   interaccion con contenido.
3. SEO de contenidos: medir descargas, clics a paginas comerciales, scroll,
   videos y recursos.
4. SEO local: medir llamadas, WhatsApp, email, reservas y rutas si ocurren en
   la web.
5. Ecommerce SEO: medir `view_item`, `add_to_cart`, `begin_checkout`,
   `purchase` y errores de medicion ecommerce.
6. CRO: medir embudos, abandonos, microconversiones y conversiones reales.
7. Control de calidad: preview, debug, versiones, publicacion controlada y
   rollback.

Reglas:

```text
No se optimiza lo que no se mide.
No se mide nada sin validar.
No se publica nada en GTM sin probar.
```

---

## Web nueva vs web existente

### Web nueva

GTM se configura antes del lanzamiento o en la fase final de desarrollo.

Flujo:

```text
1. Crear cuenta y contenedor
2. Instalar codigo GTM en la web
3. Configurar Google tag / GA4
4. Activar o validar medicion basica
5. Definir eventos importantes
6. Configurar WhatsApp
7. Configurar telefono
8. Configurar formularios
9. Configurar ecommerce, si aplica
10. Probar en Preview Mode
11. Validar en GA4 DebugView
12. Publicar version
13. Documentar todo
```

Mentalidad:

```text
En web nueva, GTM debe dejar preparada la medicion antes de invertir en SEO,
Ads o CRO.
```

### Web existente

No se toca GTM a ciegas. Primero se audita.

Flujo:

```text
1. Confirmar si existe GTM
2. Confirmar si existe GA4
3. Revisar si GA4 esta duplicado
4. Revisar etiquetas activas
5. Revisar activadores
6. Revisar variables
7. Revisar eventos enviados a GA4
8. Validar formularios
9. Validar WhatsApp/telefono
10. Validar ecommerce, si aplica
11. Revisar versiones publicadas
12. Probar en Preview Mode
13. Corregir medicion
14. Documentar cambios
```

Error grave:

```text
Instalar un nuevo GA4 desde GTM sin revisar si ya existe otro GA4 instalado por
plugin, codigo o tema.
```

---

## Conceptos base

El equipo debe dominar:

- etiqueta: envia datos a una plataforma;
- activador: decide cuando se dispara la etiqueta;
- variable: guarda valores que la etiqueta o activador necesita;
- data layer: capa donde la web deja datos para que GTM los recoja;
- contenedor: espacio de trabajo de una web;
- workspace: entorno de trabajo antes de publicar;
- version: estado publicado y recuperable;
- preview mode: modo de prueba;
- debug: revision de datos enviados.

Regla:

```text
Una web principal = un contenedor GTM.
```

---

## Configuracion inicial

Proceso:

```text
1. Crear cuenta.
2. Crear contenedor.
3. Instalar codigo en la web.
4. Probar que GTM carga.
5. Configurar Google tag.
6. Configurar eventos.
7. Probar.
8. Publicar.
9. Documentar.
```

En WordPress, puede instalarse con codigo, plugin fiable, integracion del
constructor o Site Kit si aplica.

Regla:

```text
GTM debe instalarse una sola vez, en todas las paginas y validarse en Preview Mode.
```

Error tipico:

```text
Instalar GTM por plugin y tambien manualmente en el tema.
```

---

## Como se piensa una medicion

Cada medicion debe formularse asi:

```text
Que accion quiero medir?
Por que importa para negocio?
Que evento debe llegar a GA4?
Que etiqueta lo envia?
Que activador lo dispara?
Que variables necesita?
Sera evento clave?
Como lo valido?
Donde lo documento?
```

---

## Mediciones SEO basicas

Eventos minimos frecuentes:

- `click_whatsapp`;
- `click_phone`;
- `click_email`;
- `form_submit`;
- `form_start`;
- `file_download`;
- `cta_click`;
- `booking_click`;
- eventos ecommerce si aplica.

Ejemplo de validacion:

```text
1. Hacer clic en WhatsApp en Preview Mode.
2. Confirmar que el activador se dispara.
3. Confirmar que la etiqueta se dispara.
4. Confirmar evento en GA4 DebugView.
5. Marcar como evento clave si es conversion real.
```

---

## Eventos recomendados vs personalizados

Usar eventos recomendados de GA4 cuando encajan.

Usar personalizados cuando no existe un evento recomendado adecuado.

Nomenclatura interna:

```text
lowercase_con_guiones_bajos
```

Ejemplos:

- `click_whatsapp`;
- `click_phone`;
- `form_submit`;
- `booking_click`;
- `menu_download`.

No marcar cualquier clic como evento clave.

---

## Preview Mode y publicacion

Nada se publica sin Preview Mode.

Proceso:

```text
1. Abrir GTM.
2. Entrar al contenedor correcto.
3. Hacer clic en Preview.
4. Introducir URL.
5. Conectar Tag Assistant.
6. Ejecutar accion en la web.
7. Revisar etiquetas disparadas.
8. Revisar etiquetas no disparadas.
9. Revisar variables.
10. Corregir.
11. Validar en GA4 DebugView.
12. Publicar solo si funciona.
```

Toda publicacion debe tener version con nombre, descripcion y motivo.

---

## Ecommerce y data layer

Para ecommerce, GTM exige mas criterio tecnico.

Eventos a validar:

- `view_item`;
- `add_to_cart`;
- `begin_checkout`;
- `purchase`;
- `transaction_id`;
- `value`;
- `currency`;
- `items`.

No asumir que un plugin lo mide todo bien. Hay que validar.

Error tipico:

```text
Instalar plugin de ecommerce tracking y nunca comprobar si purchase llega con
valor correcto.
```

---

## Auditoria GTM en web existente

Checklist:

```text
1. Confirmar si GTM esta instalado.
2. Confirmar ID de contenedor.
3. Revisar si GA4 esta duplicado.
4. Revisar etiquetas activas.
5. Revisar activadores.
6. Revisar variables.
7. Revisar versiones recientes.
8. Revisar eventos en GA4.
9. Probar acciones clave en Preview.
10. Documentar problemas.
```

Entregable:

```text
Cliente:
Dominio:
ID GTM:
ID GA4:
Duplicidad:
Eventos activos:
Eventos faltantes:
Errores:
Acciones:
Responsable:
Version publicada:
Fecha:
```

---

## Regla final para relevo

Google Tag Manager no se usa para "meter codigos".

Cada configuracion debe poder responder:

```text
Que accion estoy midiendo.
Por que importa.
Que etiqueta uso.
Que activador la dispara.
Que variables necesita.
Que evento llega a GA4.
Si sera evento clave o no.
Como lo valide.
Que version publique.
Donde quedo documentado.
```

Si una persona dice "ya puse el tag", todavia no entendio GTM.

Respuesta profesional:

```text
Configure el evento click_whatsapp, se dispara cuando Click URL contiene wa.me
o api.whatsapp.com, envia link_url, link_text y page_location a GA4, lo valide
en Preview Mode y DebugView, quedo publicado en una version documentada y se
revisara en GA4 en la proxima medicion.
```
