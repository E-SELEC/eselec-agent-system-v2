# Modulo SEO Changelog - Rodrigo

- Fecha: 2026-05-11
- Estado: aprendido / pendiente de verificacion viva de fuentes oficiales
- Fuente: `agents/docente/seo/fuentes/2026-05-11-manual-seo-serp-qa-changelog.md`
- Alcance: laboratorio del Docente SEO
- Restriccion: no modifica `agents/seo/`

---

## Idea central

El SEO changelog es el sistema donde se documenta cada cambio relevante hecho en
una web, URL, plantilla, contenido, medicion, arquitectura, producto, categoria,
ficha local, feed, schema o configuracion tecnica.

La explicacion simple:

```text
Un SEO changelog es la memoria operativa del proyecto.
```

Regla principal:

```text
Si no se documenta que se cambio, cuando se cambio y por que se cambio, despues
nadie puede analizar correctamente una subida, una caida o un problema.
```

Sin changelog, el analisis SEO se vuelve suposicion.

---

## Que NO es un changelog

No es:

- hoja administrativa sin uso;
- lista para demostrar que se trabajo;
- duplicado del gestor de tareas;
- reporte para cliente;
- memoria vaga;
- lugar para escribir "se optimizo pagina";
- archivo que se llena solo al final.

Regla:

```text
El changelog no es para demostrar que se trabajo.
Es para entender que paso y que efecto pudo tener.
```

---

## Web nueva vs web existente

### Web nueva

El changelog empieza desde el primer dia.

Flujo:

```text
1. Crear changelog desde inicio
2. Registrar arquitectura inicial
3. Registrar publicaciones
4. Registrar configuracion GSC/GA4/GTM
5. Registrar sitemap
6. Registrar QA previo
7. Registrar lanzamiento
8. Registrar cambios post-launch
9. Revisar resultados
```

Mentalidad:

```text
En web nueva, el changelog crea la linea base del proyecto.
```

### Web existente

Protege el historico.

Flujo:

```text
1. Revisar si existe changelog previo
2. Crear uno si no existe
3. Registrar estado inicial
4. Registrar auditoria
5. Registrar cambios ejecutados
6. Registrar QA
7. Registrar incidencias
8. Registrar resultados
9. Revisar en reportes mensuales
```

Mentalidad:

```text
En web existente, el changelog ayuda a saber si una caida viene de un cambio,
de Google, de competencia o de un problema tecnico.
```

---

## Cambios que deben documentarse

Documentar:

- titles/metas;
- H1/H2;
- contenido importante;
- URLs;
- redirecciones;
- canonicals;
- robots/noindex;
- sitemap;
- enlaces internos;
- schema;
- GTM/GA4;
- eventos clave;
- formularios;
- ecommerce tracking;
- productos/categorias;
- Merchant Center;
- GBP;
- migraciones;
- redisenos;
- cambios de plantilla;
- cambios de hosting;
- cambios de velocidad;
- QA;
- incidencias.

No necesitan changelog:

- correcciones minimas sin impacto;
- typos menores sin cambio de intencion;
- ajustes visuales irrelevantes sin impacto SEO/CRO;
- pruebas internas no publicadas.

---

## Campos minimos

Un changelog sin URL es casi inutil para SEO.

Campos:

```text
ID:
Fecha:
Cliente:
URL:
Tipo de cambio:
Descripcion:
Fuente del hallazgo:
Motivo:
Metrica previa:
Metrica esperada:
Riesgo:
Responsable:
QA:
Estado:
Fecha de revision:
Resultado:
Notas:
```

Usar fechas absolutas.

---

## Tipos de cambio

- On-Page;
- contenido;
- tecnico;
- arquitectura;
- enlaces internos;
- redirecciones;
- migracion;
- schema;
- GBP;
- Merchant Center;
- GTM/GA4;
- ecommerce tracking;
- CRO;
- velocidad;
- incidencia externa;
- core update;
- QA.

---

## Changelog por herramienta

GSC:

- anotaciones ayudan, pero no sustituyen changelog interno;
- registrar cambios relacionados con caidas/subidas;
- comparar fechas.

GA4:

- registrar cambios de eventos;
- registrar cambios de conversion/eventos clave;
- registrar tracking roto/corregido.

Looker Studio:

- visualizar changelog si el reporting es serio;
- cruzar acciones con evolucion.

Sheets / Notion:

- buenos lugares para changelog operativo si estan bien estructurados.

---

## Changelog por tipo de accion

Title/meta:

- URL;
- title/meta anterior;
- title/meta nuevo;
- query objetivo;
- motivo;
- fecha de revision.

Contenido:

