f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

loopCount = 0
bingoLineCount = 0
bingoKaart = []
bingoLine1 = []
bingoLine2 = []
bingoLine3 = []
bingoLine4 = []
bingoLine5 = []
for i in data:
    if loopCount == 0:
        list = i.split(",")
        print(list)
    if i == "":
        bingoLine1.clear()
        bingoLine2.clear()
        bingoLine3.clear()
        bingoLine4.clear()
        bingoLine5.clear()
        #print(bingoLine1)
        bingoLineCount = 1
        continue
    bingoLine(bingoLineCount) = i.split(" ")
    #Bovenstaande werkt niet, mogelijk lines in een array (list) gooien en dat vergelijken
    #is wel de nettere oplossing, maar deze vind ik overzichtelijker...+
    #bingoKaart = [bingoLine1, bingoLine2, bingoLine3, bingoLine4]
    print(bingoKaart)

    bingoLineCount += 1
    loopCount += 1
#line for line in een array gooien, vervolgens
#checken of lst[0] geweest is, dan of lst2[0] geweest is
#delimit bij blank line
#if i == ""
#   continue