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
    safe_lines = []
    for line in input_data:
        line = line.split(' ')
        line = [int(x) for x in line]
        sorted_line = sorted(line)
        if sorted_line == line or sorted_line[::-1] == line:
            check_set = set(line)
            if len(check_set) == len(line):
                is_safe = True
                for index, number in enumerate(line):
                    if index == 0:
                        continue
                    else:
                        if abs(number - line[index - 1]) > 3:
                            # print(f'{line} <-- {number} - {line[index - 1]} = {abs(number - line[index - 1])}')
                            is_safe = False
                if is_safe:
                    print(line)


if __name__ == '__main__':
    in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_2\\test_input.txt'
    input_data = readfile(in_file_path)
    loop_through_lines(input_data)