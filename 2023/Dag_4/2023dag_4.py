import re


def read_file(input_bestand):
    with open(input_bestand, "r") as file:
        input_data = file.read().splitlines()
    return input_data


def format_cards(card_line):
    card_dict = {}

    card_line = card_line.split(":")
    for part in card_line:
        if "Card" in part:
            card_key = part  # dit is Card #, dit komt later als key in de dict.
        else:
            part = part.replace("  ", " ")
            part = part.split("|")
            card_value = []
            for number_row in part:
                number_row = number_row.strip()
                number_row = number_row.split(" ")
                card_value.append(number_row)

    card_dict.update({card_key: part})
    return card_dict


def comp_results(result_cards):
    for card in result_cards:
        card = format_cards(card)
        # {'Card 1': [['41', '48', '83', '86', '17'], ['83', '86', '6', '31', '17', '9', '48', '53']]}
        for numbers in card.values():
            win_numb = numbers[0]
            numb_card = numbers[1]
            # maak de regex string:
            search_pattern = ''
            for numb in win_numb:
                search_pattern += numb + '|'
            match = re.findall(search_pattern, numb_card)
            print(match)


if __name__ == "__main__":
    cards = read_file('input.txt')
    comp_results(cards)
