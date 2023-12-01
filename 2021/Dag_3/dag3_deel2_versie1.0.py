f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ int(x) for x in data ]

Aval = 0
BVal = 0
CVal = 0
currentPos = 0
print(data)

for i in data:
    print(i)
    Aval = str(i[currentPos])
    Bval = str(i[currentPos +1])
    CVal = str(i[currentPos +2])
    print(Aval, " = A")
    print(Bval, " = B")

    