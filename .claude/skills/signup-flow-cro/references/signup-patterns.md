# Patrones Signup Flow CRO

## Campos

| Campo | Default | Nota |
|---|---|---|
| Email | requerido | evitar confirmacion doble del email |
| Password | requerido o passwordless | mostrar requisitos antes del error |
| Nombre | opcional si no se usa inmediato | evitar separar nombre/apellido salvo necesidad |
| Telefono | diferir | solo requerir si SMS/ventas lo necesita |
| Empresa | diferir o inferir | pedir despues si no bloquea valor inicial |
| Rol / uso | onboarding | una pregunta maxima si personaliza el primer valor |
| Tarjeta | evitar en prueba salvo modelo lo requiera | explicar claramente si se pide |

## Tipos de flujo

- B2B SaaS trial: email/SSO -> password o magic link -> contexto minimo -> primer valor.
- Freemium: social/email rapido -> acceso inmediato -> perfil progresivo.
- Waitlist: email + una pregunta opcional -> confirmacion clara.
- E-commerce: checkout invitado primero; cuenta despues de compra.

## Fricciones comunes

- Demasiados campos antes de ver valor.
- Password con reglas ocultas.
- Email verification bloqueando antes de explorar.
- SSO escondido.
- Captcha agresivo.
- Mobile con teclado incorrecto o campos pequenos.
- Mensajes de error genericos.

## Medicion minima

- signup page view;
- form start;
- step completion;
- field error;
- submit;
- email verified;
- account created;
- first activation event.
