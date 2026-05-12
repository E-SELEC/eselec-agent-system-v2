# Regla de gestion de accesos sensibles

Aplica siempre que una tarea mencione o use credenciales, tokens, APIs, `.env`, OAuth, cookies, sesiones, webhooks, conectores, scripts o servicios externos.

## Regla central

El repositorio guarda sistema, no secretos.

Nunca escribir valores reales de secretos en:

- codigo;
- prompts;
- logs;
- outputs;
- registros;
- manifests;
- respuestas finales;
- documentos de cliente.

## Antes de actuar

1. Clasifica el acceso como S1/S2/S3/S4.
2. Comprueba si existe registro en `registries/registro-accesos.md`.
3. Si toca produccion, aplica `protocols/activos-criticos.md`.
4. Si modifica archivos, aplica `protocols/control-artefactos.md`.

## Si detectas un secreto

- No lo copies.
- No lo resumas parcialmente salvo necesidad extrema.
- Registra ruta, tipo y severidad.
- Recomienda rotacion.
- Bloquea migracion del archivo hasta saneamiento.

## Scripts

No migrar scripts S3/S4 hasta que:

- no tengan secretos hardcodeados;
- usen variables de entorno o gestor externo;
- tengan dry-run si pueden escribir/gastar/tocar produccion;
- tengan logs redactados;
- esten registrados.

Fuente: `protocols/gestion-accesos.md`
