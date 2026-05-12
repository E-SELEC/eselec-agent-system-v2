# Checklist de revision - ingesta de evidencia

Antes de versionar o usar una evidencia:

- [ ] Lei contexto, memoria, log, mensajes y manifest del cliente.
- [ ] Identifique fuente original, cliente, dominio/cuenta y periodo.
- [ ] Clasifique Nivel E0/E1/E2/E3.
- [ ] Separe dato real, estimacion, hipotesis y conclusion.
- [ ] Declare contradicciones y limitaciones.
- [ ] No copie exports brutos por comodidad.
- [ ] No copie secretos, cookies, tokens, claves ni passwords.
- [ ] No incluya PII, IDs de usuario, pedidos individuales ni datos personales.
- [ ] No mezcle datos de otro cliente.
- [ ] Deje claro que decisiones permite y cuales no.
- [ ] Actualice manifest/log/registro si se crea archivo.

Bloquea si:

- [ ] El archivo contiene secretos o PII.
- [ ] No se puede confirmar que la fuente pertenece al cliente.
- [ ] No hay periodo.
- [ ] Hay contradiccion que cambia la decision.
- [ ] El output se quiere usar como final pero la evidencia es E1/E2.
