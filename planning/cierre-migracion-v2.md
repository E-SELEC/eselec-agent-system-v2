# Cierre de migracion E-SELEC v2

Fecha: 2026-05-13
Responsable: Codex + Arquitecto
Estado: cerrado

## Resultado

La migracion base del sistema E-SELEC v2 queda cerrada.

El backlog de migracion tiene 24 items y todos estan en estado `hecho`.

## Que quedo migrado

| Bloque | Estado | Resultado |
|---|---|---|
| P0 Seguridad y base | hecho | Protocolos, reglas y hook defensivo listos. |
| P1 Calidad y criterio | hecho | Diagnostico de calidad, contratos de output, Docente, auditorias piloto e ingesta/verificacion. |
| P2 Operacion | hecho | Lideres Cliente/Agencia, commands recurrentes y cliente piloto. |
| P3 Migracion amplia | hecho | Agencia, cliente piloto, skills, agentes y saneamiento inicial de scripts/conectores. |

## Numeros de cierre

- Items de backlog: 24/24 hechos.
- Skills legacy migradas: 40/40.
- Skills extra creadas para v2: 3 (`migration-audit`, `ingesta-evidencia`, `verificacion-medicion`).
- Roles legacy migrados como subagents: 42.
- Agentes v2 totales: 47.
- Conectores productivos legacy copiados sin sanear: 0.

## Como arrancar el sistema

1. Abrir el repo v2:

```bash
cd "C:\Users\rondr\OneDrive\Desktop\E-SELEC - copia\eselec-agent-system-v2"
```

2. Revisar estado:

```bash
git status --short
python scripts/protocol_guard.py --no-report
```

3. Elegir modo:

| Necesidad | Ruta |
|---|---|
| Trabajar cliente | `.claude/agents/leader-clientes.md` |
| Trabajar E-SELEC como negocio | `.claude/agents/leader-agencia.md` |
| Auditar una pieza legacy nueva | `.claude/agents/arquitecto-migracion-claude.md` |
| Corregir criterio tras fallo de calidad | `.claude/agents/docente.md` |
| Calibrar preferencia de Rodrigo | `.claude/agents/calibracion.md` |
| Sanar estructura interna | `.claude/agents/fenix.md` |
| Revisar patron de sistema | `.claude/agents/arquitecto.md` |

4. Antes de cerrar cualquier cambio:

```bash
python scripts/protocol_guard.py
git diff --check
```

## Reglas que no se deben romper

- No copiar carpetas legacy completas.
- No migrar conectores con accesos reales sin saneamiento.
- No guardar secretos en repo.
- No tocar produccion sin Orden de Cambio.
- No generar entregables sin leer contexto, log, memoria y criterios de output.
- No cerrar tareas con archivos modificados sin registro y guard.

## Que queda conscientemente fuera

Los siguientes conectores/scripts no estan activos en v2. No es olvido; es una decision de seguridad.

| Grupo | Estado |
|---|---|
| WordPress/WooCommerce legacy con credenciales historicas | bloqueado |
| GA4, GSC, GBP, Drive OAuth | deferido |
| Meta Ads y renovacion de token | deferido |
| Hostinger y WP REST | deferido |
| Kling | deferido |
| Scrapers publicos | deferido hasta limites y manifests |
| Generadores PDF/reportes legacy | deferido hasta contrato estable de informes |

Para activar cualquiera de ellos, crear una version v2 con:

- variables locales o gestor seguro;
- dry-run por defecto;
- parametros no interactivos;
- logs sin valores sensibles;
- registro en `registries/registro-accesos.md` si aplica;
- Orden de Cambio si toca produccion;
- prueba minima sin credenciales reales.

## Checklist de primer uso

- [ ] Confirmar que Rodrigo trabaja dentro del repo v2, no en legacy.
- [ ] Ejecutar `git pull` antes de empezar.
- [ ] Ejecutar `python scripts/protocol_guard.py --no-report`.
- [ ] Elegir lider correcto: cliente o agencia.
- [ ] Leer contexto/log/mensajes/memory antes de trabajar clientes.
- [ ] Registrar outputs o artefactos.
- [ ] Ejecutar guard antes de cerrar.
- [ ] Hacer commit/push si hubo cambios versionables.

## Criterio de exito

El sistema v2 esta listo si una tarea nueva puede entrar por un lider, leer su contexto, elegir una skill o subagent, producir una salida con contrato de calidad, registrar lo hecho y cerrar con guard limpio.

Ese estado ya se cumple para la base migrada.
