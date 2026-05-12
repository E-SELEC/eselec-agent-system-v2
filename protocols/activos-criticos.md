# Protocolo de activos criticos

## Estado

- Version: 2.0
- Fecha: 2026-05-12
- Fuente legacy: `sistema/protocolos/activos-criticos.md`
- Sistema destino: E-SELEC Agent System v2
- Estado: vigente

## Objetivo

Evitar dano operacional antes de modificar sistemas, cuentas, datos, integraciones, configuraciones o fuentes de verdad de E-SELEC o de clientes.

Este protocolo decide:

- si una accion puede afectar produccion;
- que nivel de riesgo tiene;
- si hace falta Orden de Cambio;
- que rollback o mitigacion debe existir;
- cuando el agente debe detenerse;
- que verificar despues.

## Explicacion simple para Rodrigo

Un activo critico es cualquier cosa que, si se toca mal, puede romper una web, una campana, una tienda, una medicion, un flujo de venta, un acceso, una fuente de verdad o una decision futura.

La regla es: **antes de tocar algo real, se clasifica el riesgo y se pide aprobacion si corresponde**.

## Activos criticos cubiertos

Aplica a cualquier activo actual o futuro, incluyendo:

- webs;
- WordPress;
- WooCommerce;
- plugins;
- temas;
- CSS/JS en produccion;
- hosting;
- DNS;
- SSL;
- bases de datos;
- backups/restores;
- Google Analytics;
- Google Search Console;
- Google Business Profile;
- Google Drive;
- Notion;
- Meta Ads;
- Google Ads;
- conversion tracking;
- pasarelas de pago;
- envios;
- formularios;
- automatizaciones;
- scripts;
- conectores;
- MCP;
- credenciales;
- `.env`;
- fuentes de verdad;
- documentos operativos;
- datos vivos;
- outputs que otros agentes usen para decidir.

Si hay duda razonable, se considera critico.

## Senales de afectacion

Un cambio es critico si puede:

- hacer que algo cargue peor;
- romper o degradar una web;
- alterar diseno visible;
- ocultar contenido, productos, formularios o datos;
- cambiar precios, pagos, envios o disponibilidad;
- consumir presupuesto;
- pausar, activar o modificar campanas;
- romper tracking o reporting;
- cambiar datos usados por otros agentes;
- crear contradicciones entre fuente viva y documentacion;
- exponer datos, accesos o informacion interna;
- dificultar rollback;
- hacer que Rodrigo o un cliente decidan sobre datos falsos.

## Niveles de accion

### Nivel A - Solo lectura

Ejemplos:

- auditorias;
- capturas;
- consultas API read-only;
- lectura de logs;
- crawlers defensivos no destructivos;
- revision de configuracion sin guardar cambios.

Reglas:

- permitido si el usuario pidio diagnostico;
- registrar hallazgos relevantes;
- no ejecutar cambios derivados sin nueva aprobacion;
- si aparece riesgo mayor, reclasificar.

### Nivel B - Cambio reversible menor

Ejemplos:

- texto no legal;
- meta descriptions;
- documento interno;
- CSS acotado no estructural;
- cambio de contenido facil de revertir.

Requiere Orden corta.

```text
ORDEN DE CAMBIO
Nivel: B
Activo:
Cambio:
Rollback:
Verificacion:
Apruebas?
```

### Nivel C - Cambio funcional

Ejemplos:

- plugins;
- widgets;
- formularios;
- automatizaciones;
- usuarios;
- WooCommerce en configuracion;
- reglas de envio;
- fuentes de datos de reportes;
- campanas o anuncios sin impacto irreversible;
- scripts que escriben datos.

Requiere Orden completa.

### Nivel D - Cambio irreversible o sensible

Ejemplos:

- backups/restores;
- base de datos;
- DNS;
- `wp-config`;
- borrados;
- credenciales;
- pasarelas reales;
- presupuestos Ads;
- conversion tracking;
- cambios en fuente de verdad;
- acciones que puedan exponer datos.

Requiere aprobacion explicita paso a paso. No se ejecuta como primera respuesta a un sintoma.

## Orden de Cambio completa

Para Nivel C o D:

```text
ORDEN DE CAMBIO
Nivel: C/D

1. Problema observado:
   [evidencia]

2. Diagnostico de capa:
   [hosting/cache/CMS/plugin/ads/DNS/datos/etc.]

3. Activo critico:
   [sistema, cuenta, archivo, dato o flujo]

4. Alcance exacto:
   [que se va a tocar]

5. Exclusiones:
   [que NO se va a tocar]

6. Riesgo:
   [bajo/medio/alto y que podria degradarse]

7. Rollback o mitigacion:
   [como se revierte o contiene]

8. Verificacion posterior:
   [URLs, APIs, flujos, capturas, metricas]

9. Aprobacion:
   [esperar aprobacion explicita de Rodrigo]
```

