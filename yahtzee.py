import random

uppertotaalpunten = 0
lowertotaalpunten = 0
gamecount = 0

def firstdobbelwerp():
    dobbelstenen = []
    for x in range(5):
        currentdobbel = random.randrange(1,7)
        dobbelstenen.append(currentdobbel)
    return dobbelstenen


def rerollingnumbers(rerollpositions, previouslist):
    for z in rerollpositions:
        currentreroll = random.randrange(1,7)
        z -= 1
        previouslist[z] = currentreroll
    return previouslist


def calculatelowernumbercount(checkinglist):
    for c in range(1,7):
        numberCount = 0
        for b in range(5):
            if checkinglist[b] == c:
                numberCount += 1
            else:
                None
        if numberCount >= 3:
            return numberCount


def calculatelowerstraight(checkinglist):
    followupcount = 0
    for d in range(1,7):
        securitylayer = 0
        for e in range(5):
            if securitylayer >= 2:
                break
            elif checkinglist[e] == d:
                followupcount += 1
                securitylayer += 1
            else:
                None
        if securitylayer == 0:
            followupcount = 0
    return followupcount


def calculatelowerfullhouse(checkinglist):
    filledspots = 0
    for f in range(1,7):
        securitylayer = 0
        for g in range(5):
            if checkinglist[g] == f:
                filledspots += 1
                securitylayer += 1
            else:
                None
        if securitylayer < 2:
            filledspots -= securitylayer
    return filledspots


def calculateupperscore(checkinglist):
    for c in range(1,7):
        numberCount = 0
        for b in range(5):
            if checkinglist[b] == c:
                numberCount += 1
            else:
                None
        if numberCount >= 3:
            return numberCount, c


programcompletion = False
while programcompletion == False:
    dobbelstenenlist = firstdobbelwerp()
    werpcompletion = False
    rerollpogingen = 2
    while werpcompletion == False:
        if rerollpogingen == 0:
            print("Uw dobbelstenen =", dobbelstenenlist)
            werpcompletion = True
        else:
            print("Uw dobbelstenen =", dobbelstenenlist)
            OpzijOfRollen = input("Wilt u bepaalde dobbelstenen opnieuw rollen? (Antwoord met ja of nee) ")
            if OpzijOfRollen == "ja":
                rerollpogingen -= 1
                freezecurrentnumbers = False
                while freezecurrentnumbers == False:
                    rerolls = []
                    rerollposition = input("Welke dobbelstenen wilt u opnieuw gooien? (Schrijf de bepaalde dobbelstenen als nummers aan elkaar) ")
                    for x in rerollposition:
                        x = int(x)
                        rerolls.append(x)
                    freezecurrentnumbers = True
                    dobbelstenenlist = rerollingnumbers(rerolls, dobbelstenenlist)
            elif OpzijOfRollen == "nee":
                werpcompletion = True
            else:
                None


    punten = 0
    points = 0

    print("Bovenste vakken:")
    upperresult = calculateupperscore(dobbelstenenlist)
    if upperresult[0] >= 2:
        points = upperresult[0] * upperresult[1]
        print("+",points)

    print("onderste vakken:")
    fullhouseresult = calculatelowerfullhouse(dobbelstenenlist)
    if fullhouseresult == 5:
        print("Full house!!!")
        punten += 30
        print("+",punten)
    else:
        numbercountresult = calculatelowernumbercount(dobbelstenenlist)
        if numbercountresult == 3:
            print("Three of a kind!!!")
            for o in range(5):
                punten = punten + dobbelstenenlist[0]
                del dobbelstenenlist[0]
            print("+",punten)
        elif numbercountresult == 4:
            print("Four of a kind!!!")
            for o in range(5):
                punten = punten + dobbelstenenlist[0]
                del dobbelstenenlist[0]
            print("+",punten)
        elif numbercountresult == 5:
            print("Yahtzee!!!")
            punten += 50
            print("+",punten)
        else: 
            straightcountresult = calculatelowerstraight(dobbelstenenlist)
            if straightcountresult == 4:
                print("Small straight!!!")
                punten += 30
                print("+",punten)
            elif straightcountresult == 5:
                print("Large straight!!!")
                punten += 40
                print("+",punten)
            else:
                print("Chance!!!")
                for o in range(5):
                    punten = punten + dobbelstenenlist[0]
                    del dobbelstenenlist[0]
                print("+",punten)

    print()
    uppertotaalpunten += points
    lowertotaalpunten += punten
    print("punten in de bovenste vakken deze ronde:", points)
    print("punten in de onderste vakken deze ronde:", punten)
    print()
    print("totaal aantal punten tot nu toe in de onderste vakken:", uppertotaalpunten)
    print("totaal aantal punten tot nu toe in de onderste vakken:", lowertotaalpunten)

    gamecount += 1
    if gamecount == 6:
        programcompletion = True