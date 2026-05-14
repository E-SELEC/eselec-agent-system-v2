# Protocolo de gestion de conocimiento

## Estado

- Version: 1.0
- Fecha: 2026-05-14
- Sistema: E-SELEC Agent System v2
- Estado: vigente

## Objetivo

Evitar que el sistema se vuelva desordenado cuando entra informacion nueva.

Este protocolo decide:

- donde guardar una fuente;
- cuando resumir y cuando descartar;
- cuando convertir informacion en protocolo, skill, agente, command, memoria o evidencia;
- que registrar;
- que no debe entrar al repo.

## Regla central

La informacion nueva no entra directo a cualquier carpeta.

Debe pasar por este flujo:

```text
recibir -> clasificar -> sanear -> decidir destino -> registrar -> validar
```

## Clasificacion

| Tipo | Pregunta | Destino |
|---|---|---|
| Fuente oficial | Es documentacion externa fiable? | `knowledge/[fuente]/` + `registries/registro-fuentes.md` |
| Regla viva | Obliga a cambiar comportamiento? | `protocols/` o `.claude/rules/` |
| Procedimiento | Ensena como ejecutar algo repetible? | `.claude/skills/` |
| Rol | Define quien decide o enruta? | `.claude/agents/` |
| Comando | Se invoca repetidamente por Rodrigo? | `.claude/commands/` |
| Evidencia | Soporta una decision de cliente? | `clients/[cliente]/outputs/evidencia-*.md` |
| Memoria | Cambia criterio futuro de un cliente? | `clients/[cliente]/memory.md` |
| Preferencia | Cambia como trabajar con Rodrigo? | `agency/preferencias-rodrigo.md` previa aprobacion |
| Historico | Tiene valor de archivo, no operativo | `legacy/` |
| Ruido | No cambia decisiones ni aporta fuente | descartar |

## Niveles de entrada

- K3: fuente oficial o dato vivo verificado.
- K2: export o documento reciente saneado.
- K1: nota, captura, output viejo o recuerdo util pero parcial.
- K0: no entra; contiene secretos, PII, fuente dudosa, duplicado inutil o ruido.

## Reglas

1. No guardar secretos, tokens, cookies, claves, passwords ni sesiones.
2. No guardar documentacion completa si una URL y resumen bastan.
3. No crear carpetas nuevas si existe un destino claro.
4. No mezclar memoria de cliente con reglas globales.
5. No convertir una nota puntual en regla permanente sin evidencia.
6. No sobreescribir una fuente de verdad sin declarar reemplazo.
7. Si una fuente contradice un archivo vivo, marcar contradiccion y pedir decision.
8. Si una fuente afecta produccion, aplicar `protocols/activos-criticos.md`.
9. Si una fuente implica accesos, aplicar `protocols/gestion-accesos.md`.
10. Si se crean o modifican archivos, actualizar `registries/registro-artefactos.md`.

## Flujo operativo

### 1. Recibir

Aceptar como entrada:

- URL;
- archivo local;
- captura;
- export;
- nota de Rodrigo;
- output legacy;
- documentacion oficial;
- aprendizaje de una sesion.

### 2. Clasificar

Responder:

- que tipo de informacion es;
- que decision permite;
- si ya existe en otra parte;
- si contiene riesgo;
- que destino corresponde.

### 3. Sanear

Extraer solo:

- fuente;
- fecha;
- alcance;
- resumen util;
- decision;
- destino;
- limitaciones.

No copiar:

- texto completo innecesario;
- secretos;
- datos personales;
- dumps;
- rutas locales sensibles;
- capturas pesadas.

### 4. Decidir destino

Elegir uno:

- `knowledge/`
- `protocols/`
- `.claude/rules/`
- `.claude/skills/`
- `.claude/agents/`
- `.claude/commands/`
- `clients/[cliente]/`
- `agency/`
- `quality/`
- `planning/`
- `legacy/`
- descartar.

### 5. Registrar

Actualizar:

- `registries/registro-fuentes.md` para fuentes y conocimiento;
- `registries/registro-artefactos.md` si se crean/modifican archivos;
- manifest de cliente/agencia si se crea output;
- log correspondiente si afecta cliente o agencia.

### 6. Validar

Ejecutar:

```bash
python scripts/protocol_guard.py --no-report
```

Si hay cambios Git:

```bash
git diff --check
```

## Salida esperada

```text
CONOCIMIENTO

FUENTE:
[URL/ruta/nota]

TIPO:
[oficial/evidencia/procedimiento/regla/memoria/preferencia/historico/ruido]

NIVEL:
[K3/K2/K1/K0]

DESTINO:
[ruta o descartar]

DECISION:
[guardar/resumir/convertir/registrar/descartar]

RIESGOS:
[secretos/PII/contradiccion/produccion/ninguno]

ARCHIVOS:
[creados/modificados]

SIGUIENTE PASO:
[accion concreta]
```
