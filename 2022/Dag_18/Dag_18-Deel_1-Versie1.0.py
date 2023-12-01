f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]


mySet = {}
mySecondSet = {}
for i in range(len(data)):
    mySecondSet = {data[i]}
    mySet = mySet + mySecondSet
    print(len(mySet))