# auditar-woocommerce

Audita una tienda WooCommerce y prepara plan seguro de setup o go-live.

## Uso

```text
/auditar-woocommerce [cliente] [url/opcional] [--write]
```

## Workflow

1. Leer `.claude/skills/woocommerce-setup/SKILL.md`.
2. Leer contexto, log, mensajes y protocolos.
3. Confirmar modo: auditoria, guia, setup o go-live.
4. Entregar usando `templates/woocommerce-audit.md`.

## Reglas

- No tocar pagos, envios, impuestos, productos ni paginas sin Orden de Cambio.
- No mostrar ni guardar secretos.
- Cambios reales requieren re-auditoria posterior.
