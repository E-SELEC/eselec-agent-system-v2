---
name: ingesta-evidencia
description: >
  Convierte datos vivos, exports, capturas o outputs legacy en evidencia
  saneada para E-SELEC v2. Usalo antes de meter informacion de GSC, GA4,
  SEMrush, GBP, Ads, WordPress, WooCommerce, Notion, Drive o herramientas
  externas en auditorias, informes, contextos, manifests o GitHub.
---

# Ingesta Evidencia - E-SELEC

## Proposito

Transformar datos externos en evidencia interna confiable, minima y versionable.

Esta skill no sirve para analizar el negocio. Sirve para decidir que datos entran al sistema v2, que se descarta, que se resume y que no debe tocar GitHub.

## Principio central

```text
El sistema no guarda dumps. Guarda evidencia saneada.
```

Un export, captura, JSON, CSV o output legacy puede contener ruido, datos personales, rutas locales, sesiones, identificadores, credenciales o volumen excesivo. Antes de usarlo, conviertelo en un archivo `evidencia-[tema]-YYYY-MM-DD.md`.

## Fuentes obligatorias

Antes de crear evidencia para un cliente, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/outputs/manifest.md`
6. `core/fuentes-de-verdad.md`
7. `protocols/gestion-accesos.md`
8. `protocols/control-artefactos.md`
9. `protocols/activos-criticos.md` si la fuente es viva o puede afectar produccion

No proceses secretos en chat. Si un archivo contiene secretos, no copies el valor: registra metadatos y recomienda rotacion.

## Que se puede ingerir

| Fuente | Permitido en v2 | No permitido |
|---|---|---|
| GSC | resumen de clicks, impresiones, CTR, posicion, queries/URLs top | dumps completos sin filtrar, tokens, cuentas personales |
| GA4 | resumen de eventos, conversiones, sesiones, fuente/medio | client IDs, user IDs, exports con PII |
| SEMrush | resumen de trafico estimado, keywords, paginas, competidores | capturas pesadas, credenciales, sesiones |
| GBP | resumen de reseñas, llamadas, direcciones, acciones | datos personales de usuarios o respuestas sensibles |
| Ads | gasto, CPA, ROAS, campañas, conversiones agregadas | IDs sensibles, tokens, datos personales |
| WordPress/WooCommerce | estado tecnico, URLs, productos agregados | claves, usuarios, pedidos con PII |
| Legacy outputs | hallazgos, metricas clave, limites | copiar outputs completos por comodidad |

## Nivel de evidencia

Clasifica el archivo antes de usarlo:

- E3 - vivo verificado: fuente consultada en esta sesion, cuenta/dominio/periodo confirmados.
- E2 - export reciente saneado: export o output reciente con fuente declarada, dominio y periodo claros.
- E1 - historico/orientativo: output antiguo, captura parcial o dato sin periodo verificable.
- E0 - rechazado: contiene secretos, PII, contradiccion critica, fuente equivocada o no permite asociar cliente/dominio.

Regla:

- E0 no entra al repo.
- E1 solo orienta.
- E2 permite auditoria parcial fuerte.
- E3 permite auditoria/informe final si el contrato del output tambien se cumple.

## Workflow

### 1. Definir proposito

Determina:

- cliente;
- fuente original;
- servicio afectado;
- periodo;
- decision que soportara;
- si el archivo se guardara en v2.

Si no hay decision concreta, no crees evidencia.

### 2. Clasificar riesgo

Antes de leer o resumir, clasifica:

- bajo: metricas agregadas sin PII ni secretos;
- medio: datos de cliente o negocio, sin credenciales;
- alto: exports grandes, datos vivos, cuentas, usuarios, IDs, pagos o produccion;
- bloqueado: secretos, cookies, tokens, claves, passwords, PII o datos de otro cliente.

Si es alto, resume minimo. Si es bloqueado, detente.

### 3. Extraer solo lo necesario

Extrae:

- fuente y fecha;
- dominio/cuenta/propiedad;
- periodo;
- metricas clave;
- top hallazgos;
- contradicciones;
- limites;
- decision permitida;
- decision prohibida;
- proxima accion unica.

No extraigas:

- filas completas sin necesidad;
- IDs de usuario;
- rutas locales sensibles;
- tokens, cookies o claves;
- capturas pesadas;
- datos personales;
- datos de otro cliente.

### 4. Crear evidencia saneada

Usa `templates/evidencia-datos.md`.

Ruta recomendada:

```text
clients/[cliente]/outputs/evidencia-[tema]-YYYY-MM-DD.md
```

Nombres validos:

- `evidencia-seo-2026-05-12.md`
- `evidencia-gsc-2026-05-12.md`
- `evidencia-ga4-conversiones-2026-05-12.md`
- `evidencia-meta-ads-2026-05-12.md`

### 5. Actualizar trazabilidad

Si guardas archivo:

- actualizar `clients/[cliente]/outputs/manifest.md`;
- actualizar `clients/[cliente]/log.md`;
- actualizar `registries/registro-artefactos.md` si el impacto es estrategico, sensible o reusable;
- marcar datos obsoletos si reemplaza una evidencia anterior.

### 6. Revisar antes de cerrar

Usa `checklists/revision.md`.

No cierres si:

- no hay periodo;
- no se distingue dato real de estimacion;
- no se declara fuente;
- no se declaran limitaciones;
- no queda claro si la evidencia es E1/E2/E3;
- el archivo contiene secretos o PII.

## Relacion con otras skills

- Usa `ingesta-evidencia` antes de `verificacion-medicion` cuando el dato viene de export, captura o legacy.
- Usa `verificacion-medicion` despues para decidir si el output puede ser final/parcial/orientativo.
- Usa `seo-audit`, `client-audit`, `reports`, `cro` o `ads` solo despues de tener evidencia suficiente.

## Archivos de apoyo

- `templates/evidencia-datos.md`: formato de evidencia saneada.
- `checklists/revision.md`: revision antes de versionar o usar.
