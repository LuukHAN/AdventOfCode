f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

startNumb = 0
endNumb = 0
letterCount = 0
validCount = 0
letterCheck = 0

for i in data:
    range = i.split(" ")[0]
    letter = i.split(" ")[1]
    letter = letter[:1]
    password = i.split(" ")[2]
    letterCount = 0
    range = range.split("-")
    startNumb = int(range[0])
    endNumb = int(range[1])
    letterCheck = 0

    startNumb -= 1 #Dit is nodig omdat het wachtwoord geen index[0] gebruikt
    endNumb -= 1


    if password[startNumb] == letter:
       letterCheck += 1
    if password[endNumb] == letter:
        letterCheck += 1
    if letterCheck == 1:
        validCount += 1
print("validCount == ", validCount)