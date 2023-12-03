import re
f = open("input.txt", "rt")

convert = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

total = 0

for line in f:
    string = line
    finished = False
    while not finished:
        words = {}
        for word in convert.keys():
            try:
                index = string.index(word)
                words[str(index)] = word
            except ValueError:
                pass

        words = {k: words[k] for k in sorted(words, key=lambda x: int(x))} # Sort the list

        if len(words) == 0:
            finished = True
        else:
            word = list(words.values())[0]
            value = convert[word]
            
            string = string.replace(word, value, 1)

    results = re.findall("\d", string)

    first = results[0]
    last = results[-1]
    
    number = int(f"{first}{last}")
    total += number

print(f"The total is {total}")
f.close()