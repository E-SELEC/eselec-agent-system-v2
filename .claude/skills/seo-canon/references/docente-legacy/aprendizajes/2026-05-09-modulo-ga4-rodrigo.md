# Modulo Google Analytics 4 - Rodrigo

- Fecha: 2026-05-09
- Estado: aprendido / pendiente de verificacion viva de enlaces oficiales
- Fuente: instruccion directa de Rodrigo al Docente SEO
- Skill de apoyo usada: `analytics-tracking`
- Alcance: laboratorio del Docente SEO
- Restriccion: no modifica `agents/seo/`

---

## Idea central

GA4 cambia el enfoque:

```text
Search Console dice como llega el usuario desde Google.
Google Analytics 4 dice que hace despues dentro de la web y si eso genera negocio.
```

La pregunta principal de GA4 para SEO profesional es:

```text
El trafico organico que estamos consiguiendo genera negocio?
```

GA4 no sustituye a SEMrush ni a GSC.

```text
SEMrush detecta oportunidades.
Search Console valida rendimiento en Google.
GA4 valida comportamiento y negocio.
```

GA4 no se usa para decir "subieron las visitas". Se usa para saber si el
trafico esta generando valor.

---

## Principio de medicion

El equipo debe aprender esto:

```text
No se mide por medir.
Se mide para decidir.
```

Cada evento debe responder:

1. Que decision permite tomar?
2. Que accion se hara si sube, baja o falla?
3. Que valor de negocio representa?

Esto viene del criterio de analitica:

```text
Track for decisions, not data.
```

Evitar metricas vanidosas. Priorizar datos limpios, accionables y documentados.

---

## GA4 dentro del marco maestro SEO

GA4 se conecta sobre todo con diagnostico, SEO On-Page, contenido, local,
ecommerce, CRO y medicion continua.

Bloques:

1. Diagnostico SEO: trafico organico, paginas de entrada, usuarios nuevos,
   sesiones, engagement y eventos clave.
2. SEO On-Page: landings organicas, comportamiento por URL, interaccion con
   CTAs, scroll, clics internos y conversion por pagina.
3. SEO de contenidos: paginas informacionales, retencion, contenidos sin accion,
   contenidos que asisten conversiones y contenidos que deben mejorar.
4. SEO local: ciudad/pais, movil, telefono, WhatsApp, formularios, reservas y
   landings locales.
5. Ecommerce SEO: vistas de producto, add to cart, checkout, compras, ingresos,
   categorias y productos que convierten.
6. CRO aplicado al SEO: embudos, abandonos, rutas, formularios, eventos clave y
   conversion por canal.
7. Medicion continua: adquisicion, engagement, eventos clave, ecommerce,
   exploraciones y reportes.

GA4 debe ensenar al equipo a dejar de pensar solo en trafico y empezar a pensar
en trafico con intencion, comportamiento y conversion.

---

## Web nueva vs web existente

### Web nueva

En web nueva, GA4 debe configurarse antes o justo en el lanzamiento.

La mision no es analizar historico. La mision es dejar la medicion lista.

Flujo:

```text
1. Crear propiedad GA4
2. Crear flujo de datos web
3. Instalar etiqueta
4. Activar medicion optimizada
5. Definir eventos importantes
6. Configurar eventos clave
7. Conectar Search Console
8. Conectar Google Ads, si aplica
9. Validar en Realtime y DebugView
10. Crear audiencias o segmentos basicos
11. Crear reportes iniciales
12. Documentar medicion
```

Regla:

```text
No lanzar una web sin medicion.
```

Si se lanza sin GA4 bien configurado, despues no se puede recuperar con
precision lo que no se midio.

### Web existente

En web existente, GA4 se usa primero para auditar si la medicion esta bien.

Regla:

```text
Antes de sacar conclusiones, valida que GA4 esta midiendo bien.
```

Flujo:

```text
1. Revisar si GA4 esta instalado
2. Revisar si mide paginas correctamente
3. Revisar eventos activos
4. Revisar eventos clave
5. Revisar trafico organico
6. Revisar landings organicas
7. Revisar conversiones por canal
8. Revisar ecommerce, si aplica
9. Revisar embudos
10. Revisar errores de atribucion
11. Cruzar con Search Console
12. Crear roadmap de medicion y CRO
```

---

## Configuracion inicial

La configuracion base tiene cuatro capas:

