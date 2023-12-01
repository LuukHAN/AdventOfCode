f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

calcCal = []
calorie = []
sumCal = 0
sumTopThree = 0
for i in data:
    if i == "":
        for j in calcCal:
            j = int(j)
            sumCal = j + sumCal
        calorie.append(sumCal)
        sumCal = 0
        calcCal = []
        continue
    calcCal.append(i)
calorie.sort()
sumTopThree = sumTopThree + calorie[-1]
sumTopThree = sumTopThree + calorie[-2]
sumTopThree = sumTopThree + calorie[-3]
print(sumTopThree)