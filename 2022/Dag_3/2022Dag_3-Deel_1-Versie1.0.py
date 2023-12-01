f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

firstHalf = []
secondHalf = []
null = 0
alphaCount = [] #Dit wordt gebruikt om bij te houden hoe veel van welke characters er zijn geweest.
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letterPos = 0
score = 0
for i in alphabet:
    alphaCount.append(null)
for i in data:
    i = [i for i in i] #zet i om van string naar list
    firstHalf = i[:len(i)//2]
    secondHalf = i[len(i)//2:]
    for j in firstHalf:
        if j in secondHalf:
            score = score + alphabet.find(j) + 1
            break
print("score = ",score)