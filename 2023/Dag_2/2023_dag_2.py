def read_file(input_bestand):
    with open(input_bestand, "r") as file:
        input_data = file.read().splitlines()
    return input_data

def format_data(raw_data):
    result_dict = {}
    for line in raw_data:
        rare_data = line.split(":")
        rare_data[1] = rare_data[1].split(";")
        result_dict.update({rare_data[0]: rare_data[1]})

    return result_dict


def calc_results(val_dict, max_result_dict):
    possi_games_sum = 0
    possi_games = []
    for game_numb, game_result in enumerate(val_dict.values()):
        game_numb += 1
        is_valid_game = True
        for set_result in game_result:
            #set_result = set_result.strip()
            set_result = set_result.split(",")
            for value in set_result:
                value = value.strip()
                value = value.split(" ")
                for max_check in max_result_dict:
                    if max_check == value[1]:
                        if max_result_dict[max_check] >= int(value[0]) and is_valid_game:
                            possi_games.append(game_numb)
                        else:
                            is_valid_game = False
                            while game_numb in possi_games:
                                possi_games.remove(game_numb)
                            print(f"{game_numb} gaat eruit")
            # Hier nog controleren of het aantal items in possi_games gelijk is aan het aantal resultaten in de list.
            # Als dat niet overeen komt, weet je dat het geen valid game is. dus tel je die niet mee.
                # print(value)
            # print("new set")
        # print("new_game")
    possi_games = set(possi_games)
    return sum(possi_games)


def part_two(val_dict, max_result_dict):
    possi_games = []
    power_list = []
    for game_numb, game_result in enumerate(val_dict.values()):
        game_numb += 1
        is_valid_game = True
        min_score = {
            "red": [],
            "green": [],
            "blue": []
        }
        for set_result in game_result:
            # set_result = set_result.strip()
            set_result = set_result.split(",")
            for value in set_result:
                value = value.strip()
                value = value.split(" ")
                for max_check in max_result_dict:
                    if max_check == value[1]:
                        min_score[max_check].append(value[0])
                        if max_result_dict[max_check] >= int(value[0]) and is_valid_game:
                            possi_games.append(game_numb)
                        else:
                            is_valid_game = False
                            while game_numb in possi_games:
                                possi_games.remove(game_numb)
        print(f"min_score = {min_score}")
        power = 1
        for color in min_score.keys():
            # conv_int = max(min_score[color])
            # conv_int = int(conv_int)
            # print(f"min is {conv_int}")
            int_list = [eval(i) for i in min_score[color]]
            conv_int = max(int_list)

            power *= conv_int
        power_list.append(power)
    possi_games = set(possi_games)
    return power_list


if __name__ == "__main__":
    game_results = read_file("input.txt")
    formated_data = format_data(game_results)
    max_dict = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    output = calc_results(formated_data, max_dict)
    print(f"output = {output}")
    print("-"*75)

    # part two:
    p2_output = part_two(formated_data, max_dict)
    print(f"output van part 2 is {p2_output}")
    act_output = 1
    for numb in p2_output:
        act_output += numb
    act_output -= 1
    print(f"actual output = {act_output}")
