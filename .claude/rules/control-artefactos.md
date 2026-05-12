# Regla de control de artefactos

Aplica cuando una tarea crea, modifica, mueve, archiva o elimina archivos/carpetas.

## Regla central

Si se toca un artefacto importante, debe quedar trazado.

## Antes de crear archivos

Si se van a crear mas de 3 archivos:

1. explica por que hacen falta;
2. manten la estructura minima;
3. registra el resultado.

## Durante la tarea

- No crear archivos por si acaso.
- No duplicar versiones sin marcar reemplazo.
- No subir outputs pesados o privados al repo.
- No mezclar historico con contexto activo.
- No guardar secretos en artefactos.

## Al cerrar

Indica:

- archivos creados;
- archivos modificados;
- obsoletos detectados;
- temporales pendientes;
- registros actualizados.

## Registros

- Sistema: `registries/registro-artefactos.md`
- Cliente: `clients/[cliente]/outputs/manifest.md`
- Agencia: `agency/outputs/manifest.md`

Fuente: `protocols/control-artefactos.md`
