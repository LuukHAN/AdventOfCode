import sys


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
    start_position = [0, 0]
    field = []
    for y_coord, row in enumerate(input_data):
        row = [char for char in row]
        field.append(row)
        for x_coord, column in enumerate(row):
            if input_data[y_coord][x_coord] == '^':
                start_position = [x_coord, y_coord]
    move_through_field(field, start_position)


def move_through_field(field, position):
    direction = 0
    position = {
        'x': position[0],
        'y': position[1]
    }
    field = mv_around(field, position, direction)
    x_count = 0
    for row in field:
        for letter in row:
            if letter == 'X' or letter in ['^', '>', '⌄', '<',]:
                x_count += 1
    print(f'resultaat is {x_count}')


def mv_around(field, position, direction):
    if direction == 0:
        if position['y'] - 1 > -1: # top buiten veld
            if field[position['y'] - 1][position['x']] == '#':
                direction += 1
                print('draai naar oosten')
            else:
                field[position['y']][position['x']] = 'X'
                position['y'] = position['y'] - 1
                field[position['y']][position['x']] = '^'
        else:
            return field
    elif direction == 1:
        if position['x'] + 1 < len(field[0]) + 1: # rechts buiten veld
            if field[position['y']][position['x'] + 1] == '#':
                direction += 1
                print('draai naar zuiden')
            else:
                field[position['y']][position['x']] = 'X'
                position['x'] = position['x'] + 1
                field[position['y']][position['x']] = '>'
        else:
            return field
    elif direction == 2:
        if position['y'] + 1 < len(field) + 1: # bottom buiten veld
            if field[position['y'] + 1][position['x']] == '#':
                direction += 1
                print('draai naar westen')
            else:
                field[position['y']][position['x']] = 'X'
                position['y'] = position['y'] + 1
                field[position['y']][position['x']] = '⌄'
        else:
            return field
    elif direction == 3:
        if position['x'] - 1 >= 0:
            if field[position['y']][position['x'] - 1] == '#': # naar westen
                direction += 1
                print('draai naar noorden')
            else:
                field[position['y']][position['x']] = 'X'
                position['x'] = position['x'] - 1
                field[position['y']][position['x']] = '<'
        else:
            return field
    elif direction == 4:
        direction = 0
    elif direction == -1:
        direction = 3
    for i in field:
        print(i)
    print('\n\n__________________________________________________________________________\n\n')
    return mv_around(field, position, direction)


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_6\\input.txt'
    input_data = readfile(in_file_path)
    loop_through_lines(input_data)
    # niet 4453
    #