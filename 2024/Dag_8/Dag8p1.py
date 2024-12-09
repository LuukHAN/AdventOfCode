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
        uncompress(line)


def uncompress(data_line):
    file_number = 0
    uncompressed_line = []
    even_index = False
    for index, number in enumerate(data_line):
        if index % 2 == 0:
            even_index = True
        else:
            even_index = False
            file_number += 1

        for getal in range(int(number)):
            if not even_index:
                uncompressed_line.append('.')
            else:
                uncompressed_line.append(file_number)
    print(uncompressed_line)


def mv_files(lijntje):
    lijntje = [0, '.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]

    new_lijntje = []
    for i in lijntje:
        new_lijntje.append('')
    dot_count = lijntje.count('.')
    for index, number in enumerate(lijntje):
        if number == '.':
            new_lijntje[index] = lijntje[::-1]
        else:
            new_lijntje.append(number)
            continue
    for i in range(dot_count):
        new_lijntje.append('.')
        print(new_lijntje)


if __name__ == '__main__':
    # in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_8\\test_input.txt'
    # input_data = readfile(in_file_path)
    # loop_through_lines(input_data)
    mv_files('')
