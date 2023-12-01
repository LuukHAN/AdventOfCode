f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

horizontal = 0
depth = 0
aim = 0
finalPos = 0
changeVal = 0

for i in data:
    changeVal = int(i[-1])
    if "forward" in i:
        horizontal += changeVal
        depth = depth + aim * changeVal
    elif "down" in i:
        aim += changeVal
        #mogelijk ook nog depth veranderen
    elif "up" in i:
        aim -= changeVal
    else:
        print("Er is wat fout gegaan")
finalPos = depth * horizontal
print ("finalPos = ", finalPos)