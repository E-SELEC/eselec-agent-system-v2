# Regla de activos criticos

Aplica cuando una tarea pueda afectar produccion, datos reales, fuentes de verdad, accesos, campanas, webs, WooCommerce, WordPress, tracking, scripts externos, MCP o integraciones.

## Regla central

Antes de tocar algo real, clasifica el riesgo.

## Niveles

- A: solo lectura.
- B: cambio reversible menor.
- C: cambio funcional.
- D: cambio irreversible o sensible.

## Obligaciones

- Nivel A: permitido si el usuario pidio diagnostico; no ejecutar cambios derivados.
- Nivel B: requiere Orden corta.
- Nivel C/D: requiere Orden completa y aprobacion explicita.

## Detente si

- aparece un activo no declarado;
- sube el riesgo;
- no hay rollback claro;
- hay contradiccion entre fuente viva y documentos;
- toca secretos, pagos, presupuestos, DNS, base de datos, restore o credenciales;
- la aprobacion no cubre el nuevo alcance.

## Relacion con otros protocolos

- Accesos: `protocols/gestion-accesos.md`
- Archivos: `protocols/control-artefactos.md`
- Cierre: `protocols/cierre-humano.md`

Fuente: `protocols/activos-criticos.md`
