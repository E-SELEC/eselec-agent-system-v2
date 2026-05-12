# Sprint 00 - Seguridad y protocolos

## Decision

Empezamos por seguridad/protocolos.

## Por que esta decision

Rodrigo detecto un problema real: a veces los outputs no tienen la calidad, criterio o acierto esperados aunque el sistema ya tenga mucho trabajo previo.

La causa probable no es una sola. Puede venir de contexto excesivo, instrucciones mezcladas, duplicidades, falta de pruebas, agentes mal ubicados o procedimientos que no estan donde Claude Code espera encontrarlos.

Aun asi, antes de mejorar outputs SEO/informes hay que blindar la base. Si migramos calidad antes de seguridad, podriamos copiar al v2 scripts sensibles, secretos historicos, protocolos duplicados o permisos mal definidos.

## Objetivo del sprint

Dejar el sistema v2 preparado para migrar piezas legacy sin:

- subir secretos;
- tocar produccion por accidente;
- crear artefactos sin registro;
- mezclar historico con instrucciones vivas;
- perder trazabilidad.

## Alcance

Este sprint cubre P0:

| ID | Accion | Resultado |
|---|---|---|
| P0-001 | Inventario legacy inicial | `planning/inventario-legacy.md` |
| P0-002 | Auditoria scripts con secretos historicos | lista saneamiento sin valores |
| P0-003 | Migrar gestion-secretos | `protocols/gestion-secretos.md` |
| P0-004 | Migrar control-artefactos | `protocols/control-artefactos.md` |
| P0-005 | Migrar activos-criticos | `protocols/activos-criticos.md` |
| P0-006 | Migrar cierre-humano | `protocols/cierre-humano.md` |
| P0-007 | Disenar hook bloqueo secretos | especificacion y primer hook |

## Fuera de alcance

- Migrar clientes completos.
- Migrar todos los agentes.
- Migrar todas las skills.
- Sanear credenciales reales directamente.
- Tocar WordPress, WooCommerce, Ads, GBP, GA4, GSC o produccion.
- Subir outputs privados de clientes.

## Orden de ejecucion

1. Crear `planning/inventario-legacy.md`.
2. Clasificar cada carpeta legacy por responsabilidad.
3. Detectar piezas sensibles y scripts bloqueados.
4. Migrar `gestion-secretos`.
5. Migrar `control-artefactos`.
6. Migrar `activos-criticos`.
7. Migrar `cierre-humano`.
8. Disenar hooks minimos.
9. Ejecutar prueba de cierre.
10. Abrir P1 calidad/criterio.

## Criterios de salida

El sprint se considera terminado cuando:

- Existe inventario legacy inicial.
- Hay lista de scripts sensibles sin valores secretos.
- Los cuatro protocolos base existen en v2.
- El backlog P0 queda marcado como hecho o bloqueado con motivo.
- El registro de migracion esta actualizado.
- El guard de cierre no detecta secretos ni artefactos sueltos.

## Riesgos

| Riesgo | Mitigacion |
|---|---|
| Copiar secretos por accidente | escaneo antes de commit y `.gitignore` estricto |
| Migrar material obsoleto | usar `migration-audit` antes de mover |
| Duplicar protocolos | elegir fuente canonica antes de escribir |
| Quedarse solo en seguridad | abrir P1 inmediatamente al cerrar P0 |
| Hacerlo demasiado tecnico para Rodrigo | cada cierre debe explicar que se hizo y por que |

## Siguiente accion concreta

Ejecutar P0-001:

```text
Crear planning/inventario-legacy.md
```

Ese inventario no debe contener secretos ni copiar archivos completos. Debe mapear responsabilidades y destinos Claude Code probables.