```text
1. Cuenta
2. Propiedad
3. Flujo de datos
4. Etiqueta instalada en la web
```

Proceso:

```text
1. Crear cuenta o usar cuenta existente.
2. Crear propiedad GA4.
3. Crear flujo de datos web.
4. Instalar etiqueta mediante Google tag, GTM, plugin CMS o integracion directa.
5. Confirmar recogida de datos en Realtime y DebugView.
```

Entregable interno:

```text
Cliente:
Dominio:
Propiedad GA4:
ID de medicion:
Metodo de instalacion:
GTM instalado: si/no
Medicion optimizada: si/no
Eventos clave configurados:
Search Console conectado: si/no
Google Ads conectado: si/no
Ecommerce configurado: si/no
Fecha:
Responsable:
```

Errores comunes:

- crear varias propiedades sin criterio;
- instalar GA4 dos veces;
- no documentar el ID de medicion;
- no validar eventos;
- no configurar eventos clave;
- no conectar Search Console;
- medir trafico pero no conversiones.

---

## Medicion optimizada

La medicion optimizada permite medir interacciones basicas sin codigo
adicional.

Eventos habituales:

- `page_view`;
- `scroll`;
- clic externo;
- `site_search`;
- video;
- `file_download`;
- `form_start`;
- `form_submit`, segun configuracion/disponibilidad.

Criterio:

```text
La medicion optimizada es base, no estrategia completa.
```

No se activa todo sin pensar. Se revisa si cada evento sirve para SEO, CRO o
negocio.

Plantilla:

```text
Evento:
Activo:
Que mide:
Sirve para SEO/CRO:
Se marca como evento clave: si/no
Observaciones:
```

Error tipico:

```text
Pensar que, porque GA4 mide eventos automaticamente, ya esta todo configurado.
```

---

## Eventos

Un evento es una accion del usuario.

Ejemplos:

- ver una pagina;
- hacer scroll;
- clic en WhatsApp;
- clic en telefono;
- enviar formulario;
- descargar catalogo;
- ver producto;
- añadir al carrito;
- comprar.

Tipos de eventos:

```text
Automaticos -> GA4 los recoge por defecto.
Medicion optimizada -> se activan desde el flujo web.
Recomendados -> Google propone nombres y parametros.
Personalizados -> el equipo los define cuando no hay evento recomendado adecuado.
```

Regla:

```text
Usar evento recomendado cuando encaja.
Usar evento personalizado solo cuando ninguno encaja.
```

Eventos utiles para web de servicios:

- `generate_lead`;
- `form_submit`;
- `click_whatsapp`;
- `click_phone`;
- `click_email`;
- `booking_click`;
- `calendar_click`;
- `file_download`.

Eventos utiles para ecommerce:

- `view_item`;
- `view_item_list`;
- `select_item`;
- `add_to_cart`;
- `remove_from_cart`;
- `begin_checkout`;
- `add_shipping_info`;
- `add_payment_info`;
- `purchase`;
- `refund`.

Matriz de eventos:

```text
Evento:
Tipo:
Donde ocurre:
Que mide:
Valor para negocio:
Se marca como evento clave:
Parametros:
Metodo de implementacion:
Responsable:
```

Implementacion posible:

- Google Tag Manager;
- `gtag.js`;
- integracion CMS;
- plugin ecommerce;
- Measurement Protocol en casos avanzados.

Validacion:

- Realtime;
- DebugView;
- Events report;
- revision de duplicidad.

---

## Eventos clave

Evento:

```text
Cualquier interaccion medida.
```

Evento clave:

```text
Interaccion importante para negocio.
```

Conversion de Google Ads:

```text
Accion usada para medicion y optimizacion publicitaria en Google Ads.
```

El equipo debe diferenciar microconversion de conversion principal.

Microconversion:

- scroll;
- click en producto;
- descarga de catalogo;
- `add_to_cart`.

Conversion principal:

- lead;
- reserva;
- compra;
- llamada;
- WhatsApp.

Eventos clave por tipo de web:

Servicios:

- `form_submit`;
- `click_phone`;
- `click_whatsapp`;
- `booking_request`;
- `calendar_booking`;
- `lead_generated`.

Ecommerce:

- `purchase`;
- `begin_checkout`;
- `add_to_cart`, si se define como microconversion.

Local:

- `click_phone`;
- `click_whatsapp`;
- `reservation_click`;
- `directions_click`, si se mide desde la web;
- `menu_download`.

