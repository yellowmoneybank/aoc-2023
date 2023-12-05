from aoc import get_input
import re

testInput = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""




def translate(num:int, section:str):
    for range in  section.splitlines()[1:]:
        numbers = [int(x) for x in re.findall(r"\d+", range)]
        source = numbers[1]
        dest = numbers[0]
        range = numbers[2]
        if source <= num <= (source + range):
            return dest + (num - source)

    return num







sections = get_input(5).split("\n\n")
# sections = testInput.split("\n\n")

seedranges = [int(x) for x in re.findall(r"\d+", sections[0])]

seedPairs = [(seedranges[i], seedranges[i+1]) for i in range(0, len(seedranges), 2)]

translatedNumbers = []
for p in seedPairs:
	for seed in range(p[0], p[0] + p[1]):
	    translatedNumber = seed
	    for section in sections[1:]:
	        translatedNumber = translate(translatedNumber, section)
	    translatedNumbers.append(translatedNumber)

print(min(translatedNumbers))
