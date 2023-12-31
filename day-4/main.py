import re

# Tried it using set comprehension bc why not

data = open("./day-4/input.txt").read().splitlines()

card_counter = {card_number: 1 for card_number in range(1, len(data) + 1)}

for card_number, line in enumerate(data, start=1):
    left, right = line.split(":")[1].split("|")

    winning_numbers = {int(number) for number in re.findall(r"\d+", left)}

    my_numbers = {int(number) for number in re.findall(r"\d+", right)}

    num_matches = len(winning_numbers & my_numbers)

    for won_copies in range(card_number + 1, card_number + 1 + num_matches):
        card_counter[won_copies] += card_counter[card_number]

print(sum(card_counter.values()))
