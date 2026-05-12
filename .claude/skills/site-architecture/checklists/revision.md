# Checklist de revision - Site Architecture

Antes de entregar, comprobar:

## Contexto

- [ ] Lei contexto, memoria, log, mensajes y tasks si existen.
- [ ] Verifique si ya habia una arquitectura o redisenos previos en outputs/manifest.
- [ ] Declare fuentes y datos faltantes.
- [ ] No repeti decisiones ya descartadas en log.

## Calidad de arquitectura

- [ ] Cada pagina principal tiene objetivo claro.
- [ ] La jerarquia es entendible para usuario y SEO.
- [ ] El menu no intenta mostrarlo todo.
- [ ] Las URLs son consistentes, cortas y estables.
- [ ] El plan contempla mobile, footer y breadcrumbs cuando aplica.
- [ ] El enlazado interno conecta hubs, servicios y conversiones.

## Riesgo SEO y produccion

- [ ] Si hay URLs actuales, inclui accion por URL.
- [ ] Si cambia una URL, inclui redireccion 301.
- [ ] No propuse eliminar paginas con posible trafico sin verificar datos.
- [ ] Marque WordPress, WooCommerce, formularios, checkout, redirects y tracking como produccion.
- [ ] Aplique Orden de Cambio si se pidio implementar, no solo planificar.

## Calidad E-SELEC

- [ ] Clasifique nivel SA0-SA3.
- [ ] Use `quality/criterios-output.md`, contrato Web / arquitectura.
- [ ] Deje una siguiente accion unica.
- [ ] Si faltan GSC/GA4/SEMrush, marque el output como parcial.
- [ ] No inclui secretos, credenciales, datos personales ni exports brutos.
