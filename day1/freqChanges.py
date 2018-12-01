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
# print(3 == freqAdj([1, -2, 3, 1]))
# print(3 == freqAdj([1, 1, 1]))
# print(0 == freqAdj([1, 1, -2]))
# print(-6 == freqAdj([-1, -2, -3]))

# Day 1: part 1 solution
print(f"Day 1 part 1 answer: {freqAdj(day1input)}")


# part 2

def freqRepeat(adjustList):

    priorFreq = [0]  # list to hold intermediate frequencies
    freq = 0  # start at frequency of zero
    i = 0  # index

    # loop over adjustment potnetially multiple times
    while adjustList[i % len(adjustList)]:

        # add adjustment to current frequency
        freq += adjustList[i % len(adjustList)]

        # end the while loop if the freq already have been seen
        if freq in priorFreq:
            break
        else:
            priorFreq.append(freq) # add current frequency to list of known frequencies
            i += 1  # add 1 to index
    return freq


# tests
# print(0 == freqRepeat([1, -1]))
# print(10 == freqRepeat([3, 3, 4, -2, -4]))
# print(5 == freqRepeat([-6, 3, 8, 5, -6]))
# print(14 == freqRepeat([7, 7, -2, -7, -4]))

print(f"Day 1 part 2 answer: {freqRepeat(day1input)}")  # this is kinda of slow
