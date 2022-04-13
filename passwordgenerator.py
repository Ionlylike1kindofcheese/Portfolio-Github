import random

uppercases = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowercases = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
specialsymbols = ["@", "#", "$", "%", "&", "_", "?"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

completion = False

def generator():
    password = ""
    passwordlength = 1
    symbolusage, numberusage, upperusage, lowerusage = 0, 0, 0, 0
    passwordlist = []
    while passwordlength < 25:
        chosensymbol, chosennumber, chosenupper, chosenlower = "", "", "", ""
        assignedteken = False
        tekenkeuze = random.randrange(1,5)

        if tekenkeuze == 1 and passwordlength in range(2,23) and symbolusage != 3:
            symbolchoice = random.randrange(0,7)
            chosensymbol = specialsymbols[symbolchoice]
            symbolusage += 1
        
        elif tekenkeuze == 2 and passwordlength > 3 and numberusage < 8:
            numberchoice = random.randrange(0,10)
            chosennumber = numbers[numberchoice]
            numberusage += 1
        
        elif tekenkeuze == 3 and upperusage < 7:
            upperchoice = random.randrange(0,26)
            chosenupper = uppercases[upperchoice]
            upperusage += 1
        
        elif tekenkeuze == 4:
            lowerchoice = random.randrange(0,26)
            chosenlower = lowercases[lowerchoice]
            lowerusage += 1

        if chosensymbol != "":
            currentteken = chosensymbol
            assignedteken = True
        elif chosennumber != "":
            currentteken = chosennumber
            assignedteken = True
        elif chosenupper != "":
            currentteken = chosenupper
            assignedteken = True
        elif chosenlower != "":
            currentteken = chosenlower
            assignedteken = True

        if assignedteken == True:
            passwordlist.append(currentteken)
            passwordlength += 1
    
    if symbolusage == 3 and numberusage > 4 and upperusage > 2 and lowerusage > 8:
        for x in passwordlist:
            password += x
        succesorfailure = True
    else:
        succesorfailure = False
    
    return password, succesorfailure

while completion == False:
    showpassword, results = generator()
    if results == False:
        None
    elif results == True:
        print("Password =", showpassword)
        completion = True