f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

position = [0, 0]   #position is in [y , x] format
boomCount = 0
nextPos = 0

for i in data:
    if position[0] == 0:
        position[1] += 1
    elif position[0] == 1:
        position[1] -= 1
    #print("position = ", position)

    if i[position[1]] == "#":
        #print("Boom encountered")
        boomCount += 1
        newString = i[:position[1]] + "X" + i[position[1]+1:]
    else:
        newString = i[:position[1]] + "O" + i[position[1]+1:]
    print(newString)
    #bovenstaande laat de gecheckte string zien met de gecheckte positie als X

    if len(i) <= position[1] + 3:
        position[1] = len(i) - position[1] -1
    else:
        position[1] += 3
    position[0] += 1

print("er zijn ", boomCount, " bomen gevonden!")