import re


def readfile(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            input_data = file.read()
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


def find_muls(input_data):
    search_pattern = r"(mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\))"
    found = re.findall(search_pattern, input_data)
    return found


def find_correct_muls(found_strings):
    doing = True
    correct_muls = []
    for found_string in found_strings:
        if found_string == "don't()":
            doing = False
        elif found_string == "do()":
            doing = True
        else:
            if doing:
                correct_muls.append(found_string)
    return correct_muls


def multiply_muls(muls):
    total = 0
    for mul in muls:
        mul = mul.replace('mul(', '').replace(')', '')
        mul = mul.split(',')
        total += int(mul[0]) * int(mul[1])
    return total


if __name__ == '__main__':
    in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_3\\input.txt'
    input_data = readfile(in_file_path)
    found = find_muls(input_data)
    filtered_muls = find_correct_muls(found)
    total = multiply_muls(filtered_muls)
    print(total)
