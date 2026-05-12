# GA4 / GTM Notes - E-SELEC

## GA4

Checklist minimo:

- propiedad correcta;
- data stream correcto;
- enhanced measurement revisado;
- conversiones marcadas solo para acciones valiosas;
- eventos personalizados documentados;
- custom dimensions creadas si se van a usar en reporting;
- retencion y consentimiento revisados.

## GTM

Estructura recomendada:

| Elemento | Nomenclatura |
|---|---|
| Tags | `GA4 - Event - Form Submitted` |
| Triggers | `Submit - Contact Form` |
| Variables | `DL - form_name` |

## DataLayer

Patron recomendado:

```javascript
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  event: "form_submitted",
  form_name: "contact",
  form_location: "footer",
  service_category: "seo"
});
```

## Validacion

Usar:

- GTM Preview;
- GA4 DebugView;
- Real-time GA4;
- navegador mobile/desktop;
- prueba de formulario real si esta aprobado;
- revision de duplicados.

## Errores comunes

- evento duplicado por gtag + GTM;
- trigger demasiado amplio;
- evento dispara antes de consentimiento;
- propiedad mal nombrada;
- conversion marcada antes de validar;
- formularios Ajax sin evento de exito;
- WhatsApp/telefono medidos solo como click, no como lead cerrado.
