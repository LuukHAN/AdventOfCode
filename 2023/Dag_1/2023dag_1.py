import re

def read_file(input_bestand):
    with open(input_bestand, "r") as file:
        input_data = file.read().splitlines()
    return input_data


def get_ints(list):
    number_container = []
    for item in list:
        number_list = []
        for letter in item:
            try:
                number = int(letter)
                number_list.append(number)
            except ValueError:
                continue
        number_container.append(number_list)
    return number_container


def get_first_n_last(list_list):
    total = 0
    for numbers in list_list:
        first_numb = str(numbers[0])
        last_numb = str(numbers[-1])
        add_numb = int(first_numb + last_numb)
        total += add_numb
    return total


def get_lit_numbs(string_list):
    parent_numb_list = []
    for item in string_list:
        item = item.lower()
        numb_list = check_numb(item)
        parent_numb_list.append(numb_list)
    # print(parent_numb_list)
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
        "nine": 9
        #"zero": 0
    }
    numb_on_pos_dict = {}

    for lit_number in number_dict.keys():
        found_pos = txt_line.find(lit_number)
        if found_pos != -1:
            numb_on_pos_dict.update({number_dict[lit_number]: found_pos})

    for int_number in number_dict.values():
        int_number = str(int_number)
        found_int_pos = txt_line.find(int_number)
        if found_int_pos != -1:
            numb_on_pos_dict.update({int_number: found_int_pos})
    gesorteerde_keys = sorted(numb_on_pos_dict, key=numb_on_pos_dict.get)
    return gesorteerde_keys


def get_output(big_list):
    total = 0
    print(big_list)
    for small_list in big_list:
        add_value = ""
        add_value = str(small_list[0]) + str(small_list[-1])
        add_value = int(add_value)
        total += add_value
    return total


if __name__ == "__main__":
    cali = read_file("input.txt")
    lit_numbs = get_lit_numbs(cali)
    output = get_output(lit_numbs)
    print(output)
    # output = get_first_n_last(ints)
    # print(ints)
