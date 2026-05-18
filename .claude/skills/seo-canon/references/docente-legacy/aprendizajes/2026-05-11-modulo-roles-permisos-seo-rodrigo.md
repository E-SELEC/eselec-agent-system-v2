# Modulo Roles Internos y Permisos SEO - Aprendizaje del Docente

- Fecha: 2026-05-11
- Origen: `Manual_SEO_Priorizacion_IA_Internacional_Roles_EXACTO.pdf`
- Estado: aprendido / pendiente de convertir en matriz operativa

---

## Que debe aprender el Docente

Los roles internos y permisos definen quien puede ver, editar, aprobar, publicar, medir, corregir, eliminar o tocar configuraciones criticas dentro de un proyecto SEO.

Regla central:

```text
No todo el que sabe entrar a una herramienta
debe tener permiso para cambiarla.
```

En SEO, un error de permisos puede romper:

```text
indexacion
medicion
conversiones
datos historicos
Merchant Center
Google Business Profile
GTM
GA4
WordPress
WooCommerce
robots.txt
canonicals
redirecciones
checkout
trafico organico
reporting
```

---

## Diferencia entre rol y permiso

```text
Rol:
responsabilidad de una persona dentro del sistema.

Permiso:
accion que esa persona puede ejecutar en una herramienta.
```

Tambien debe diferenciarse:

```text
ver
editar
aprobar
publicar
eliminar
administrar usuarios
modificar configuracion critica
```

---

## Roles SEO principales

```text
SEO Lead:
prioriza, aprueba riesgo, decide estrategia y coordina.

Technical SEO Specialist:
diagnostica rastreo, indexacion, canonicals, redirects, CWV, logs, schema tecnico.

SEO Content Specialist:
briefs, contenido, intencion, optimizacion semantica, FAQs y enlaces internos.

SEO Junior / Assistant:
extrae datos, prepara tablas, revisa checklists y ejecuta tareas de bajo riesgo.

CRO / UX:
analiza conversion, CTAs, formularios, experiencia movil y friccion.

Developer / Implementer:
aplica cambios tecnicos, plantillas, CMS, redirects, performance y QA tecnico.

Analytics / Tracking:
GTM, GA4, eventos, key events, ecommerce, cross-domain y validacion.

Local SEO:
GBP, NAP, categorias, reseñas, landings locales y senales locales.

Ecommerce / Merchant Center:
feeds, productos, schema Product, envios, devoluciones, precios y shopping.

Reports / Looker:
dashboards, informes, visualizacion y narrativas de decision.

Cliente / Approver:
aprueba cambios de negocio, marca, legales, precios, ofertas y riesgos altos.
```

---

## RACI

El Docente debe ensenar a clasificar cada tarea:

```text
R - Responsible:
quien ejecuta.

A - Accountable:
quien responde por el resultado.

C - Consulted:
quien debe ser consultado.

I - Informed:
quien debe ser informado.
```

Regla:

```text
Una tarea critica sin accountable claro es una tarea peligrosa.
```

---

## Permisos por herramienta

### Google Search Console

```text
Owner:
solo responsables senior o propietarios reales.

Full user:
perfiles que necesitan operar y revisar datos completos.

Restricted user:
lectura y analisis sin poder sensible.
```

### GA4

No todo analista necesita administrar propiedad.

Controlar:

```text
administradores
editores
marketers
analistas
viewers
eventos clave
vinculaciones
data retention
```

### Google Tag Manager

Alto riesgo.

Separar:

```text
leer
editar workspace
aprobar
publicar
administrar usuarios
```

Regla:

```text
Un junior no publica cambios en GTM sin revision.
```

### Google Business Profile

Cambios sensibles:

```text
categoria principal
nombre
direccion
telefono
URL
horarios
servicios
propietarios
```

Estos cambios requieren aprobacion.

### Merchant Center

Alto impacto comercial.

Controlar:

```text
feeds
productos
envios
devoluciones
politicas
vinculacion Google Ads
diagnosticos
usuarios
```

### WordPress / WooCommerce

No dar Administrator por comodidad.

Separar:

```text
editor
author
shop manager
SEO manager si existe
administrator solo para responsables reales
```

WooCommerce afecta ventas, precios, stock, checkout y pedidos.

---

## Niveles de riesgo

```text
Bajo:
acciones reversibles y sin impacto tecnico critico.

Medio:
cambios que afectan contenido, enlaces o pequenas configuraciones.

Alto:
URLs, canonicals, robots, indexacion, tracking, GTM, Merchant Center, GBP.

Critico:
migraciones, dominio, checkout, eliminacion masiva, permisos admin, datos historicos.
```

Regla:

```text
Riesgo alto o critico requiere aprobacion senior y changelog.
```

---

## Onboarding y offboarding

Al incorporar a alguien:

```text
definir rol
definir herramientas
dar minimo permiso necesario
documentar acceso
explicar riesgos
asignar responsable
```

Al retirar a alguien:

```text
revocar accesos
transferir propiedad
rotar secretos si aplica
cerrar usuarios
documentar fecha
validar que no quedan permisos activos
```

Regla:

```text
No usar cuentas personales como fuente de verdad.
No compartir contrasenas por comodidad.
No dejar excolaboradores con accesos activos.
```

---

## Casos especiales

### Migraciones

Requieren comite minimo:

```text
SEO Lead
Technical SEO
Developer
Analytics
Cliente / Approver
```

### SEO internacional

Multiplica el riesgo.

No permitir cambios de hreflang, canonicals, arquitectura o versiones regionales sin revision senior.

### SEO para IA externo

Robots.txt, llms.txt y permisos de crawlers IA son decisiones estrategicas.

No deben quedar en manos de un perfil junior o de desarrollo sin criterio SEO.

---

## Plantilla de matriz de permisos

```text
Cliente:
Proyecto:
Herramienta:
Usuario:
Rol interno:
Permiso asignado:
Puede ver:
Puede editar:
Puede publicar:
Puede administrar usuarios:
Riesgo:
Aprobador:
Fecha de alta:
Fecha de revision:
Fecha de baja:
Observaciones:
```

---

## Errores que el Docente debe corregir

```text
Dar administrador a todos.
Compartir una misma cuenta.
No documentar accesos.
No revocar permisos al terminar una relacion.
Permitir que juniors publiquen en GTM.
Permitir cambios de GBP sin aprobacion.
Dar acceso a Merchant Center sin explicar impacto.
No distinguir ver de editar.
No tener accountable para tareas criticas.
No registrar cambios sensibles en changelog.
```

---

## Regla final

```text
Roles y permisos no son burocracia.
Son proteccion contra errores que pueden romper SEO,
medicion, ventas y reputacion.
```
