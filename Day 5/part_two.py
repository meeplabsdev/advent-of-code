import re
from itertools import islice

f = open("input.txt", "rt")
input = f.read().strip().split("\n\n")[::]


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


class AoCMap():
    def __init__(self, ranges):
        self.ranges = ranges
    
    def convert(self, num):
        for ranger in self.ranges:
            dest = int(ranger[0])
            source = int(ranger[1])
            length = int(ranger[2])
            change = dest - source

            num = int(num)
            if num >= source and num < source + length:
                # Within this range
                return num + change
        # Not within a range
        return num


seeds_line = input.pop(0)

seed_soil_line = input.pop(0)
seed_soil = seed_soil_line.splitlines()[1:]
# print("Seeds -> Soil:", seed_soil)
# ["Dest Source Length", "Dest Source Length" ...]
vals = []
for ranger in seed_soil:
    data = ranger.split(" ")
    vals.append(data)
seed_soil = AoCMap(vals)

soil_fert_line = input.pop(0)
soil_fert = soil_fert_line.splitlines()[1:]
# print("Soil -> Fertiliser", soil_fert)
vals = []
for ranger in soil_fert:
    data = ranger.split(" ")
    vals.append(data)
soil_fert = AoCMap(vals)

fert_water_line = input.pop(0)
fert_water = fert_water_line.splitlines()[1:]
# print("Fertiliser -> Water", fert_water)
vals = []
for ranger in fert_water:
    data = ranger.split(" ")
    vals.append(data)
fert_water = AoCMap(vals)

water_light_line = input.pop(0)
water_light = water_light_line.splitlines()[1:]
# print("Water -> Light", water_light)
vals = []
for ranger in water_light:
    data = ranger.split(" ")
    vals.append(data)
water_light = AoCMap(vals)

light_temp_line = input.pop(0)
light_temp = light_temp_line.splitlines()[1:]
# print("Light -> Temperature", light_temp)
vals = []
for ranger in light_temp:
    data = ranger.split(" ")
    vals.append(data)
light_temp = AoCMap(vals)

temp_humid_line = input.pop(0)
temp_humid = temp_humid_line.splitlines()[1:]
# print("Temperature -> Humidity", temp_humid)
vals = []
for ranger in temp_humid:
    data = ranger.split(" ")
    vals.append(data)
temp_humid = AoCMap(vals)

humid_loc_line = input.pop(0)
humid_loc = humid_loc_line.splitlines()[1:]
# print("Humidity -> Location", humid_loc)
vals = []
for ranger in humid_loc:
    data = ranger.split(" ")
    vals.append(data)
humid_loc = AoCMap(vals)


def seedToLocation(seed):
    soil = seed_soil.convert(seed)
    fert = soil_fert.convert(soil)
    water = fert_water.convert(fert)
    light = water_light.convert(water)
    temp = light_temp.convert(light)
    humid = temp_humid.convert(temp)
    loc = humid_loc.convert(humid)

    return loc

print("Calculating seeds...")

seeds_individuals = re.findall("\d+", seeds_line)
seeds_pairs = list(chunk(seeds_individuals, 2))

minimum = -1
for pair in seeds_pairs:
    for seed in range(int(pair[0]), int(pair[0]) + int(pair[1]) + 1): # Takes a very long time...
        loc = seedToLocation(seed)
        minimum = loc if minimum < 0 else min(minimum, loc)

print("Seeds calculated!")
print(f"The lowest location is {minimum}")
f.close()