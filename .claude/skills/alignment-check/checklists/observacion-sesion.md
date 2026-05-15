# Checklist de observacion de sesion

Usar cuando Rodrigo pregunte por calidad, criterio, acierto, resultados flojos, confusion de agentes o mala ejecucion reciente.

## Regla previa

Antes de juzgar una sesion, identifica que tipo de trabajo era:

- cliente;
- agencia;
- sistema;
- produccion/accesos;
- investigacion;
- entregable.

Lee la fuente oficial local que corresponda al mecanismo usado: agents, skills, commands, hooks, MCP, settings o contexto.

## Preguntas de observacion

- [ ] Se eligio el modo correcto: cliente, agencia o sistema?
- [ ] Se leyo la memoria/contexto local correcto antes de actuar?
- [ ] Se uso agente cuando hacia falta contexto propio?
- [ ] Se uso skill cuando hacia falta procedimiento?
- [ ] Se cargo la skill correcta?
- [ ] Se ejecuto una accion sin fuente oficial o sin evidencia?
- [ ] Se mezclaron cliente y agencia?
- [ ] Se tocaron archivos sin registro?
- [ ] Se omitio `protocol_guard.py` despues de cambios?
- [ ] Se pidio aprobacion antes de produccion, accesos o datos vivos?
- [ ] El output siguio `quality/criterios-output.md` cuando aplicaba?
- [ ] Rodrigo corrigio algo que debe convertirse en preferencia, regla o ajuste de skill?

## Senales de baja calidad

Marcar como alerta si aparece alguna:

- recomendaciones genericas sin datos;
- salida sin fuente ni evidencia;
- output que ignora `context.md`, `memory.md` o `log.md`;
- agente que opina sin leer la skill;
- agente que recomienda cambios fuertes sin leer docs oficiales locales;
- repetir una accion ya registrada en log;
- usar un reporte viejo como verdad;
- no distinguir hecho, inferencia y recomendacion;
- cerrar con "listo" sin decir que se hizo y que no se toco.

## Salida

```text
OBSERVACION DE SESION

MODO DETECTADO:

FUENTES LEIDAS:

QUE FUNCIONO:

QUE FALLO:

CAUSA PROBABLE:

AJUSTE RECOMENDADO:

TIPO DE AJUSTE:
rule | skill | agent | command | settings | hook | memoria | proceso humano

RIESGO:
bajo | medio | alto
```
