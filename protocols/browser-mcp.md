# Protocolo Browser MCP

## Proposito

Permitir que Claude Code use un navegador de forma controlada mediante Playwright MCP, especialmente cuando Rodrigo quiera inspeccionar paginas web, interfaces autenticadas, dashboards o flujos visuales sin copiar datos manualmente al chat.

Este protocolo no crea un navegador oculto ni una forma de evadir restricciones. El navegador debe ser visible, iniciado por Rodrigo o bajo su control, y cualquier login, CAPTCHA, permiso sensible o accion irreversible debe resolverse manualmente.

## Canal recomendado

El servidor recomendado es el MCP oficial de Playwright:

```json
"playwright-chrome": {
  "command": "npx",
  "args": [
    "-y",
    "@playwright/mcp@latest",
    "--cdp-endpoint=http://localhost:9222"
  ]
}
```

La configuracion versionable vive como ejemplo en `.mcp.example.json`. El archivo `.mcp.json` local puede existir en la maquina de Rodrigo, pero esta ignorado por git y no debe contener secretos.

## Como iniciar Chrome para MCP

Opcion recomendada con helper local:

```powershell
python scripts/chrome_debug_helper.py status
python scripts/chrome_debug_helper.py open
```

Accesos rapidos desde PowerShell:

```powershell
.\scripts\open_eselec_chrome.ps1       # perfil real E-SELEC
.\scripts\open_eselec_automation.ps1   # perfil automatizable CDP
```

`open` usa un perfil CDP separado por defecto en:

```powershell
%LOCALAPPDATA%\ESELEC\chrome-debug-profile
```

Esto es necesario porque Chrome 136+ ya no permite que `--remote-debugging-port` controle el perfil real/default de Chrome. Para usar ChatGPT, Google, Meta u otra herramienta autenticada desde ese perfil CDP, inicia sesion una vez dentro de esa ventana separada.

Opcion manual:

1. Usa un perfil separado, no el perfil real/default de Chrome.
2. Abre PowerShell.
3. Ejecuta:

```powershell
Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList @("--remote-debugging-port=9222","--user-data-dir=$env:LOCALAPPDATA\ESELEC\chrome-debug-profile")
```

4. Entra manualmente a las paginas necesarias.
5. Inicia Claude Code desde el repo y revisa `/mcp`.
6. Si Claude ya estaba abierto, cierralo y abrelo de nuevo para que lea `.mcp.json`.

Para listar pestanas o extraer el texto visible de ChatGPT desde Codex:

```powershell
python scripts/chrome_debug_helper.py tabs
python scripts/chrome_debug_helper.py scrape-chatgpt
```

Si quieres trabajar exactamente sobre tu Chrome real E-SELEC, usa la integracion nativa de Claude en Chrome (`claude --chrome` o `/chrome`) o Playwright MCP con extension. CDP/Playwright CLI debe usar perfil separado.

## Uso permitido

- Leer URL, titulo, texto visible, estado visual, consola y DOM cuando la tarea lo requiera.
- Tomar screenshots para diagnostico o verificacion.
- Probar flujos locales o sitios propios bajo control de E-SELEC.
- Revisar dashboards autenticados cuando Rodrigo ya tenga sesion abierta y haya dado permiso explicito.

## Uso restringido

- No usar para saltar detecciones anti-bot, CAPTCHAs, bloqueos de seguridad o limites de plataformas.
- No guardar cookies, tokens, storage state, screenshots sensibles o HTML privado dentro del repo sin necesidad, registro y aprobacion.
- No modificar webs, anuncios, CRM, documentos, formularios reales o cuentas de cliente sin aplicar `protocols/activos-criticos.md`.
- No usar el navegador como sustituto de conectores vivos cuando exista MCP/API oficial estable para la misma fuente.

## Regla operativa

Antes de usar Browser MCP en una tarea, declarar:

```text
Browser MCP: lectura | diagnostico | prueba local | accion sensible
Pagina/sistema:
Cuenta o cliente afectado:
Datos que se van a leer:
Datos que se podrian escribir:
Permiso requerido:
```

Si la clasificacion es `accion sensible`, abrir Orden de Cambio antes de ejecutar.

## Alternativas

- `claude --chrome` o `/chrome`: preferible cuando se quiera usar la integracion oficial de Claude con la extension de Chrome y sesiones visibles.
- `@playwright/mcp@latest` sin `--cdp-endpoint`: preferible para pruebas aisladas donde no se necesite la sesion real de Chrome.
- Conector MCP/API especifico: preferible para Notion, Drive, GitHub, Gmail, GA4, GSC o plataformas con integracion estructurada.
