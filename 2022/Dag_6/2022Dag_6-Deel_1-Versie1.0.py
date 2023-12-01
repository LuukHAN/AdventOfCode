f = open("Input.txt", "r")
data = f.read()
#data = [data for data in data]
prevLet = []
print(data)
mySet = {}
for i in range(len(data)):
    if len(prevLet) == 4:
        mySet = set(prevLet)
        if len(mySet) == len(prevLet):
            print(mySet, " == ", prevLet)
            print(i)
            break
    mySet = {}
    prevLet.append(data[i])
    if len(prevLet) > 4:
        del prevLet[0]

#Een set kan alleem maar unieke values dragen,
#dit zorgt ervoor dat als er velden hetzelfde zijn
#de string korter is, is dit niet het geval: zijn het 4 unieke letters
