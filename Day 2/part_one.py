f = open("input.txt", "rt")

total = 0

red_max = 12
green_max = 13
blue_max = 14

for line in f:
    # Setup and convert to json data

    game_id = int(line.split(":")[0].replace("Game ", ""))
    game_draws = line.split(":")[1].split(";")
    for index, game_draw in enumerate(game_draws):
        game_draws[index] = {"red": 0, "green": 0, "blue": 0}
        turn_draws = str(game_draw.replace("\n", "").replace(" ", "")).split(",")

        for turn_draw in turn_draws:
            colours = ["red", "green", "blue"]
            for colour in colours:
                if colour in turn_draw:
                    game_draws[index][colour] = max(int(turn_draw.replace(colour, "")), game_draws[index][colour])

    # Logic starts here

    red_total = 0
    green_total = 0
    blue_total = 0

    for draw in game_draws:
        red_total = max(draw["red"], red_total)
        green_total = max(draw["green"], green_total)
        blue_total = max(draw["blue"], blue_total)

    if (red_total <= red_max) and (green_total <= green_max) and (blue_total <= blue_max):
        total += game_id

print(f"The total is {total}")
f.close()
