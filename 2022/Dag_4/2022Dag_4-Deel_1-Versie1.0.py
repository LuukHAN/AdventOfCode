f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

containCount = 0
for i in data:
    i = i.replace("-",",")  #replace - with , so i can split on comma
    i = i.split(",")
    i = [int(i) for i in i] #omzetten van string naar int
    if i[0] <= i[2] and i[1] >= i[3]:
        containCount += 1
        print(i,"1")
    elif i[2] <= i[0] and i[3] >= i[1]:
        containCount += 1
        print(i,"2")
print(containCount)