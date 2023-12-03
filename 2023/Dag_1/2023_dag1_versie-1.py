import re


def read_file(input_bestand):
    with open(input_bestand, "r") as file:
        input_data = file.read().splitlines()
    return input_data


def find_numbers_in_line(input_data):
    search_words = "[1-9]|zero|one|two|three|four|five|six|seven|eight|nine"
    search_pattern = re.compile(search_words)
    # werkt redelijk, alleen krijg ik bij twone en oneight alleen two en one terug.
    # dit moet two one & one eight zijn.
    match_list = []
    for line in input_data:
        matches = [match.group() for match in search_pattern.finditer(line)]
        match_list.append(matches)
        print(matches)

    rev_search_words = search_words.split("|")
    rev_search_words = rev_search_words[1:]
    rev_search_words = [i[::-1] for i in rev_search_words]
    rev_search_words.append("[1-9]")
    rev_search_words = '|'.join(rev_search_words)
    rev_search_pattern = re.compile(rev_search_words)
    rev_match_list = []
    for rev_line in input_data:
        rev_line = rev_line[::-1]
        reverse_matches = [match.group() for match in rev_search_pattern.finditer(rev_line)]
        rev_match_list.append(reverse_matches)
    # print(f'match_list = {match_list}\nrev_match_list = {rev_match_list}') # [[two, 1, nine], [eight, three]]
    get_first_n_last(match_list, rev_match_list)


def conv_lit_to_int(string_list):
    number_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'zero': 0,
        'eno': 1,
        'owt': 2,
        'eerht': 3,
        'ruof': 4,
        'evif': 5,
        'xis': 6,
        'neves': 7,
        'thgie': 8,
        'enin': 9,
        'orez': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0
    }
    int_list = []

    for number in string_list:
        for lit_numb in number_dict.keys():
            if number == lit_numb:
                int_list.append(number_dict[lit_numb])
    print(int_list)
    return int_list


def get_first_n_last(forward_list, reverse_list):
    int_forward_list = []
    int_rev_list = []
    for row in forward_list:
        int_forward_list.append(conv_lit_to_int(row))
    for row in reverse_list:
        int_rev_list.append(conv_lit_to_int(row))
    add_first_n_last(int_forward_list, int_rev_list)


def add_first_n_last(first_twod_list, sec_twod_list):
    total = 0
    for list_count, numb_list in enumerate(first_twod_list):
        add_val = str(numb_list[0]) + str(sec_twod_list[list_count][0])
        print(add_val)
        total += int(add_val)
    print('--+')
    print(total)


if __name__ == "__main__":
    input = read_file("input.txt")
    output = find_numbers_in_line(input)
    # output = conv_to_numbs(input)
    print(output)
