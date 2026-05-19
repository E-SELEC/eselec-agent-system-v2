# Auditoria CRO/Web/Social - 2026-05-19

## Objetivo

Revisar si CRO, Web y Social necesitan canon propio, refuerzo de skills o ajustes de routing antes de replicar el patron SEO en otras areas.

La regla aplicada fue: no copiar la estructura SEO completa si no hay evidencia de fallo. Copiar solo el patron que funciono:

1. agente breve para enrutar;
2. skill como procedimiento;
3. referencias largas bajo demanda;
4. canon solo si existe criterio transversal obligatorio y probado.

## Evidencia leida

### Agentes

Comando:

```powershell
rg -n "skill|\\.claude/skills|Bloqueos|Routing|Comunidad|crisis" .claude\agents\cro-*.md .claude\agents\web-*.md .claude\agents\social-*.md
```

Resultado operativo:

| Area | Agentes revisados | Estado |
|---|---:|---|
| CRO | 6 | Lider y especialistas enrutan a skills procedurales. |
| Web | 7 | Lider y especialistas tienen bloqueos de produccion y rutas a skills. |
| Social | 4 | Lider y especialistas existen; habia una ruta marcada como futura aunque el agente ya existe. |

### Skills

Comando:

```powershell
rg --files .claude\skills\page-cro .claude\skills\form-cro .claude\skills\web-feedback-loop .claude\skills\site-architecture .claude\skills\woocommerce-setup .claude\skills\social-content
```

Skills confirmadas:

- `page-cro`
- `form-cro`
- `web-feedback-loop`
- `site-architecture`
- `woocommerce-setup`
- `social-content`

Todas tienen `SKILL.md` y material de apoyo suficiente para operar como procedimiento.

### Contaminacion de clientes

Comando:

```powershell
rg -n -i "computer|chamberi|stramondo|cashier|chashier|bottega|shogun|gemma|venezuela" .claude\skills\page-cro .claude\skills\form-cro .claude\skills\web-feedback-loop .claude\skills\site-architecture .claude\skills\woocommerce-setup .claude\skills\social-content
```

Resultado: sin coincidencias en esas skills generales.

## Consulta a Claude

Se pidio a Claude revisar la evidencia de CRO/Web/Social contra la documentacion y el patron v2.

Conclusion de Claude:

- La estructura de skills es conforme.
- No conviene crear canon CRO/Web/Social todavia.
- Los agentes con `Read`, `Grep`, `Glob` son coherentes para diagnostico y recomendacion.
- Hay un ajuste real de bajo riesgo: `social-leader.md` marcaba `social-comunidad` como futuro aunque el agente existe.

## Decision

No crear nuevos canons para CRO, Web ni Social en esta fase.

Motivo: crear canon sin evidencia puede aumentar contexto, duplicar reglas y producir rigidez. Estas areas ya tienen skills procedurales; lo correcto es observar outputs reales y solo reforzar cuando aparezca un fallo repetido.

## Cambio aplicado

Archivo:

- `.claude/agents/social-leader.md`

Cambio:

```diff
- | Comunidad/crisis | futuro `social-comunidad`; fallback protocolo de mensajes |
+ | Comunidad/crisis | `social-comunidad`; fallback protocolo de mensajes |
```

## Estado

- [x] Inventario CRO/Web/Social revisado.
- [x] Skills base confirmadas.
- [x] Contaminacion de clientes buscada en skills generales.
- [x] Claude consultado.
- [x] Routing Social corregido.
- [ ] Observar outputs reales de CRO.
- [ ] Observar outputs reales de Web.
- [ ] Observar outputs reales de Social.

## Siguiente criterio

Si una de estas areas produce salidas flojas, repetitivas o inconsistentes, no crear canon automaticamente. Primero clasificar el problema:

| Sintoma | Solucion probable |
|---|---|
| Falta procedimiento | Mejorar `SKILL.md`. |
| Falta conocimiento largo | Crear `references/*.md`. |
| Falta formato | Crear `templates/*.md`. |
| Falta criterio transversal obligatorio | Crear canon. |
| Rodrigo necesita entrada simple | Crear command wrapper. |
