def media_mobile(listaNumeri, n_elementi):

    lunghezzaLista = len(listaNumeri)
    medieSvolte = []
    puntatore = 1  


    while puntatore <= lunghezzaLista:                                          
        inizio = max(0, puntatore - n_elementi)                                 # sceglie il punto di partenza prendendo il più alto tra 0 (primo elemento) e il puntatore meno il numero dato
        media = sum(listaNumeri[inizio:puntatore]) / (puntatore - inizio)       # somma i numeri dal punto scelto sopra e il puntatore, poi li divide per la quantità di numeri utilizzati
        if media.is_integer():                                                  # se il risultato non ha bisogno di essere float, lo trasforma in int
         media = int(media)
        medieSvolte.append(media)                                               # aggiunge alla lista finale il numero
        puntatore += 1                                                          
    
    
    
    return medieSvolte




listaNumeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n_elementi = 3
print(media_mobile(listaNumeri, n_elementi))
