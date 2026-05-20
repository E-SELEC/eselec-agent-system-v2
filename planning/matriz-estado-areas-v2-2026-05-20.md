# Matriz de estado por area - E-SELEC v2

Fecha: 2026-05-20
Responsable: Codex
Consulta de contraste: Claude Code, solo lectura, sin edicion de archivos
Alcance: CRO, SEM/Paid Ads, Reports, Web/WooCommerce y Social

## Decision ejecutiva

SEO es la unica area que hoy tiene una arquitectura completa de este tipo:

```text
manual operativo heredado -> canon activo -> indice bajo demanda -> skills -> agentes
```

Las demas areas no estan mal. Estan operativas, pero funcionan de otra manera:

```text
leader ligero -> skills procedurales -> references/checklists/templates
```

Eso es suficiente para ejecutar tareas controladas, pero no reproduce todavia el nivel de criterio profundo que hizo fuerte al Docente SEO.

## Evidencia usada

### Inventario de piezas relevantes

Comando usado:

```powershell
rg --files .claude\agents .claude\skills .claude\commands | rg "cro|sem|paid|ads|reports|report|analytics|web|social|content|woocommerce|copy|meta|google-ads"
```

Resultado:

- Existen leaders y especialistas para CRO, SEM, Reports, Web y Social.
- Existen commands para CRO, Paid Ads, Web, WooCommerce, Social y Copy.
- Existen skills operativas para Paid Ads, Reports, CRO, Web, WooCommerce, Social y Analytics.

### Conteo de soporte por skill

Comando usado:

```powershell
& { $skills = 'paid-ads','reports','page-cro','form-cro','signup-flow-cro','onboarding-cro','popup-cro','paywall-upgrade-cro','ab-test-setup','web-feedback-loop','woocommerce-setup','social-content','content-strategy','analytics-tracking'; foreach ($s in $skills) { $path = ".claude\skills\$s"; if (Test-Path -LiteralPath $path) { $files = Get-ChildItem -LiteralPath $path -Recurse -File; $refs = @($files | Where-Object { $_.FullName -match '\\references\\' }); $checks = @($files | Where-Object { $_.FullName -match '\\checklists\\' }); $templates = @($files | Where-Object { $_.FullName -match '\\templates\\' }); [PSCustomObject]@{Skill=$s; Files=$files.Count; References=$refs.Count; Checklists=$checks.Count; Templates=$templates.Count} } } } | Format-Table -AutoSize
```

Resultado resumido:

| Skill | Archivos | Referencias | Checklists | Templates |
|---|---:|---:|---:|---:|
| `paid-ads` | 5 | 2 | 1 | 1 |
| `reports` | 5 | 1 | 0 | 3 |
| `page-cro` | 5 | 2 | 1 | 1 |
| `analytics-tracking` | 5 | 2 | 1 | 1 |
| `content-strategy` | 5 | 2 | 1 | 1 |
| `web-feedback-loop` | 4 | 1 | 1 | 1 |
| `woocommerce-setup` | 4 | 1 | 1 | 1 |
| `social-content` | 4 | 1 | 1 | 1 |

### Revision de canons existentes

Comando usado:

```powershell
rg --files .claude\skills .claude\agents .claude\commands | rg "canon"
```

Resultado:

- Solo aparece `seo-canon` como canon real.
- No existe `sem-canon`, `cro-canon`, `reports-canon`, `web-canon` ni `social-canon`.

### Revision de contaminacion por clientes reales

Comando usado:

```powershell
rg -n "computer-chamberi|Computer Chamber|Stramondo|stramondo|cashier-bubble|Cashier|Chashier|bottega|Bottega|shogun|Shogun|tallermotoshogun|labottega|cliente real" .claude\agents .claude\commands .claude\skills\paid-ads .claude\skills\reports .claude\skills\page-cro .claude\skills\form-cro .claude\skills\signup-flow-cro .claude\skills\onboarding-cro .claude\skills\popup-cro .claude\skills\paywall-upgrade-cro .claude\skills\ab-test-setup .claude\skills\web-feedback-loop .claude\skills\woocommerce-setup .claude\skills\social-content .claude\skills\content-strategy .claude\skills\analytics-tracking
```

Resultado:

- Sin coincidencias.
- No se detectaron nombres de clientes reales en las carpetas generales revisadas.

## Estado por area

| Area | Estado actual | Canon/manual profundo | Riesgo principal | Decision |
|---|---|---|---|---|
| SEO | Completo y operativo | Si: `seo-canon` + manual heredado | Verificacion viva pendiente en algunos modulos | Mantener, no reescribir. |
| SEM / Paid Ads | Operativo procedimental | No | Gasto real, tracking, presupuesto, claims, plataformas | Crear conversacion fuente/manual operativo SEM antes de pensar en canon. |
| CRO | Operativo procedimental | No | Decisiones implicitas: que cambiar, que testear, que priorizar | Segundo candidato despues de SEM. |
| Reports / Analytics | Operativo fuerte | No | Narrativa con datos parciales o metricas sin fuente | Mantener; reforzar si fallan informes reales. |
| Web / WooCommerce | Operativo con guardrails | No | Produccion, WordPress, pagos, tracking, SEO tecnico | Mantener como skills + protocolos; canon solo si aparece patron repetido. |
| Social / Content | Operativo basico-fuerte | No | Contenido generico, tono intercambiable, claims sin fuente | Mantener como skill; observar outputs antes de canon. |

