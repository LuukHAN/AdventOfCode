f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

calorie = []
calcCal = []
sumCal = int(0)
keepLoop = True
for i in data:
    sumCal = 0
    calcCal.append(i)
    #print(calcCal)
    if i == "":
        for j in calcCal:
            print(j)
            try:
                sumCal = j + sumCal
                print("sumCal = ", sumCal)
            except:
                calcCal = []
                continue
    calorie.append(sumCal)
print(calorie)