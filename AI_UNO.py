# Belangrijke imports
import random
from time import sleep

# Belangrijke variabelen
errormessage = "Error! Probeer opnieuw a.u.b"
cardColours = ['blauwe', 'rode', 'gele', 'groene']
specialColoured = ['neem-twee', 'keer-om', 'sla-beurt-over']
withoutColours = ['keuzekaart', 'neem-vier']

def uitleg():
    print("We zullen effe beginnen met het uitleggen hoe de regels werken.")
    sleep(2)
    print("Voordat het spel begint worden alle kaarten geschud en gegeven. De bovenste kaart op de stapel gelegd. Deze bovenste kaart die wordt getrokken heeft geen effect in het begin")
    sleep(4)
    print("In het begin van het spel krijgt iedereen 7 kaarten")
    sleep(2)
    print("Als u aan de beurt bent dan moet uw de positienummer van uw kaart benoemen (Waar de kaart van links naar rechts staat in uw deck)")
    sleep(4)
    print("U moet 'uno' typen wanneer er aan u wordt gevraagd welke kaart u wilt spelen en u nog 1 kaart heb in uw deck. Wanneer u dit niet doet dan moet u voor straf 2 kaarten geforceerd pakken")
    sleep(5)
    print("Als u geen kaarten heb om te spelen dan moet u 'pak' typen. Dan wordt er een kaart van de kaartenstapel gepakt. U kan dan kiezen of u de kaart wilt spelen of niet.")
    sleep(5)
    print("Je hebt normale kaarten en speciale kaarten (We komen daar later op terug)")
    sleep(3)
    print("In totaal zijn er 108 kaarten in het spel op gebied van inhoud")
    sleep(2)
    print("Er zijn in totaal 4 kleuren: rood, blauw, geel en groen")
    sleep(3)
    print("Normale kaarten gaan van 0 tot 9. In totaal is dat 19 kaarten van elke kleur (1x een 0-kaart en 2x een 1 t/m 9 kaart)")
    sleep(5)
    print("Je kan alleen normale kaarten boven op elkaar gooien als de kleur of het nummer hetzelfde zijn")
    sleep(4)
    print("En nu de speciale kaarten")
    sleep(2)
    print(" - Neem-twee kaart - ")
    sleep(1)
    print("Als er een neem-twee kart op de stapel gegooid wordt dan moet een speler 2 kaarten erbij pakken.")
    sleep(4)
    print("Deze kaart kan alleen gespeeld worden wanneer op de stapel dezelfde kleur van de kaart ligt of een andere +2 of +4 kaart.")
    sleep(5)
    print("In totaal zijn er 8 kaarten hievan (2 kaarten van elke kleur)")
    sleep(3)
    print(" - Keer-om kaart - ")
    sleep(1)
    print("Wanneer er bijvoorbeeld linksom wordt gespeeld en je legt de kaart op de stapel dan draait de volgorde om en wordt er rechtsom gespeeld")
    sleep(4)
    print("Deze kaart kan alleen gespeeld worden wanneer er een dezelfde kleur op de stapel ligt of als er een andere keer-om kaart op de stapel ligt")
    sleep(5)
    print("In totaal zijn er 8 kaarten hievan (2 kaarten van elke kleur)")
    sleep(3)
    print(" - Sla-beurt-over kaart - ")
    sleep(1)
    print("Als er een sla-beurt-over kaart op de stapel gegooit wordt dan moet de speler na de speler die de kaart neerlegt een beurt overslaan.")
    sleep(5)
    print("Deze kaart kan alleen gespeeld worden wanneer er een dezelfde kleur op de stapel ligt of als er een andere sla-beurt-over kaart op de stapel ligt")
    sleep(5)
    print("In totaal zijn er 8 kaarten hievan (2 kaarten van elke kleur)")
    sleep(3)
    print(" - Keuzekaart - ")
    sleep(1)
    print("De speler die de kaart neerlegt mag een kleur kiezen waarin het spel verder gespeeld wordt")
    sleep(3)
    print("De speler mag ongeacht de kleur op de stapel de kaart spelen")
    sleep(3)
    print("In totaal zijn er 4 kaarten hievan (1 van elke kleur)")
    sleep(3)
    print(" - Neem-4 kaart - ")
    sleep(1)
    print("Als de speler deze kaart neerlegt dan moet de volgende speler 4 kaarten pakken en mag de speler die de kaarten heb gepakt de kleur kiezen")
    sleep(4)
    print("Deze kaart mag ongeacht de kleur of kaart gespeeld worden")
    sleep(3)
    print("In totaal zijn er 4 kaarten hievan (1 van elke kleur)")
    sleep(3)
    print("Dat was het voor de uitleg")
    sleep(2)
    anwsered = False
    while anwsered == False:
        nogeenkeer = input("Wilt u het nog een keer horen? (Antwoord met 'ja' of 'nee')")
        if nogeenkeer == "ja":
            anwsered = True
            uitleg()
        elif nogeenkeer == "nee":
            anwsered = True
        else:
            print(errormessage)