## Lectura por area

### SEM / Paid Ads

Fortalezas actuales:

- `sem-leader` clasifica por capa: objetivo, tracking, oferta, audiencia, presupuesto, creatividad, landing o cuenta.
- `paid-ads` tiene niveles PA0-PA3, reglas de tracking, presupuesto, landing y bloqueo de produccion.
- Tiene referencias para plataformas y reglas.

Falta:

- Manual profundo comparable a SEO.
- Criterio propietario: como Rodrigo quiere pensar presupuesto, learning phase, escalado, riesgo y lectura de plataformas.
- Fuentes oficiales por plataforma separadas: Meta desde Meta, Google Ads desde Google, LinkedIn desde LinkedIn, TikTok desde TikTok.

Decision:

```text
SEM es el siguiente paso.
Primero manual operativo fuente; despues se decide si merece canon.
```

### CRO

Fortalezas actuales:

- `cro-leader` enruta bien.
- `page-cro` tiene niveles PC0-PC3, workflow, bloqueos y templates.
- Existen skills especializadas: forms, signup, onboarding, popup, paywall, AB tests.

Falta:

- Canon de decision: cuando cambiar directo, cuando testear, cuando medir, cuando no tocar.
- Criterio de UX/conversion propio de E-SELEC.

Decision:

```text
CRO debe ir despues de SEM si se busca replicar el patron SEO.
```

### Reports / Analytics

Fortalezas actuales:

- `reports` es una skill fuerte.
- Distingue informe mensual, alerta y proximos pasos.
- Tiene niveles R0-R3, fuentes, bloqueos y templates.
- `analytics-tracking` es fuerte y separa medicion por decision.

Falta:

- Checklist de revision propio en `reports`.
- Manual de criterio narrativo si los informes salen flojos.

Decision:

```text
No crear canon ahora. Mantener como skill fuerte y observar outputs reales.
```

### Web / WooCommerce

Fortalezas actuales:

- `web-leader` bloquea cambios de produccion sin Orden de Cambio.
- `web-feedback-loop` cubre revision visual.
- `woocommerce-setup` tiene niveles WC0-WC3 y guardrails.

Falta:

- Manual de QA/prelaunch si se repiten cambios web complejos.
- Criterio visual/brand mas profundo si Web empieza a producir entregables grandes.

Decision:

```text
No crear canon ahora. Web depende mas de protocolos y verificacion que de canon.
```

### Social / Content

Fortalezas actuales:

- `social-leader` exige objetivo de negocio.
- `social-content` pide canal, audiencia, tono, oferta y CTA.
- `content-strategy`, `copywriting`, `copy-editing` y `humanizalo` cubren gran parte del flujo.

Falta:

- Criterio profundo de marca/canales si se busca una metodologia propietaria.
- Manual de social por plataforma solo si empieza a ser una linea fuerte de E-SELEC.

Decision:

```text
Mantener como skill operativa. No canon todavia.
```

## Acuerdo con Claude

Claude confirmo la clasificacion con dos ajustes:

1. SEM primero, pero con una condicion: no convertirlo en canon si solo produce buenas practicas genericas. Debe tener fuentes primarias y criterio propio de Rodrigo/E-SELEC.
2. Despues de SEM, CRO es mejor candidato que Web o Social porque contiene muchas decisiones implicitas que hoy no viven en una capa de criterio estable.

## Orden recomendado

| Orden | Area | Accion |
|---|---|---|
| 1 | SEM / Paid Ads | Crear conversacion fuente y manual operativo. No canon inmediato. |
| 2 | CRO | Crear conversacion fuente si SEM valida el metodo. |
| 3 | Reports / Analytics | Reforzar skill/checklist si se detectan outputs flojos. |
| 4 | Web / WooCommerce | Mantener protocolos; evaluar QA/prelaunch luego. |
| 5 | Social / Content | Observar calidad antes de crear metodologia larga. |

## Checklist de esta fase

- [x] Inventariar leaders y skills no SEO.
- [x] Confirmar que no hay canons no SEO.
- [x] Medir referencias, checklists y templates por skill.
- [x] Revisar contaminacion por clientes reales en carpetas generales relevantes.
- [x] Consultar con Claude.
- [x] Definir prioridad: SEM primero, CRO despues.

## Siguiente paso

Preparar el brief de conversacion fuente para SEM/Paid Ads usando `planning/metodo-creacion-canons-por-area-2026-05-20.md`.

Ese brief no debe crear canon todavia. Debe producir manual operativo profundo con fuentes oficiales por plataforma.
