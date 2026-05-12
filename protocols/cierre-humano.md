# Protocolo de cierre humano

## Estado

- Version: 2.0
- Fecha: 2026-05-12
- Fuente legacy: `sistema/protocolos/cierre-humano.md`
- Sistema destino: E-SELEC Agent System v2
- Estado: vigente

## Objetivo

Evitar que Rodrigo termine una sesion sin entender que paso realmente.

Cada cierre debe traducir el trabajo tecnico a lenguaje humano:

- que se pidio;
- que se hizo;
- por que se hizo;
- que cambio;
- que no se toco;
- que se encontro;
- que queda pendiente;
- cual es el siguiente paso.

## Explicacion simple para Rodrigo

Este protocolo existe porque un sistema de agentes puede hacer mucho trabajo detras: leer archivos, crear reglas, tocar registros, ejecutar scripts, usar conectores o tomar decisiones tecnicas.

Si al final solo dice `listo`, Rodrigo no puede saber si el sistema avanzo bien, si dejo riesgos, si cambio algo importante o si necesita decidir algo.

La regla es: **si hubo trabajo detras, el cierre debe explicar la historia completa en menos de un minuto**.

## Cuando se activa

Se activa siempre que ocurra una de estas cosas:

- se crean o modifican archivos;
- se toca una web, cliente, campana, acceso, output, protocolo, agente, skill, command o hook;
- se ejecuta un script;
- se usa una API, MCP, credencial o conector;
- se detecta una alerta, bloqueo, dependencia o pendiente;
- se sube un commit;
- se actualiza un registro;
- el trabajo duro mas de unos minutos;
- Rodrigo podria no haber visto lo que paso detras.

Si la tarea fue pequena, usar cierre corto.

Si hubo cambios, accesos, produccion, outputs, registros, commits o riesgo, usar cierre normal.

## Cierre normal

Usar esta estructura cuando haya trabajo real detras:

```text
Rodrigo, esto fue lo que paso:

1. Me pediste:
[Una frase clara.]

2. Hice:
[Acciones reales, sin humo.]

3. Cambio:
[Archivos, sistemas, reglas, commits o decisiones tocadas.]

4. No toque:
[Zonas sensibles que quedaron intactas.]

5. Encontre:
[Alertas, bloqueos, riesgos, contradicciones o nada relevante.]

6. Estado:
[Listo / pendiente / bloqueado / necesita decision.]

7. Siguiente paso:
[Una accion concreta.]
```

No hace falta copiar la plantilla literal si una version natural comunica mejor lo mismo.

## Cierre corto

Para tareas pequenas:

```text
Rodrigo, resumen rapido:
Hice [accion].
Cambio [cosa].
No toque [zona sensible].
Estado: [listo / pendiente / bloqueado].
Siguiente paso: [accion].
```

## Checklist de cierre para migracion v2

Cuando la tarea sea de migracion del sistema, incluir tambien:

- item de backlog completado;
- item de backlog siguiente;
- commit subido, si existe;
- archivos principales creados o modificados;
- estado de `El Escolta` si se ejecuto;
- riesgos o bloqueos pendientes.

Ejemplo:

```text
Checklist:
- Hecho: P0-004 control de artefactos.
- Hecho: P0-005 activos criticos.
- En curso: P0-006 cierre humano.
- Pendiente: P0-007 hook anti-secretos.
```

## Tono obligatorio

El cierre debe sonar como una persona competente poniendo a Rodrigo al dia.

Usar un tono:

- claro;
- directo;
- humano;
- breve cuando sea posible;
- honesto con pendientes y riesgos.

Evitar:

- jerga innecesaria;
- lenguaje corporativo;
- frases genericas como `todo esta listo` si hay pendientes;
- listas de rutas sin explicar que significan;
- exagerar el trabajo;
- esconder bloqueos;
- cerrar con solo `listo`.

## Relacion con Claude Code

Claude Code favorece instrucciones persistentes pequenas, contexto limpio y ejecucion verificable. Este protocolo traduce eso al cierre:

- no repetir todo el razonamiento interno;
- si hubo cambios, nombrar archivos importantes;
- si hubo pruebas, decir cuales pasaron o cuales no se pudieron ejecutar;
- si hubo commits, indicar hash corto;
- si hubo riesgos, decirlos claramente;
- si el siguiente paso ya esta definido, dejarlo listo.

## Relacion con El Escolta

El Escolta no protagoniza el cierre. Solo se menciona cuando reviso o bloqueo algo.

Si esta limpio:

```text
Revision de cierre: El Escolta quedo limpio.
```

Si bloquea:

```text
Estado: bloqueado.
Motivo: El Escolta detecto [problema concreto].
```

No ocultar un bloqueo de El Escolta aunque el resto de la tarea haya salido bien.

## Relacion con otros protocolos

Aplicar tambien:

- `protocols/control-artefactos.md` si se crearon o modificaron archivos.
- `protocols/gestion-accesos.md` si hubo secretos, credenciales, tokens, OAuth, MCP o conectores.
- `protocols/activos-criticos.md` si se toco o se pudo tocar produccion, datos vivos o fuentes de verdad.

## Que no hacer

No cerrar asi:

```text
Listo.
```

No cerrar asi:

```text
Cambios:
- archivo1
- archivo2
- archivo3
```

sin explicar que significan.

No decir que algo esta completado si:

- no se pudo verificar;
- queda un script fallando;
- falta subir commit;
- falta registrar artefactos;
- falta decision de Rodrigo;
- El Escolta bloqueo el cierre.

## Criterio de exito

El cierre esta bien si Rodrigo puede leerlo rapido y entender:

- que pidio;
- que paso;
- que cambio;
- que quedo intacto;
- si hay riesgo;
- si esta terminado;
- que sigue.

