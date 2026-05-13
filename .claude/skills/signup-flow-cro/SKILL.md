---
name: signup-flow-cro
description: >
  Audita y optimiza flujos de signup, registro, creacion de cuenta y alta de
  prueba para clientes de E-SELEC: signup conversion, registration friction,
  trial signup, account creation, signup abandonment, campos de registro,
  social login, password UX, verificacion de email, pasos de alta, mobile y
  medicion. Usalo cuando se hable de signup, registro, crear cuenta, free
  trial, baja conversion de registro, demasiados pasos para registrarse o
  friccion antes de acceder al producto. Para formularios de lead no cuenta,
  usar form-cro. Para post-signup y activacion, usar onboarding-cro.
---

# Signup Flow CRO - E-SELEC

## Proposito

Reducir friccion en el alta de cuenta sin perder datos realmente necesarios, romper tracking, crear riesgos de privacidad ni degradar activacion posterior.

Esta skill no implementa cambios reales. Produce auditoria, redisenio recomendado o hipotesis de test.

## Fuentes obligatorias

Si el cliente existe, lee:

1. `clients/[cliente]/context.md`
2. `clients/[cliente]/memory.md` si existe
3. `clients/[cliente]/log.md`
4. `clients/[cliente]/mensajes.md`
5. `clients/[cliente]/tasks.md` si existe
6. `clients/[cliente]/outputs/manifest.md`
7. `quality/criterios-output.md`
8. `.claude/skills/page-cro/SKILL.md` si el signup nace desde una landing
9. `.claude/skills/form-cro/SKILL.md` si hay formulario de alta
10. `.claude/skills/analytics-tracking/SKILL.md` para eventos y conversiones
11. `.claude/skills/onboarding-cro/SKILL.md` si el cambio afecta activacion
12. `.claude/skills/ab-test-setup/SKILL.md` si propones test
13. `protocols/activos-criticos.md`

Necesitas ver el flujo, captura, pasos o lista de campos. Si no existe, entrega solo diagnostico orientativo.

## Niveles

- SF3 - validado: flujo revisado, pasos/campos medidos, mobile y tracking comprobados.
- SF2 - diagnostico fuerte: flujo visible y objetivo claro; faltan datos cuantitativos completos.
- SF1 - orientativo: hay descripcion parcial, pero faltan pantallas, metricas o restricciones.
- SF0 - bloqueado: falta flujo, objetivo de alta o acceso a informacion basica.

## Workflow

1. Clasificar flujo: free trial, freemium, cuenta pagada, waitlist, B2B, B2C.
2. Definir conversion principal: signup submit, email verified, trial started, account created.
3. Mapear pasos, campos, auth, verificacion, errores y pantalla posterior.
4. Evaluar valor antes de compromiso: que ve/recibe el usuario antes de registrarse.
5. Revisar friccion: campos, password, SSO, telefono, empresa, pasos, captcha, terminos.
6. Revisar confianza: no credit card, privacidad, seguridad, expectativa y soporte.
7. Revisar mobile y accesibilidad basica.
8. Revisar medicion: view, start, step complete, error, submit, verification, activation handoff.
9. Preparar output con `templates/auditoria-signup-flow.md`.

## Reglas

- Cada campo requerido debe justificar por que no puede esperar a onboarding.
- No pedir telefono, empresa, rol o tarjeta si no son necesarios antes del primer valor.
- No recomendar eliminar verificacion/compliance sin entender riesgo.
- No llamar mejora a un cambio que sube signup pero dana activacion.
- No recomendar test si no hay tracking, baseline y trafico.
- No tocar web, producto, auth, checkout, CRM, email ni tracking sin Orden de Cambio.

## Bloqueos

- no hay flujo visible, captura o descripcion de pasos;
- no se conoce la conversion objetivo;
- falta informacion sobre requisitos legales/compliance que afectan registro;
- la recomendacion rompe auth, pagos, CRM, seguridad o activacion;
- se piden cambios reales sin aprobacion.

## Referencias

- `references/signup-patterns.md`: patrones por tipo de signup.
- `templates/auditoria-signup-flow.md`: formato de salida.
- `checklists/revision.md`: revision final.
