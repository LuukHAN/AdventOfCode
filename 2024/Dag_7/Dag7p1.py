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
    right_answer_count = 0
    for line in input_data:
        line = line.replace(':', '').split(' ')
        line = [int(item) for item in line]
        for numb_index, number in enumerate(line):
            if numb_index == 0:
                continue
            else:
                check_if_calcable(line[0], line[1:])


def check_if_calcable(answer, numbers):




if __name__ == '__main__':
    in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_7\\test_input.txt'
    input_data = readfile(in_file_path)
    loop_through_lines(input_data)
