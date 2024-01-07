def read_file(input_bestand):
    with open(input_bestand, "r") as file:
        input_data = file.read().splitlines()
    return input_data


def format_data(raw_data):
    formated_data = {}
    for line in raw_data:
        line = line.split(" ")
        while '' in line:
            line.remove('')
        temp_list = []
        for i in line[1:]:
            temp_list.append(int(i))
        formated_data.update({line[0]: temp_list})
    return formated_data


def calc_beatways(results_dict):
    #print(results_dict)
    total = 1
    for race_count, result in enumerate(results_dict['Time:']):
        beat_count = 0
        for hold_time in range(result):
            distance = hold_time * (result - hold_time)
            #print(f'hold_time = {hold_time} ::: distance = {distance}')
            if distance > results_dict['Distance:'][race_count]:
                #print(f'holdtime = {hold_time}')
                beat_count += 1
        print(f'beat_count = {beat_count}')
        total *= beat_count
    return total


def part_two_calc_beat(results_dict):
    beat_count = 0
    for hold_time in range(results_dict['Time']):
        distance = hold_time * (results_dict['Time'] - hold_time)
        if distance > results_dict['Distance']:
            beat_count += 1
    #  print(f'beatCount = {beat_count}')
    return beat_count


def format_part_two(raw_data):
    formated_data = {}
    for line in raw_data:
        line = line.replace(" ", '')
        line = line.split(":")
        while '' in line:
            line.remove('')
        formated_data.update({line[0]: int(line[1])})
    print(f'formated_data = {formated_data}')
    return formated_data


if __name__ == "__main__":
    results = read_file("input.txt")
    formated_results = format_part_two(results)
    #formated_results = format_data(results)
    #amounts_of_beatways = calc_beatways(formated_results)
    amounts_of_beatways = part_two_calc_beat(formated_results)
    print(f'Output = {amounts_of_beatways}')
