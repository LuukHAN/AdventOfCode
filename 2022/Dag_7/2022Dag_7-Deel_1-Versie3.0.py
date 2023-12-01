f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]


myDictionaryFellOff = {}#{location:size,etc}
currentDir = ""
fileProps = []
score = 0
for line in data:
    line = line.strip().split(" ")
    if "$" in line:
        if line[1] == "cd":
            if line[2] != "..":
                currentDir+= line[2]
                print(currentDir)
            elif line[2] == "..":
                if currentDir != "/":
                    currentDir = currentDir[-1]
                elif currentDir == "":
                    currentDir = "/"
            if currentDir != "/":
                currentDir += "/"
        
        elif line[1] == "ls":
            continue    #als er een $ in zit, en het is niet cd hoeft er niets met die regel
####
#opslaan hoe groot de bestanden zijn en op welke locatie ze staan
    else:   #Het begint of met een nummer of met dir
        if line[0] == "dir":
            print(line[1])
            # line[1] = line[1].split(" ")
            print(type(line))
            myDictionaryFellOff.update({currentDir+"submappie="+line[1]:0})
        else:
            line[0] = int(line[0])
            myDictionaryFellOff.update({currentDir+line[1]:line[0]})
    print(myDictionaryFellOff)

currentDir = ""
smallMapCount = 0
subMamExist = False
for lineNumb in range(len(data)):
    data[lineNumb] = data[lineNumb].strip().split(" ")
    if "$" in data[lineNumb]:
        if data[lineNumb][1] == "cd":
            if data[lineNumb][2] != "..":
                currentDir+= data[lineNumb][2]
            elif data[lineNumb][2] == "..":
                if currentDir != "/":
                    currentDir = currentDir[-1]
                elif currentDir == "":
                    currentDir = "/"
            if currentDir != "/":
                currentDir += "/"
        
        elif data[lineNumb][1] == "ls":
            continue
    print(currentDir)
    fileExist = False
    fileIsFolder = False
    fileSize = 0
    safeSize = 0
    skipLoop = False
    for i in myDictionaryFellOff:
        if skipLoop == True:
            skipLoop = False
            continue
        fileExist = i.startswith(currentDir)
        if fileExist == True:
            fileSize = fileSize + myDictionaryFellOff[i]
            skipLoop = True
            continue
    if fileSize != 0 and safeSize != fileSize:
        if fileSize < 100000:
            print("kleiner dan 100.000, namelijk: ", fileSize)
            smallMapCount += 1
            score += fileSize
            safeSize = fileSize
            print("safeSize = ", safeSize)
            print("fileSize = ", fileSize)
print("Er zijn ",smallMapCount," mappen met een totale som van ",score)