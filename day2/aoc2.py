# 2018 Advent of Code - Day 1
from collections import Counter

# load the input from the text file as a list
inputFile = open("input.txt", 'r')
inputValues = [x.strip() for x in inputFile.readlines()]  # read lines to list


def scanBox(boxid):

    # calculate the letter counts in each box id
    d = Counter(boxid)

    # init values for counting double letters
    two = 0
    three = 0

    for key, value in d.items():
        if value == 2:
            two = 1
        if value == 3:
            three = 1
        else:
            pass

    return two, three

# tests
# print(scanBox("abcdef") == (0,0))
# print(scanBox("bababc") == (1,1))
# print(scanBox("abbcde") == (1,0))
# print(scanBox("abcccd") == (0,1))
# print(scanBox("aabcdd") == (1,0))
# print(scanBox("abcdee") == (1,0))
# print(scanBox("ababab") == (0,1))

# counter for checksum
twoCounter = 0
threeCounter = 0

# loop through input values and add to counters
for b in inputValues:
    sc = scanBox(b)
    twoCounter += sc[0]
    threeCounter += sc[1]

# checksum
p1answer = twoCounter * threeCounter
print(f"The solution to part 1 is {p1answer}")

# Part 2
exampleInput = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]

matches = []

for string in inputValues:
    for search in inputValues:
        if string != search:
            letters = []
            for i in range(len(string)):
                if string[i] == search[i]:
                    letters.append(string[i])
            matches.append((string, search, letters, len(letters)))

m = max(matches, key=lambda x: x[3])
print(m)

p2ans = "".join(m[2])
print(f'Part 2 answer is {p2ans}')
