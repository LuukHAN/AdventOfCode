f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ int(x) for x in data ]

increaseCount = 0
i = 1
oldDepth = data[0]

for i in data:
    if i > oldDepth:
        increaseCount += 1
        print("increaseCount ++, total is: ", increaseCount)
    oldDepth = i
print("De waarde is ", increaseCount, " keer toegenomen")