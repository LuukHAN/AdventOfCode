def read_file(input_bestand):
    with open(input_bestand, "r") as file:
        input_data = file.read().splitlines()
    return input_data


def format_data(raw_data):
    formated_dict = {}
    start_new_dict = False
    dict_value = []
    for line_count, line in enumerate(raw_data):
        cur_dict = {}
        if line.startswith("seeds"):
            line = line.split(" ")
            formated_dict.update({line[0]: line[1:]})
            continue
        elif line == "":
            start_new_dict = True
            try:
                formated_dict.update({dict_key: dict_value})
            except:
                pass

        if start_new_dict:
            dict_key = line
            start_new_dict = False
        else:
            line = line.split(" ")
            dict_value.append(line)
            continue

    print(formated_dict)


if __name__ == "__main__":
    input = read_file("input.txt")
    map_dict = format_data(input)
