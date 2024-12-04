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
        forward_pop = False
        backward_pop = False
        line_is_safe = True
        line = line.split(' ')
        line = [int(x) for x in line]
        direction = ''
        error_count = 0

        # begin eerst met kijken of het oploopt
        error_list_forward = is_scending(line, 'forward')
        if len(error_list_forward) == 1:
            error_list_forward = is_scending(line, 'forward', to_pop=error_list_forward[0])
            forward_pop = True
        error_list_backward = is_scending(line, 'backward')
        if len(error_list_backward) == 1:
            error_list_backward = is_scending(line, 'backward', to_pop=error_list_backward[0])
            backward_pop = True

        if error_list_forward > error_list_backward:
            direction = 'descending'
            if backward_pop:
                error_count += 1
        elif error_list_forward < error_list_backward:
            direction = 'ascending'
            if forward_pop:
                error_count += 1
        else:
            direction = 'gelijk'
        print(f'{line} <--{direction}<--{error_count}')

        if direction == 'descending':
            for index, number in enumerate(line):
                if number == 0:
                    continue
                else:
                    if abs(number - line[index - 1]) > 3 or abs(number - line[index]) <= 1:
                        error_list_backward.append(number)
        elif direction == 'ascending':
            for index, number in enumerate(line):
                if number == 0:
                    continue
                else:
                    if abs(number - line[index - 1]) > 3 or abs(number - line[index]) <= 1:
                        error_list_forward.append(number)

        if len(error_list_forward) > 0 and len(error_list_backward) > 0:
            print(f'{line} is unsafe')
            line_is_safe = False





def is_scending(numb_line, direction, to_pop=None):
    """
    :param numb_line: list met nummers (int)
    :param direction: [forward|backward] ascending or descending
    :return: error_cases: de nummers die problemen veroorzaakten
    """
    error_cases = []
    if to_pop:
        numb_line.remove(to_pop)
    for index, number in enumerate(numb_line):
        if index == 0:
            continue
        else:
            if direction == 'forward': # kijk of het omhoogloopt
                if not number > numb_line[index - 1]:
                    error_cases.append(number)
            elif direction == 'backward':
                if not number < numb_line[index - 1]:
                    error_cases.append(number)
    return error_cases

if __name__ == '__main__':
    in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_2\\test_input.txt'
    input_data = readfile(in_file_path)
    safe = loop_through_lines(input_data)
