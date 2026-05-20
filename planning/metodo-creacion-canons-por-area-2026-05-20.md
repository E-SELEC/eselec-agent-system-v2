# Metodo de creacion de manuales operativos y canons por area

Fecha: 2026-05-20

Estado: metodo aprobado para preparar conversaciones fuente. No crea canons nuevos.

## Para que existe

Este documento fija el metodo que produjo el manual operativo SEO y la estructura posterior de agentes SEO para poder replicar ese resultado en otras areas de E-SELEC sin crear canons debiles, resumidos o contaminados por clientes.

La conclusion principal es simple: el sistema SEO no nacio de pedir "crea un canon". Nacio de una conversacion formativa progresiva que produjo un manual de uso operativo; despues ese manual se adapto a la estructura actual de agentes, skills, referencias y canon SEO.

## Principio rector

Primero se desarrolla una conversacion fuente por area. Esa conversacion debe producir un manual operativo de uso. Despues se evalua que piezas merecen convertirse en canon, skill, referencia, checklist, template o agente.

No se crea un canon nuevo hasta cumplir `.claude/rules/canon-admision.md`.

## Correcciones obligatorias de Rodrigo

1. Los links deben venir de la fuente propia de la herramienta o plataforma cuando la herramienta exista. Si el modulo trata Meta, las URLs deben venir de Meta. Si trata Google Ads, GA4, GSC o GTM, las URLs deben venir de Google. Fuentes externas solo se aceptan como apoyo, no como base principal.
2. El resultado inicial de estas conversaciones es un manual de uso operativo, no un canon directo.
3. La estructura que hoy tienen los agentes SEO nacio de adaptar el buen funcionamiento del Docente SEO al sistema v2. Antes de replicar a otras areas, hay que verificar si esa migracion SEO esta completa y documentar cual es exactamente el patron que funciono.

## Metodo que funciono en SEO

### 1. Jerarquia actual del area

Rodrigo empezo pidiendo una explicacion actualizada de la disciplina y sus jerarquias reales.

Funcion:

- obliga a ordenar el area antes de ejecutar;
- evita listas genericas de tareas;
- separa fundamentos, prioridades, riesgos y medicion;
- permite detectar que cambia entre proyectos nuevos y proyectos existentes.

Prompt adaptable:

```text
Hablame de [AREA] y sus jerarquias actualizadas al dia de hoy.
```

### 2. Verificacion profesional profunda

Rodrigo subio la exigencia: el modelo debia actuar como profesional experto, verificar lo escrito, corregir, profundizar y evitar informacion superficial.

Prompt base original adaptado:

```text
Imagina que eres un profesional experto en [AREA]. Tu rol es verificar que esto que se escribio sea asi como tal. Verificaras la informacion y profundizaras hasta explicar cada punto con el maximo detalle necesario.

El contexto es simple: debes dar informacion correcta, sin canibalizar, siendo ordenado, coherente y explicito. No tienes problema en extenderte y dar todo tu conocimiento al respecto. Al contrario, eres alguien con mucha experiencia, adaptado a estos tiempos, con larga trayectoria y una empresa que te respalda.
```

Funcion:

- convierte una respuesta inicial en auditoria profesional;
- obliga a corregir enfoque si estaba incompleto;
- reduce respuestas complacientes;
- pide criterio, no solo informacion.

### 3. Alcance nuevo vs existente

Rodrigo corrigio el alcance para que el sistema sirviera tanto para proyectos nuevos como para proyectos ya creados.

Prompt adaptable:

```text
Para un proyecto nuevo y tambien para uno existente.
```

Funcion:

- evita manuales que solo sirven para creacion desde cero;
- fuerza diferencias de prioridad, riesgo y diagnostico;
- hace que el material sea reutilizable para clientes reales sin mezclar datos de clientes.

### 4. Formacion operativa para relevo

