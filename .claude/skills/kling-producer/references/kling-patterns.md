# Kling Patterns

## Modos

| Modo | Uso |
|---|---|
| image2video | animar una imagen de referencia |
| text2video | crear video solo desde texto |
| motion-control | transferir o controlar movimiento |
| lip-sync | sincronizar labios en rostro humano |

## Parametros minimos

- Modelo.
- Duracion: 5s para prueba, 10s para narrativa.
- Ratio: 9:16 redes verticales, 16:9 web/YouTube, 1:1 feed.
- Modo/calidad: standard para prueba, professional para final.
- Negative prompt.

## Prompt de imagen

Incluir sujeto, accion/postura, entorno, iluminacion, paleta, estilo, composicion y "no text in the image".

## Prompt de video

Describir eventos en orden:

1. camara o punto de vista;
2. sujeto;
3. movimiento principal;
4. elementos secundarios;
5. atmosfera;
6. estabilidad o intensidad.

## Negative prompt base

distorted, disfigured, blurry, low resolution, warp, deform, flickering, overexposed, text, watermark, logo, subtitle, extra limbs, morphing

## Riesgos

- Imagen de baja resolucion.
- Movimiento demasiado complejo.
- Texto o logos deformados.
- Coste alto por iteraciones.
- Derechos de imagen o marca.
