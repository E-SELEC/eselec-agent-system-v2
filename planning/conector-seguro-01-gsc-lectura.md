# Conector seguro 01 - GSC solo lectura

Fecha: 2026-05-13
Estado: especificado, no implementado
Tipo: especificacion reutilizable; ejemplos anonimizados
Decision Sprint 01: O1-005
Responsable: Codex + Arquitecto
Produccion tocada: no
Accesos usados: ninguno

## Decision

El primer conector seguro a reconstruir debe ser Google Search Console en modo solo lectura.

Nombre operativo propuesto:

```text
gsc-readonly
```

## Por que este primero

GSC desbloquea una prioridad critica en clientes SEO: verificar rendimiento real antes de tomar decisiones de CTR, paginas nuevas, auditoria final o informes.

Es mejor primer conector que otras opciones porque:

- aporta datos reales de SEO sin tocar web ni Ads;
- permite validar `seo-audit` y `verificacion-medicion`;
- reduce dependencia de outputs legacy;
- su uso puede limitarse a consultas read-only;
- no consume presupuesto;
- no modifica produccion si se implementa con alcance estricto.

## Candidatos descartados por ahora

| Candidato | Decision | Motivo |
|---|---|---|
| WordPress/WooCommerce | no empezar aqui | Puede modificar web, checkout, productos, plugins o contenido. Riesgo C/D. |
| Meta Ads | no empezar aqui | Puede afectar gasto, billing, campanas y tokens sensibles. Riesgo alto. |
| SEMrush automatizado | no empezar aqui | Fuente critica pero acceso sensible; primero usar exports saneados. |
| GA4 | despues de GSC | Valioso para conversion, pero mas facil mezclar propiedades/eventos y datos sensibles. |
| Notion sync | no prioritario | MCP ya cubre lectura/actualizacion directa cuando esta disponible. |
| Google Drive | despues | Almacenamiento util, pero no desbloquea la decision SEO inmediata. |

## Alcance permitido

Permitido:

- leer Search Analytics por propiedad confirmada;
- consultar clics, impresiones, CTR y posicion;
- agrupar por query, page, country, device o date cuando haga falta;
- limitar periodo con fechas explicitas;
- producir evidencia saneada, no dumps;
- trabajar cliente por cliente.

No permitido:

- modificar propiedades;
- enviar sitemaps;
- gestionar usuarios/permisos;
- cambiar configuracion de GSC;
- guardar JSON bruto completo;
- guardar tokens, client secrets, rutas privadas o IDs innecesarios;
- mezclar datos de varias propiedades sin confirmacion;
- usar datos como finales si dominio/periodo no estan verificados.

## Clasificacion de riesgo

Accion API prevista: Nivel A, solo lectura.

Acceso OAuth futuro: tratar como S4 por contener token/refresh token, aunque el scope sea read-only.

Implicacion:

- no se crea ni usa ningun token en esta especificacion;
- el token debe vivir fuera del repo;
- el registro debe guardar metadatos, nunca valores;
- antes de usar credenciales reales hay que actualizar `registries/registro-accesos.md`;
- cualquier ampliacion de scope exige nueva revision.

## Variables esperadas

Estas variables son nombres propuestos, sin valores:

```text
GSC_CLIENT_SECRET_FILE
GSC_TOKEN_FILE
GSC_DEFAULT_DAYS
```

Reglas:

- `GSC_CLIENT_SECRET_FILE` y `GSC_TOKEN_FILE` deben apuntar a rutas locales fuera del repo.
- `.env` puede contener rutas, pero nunca debe subirse.
- Ningun valor real debe aparecer en logs, outputs, manifests o commits.

## Interfaz futura propuesta

```bash
python scripts/gsc_readonly_connector.py --cliente [nombre-cliente] --site-url [site-url] --start YYYY-MM-DD --end YYYY-MM-DD --dry-run
```

Modo de escritura opcional:

```bash
python scripts/gsc_readonly_connector.py --cliente [nombre-cliente] --site-url [site-url] --start YYYY-MM-DD --end YYYY-MM-DD --write-evidence
```

Reglas:

- `--dry-run` debe ser el comportamiento por defecto.
- `--write-evidence` solo crea evidencia saneada.
- Si faltan credenciales, el script debe fallar con mensaje operativo sin pedir secretos por chat.
- Si la propiedad no coincide con `clients/[cliente]/context.md`, debe bloquear la salida.

## Output permitido

Ruta:

```text
clients/[cliente]/outputs/evidencia-gsc-YYYY-MM-DD.md
```

Contenido minimo:

- fuente: Google Search Console;
- cliente;
- dominio/propiedad;
- periodo;
- fecha de extraccion;
- filtros usados;
- nivel de evidencia;
- metricas agregadas;
- top oportunidades resumidas;
- limites;
- decision permitida;
- decision prohibida;
- proxima accion unica.

No guardar:

- dumps completos;
- tokens;
- rutas locales;
- capturas pesadas;
- datos de otros clientes;
- filas sin utilidad para la decision.

## Pruebas minimas antes de implementarlo

1. `python scripts/gsc_readonly_connector.py --help` no imprime secretos.
2. Sin credenciales reales, el script falla limpio y explica variables faltantes.
3. Con fixture/mock, genera resumen saneado sin red.
4. Con credenciales reales, primero ejecutar `--dry-run`.
5. Verificar que propiedad/dominio coinciden con `context.md`.
6. Ejecutar `python scripts/protocol_guard.py --no-report`.
7. Registrar acceso en `registries/registro-accesos.md` antes del primer uso real.
8. Registrar evidencia en manifest si se crea output.

## Orden de implementacion futura

1. Crear script con `--help`, validacion de argumentos y dry-run sin credenciales.
2. Agregar lectura de variables/rutas sin imprimir valores.
3. Agregar capa de cliente: leer `context.md` y confirmar dominio esperado.
4. Agregar modo mock/fixture.
5. Agregar conexion real read-only.
6. Agregar salida saneada `evidencia-gsc`.
7. Ejecutar con el cliente piloto aprobado.
8. Usar resultado en `verificacion-medicion` antes de auditoria SEO final.

## Decision final O1-005

Primer conector seguro elegido: GSC solo lectura.

Implementacion: pendiente de aprobacion y de preparacion segura de OAuth fuera del repo.
