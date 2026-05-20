# Politica de activacion de skills

Fecha: 2026-05-20
Estado: decision vigente
Alcance: `.claude/skills/`, `.claude/agents/`, settings de Claude Code

## Decision

Las skills pueden existir dentro de `.claude/skills/`.

Eso no significa que deban activarse solas ni quedar adheridas a agentes.

Una skill solo puede quedar como automatica o precargada si cumple una de estas condiciones:

1. fue creada o adaptada al sistema E-SELEC;
2. tiene manual operativo, canon o criterio E-SELEC detras;
3. tiene evidencia de validacion por Rodrigo o por una auditoria especifica;
4. tiene un rol claro y no compite con otra skill activa;
5. no mete ejemplos de clientes reales en material general.

## Definiciones

### Skill existente

La carpeta existe en `.claude/skills/`.

Puede quedarse ahi aunque no este validada. Existir no es el problema.

### Skill auto-invocable

Claude puede usarla sin que Rodrigo la nombre si su `description` coincide con la tarea.

Segun la documentacion oficial local de Claude Code, por defecto Claude puede invocar cualquier skill que no tenga `disable-model-invocation: true`.

### Skill adherida

Una skill aparece en el frontmatter de un agente:

```yaml
skills:
  - nombre-skill
```

Esto precarga la skill en el agente y la convierte en parte de su criterio de arranque.

### Skill bajo demanda

La skill existe, pero solo debe usarse cuando Rodrigo la nombra, un agente la elige conscientemente o una tarea la justifica despues de leer contexto.

## Regla E-SELEC

```text
Carpeta de skills = biblioteca disponible.
Skill auto-invocable = confianza operativa.
Skill adherida a agente = criterio estructural.
```

Por tanto:

```text
No toda skill existente puede ser auto-invocable.
No toda skill util puede estar adherida a un agente.
Solo las skills con criterio E-SELEC probado pueden mandar solas.
```

## Estado actual verificado

Comandos de evidencia:

```powershell
Get-ChildItem -LiteralPath .claude\skills -Directory
Select-String -Path .claude\agents\*.md -Pattern '^skills:|^\s+-\s+'
```

Resultado:

- carpetas de skills: 47;
- skills con `SKILL.md`: 46;
- skills con `disable-model-invocation: true` en frontmatter: 0;
- skills adheridas por agentes: `alignment-check` y `seo-canon`;
- `seo-canon` esta adherida a todos los agentes SEO;
- `alignment-check` esta adherida al agente `alineacion`;
- el resto de skills no estan adheridas a agentes, pero siguen auto-invocables por descripcion.

## Skills estructurales validadas

| Skill | Estado | Motivo |
|---|---|---|
| `seo-canon` | validada/adherida | Fue creada desde el metodo real de Rodrigo, contiene criterio E-SELEC y respalda a los agentes SEO. |
| `alignment-check` | validada/adherida con vigilancia | Es la skill de auditoria Claude Code. Debe seguir basada en fuentes oficiales y evidencia local; no debe ejecutar cambios. |

## Skills no validadas completamente

Todas las demas skills quedan en estado:

```text
existentes, potencialmente utiles, pero no aprobadas como criterio automatico E-SELEC.
```

Esto incluye skills de:

- SEM / Paid Ads;
- CRO;
- Reports;
- Web;
- Social;
- copywriting;
- estrategia;
- ventas;
- retencion;
- pricing;
- herramientas especificas.

No se eliminan. No se desprecia su utilidad. Solo no deben gobernar solas hasta pasar por auditoria o reconstruccion.

## Orden seguro recomendado

Claude recomendo este orden y queda adoptado:

1. Matriz primero.
2. Usar `settings.local.json` para skills dudosas si hay que hacer cuarentena reversible.
3. Usar `disable-model-invocation: true` en frontmatter solo cuando una skill se confirme como no apta o de uso estrictamente manual.

## Por que no desactivar todo de golpe

Desactivar sin mapa puede romper flujos utiles.

El objetivo no es apagar el sistema, sino ordenar la confianza:

- lo validado puede operar;
- lo dudoso queda bajo demanda;
- lo claramente incorrecto se desactiva;
- lo que necesita mejora pasa por manual operativo y canon.

## Criterio para promocionar una skill

Una skill puede pasar de "bajo demanda" a "auto-invocable" si tiene:

1. proposito claro;
2. descripcion precisa;
3. fuentes o criterio documentado;
4. limites de accion;
5. checklist de salida;
6. relacion clara con agente o area;
7. prueba de calidad con caso real o simulado;
8. aprobacion explicita de Rodrigo o auditoria de alineacion.

## Criterio para adherir una skill a un agente

Una skill solo debe ir en `skills:` de un agente si representa criterio base, no solo una herramienta.

Ejemplo correcto:

```yaml
skills:
  - seo-canon
```

Motivo: `seo-canon` define como piensa SEO en E-SELEC.

Ejemplo no recomendado:

```yaml
skills:
  - paid-ads
```

Motivo actual: `paid-ads` todavia es una skill procedural, no un canon validado por la metodologia E-SELEC.

## Siguiente accion

Crear una matriz de skills con columnas:

- skill;
- area;
- origen probable;
- adherida a agente;
- auto-invocable actual;
- manual/canon detras;
- riesgo;
- estado recomendado;
- accion.

Despues de esa matriz se decide si aplicar cuarentena local con `skillOverrides`.
