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

    card_dict.update({card_key: card_value})
    return card_dict


def comp_results(result_cards):
    total = 0
    cards_to_play = [1]
    card_numb = 1
    cards_dict = {}
    for card_numb, card in enumerate(result_cards):
        card = format_cards(card)
        cur_card = {}
        # {'Card 1': [['41', '48', '83', '86', '17'], ['83', '86', '6', '31', '17', '9', '48', '53']]}
        for numbers in card.values():
            win_numb = numbers[0]
            numb_card = numbers[1]

            # maak de regex string:
            """
            search_pattern = ''
            for numb in win_numb:
                search_pattern += numb + '|'
            match = re.findall(search_pattern, numb_card)
            print(match)
            """
            points = 0
            has_point = False
            for number in numb_card:
                if number in win_numb:
                    # print(f'match is on {number}')
                    if not has_point:
                        has_point = True
                        points = 1
                    elif has_point:
                        points += 1
            print(f'points for {card.keys()}: {points}')
            total += points
        card_numb += 1
        cards_dict.update({card_numb: points})
    return cards_dict


if __name__ == "__main__":
    cards = read_file('input.txt')
    output = comp_results(cards)
    print(f'de kaarten zijn {output} punten waard!')
