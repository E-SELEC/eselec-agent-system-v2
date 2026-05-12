# Mensajes Agencia

## Formato

```text
---
DE:
PARA:
TIPO: alerta | oportunidad | dependencia | info
FECHA: YYYY-MM-DD
ESTADO: pendiente | leido | ejecutado
MENSAJE:
ACCION SUGERIDA:
---
```

## Pendientes migrados

---
DE: Arquitecto
PARA: Rodrigo / Lider Agencia
TIPO: alerta
FECHA: 2026-05-12
ESTADO: pendiente
MENSAJE: Se detectaron scripts historicos WordPress/WooCommerce y conectores legacy que no deben migrarse sin saneamiento. No se reproducen valores ni secretos en v2.
ACCION SUGERIDA: Antes de migrar conectores, ejecutar auditoria de scripts, mover secretos a entorno local/gestor externo y rotar accesos si procede.
---

---
DE: Agente SEO Organico
PARA: Agencia / Captacion
TIPO: oportunidad
FECHA: 2026-03-28
ESTADO: pendiente
MENSAJE: Shogun Motors podria servir como caso historico de reputacion local si se recuperan resultados medibles y permiso de uso.
ACCION SUGERIDA: No usar como caso publico hasta validar estado contractual, permiso y datos.
---

---
DE: Arquitecto
PARA: Lider Agencia
TIPO: dependencia
FECHA: 2026-05-12
ESTADO: pendiente
MENSAJE: SEMrush aparece como fuente critica para SEO, pero su acceso/conector legacy debe tratarse como sensible.
ACCION SUGERIDA: Usar `ingesta-evidencia` con exports saneados antes de migrar cualquier automatizacion SEMrush.
---

