# Cliente: Computer Chamberi

## Estado

- Cliente piloto v2: si
- Fecha de migracion minima: 2026-05-12
- Fuente legacy: `clients/computer-chamberi/`
- Nivel de datos: parcial fuerte
- Riesgo operativo: medio si se toca produccion; bajo para auditoria

## Datos basicos

- Negocio: tienda local de informatica y reparacion en Chamberi, Madrid.
- Web: `https://www.computerchamberi.com/`
- Mercado: local Madrid + busquedas en ingles para publico internacional.
- Servicios principales: reparacion de ordenadores, portatiles, moviles, tablets, consolas, relojes inteligentes y camaras de accion.

## Servicios E-SELEC activos

| Servicio | Estado | Nota |
|---|---|---|
| SEO Local | activo | GBP fuerte y trabajo local previo. |
| SEO Organico | activo | Hay auditorias recientes y oportunidades de CTR/contenido. |
| SEO Tecnico | basico | Pendiente profundizar antes de cambios. |
| Desarrollo Web | activo | Web en ingles casi completa, UX/UI en progreso. |
| CRO | pendiente | Recomendado despues de medicion y paginas clave. |

## Datos SEO resumidos

- Marca posicionada: domina busquedas de marca.
- GSC historico: trafico real relevante y CTR bajo.
- Oportunidad principal: optimizar CTR en paginas con muchas impresiones.
- Nichos detectados: Amazfit, Xiaomi y GoPro tienen demanda sin paginas dedicadas suficientes.
- Autoridad: backlinks numerosos pero calidad baja segun legacy.
- GBP: activo fuerte con muchas reseñas y alta valoracion.
- Instagram: canal debil; no priorizar salvo decision explicita.

## Fuentes y accesos

- GSC: disponible via perfil Chrome E-SELEC segun legacy.
- GBP: disponible via perfil Chrome E-SELEC segun legacy.
- GA4: indicado como operativo en mensaje legacy, pero debe verificarse de forma segura antes de usarlo.
- CMS/hosting: pendiente de confirmar antes de cualquier cambio tecnico.

No hay secretos ni credenciales en este archivo.

## Prioridades vigentes

1. Verificar medicion: GA4, eventos, conversiones y linea base.
2. Ejecutar diagnostico SEO con `seo-audit` v2 usando datos disponibles.
3. Priorizar optimizacion de CTR en paginas con alto volumen de impresiones.
4. Evaluar creacion de paginas dedicadas Amazfit/Xiaomi/GoPro.
5. Activar CRO solo despues de tener medicion minima y paginas prioritarias claras.

## Restricciones

- No tocar produccion durante el piloto.
- No ejecutar scripts con credenciales.
- No modificar web, GBP, GSC, GA4 ni CMS sin Orden de Cambio.
- No migrar outputs historicos completos al repo v2.

## Notas para agentes

- Usar `leader-clientes` como entrada.
- Usar `client-audit` para foto general.
- Usar `seo-audit` para diagnostico SEO.
- Marcar cualquier diagnostico como parcial si no se consultan GSC/SEMrush/GA4 en vivo.
- Si Rodrigo corrige el output, activar `docente`.

