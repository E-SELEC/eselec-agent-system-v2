# Folder Cleanup Patterns

## Senales de duplicado

- Mismo tema con sufijos v1, v2, final, final-final.
- Mismo periodo de datos en varios archivos.
- Un archivo contiene por completo a otro.
- JSON raw anterior superado por version mas completa.

## Senales de obsolescencia

- Log confirma que una decision cambio.
- Fecha antigua y output reemplazado por uno posterior.
- Archivo contradice context actual.
- Documento dice "borrador" pero existe version aprobada.

## Acciones

| Accion | Cuando |
|---|---|
| conservar | vigente o fuente historica |
| renombrar | nombre generico o dificil de entender |
| mover | archivo correcto en carpeta incorrecta |
| archivar | obsoleto pero puede necesitarse |
| eliminar | duplicado inequívoco y aprobado |
| revisar | duda, contradiccion o riesgo |

## Nombres

- kebab-case;
- fecha ISO si aplica;
- describir contenido, no herramienta;
- evitar "final" como estado permanente.

## Estructura sugerida outputs

- `auditorias/`
- `reportes/`
- `estrategia/`
- `templates/`
- `datos/`
- `archivo/`
