# ATTACCO RANSOMWARE + Sessione meterpreter
In questa simulazione si è simulato uno scenario di attacco informatico composto da varie tipologie di attacchi
al fine di mostrare come molto spesso una delle vulnerabilità dei sistemi informatici è proprio l'utente inesperto.

La vittima in questa simulazione è Marinobus.s.r.l, un azienda di trasporti che opera sul territorio italiano, 
più precisamente nel sud Italia; l'obiettivo dell'attacco è colpire i dati sensibili dei clienti è chiedere un 
riscatto.

### FASE 1 - Ricognizione
Come primo passo si è svolta una ricognizione per individuare i contatti di assistenza e i contatti di segreteria.
Dopo di che si procede all'accedere alla sede centrale di Marinobus (attualmente risiede ad Altamura (BA); l'obiettivo 
è quello di entrare all'interno della struttura fisica e piazzarsi nell'area ristoro della struttura.

## FASE 2 - Connessione Wi-Fi
Per procedere con l'attacco, si ha bisogno di connettersi alla Wi-Fi della struttura, si procede semplicemente chiedendo 
la password della rete (Prima vulnerabilità possibile - non dovrebbe essere comunicata cosi facilmente!)

Una volta connessi, rileviamo gli indirizzi IP connessi, in particolare il nostro indirizzo IP, dove verrà reindirizzato
il traffico della rete e l'indirizzo IP di Kali, creando un "Ponte" tra i due IP

# FASE 3 - Stabilire le regole del Firewall
