# Scripts

Solo deben entrar scripts revisados y saneados.

Requisitos:

- Sin secretos hardcodeados.
- Modo dry-run cuando pueda tocar produccion, gastar dinero o modificar datos.
- Logs sin credenciales.
- Parametros no interactivos.
- Registro en `registries/registro-artefactos.md`.

## Estado P3-005

Migrado ahora:

- `protocol_guard.py`: guard de cierre adaptado a rutas v2.
- `.mcp.example.json`: ejemplo local seguro; copiar a `.mcp.json` solo en local.
- `chrome_debug_helper.py`: diagnostico y lectura local de Chrome via CDP, sin guardar sesiones ni contenido.

Bloqueado o deferido:

- WordPress/WooCommerce legacy con credenciales historicas.
- Google OAuth, GBP, GA4, Drive, Meta Ads, Hostinger, Kling y WP REST.
- Scrapers y generadores de informes hasta tener limites, manifests y contratos de output.

## Comandos

```bash
python scripts/protocol_guard.py
python scripts/protocol_guard.py --all --strict
python scripts/chrome_debug_helper.py status
python scripts/chrome_debug_helper.py open
python scripts/chrome_debug_helper.py tabs
python scripts/chrome_debug_helper.py scrape-chatgpt
.\scripts\open_eselec_chrome.ps1
.\scripts\open_eselec_automation.ps1
```

El reporte se escribe en `outputs/system/protocol-guard-latest.md`, que no se versiona.