La aprobacion aplica solo al alcance declarado.

## Diagnostico por capas

Antes de actuar sobre una capa destructiva, separar capas.

Ejemplos:

- No restaurar base de datos si no se descarto cache.
- No cambiar DNS si no se separo DNS, SSL, hosting y cache.
- No pausar campanas si no se separo creativo, presupuesto, tracking y atencion comercial.
- No borrar archivos si no se sabe si son fuente de verdad.
- No modificar Notion si contradice datos vivos sin marcar la fuente.
- No cambiar pagos/envios sin probar checkout y reglas reales.

## Regla anti-restore

Restaurar backups, base de datos o archivos es Nivel D.

Prohibido como primera respuesta a sintomas visuales, cache, layout, tracking o configuracion.

Solo se considera tras:

1. confirmar que no es cache;
2. confirmar que no es plantilla, pagina o fuente equivocada;
3. confirmar perdida real, corrupcion o fallo no reversible;
4. documentar que se perderia y que se conservaria;
5. tener aprobacion explicita paso a paso.

## Fuentes de verdad

Antes de cambiar datos que otros agentes usan, declarar fuente de verdad:

| Tipo | Fuente principal |
|---|---|
| tareas | Notion |
| perfil rapido cliente | `clients/[cliente]/context.md` |
| memoria cliente | `clients/[cliente]/memory.md` |
| historial | `log.md` |
| alertas/dependencias | `mensajes.md` |
| rendimiento real | conectores vivos/API |
| configuracion en produccion | sistema vivo |
| credenciales | `.env` local o gestor externo |
| sistema v2 | repo GitHub privado |

Si una fuente viva contradice un documento, no continuar como si nada. Marcar contradiccion y sincronizar o pedir confirmacion.

## Cuando parar

El agente debe detenerse si:

- el cambio sube de nivel;
- aparece un activo no declarado;
- el rollback no es claro;
- hay contradiccion entre datos vivos y documentos;
- la accion implica secretos, pagos, presupuestos, DNS, base de datos o restore;
- la aprobacion cubria una cosa y ahora hace falta otra;
- falta fuente de verdad;
- el usuario pide rapidez pero el riesgo es C/D.

## Log y registros

Todo cambio Nivel B/C/D debe registrar:

```text
[YYYY-MM-DD] [AGENTE] [ACTIVO CRITICO] | RESULTADO: ... | PROXIMO PASO: ...
```

Ademas:

- si toca accesos: `registries/registro-accesos.md`;
- si crea/modifica archivos: `registries/registro-artefactos.md` o manifest;
- si migra pieza legacy: `registries/registro-migracion.md`;
- si toca cliente: `clients/[cliente]/log.md`.

## Relacion con Claude Code

En el sistema v2:

- actions read-only suelen ser Nivel A;
- ediciones locales del repo pueden ser Nivel A/B segun impacto;
- cambios en scripts que luego tocaran produccion son C/D aunque el commit sea local;
- comandos, hooks y MCP pueden ser criticos si ejecutan acciones externas;
- subagents no reducen el nivel de riesgo: la accion manda, no el agente.

## Relacion con otros protocolos

Aplicar tambien:

- `protocols/gestion-accesos.md` si hay credenciales, tokens o accesos.
- `protocols/control-artefactos.md` si se crean o modifican archivos.
- `protocols/cierre-humano.md` para explicar el cierre.

## Checklist antes de tocar un activo critico

1. Identificar activo.
2. Clasificar nivel A/B/C/D.
3. Declarar fuente de verdad.
4. Definir alcance exacto.
5. Definir exclusiones.
6. Definir rollback o mitigacion.
7. Definir verificacion posterior.
8. Pedir aprobacion si B/C/D.
9. Ejecutar solo lo aprobado.
10. Registrar resultado.

## Criterio de exito

El protocolo funciona si:

- ninguna accion sensible ocurre por accidente;
- Rodrigo sabe que se va a tocar antes de tocarlo;
- los cambios tienen rollback o mitigacion;
- las fuentes de verdad no se contradicen silenciosamente;
- los logs permiten reconstruir que paso;
- la velocidad nunca supera la seguridad operativa.
