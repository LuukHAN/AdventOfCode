f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

score = 0
tallestTree = False
for i in range(len(data)):
    data[i] = [int(data[i]) for data[i] in data[i]] #omzetten van string naar lijst met intergers
    for tree in range(len(data[i])):
        tallestTree = False
        
        for compTree in data[i]:    #check van links naar rechts
            if data[i][tree] > compTree:
                tallestTree = True
            if data[i][tree] < compTree:
                tallestTree = False
        
        if tallestTree == False:    #check verticaal van boven naar onder
            for compTree in range(len(data[i])):
                if data[i][tree] > data[compTree][tree]:    #[tree, tree, tree]
                    tallestTree = True                      #[  i,    i,    i ]
                elif data[i][tree] < data[compTree][tree]:
                    tallestTree = False
        
        if tallestTree == False:
            pass
    print(data[i])

score = score + len(data) * 2
score = score + len(data[i]) * 2    #Dit zorgt ervoor dat je weet hoeveel bomen er aan de boven en onderkant staan
score -= 4 #voor de corners
#Hier zou ook nog len(data) * 2 bij opgeteld moeten worden, hier zouden zoiezo 4 nog vanaf moeten omdat je anders bomen
#2 keer telt.
#maar als bomen aan de rand het hoogst zijn zorgt dat dat de uiteindelijke score te hoog wordt.
#je zou dus kunnen checken of het een rand boom is en dan inplaats van de score op te hogen de score verlagen.
#op die manier kan je die formule nog wel aan het einde toepassen.
print(score)

#Het zou verstandig kunnen zijn om de positie van een zichtbare boom op te slaan, vervolgens check je of hij van andere kanten ook zichtbaar is...
#het is mischien nog verstandiger om te zeggen dat als tallestTree True is, hij de rest niet meer checkt.