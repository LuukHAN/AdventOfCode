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
    for line in input_data:
        is_descending = check_ascending_order(line)
        #is_ascending = check_ascending_order(line)
        if is_descending:
            print(line)


def check_descending_order(data):
    data = data.split(' ')
    data = [int(x) for x in data]
    is_descending = True
    for index, number in enumerate(data):
        if index == 0:
            continue
        else:
            if number > data[index - 1]:
                is_descending = False
    return is_descending


def check_ascending_order(data):
    data = data.split(' ')
    data = [int(x) for x in data]
    is_ascending = True
    for index, number in enumerate(data):
        if index == 0:
            continue
        else:
            if number > data[index - 1]:
                is_ascending = False
    return is_ascending


if __name__ == '__main__':
    in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_2\\test_input.txt'
    input_data = readfile(in_file_path)
    loop_through_lines(input_data)