def createCards():
    # belangrijke lists
    listColors = ['blauwe 0', 'rode 0', 'gele 0', 'groene 0']
    listSpecial = []
    # hulp materiaal
    colorsGiven = ['blauwe ', 'rode ', 'gele ', 'groene ']

    # Duplicate below
    eightSpecial = ['neem-twee', 'keer-om', 'sla-beurt-over']
    fourSpecial = ['keuzekaart', 'neem-vier']
    # Duplicate above

    # uitvoer opvulling lists
    for kleur in colorsGiven:
        for repeat in range(2):
            for nummers in range(1,10):
                listColors.append(str(kleur) + str(nummers))
    for kleur in colorsGiven:
        for repeat in range(2):
            for achteenheden in eightSpecial:
                listSpecial.append(str(kleur) + str(achteenheden))
        for viereenheden in fourSpecial:
            listSpecial.append(str(viereenheden))
    # combineer 2 lists en buiten de function sturen
    sortedCards = list(listColors) + list(listSpecial)
    return sortedCards


def randomizeCards(currentCardlist):
    # randomize de list en stop in nieuwe list
    randomizedCards = []
    randomizeProcess = False
    indexrange = len(currentCardlist)
    while randomizeProcess == False:
        chosenCardNumber = random.randrange(0,int(indexrange))
        pickedCard = currentCardlist[chosenCardNumber]
        randomizedCards.append(pickedCard)
        del currentCardlist[chosenCardNumber]
        indexrange -= 1
        # indexrange check voor afbreken while loop
        if indexrange == 0:
            randomizeProcess = True
        else:
            None
    # voltooide resultaat terugsturen buiten de function
    return randomizedCards


def giveCards(playerammout):
    # deelt de top kaart uit aan iedereen 7 keer
    for cardrounds in range(7):
        for playercount in range(0,playerammout):
            currentcard = currentCardlist[0]
            del currentCardlist[0]
            playerlist[playercount].append(currentcard)
    # creërt een local variable voor de speelstapel en legt de eerste kaart op de speelstapel
    speelstapel = []
    currentcard = currentCardlist[0]
    del currentCardlist[0]
    speelstapel.append(currentcard)
    # return de huidige speelstapel buiten de function
    return speelstapel


def playableCard(checkingcard):
    canBePlayed = False
    # Kaart heeft een kleur?
    if canBePlayed == False:
        for colour in cardColours:
            if colour in checkingcard:
                # Kijk of er een andere kleur gespeeld moest worden dan de topkaart (Gevolg van kleurkaart)
                if mustcolour != "":
                    if colour in mustcolour:
                        canBePlayed = True
                else:
                    if colour in topcard:
                        canBePlayed = True
    # De kaart heeft een waarschijnlijk een andere kleur dan de topkaart. Zijn de nummers gelijk aan de topkaart?
    if canBePlayed == False:
        for number in range(0,10):
            if str(number) in checkingcard:
                if str(number) in topcard:
                    canBePlayed = True
    # De kaart heeft geen nummer? Is het een speciale kaart?
    if canBePlayed == False:
        for specialColour in specialColoured:
            if specialColour in checkingcard:
                if specialColour in topcard:
                    canBePlayed = True
    # Het kan een kaart zonder kleur zijn?
    if canBePlayed == False:
        for noColour in withoutColours:
            if noColour in checkingcard:
                canBePlayed = True
    # De kaart kan gewoon niet gespeeld worden en variable canBePlayed blijft False.
    else:
        None
    # Return True or False
    return canBePlayed


