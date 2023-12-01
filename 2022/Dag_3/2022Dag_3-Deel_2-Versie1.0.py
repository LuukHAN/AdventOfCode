f = open("Input.txt", "r")
data = f.read().splitlines()
data = [ str(x) for x in data ]

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score = 0
skip = False
skipCount = 0
for i in range(len(data)):
    if skip == True:
        if skipCount == 2:
            skip = False
            skipCount = 0
        else:
            skipCount += 1
            continue
    data[i] = [data[i] for data[i] in data[i]] #zet data[i] om van string naar list
    try:
        for j in data[i]:
            if j in data[i +1]:
                if j in data[i +2]:
                    score = score +alphabet.find(j) +1
                    print(j)
                    skip = True
                    break
                else:
                    continue
    except:
        continue
print("score = ",score)