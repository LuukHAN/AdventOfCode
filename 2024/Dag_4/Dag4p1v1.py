import re


def readfile(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            input_data = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: File not found - {file_name}")
        return None
    except UnicodeError:
        print(f"Error: Unable to decode file - {file_name}")
        return None
    except PermissionError:
        print(f"Error: Permission denied - {file_name}")
        return None
    return input_data


def make_mock_list(two_d_list):
    mock_list = []
    for line in two_d_list:
        add_to = []
        for letter in line:
            add_to.append('.')
        mock_list.append(add_to)
    return mock_list


def loop_through_lines(input_data):
    found_chart = make_mock_list(input_data)

    all_found = []
    for line_number, line in enumerate(input_data):
        found = []
        for letter_index, letter in enumerate(line):
            if letter == 'X':
                try:
                    if input_data[line_number][letter_index + 1] == 'M':
                        if input_data[line_number][letter_index + 2] == 'A':
                            if input_data[line_number][letter_index + 3] == 'S':
                                found.append(f"XMAS_hori_R <-- {letter_index}, {line_number}")
                                found_chart[line_number][letter_index] = 'X'
                                found_chart[line_number][letter_index + 1] = 'M'
                                found_chart[line_number][letter_index + 2] = 'A'
                                found_chart[line_number][letter_index + 3] = 'S'
                except IndexError:
                    pass

                try:
                    if input_data[line_number][letter_index - 1] == 'M':
                        if input_data[line_number][letter_index - 2] == 'A':
                            if input_data[line_number][letter_index - 3] == 'S':
                                found.append(f"XMAS_hori_L <-- {letter_index}, {line_number}")
                                found_chart[line_number][letter_index] = 'X'
                                found_chart[line_number][letter_index - 1] = 'M'
                                found_chart[line_number][letter_index - 2] = 'A'
                                found_chart[line_number][letter_index - 3] = 'S'
                except IndexError:
                    pass

                try:
                    if input_data[line_number + 1][letter_index] == "M": # zeokt verticaal naar beneden
                        if input_data[line_number + 2][letter_index] == "A":
                            if input_data[line_number + 3][letter_index] == "S":
                                found.append(f'XMAS_vert_down <-- {letter_index}, {line_number}')
                                found_chart[line_number][letter_index] = 'X'
                                found_chart[line_number + 1][letter_index] = 'M'
                                found_chart[line_number + 2][letter_index] = 'A'
                                found_chart[line_number + 3][letter_index] = 'S'
                except IndexError:
                    pass

                try:
                    if input_data[line_number - 1][letter_index] == "M": # zoekt verticaal omhoog
                        if input_data[line_number - 2][letter_index] == "A":
                            if input_data[line_number - 3][letter_index] == "S":
                                found.append(f'XMAS_vert_up <-- {letter_index}, {line_number}')
                                found_chart[line_number][letter_index] = 'X'
                                found_chart[line_number - 1][letter_index] = 'M'
                                found_chart[line_number - 2][letter_index] = 'A'
                                found_chart[line_number - 3][letter_index] = 'S'
                except IndexError:
                    pass

                try:
                    if input_data[line_number + 1][letter_index + 1] == "M": # zoekt diagonaal rechts naarbeneden
                        if input_data[line_number + 2][letter_index + 2] == "A":
                            if input_data[line_number + 3][letter_index + 3] == "S":
                                found.append(f'XMAS_dia_Rdown <-- {letter_index}, {line_number}')
                                found_chart[line_number][letter_index] = 'X'
                                found_chart[line_number + 1][letter_index + 1] = 'M'
                                found_chart[line_number + 2][letter_index + 2] = 'A'
                                found_chart[line_number + 3][letter_index + 3] = 'S'
                except IndexError:
                    pass

                try:
                    if input_data[line_number + 1][letter_index - 1] == "M": # zoek diagonaal links naarbeneden
                        if input_data[line_number + 2][letter_index - 2] == "A":
                            if input_data[line_number + 3][letter_index - 3] == "S":
                                found.append(f'XMAS_dia_Ldown <-- {letter_index}, {line_number}')
                                found_chart[line_number][letter_index] = 'X'
                                found_chart[line_number + 1][letter_index - 1] = 'M'
                                found_chart[line_number + 2][letter_index - 2] = 'A'
                                found_chart[line_number + 3][letter_index - 3] = 'S'
                except IndexError:
                    pass

                try:
                    if input_data[line_number - 1][letter_index - 1] == "M": # zoek diagonaal links naarboven
                        if input_data[line_number - 2][letter_index - 2] == "A":
                            if input_data[line_number - 3][letter_index - 3] == "S":
                                found.append(f"XMAS_dia_Lup <-- {letter_index}, {line_number}")
                                found_chart[line_number][letter_index] = 'X'
                                found_chart[line_number - 1][letter_index - 1] = 'M'
                                found_chart[line_number - 2][letter_index - 2] = 'A'
                                found_chart[line_number - 3][letter_index - 3] = 'S'
                except IndexError:
                    pass

                try:
                    if input_data[line_number - 1][letter_index + 1] == 'M': # zoek diagnonaal rechts boven
                        if input_data[line_number - 2][letter_index + 2] == "A":
                            if input_data[line_number - 3][letter_index + 3] == "S":
                                found.append(f"XMAS_dia_Rup <-- {letter_index}, {line_number}")
                                found_chart[line_number][letter_index] = 'X'
                                found_chart[line_number - 1][letter_index + 1] = 'M'
                                found_chart[line_number - 2][letter_index + 2] = 'A'
                                found_chart[line_number - 3][letter_index + 3] = 'S'
                except IndexError:
                    pass

        for i in found:
            all_found.append(i)
    print(f'{len(all_found)} biep biep boep\n{all_found}')
    for i in found_chart:
        print(''.join(i))
    for i in all_found:
        print(i)


if __name__ == '__main__':
    in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_4\\test_input.txt'
    input_data = readfile(in_file_path)
    loop_through_lines(input_data)
    # print(input_data[9][10])


    #wat er fout gaat is dat als hij links zit, en hij zegt ga 1 omlaag, dan komt het op - uit
    # wat er voor zorgt dat hij aan de andere kant verder gaat zoeken omdat list[-1] rechts teld.