B2B:

- `form_submit`;
- `demo_request`;
- `download_catalog`;
- `contact_sales`;
- `quote_request`.

Error tipico:

```text
Marcar cualquier clic como evento clave.
```

---

## Adquisicion

GA4 permite saber de donde vienen usuarios y sesiones.

Diferencia clave:

```text
User acquisition -> como llegaron usuarios nuevos por primera vez.
Traffic acquisition -> de donde vienen las sesiones, nuevas o recurrentes.
```

Para SEO se revisa:

- `Session default channel group = Organic Search`;
- `Session source / medium = google / organic`;
- Landing page;
- Key events;
- Engagement;
- Revenue, si aplica.

Proceso:

```text
1. Ir a Traffic acquisition.
2. Filtrar Organic Search.
3. Revisar google / organic, bing / organic y otros buscadores.
4. Comparar contra canales: Paid Search, Direct, Referral, Social, Email.
5. Revisar calidad: sesiones, engagement, eventos clave, ingresos.
```

Interpretacion:

- SEO con trafico sin eventos clave -> revisar intencion, landing o CRO.
- SEO con menos trafico pero alta conversion -> canal de alta calidad.
- Paid con trafico caro sin conversion -> revisar campanas/landing.
- Direct muy alto -> puede ser marca, trafico mal etiquetado o atribucion.

---

## Source, medium, channel y campaign

Definiciones:

- Channel group: categoria general, por ejemplo Organic Search.
- Source: origen concreto, por ejemplo google.
- Medium: tipo de medio, por ejemplo organic.
- Campaign: campaña concreta.

SEO organico:

```text
Default channel group: Organic Search
Source / medium: google / organic
```

Problemas a detectar:

- Unassigned;
- Referral extraño;
- Direct demasiado alto;
- campañas sin UTM;
- pasarelas de pago robando atribucion;
- dominios propios clasificados mal.

Error tipico:

```text
No etiquetar campañas con UTMs y contaminar decisiones SEO.
```

---

## Landing Page Report

Para SEO, Landing Page Report es uno de los informes mas importantes porque
trabaja por URL de entrada.

Proceso:

```text
1. Entrar en Landing Page Report.
2. Filtrar Organic Search.
3. Revisar sesiones, usuarios, engaged sessions, engagement rate, average
   engagement time, key events e ingresos.
4. Clasificar paginas.
```

Clasificacion:

- trafico alto + eventos clave -> ganadora, proteger y reforzar;
- trafico alto + cero eventos clave -> problema de conversion o intencion;
- trafico bajo + alta conversion -> pagina valiosa, reforzar SEO;
- trafico alto + bajo engagement -> mala intencion, contenido debil o UX pobre;
- landing importante sin trafico -> problema SEO, indexacion, autoridad o
  arquitectura.

Conexion profesional:

```text
GSC: impresiones, clics, CTR y posicion.
GA4: sesiones, engagement, eventos clave e ingresos.
Decision: optimizar snippet, contenido, UX, CTA o arquitectura.
```

Entregable:

```text
Landing page:
Canal:
Sesiones organicas:
Engagement rate:
Tiempo medio:
Eventos clave:
Ingresos:
Problema:
Accion SEO/CRO:
Prioridad:
```

---

## Pages and Screens

Landing Page:

```text
Primera pagina de entrada de la sesion.
```

Pages and Screens:

```text
Todas las paginas vistas durante la navegacion.
```

Usos:

- ver articulos visitados;
- entender retencion;
- detectar paginas sin accion;
- revisar categorias/productos;
- detectar paginas con muchas vistas y pocos eventos.

Error tipico:

```text
Confundir muchas vistas con buen rendimiento.
```

---

## Conectar Search Console con GA4

Conectar GSC con GA4 permite ver informes de busqueda organica de Google dentro
de Analytics.

Requisitos:

- rol Editor en GA4;
- propietario verificado en Search Console.

Ruta:

```text
Admin -> Product links -> Search Console Links -> Link
```

Revisar:

- propiedad GSC correcta;
- flujo web correcto;
- dominio HTTPS correcto;
- datos disponibles.

Criterio:

```text
Aunque se conecten, GSC sigue siendo la fuente principal para consultas,
impresiones, CTR y posicion.
```

---

## GA4 para SEO On-Page

SEO On-Page no termina al subir title, H1, contenido y FAQs. Termina cuando se
comprueba si la pagina atrae usuarios correctos y genera acciones valiosas.

