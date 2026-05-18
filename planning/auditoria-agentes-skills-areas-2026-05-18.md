# Auditoria por areas de agentes y skills - 2026-05-18

## Objetivo

Revisar si los agentes por area de E-SELEC v2 tienen una estructura suficiente para trabajar con calidad bajo Claude Code, sin copiar automaticamente el patron SEO a todo el sistema.

Esta fase no ejecuta cambios sobre agentes, skills ni commands. Solo separa:

- hechos verificados;
- inferencias;
- riesgos;
- acciones recomendadas para fases siguientes.

## Evidencia operativa

Comando usado para conteo:

```powershell
$agents = Get-ChildItem -Path .claude\agents -Filter *.md | Where-Object { $_.Name -ne 'README.md' }
$skills = Get-ChildItem -Path .claude\skills -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') }
$commands = Get-ChildItem -Path .claude\commands -Filter *.md | Where-Object { $_.Name -ne 'README.md' }
[pscustomobject]@{ Agents=$agents.Count; Skills=$skills.Count; Commands=$commands.Count } | ConvertTo-Json -Compress
```

Resultado:

```json
{"Agents":47,"Skills":45,"Commands":43}
```

Agentes por prefijo:

```text
agency: 5
alineacion: 1
arquitecto: 2
calibracion: 1
cro: 6
docente: 1
fenix: 1
leader: 2
loops: 1
reports: 4
sem: 6
seo: 6
social: 4
web: 7
```

## Consulta a Claude

Se pidio a Claude revisar el criterio antes de documentar. Su correccion principal fue:

- No tratar `canon` y `skill dedicada` como soluciones equivalentes.
- No llamar duplicacion a `commands` y `skills` por defecto; en Claude Code son capas distintas.
- El problema real de commands seria que contengan logica propia pesada en vez de actuar como entrada fina hacia una skill.
- Un canon no es solo "conocimiento historico denso"; es una puerta transversal de criterio que debe aplicarse antes de cualquier tarea del area.

Orden recomendado por Claude:

1. Crear o reforzar skill de reports.
2. Auditar SEM con mas detalle.
3. Leer commands representativos para confirmar si son wrappers finos.
4. Revisar si Web necesita una puerta transversal.
5. Documentar criterios corregidos.

## Criterio corregido

### Skill dedicada

Una skill dedicada resuelve el procedimiento de trabajo:

- que leer;
- que fuentes usar;
- como priorizar;
- que output entregar;
- que bloquear;
- que plantilla usar.

Ejemplo: `page-cro`, `paid-ads`, `analytics-tracking`, `site-architecture`.

### Canon

Un canon es una capa de criterio transversal que debe leerse antes de cualquier tarea importante del area, aunque luego se use una skill especifica.

Sirve cuando existe un juicio comun que no pertenece a una sola tarea:

- forma de pensar del area;
- estandares de calidad;
- errores historicos que no deben repetirse;
- reglas de priorizacion;
- criterio docente;
- lenguaje comun entre subagentes.

Ejemplo actual: `seo-canon`.

### Command

Un command es una entrada facil para Rodrigo, no una segunda skill.

El patron correcto observado en commands revisados:

1. leer la skill correspondiente;
2. leer contexto del cliente/agencia;
3. entregar en chat por defecto;
4. escribir solo con `--write`;
5. aplicar manifest, log y protocolos si escribe.

Commands revisados:

- `.claude/commands/auditar-cro-pagina.md`
- `.claude/commands/plan-paid-ads.md`
- `.claude/commands/plan-contenido.md`
- `.claude/commands/verificar-medicion.md`

Conclusion: estos commands no son duplicacion problematica; son wrappers finos.

## Mapa por area

