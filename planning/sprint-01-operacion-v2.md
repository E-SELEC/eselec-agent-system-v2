# Sprint 01 - Arranque operativo v2

Fecha: 2026-05-13
Responsable: Codex + Arquitecto
Estado: completado

## Objetivo

Pasar de "sistema migrado" a "sistema usado con criterio".

Este sprint no migra mas piezas legacy. Prueba el sistema v2 en condiciones reales, con bajo riesgo, trazabilidad y cierre limpio.

## Principio

La primera semana de uso debe demostrar tres cosas:

1. El routing por lideres funciona.
2. Los outputs salen con criterio y no solo con formato.
3. Los protocolos no bloquean el trabajo, sino que evitan errores.

## Orden recomendado

| ID | Estado | Accion | Resultado esperado |
|---|---|---|---|
| O1-001 | hecho | Primer arranque Cliente con `computer-chamberi` | Diagnostico breve de estado usando `leader-clientes`, sin tocar produccion. |
| O1-002 | hecho | Primer arranque Agencia | Prioridad interna clara usando `leader-agencia`, sin mezclar clientes. |
| O1-003 | hecho | Ejecutar `LOOP: auditoria-semanal` en modo lectura | Resumen multi-cliente sin cambios reales. |
| O1-004 | hecho | Probar Calibracion con una correccion real o simulada | Decidir si guarda, descarta o deriva a Docente. |
| O1-005 | hecho | Elegir primer conector a reconstruir de forma segura | Especificacion, no implementacion productiva. |

## O1-001 - Primer arranque Cliente

Cliente recomendado: `computer-chamberi`.

Motivo: ya fue cliente piloto y tiene contexto migrado.

Lectura obligatoria:

- `clients/computer-chamberi/context.md`
- `clients/computer-chamberi/log.md`
- `clients/computer-chamberi/memory.md`
- `clients/computer-chamberi/mensajes.md`
- `quality/criterios-output.md`

Salida esperada:

```text
EQUIPO: Clientes
CLIENTE: computer-chamberi
NIVEL DE DATOS:
PRIORIDAD:
DIAGNOSTICO:
SIGUIENTE ACCION SEGURA:
NO TOCAR:
```

Bloqueo: no modificar web, WordPress, GBP, Ads ni datos reales.

## O1-002 - Primer arranque Agencia

Lectura obligatoria:

- `agency/context.md`
- `agency/brand.md`
- `agency/log.md`
- `agency/mensajes.md`
- `agency/preferencias-rodrigo.md`

Salida esperada:

```text
EQUIPO: Agencia Interna
NIVEL DE DATOS:
PRIORIDAD:
OPORTUNIDAD:
RIESGO:
SIGUIENTE ACCION:
```

## Resultado O1-002 - Primer arranque Agencia

Archivo local generado: `agency/outputs/arranque-agencia-v2-2026-05-13.md`.

Resultado:

- Equipo correcto: Agencia Interna.
- Produccion tocada: no.
- Prioridad: IMPORTANTE.
- Hallazgo principal: `agency/context.md` sigue expresando prioridades de migracion ya cerradas, por lo que debe actualizarse antes de usar Agencia para decisiones internas mas amplias.
- Siguiente accion segura: actualizar contexto interno y continuar con O1-003 en modo lectura.

## O1-003 - Loop semanal en lectura

Ejecutar el loop como auditoria de estado, no como generador masivo.

Resultado esperado:

- detectar clientes sin log reciente;
- detectar mensajes pendientes;
- no crear entregables para cliente;
- si se crea output interno, registrarlo.

## Resultado O1-003 - Loop semanal en lectura

Archivo local generado: `agency/outputs/resumen-semanal-2026-05-13.md`.

Resultado:

