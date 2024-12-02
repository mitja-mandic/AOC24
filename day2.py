fileLoc = r'C:/Users/mandicm/Desktop/AOC24/day2_input.txt'
safe = 0

def ascOrDesc(inputList):
    print(inputList==sorted(inputList))
    print(inputList==sorted(inputList, reverse=False))
    return inputList == inputList.sort() or inputList == inputList.sort(reverse=True)


def isItSafe(inputList):
    inputList = list(map(int, inputList))
    #print(ascOrDesc(inputList))
    sortedList = sorted(inputList)
    descSortedList = sorted(inputList, reverse=True)
    if not(inputList == sortedList or inputList == descSortedList):
        return 0
    if len(inputList) == 1:
        return 1
    else:
        first = int(inputList[0])
        second = int(inputList[1])
        if 0 < abs(first-second) <= 3:
            return isItSafe(inputList[1:])
        else:
            return 0

print(isItSafe(['6', '7', '8', '10', '11', '13', '14']))
#print(isItSafe([55,58,61,64,67,70,72]))

safeLocs = 0
with open(fileLoc, 'r') as f:
    for line in f:
        currentLine = line.split()
        print(currentLine)
        safeLocs += isItSafe(currentLine)
print(safeLocs)

