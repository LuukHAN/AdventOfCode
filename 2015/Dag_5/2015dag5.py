def read_file(input_file):
    with open(input_file, "r") as file:
        data = file.read().splitlines()
    return data


def find_vowels(word_list):
    vowel_list = []
    for string in word_list:
        vowel_count = 0
        for letter in string:
            if letter == "a":
                vowel_count += 1
            elif letter == "e":
                vowel_count += 1
            elif letter == "i":
                vowel_count += 1
            elif letter == "o":
                vowel_count += 1
            elif letter == "u":
                vowel_count += 1
        if vowel_count >= 3:
            vowel_list.append(string)
    return vowel_list


def find_doubles(word_list):
    double_list = []
    for word in word_list:
        double_found = False
        for index, letter in enumerate(word):
            try:
                if letter == word[index + 1]:
                    double_found = True
                    break
            except IndexError:
                pass
        if double_found:
            double_list.append(word)
    return double_list


def find_forbidden(word_list):
    forbidden_list = []
    for word in word_list:
        if "ab" not in word:
            if "cd" not in word:
                if "pq" not in word:
                    if "xy" not in word:
                        forbidden_list.append(word)
    return forbidden_list


def find_repe(word_list):
    repe_list = []
    for word in word_list:
        repe_found = False
        for index, letter in enumerate(word):
            try:
                if letter == word[index + 2]:
                    repe_found = True
            except IndexError:
                continue
        if repe_found:
            repe_list.append(word)
    return repe_list


def find_double_pair(word_list):
    doub_pair_list = []
    for word in word_list:
        double_pair_found = False
        for index, letter in enumerate(word):
            try:
                check_pair = letter + word[index + 1]
                if check_pair in word[index + 1:]:
                    start_index = index + 1
                    stop_index = word.find(check_pair, start_index) + 1
                    word = word[start_index:stop_index]
                    double_pair_found = True
            except IndexError:
                pass
        if double_pair_found:
            doub_pair_list.append(word)
    return doub_pair_list


if __name__ == "__main__":
    part = 2
    input_data = read_file("input.txt")
    if part == 1:
        strings = find_vowels(input_data)
        strings = find_doubles(strings)
        strings = find_forbidden(strings)

    elif part == 2:
        strings = find_double_pair(input_data)
        print(strings)
        strings = find_repe(strings)
        print(len(strings))
