f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

horizontalPos = 0
boomCount = 0
keepLoop = 0
keepSecLoop = 0

while keepLoop == 0:
    for i in data:
        if keepSecLoop == 0:
            if i[horizontalPos] == "#":
                print("Boom encountered")
                boomCount += 1
            horizontalPos += 3
            try:
                if i[horizontalPos] == "#":
                    print("test")
            except:
                keepLoop = 1
                keepSecLoop = 1
                continue
print("er zijn ", boomCount, " bomen die in de weg stonden!")

#geprobeerde nummers:
#                    86