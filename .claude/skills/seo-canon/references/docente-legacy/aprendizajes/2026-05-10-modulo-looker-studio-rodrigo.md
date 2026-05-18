# Modulo Looker Studio - Rodrigo

- Fecha: 2026-05-10
- Estado: aprendido / pendiente de verificacion viva de enlaces oficiales
- Fuente: `agents/docente/seo/fuentes/2026-05-10-manual-seo-post-neuronwriter.md`
- Alcance: laboratorio del Docente SEO
- Restriccion: no modifica `agents/seo/`

---

## Idea central

Looker Studio es una herramienta de reporting y visualizacion de datos.

La idea simple:

```text
Looker Studio no hace SEO.
Looker Studio comunica, organiza y visualiza el rendimiento SEO.
```

No se usa para hacer dashboards bonitos.

```text
Se usa para que Rodrigo, el equipo o el cliente entiendan que esta pasando,
que importa y que accion toca ejecutar.
```

---

## Lugar en el sistema

```text
SEMrush -> investiga mercado, competencia, keywords y oportunidades.
GSC -> muestra como Google enseña la web en resultados.
GA4 -> mide comportamiento, eventos, leads, ventas y valor.
GTM -> implementa medicion.
Screaming Frog -> audita la web por dentro.
GBP -> mide y optimiza presencia local.
WordPress/WooCommerce -> implementa web y ecommerce.
Looker Studio -> comunica datos y decisiones.
```

Looker Studio conecta especialmente con:

- medicion continua;
- reporting mensual;
- SEO tecnico si se importan datos;
- GSC;
- GA4;
- GBP;
- ecommerce;
- roadmap;
- changelog;
- seguimiento de acciones.

---

## Web nueva vs web existente

### Web nueva

Looker Studio se configura para crear linea base desde el lanzamiento.

Flujo:

```text
1. Definir KPIs
2. Crear reporte base
3. Conectar GA4
4. Conectar GSC
5. Conectar GBP si aplica
6. Crear vista Search Console
7. Crear vista GA4 organico
8. Crear vista landings
9. Crear vista eventos/conversiones
10. Crear changelog
11. Medir primeros datos
```

Mentalidad:

```text
En web nueva, Looker Studio evita trabajar a ciegas desde el inicio.
```

### Web existente

Looker Studio ordena datos historicos y los convierte en decisiones.

Flujo:

```text
1. Auditar fuentes
2. Conectar GA4
3. Conectar GSC
4. Conectar GBP si aplica
5. Añadir datos de SEMrush exportados si aplica
6. Añadir Screaming Frog/Sheets si aplica
7. Crear resumen ejecutivo
8. Crear paginas por area
9. Crear filtros y comparativas
10. Crear roadmap/changelog
11. Revisar mensualmente
```

Mentalidad:

```text
En web existente, Looker Studio no debe repetir datos: debe ordenar decisiones.
```

---

## Que NO es Looker Studio

Looker Studio no es:

- fuente primaria de datos;
- herramienta de auditoria SEO;
- sustituto de GSC;
- sustituto de GA4;
- sustituto de SEMrush;
- solucion a datos mal configurados;
- reporte para llenar graficas.

Regla:

```text
Looker Studio depende de sus fuentes.
Si GA4 esta mal, el dashboard estara mal.
Si GSC esta mal conectado, el reporte estara incompleto.
Si no existen eventos clave, Looker Studio no puede inventar conversiones.
```

---

## Conceptos base

El equipo debe entender:

- reporte;
- pagina;
- fuente de datos;
- conector;
- campo;
- metrica;
- dimension;
- control;
- filtro;
- parametro;
- campo calculado;
- blend;
- credenciales;
- permiso de visualizacion/edicion.

Fuente de datos:

```text
Conexion entre Looker Studio y una plataforma.
```

---

## Fuentes SEO obligatorias

Fuentes habituales:

- Google Search Console;
- Google Analytics 4;
- Google Business Profile, si aplica;
- Google Ads, si aplica;
- Google Sheets;
- SEMrush exportado;
- Screaming Frog exportado;
- BigQuery, si aplica.

Regla:

```text
Cada fuente debe tener nombre claro, propietario claro y permiso controlado.
```

---

## Conectar GSC y GA4

GSC:

```text
1. Entrar en Looker Studio.
2. Crear fuente de datos.
3. Elegir Search Console.
4. Autorizar acceso.
5. Elegir propiedad.
6. Elegir tabla Site Impression o URL Impression.
7. Añadir a reporte.
```

GA4:

```text
1. Crear fuente de datos.
2. Elegir Google Analytics.
3. Autorizar.
4. Seleccionar cuenta.
5. Seleccionar propiedad GA4.
6. Añadir a reporte.
```

Criterio:

```text
GSC muestra busqueda.
GA4 muestra comportamiento.
Ambos deben convivir, no mezclarse sin sentido.
```

---

## Estructura profesional de dashboard SEO

Paginas recomendadas:

1. Resumen ejecutivo.
2. Search Console.
3. GA4 organico.
4. Landing pages SEO.
5. Contenidos.
6. Conversion / CRO SEO.
7. SEO local.
8. Ecommerce SEO.
9. Tecnico / issues.
10. Roadmap y changelog.

