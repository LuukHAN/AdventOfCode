"""
Deel 1 is gelukt, nu moet de gear ratio gevonden worden.
"""
import re

def read_file(input_bestand):
    with open(input_bestand, "r") as file:
        input_data = file.read().splitlines()
    return input_data


def find_numbs(parts):
    numb_pos = {}  # {0: [[467, (0,3)], [114, (5,8)]]}
    search_pattern = re.compile(r"\d+")
    for vert_pos, line in enumerate(parts):
        # vind waar de nummers zich bevinden
        match = re.finditer(search_pattern, line)

        add_to_dict = []
        for occurance in match:
            # print(occurance.group())
            # print(occurance.span())
            add_to_dict.append([occurance.group(), occurance.span()])
        numb_pos.update({vert_pos: add_to_dict})

    return numb_pos


def find_asterix(spec_strings):
    spec_char_pos = {}  # {1: [3,3]}
    search_pattern = re.compile(r"[*]")
    for line_numb, line in enumerate(spec_strings):
        match = re.finditer(search_pattern, line)
        # print(match)
        add_to_dict = []
        for occurance in match:
            # print(occurance.span())
            add_to_dict.append(occurance.span()[0])
        spec_char_pos.update({line_numb: add_to_dict})
    return spec_char_pos


def find_touch(numb_pos, char_pos):
    part_list = []
    for line_count in numb_pos:
        for numb in numb_pos[line_count]:
            is_part = False
            # numb is ['467', (0, 3)]
            # print(f'numb = {numb[0]}')

            # check de line die erboven zit of daar aangrenzende spec chars zitten
            if line_count != 0 and not is_part:
                check_line = line_count - 1
                for spec_char_pos in char_pos[check_line]:
                    # print(f'spec_char on {check_line} = {char_pos[check_line]}')
                    if spec_char_pos >= (numb[1][0] - 1):  # de pos van spec char >= de start pos van het nummer
                        if spec_char_pos < (numb[1][1] + 1):  # de pos van spec char is kleiner dan het nummer
                            print(f'Een machine onderdeel = {numb[0]}')
                            is_part = True
                            part_list.append(numb[0])

            # check of de line eronder een aangrenzend spec char heeft
            if not is_part:
                check_line_bel = line_count + 1
                try:
                    for spec_char_pos in char_pos[check_line_bel]:
                        if spec_char_pos >= (numb[1][0] - 1):
                            if spec_char_pos < (numb[1][1] + 1):
                                print(f'Een machine onderdeel (below) = {numb[0]}')
                                is_part = True
                                part_list.append(numb[0])
                except KeyError:  # Op de laastste line geeft hij een foutmelding
                    pass  # geen continue, omdat we nog andere dingen moeten proberen

            # check of er een aangrenzende spec_char is
            if not is_part:
                for spec_char_pos in char_pos[line_count]:  # line count is de huidige line
                    # numb is ['467', (0, 3)]
                    # char_pos = {0: [], 1: [3], 2: [], 3: [6], 4: [3], 5: [5], 6: [], 7: [], 8: [3, 5], 9: []}

                    pos_before = numb[1][0] - 1
                    pos_after = numb[1][1] # voor pos after hoeft +1 niet omdat regex dat al doet
                    # print(f'spec_char_pos = {spec_char_pos}')
                    if pos_before < 0:
                        pass
                    else:
                        if spec_char_pos == pos_before:
                            is_part = True
                            part_list.append(numb[0])
                            print(f'een karakter die er een direct voor heeft: {numb[0]}')
                    if spec_char_pos == pos_after and not is_part:
                        print(f'een karakter die er een NA heeft: {numb[0]}')
                        is_part = True
                        part_list.append(numb[0])
    return part_list


if __name__ == "__main__":
    given_data = read_file('actual_input.txt')
    number_positions = find_numbs(given_data)
    spec_char_positions = find_asterix(given_data)
    parts = find_touch(number_positions, spec_char_positions)
    int_list = [eval(i) for i in parts]
    total = sum(int_list)

    print(f'total = {total}')