Proceso:

```text
1. Elegir URL.
2. Revisar GSC: consultas, clics, impresiones, CTR y posicion.
3. Revisar GA4: sesiones organicas, engagement, eventos, eventos clave e ingresos.
4. Diagnosticar.
5. Mejorar.
6. Revisar despues.
```

Diagnosticos:

- buen trafico + mala conversion -> CTA, confianza, formulario, mobile,
  intencion u oferta.
- bajo trafico + buena conversion -> pagina valiosa con problema de SEO.
- mucho engagement + cero leads -> contenido util sin salida comercial.

---

## GA4 para contenidos

GA4 ayuda a decidir que contenidos crear, mejorar, fusionar o mantener por
comportamiento real.

Clasificacion:

- contenido captador: trae usuarios desde Google;
- contenido asistente: ayuda antes de convertir;
- contenido comercial: convierte o empuja conversion;
- contenido muerto: no trae trafico, no retiene, no enlaza, no convierte;
- contenido peligroso: canibaliza pagina comercial.

Acciones:

- mejorar si trae trafico pero no convierte;
- reforzar si convierte y puede traer mas trafico;
- fusionar si hay similares debiles;
- eliminar/noindexar solo si no tiene trafico, enlaces, valor ni funcion;
- crear solo si hay intencion no cubierta.

Error tipico:

```text
Crear mas articulos sin revisar si los actuales generan valor.
```

---

## GA4 para SEO local

En SEO local no basta con aparecer. Hay que medir acciones reales.

Revisar:

- trafico por ciudad/pais;
- dispositivo movil;
- landings locales;
- clics en telefono;
- clics en WhatsApp;
- formularios;
- reservas;
- clics en como llegar, si se mide desde la web.

GSC + GBP + GA4:

```text
GSC muestra rendimiento organico.
GBP muestra acciones en Maps/perfil.
GA4 muestra comportamiento dentro de la web.
```

Error tipico:

```text
Ver trafico organico total y no separar trafico local real.
```

---

## GA4 para ecommerce SEO

SEO ecommerce se mide por negocio:

- productos vistos;
- add to cart;
- checkout iniciado;
- compras;
- ingresos;
- categorias que venden;
- productos que atraen trafico;
- productos con vistas pero sin compra.

Eventos clave:

- `view_item`;
- `view_item_list`;
- `select_item`;
- `add_to_cart`;
- `remove_from_cart`;
- `begin_checkout`;
- `add_shipping_info`;
- `add_payment_info`;
- `purchase`;
- `refund`.

Diagnosticos:

- categoria con trafico y ventas -> reforzar SEO, enlaces internos y contenido;
- producto con vistas y pocas compras -> precio, fotos, descripcion, confianza,
  stock;
- categoria sin trafico -> indexacion, contenido, keywords, enlaces internos;
- add_to_cart alto + purchase bajo -> checkout, envio, precio, confianza.

---

## Funnel Exploration

Funnel Exploration muestra pasos hacia una accion y donde abandonan los usuarios.

Ejemplos:

Servicios:

```text
Landing SEO -> click CTA -> formulario iniciado -> formulario enviado
```

Ecommerce:

```text
Landing categoria -> view_item -> add_to_cart -> begin_checkout -> purchase
```

Reserva:

```text
Pagina servicio -> click reservar -> calendario abierto -> reserva completada
```

Proceso:

```text
1. Ir a Explorations -> Funnel exploration.
2. Definir pasos.
3. Aplicar segmento Organic Search.
4. Analizar abandono por paso, pagina y dispositivo.
```

Error tipico:

```text
Medir solo evento final y no saber donde se pierde el usuario.
```

---

## Path Exploration

Path Exploration ayuda a ver rutas de usuario.

Preguntas:

- desde que paginas entra el trafico organico;
- a donde va despues;
- que contenidos empujan conversion;
- que caminos terminan en abandono;
- que paginas actuan como puente.

Interpretacion:

- articulo -> servicio: el contenido apoya conversion;
- articulo -> salida: falta CTA, enlaces internos o intencion comercial;
- contacto sin formulario enviado: problema de formulario/confianza/friccion;
- muchos van al menu: puede faltar claridad en la landing.

---

## Segmentos y audiencias

Segmento:

```text
Subconjunto de usuarios, sesiones o eventos usado en exploraciones.
```

Audiencia:

