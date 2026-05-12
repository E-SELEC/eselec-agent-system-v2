# Registro de accesos

Este registro no contiene secretos reales. Solo metadatos, nivel de riesgo, ubicacion segura esperada y rotacion recomendada.

## Niveles

- S1: bajo riesgo, sin datos sensibles.
- S2: acceso limitado o lectura parcial.
- S3: acceso operativo con impacto en cliente/sistema.
- S4: acceso critico, produccion, pagos, datos sensibles o administracion.

## Entradas

### 2026-05-12 - Scripts legacy WordPress/WooCommerce con credenciales hardcodeadas
- Tipo de acceso: credenciales tecnicas detectadas por nombre de variable en scripts legacy.
- Nivel: S4
- Rutas afectadas: `scripts/deploy_bottega_plugin.py`, `scripts/woo_activacion_bottega.py`, `scripts/woo_debug.py`, `scripts/woo_paginas_legales.py`
- Valores registrados: ninguno.
- Estado: bloqueado para migracion.
- Ubicacion segura esperada: `.env` local o gestor externo, nunca codigo.
- Rotacion recomendada: alta si esas credenciales siguen activas.
- Riesgo si se filtra: modificacion de contenido, tienda, configuracion o datos WordPress/WooCommerce.

### 2026-05-12 - Conectores legacy con OAuth/tokens/API externas
- Tipo de acceso: scripts que usan OAuth, tokens, Authorization headers o servicios externos.
- Nivel: S3/S4 segun servicio.
- Rutas afectadas: `scripts/drive_connector.py`, `scripts/ga4_connector.py`, `scripts/gbp_setup_computer_chamberi.py`, `scripts/get_gbp_account_id.py`, `scripts/hostinger_connector.py`, `scripts/meta_ads_connector.py`, `scripts/refresh_meta_token.py`, `scripts/wp_connector.py`, `scripts/kling_connector.py`, `scripts/notion_connector.py`, `scripts/semrush_login.py`
- Valores registrados: ninguno.
- Estado: no migrar hasta `protocols/gestion-secretos.md`.
- Ubicacion segura esperada: variables de entorno locales, gestor externo o token file fuera del repo segun servicio.
- Rotacion recomendada: revisar por servicio antes de activarlos en v2.
- Riesgo si se filtra: acceso a datos de clientes, produccion, Ads, Drive, GBP, Hostinger, WordPress/WooCommerce o consumo de creditos.

