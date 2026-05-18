# Lectura del sistema completo previa a reestructuracion SEO

Fecha: 2026-05-11
Estado: version operativa anonimizada para `seo-canon`

## Por que existe esta version

El archivo historico original contenia nombres de clientes reales del sistema
legacy. Ese archivo ya no vive dentro del canon operativo para evitar que una
skill general aprenda desde casos concretos.

La version historica completa se conserva fuera del canon en:

```text
legacy/docente-seo-historico-con-clientes/2026-05-11-lectura-sistema-completo-previa-reestructuracion.md
```

## Decision inicial

El Agente SEO no debe recibir cambios estructurales hasta entender primero como
funciona el sistema completo.

La tarea no es meter mas informacion SEO en prompts. La tarea correcta es
entender:

- quien decide;
- quien ejecuta;
- que archivo es fuente de verdad;
- que protocolo protege el sistema;
- que conocimiento SEO vive en cada capa;
- que informacion esta duplicada;
- que informacion esta obsoleta;
- que cambio puede romper clientes, medicion, URLs, webs o autoridad.

## Alcance que debe leerse antes de reestructurar

Antes de tocar agentes SEO, revisar las capas relevantes sin convertir ningun
cliente concreto en regla general:

- archivos raiz del sistema;
- protocolos globales;
- indices y registros;
- contexto interno de agencia;
- agentes y lideres;
- plantillas de cliente y estructura de memoria;
- skills SEO y skills relacionadas;
- scripts y conectores;
- outputs historicos solo como evidencia, no como verdad actual.

## Regla operativa

Los clientes reales viven en `clients/[cliente]/`.

El canon SEO solo guarda:

- criterios;
- procedimientos;
- patrones anonimos;
- mapas de lectura;
- reglas de decision.

No uses nombres de clientes, rutas de outputs reales o conversaciones reales
como ejemplo obligatorio dentro de una skill general.

## Preguntas de control

Antes de cambiar agentes SEO, responde:

1. Que problema real corrige este cambio?
2. Que pieza decide y que pieza ejecuta?
3. Que fuente oficial o canonica lo respalda?
4. Que evidencia del repo demuestra que el problema existe?
5. Que riesgo operativo crea?
6. Donde queda registrada la trazabilidad?

## Criterio final

Una reestructuracion SEO solo esta alineada si mejora conducta verificable sin
mezclar memoria de cliente con reglas generales del sistema.
