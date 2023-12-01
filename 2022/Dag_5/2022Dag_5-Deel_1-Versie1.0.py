f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

stapel1 = []
stapel2 = []
stapel3 = []
stapel4 = []
stapel5 = []
stapel6 = []
stapel7 = []
stapel8 = []
stapel9 = []
stapels = []
charPos = 0
fillVar = ""
for i in range(len(data)):
    if data[i] == " 1   2   3 " or i == " 1   2   3   4   5   6   7   8   9 ":
        break
    for j in range(0,3):
        fillVar = fillVar + data[i][charPos]
        charPos += 1
    charPos += 1
    stapels.append(fillVar) 
    fillVar = ""
print(stapels)