def countAndSortDictinary():
    # Stopt alles in een niet gesorteerde dictionary
    unsorted_dict = {}
    for colour in cardColours:
        currentcount = 0
        for position in playerlist[currentplayer]:
            if colour in position:
                currentcount += 1
        unsorted_dict[colour] = currentcount
     # Sorteerd de waardes en stopt ze in nieuwe dictionary
    sorted_values = sorted(unsorted_dict.values(),reverse= True)
    sorted_dict = {}
    for i in sorted_values:
        for k in unsorted_dict.keys():
            if unsorted_dict[k] == i:
                sorted_dict[k] = unsorted_dict[k]
                break
    return sorted_dict


def normalOrSpecial(normals, specials):
    # Bepaalt per kleur of speciale kaart of normale kaart eerst gespeeld moet worden
    for colours in dictCount:
        for specialpositions in specials:
            for units in specialColoured:
                if units in specialpositions:
                    chosencard = specialpositions
                    return chosencard
        for normalpositions in normals:
            for numbers in range(9,-1,-1):
                if str(numbers) in normalpositions:
                    chosencard = normalpositions
                    return chosencard


def grabCards(ammoutcards, onepick, nextperson):
    if nextperson == True:
        nextinline(1)
    for times in range(ammoutcards):
        grabbedcard = currentCardlist[0]
        playerlist[currentplayer].append(currentCardlist[0])
        del currentCardlist[0]
    if onepick == True:
        if currentplayer == 0:
            print("Uw gepakte kaart:", grabbedcard)
            playcard = input("Wilt u deze kaart spelen? (Antwoord met 'ja' of 'nee')")
            if playcard == "ja":
                playablecardstatus = playableCard(chosencard)
                if playablecardstatus == True:
                    del playerlist[currentplayer][chosencardposition]
                    gespeeldekaarten.insert(0,chosencard)
            elif playcard == "nee":
                None
            else:
                print(errormessage)
        else:
            playablecardstatus = playableCard(chosencard)
            if playablecardstatus == True:
                del playerlist[currentplayer][chosencardposition]
                gespeeldekaarten.insert(0,chosencard)
    else:
        None


def rotationGame():
    print("De speelvolgorde van het spel wordt omgedraaid!!!")
    if rotation == "forwards":
        return "backwards"
    elif rotation == "backwards":
        return "forwards"


def skipTurn():
    print("De volgende speler moet een beurt overslaan")
    nextinline(2)


def colourChoice():
    if currentplayer == 0:
        anwsered = False
        while anwsered == False:
            chosencolour = input("Kies een kleur waarvan de volgende kaart gespeeld moet worden (Antwoord met 'blauw', 'rood', 'geel' of 'groen')")
            if chosencolour == 'blauw':
                chosencolour = cardColours[0]
                anwsered = True
            elif chosencolour == 'rood':
                chosencolour = cardColours[1]
                anwsered = True
            elif chosencolour == 'geel':
                chosencolour = cardColours[2]
                anwsered = True
            elif chosencolour == 'groen':
                chosencolour = cardColours[3]
                anwsered = True
            else:
                print(errormessage)
    else: 
        chosencolour = random.choice(cardColours)
    return chosencolour


def nextinline(ammout):
    mininumplayer = 0
    maxinumplayer = players - 1
    global currentplayer
    for x in range(ammout):
        if rotation == "forwards":
            currentplayer += 1
            if currentplayer > maxinumplayer:
                currentplayer = mininumplayer
        elif rotation == "backwards":
            currentplayer -= 1
            if currentplayer < mininumplayer:
                currentplayer = maxinumplayer



