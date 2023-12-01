f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

# stapel1 = ["[N]", "[Z]"]
# stapel2 = ["[D]", "[C]", "[M]"]
# stapel3 = ["[P]"]
# stapels = [stapel1,stapel2,stapel3]

stapel1 = ["G","W","L","J","B","R","T","D"]
stapel2 = ["C","W","S"]
stapel3 = ["M","T","Z","R"]
stapel4 = ["V","P","S","H","C","T","D"]
stapel5 = ["Z","D","L","T","P","G"]
stapel6 = ["D","C","Q","J","Z","R","B","F"]
stapel7 = ["R","T","F","M","J","D","B","S"]
stapel8 = ["M","V","T","B","R","H","L"]
stapel9 = ["V","S","D","P","Q"]
stapels = [stapel1,stapel2,stapel3,stapel4,stapel5,stapel6,stapel7,stapel8,stapel9]
move = []
eindString = ""
for i in range(len(data)):
    if "m" not in data[i]:
        continue
    move = data[i].split(" ")
    del move[0]
    del move[1]
    del move[2]
    move = [eval(x) for x in move]
    #move = [int(s) for s in data[i] if s.isdigit()]
    print("move = ", move)
    move[1] -= 1
    move[2] -= 1
    for j in range(0,move[0]):
        try:
            stapels[move[2]].insert(0, stapels[move[1]][0])
            del stapels[move[1]][0]
        except:
            #print("Gaat fout")
            continue
for i in stapels:
    try:
        eindString = eindString + i[0]
    except:
        continue
print(eindString)

#Het gaat fout omdat als het getal uit 2 of meer characters bestaat,
#wordt het alsnog gesplit op individuele intergers