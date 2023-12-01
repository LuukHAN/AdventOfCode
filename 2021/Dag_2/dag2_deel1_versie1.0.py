f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]
#let hierbij op dat [ str(x) ] in dit geval str is en niet int
#dit is afhankelijk van wat je probeert te lezen.

horizontal = 0
depth = 0
finalPos = 0

for i in data:
    #Hoe haal je een integer uit een string
    #Hij pakt het laatste karakter van i
    changeVal = int(i[-1])
    if "forward" in i:
        horizontal += changeVal
    elif "down" in i:
        depth += changeVal
    elif "up" in i:
        depth -= changeVal
    else:
        print("Er is wat fout gegaan")
finalPos = depth * horizontal
print(finalPos)