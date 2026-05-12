# Protocolo de gestion de accesos sensibles y brechas

## Estado

- Version: 2.0
- Fecha: 2026-05-12
- Fuente legacy: `sistema/protocolos/gestion-secretos.md`
- Sistema destino: E-SELEC Agent System v2
- Estado: vigente

## Objetivo

Evitar que secretos, credenciales, tokens, sesiones, claves API o accesos delegados se filtren, se registren mal o se migren al sistema v2 de forma insegura.

Este protocolo gobierna:

- donde pueden vivir los secretos;
- como se clasifican;
- como se registran sin revelar valores;
- cuando se recomienda rotacion;
- que scripts quedan bloqueados;
- que debe pasar antes de usar conectores o MCP;
- como se cierra una tarea con accesos.

## Explicacion simple para Rodrigo

Un secreto es cualquier dato que permita entrar, leer, modificar, publicar, gastar dinero o actuar en nombre de E-SELEC o de un cliente.

Ejemplos: claves API, tokens, passwords de WordPress, claves WooCommerce, OAuth de Google, token de Meta Ads, Hostinger, Notion, Kling, webhooks o cookies de sesion.

La regla es: **el repo guarda instrucciones y codigo, no secretos**.

## Regla central

Ningun secreto real puede guardarse en:

- scripts;
- prompts;
- `CLAUDE.md`;
- `AGENTS.md`;
- `.claude/rules/`;
- `.claude/skills/`;
- `.claude/agents/`;
- `.claude/commands/`;
- `protocols/`;
- `planning/`;
- `registries/`;
- outputs;
- logs;
- manifests;
- documentos de cliente;
- mensajes finales.

Si un secreto aparece en una conversacion, archivo, output o script, se considera potencialmente expuesto y debe recomendarse rotacion.

## Alcance

Aplica a E-SELEC, clientes, agentes, scripts, MCP, conectores, automatizaciones y herramientas futuras.

Incluye:

- WordPress Application Passwords;
- WooCommerce Consumer Key / Consumer Secret;
- Hostinger API tokens;
- Anthropic/OpenAI/Claude keys;
- Google OAuth, GA4, GSC, GBP, Drive;
- Meta Ads tokens;
- Notion tokens;
- Toolsmine, SEMrush, Majestic;
- Kling API;
- webhooks;
- cookies;
- sesiones;
- `.env`;
- credentials files;
- token files;
- usuarios tecnicos;
- permisos de agentes.

Si una plataforma no esta listada pero permite leer datos, modificar sistemas, publicar, borrar, gastar dinero, cambiar DNS, tocar hosting o actuar en nombre de alguien, entra automaticamente en este protocolo.

## Clasificacion

| Nivel | Nombre | Significado | Ejemplos |
|---|---|---|---|
| S1 | Publico controlado | No es secreto, pero ayuda a identificar sistemas | dominios, URLs publicas, account IDs, slugs |
| S2 | Acceso limitado | Lectura o accion acotada sin impacto critico | API read-only, analitica solo lectura |
| S3 | Acceso funcional | Puede modificar sistemas reales o consumir recursos | WP application password, WooCommerce write key, Kling con creditos |
| S4 | Acceso critico | Puede afectar pagos, DNS, hosting, Ads, usuarios, datos personales o credenciales | OAuth con refresh token, Hostinger, Meta Ads con billing, admin tokens |

Si hay duda, clasificar en el nivel mas alto razonable.

## Ubicaciones permitidas

| Tipo | Permitido | Condicion |
|---|---|---|
| `.env` local | si | nunca se commitea |
| gestor externo de secretos | si | recomendado para accesos reales |
| token file fuera del repo | si | ruta privada documentada sin valor |
| variables de entorno de despliegue | si | nunca en codigo |
| GitHub repo | no | salvo `.env.example` sin valores |
| Google Drive/Notion/docs | no | no almacenar secretos completos |
| logs/outputs/manifests | no | solo metadatos |

## Registro obligatorio

Todo acceso S2/S3/S4 debe registrarse en:

```text
registries/registro-accesos.md
```

El registro debe contener:

```text
### YYYY-MM-DD - servicio - cliente/area
- Tipo de acceso:
- Nivel:
- Agente autorizado:
- Permisos aproximados:
- Valores registrados: ninguno
- Ubicacion segura esperada:
- Fecha de creacion:
- Rotacion recomendada:
- Estado:
- Riesgo si se filtra:
```

Nunca registrar valores reales.

## Reglas obligatorias