Rodrigo no queria teoria. Queria formar personas nuevas que pudieran ejecutar trabajo real dentro de la empresa.

Prompt base original adaptado:

```text
Esta muy bien hecho, mas aun no es suficiente. Ahora, de manera organizada, coherente, eficaz y detallada, explicaras a alguien que no tiene conocimiento de [AREA] como se supone que debe ejecutar las tareas que mencionas en cada punto.

Recuerda que hablas con alguien que no conoce nada de [AREA] y debes educarlo para abarcar estas tareas. Los detalles del proceso son claves porque estas personas se encargaran de aplicar tus conocimientos en tu misma empresa; son tu generacion de relevo.

Debes cubrir proyectos nuevos y proyectos ya creados. No tienes problema en extenderte, porque la reputacion de la empresa queda en manos de estas nuevas personas. Pero no debes sonar redundante, no debes canibalizar y no debes rellenar: cada palabra vale oro.
```

Funcion:

- transforma conocimiento en procedimiento;
- obliga a explicar como se ejecuta, no solo que existe;
- introduce criterio junior/senior;
- hace que el area tenga una columna vertebral formativa.

### 5. Fuentes y links de alto valor

Rodrigo exigio links utiles, actuales y de calidad. No cualquier fuente.

Prompt adaptable:

```text
En cada punto anadiras los 5 links que mas aporten valor y conocimiento a esta generacion de relevo. No utilizaras cualquier link: debes corroborar que usas fuentes top, solidas, actualizadas o funcionales con la actualidad.

Cuando el modulo trate una herramienta o plataforma concreta, los links principales deben venir de su fuente propia u oficial. Ejemplos: Meta desde Meta, Google Ads desde Google, GA4 desde Google, Google Search Console desde Google, WooCommerce desde WooCommerce, WordPress desde WordPress, Shopify desde Shopify. Fuentes externas solo pueden complementar, no reemplazar la fuente primaria.
```

Funcion:

- evita manuales basados en opinion;
- obliga a conectar cada modulo con fuentes;
- permite auditoria posterior de calidad;
- crea una base para referencias bajo demanda.
- impide que una herramienta sea explicada desde blogs secundarios cuando existe documentacion original.

### 6. Herramientas del area, una por una

Despues del marco general, Rodrigo bajo la teoria a herramientas reales.

Prompt base original adaptado:

```text
Me gusta, pero no estas explicando como deben utilizar [HERRAMIENTA]. Empecemos por [HERRAMIENTA]. Utiliza links de la fuente propia u oficial de esa herramienta para dotar profundamente a tu personal.

Considera todo lo que has ensenado previamente:
- marco maestro de [AREA];
- estructura completa profesional;
- ejecucion para formar a alguien nuevo;
- diferencia entre proyecto nuevo y proyecto existente;
- criterio profesional y operativo.
```

Funcion:

- convierte el canon en capacidad operativa;
- evita que las herramientas queden como menciones decorativas;
- crea modulos profundos y cerrados;
- permite formar personas sobre procesos reales.

### 7. Modulos cerrados y fidelidad documental

Rodrigo exigio que los documentos finales mantuvieran el contenido exacto, mismo orden y sin resumen.

Regla adaptable:

```text
El documento final debe conservar exactamente la informacion generada: mismas palabras, mismo orden, sin resumen, sin reescritura, sin recortes y sin mejoras de estilo. Solo puedes anadir estructura minima de modulo e indice para navegacion.
```

Funcion:

- protege el aprendizaje original;
- evita que una segunda capa de resumen rebaje el criterio;
- permite que Codex integre despues sin perder origen.

## Paso cero antes de replicar a otras areas

Antes de desarrollar SEM, Reports, CRO, Web o Social, hay que auditar si SEO quedo completamente migrado.

La auditoria debe responder:

