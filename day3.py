import re

fileLoc = r'C:/Users/mandicm/Desktop/AOC24/day 3/day3_input.txt'

with open(fileLoc, 'r') as f:
    data = f.read().replace('\n','')

pat = r'mul\(\d{1,3},\d{1,3}\)'
parsedList = re.findall(pat, data)

def parseList(pattern, inputList):
    return re.findall(pattern, inputList)  

def calculate(inputList):
    sol = 0
    for pair in inputList:
        nums = re.findall(r'\d{1,3}',pair)
        sol += int(nums[0])*int(nums[1])
    return sol

dontPat = re.compile('don\'t\(\)')
doPat = re.compile('do\(\)')

complexPat = re.compile('(?<=don\'t\(\))(.*)(?=do\(\))')
toRemove = re.split(dontPat, data)




#for removal in toRemove:
#    newData = data.replace(removal,'')

#print(calculate(parseList(pat,newData)))