- Clientes evaluables en v2: 1 (`computer-chamberi`).
- Estado Computer Chamberi: activo, ultimo log 2026-05-13.
- Mensajes pendientes Computer Chamberi: 5.
- Alertas/dependencias Agencia: 3.
- Clientes activos legacy fuera de alcance v2: 3.
- Produccion tocada: no.
- Siguiente accion segura: ejecutar O1-004 Calibracion antes de migrar mas clientes o automatizar loops.

## O1-004 - Calibracion

Probar que el sistema no guarda todo por reflejo.

Criterio:

- Si Rodrigo corrige algo reutilizable, proponer guardarlo.
- Si es un ajuste puntual, declararlo como ruido.
- Si afecta criterio de agentes, derivar a `docente`.

## Resultado O1-004 - Calibracion

Archivo local generado: `agency/outputs/calibracion-o1-004-2026-05-13.md`.

Resultado:

- Checklist visible: duplicado ya existente en `agency/preferencias-rodrigo.md`; no se guarda de nuevo.
- Reanudar exactamente donde se quedo: preferencia nueva propuesta, no escrita sin aprobacion.
- Memoria permanente modificada: no.
- Produccion tocada: no.
- Siguiente accion segura: O1-005 primer conector seguro.

## O1-005 - Primer conector seguro

No reconstruir todos.

Elegir uno segun impacto y riesgo:

| Candidato | Valor | Riesgo | Recomendacion |
|---|---|---|---|
| GSC/GA4 lectura | alto | medio | buen primer conector si las credenciales estan ordenadas. |
| Notion sync local | medio | bajo-medio | solo si MCP no cubre el flujo. |
| Meta Ads lectura | alto | alto | esperar hasta definir acceso seguro. |
| WordPress/Woo | alto | alto | no empezar aqui. |

## Resultado O1-005 - Primer conector seguro

Archivo creado: `planning/conector-seguro-01-gsc-lectura.md`.

Resultado:

- Primer conector elegido: GSC solo lectura.
- Implementacion productiva: no realizada.
- Accesos usados: ninguno.
- Produccion tocada: no.
- Riesgo API previsto: Nivel A si se limita a lectura.
- Riesgo de token futuro: S4 por OAuth/refresh token, aunque el scope sea read-only.
- Motivo: desbloquea la verificacion SEO de Computer Chamberi con menos riesgo que WordPress, WooCommerce, Meta Ads, SEMrush automatizado o GA4 inicial.

## Criterio de cierre del sprint

- Al menos una tarea real entra por `leader-clientes`.
- Al menos una tarea interna entra por `leader-agencia`.
- Se ejecuta guard antes de cerrar.
- No se toca produccion.
- Se detecta si el sistema resulta claro para Rodrigo o si necesita ajuste de cierre/tono.

## Resultado buscado

Que Rodrigo pueda decir:

```text
Ya no estamos migrando. Ahora el sistema trabaja ordenado.
```

## Cierre Sprint 01

Estado final: completado.

Tareas ejecutadas:

- O1-001: primer arranque Cliente con `computer-chamberi`.
- O1-002: primer arranque Agencia.
- Ajuste derivado: `agency/context.md` actualizado a fase operativa.
- O1-003: `LOOP: auditoria-semanal` probado en modo lectura.
- O1-004: Calibracion probada sin escribir memoria permanente.
- O1-005: primer conector seguro elegido y especificado: GSC solo lectura.

Produccion tocada: no.

Accesos usados: ninguno.

Outputs locales ignorados por Git:

- `clients/computer-chamberi/outputs/auditoria-arranque-v2-2026-05-13.md`
- `agency/outputs/arranque-agencia-v2-2026-05-13.md`
- `agency/outputs/resumen-semanal-2026-05-13.md`
- `agency/outputs/calibracion-o1-004-2026-05-13.md`

Siguiente fase recomendada:

1. Decidir si Rodrigo aprueba guardar la preferencia de reanudacion exacta propuesta por Calibracion.
2. Implementar `gsc-readonly` solo si se aprueba preparar OAuth fuera del repo.
3. Usar GSC para subir Computer Chamberi a medicion verificada antes de auditoria SEO final.
