# Protocolo de control de artefactos

## Estado

- Version: 2.0
- Fecha: 2026-05-12
- Fuente legacy: `sistema/protocolos/control-artefactos.md`
- Sistema destino: E-SELEC Agent System v2
- Estado: vigente

## Objetivo

Evitar que el sistema cree, modifique, mueva, archive o deje archivos sin trazabilidad.

Este protocolo responde:

- que archivo existe;
- por que existe;
- donde debe vivir;
- si esta vigente;
- que reemplaza;
- que riesgo tiene;
- si debe subirse al repo o quedarse fuera.

## Explicacion simple para Rodrigo

Un artefacto es cualquier archivo o carpeta que el sistema toca: un protocolo, un script, un output, un informe, un prompt, una skill, un registro, una captura, un JSON, un manifest o una carpeta nueva.

El problema que evita este protocolo es que aparezcan archivos que luego nadie sabe si son buenos, viejos, borradores, temporales o peligrosos.

La regla es: **si se crea o modifica algo importante, debe quedar registrado**.

## Definicion de artefacto

Artefacto es cualquier archivo, carpeta o entregable creado, modificado, movido, archivado o marcado como obsoleto por un agente.

Incluye:

- `CLAUDE.md`;
- `AGENTS.md`;
- `.claude/agents/`;
- `.claude/skills/`;
- `.claude/rules/`;
- `.claude/commands/`;
- `.claude/hooks/`;
- `protocols/`;
- `registries/`;
- `planning/`;
- `scripts/`;
- `clients/`;
- `agency/`;
- outputs de clientes;
- informes;
- auditorias;
- capturas;
- JSON;
- manifests;
- documentos internos;
- carpetas experimentales.

## Registros

### Registro global

Ruta:

```text
registries/registro-artefactos.md
```

Usar para:

- cambios de arquitectura;
- protocolos;
- scripts;
- reglas Claude;
- subagents;
- skills;
- commands;
- hooks;
- documentos de planificacion;
- cambios transversales;
- outputs con impacto sensible.

### Manifest por cliente

Ruta:

```text
clients/[cliente]/outputs/manifest.md
```

Usar para:

- entregables del cliente;
- auditorias del cliente;
- informes;
- scrapes;
- assets;
- outputs tecnicos asociados al cliente.

### Manifest de agencia

Ruta:

```text
agency/outputs/manifest.md
```

Usar para:

- propuestas internas;
- captacion;
- documentos de estrategia;
- auditorias internas;
- outputs de agencia.

## Campos obligatorios

Cada entrada debe incluir:

```text
### YYYY-MM-DD - ruta
- Area:
- Agente:
- Tipo:
- Motivo:
- Estado:
- Reemplaza a:
- Accion recomendada:
- Riesgo:
```

Estados permitidos:

- `borrador`
- `vigente`
- `aprobado`
- `obsoleto`
- `archivado`
- `temporal`
- `bloqueado`

No inventar estados nuevos sin actualizar este protocolo.

## Donde debe vivir cada cosa

| Artefacto | Destino |
|---|---|
| instrucciones siempre activas | `CLAUDE.md`, `AGENTS.md` |
| reglas contextuales | `.claude/rules/` |
| procedimientos reutilizables | `.claude/skills/<skill>/SKILL.md` |
| trabajadores especializados | `.claude/agents/` |
| comandos repetibles | `.claude/commands/` |
| hooks | `.claude/hooks/` |
| protocolos humanos/operativos | `protocols/` |
| trazabilidad | `registries/` |
| planes e inventarios | `planning/` |
| scripts saneados | `scripts/` |
| memoria de cliente | `clients/[cliente]/` |
| outputs de cliente | `clients/[cliente]/outputs/` o Drive |
| outputs internos agencia | `agency/outputs/` o Drive |
| historico no activo | `legacy/` |

## Reglas de creacion

Antes de crear mas de 3 archivos en una misma tarea:

1. explicar que archivos se planean crear;
2. explicar por que no basta con menos;
3. crear un registro claro al cierre.

Si la tarea ya aprobada exige mas de 3 archivos, se puede continuar, pero el cierre debe listar los archivos principales y el registro debe quedar actualizado.

Antes de crear una carpeta nueva:

1. definir proposito;
2. definir que puede contener;
3. definir cuando se considera terminada;
4. registrarla si sera parte viva del sistema.

## Reglas anti-ruido

No crear archivos con nombres como:

- `final-final`;
- `nuevo`;
- `test` fuera de carpeta temporal clara;
- `v2` sin motivo;
- `copia`;
- `backup` sin fecha;
- `definitivo`.

Usar nombres claros:

```text
tipo-tema-fecha.md
```

Ejemplos:

- `auditoria-scripts-sensibles.md`
- `sprint-00-seguridad-protocolos.md`
- `control-artefactos.md`
- `plan-maestro-migracion.md`

## Politica de repo

No todo artefacto debe subirse a GitHub.

### Si se sube al repo

Debe ser:

- sistema;
- protocolo;
- regla;
- skill;
- subagent;
- command;
- script saneado;
- plantilla;
- registro;
- plan;
- documentacion sin datos privados.

### Si no se sube al repo

Debe quedarse fuera o en Drive/local:

- `.env`;
- secretos;
- credentials;
- token files;
- PDFs finales de cliente;
- DOCX/XLSX/PPTX pesados;
- capturas sensibles;
- exports brutos;
- outputs privados;
- zips;
- binarios;
- backups operativos.

Si un output pesado necesita referencia, crear resumen o manifest, no subir el archivo completo.

## Prohibiciones

Nunca:

- crear archivos por si acaso;
- duplicar outputs sin marcar el anterior como obsoleto;
- mezclar pruebas tecnicas con entregables finales;
- guardar secretos en outputs, logs, manifests o registros;
- cerrar una tarea con cambios sin decir que archivos se tocaron;
- migrar carpetas completas sin inventario;
- dejar outputs de cliente sin manifest;
- meter historico pesado en contexto activo.

## Cierre obligatorio

Toda tarea con cambios debe cerrar con:

```text
Archivos creados:
- ruta - motivo - estado

Archivos modificados:
- ruta - motivo - estado

Archivos obsoletos detectados:
- ruta - reemplazo o accion recomendada

Archivos temporales pendientes:
- ruta - conservar / revisar / eliminar
```

Si no se creo ni modifico nada:

```text
No se crearon ni modificaron archivos.
```

## Relacion con otros protocolos

Aplicar tambien:

- `protocols/gestion-accesos.md` si el artefacto toca secretos, credenciales o accesos.
- `protocols/activos-criticos.md` si puede afectar produccion, datos, Ads, webs, integraciones o fuentes de verdad.
- `protocols/cierre-humano.md` para explicar el cierre en lenguaje simple.

## Checklist antes de commit

Antes de commitear:

1. `git status` revisado.
2. Artefactos relevantes registrados.
3. Outputs pesados no incluidos.
4. Secretos no incluidos.
5. `git diff --check` sin problemas relevantes.
6. Backlog actualizado si aplica.
7. Registro de migracion actualizado si aplica.

## Criterio de exito

El protocolo funciona si Rodrigo puede abrir registros/manifests y entender:

- que se creo;
- por que se creo;
- que esta vigente;
- que se reemplazo;
- que queda pendiente;
- que no debe tocarse;
- que puede archivarse o eliminarse.
