def read_file(input_file):
    with open(input_file, "r") as file:
        data = file.read()
    return data


def check_dupes(int_string):
    total_sum = 0
    for index, number in enumerate(int_string):
        if index == len(int_string)-1:
            if number == int_string[0]:
                number = int(number)
                total_sum += number
        elif number == int_string[index+1]:
            number = int(number)
            total_sum += number
    return total_sum


def part_2(int_string):
    for index, number in enumerate(int_string):


def out_of_range_check(int_string, index):
    """
    check if the index + len(int_string)/2 falls out of range
    if it does, continue on first character
    return on whatever you land
    :param int_string:  string of all the numbers
    :param index: number to check position
    :return: the character on index + len(int_string)/2
    """
    comp_pos = 0
    expected_pos = 0
    if index + len(int_string)/2 > len(int_string):
        comp_pos = (index + len(int_string)/2) - len(int_string)

if __name__ == "__main__":
    input_data = read_file("input.txt")
    part = 2
    if part == 1:
        complete_sum = check_dupes(input_data)
        print("complete sum = ", complete_sum)
    elif part == 2:
        complete_sum = part_2(input_data)