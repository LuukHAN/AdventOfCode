f = open("Input.txt", "r")
data = f.read()
#data = [data for data in data]
prevLet = []
print(data)
mySet = {}
for i in range(len(data)):
    if len(prevLet) == 14:
        mySet = set(prevLet)
        if len(mySet) == len(prevLet):
            print(mySet, " == ", prevLet)
            print(i)
            break
    prevLet.append(data[i])
    if len(prevLet) > 14:
        del prevLet[0]