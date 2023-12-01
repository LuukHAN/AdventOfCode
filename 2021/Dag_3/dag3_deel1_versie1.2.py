f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]
#als ik hier boven int(x) gebruik worden 
#de leading 0's weggehaald, als ik er een string
#van maak is dat geen probleem
#aankijken of het een probleem wordt dat het een string 
#is, anders een andere optie zoeken

oneCount = 0
zeroCount = 0
currentPos = 0
checkVal = 0
endGammaVal = ""
endEpsilonVal = ""

#De 0-en aan het begin worden weggehaald door python
#Hoe zorg ik ervoor dat die blijven staan??
for i in data:
    print(i)
    for i in data:
        try:
            checkVal = str(i[currentPos])
            #print(checkVal, " = checkVal")
            if checkVal == "0":
                zeroCount += 1
            elif checkVal == "1":
                oneCount += 1
            else:
                #print("er is iets fout gegaan")
                exit
        except:
            #print(endGammaVal, " = endGammaVal")
            exit

    if currentPos != (len(data)):
        currentPos += 1
        if zeroCount > oneCount:
            endGammaVal = endGammaVal + "0"
        elif oneCount > zeroCount:
            endGammaVal = endGammaVal + "1"
        else:
            #print("wat moet er gebeuren als ze gelijk zijn?")
            exit
    else:
        exit
    zeroCount = 0
    oneCount = 0

#Als dit allemaal is uitgevoert heb je de binaire waarde in endGammaVal opgeslagen
#Voor Gamma, nu moet dit allemaal nog een keer maar dan andersom voor de
#epsilon rate.
oneCount = 0
zeroCount = 0
currentPos = 0
checkVal = 0
for i in data:
    for i in data:
        try:
            checkVal = str(i[currentPos])
            if checkVal == "0":
                zeroCount += 1
            elif checkVal == "1":
                oneCount += 1
            else:
                exit

        except:
            exit

    if currentPos != (len(data)):
        currentPos += 1
        if zeroCount < oneCount:
            endEpsilonVal = endEpsilonVal + "0"
        elif oneCount < zeroCount:
            endEpsilonVal = endEpsilonVal + "1"
        else:
            exit
    else:
        exit
    zeroCount = 0
    oneCount = 0
convertNumb = 0
def binaryToDeci(convertNumb):
    if(convertNumb == 0):
        return 0
    return(convertNumb % 10 + 2 * binaryToDeci(convertNumb // 10))

endEpsilonVal = int(endEpsilonVal)
endGammaVal = int(endGammaVal)
endEpsilonVal = binaryToDeci(endEpsilonVal)
endGammaVal = binaryToDeci(endGammaVal)

powerConsum = endEpsilonVal * endGammaVal
print("De totale powerconsumtie = ", powerConsum)