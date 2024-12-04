fileLoc = r'C:/Users/Mitja/Documents/AOC24/AOC24/day 4/day4_input.txt'
rows = []
with open(fileLoc,'r') as f:
    for line in f:
        rows.append(line.strip())

def check4rows(str1,str2,str3,str4):
    rowLength = len(str1)
    
    counter = 0
    i = 0
    while i < rowLength:
        
        #check if it appears in rows
        
        #column
        col = str1[i] + str2[i] + str3[i] + str4[i]

        #diagonal  
        if i < rowLength - 3:
            diag = str1[i] + str2[i + 1] + str3[i + 2] + str4[i + 3]
            
            row = str1[i:i + 4]

            diag2 = str1[i+3] + str2[i + 2] + str3[i + 1] + str4[i]
        else:
            diag = ""
            row = ""
            diag2 = ""
        solList = [row,col,diag,diag2]
        counter += solList.count('XMAS')
        counter += solList.count('SAMX')

        i+=1
    return counter


#solution = 0
#solution += rows[-1].count("XMAS") + rows[-1].count("SAMX") + rows[-2].count("XMAS") + rows[-2].count("SAMX") + rows[-3].count("XMAS") + rows[-3].count("SAMX")
#print(solution)
#for i in range(len(rows)-3):
#    solution += check4rows(rows[i],rows[i+1],rows[i+2],rows[i+3])
#print(solution)

def checkXmas(str1,str2,str3):
    rowLength = len(str1)
    i = 0
    sol = 0
    while i < rowLength - 2:
        diag1 = str1[i] + str2[i + 1] + str3[i + 2]
        diag2 = str1[i + 2] + str2[i + 1] + str3[i]

        if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
            sol += 1
        i += 1

    return sol

solution = 0
for i in range(len(rows)-2):
    solution += checkXmas(rows[i],rows[i+1],rows[i+2])
print(solution)