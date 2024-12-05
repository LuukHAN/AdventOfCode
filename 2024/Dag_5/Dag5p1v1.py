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
    rules = []
    page_orders = []
    is_rule = True
    for line in input_data:
        if line == '':
            is_rule = False
        else:
            if is_rule:
                rules.append(line.split('|'))
            else:
                page_orders.append(line.split(','))
    return rules, page_orders


def check_allowed(rules, page_orders):
    print('checking allowed')
    proper_lines = []
    for pages_line in page_orders:
        pages_line = [int(item) for item in pages_line]
        is_proper = True
        for rule in rules:
            rule = [int(item) for item in rule]
            if rule[0] in pages_line and rule[1] in pages_line:
                L_numb_index = pages_line.index(rule[0])
                R_numb_index = pages_line.index(rule[1])
                if L_numb_index > R_numb_index:
                    is_proper = False
        if is_proper:
            proper_lines.append(pages_line)
    return proper_lines


def find_middle(this_list):
    return this_list[len(this_list) // 2]


if __name__ == '__main__':
    in_file_path = 'C:\\Users\\luukv\\PycharmProjects\\AoC\\2024\\Dag_5\\input.txt'
    input_data = readfile(in_file_path)
    rules, page_orders = loop_through_lines(input_data)
    lijntjes = check_allowed(rules, page_orders)
    total = 0
    for i in lijntjes:
        total += find_middle(i)
    print(total)
