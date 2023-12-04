import re
f = open("input.txt", "rt")

cards = {}
cards_collected = 0
processing = []

for line in f:
    card_id = line.split(":")[0].replace("Card ", "").strip()
    card_data = line.split(":")[1]

    winning_nums = re.findall("\d+", card_data.split("|")[0])
    card_nums = re.findall("\d+", card_data.split("|")[1])

    correct_nums = []
    for num in card_nums:
        if num in winning_nums:
            correct_nums.append(num)

    cards[card_id] = list(range(int(card_id) + 1, int(card_id) + len(correct_nums) + 1))
    processing.append(card_id)

print(cards)

def do_process(card_id):
    global cards_collected
    card_refs = cards[str(card_id)]

    for id in card_refs:
        processing.append(id)
    
    cards_collected += 1

while len(processing) > 0:
    # print(len(processing))
    card_id = processing.pop()
    do_process(card_id)

print(f"\nThe total is {cards_collected}")
f.close()