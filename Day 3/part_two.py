import re
from collections import defaultdict
from functools import reduce

file = open("input.txt").read().strip()
lines = file.split('\n')

symbols = []
dirs = [(-1,-1),(1,1),(1,-1),(-1,1),(-1,0),(1,0),(0,-1),(0,1)]
for row, line in enumerate(lines):
    for y, character in enumerate(line):
        if not character.isdigit() and character != '.':
            for dir in dirs:
              symbols.append((row+dir[0],y+dir[1]))     

res1 = 0
possible_gear = defaultdict(list)

for row, line in enumerate(lines):
    nums = re.findall(r'\d+',line )
    lf = 0
    for num in nums:
        y = line.find(num,lf)
        lf = y+len(num)
        for col in range(y,lf):
            if ((row,col)) in symbols:
                res1 += int(num)
                gear_idx = int(symbols.index((row,col))/8)
                possible_gear[gear_idx].append(int(num))
                break

gear_ratio = sum(map(lambda kv: reduce(lambda x, y: x * y, kv[1]) if len(kv[1]) > 1 else 0, possible_gear.items()))
print("Total: ", gear_ratio)