```text
Grupo de usuarios con caracteristicas o comportamientos definidos.
```

Segmentos utiles:

- Organic Search users;
- Organic Search sessions;
- usuarios que llegaron por blog;
- usuarios que llegaron por landing comercial;
- usuarios que convirtieron;
- usuarios que no convirtieron;
- usuarios moviles organicos;
- usuarios de Madrid;
- usuarios que vieron producto pero no compraron;
- usuarios con add_to_cart sin purchase.

---

## Cross-domain, referrals y limpieza de datos

Si hay subdominios, pasarelas, reservas externas o dominios externos, GA4 puede
cortar sesiones o atribuir mal conversiones.

Ejemplo:

```text
Google organic -> checkout externo -> thank you page
```

Si esta mal configurado, GA4 puede atribuir la conversion a referral o direct,
no a organic.

Revisar:

- subdominios;
- dominios externos de checkout;
- pasarelas de pago;
- calendarios externos;
- herramientas de reserva;
- WhatsApp links;
- cross-domain;
- unwanted referrals;
- internal traffic.

Error tipico:

```text
Celebrar que Referral convierte mucho cuando en realidad es la pasarela de pago
robando atribucion.
```

---

## Data retention y limitaciones

Data retention afecta cuanto tiempo conserva GA4 datos a nivel de usuario y
evento para exploraciones y analisis avanzados.

Documentar:

```text
Retencion actual:
Fecha de revision:
Quien la configuro:
Necesidad del proyecto:
Observaciones legales:
```

No todo es tecnico. Debe respetar privacidad, consentimiento y criterio legal
del proyecto.

Error tipico:

```text
Descubrir tarde que no se puede analizar un rango amplio porque la retencion
estaba mal configurada.
```

---

## CRO aplicado al SEO

Logica:

```text
SEO trae usuarios.
CRO convierte usuarios.
GA4 muestra donde se pierde el valor.
```

Proceso:

```text
1. Filtrar Organic Search.
2. Identificar landing pages principales.
3. Revisar eventos clave.
4. Revisar engagement.
5. Revisar funnel.
6. Revisar path exploration.
7. Detectar abandono.
8. Formular hipotesis.
9. Ejecutar cambio.
10. Medir resultado.
```

Entregable:

```text
URL:
Canal:
Evento esperado:
Evento real:
Punto de abandono:
Hipotesis:
Cambio:
Fecha:
Metrica objetivo:
```

---

## Rutinas

### Semanal

Detectar problemas:

1. sigue llegando trafico organico;
2. siguen funcionando eventos clave;
3. hay caidas raras en leads/compras;
4. hay trafico Unassigned extraño;
5. Realtime/DebugView confirma eventos nuevos;
6. hay cambios bruscos por canal;
7. landing principal perdio conversion.

Entregable:

```text
Fecha:
Problemas detectados:
Canal afectado:
Evento afectado:
URL afectada:
Accion urgente:
Responsable:
```

### Mensual

Alimenta roadmap SEO:

- sesiones organicas;
- usuarios organicos;
- engagement organico;
- eventos clave organicos;
- tasa de eventos clave;
- ingresos organicos, si aplica;
- landing pages organicas;
- paginas de contenido;
- ecommerce;
- embudos;
- rutas;
- comparativa contra mes anterior;
- comparativa YoY si aplica.

---

## Protocolos finales

### Web nueva + GA4

```text
1. Crear propiedad
2. Crear flujo web
3. Instalar etiqueta
4. Activar medicion optimizada
5. Definir plan de medicion
6. Configurar eventos personalizados/recomendados
7. Marcar eventos clave
8. Validar con Realtime
9. Validar con DebugView
10. Conectar Search Console
11. Configurar ecommerce, si aplica
12. Revisar cross-domain, si aplica
13. Crear segmentos basicos
14. Crear reporte SEO base
15. Documentar todo
```

No hacer:

- lanzar sin GA4;
- lanzar sin eventos clave;
- confiar solo en `page_view`;
- dejar formularios sin medicion;
- dejar WhatsApp/telfono sin medicion;
- medir ecommerce solo por visitas;
- instalar GA4 duplicado.

### Web existente + GA4

```text
1. Auditar instalacion
2. Revisar duplicidad de etiquetas
3. Revisar propiedad correcta
4. Revisar flujo web
5. Revisar eventos activos
6. Revisar eventos clave
7. Revisar trafico organico
8. Revisar landings organicas
9. Revisar Search Console conectado
10. Revisar ecommerce
11. Revisar cross-domain/referrals
12. Revisar data retention
13. Crear segmentos SEO
14. Crear embudos
15. Crear informe mensual
16. Crear roadmap CRO/SEO
```

