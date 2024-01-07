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


def deze_functie_krijgt_nog_een_andere_naam(result_cards):
    won_scratch_cards = []
    for index, line in enumerate(result_cards):
        card = format_cards(line)
        index += 1
        times_won = 0
        new_games = []
        for numbers in card.values():
            win_numb = numbers[0]
            numb_card = numbers[1]

            for number in numb_card:
                if number in win_numb:
                    times_won += 1

            for i in range(times_won):
                new_games.append(index+i+1)
        print(f'card {index} zorgt voor de volgende nieuwe kaarten: {new_games}')
        won_scratch_cards.append(new_games)
    print(f'won_scratch_cards = {won_scratch_cards}')
    return won_scratch_cards


def get_sec_round_cards(result_cards, temp_won_cards):
    won_cards = []
    for i in temp_won_cards:
        won_cards += i
    print(won_cards)

    new_card_list = []
    for line in result_cards:
        card = format_cards(line)

        search_pattern = re.compile('\d')
        string_card = str(card.keys())
        card_numb = re.findall(search_pattern, string_card)
        listToStr = ''.join([str(elem) for elem in card_numb])
        card_numb = int(listToStr)
        print(card_numb)
        # het nummer is geisoleerd.

        if card_numb:
            while card_numb in won_cards:
                new_card_list.append(line)
                won_cards.remove(card_numb)
    for i in new_card_list:
        print(i)
    return new_card_list

if __name__ == "__main__":
    cards = read_file('input.txt')
    won_cards = deze_functie_krijgt_nog_een_andere_naam(cards)
    sec_round_cards = get_sec_round_cards(cards, won_cards)
    sec_round = deze_functie_krijgt_nog_een_andere_naam(sec_round_cards)
    print(f'sec_round = {sec_round}')