# Tirocinio
Come configurare il programma

1 - il programma per funzionare ha bisogno di un interprete Python(3.8+) : https://www.python.org/downloads/

2 - installare le seguenti librerie: 
    
    pip install semanticscholar
    pip install selenium
    pip install webdriver_manager
    
Nel programma:

3 - se si usano browser diversi da Chrome, cambiare nel programma la riga 4 con una delle classi disponibili in questo link:
https://github.com/rasjani/webdrivermanager#classes

4 - sostituire nella riga 103 il percorso, inserendo al posto di "D:/github/Tirocinio/" il proprio
dove risiede il file CSVcreator.py

es. "C:/miopercorso/github/Tirocinio/"
    
5- Avviare il programma tramite cmd (terminale) con il comando python miopercorso/CSVcreator.py
