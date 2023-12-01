f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

command = []
tree = []
inhoud = []
newComFound = False
x = 0
# for i in range(len(data)):
#     if "$" in data[i]:
#         command = data[i].split(" ")
#         if command[1] == "ls":
#             newComFound = False
#             x = i
#             while newComFound == False:
#                 if "$" in data[x+1]:
#                     newComFound = True
#                 if "dir" not in data[x]:
#                     inhoud = data[x].split(" ")
#                 x += 1
##################################################################
# root = []
# workingDir = []
# depthCount = 0
# for i in range(len(data)):
#     if "$" in data[i]:
#         command = data[i].split(" ")
#         if command[1] == "ls":
#             for j in range(i,len(data)):
#                 if "$" in data[j]:
#                     continue
#                 else:
#                     root[depthCount].append(data[j])
#     print(root)
currentDir = ""
filesystem = {}
for line in data:
    line=line.strip().split(" ")
    if line[0] == "$":
        if line[1] == "ls":
            pass
        elif line[1] == "cd":
            if line[2] == "..":
                subpaths = currentDir.split("/")
                currentDir = ""

                for i in range(len(subpaths)-1):
                    if subpaths[i] != "":
                        currentDir += ("/" + subpaths[i])
                if currentDir == "":
                    currentDir = "/"
            
            elif line[2] == "/":
                currentDir = "/"
            else:
                if currentDir == "/":
                    currentDir += line[2]
                else:
                    currentDir += "/" + line[2]
        else:
            if line[0] == "dir":
               pass
            else:
                if currentDir == "/" :
                    filesystem.update({currentDir+line[1]:line[0]})
                else:
                    filesystem.update({currentDir+"/"+line[1]:line[0]})
        print("dir", currentDir)
        print("\n")
        print(filesystem)