# 2018 Advent of Code - Day 1

# load the input from the text file as a list
day1inputFile = open("input.txt", 'r')
day1input = [int(x.strip()) for x in day1inputFile.readlines()] # cast as numbers


def freqAdj(adjustList):
    """
    Change the frequency by the adjustments in the list of values sequentially
    :param adjustList: list of values to adjust
    :return: final frequency
    """
    freq = 0 # start at frequency of zero

    for i in adjustList: # loop through list of adjustments
        freq += i  # add adjustment to current frequency

    return freq

# tests
print(3 == freqAdj([1, -2, 3, 1]))
print(3 == freqAdj([1, 1, 1]))
print(0 == freqAdj([1, 1, -2]))
print(-6 == freqAdj([-1, -2, -3]))

# Day 1: part 1 solution
print(f"Day 1 part 1 answer: {freqAdj(day1input)}")
