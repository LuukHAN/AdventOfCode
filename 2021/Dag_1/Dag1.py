f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ int(x) for x in data ]
increaseCount = 0
i = 0
oldDepth = 0
for i in data:
    if i >= 10:
        exit
    print(i, " is data[i]")
    if i > 1:
        if oldDepth > i:
            increaseCount += 1
    oldDepth = data[i]
print("De waarde is ",increaseCount, "keer groter geworden")