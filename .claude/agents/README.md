# Agentes Claude

Aqui viviran los subagents nativos cuando se migren.

No migrar prompts antiguos en bloque. Cada agente debe tener:

- Proposito unico.
- Herramientas necesarias.
- Inputs esperados.
- Criterios de parada.
- Formato de salida.
- Riesgos y permisos.

Agentes activos:

- `arquitecto-migracion-claude`: audita y planifica la migracion legacy -> v2.
- `docente`: convierte correcciones y fallos de calidad en criterio operativo examinable.
- `leader-clientes`: orquesta trabajo de clientes, prioriza y elige skills/subagents sin ejecutar produccion.
- `leader-agencia`: orquesta trabajo interno de E-SELEC sin mezclarlo con clientes.