No hacer:

- confiar en datos sin auditar medicion;
- comparar meses si hubo cambio de tracking;
- sacar conclusiones SEO sin filtrar Organic Search;
- llamar conversion a cualquier evento;
- ignorar Unassigned;
- mezclar usuarios nuevos con sesiones sin entender diferencia;
- optimizar paginas sin mirar eventos clave.

---

## Plantilla interna de analisis GA4

```text
Cliente:
Dominio:
Fecha:
Responsable:

1. Configuracion
- Propiedad:
- Flujo web:
- ID de medicion:
- GTM:
- Medicion optimizada:
- Search Console conectado:
- Ecommerce:
- Cross-domain:
- Data retention:

2. Trafico organico
- Sesiones organicas:
- Usuarios organicos:
- Engagement rate:
- Tiempo medio:
- Eventos:
- Eventos clave:
- Ingresos:

3. Landings SEO
- URL:
- Sesiones:
- Engagement:
- Eventos clave:
- Ingresos:
- Diagnostico:

4. Contenido
- Paginas informacionales:
- Paginas comerciales:
- Paginas sin conversion:
- Paginas asistenciales:

5. Eventos clave
- Evento:
- Volumen:
- Canal:
- URL:
- Estado:
- Observaciones:

6. Ecommerce, si aplica
- view_item:
- add_to_cart:
- begin_checkout:
- purchase:
- revenue:
- productos destacados:

7. Embudos
- Embudo:
- Paso de abandono:
- Hipotesis:
- Accion:

8. Problemas de medicion
- Duplicidad:
- Unassigned:
- Referral incorrecto:
- Eventos faltantes:
- Cross-domain:

9. Acciones recomendadas
- Accion:
- URL:
- Motivo:
- Prioridad:
- Responsable:
- Fecha de revision:
```

---

## Errores comunes

1. Mirar usuarios sin mirar eventos clave.
2. Mirar trafico organico sin filtrar bien el canal.
3. Confundir User acquisition con Traffic acquisition.
4. No medir WhatsApp, telefono o formularios.
5. Marcar eventos irrelevantes como eventos clave.
6. No validar eventos en DebugView.
7. No conectar Search Console.
8. No revisar Landing Page Report.
9. No configurar ecommerce correctamente.
10. No revisar cross-domain en pagos/reservas.
11. No revisar Unassigned.
12. No documentar eventos.
13. No cruzar GA4 con Search Console.
14. Optimizar SEO por trafico y no por negocio.
15. Hacer reportes sin decisiones.

---

## Formacion minima obligatoria

Nivel 1 - Base:

1. Set up Analytics for a website/app.
2. About events.
3. Enhanced measurement.
4. Realtime / DebugView.
5. Key events.

Nivel 2 - SEO y adquisicion:

6. Acquisition overview.
7. Traffic acquisition.
8. User acquisition vs Traffic acquisition.
9. Landing page report.
10. Connect Search Console to GA4.

Nivel 3 - CRO y comportamiento:

11. Pages and screens.
12. Explorations.
13. Funnel exploration.
14. Path exploration.
15. Segment builder.

Nivel 4 - Ecommerce y medicion avanzada:

16. Recommended events.
17. Measure ecommerce.
18. Ecommerce purchases report.
19. Measurement Protocol.
20. Data retention / configuration limits.

Nota:

```text
Rodrigo dio nombres de fuentes oficiales, pero no todas las URLs explicitas.
Antes de convertirlas en examen o modulo oficial para agentes reales, el
Docente SEO debe verificar cada enlace en fuente viva.
```

---

## Regla final para relevo

Cada analisis de GA4 debe terminar con:

```text
Que canal trajo usuarios.
Que landing recibio trafico.
Que hizo el usuario.
Que evento ejecuto.
Que valor genero.
Donde se perdio.
Que accion debemos tomar.
Como vamos a medir si funciono.
```

La persona que mira GA4 y solo reporta usuarios, sesiones y paginas vistas no
esta haciendo analitica SEO profesional. Esta mirando estadisticas.

La persona que cruza canal + landing + intencion + evento clave + negocio ya
esta empezando a trabajar como analista SEO real.
