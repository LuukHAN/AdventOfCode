f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

#https://stackoverflow.com/questions/55986094/comparing-two-lists-element-wise-in-python
#overweeg de zip functie, het vergelijken is het probleem niet.
#Het gaat vooral om het lezen van de verschillende lijnen in een list

loopCount = 100

bingoNummers = []
bingoLine0 = []
bingoLine1 = []
bingoLine2 = []
bingoLine3 = []
bingoLine4 = []

for i in data:
    if loopCount == 100:
        #Deze code wordt alleen de allereerste keer uitgevoert
        bingoNummers = i.split(",")
        print(bingoNummers)
        loopCount = -2
    if loopCount > 4:
        loopCount = 0
    if loopCount == 0:
        bingoLine0 = i.split(" ")
        bingoLine0 = list(filter(None, bingoLine0)) #Voorkomt dat er lege entries zijn in de list, dus de index van de getallen zijn hetzelfde.
    if loopCount == 1:
        bingoLine1 = i.split(" ")
        bingoLine1 = list(filter(None, bingoLine1))
    if loopCount == 2:
        bingoLine2 = i.split(" ")
        bingoLine2 = list(filter(None, bingoLine2))
    if loopCount == 3:
        bingoLine3 = i.split(" ")
        bingoLine3 = list(filter(None, bingoLine3))
    if loopCount == 4:
        bingoLine4 = i.split(" ")
        bingoLine4 = list(filter(None, bingoLine4))
        loopCount = -2
    loopCount += 1

print(bingoLine4)