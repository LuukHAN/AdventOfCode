f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ int(x) for x in data ]

increaseCount = 0
valGroup = 0
firstVal = 0
secVal = 1
ThirdVal = 2
sumVal = []


for i in data:
    sum = data[firstVal] + data[secVal] + data[ThirdVal]
    if ThirdVal != (len(data)-1):
        firstVal += 1
        secVal += 1
        ThirdVal += 1
    else:
        sum = data[-1] + data[-2] + data[-3]
        sumVal.append(sum)
        break
    sumVal.append(sum)
    print(i)
#print(sumVal)

#Het deel hierboven zorgt ervoor dat de data in een array komt
#Nu is het een kwestie van het script van deel 1 over deze array 
#laten gaan en dan werkt het. Dat is wat hieronder komt.

j = 1
oldDepth = sumVal[0]
for j in sumVal:
    if j > oldDepth:
        increaseCount +=1
    oldDepth = j
print("de waarde is ",increaseCount," keer toegenomen")