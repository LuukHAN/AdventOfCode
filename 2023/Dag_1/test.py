import re

def read_file(input_bestand):
    with open(input_bestand, "r") as file:
        input_data = file.read().splitlines()
    return input_data

def get_lit_numbs(string_list):
    parent_numb_list = []
    for item in string_list:
        numb_list = check_numb(item)
        parent_numb_list.append(numb_list)
    return parent_numb_list

def check_numb(txt_line):
    number_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0
    }
    numb_str = ""

    for lit_number in number_dict.keys():
        found_pos = txt_line.find(lit_number)
        if found_pos != -1:
            numb_str += str(number_dict[lit_number])

    return numb_str

def get_output(big_list):
    total = 0
    for small_list in big_list:
        if small_list:  # Check if the list is not empty
            add_value = int(small_list)
            total += add_value
    return total

if __name__ == "__main__":
    cali = read_file("input.txt")
    lit_numbs = get_lit_numbs(cali)
    output = get_output(lit_numbs)
    print(output)