1. No escribir secretos completos en respuestas.
2. No confirmar secretos imprimiendo el valor.
3. No guardar secretos en scripts.
4. No subir `.env`.
5. No subir `credentials.json`, `token.json`, `client_secret*.json` ni archivos equivalentes.
6. No mezclar accesos de clientes con accesos internos de E-SELEC.
7. No reutilizar un token para varios agentes si se puede evitar.
8. Aplicar minimo privilegio.
9. Todo secreto compartido manualmente se considera temporal.
10. Todo secreto temporal debe tener recomendacion de rotacion.
11. Si un secreto aparece hardcodeado, el script queda bloqueado hasta saneamiento.
12. Si una accion con secretos toca produccion, aplicar tambien `protocols/activos-criticos.md`.
13. Si se crea/modifica archivo por la gestion de accesos, aplicar tambien `protocols/control-artefactos.md`.

## Flujo operativo

### 1. Antes de usar un acceso

Comprobar:

- servicio;
- cliente/area;
- nivel S1/S2/S3/S4;
- ubicacion segura esperada;
- si existe registro;
- si la accion toca produccion;
- si requiere Orden de Cambio.

### 2. Durante la tarea

- Leer valores solo desde ubicacion segura.
- No imprimir valores.
- No escribirlos en outputs.
- Redactar cualquier hallazgo.
- Usar dry-run si hay riesgo de escritura, gasto o produccion.

### 3. Si se detecta un secreto expuesto

Registrar metadatos:

- ruta;
- tipo probable;
- nivel;
- servicio afectado;
- estado;
- recomendacion de rotacion.

No copiar el valor.

### 4. Al cerrar

Incluir en el cierre:

```text
Accesos usados:
- servicio - tipo - nivel - estado

Secretos expuestos o detectados:
- ruta - tipo - severidad - valor no reproducido

Rotaciones recomendadas:
- servicio - motivo - prioridad

Acciones pendientes:
- revocar / rotar / limitar permisos / mover a .env / bloquear script
```

Si no se usaron ni detectaron secretos:

```text
No se usaron ni detectaron secretos en esta tarea.
```

## Politica para scripts legacy

Resultado de P0-002:

- scripts WordPress/WooCommerce con `WP_USER`/`WP_PASS` quedan bloqueados;
- conectores Google, Meta, Hostinger, WP, Kling y Notion no se migran hasta cumplir este protocolo;
- scripts S4 requieren saneamiento, dry-run si aplica y registro de acceso;
- ningun script que escriba `.env` entra al v2 sin aprobacion explicita.

Antes de migrar un script:

1. Escanear secretos.
2. Retirar hardcoding.
3. Mover configuracion a variables de entorno o gestor seguro.
4. Documentar variables en `.env.example` sin valores.
5. Agregar dry-run por defecto si puede escribir, gastar dinero o tocar produccion.
6. Redactar logs.
7. Registrar acceso en `registries/registro-accesos.md`.
8. Registrar artefacto en `registries/registro-artefactos.md`.
9. Probar sin credenciales reales o con mocks.

## Politica para MCP

No crear `.mcp.json` real si contiene secretos.

Permitido:

- `.mcp.example.json` sin valores;
- instrucciones para configurar MCP localmente;
- referencias a variables de entorno.

Prohibido:

- tokens MCP en repo;
- OAuth client secrets;
- URLs con credenciales embebidas;
- headers Authorization guardados.

## Patrones que deben bloquearse en hooks futuros

El hook P0-007 debe detectar como minimo:

- `WP_PASS =`
- `WP_USER =`
- `META_ACCESS_TOKEN =`
- `ANTHROPIC_API_KEY =`
- `OPENAI_API_KEY =`
- `NOTION_TOKEN =`
- `HOSTINGER_API_TOKEN =`
- `KLING_ACCESS_KEY_SECRET =`
- `ck_...`
- `cs_...`
- `Bearer <valor>`
- `credentials.json`
- `token.json`
- `client_secret*.json`
- `.env`

El hook debe reportar ruta y tipo, nunca valor.

## Coordinacion con crawler defensivo

Si un crawler detecta endpoints publicos, usuarios enumerables, APIs abiertas o archivos visibles:

1. evaluar si implica secreto interno;
2. revisar si hay usuarios tecnicos expuestos;
3. recomendar rotacion si procede;
4. abrir Orden de Cambio si requiere tocar produccion;
5. actualizar `registries/registro-accesos.md`.

## Criterio de exito

El protocolo funciona si cualquier persona puede responder:

- que accesos existen;
- que nivel de riesgo tienen;
- donde deberian vivir;
- que scripts estan bloqueados;
- que debe rotarse;
- que no debe subirse al repo;
- que hacer si aparece un secreto.

## Checklist de migracion de secretos

Antes de cerrar P0-003:

- `protocols/gestion-accesos.md` existe.
- `registries/registro-accesos.md` contiene entradas P0-002.
- `planning/backlog-migracion.md` marca P0-003 como hecho.
- P0-007 tiene requisitos claros para el hook de bloqueo.
- No hay valores secretos en el commit.
