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
                print(line)


if __name__ == '__main__':
    in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_2\\test_input.txt'
    input_data = readfile(in_file_path)
    loop_through_lines(input_data)