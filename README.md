# E-SELEC Agent System v2

Sistema operativo de agentes, protocolos, skills y memoria de E-SELEC.

Este repositorio es la nueva base limpia del sistema. El sistema anterior queda como fuente historica y no se migra en bloque. Cada pieza debe pasar un filtro antes de entrar aqui.

## Principios

- Cloud-first, no cloud-only: GitHub versiona el sistema; la ejecucion puede ser local o controlada.
- Sin secretos en repo: nada de tokens, passwords, application passwords, claves API, OAuth ni `.env`.
- Modular: reglas, skills, agentes, protocolos, memoria y scripts viven separados.
- Trazable: todo cambio operativo importante deja registro.
- Migracion selectiva: solo entra lo que tenga utilidad viva.

## Capas del sistema

1. `core/` - identidad, prioridades y fuentes de verdad.
2. `.claude/` - configuracion, reglas, skills, hooks y agentes nativos.
3. `teams/` - equipos operativos: clientes, agencia, arquitecto, docente y fenix.
4. `clients/` - memoria y trabajo por cliente.
5. `agency/` - memoria y trabajo interno de E-SELEC.
6. `protocols/` - protocolos obligatorios.
7. `registries/` - trazabilidad de artefactos, accesos y decisiones.
8. `scripts/` - herramientas locales revisadas y sin secretos.
9. `legacy/` - notas de migracion desde el sistema anterior, no vertedero.

## Filtro de migracion

Antes de mover una pieza desde el sistema anterior, responder:

- Es una regla viva?
- Ensena criterio reutilizable?
- Ejecuta una tarea necesaria?
- Conserva memoria de cliente?
- Es obligatorio por seguridad, trazabilidad o cierre?
- Esta libre de secretos?
- Tiene propietario y proposito claro?

Si la respuesta no es clara, no se migra todavia.

