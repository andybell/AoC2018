# AoC day 4
import datetime
import pandas as pd

# puzzle input
inputFile = open("input.txt", 'r')
inputValues = [x.strip() for x in inputFile.readlines()]  # read lines to list

print(inputValues)

# example values
exampleValues = ["[1518-11-01 00:05] falls asleep",
                 "[1518-11-01 00:25] wakes up", "[1518-11-01 00:30] falls asleep", "[1518-11-01 00:55] wakes up",
                 "[1518-11-01 23:58] Guard #99 begins shift", "[1518-11-02 00:40] falls asleep",
                 "[1518-11-02 00:50] wakes up", "[1518-11-03 00:05] Guard #10 begins shift",
                 "[1518-11-03 00:24] falls asleep", "[1518-11-03 00:29] wakes up",
                 "[1518-11-04 00:02] Guard #99 begins shift", "[1518-11-04 00:36] falls asleep",
                 "[1518-11-04 00:46] wakes up", "[1518-11-05 00:03] Guard #99 begins shift",
                 "[1518-11-05 00:45] falls asleep", "[1518-11-05 00:55] wakes up", "[1518-11-01 00:00] Guard #10 begins shift", ]

# parse inputs in
def parseInputs(line):
    ts = datetime.datetime.strptime(line[1:17], "%Y-%m-%d %H:%M")
    id = None
    if "Guard" in line:
        lineType = "id"
        id = int(line.split(" ")[3].replace("#", ""))
    if "wakes" in line:
        lineType = "wakeup"
    if "asleep" in line:
        lineType = "asleep"
    return ts, lineType, id


def minuteBins(startMin, endMin):
    bins = []
    if endMin > startMin:
        startMin = startMin + 60

    current = startMin
    while current > endMin:
        current += -1
        bins.append(current % 60)
    return bins


print(minuteBins(5, 2))

print(minuteBins(6, 55))

# list comp to pull out the minutes
def binList(inputValues):

    binList = []

    for i in range(len(inputValues)):
        if i == 0:
            #print("skip")
            pass
        else:
            binList.append(minuteBins(int(inputValues[i][15:17]), int(inputValues[i-1][15:17])))
    return binList


# TODO make sure list is in order

binTimes = binList(exampleValues)

print(binTimes)