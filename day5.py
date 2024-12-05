fileLoc1 = r'C:/Users/mandicm/Desktop/AOC24/input_day5_part1.txt'
fileLoc2 = r'C:/Users/mandicm/Desktop/AOC24/input_day5_part2.txt'

rules_firstNumber = {}
rules_secondNumber = {}
with open(fileLoc1,'r') as f:
    for line in f:
        auxLst = line.split("|")
        key = int(auxLst[0])
        val = int(auxLst[1].strip())
        if key not in rules_firstNumber:
            rules_firstNumber[key] = {val}
        else:
            rules_firstNumber[key].add(val)
        if val not in rules_secondNumber:
            rules_secondNumber[val] = {key}
        else:
            rules_secondNumber[val].add(key)

instructions = []
with open(fileLoc2,'r') as f:
    for line in f:
        lineList = line.strip().split(',')
        lineList = list(map(int,lineList))
        instructions.append(lineList)

#print(rules_firstNumber)
#print(rules_secondNumber)
def checkLine(lst):
    i = 0
    currentNumber = lst[i]
    before = set(lst[:i])
    after = set(lst[i+1:])


    while after.issubset(rules_firstNumber[currentNumber]) and before.issubset(rules_secondNumber[currentNumber]) and i < len(lst):
        currentNumber = lst[i]
        before = set(lst[:i])
        after = set(lst[i+1:])
        i += 1
    
    #print(i)
    if i==len(lst):
        return lst[len(lst)//2]
    else:
        return 0



solution = 0
for line in instructions:
    solution += checkLine(line)

print(solution)
