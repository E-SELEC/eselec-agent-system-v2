# Auditoria SEO - migracion Docente -> manual -> canon -> agentes

Fecha: 2026-05-20
Responsable: Codex
Consulta de contraste: Claude Code, solo lectura, sin edicion de archivos
Alcance: estructura SEO general de E-SELEC v2, no clientes concretos

## Decision ejecutiva

SEO esta funcional y operativo en v2.

La estructura correcta ya existe:

- `seo-canon` conecta el aprendizaje historico del Docente SEO con Claude Code v2.
- `aprendizajes/` conserva el manual operativo SEO heredado.
- `fuentes/` conserva fuentes historicas y puntos pendientes de verificacion viva.
- `indice-canon-seo.md` decide que leer segun el caso.
- Los agentes SEO usan `skills: seo-canon`.
- Los casos reales no viven dentro del canon general; el patron reutilizable esta anonimizado.

No hace falta reconstruir SEO desde cero.

Si queremos replicar este patron en SEM, CRO, Reports, Web o Social, no hay que copiar todos los archivos SEO. Hay que copiar la arquitectura:

```text
conversacion fuente -> manual operativo -> filtro de contaminacion -> canon solo si aplica -> skill -> referencias -> checklist -> agentes ligeros
```

## Evidencia usada

### Inventario SEO actual

Comando usado:

```powershell
rg --files .claude\skills\seo-canon .claude\agents .claude\skills .claude\commands | rg "seo|docente|canon|alignment|alineacion"
```

Resultado relevante:

- `seo-canon/SKILL.md` existe.
- `seo-canon/references/indice-canon-seo.md` existe.
- `seo-canon/references/docente-legacy/docente.md` existe.
- `seo-canon/references/docente-legacy/docente-seo.md` existe.
- `seo-canon/references/docente-legacy/aprendizajes/` existe.
- `seo-canon/references/docente-legacy/fuentes/` existe.
- `seo-canon/references/patrones/` existe.
- `seo-leader`, `seo-local`, `seo-organico`, `seo-tecnico`, `seo-web` y `seo-llms` existen.

### Conteos verificados

Comandos usados:

```powershell
(Get-ChildItem -LiteralPath '.claude\skills\seo-canon\references\docente-legacy\aprendizajes' -File).Count
(Get-ChildItem -LiteralPath '.claude\skills\seo-canon\references\docente-legacy\fuentes' -File).Count
(Get-ChildItem -LiteralPath '.claude\skills\seo-canon\references\patrones' -File).Count
(Get-ChildItem -LiteralPath '.claude\agents' -Filter 'seo-*.md' -File).Count
```

Resultado:

- 28 archivos en `aprendizajes/`.
- 5 archivos en `fuentes/`.
- 1 patron anonimizado en `patrones/`.
- 6 agentes SEO activos.

### Uso del canon en agentes SEO

Comando usado:

```powershell
rg -n "^(name|description|tools|model|permissionMode|skills|effort):" .claude\agents\seo-leader.md .claude\agents\seo-llms.md .claude\agents\seo-local.md .claude\agents\seo-organico.md .claude\agents\seo-tecnico.md .claude\agents\seo-web.md
```

Resultado:

- Los 6 agentes SEO tienen frontmatter.
- Los 6 agentes SEO declaran `skills:`.
- Los 6 agentes SEO usan `Read, Grep, Glob`, no herramientas de escritura directa.
- Los 6 agentes SEO usan `model: sonnet` y `effort: high`.

## Mapa de capas SEO

| Capa | Ubicacion | Estado | Funcion |
|---|---|---|---|
| Fuente historica del Docente | `.claude/skills/seo-canon/references/docente-legacy/docente.md` | Migrada como referencia historica | Explica la filosofia del Docente, no opera como instruccion activa. |
| Fuente historica Docente SEO | `.claude/skills/seo-canon/references/docente-legacy/docente-seo.md` | Migrada como referencia historica | Explica como nacio la formacion SEO, no opera como agente activo. |
| Manual operativo heredado | `.claude/skills/seo-canon/references/docente-legacy/aprendizajes/` | Migrado | Contiene los modulos profundos que hicieron funcionar el Docente SEO. |
| Fuentes historicas | `.claude/skills/seo-canon/references/docente-legacy/fuentes/` | Migradas | Conservan origen y links; no sustituyen verificacion viva. |
| Canon activo | `.claude/skills/seo-canon/SKILL.md` | Activo | Decide como aplicar el criterio SEO sin cargar todo siempre. |
| Indice de lectura | `.claude/skills/seo-canon/references/indice-canon-seo.md` | Activo | Mapa para elegir archivo segun caso. |
| Skill operativa | `.claude/skills/seo-audit/SKILL.md` | Activa | Ejecuta auditorias SEO verificables. |
| Checklist SEO | `.claude/skills/seo-audit/checklists/revision.md` | Activo | Valida fuentes, alcance, evidencia, schema, riesgo y cierre. |
| Patron anonimizado | `.claude/skills/seo-canon/references/patrones/` | Activo bajo demanda | Permite aprender de casos reales sin contaminar el canon con clientes. |
| Agentes SEO | `.claude/agents/seo-*.md` | Activos | Rutean y diagnostican sin cargar prompts largos. |

