import re
f = open("input.txt", "rt")

total = 0

for line in f:
    card_id = line.split(":")[0].replace("Card ", "")
    card_data = line.split(":")[1]

    winning_nums = re.findall("\d+", card_data.split("|")[0])
    card_nums = re.findall("\d+", card_data.split("|")[1])

    correct_nums = []
    for num in card_nums:
        if num in winning_nums:
            correct_nums.append(num)

    if len(correct_nums) > 0:
        card_value = 2 ** (len(correct_nums) - 1)
        total += card_value

print(f"The total is {total}")
f.close()