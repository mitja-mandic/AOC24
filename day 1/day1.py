list1 = []
list2 = []
fileLoc = r'C:/Users/Mitja/Documents/AOC24/AOC24/day 1/day1_input.txt'
with open(fileLoc,'r') as f:   
    for line in f:
        values = line.split()
        list1.append(values[0])
        list2.append(values[1])

#tuplesList = zip(sorted(list1), sorted(list2))
#
#result = 0
#for x in tuplesList:
#    result += abs(int(x[0])-int(x[1]))

#print(result)
result2 = 0
for x in list1:
    repetitions = list2.count(x)
    result2 += int(x) * repetitions
print(result2)