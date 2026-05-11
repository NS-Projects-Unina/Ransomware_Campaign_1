# ATTACCO RANSOMWARE + Sessione meterpreter
In questa simulazione si è simulato uno scenario di attacco informatico composto da varie tipologie di attacchi
al fine di mostrare come molto spesso una delle vulnerabilità dei sistemi informatici è proprio l'utente inesperto.

La vittima in questa simulazione è Marinobus.s.r.l, un azienda di trasporti che opera sul territorio italiano, 
più precisamente nel sud Italia; l'obiettivo dell'attacco è colpire i dati sensibili dei clienti è chiedere un 
riscatto.

# PREPARAZIONE - Ricognizione e raggiro del Firewall

## FASE 1.1 - Ricognizione
Come primo passo si è svolta una ricognizione per individuare i contatti di assistenza e i contatti di segreteria.
Dopo di che si procede all'accedere alla sede centrale di Marinobus (attualmente risiede ad Altamura (BA); l'obiettivo 
è quello di entrare all'interno della struttura fisica e piazzarsi nell'area ristoro della struttura.

## FASE 1.2 - Connessione Wi-Fi
Per procedere con l'attacco, si ha bisogno di connettersi alla Wi-Fi della struttura, si procede semplicemente chiedendo 
la password della rete (Prima vulnerabilità possibile - non dovrebbe essere comunicata cosi facilmente!)

Una volta connessi, rileviamo gli indirizzi IP connessi, in particolare il nostro indirizzo IP, dove verrà reindirizzato
il traffico della rete e l'indirizzo IP di Kali, creando un "Ponte" tra i due IP

## FASE 1.3 - Stabilire le regole del Firewall
Una volta costruito il bridge, è importante stabilire delle nuove regole per il firewall, per creare una sorta di eccezione
di sicurezza, chiedendogli sostanzialmente di fare un eccezione sul traffico che arriverà sulla porta 4447 che verrà utilizzata 
per l'attacco meterpreter

# PREPARAZIONE DEL PAYLOAD - Accensione della sessione Apache2 e Metaxploit Framework

## FASE 2.1 - Preparazione del Payload
Si accede su Kali e si apre un terminale, poi si procede con l'elaborazione di un file .apk malevolo con l'utilizzo di msfvenom
un comando che permette di costruire un file eseguibile contentente un payload. quest'ultimo stabilisce un controllo remoto
e di interagire con il sistema compromesso.

Tutto questo è permesso grazie al comando **android/meterpreter/reverse_tcp**, il quale permette di stabilire silenziosamente
una connessione con il nostro pc (*LHOS: nostroIP*), e con il termine *reverse* il cellulare android della vittima si connetterà 
con il nostro pc ma non viceversa.

## FASE 2.2 - Avvio della sessione Apache2
Dopo aver assegnato al payload i vari permessi, apriamo la sessione di **Apache2** che permette di rendere scaricabile online
il nostro payload; nello specifico, ora, è possibile poter scaricare il payload malevolo su internet (ATTENZIONE - saremo noi a
scaricarlo poi inviarlo alla vittima con una mail di phishing)

## FASE 2.3 - Avvio della sessione Meterpreter
Apriamo un secondo terminale ed si avvia la **msfconsole**, una volta dentro si dovrà creare nuovamente il payload impostato come
è stato fatto nella fase precedente ma con l'inserimento di alcune righe che permettono di tenere la connessione con la vittima attiva.
Questa fase è il cuore dell'attacco, il quale permette di penetrare nel sistema della vittima ed ottenere tutti i dati sensibili; il nostro
obiettivo è quello di accedere ai suoi contatti e trovare il contatto del DBA al quale verrà inviato il file eseguibile ransomware.

## FASE 2.4 - PHISHING - Invio del payload alla vittima con WeTransfer
Una volta che è tutto pronto e le sessioni sono attive, utilizziamo WeTransfer per inviare il payload alla vittima (questo perchè 
quest'ultimo non ha restrizioni di sicurezza rigide come gmail) specificando di scaricare immediatamente il file allegato per
aggiornare i protocolli di sicurezza a seguito di un attacco (seconda vulnerabilità - un utente consapelove dovrebbe controllare
il file e stare attento sulle mail che riceve).
Quando la vittima avrà eseguito ed aperto l'app (è stato scelto proprio android come sistema operativo perchè quest'ultimo, 
dopo aver segnalato che l'app potrebbe essere dannosa, permette all'utente di scegliere se correre il rischio di eseguirla ugualmente)
nella sessione meterpreter, avremo stabilito la connessione e possiamo accedere a tutti i suoi dati senza che la vittima
ne sia a conoscenza.

# ATTACCO RANSOMWARE - Creazione del file malevolo da inviare tramite messaggio all'DBA

## FASE 3.1 - PREPARAZIONE AMBIENTE - File con dati da criptare
L'attacco ransomware inizia con la preparazione del file vittima, sempre all'interno dell'ambiente simulato kali si
è elaborato una cartella contenente un file con nomi, cognomi e metodi di pagamento (fasulli) che verranno poi criptati/
decriptati con l eseguibile ransomware.

## FASE 3.2 - ELABORAZIONE VIRUS - Costruzione del ransomware
Si procede con l'elaborazione del virus ransomware_win.py in python: in questo file si utilizza la libreria
Fernet di python, e si costruisce un codice ad hoc che trova la cartella contentente il file dei dati nel 
dispositivo, poi procede con il crypting impostando l'estensione del file vittima con ".locked"; successivamente
viene generato un file con la (finta) richiesta di riscatto, il quale, dopo il pagamento, avrebbe decryptato il
file e rimosso l'estensione ".locked".

## FASE 3.3 - COMPILAZIONE DELL'ESEGUIBILE - Per inviare il file alla vittima e concludere l'attacco
L'ultima fase prevede l'elaborazione dell'eseguibile, il quale automatizza tutto il procedimento
crypting-riscatto-decrypting.

E' bene specificare che le "vittime" sono in realtà persone consensienti e che tutti gli attacchi sono stati
svolti su kali linux!

