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


def loop_through_lines(input_data):
    search_pattern = r'XMAS'
    rev_search_pattern = r'SAMX'
    all_found = []
    for line_number, line in enumerate(input_data):
        found_hori_r = re.findall(search_pattern, line) # zoekt horizontaal
        found_hori_l = re.findall(rev_search_pattern, line)
        found = found_hori_r + found_hori_l
        for i in found:
            all_found.append(i)
        found = []
        for letter_index, letter in enumerate(line):
            if letter == 'X':
                try:
                    if input_data[line_number + 1][letter_index] == "M": # zeokt verticaal naar beneden
                        if input_data[line_number + 2][letter_index] == "A":
                            if input_data[line_number + 3][letter_index] == "S":
                                found.append(f'XMAS_vert_down, {line_number}')
                except IndexError:
                    pass

                try:
                    if input_data[line_number - 1][letter_index] == "M": # zoekt verticaal omhoog
                        if input_data[line_number - 2][letter_index] == "A":
                            if input_data[line_number - 3][letter_index] == "S":
                                found.append(f'XMAS_vert_up, {line_number}')
                except IndexError:
                    pass

                try:
                    if input_data[line_number + 1][letter_index + 1] == "M": # zoekt diagonaal rechts naarbeneden
                        if input_data[line_number + 2][letter_index + 2] == "A":
                            if input_data[line_number + 3][letter_index + 3] == "S":
                                found.append(f'XMAS_dia_Rdown, {line_number}')
                except IndexError:
                    pass

                try:
                    if input_data[line_number + 1][letter_index - 1] == "M": # zoek diagonaal links naarbeneden
                        if input_data[line_number + 2][letter_index - 2] == "A":
                            if input_data[line_number + 3][letter_index - 3] == "S":
                                found.append(f'XMAS_dia_Ldown, {line_number}')
                except IndexError:
                    pass

                try:
                    if input_data[line_number - 1][letter_index - 1] == "M": # zoek diagonaal links naarboven
                        if input_data[line_number - 2][letter_index - 2] == "A":
                            if input_data[line_number - 3][letter_index - 3] == "S":
                                found.append(f"XMAS_dia_Lup, {line_number}")
                except IndexError:
                    pass

                try:
                    if input_data[line_number - 1][letter_index + 1] == 'M': # zoek diagnonaal rechts boven
                        if input_data[line_number - 2][letter_index + 2] == "A":
                            if input_data[line_number - 3][letter_index + 3] == "S":
                                found.append(f"XMAS_dia_Rup, {line_number}")
                except IndexError:
                    pass

        for i in found:
            all_found.append(i)
    print(f'{len(all_found)} biep biep boep\n{all_found}')


if __name__ == '__main__':
    in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_4\\test_input.txt'
    input_data = readfile(in_file_path)
    loop_through_lines(input_data)
