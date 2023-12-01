f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

#X = rock, 1 points
#Y = Paper, 2 points
#Z = scissors, 3 points
 
#A = rock
#B = paper
#C = scissors

#0 if lost
#3 if draw
#6 if win

currentRound = []
score = 0

for i in data:
    currentRound = i.split(" ")
    if currentRound[1] == "X":
        score = score + 1
        if currentRound[0] == "A":
            score = score + 3   #0 punten omdat het gelijk is
        elif currentRound[0] == "B":
            score = score + 0   #lost
        elif currentRound[0] == "C":
            score = score + 6
    elif currentRound[1] == "Y":
        score = score + 2
        if currentRound[0] == "A":
            score = score + 6
        elif currentRound[0] == "B":
            score = score + 3
        elif currentRound[0]:
            score = score + 0
    elif currentRound[1] == "Z":
        score = score + 3
        if currentRound[0] == "A":
            score = score + 0
        elif currentRound[0] == "B":
            score = score + 6
        elif currentRound[0] == "C":
            score = score + 3
print("score = ",score)
