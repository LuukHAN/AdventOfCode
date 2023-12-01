""""
Name: Luuk van Ham
Function: Advent of code 2019, Day 2, part 1
Date of creation: 24-10-2023
Inspiration: This code was created as practice for the exam.
"""
def readFile(inputBestand):
    """
    Reading the given file
    :param inputBestand: str, path to the file
    :return conten: list, split on commas of given file
    """
    with open(inputBestand, "r") as f:
        data = f.read()
    data = data.replace("\n", "")
    data = data.split(",")
    return data

def strListToInt(strList):
    """
    Converting a list of strings to a list of intergers
    :param strList: list, a list where the contents are strings but all numbers
    :return content: list, the same list but everything in it is an interger
    """
    try:
        output = [eval(i) for i in strList]
    except:
        print("Er zit een niet int character in de lijst, het converten is overgeslagen.")
        print(strListToInt)
    return output

def calculate(input):
    """
    Calculating with positions and gravity asists, look for more info on https://adventofcode.com/2019/day/2
    :param input: list, the list of input values
    :return content: whatever ends up at position 0 of the list
    """
    input = strListToInt(input)
    for index, string in enumerate(input):
        if index % 4 != 0:
            continue
        if string == 1 or string == 2:
            firstPos = input[index+1]
            secPos = input[index+2]
            replacePos = input[index + 3]
        if string == 99:
            continue
        elif string == 1:
            replaceWith = input[firstPos] + input[secPos]
        elif string == 2:
            replaceWith = input[firstPos] * input[secPos]
        input[replacePos] = replaceWith
        
    # print(input[1:3])
    return(input[0])

if __name__ == "__main__":
    UI = int(input("Wil je deel 1 of deel 2 uit voeren? [1/2]: "))
    inputBestand = "E:\\Documents\\Prive\\AdventOfCode\\2019\\Dag_2\\Input.txt"
    input = readFile(inputBestand)

    if UI == 1:
        print(calculate(input))
    elif UI == 2:
        for i in range(0, 100):
            input[1] = str(i)
            for j in range(0, 100):
                input[2] = str(j)
                output = calculate(input)
                if output == 19690720:
                    print(input[1:3])
                    exit()