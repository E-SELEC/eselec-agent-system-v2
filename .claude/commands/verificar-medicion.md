# verificar-medicion

Verifica si un cliente tiene datos suficientes antes de auditorias, informes, SEO, CRO o Ads.

## Uso

```text
/verificar-medicion [cliente] [alcance opcional] [--write]
```

Ejemplos:

```text
/verificar-medicion computer-chamberi SEO
/verificar-medicion stramondo-venezuela Meta Ads --write
/verificar-medicion cashier-bubble-tea informe mensual
```

## Workflow

1. Leer `.claude/skills/verificacion-medicion/SKILL.md`.
2. Identificar cliente, dominio, periodo y servicio afectado.
3. Leer:
   - `clients/[cliente]/context.md`
   - `clients/[cliente]/log.md`
   - `clients/[cliente]/mensajes.md`
   - `clients/[cliente]/memory.md` si existe
   - `clients/[cliente]/tasks.md` si existe
4. Definir fuentes necesarias segun el alcance:
   - SEO: GSC, SEMrush, revision tecnica/render.
   - Local: GBP, GSC, sitio.
   - Informe: fuentes de todos los servicios activos.
   - CRO: GA4 eventos/conversiones y pagina.
   - Ads: plataforma Ads, pixel/conversion y landing.
5. Comprobar solo lectura:
   - fuente existe;
   - coincide con cliente;
   - rango de fechas;
   - evidencia minima;
   - limitaciones.
6. Clasificar Nivel 0/1/2/3.
7. Entregar resultado usando `templates/informe-medicion.md`.

## Escritura opcional

Por defecto, responder en chat.

Solo si Rodrigo usa `--write`, guardar:

```text
clients/[cliente]/outputs/medicion/verificacion-medicion-YYYY-MM-DD.md
```

Despues de guardar:

- actualizar `clients/[cliente]/outputs/manifest.md`;
- registrar en `clients/[cliente]/log.md`;
- aplicar `protocols/control-artefactos.md`.

## Reglas

- No pedir ni mostrar secretos.
- No modificar GA4, GSC, GBP, Ads, CMS, etiquetas, conversiones ni fuentes vivas.
- No afirmar rendimiento, trafico, ranking o conversion sin fuente verificada o sin marcar parcial.
- Si la verificacion exige cambios reales, detener y aplicar `protocols/activos-criticos.md`.

## Criterio de exito

El comando termina bien cuando deja claro:

- nivel de medicion;
- fuentes verificadas;
- fuentes faltantes;
- que conclusiones quedan permitidas;
- si el siguiente output puede ser final, parcial, orientativo o queda bloqueado.
