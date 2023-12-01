f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

myDictionaryFellOff = {}
currentDir = ""
for line in data:
    line = line.strip().split(" ")#split op de spaties en haal de spaties eruit
    if "$" in line:
        if line[1] == "cd":
            if line[2] == "..":
                subpaths = currentDir.split("/")
                currentDir = ""
                print(subpaths)

                for a in range(len(subpaths)-1):
                    if subpaths[a] != "":
                        currentDir +=("/"+subpaths[a])
                if currentDir == "":
                    currentDir = "/"
            if line[2] == "/":
                currentDir = "/"
            else:
                if currentDir == "/":
                    currentDir += line[2]   #als je al root bent hoeft er geen/ toegevoegd te worden
                else:
                    currentDir += "/"+line[2]

    #de mappen structuur is nu in kaart gebracht
print(myDictionaryFellOff)