- que parte del Docente SEO antiguo se convirtio en manual operativo;
- que parte vive hoy como canon SEO;
- que parte vive como skill;
- que parte vive como referencia bajo demanda;
- que parte vive como checklist o template;
- que agentes SEO usan esa estructura;
- que piezas faltan por migrar;
- si hay instrucciones SEO duplicadas, incompletas o contaminadas por clientes.

La razon es importante: los demas agentes deben funcionar con el mismo patron que hizo que SEO funcionara, no con una version inventada desde cero.

## Orden recomendado de areas

No todas las areas deben convertirse en canon al mismo tiempo.

| Orden | Area | Motivo |
|---|---|---|
| 0 | SEO | Auditar si la migracion Docente SEO -> manual operativo -> canon/skills/agentes esta completa. |
| 1 | SEM / Paid Ads | Alto impacto economico; necesita reglas duras de presupuesto, tracking, creatividades y optimizacion. |
| 2 | CRO | Mucho criterio implicito: que cambiar, cuando testear, cuando medir y cuando no tocar. |
| 3 | Reports / Analytics | Necesario para convertir datos en decisiones; ya tiene skill fuerte, se refuerza si los outputs fallan. |
| 4 | Web / WooCommerce | Toca produccion; requiere protocolo fuerte antes de convertirse en canon. |
| 5 | Social / Content | Puede empezar como skill reforzada; solo merece canon si desarrolla criterio profundo de marca, formatos y medicion. |

Nota de revision: Claude confirmo SEM primero por riesgo economico. Tras auditar el estado real de las areas en `planning/matriz-estado-areas-v2-2026-05-20.md`, CRO queda segundo porque contiene mas criterio implicito sin capa estable; Reports se mantiene como skill fuerte y se refuerza cuando falle un output real.

## Conversaciones en ChatGPT

Claude debe crear una conversacion separada por area dentro del proyecto ChatGPT `Sistema de agentes`.

Nombres sugeridos:

- `Manual operativo CRO - conversacion fuente`
- `Manual operativo SEM Paid Ads - conversacion fuente`
- `Manual operativo Reports Analytics - conversacion fuente`
- `Manual operativo Web WooCommerce - conversacion fuente`
- `Manual operativo Social Content - conversacion fuente`

Cada conversacion debe comenzar con el area completa, no con una herramienta.

## Prompt 0: contrato permanente de la conversacion

Antes de pedir jerarquias, Claude debe fijar el contrato de calidad dentro de ChatGPT.

```text
Esta conversacion es una fuente formativa para E-SELEC. No estas creando el canon final ni escribiendo en el repositorio.

Tu trabajo es desarrollar un manual operativo profundo sobre [AREA] para formar criterio, procesos y capacidad de ejecucion.

Reglas permanentes:
- No inventes datos.
- Si usas ejemplos ficticios, etiquetalos como ficticios.
- No uses clientes reales de E-SELEC como ejemplos.
- No mezcles esta area con otras salvo cuando haya dependencia clara.
- No resumas ni recortes modulos cerrados.
- Toda recomendacion debe distinguir entre informacion, criterio, proceso y validacion.
- Cuando cites fuentes de herramientas o plataformas, usa primero la fuente propia u oficial. Usa referencias externas solo como apoyo.
- Si algo no esta verificado, dilo como pendiente de verificacion.
```

## Brief para Claude antes de abrir cada conversacion

