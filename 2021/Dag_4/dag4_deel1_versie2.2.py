f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]


#https://stackoverflow.com/questions/55986094/comparing-two-lists-element-wise-in-python
#overweeg de zip functie, het vergelijken is het probleem niet.
#Het gaat vooral om het lezen van de verschillende lijnen in een list

lineCount = 100
loopCount = 0

bingoNummers = []
bingoLine0 = []
bingoLine1 = []
bingoLine2 = []
bingoLine3 = []
bingoLine4 = []

for h in data:
    if lineCount == 100:
        bingoNummersCheck = h
        bingoNummers = h.split(",")
        
        print(bingoNummers)
        lineCount = 0
bingoNummers = [int(a) for a in bingoNummers]#omzetten naar intergers
#print(type(bingoNummers[0]))
print(lineCount)

for j in range(len(bingoNummers)):
    print(j, "= j")
    lineCount = -2
    i = 0
    for i in data:
        print(lineCount, "= linecount")

        #print(i)
        if i == bingoNummersCheck:
            continue

        if lineCount > 4:
            lineCount = 0
            print("linecount gaat terug naar 0")
        if lineCount == 0:
            bingoLine0 = i.split(" ")
            bingoLine0 = list(filter(None, bingoLine0)) #Voorkomt dat er lege entries zijn in de list, dus de index van de getallen zijn hetzelfde.
            #bingoLine0 = [int(a) for a in bingoLine0]
            lineCount += 1
        if lineCount == 1:
            bingoLine1 = i.split(" ")
            bingoLine1 = list(filter(None, bingoLine1))
            #bingoLine1 = [int(a) for a in bingoLine1]
            lineCount += 1
        if lineCount == 2:
            bingoLine2 = i.split(" ")
            bingoLine2 = list(filter(None, bingoLine2))
            #bingoLine2 = [int(a) for a in bingoLine2]
            lineCount += 1
        if lineCount == 3:
            bingoLine3 = i.split(" ")
            bingoLine3 = list(filter(None, bingoLine3))
            #bingoLine3 = [int(a) for a in bingoLine3]
            lineCount += 1
        if lineCount == 4:
            bingoLine4 = i.split(" ")
            bingoLine4 = list(filter(None, bingoLine4))
            #bingoLine4 = [int(a) for a in bingoLine4]
            #lineCount = 3
        #Vanaf hier wordt er gecheckt of het nummer voorkomt, als dat het geval is wordt dat nummer gereplaced met 101
        if lineCount < 0:
            lineCount += 1

        try:
            if bingoLine0[i] == j:
                bingoLine0[i] = 101
                print(j ," komt voor")
            elif bingoLine1[i] == j:
                bingoLine1[i] = 101
            elif bingoLine2[i] == j:
                bingoLine2[i] = 101
            elif bingoLine3[i] == j:
                bingoLine3[i] = 101
            elif bingoLine4[i] == j:
                bingoLine4[i] = 101
            else:
                print(j, " komt niet voor")
        except:
            #print("continue")
            continue
        loopCount += 1
print(bingoLine0)
print(bingoLine1)
print(bingoLine2)
print(bingoLine3)
print(bingoLine4)