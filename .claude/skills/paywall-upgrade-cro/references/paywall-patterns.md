# Patrones Paywall Upgrade CRO

## Tipos

| Tipo | Momento | Riesgo |
|---|---|---|
| Feature gate | usuario intenta usar funcion premium | frustracion si no se entiende valor |
| Usage limit | llega a limite de plan | bloqueo abrupto si no hubo aviso |
| Trial expiration | antes o despues de fin de prueba | perdida de confianza si cambia acceso sin explicar |
| Upsell modal | despues de logro o uso recurrente | fatiga si aparece demasiado |
| In-app pricing | dentro del producto | confusion si difiere de pricing publico |

## Componentes

- headline con beneficio;
- que desbloquea;
- por que aparece ahora;
- comparacion clara de planes;
- precio y periodo;
- CTA de upgrade;
- escape hatch visible;
- nota sobre cambios en datos/acceso;
- soporte o ayuda si hay dudas.

## Guardrails

- churn post-upgrade;
- refunds;
- tickets de soporte;
- drop-off en flujo critico;
- downgrade/cancel;
- revenue por usuario;
- conversion por segmento.

## Medicion minima

- paywall impression;
- CTA click;
- checkout start;
- purchase/upgrade;
- payment failure;
- dismiss/not now;
- feature used after upgrade;
- churn/refund after upgrade.
