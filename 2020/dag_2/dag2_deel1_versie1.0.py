f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

startNumb = 0
letterCount = 0
loopCount = 0
validCount = 0

for i in data:
    range = i.split(" ")[0]
    letter = i.split(" ")[1]
    letter = letter[:1]
    password = i.split(" ")[2]
    letterCount = 0
    range = range.split("-")
    startNumb = int(range[0])
    endNumb = int(range[1])

    #bovenstaande zorgt dat het minimum aantal in startNumb wordt opgeslagen
    #het maximum aantal wordt in endNumb opgeslagen.

    #bij onderstaande moet het vergeleken worden en getest of het een correct wachtwoord is
    #Hierbij gaat nog iets fout geloof ik

    for j in password:
        if letter == j:
            letterCount += 1
    if letterCount <= endNumb:
        if letterCount >= startNumb:
            validCount += 1
            print("valid")
        else:
            print("invalid")
    else:
        print("Invalid")
print(validCount)