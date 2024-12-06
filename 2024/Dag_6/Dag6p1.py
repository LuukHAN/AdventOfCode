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
    for y_coord, row in enumerate(input_data):
        for x_coord, column in enumerate(y_coord):
            if input_data[y_coord][x_coord] == '^':
                start_position = [x_coord, y_coord]


def move_through_field(field, position):
    direction = 0
    in_field = True
    position = {
        'x': position[0],
        'y': position[1]
    }
    while in_field:
        if position['x'] > len(field[0]):
            in_field = False
        elif position['x'] < 0:
            in_field = False
        elif position['y'] > len(field):
            in_field = False
        elif position['y'] < 0:
            in_field = False
        position, direction = mv_to_next_pos(field, position, direction)


def mv_to_next_pos(field, position, direction):
    if direction == 0:
        if field[position['y'] - 1][position['x']] == '#':
            direction += 1
        else:
            position['y'] -= 1
    elif direction == 1:
        if field[position['y']][position['x'] + 1] == '#':
            direction += 1
        else:
            position['x'] += 1
    elif direction == 2:
        if field[position['y'] + 1][position['x']] == '#':
            direction += 1
        else:
            position['y'] += 1
    elif direction == 3:
        if field[position['y']][position['x'] - 1] == '#':
            direction += 1
        else:
            position['x'] -= 1
    return position, direction

if __name__ == '__main__':
    in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_6\\input.txt'
    input_data = readfile(in_file_path)
    loop_through_lines(input_data)
