import re
f = open("input.txt", "rt")

total = 0

for line in f:
    results = re.findall("\d", line)

    first = results[0]
    last = results[-1]
    
    number = int(f"{first}{last}")
    total += number

print(f"The total is {total}")
f.close()