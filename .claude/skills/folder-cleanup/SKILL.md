---
name: folder-cleanup
description: >
  Audita y reorganiza carpetas de clientes, outputs, duplicados, versiones
  obsoletas, archivos mal ubicados, canibalizacion documental, tasks, mensajes,
  logs y manifests. Usalo cuando se pida organizar carpeta, limpiar outputs,
  detectar duplicados, archivar documentos o ordenar archivos de cliente.
---

# Folder Cleanup - E-SELEC

## Proposito

Ordenar carpetas de cliente sin perder trazabilidad ni borrar conocimiento util.

Esta skill primero diagnostica y propone. No mueve, elimina ni archiva archivos sin confirmacion explicita.

## Fuentes obligatorias

Lee `clients/[cliente]/context.md`, `clients/[cliente]/log.md`, `clients/[cliente]/mensajes.md`, `clients/[cliente]/tasks.md` si existen, `clients/[cliente]/outputs/manifest.md` si existe, `protocols/control-artefactos.md`, `protocols/activos-criticos.md` y `quality/criterios-output.md`.

Necesitas cliente, alcance, carpeta objetivo, criterio de conservacion y permiso antes de ejecutar cambios.

## Niveles

- FCU3 - listo: diagnostico, propuesta, mapa de acciones, aprobacion y registro definidos.
- FCU2 - fuerte: diagnostico y propuesta listos, falta aprobacion.
- FCU1 - orientativo: inventario parcial.
- FCU0 - bloqueado: falta cliente, carpeta o permiso.

## Workflow

1. Leer contexto, log, mensajes, tasks y manifest.
2. Inventariar archivos sin mover nada.
3. Detectar duplicados, versiones superadas, archivos sueltos, nombres genericos y contradicciones.
4. Clasificar cada accion: conservar, renombrar, mover, archivar, eliminar o revisar.
5. Presentar propuesta con riesgos y esperar aprobacion.
6. Si se aprueba, ejecutar solo las acciones aprobadas y registrar artefactos.
7. Entregar informe usando `templates/folder-cleanup-report.md`.

## Reglas

- Nunca borrar si hay duda. Archivar es preferible a eliminar.
- No modificar `context.md`, `tasks.md`, `mensajes.md` o `log.md` si hay contradiccion sin resolver.
- No usar comandos destructivos recursivos.
- Antes de mover/eliminar, verificar rutas absolutas dentro del cliente.
- Registrar cambios en manifest o registro de artefactos.

## Bloqueos

- falta cliente o carpeta;
- hay contradiccion entre fuentes;
- el usuario no aprobo acciones de mover/eliminar;
- la ruta objetivo queda fuera del workspace o cliente;
- hay mas de cinco candidatos a eliminacion sin certeza total.

## Referencias

- `references/folder-cleanup-patterns.md`: criterios de clasificacion.
- `templates/folder-cleanup-report.md`: formato de salida.
- `checklists/revision.md`: revision final.