# --------------------------------------------------- Functions above --------------------------------------------------------------------------

print("Welkom bij Uno!")
startup = False
while startup == False:
    explain = input("Wilt u een uitleg van het spel? Antwoord met 'ja' of 'nee' (Aangeraden om te doen als je nog nooit dit programma heb gebruikt) ")
    if explain == "ja":
        uitleg()
        startup = True
    elif explain == "nee":
        startup = True
    else:
        print(errormessage)

setup = False
while setup == False:
    players = int(input("Hoeveel spelers wilt u dat er meedoen? (Geef een nummer op) "))
    if players > 1 and players < 9:
        setup = True
    elif players == 1:
        print("Te weinig spelers")
    elif players > 8:
        print("Te veel spelers")
    else:
        print(errormessage)

# aanmaken van lists gebaseerd op aantal spelers en dan alle individuele lijsten in 1 lijst stoppen tussen blokhaakjes
playerlist = [[] for i in range(players)]
# aanroepen function voor kaarten aanmaken eenmalig en het randomizen van de kaarten
sortedcardList = createCards()
currentCardlist = randomizeCards(sortedcardList)
# aanroepen function waar aan iedereen 7 kaarten wordt gegeven in het begin en de eerste kaart op de speelstapel legt. Deze eerste kaart heeft verder geen effect als het spel begint.
gespeeldekaarten = giveCards(players)
# belangrijke onderdelen voor het programma om functioneel te werken
currentplayer = 0
rotation = "forwards"
winnerknown = False
deckcount = 7
playercheckcount = players
topcard = gespeeldekaarten[0]
Colouradjustmentcheck = False
mustcolour = ""
chosencard = None
sleep(1)
print("Huidige kaart boven op de speelstapel:", topcard)
sleep(2)
# ----------------------------------------------------- Setup installation above --------------------------------------------------------------------
while winnerknown == False:
    for listaccess in range(0,playercheckcount):
        if len(playerlist[listaccess]) == 0:
            winnerknown = True
            break
    if winnerknown == True:
        break
    if Colouradjustmentcheck == True:
        print("de game wordt verder gespeeld met een", mustcolour, "kaart")  # AANPASSING NODIG OP ANDERE PLEKKEN VANWEGE DIT!!!???
    else:
        mustcolour = ""
    chosencard = None
    cardPlayed = False
    Colouradjustmentcheck = False

    if currentplayer == 0:
        while cardPlayed == False:
            # Laat deck zien en laat speler kiezen welke kaartpositie gespeeld moet worden
            print("Uw deck:", playerlist[0])
            chosencardposition = input("Welke kaart wilt u spelen? ")
            # Als er nog 1 kaart over is dan moet er uno geroepen worden
            if chosencardposition == "uno":
                if len(playerlist[0]) == 1:
                    unocalled = True # Hier moet nog wat mee gedaan worden!!!
                else:
                    print("U kan nog geen uno roepen")
            # Player kan een kaart pakken als hij niks kan spelen (Special card functions kunnen per ongeluk herhaald worden!!!)
            elif chosencardposition == "pak":
                grabCards(1, True, False)
                cardPlayed = True
            # Als chosencardposition een nummer is dan ga verder
            elif chosencardposition.isdigit() == True:
                chosencardposition = int(chosencardposition)
                deckcount = len(playerlist[currentplayer])
                # Check of het nummer niet verder gaat dan de minimale index en de maximale index van de kaart positie
                if chosencardposition > 0 and chosencardposition <= deckcount:
                    chosencardposition -= 1
                    chosencard = playerlist[currentplayer][chosencardposition]
                    # Check of de kaart daadwerkelijk waar gespeeld kan worden en speel de kaart
                    playablecardstatus = playableCard(chosencard)
                    if playablecardstatus == True:
                        del playerlist[currentplayer][chosencardposition]
                        gespeeldekaarten.insert(0,chosencard)
                        cardPlayed = True
                    elif playablecardstatus == False:
                        print("Kaart kan niet gespeeld worden. Probeer het opnieuw. Anders pak een kaart van de stapel")
                    else:
                        print(errormessage)
                else:
                    print(errormessage)
            else:
                print(errormessage)
    else:
        while cardPlayed == False:
            choosingcard = False
            dictCount = countAndSortDictinary()
            while choosingcard == False:
                # Check voor niet gekleurde kaarten
                if choosingcard == False:
                    for uncoloured in withoutColours:
                        for index, positions in enumerate(playerlist[currentplayer]):
                            if uncoloured in positions:
                                chosencard = playerlist[currentplayer][index]
                                choosingcard = True
                    if chosencard == None:
                        playablecardstatus = False
                    else:
                        playablecardstatus = playableCard(chosencard)
                        if playablecardstatus == True:
                            for index, positions in enumerate(playerlist[currentplayer]):
                                if chosencard == positions:
                                    break
                            del playerlist[currentplayer][index]
                            gespeeldekaarten.insert(0,chosencard)
                            cardPlayed = True
                # Check voor gekleurde kaarten
                if choosingcard == False:
                    # Scheid special en normal van elkaar
                    listSpecial = []
                    for specialunit in specialColoured:
                        for positions in playerlist[currentplayer]:
                            if specialunit in positions:
                                listSpecial.append(positions)
                    listNormal = []
                    for positions in playerlist[currentplayer]:
                        for numbers in range(9,-1,-1):
                            if str(numbers) in positions:
                                listNormal.append(positions)
                    continuecomfirmed = False
                    # Loop onder condities
                    while (len(listSpecial) > 0 and len(listNormal) > 0) and continuecomfirmed == False:
                        chosencard = normalOrSpecial(listNormal, listSpecial)
                        choosingcard = True
                        # Check als choosingcard gelijk staat aan None
                        if chosencard == None:
                            playablecardstatus = False
                        else:
                            playablecardstatus = playableCard(chosencard)
                            if playablecardstatus == True:
                                for index, positions in enumerate(playerlist[currentplayer]):
                                    if chosencard == positions:
                                        break
                                del playerlist[currentplayer][index]
                                gespeeldekaarten.insert(0,chosencard)
                                continuecomfirmed = True
                                cardPlayed = True
                            else:
                                if len(listSpecial) > 0:
                                    for index, positions in enumerate(listSpecial):
                                        if chosencard in positions:
                                            del listSpecial[index]
                                elif len(listNormal) > 0:
                                    for index, positions in enumerate(listNormal):
                                        if chosencard in positions:
                                            del listNormal[index]
                                else:
                                    grabCards(1, True, False)
                                    cardPlayed = True
                                    break
                    # grabCards(1, True, False)
                    # cardPlayed = True
                                

    # Laat zien wat er gespeeld wordt
    showcurrentplayernumber = ""
    if rotation == "forward":
        showcurrentplayernumber = currentplayer + 1
    elif rotation == "backwards":
        showcurrentplayernumber = currentplayer - 1
    else:
        None

    print("Speler", str(showcurrentplayernumber), "speelt:", chosencard)

    # Speciale kaarten functie calls
    if 'neem-twee' in chosencard:
        grabCards(2, False, True)
    elif 'neem-vier' in chosencard:
        grabCards(4, False, True)
        mustcolour = colourChoice()
        Colouradjustmentcheck = True
    elif 'keer-om' in chosencard:
        rotationGame()
        nextinline(1)
    elif 'sla-beurt-over' in chosencard:
        skipTurn()
    elif 'keuzekaart' in chosencard:
        mustcolour = colourChoice()
        nextinline(1)
        Colouradjustmentcheck = True
    else:
        nextinline(1)
    
    topcard = gespeeldekaarten[0]
    sleep(1)
    print("Huidige kaart boven op de speelstapel:", topcard)
    sleep(2)