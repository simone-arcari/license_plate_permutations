targa = "aa000aa"
ultimaTargaImmatricolata = "gg580ef"
ultimaTargaPossibile = "zz999zz"
contatore = 1


def aggiungiZeri(numero):
    #@param numero: int
    #@return: string
    if numero < 10:
        numero =  "00" + str(numero)
    elif numero < 100:
        numero = "0" + str(numero)
    else:
        numero = str(numero)

    return numero


def aumentaLettere(lettere):
    #@para lettere: string
    #@return: string
    primaLettera = ord(lettere[1])
    secondaLettera = ord(lettere[0])

    primaLettera+=1

    if primaLettera > ord("z"):
        primaLettera = ord("a")

        secondaLettera+=1

        if secondaLettera > ord("z"):
            secondaLettera = ord("a")

    lettereAumentate = chr(secondaLettera) + chr(primaLettera)
    return lettereAumentate
        


def aumentaTarga(targa):
    #@param targa: str
    numeroTarga = int(targa[2:5])
    lettereBasse = targa[5:]
    lettereAlte = targa[:2]
    
    numeroTarga+=1

    if numeroTarga > 999:
        numeroTarga = 0
        
        if lettereBasse == "zz":
            lettereAlte = aumentaLettere(lettereAlte)
            
        lettereBasse = aumentaLettere(lettereBasse)
    
    numeroTarga = aggiungiZeri(numeroTarga)
    targaAumentata = lettereAlte + numeroTarga + lettereBasse
    return targaAumentata


while targa != ultimaTargaImmatricolata and targa != ultimaTargaPossibile:
    print(targa + "\tcount: " + str(contatore))
    targa = aumentaTarga(targa)
    contatore+=1
else:
    if targa == ultimaTargaImmatricolata:
        print("La targa cercata è: " + targa + "\t\tRisulta la numero: " + str(contatore))
