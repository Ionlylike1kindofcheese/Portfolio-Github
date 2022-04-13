aantalDict = {"bollen" : 0, "hoorntjes" : 0, "bakjes" : 0, "slagroom" : 0, "sprinkels" : 0, "caramelsaushoorn" : 0, "caramelsausbak" : 0, "liter" : 0}
prijsDict = {"bollen" : 0.95, "hoorntjes" : 1.25, "bakjes" : 0.75, "slagroom" : 0.50, "sprinkels" : 0.30, "caramelsaushoorn" : 0.60, "caramelsausbak" : 0.90, "liter" : 9.80}


# print tekst als er een antwoord wordt gegeven dat niet klopt
def showNotunderstood():
    print("Sorry dat begrijp ik niet...")


# Hiermee kan je een aantal witregels laten ontstaan
def unnecesarySpaces(ammoutSpaces):
    for x in range(ammoutSpaces):
        print()


# Vraag naar reden voor gebruik
def askReason():
    reasons = False
    while reasons == False:
        bussinesorder = input("Bent u 1) particulier of 2) zakelijk? ")
        if bussinesorder == "1":
            reasons = True
            askBollen()
        elif bussinesorder == "2":
            reasons = True
            bussinesOrder()
        else:
            showNotunderstood()
    

# Vraagt hoeveel liter ijs
def bussinesOrder():
    global aantalDict
    hoeveelliter = int(input("Hoeveel liter ijs wilt u? "))
    literCount = 1
    while literCount <= hoeveelliter:
        litersmaak = input("Welke smaak wilt u voor liter nummer " + str(literCount) + "? A) Aardbei, C) Chocolade of V) Vanille? ")
        if litersmaak == "A" or litersmaak == "C" or litersmaak == "V":
            literCount += 1
        else:
            showNotunderstood()
    aantalDict["liter"] = hoeveelliter
    orderLabel("bussines")


# Vraagt naar aantal bollen en vraagt ook naar hoorntje of bakje
def askBollen():
    global aantalDict
    bollenVraag = False
    hoornofbak = ""
    while bollenVraag == False:
        aantalbollen = input("Hoeveel bolletjes wilt u? ")
        if aantalbollen.isdigit() == True:
            aantalbollen = int(aantalbollen)
            aantalDict["bollen"] += aantalbollen       
            if aantalbollen >= 1 and aantalbollen <= 3:
                bollenVraag = True
                unnecesarySpaces(1)
                askhoornofbak = False
                while askhoornofbak == False:
                    askWhich = input("Wilt u dit in A) een hoorntje of B) een bakje? ")
                    if askWhich == "A":
                        aantalDict["hoorntjes"] += 1
                        hoornofbak = "hoorn"
                    elif askWhich == "B":
                        aantalDict["bakjes"] += 1
                        hoornofbak = "bak"
                    else:
                        showNotunderstood()
                    if askWhich == "A" or askWhich == "B":
                        askhoornofbak = True        
            elif aantalbollen >= 4 and aantalbollen <= 8:
                print("Dan krijgt u van mij een bakje met " + str(aantalbollen) + " bolletjes.")
                unnecesarySpaces(1)
                aantalDict["bakjes"] += 1
                hoornofbak = "bak"
                bollenVraag = True
            elif aantalbollen > 8:
                print("Sorry zulke grote bakken hebben we niet")
            else:
                showNotunderstood()
        else:
            showNotunderstood()
    askFlavours(aantalbollen, hoornofbak)


# Vraagt naar smaak per bol (Smaken zijn allemaal dezelfde prijs)
def askFlavours(aantalbollen, hoornofbak): 
    bolnummer = 1
    flavourquestions = False      
    while flavourquestions == False:
        if bolnummer <= int(aantalbollen):
            askflavour = input("Welke smaak wilt u voor bolletje nummer " + str(bolnummer) + "? A) Aardbei, C) Chocolade of V) Vanille? ")       
            if askflavour == "A" or askflavour == "C" or askflavour == "V":
                bolnummer += 1
            else:
                showNotunderstood()
        else:
            flavourquestions = True
            unnecesarySpaces(1)
    askToppings(aantalbollen, hoornofbak)


# Vraagt naar topping
def askToppings(aantalbollen, hoornofbak):
    global aantalDict
    toppingphase = False
    while toppingphase == False:
        askTopping = input("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? ")
        if askTopping == "A":
            None
        elif askTopping == "B":
            aantalDict["slagroom"] += 1
        elif askTopping == "C":
            aantalDict["sprinkels"] += aantalbollen
        elif askTopping == "D":
            if hoornofbak == "hoorn":
                aantalDict["caramelsaushoorn"] += 1
            elif hoornofbak == "bak":
                aantalDict["caramelsausbak"] += 1
        else:
            showNotunderstood()

        if askTopping == "A" or askTopping == "B" or askTopping == "C" or askTopping == "D":
            toppingphase = True
            unnecesarySpaces(1)
    askMore(aantalbollen, hoornofbak)


# Vraagt of er meer bestelt moet worden (Alleen particulier)
def askMore(aantalbollen, hoornofbak):
    needMore = False
    while needMore == False:
        yesorno = str(input("Hier is uw " + hoornofbak + " met " + str(aantalbollen) + " aantal bollen. Wilt u nog meer bestellen? (Y/N) "))
        if yesorno == "Y":
            unnecesarySpaces(2)
            needMore = True
            askBollen()
        elif yesorno == "N":
            unnecesarySpaces(2)
            needMore = True
            orderLabel("personal")
        else:
            showNotunderstood()


def orderLabel(kindLabel):
    print('---------["Papi Gelatto"]---------')
    unnecesarySpaces(1) 
    notationList = ["bolletje              ", "horrentje             ", "bakje                 ", "slagroom              ", "sprinkels             ", "caramel saus (hoorn)  ", "caramel saus (bak)    "]
    dictKeyList = list(aantalDict.keys())
    if kindLabel == "personal":
        totaalprijs = 0
        for index, notationItem in enumerate(notationList):
            aantal = aantalDict.get(dictKeyList[index])
            prijs = prijsDict.get(dictKeyList[index])
            aantalprijs = aantal * prijs
            totaalprijs += aantalprijs   
            if aantal >= 1:
                print(notationItem + str(aantal) + " x " + str(prijs) + " = €" + str(round(aantalprijs, 2)))
        print("                      ------------ +")
        print("totaal                 = €" + str(round(totaalprijs, 2)))
    elif kindLabel == "bussines":
        notationItem = "Liter                 "
        aantal = aantalDict.get("liter")
        prijs = prijsDict.get("liter")
        totaalprijs = aantal * prijs
        btw = totaalprijs / 100 * 6
        print(notationItem + str(aantal) + " x " + str(prijs) + " = €" + str(round(totaalprijs, 2)))
        print("                      ------------ +")
        print("Totaal                = €" + str(round(totaalprijs, 2)))
        print("BTW (6%)              = €" + str(round(btw, 2)))


print("Welkom bij Papi Gelato")
askReason()