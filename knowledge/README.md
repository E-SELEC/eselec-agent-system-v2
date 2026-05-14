# Knowledge

Esta carpeta ordena fuentes externas, documentacion, aprendizajes y material de referencia que todavia no pertenece a un cliente, protocolo, skill, agente o entregable.

No es un vertedero. Es una antesala de clasificacion.

## Para que existe

Cuando entra informacion nueva, el sistema debe decidir:

- si es fuente oficial;
- si es evidencia de cliente;
- si es criterio operativo;
- si debe convertirse en protocolo, skill, agente, command o memoria;
- si solo debe quedar como referencia;
- si no debe entrar por contener secretos, PII, ruido o datos obsoletos.

## Estructura

| Ruta | Uso |
|---|---|
| `knowledge/claude-code/` | Indices y notas sobre documentacion oficial Claude Code. |
| `knowledge/inbox/` | Entrada temporal para informacion pendiente de clasificar. |
| `knowledge/decisiones/` | Decisiones de clasificacion cuando una fuente cambia el sistema. |

## Regla central

Guardar el minimo util:

```text
fuente -> resumen saneado -> decision -> destino -> registro
```

No copiar documentacion completa si basta con URL, resumen, fecha y decision.

## Flujo recomendado

1. Usar `/ingestar-conocimiento [fuente o ruta]`.
2. Clasificar la informacion.
3. Decidir destino.
4. Crear o actualizar solo el archivo necesario.
5. Registrar en `registries/registro-fuentes.md`.
6. Si se modifica estructura, actualizar `registries/registro-artefactos.md`.
7. Ejecutar `python scripts/protocol_guard.py --no-report`.

## Destinos correctos

| Tipo de informacion | Destino |
|---|---|
| URL oficial o documentacion externa | `knowledge/[fuente]/` + `registries/registro-fuentes.md` |
| Regla obligatoria | `protocols/` o `.claude/rules/` |
| Procedimiento reutilizable | `.claude/skills/<skill>/SKILL.md` |
| Rol o criterio de delegacion | `.claude/agents/*.md` |
| Comando repetible | `.claude/commands/*.md` |
| Preferencia de Rodrigo | `agency/preferencias-rodrigo.md` previa aprobacion |
| Memoria de cliente | `clients/[cliente]/memory.md` |
| Evidencia de datos | `clients/[cliente]/outputs/evidencia-*.md` |
| Output pesado | Drive u output local ignorado; registrar manifest |
| Historico no operativo | `legacy/` |

## No guardar aqui

- secretos;
- tokens;
- credenciales;
- dumps completos;
- archivos pesados;
- datos personales;
- capturas sin proposito;
- outputs finales de cliente;
- informacion no clasificada por comodidad.
