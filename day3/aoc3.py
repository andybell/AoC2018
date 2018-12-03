# advent of code day 3

import numpy as np

# create fabric
dim = 1000
fab = np.zeros((dim, dim))

# parse inputs
def parseInput(inputLine):
    a = inputLine.split()
    num = a[0].replace("#", "")
    x_offset, y_offset = a[2].replace(":", "").split(",")
    dimensions = a[3]
    x, y = dimensions.split("x")
    return int(x_offset), int(y_offset), int(x), int(y), num

print(parseInput( "#123 @ 3,2: 5x4") == (3, 2, 5, 4))

# write to matrix
def matrixOffset(x_offset, y_offset, x, y):
    f = np.full((x, y), 1)

    # pad with offset
    p = np.pad(f, ((x_offset, dim - x - x_offset), (y_offset, dim - y - y_offset )), 'constant') #((top, bottom), (left, right))

    return p


# puzzle input
inputFile = open("input.txt", 'r')
inputValues = [x.strip() for x in inputFile.readlines()]  # read lines to list

#inputValues = ["#1 @ 1,3: 4x4",  "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]

for l in inputValues:
    x_offset, y_offset, x, y, num = parseInput(l)
    m = matrixOffset(x_offset, y_offset, x, y)
    fab = np.add(fab, m)

# boolean array greater than zero
b = np.greater(fab, np.full((dim, dim), 1))

print(f"The solution to AOC day 3 is {np.sum(b)}")


## part 2

for l in inputValues:
    x_offset, y_offset, x, y, num = parseInput(l)
    newM = np.full((x, y), 1)
    # print(x)

    # extract values from fab
    v = fab[x_offset:x_offset+x, y_offset:y_offset+y]

    if np.array_equal(newM, v):
        print(f'The answer to part 2 is {num}')
