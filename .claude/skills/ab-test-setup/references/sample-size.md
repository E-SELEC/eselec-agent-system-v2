# Sample size y duracion

## Inputs minimos

- baseline conversion rate;
- trafico diario elegible;
- metrica primaria;
- MDE: mejora minima que vale la pena detectar;
- numero de variantes;
- porcentaje de trafico expuesto.

## Reglas practicas

- Si no hay baseline, no hay test listo.
- Si el test tardaria mas de 8 semanas, reconsiderar.
- Ejecutar al menos 1 semana completa.
- En B2B, cubrir ciclos laborables.
- No dividir trafico en demasiadas variantes.

## Decision rapida

| Situacion | Recomendacion |
|---|---|
| trafico bajo + cambio obvio | cambio directo con medicion antes/despues |
| trafico medio + riesgo bajo | A/B simple |
| trafico alto + varias opciones | A/B/n limitado |
| sin tracking | primero analytics-tracking |
| impacto pequeno | no testear |

## Formula de duracion

```text
dias = (muestra_por_variante * variantes) / (trafico_diario * exposicion)
```

Si no puedes calcular muestra exacta, marca AB1/AB2 y deja el calculo pendiente.
