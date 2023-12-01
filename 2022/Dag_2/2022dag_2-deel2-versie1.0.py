f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

currentRound = []
score = 0
for i in data:
    currentRound = i.split(" ")
    if currentRound[0] == "A":      #hij speelt rock
        if currentRound[1] == "X":      #V
            score = score + 0   #
            score = score + 3   #
        elif currentRound[1] == "Y":    #D
            score = score + 3   #
            score = score + 1   #
        elif currentRound[1] == "Z":    #W
            score = score + 6   #
            score = score + 2   #
    elif currentRound[0] == "B":    #hij speelt paper
        if currentRound[1] == "X":
            score = score + 0   #
            score = score + 1   
        elif currentRound[1] == "Y":
            score = score + 3
            score = score + 2
        elif currentRound[1] == "Z":
            score = score + 6
            score = score + 3
    elif currentRound[0] == "C":    #hij speelt scissors
        if currentRound[1] == "X":
            score = score + 0
            score = score + 2
        elif currentRound[1] == "Y":
            score = score + 3
            score = score + 3
        elif currentRound[1] == "Z":
            score = score + 6
            score = score + 1
print("score = ", score)

        