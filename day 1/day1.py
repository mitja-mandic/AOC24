list1 = []
list2 = []
with open("day1_input.txt",'r') as f:   
    for line in f:
        values = line.split()
        list1.append(values[0])
        list2.append(values[1])

    