## Estado por tipo de pieza

| Tipo | Estado | Nota |
|---|---|---|
| Docente SEO antiguo | Migrado como fuente historica | No debe ejecutarse como agente activo. |
| Manual operativo SEO | Migrado | Vive en `aprendizajes/`; ahora queda declarado explicitamente en `seo-canon/SKILL.md`. |
| Canon SEO | Activo | No se reescribe ni se resume. |
| Skills SEO | Activas | `seo-audit` ejecuta; `seo-canon` da criterio. |
| Agentes SEO | Activos | Todos cargan `seo-canon`; `seo-leader` enruta. |
| Casos reales | Fuera del canon | Solo patrones anonimizados pueden vivir en referencias generales. |
| Fuentes oficiales vivas | Parcial | Varios modulos indican pendiente de verificacion viva. |

## Contaminacion revisada

Comando usado:

```powershell
rg -n "computer|chamber[ií]|stramondo|cashier|bottega|shogun|cliente real|datos reales|outputs/|clients/" .claude\skills\seo-canon\references
```

Resultado:

- No aparecieron nombres de clientes reales dentro del canon SEO.
- Aparecen menciones genericas a `clients/[cliente]/`, que son aceptables porque describen ubicacion, no un caso real.
- El patron reutilizable declara explicitamente que un caso real puede vivir en `clients/[cliente]/`, pero el canon solo debe guardar patrones generales y anonimos.

Conclusion: no se detecto contaminacion de clientes reales en el alcance revisado.

## Deudas tecnicas detectadas y acciones

| Deuda | Severidad | Accion | Estado |
|---|---|---|---|
| `seo-leader.md` decia `seo-local cuando migre` aunque `seo-local.md` ya existe | Media | Corregir routing hacia `seo-local` + `seo-canon` | Corregido |
| `docente.md` y `docente-seo.md` podian confundirse con instrucciones activas | Baja | Agregar cabecera `FUENTE HISTORICA` | Corregido |
| `aprendizajes/` no estaba declarado explicitamente como manual operativo heredado | Baja | Declararlo en `seo-canon/SKILL.md` | Corregido |
| Modulos con `pendiente de verificacion viva` no tienen nivel de confianza consolidado | Baja | Crear backlog de verificacion por fuente oficial antes de convertirlos en examen/canon nuevo | Pendiente |

## Acuerdo con Claude

Claude reviso los hallazgos en modo solo lectura y propuso no decir que SEO "no esta documentado como patron replicable", porque la estructura ya existe. La formulacion correcta es:

```text
SEO funcional y operativo. Canon cargado, agentes conectados, routing activo.
Queda una deuda menor de verificacion viva de fuentes oficiales en modulos
marcados como pendientes.
```

Se adopta esa formulacion.

## Implicacion para SEM y otras areas

Podemos continuar hacia SEM, pero no creando un canon inmediato.

El paso correcto es abrir una conversacion fuente/manual operativo SEM siguiendo el metodo documentado en:

```text
planning/metodo-creacion-canons-por-area-2026-05-20.md
```

Regla para SEM:

- fuente primaria de Meta Ads: Meta.
- fuente primaria de Google Ads: Google.
- fuente primaria de tracking GA4/GTM: Google.
- fuentes externas solo como apoyo.
- no usar clientes reales como ejemplos.
- no convertir en canon hasta pasar `canon-admision.md`.

## Checklist de cierre SEO

- [x] Inventario de piezas SEO actuales.
- [x] Conteos con comandos visibles.
- [x] Cruce Docente SEO antiguo -> manual -> canon -> skills -> agentes.
- [x] Revision de contaminacion de clientes reales.
- [x] Consulta de contraste con Claude.
- [x] Correccion de routing `seo-local`.
- [x] Cabecera historica en `docente-legacy`.
- [x] Declaracion de `aprendizajes/` como manual operativo heredado.
- [ ] Nivel de confianza consolidado por modulo pendiente de verificacion viva.

## Siguiente paso recomendado

Antes de crear el manual SEM, decidir si la deuda pendiente de fuentes SEO se queda como backlog o si se resuelve ahora con una tabla de confianza por modulo.

Mi recomendacion: dejarla en backlog y pasar a SEM, porque no bloquea la operacion SEO actual y no conviene reescribir el canon largo.