- secciones cambiadas;
- intencion;
- SERP;
- terminos;
- CTA;
- enlaces;
- fecha de revision.

Enlaces internos:

- origen;
- destino;
- anchor;
- motivo;
- paginas reforzadas.

Tecnico:

- problema;
- URLs;
- correccion;
- validacion;
- riesgo.

Redirecciones:

- URL antigua;
- URL nueva;
- tipo;
- motivo;
- estado.

Migraciones:

- obligatorio;
- cada fase debe quedar registrada;
- sin changelog, la migracion queda sin control.

GBP:

- categoria;
- servicios;
- fotos;
- reseñas;
- horarios;
- URL;
- cambios sensibles.

Merchant Center:

- feed;
- precio;
- stock;
- disponibilidad;
- politicas;
- errores corregidos.

Schema:

- tipo;
- fuente;
- validacion;
- errores;
- coincidencia con contenido.

GTM/GA4:

- etiqueta;
- activador;
- variable;
- evento;
- version;
- DebugView;
- evento clave.

---

## Changelog y analisis de caidas

Proceso:

```text
1. Detectar caida en GSC/GA4.
2. Revisar fecha exacta.
3. Abrir changelog.
4. Ver cambios ocurridos antes.
5. Revisar eventos externos.
6. Revisar Search Status Dashboard.
7. Revisar core updates.
8. Revisar tecnico.
9. Formular hipotesis.
10. Validar.
```

Regla:

```text
Cuando cae trafico, el changelog es una de las primeras fuentes.
```

---

## Changelog y analisis de subidas

Proceso:

```text
1. Detectar subida.
2. Revisar fecha.
3. Consultar changelog.
4. Identificar cambios previos.
5. Revisar eventos externos.
6. Confirmar si el cambio pudo causar impacto.
7. Replicar aprendizajes.
```

El changelog no solo explica problemas. Tambien ayuda a entender que funciono.

---

## Changelog, QA y tareas

El changelog no sustituye el gestor de tareas.

```text
Tarea = que hay que hacer.
Changelog = que se hizo, cuando, por que y que efecto tuvo.
```

QA debe alimentar changelog.

```text
Todo cambio que nace de QA debe quedar registrado.
```

Tarea ejecutada sin changelog queda incompleta si afecta SEO, medicion o negocio.

---

## Roles y permisos

Roles:

- ejecutor;
- revisor;
- aprobador;
- responsable de resultado.

Regla:

```text
No todos editan el changelog historico sin control.
```

Si se corrige una entrada antigua, debe quedar claro.

---

## Changelog y cliente

No se envia al cliente todo el changelog crudo.

Se traduce:

- que se hizo;
- por que importa;
- que impacto se espera;
- que se medira;
- que sigue.

El changelog protege profesionalmente a la agencia porque muestra decisiones,
fechas, responsables y contexto.

---

## Changelog y resultados

Un changelog sin resultado es medio changelog.

Cada entrada importante debe revisarse:

- sin resultado aun;
- mejoro;
- empeoro;
- neutral;
- necesita mas tiempo;
- revertir;
- iterar.

Reversion:

- documentar que se revierte;
- por que;
- a que estado;
- fecha;
- validacion.

---

## Plantilla interna SEO changelog

```text
ID:
Fecha:
Cliente:
Dominio:
URL:
Tipo de cambio:
Modulo SEO afectado:
Descripcion del cambio:
Fuente del hallazgo:
Motivo:
Metrica previa:
Resultado esperado:
Riesgo:
Responsable:
Revisor:
QA realizado:
Estado:
Fecha de revision:
Resultado:
Decision siguiente:
Notas:
Captura/enlace:
```

---

## Errores comunes

1. No tener changelog.
2. Registrar "optimizacion" sin URL.
3. No poner fecha absoluta.
4. No registrar motivo.
5. No registrar metrica previa.
6. No registrar fecha de revision.
7. No conectar QA.
8. No registrar GTM/GA4.
9. No registrar redirecciones.
10. No registrar migraciones.
11. No registrar GBP/Merchant/schema.
12. Modificar historico sin avisar.
13. Usarlo como reporte cliente crudo.
14. No revisar resultados.
15. No aprender de cambios repetidos.

---

## Regla final para relevo

Un SEO changelog no se hace para llenar una hoja.

```text
Se hace para que el equipo pueda entender que cambio, por que cambio y que
impacto tuvo.
```

Cada entrada debe poder responder:

```text
Que se cambio.
En que URL.
Cuando.
Por que.
Quien lo hizo.
Que riesgo tenia.
Que QA tuvo.
Que resultado se esperaba.
Cuando se revisara.
Que resultado obtuvo.
```