Regla:

```text
Primero decision, despues grafico.
```

---

## Pagina 1: resumen ejecutivo

Debe responder:

- que subio;
- que bajo;
- que importa;
- que problema existe;
- que accion toca;
- que se hizo;
- que se hara.

No debe ser una coleccion de graficas sin interpretacion.

---

## Paginas clave

Search Console:

- clics;
- impresiones;
- CTR;
- posicion media;
- top queries;
- top pages;
- oportunidades;
- caidas.

GA4 organico:

- sesiones organicas;
- usuarios;
- engagement;
- eventos clave;
- ingresos;
- landings;
- canales.

Landings SEO:

- URL;
- clics GSC;
- sesiones GA4;
- eventos clave;
- ingresos;
- diagnostico.

Contenidos:

- articulos con trafico;
- engagement;
- asistencia a conversion;
- contenidos sin accion;
- oportunidades.

CRO SEO:

- formularios;
- WhatsApp;
- telefono;
- reservas;
- compras;
- embudos.

SEO local:

- GBP;
- llamadas;
- rutas;
- clics a web;
- landings locales;
- consultas locales.

Ecommerce:

- categorias;
- productos;
- add to cart;
- checkout;
- purchases;
- revenue.

Tecnico:

- issues de Screaming Frog importados;
- indexacion;
- 404;
- canonicals;
- redirecciones;
- Core Web Vitals si se importa.

Roadmap:

- acciones realizadas;
- acciones pendientes;
- responsable;
- fecha;
- impacto esperado;
- estado.

---

## Campos calculados, blends y filtros

Campos calculados:

- ayudan a crear metricas propias;
- deben documentarse;
- no deben inventar precision falsa.

Blending:

- permite combinar datos de fuentes;
- puede romper interpretacion si las claves no coinciden;
- usar con cuidado.

Filtros:

- canal organico;
- pais;
- dispositivo;
- tipo de pagina;
- fecha;
- cliente;
- URL.

Regla:

```text
Un filtro mal puesto puede hacer que el dashboard mienta.
```

---

## Permisos y credenciales

Reglas:

```text
1. No crear dashboards criticos desde cuentas personales sin control.
2. Nombrar fuentes claramente.
3. Separar reportes por cliente.
4. Revisar permisos antes de compartir.
5. No dar edicion si solo deben ver.
```

Riesgo:

```text
Un dashboard puede exponer datos sensibles si se comparte mal.
```

---

## Reporte interno vs cliente

Interno:

- puede mostrar problemas crudos;
- incluye tareas;
- incluye riesgos;
- incluye responsables;
- puede tener datos tecnicos.

Cliente:

- debe ser claro;
- debe explicar impacto;
- debe evitar ruido;
- debe mostrar decisiones;
- debe traducir datos a negocio.

Regla:

```text
El cliente no necesita ver todo. Necesita entender que pasa y que haremos.
```

---

## Como evitar dashboards inutiles

Errores comunes:

1. Demasiados graficos.
2. Sin resumen ejecutivo.
3. Sin acciones.
4. Sin comparacion de fechas.
5. Sin filtros utiles.
6. Sin separar organico de otros canales.
7. Sin eventos clave.
8. Sin ingresos o leads.
9. Sin contexto.
10. Sin changelog.
11. Sin prioridades.
12. Datos mezclados incorrectamente.
13. Fuentes rotas.
14. Diseño bonito, decision pobre.

Regla:

```text
Un dashboard util reduce confusion y acelera decisiones.
```

---

## Rutina mensual

Cada revision debe:

```text
1. Revisar fuentes rotas.
2. Revisar periodo.
3. Comparar contra mes anterior.
4. Comparar YoY si aplica.
5. Revisar GSC.
6. Revisar GA4 organico.
7. Revisar conversiones.
8. Revisar landings.
9. Revisar contenido.
10. Revisar local/ecommerce si aplica.
11. Revisar roadmap.
12. Definir acciones.
```

---

## Plantilla de configuracion

```text
Cliente:
Dominio:
Fecha:
Responsable:

1. Fuentes
- GSC:
- GA4:
- GBP:
- Sheets:
- SEMrush:
- Screaming Frog:

2. Permisos
- Propietario:
- Editores:
- Visores:
- Credenciales:

3. Paginas del reporte
- Resumen:
- GSC:
- GA4:
- Landings:
- Contenido:
- CRO:
- Local:
- Ecommerce:
- Tecnico:
- Roadmap:

4. KPIs
- Visibilidad:
- Trafico:
- Engagement:
- Conversion:
- Ingresos:
- Tecnico:

5. Changelog
- Fecha:
- Cambio:
- Responsable:
- Impacto esperado:
```

---

## Regla final para relevo

Looker Studio no se usa para enseñar numeros.

```text
Se usa para explicar rendimiento y convertir datos en decisiones.
```

Cada dashboard debe poder responder:

```text
Que fuentes usa.
Que periodo muestra.
Que canal analiza.
Que subio.
Que bajo.
Que URL importa.
Que evento importa.
Que accion toca.
Quien la hara.
Cuando se revisara.
```

Si una persona dice "hice un dashboard bonito", todavia no entendio Looker
Studio.
