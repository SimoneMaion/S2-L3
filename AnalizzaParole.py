import re
def analizza_parole(testoinput):

    counter= 0
    dizionario = {}                                                             # creo un dizionario
    
    testoinput = re.sub(r'[^\w\s]', '', testoinput)                             # rimuove tutto quello che non è un carattere o uno spazio
    testoinput = testoinput.lower()                                             # Converti il testo in minuscolo
    lista_parole = testoinput.split()                                           # Divide il testo in parole
    
    for parola in lista_parole:
        dizionario[parola] = dizionario.get(parola, 0) + 1                      # Per ogni parola della lista, cerca la corrispondenza nel dizionario e aggiorna il valore o aggiunge la parola

    return dizionario

# Esempio di utilizzo
testo = "Ciao, ciao! Come stai? Stai bene?"
risultato = analizza_parole(testo)
print(risultato)