```text
Vas a desarrollar una conversacion fuente para E-SELEC, no un canon final.

Objetivo: reproducir el metodo que funciono con SEO para construir un manual operativo profundo sobre [AREA].

Reglas:
- No crees archivos dentro del repo.
- No uses clientes reales como ejemplos operativos.
- No mezcles areas.
- No resumas el resultado final.
- No conviertas esto en canon todavia.
- Usa fuentes propias u oficiales cuando trates herramientas concretas. Usa fuentes externas de maxima calidad solo como complemento.
- Mantener separadas: jerarquia, criterio, ejecucion, herramientas, checklists y fuentes.
- Explica siempre diferencias entre proyecto nuevo y proyecto existente cuando aplique.
- Si usas ejemplos ficticios, indicalo como ficticio.
- Trabaja en espanol claro, profesional, ordenado y formativo.

Al terminar, entrega:
1. indice de modulos desarrollados;
2. fuentes principales usadas, separando fuente propia/oficial y fuentes externas de apoyo;
3. puntos que parecen candidatos a canon;
4. puntos que solo deberian ser skill, checklist, template o referencia;
5. dudas o riesgos antes de integrar a E-SELEC v2.
```

## Secuencia minima por area

0. Contrato permanente de la conversacion.
1. Jerarquias actuales del area.
2. Verificacion profesional profunda.
3. Diferencia entre proyecto nuevo y proyecto existente.
4. Ejecucion para formar a alguien sin experiencia.
5. Fuentes y links de alto valor, priorizando la fuente propia de cada herramienta.
6. Herramientas principales, una por una.
7. Protocolos de calidad y errores comunes.
8. Que NO debe hacer un perfil junior.
9. Modulos cerrados sin comprimir ni reescribir.
10. Handoff para Codex.

## Handoff de vuelta a Codex

Cuando Claude termine una conversacion fuente, no se integra directamente.

Codex debe revisar:

- si la fuente cumple `.claude/rules/canon-admision.md`;
- si contiene datos de clientes o ejemplos no anonimizados;
- si hay fuentes oficiales o solidas;
- si hay modulos suficientes;
- si cada modulo tiene criterio operativo y no solo informacion;
- si debe convertirse en canon, skill, referencia, checklist o template;
- si el agente de alineacion detecta conflictos con Claude Code.

Proceso recomendado:

1. Mantener la conversacion fuente fuera del repo mientras se desarrolla.
2. Exportarla o compartirla como fuente primaria cuando Rodrigo la apruebe.
3. Revisarla en Codex con `canon-admision.md`.
4. Si pasa, convertirla en estructura operativa: canon, skill, referencias, checklists y templates.
5. Si no pasa, conservarla como fuente o reforzar una skill sin llamarla canon.

## Criterios de rechazo

Una conversacion fuente se rechaza o se devuelve a ampliacion si:

- usa frases tipo "siempre deberias" sin condicion, contexto o criterio;
- parece resumen de buenas practicas;
- no distingue nuevo vs existente cuando aplica;
- no explica ejecucion paso a paso;
- no trae fuentes suficientes;
- trata una herramienta usando fuentes secundarias cuando existe fuente propia u oficial;
- se apoya en ejemplos de clientes reales;
- mezcla varias areas;
- no define errores comunes o limites junior;
- no permite extraer checklists;
- no cambia decisiones operativas.

## Riesgos y mitigaciones

| Riesgo | Mitigacion |
|---|---|
| Crear canons flojos por entusiasmo | Aplicar regla de admision antes de integrar. |
| Contaminar con clientes reales | Mantener ejemplos reales solo en `clients/[cliente]/`; usar patrones anonimizados. |
| Copiar SEO literalmente | Replicar metodo, no contenido SEO. |
| Usar fuentes superficiales | Exigir fuentes oficiales o top por modulo. |
| Explicar herramientas desde fuentes ajenas | Exigir fuente propia u oficial como base del modulo. |
| Cargar demasiado contexto en agentes | Convertir material largo en referencias bajo demanda. |
| Perder fidelidad del aprendizaje | Conservar conversacion fuente como fuente; integrar solo despues de revision. |

## Decision actual

El siguiente paso no es crear un canon.

El siguiente paso es auditar si SEO esta completamente migrado y documentar el patron exacto que hay que replicar. Despues se usa este metodo para pedir a Claude la primera conversacion fuente, preferiblemente SEM / Paid Ads, y despues evaluarla con Codex + agente de alineacion.
