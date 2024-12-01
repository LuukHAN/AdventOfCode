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


def prep_data(data):
    left_line = []
    right_line = []
    for line in data:
        line = line.split('   ')
        left_line.append(line[0])
        right_line.append(line[1])
    left_line.sort()
    right_line.sort()
    return left_line, right_line


def calc_distance(left_line, right_line):
    total_distance = 0
    for index, number in enumerate(left_line):
        total_distance += abs(int(left_line[index]) - int(right_line[index]))
    return total_distance


def calc_simmilarity(left_line, right_line):
    total_simmilarity = 0
    for index, number in enumerate(left_line):
        times_found = 0
        for index2, number2 in enumerate(right_line):
            if number == number2:
                times_found += 1
        total_simmilarity += int(number) * times_found
    return total_simmilarity


if __name__ == '__main__':
    test_data = readfile('C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_1\\input.txt')
    left_line, right_line = prep_data(test_data)
    print(calc_simmilarity(left_line, right_line))