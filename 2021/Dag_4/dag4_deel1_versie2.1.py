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
        bingoNummers = h.split(",")
        print(bingoNummers)
        lineCount = -2

#for j in bingoNummers:
    for i in data:
        if lineCount > 4:
            lineCount = 0
        if lineCount == 0:
            bingoLine0 = i.split(" ")
            bingoLine0 = list(filter(None, bingoLine0)) #Voorkomt dat er lege entries zijn in de list, dus de index van de getallen zijn hetzelfde.
        if lineCount == 1:
            bingoLine1 = i.split(" ")
            bingoLine1 = list(filter(None, bingoLine1))
        if lineCount == 2:
            bingoLine2 = i.split(" ")
            bingoLine2 = list(filter(None, bingoLine2))
        if lineCount == 3:
            bingoLine3 = i.split(" ")
            bingoLine3 = list(filter(None, bingoLine3))
        if lineCount == 4:
            bingoLine4 = i.split(" ")
            bingoLine4 = list(filter(None, bingoLine4))
            lineCount = -2
        lineCount += 1
        loopCount += 1
        try:
            if bingoLine0[loopCount] == h:
                bingoLine0[loopCount] = 101
        except:
            continue
print(bingoLine4)