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
    for item in string_list:
        number_list = []
        for index, letter in enumerate(item):
            if letter == "t":
                if item[index+1:index+2] == "wo":
                    number_list.append(2)
            if letter == "o":



if __name__ == "__main__":
    cali = read_file("input.txt")
    ints = get_ints(cali)
    output = get_first_n_last(ints)
    print(output)
