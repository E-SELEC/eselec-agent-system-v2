---
name: verificacion-medicion
description: >
  Verifica si un cliente tiene medicion suficiente antes de auditorias,
  informes, SEO, CRO, Ads o decisiones de negocio. Usalo cuando falten GA4,
  GSC, GBP, SEMrush, Ads, conversiones, eventos, fuentes vivas, lineas base o
  cuando un output pueda perder calidad por datos no comprobados.
---

# Verificacion Medicion - E-SELEC

## Proposito

Comprobar si los datos disponibles permiten tomar decisiones fiables.

Esta skill evita tres fallos frecuentes:

- auditar como si hubiera datos vivos cuando solo hay contexto antiguo;
- mezclar fuentes sin confirmar que pertenecen al mismo dominio/cliente;
- entregar recomendaciones finales cuando el diagnostico debe ser parcial.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/log.md`
3. `clients/[cliente]/memory.md` si existe
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `quality/criterios-output.md`
7. `protocols/gestion-accesos.md`
8. `protocols/activos-criticos.md` si la verificacion implica fuentes vivas

No pidas ni guardes secretos. Si falta un acceso, registra el acceso como faltante y explica como conectarlo sin pedir tokens en chat.

## Nivel de medicion

Clasifica antes de recomendar acciones:

- Nivel 3 - verificada: fuentes vivas necesarias revisadas, propiedad/cuenta coincide con el cliente y hay rango de fechas claro.
- Nivel 2 - parcial fuerte: al menos una fuente viva o export reciente relevante, pero faltan fuentes que pueden cambiar la decision.
- Nivel 1 - declarada: solo contexto, logs, capturas antiguas o afirmaciones no comprobadas.
- Nivel 0 - bloqueada: falta dominio/cliente, hay contradiccion critica o no se puede saber que fuente corresponde al cliente.

Regla:

- Nivel 0 no permite auditoria final.
- Nivel 1 solo permite orientacion.
- Nivel 2 permite diagnostico parcial.
- Nivel 3 permite auditoria o informe final si el resto del output cumple su contrato.

## Fuentes por tipo de trabajo

Usa esta matriz para decidir que falta:

| Trabajo | Fuentes minimas recomendadas |
|---|---|
| SEO organico | GSC + SEMrush + revision tecnica/render + contexto |
| SEO local | GBP + GSC + sitio + contexto local |
| Informe mensual | GA4/GSC/GBP/Ads/redes segun servicios contratados + log del periodo |
| CRO | GA4 eventos/conversiones + URL/pagina + objetivo de conversion |
| SEM/Ads | plataforma Ads + conversion/pixel + landing + presupuesto |
| Web/WooCommerce | sitio/CMS + analitica + formularios/checkout si aplica |
| Social | plataforma o export + calendario/log + objetivo del canal |

Si una fuente no existe o no esta conectada, no bloquees todo por defecto. Decide si esa fuente cambia la conclusion.

## Workflow

### 1. Definir alcance

Determina:

- cliente;
- dominio o URL;
- periodo de analisis;
- servicio afectado;
- decision que se quiere tomar;
- si el resultado queda en chat o se guarda en `clients/[cliente]/outputs/`.

Si falta el cliente o dominio, no inventes.

### 2. Leer contexto e historial

Extrae:

- servicios contratados;
- dominio principal;
- herramientas declaradas;
- ultimas acciones de medicion;
- problemas o mensajes pendientes;
- outputs recientes relacionados.

Marca contradicciones entre contexto, log y mensajes.

### 3. Revisar disponibilidad de fuentes

Para cada fuente relevante, comprueba:

- si existe acceso o dato disponible;
- si la cuenta/propiedad corresponde al cliente;
- dominio, URL, cuenta o negocio asociado;
- rango de fechas;
- ultima actualizacion;
- metrica minima visible;
- limitacion o duda.

No ejecutes cambios en herramientas vivas. Solo lectura.

### 4. Detectar bloqueos de calidad

Bloquea o marca parcial si:

- el dominio no coincide;
- la fuente parece de otro cliente;
- el periodo no esta definido;
- faltan conversiones para decidir Ads/CRO;
- falta GSC/SEMrush para afirmar causas SEO;
- hay datos contradictorios que cambian la prioridad;
- se necesita accion en produccion para seguir.

### 5. Decidir nivel y siguiente accion

El resultado debe responder:

- que se puede afirmar;
- que no se puede afirmar;
- que fuente falta;
- que decision queda permitida;
- una sola proxima accion.

### 6. Generar output

Usa `templates/informe-medicion.md`.

Reglas:

- no mas de 7 fuentes revisadas;
- no convertir falta de datos en recomendacion generica;
- separar "fuente no conectada" de "fuente conectada pero sin datos";
- incluir permiso de uso: final, parcial, orientativo o bloqueado.

### 7. Revisar antes de entregar

Usa `checklists/revision.md`.

El minimo aceptable para auditorias SEO, informes o decisiones de Ads es Nivel 2. El estandar E-SELEC es Nivel 3.

## Bloqueos

Detente si:

- el usuario pide pegar tokens, claves, cookies o secretos;
- no hay forma de asociar la fuente al cliente correcto;
- la verificacion exige modificar una web, campana, propiedad, pixel, etiqueta, conversion o fuente de verdad;
- una contradiccion puede llevar a una recomendacion falsa.

Si hay que tocar produccion, aplica `protocols/activos-criticos.md` y pide confirmacion explicita.

## Archivos de apoyo

- `templates/informe-medicion.md`: formato de salida.
- `checklists/revision.md`: revision antes de entregar.