| Area | Agentes | Skills principales | Canon compartido | Estado | Riesgo | Recomendacion |
|---|---:|---|---|---|---|---|
| SEO | 6 | `seo-audit`, `content-strategy`, `ai-seo`, `schema-markup`, `site-architecture`, `analytics-tracking` | Si: `seo-canon` | Patron mas maduro | Bajo-medio | Mantener como base. No resumir el canon. Usarlo como puerta antes de SEO profundo. |
| CRO | 6 | `page-cro`, `form-cro`, `signup-flow-cro`, `onboarding-cro`, `popup-cro`, `paywall-upgrade-cro`, `ab-test-setup`, `marketing-psychology` | No | Skills fuertes | Medio | No crear canon todavia. Primero observar calidad real; crear canon solo si aparecen criterios transversales repetidos. |
| SEM / Paid Ads | 6 | `paid-ads`, `ad-creative`, `analytics-tracking`, `page-cro`, `copywriting`, `social-content` | No | Skills fuertes, riesgo operativo alto | Medio-alto | Auditar con mas detalle. Posible candidato futuro a `paid-media-canon` si hay criterio transversal de presupuesto, tracking, Meta/Google y seguridad. |
| Reports | 4 | `analytics-tracking`, `copy-editing`, `humanizalo`, `client-audit`, `quality/criterios-output.md` | No | Area mas debil estructuralmente | Alto | Crear primero una skill dedicada de reports. Solo crear canon si existe historial valioso de feedback, errores o estilo de informes. |
| Web | 7 | `site-architecture`, `web-feedback-loop`, `woocommerce-setup`, `schema-markup`, `analytics-tracking`, `page-cro`, `seo-audit` | No | Skills fuertes y guardrails claros | Medio-alto | No tocar aun. Revisar si necesita canon transversal de produccion/WordPress/QA o si bastan skills + protocolos. |
| Social | 4 | `content-strategy`, `social-content`, `copywriting`, `humanizalo`, `marketing-psychology` | No | Skills suficientes para operar | Medio | No crear canon por ahora. Revisar outputs reales antes de decidir. |

## Hallazgos

### H1 - SEO ya tiene el patron que funciono

SEO combina:

- agentes ligeros;
- canon transversal (`seo-canon`);
- skills operativas por tarea;
- datos de cliente fuera del canon;
- patrones anonimizados cuando un caso real deja aprendizaje reutilizable.

Esto debe ser el patron mental del sistema, pero no se debe copiar literalmente a todas las areas.

### H2 - Reports es el siguiente punto mas importante

Reports no tiene una skill propia equivalente a `page-cro` o `paid-ads`.

Actualmente depende de:

- `analytics-tracking` para datos;
- `copy-editing` y `humanizalo` para claridad;
- `quality/criterios-output.md` para contrato de calidad.

Inferencia: puede funcionar, pero el riesgo de outputs inconsistentes es mayor porque no hay procedimiento especifico de informe: narrativa, secciones, decision, limitaciones, lectura ejecutiva y proximos pasos.

Accion recomendada: crear o reforzar una skill dedicada de reports antes de pensar en canon.

### H3 - CRO no necesita canon inmediato

CRO tiene skills procedurales maduras. Por ahora el problema no es falta de estructura, sino comprobar si en uso real hay fallos repetidos de criterio.

Accion recomendada: observar outputs CRO antes de crear `cro-canon`.

### H4 - SEM requiere auditoria propia por riesgo operativo

SEM/Paid Ads tiene skills fuertes, pero opera cerca de presupuesto, pixels, conversiones y cuentas reales.

Accion recomendada: auditar SEM como subfase propia antes de crear cambios. Si aparece criterio transversal, evaluar `paid-media-canon`.

### H5 - Commands no son duplicacion por defecto

La superposicion command/skill es normal si el command es una entrada fina y la skill mantiene el procedimiento.

Accion recomendada: en una fase posterior, revisar los 43 commands con una regla simple:

- correcto: command lee skill, contexto y define salida;
- incorrecto: command repite logica que deberia vivir en la skill.

## Orden de trabajo recomendado

1. Reports: disenar skill dedicada de informes.
2. SEM: auditoria profunda por riesgo operativo.
3. Commands: revisar wrappers finos vs logica duplicada.
4. Web: decidir si necesita canon transversal o no.
5. Social y CRO: observar outputs antes de crear canons.
6. Gobernanza: actualizar checklist de uso para Rodrigo cuando se estabilice el patron.

## Checklist de Fase 3

- [x] Contar agentes, skills y commands con evidencia operativa.
- [x] Verificar que SEO usa `seo-canon`.
- [x] Revisar rutas de skills en CRO.
- [x] Revisar rutas de skills en SEM.
- [x] Revisar rutas de skills en Reports.
- [x] Revisar rutas de skills en Web.
- [x] Revisar rutas de skills en Social.
- [x] Consultar a Claude y corregir criterio.
- [x] Revisar commands representativos.
- [x] Documentar hallazgos y orden recomendado.
