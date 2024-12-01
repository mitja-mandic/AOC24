fileLoc = "C:/Users/Mitja/Documents/AOC24/AOC24/day 1/day1_input.txt"

f = open(fileLoc, "r")
 
# to count total lines in the file
line_count = 0             
list1 = []
list2 = []

for lines in readlines(f)
    val1, val2 = split(lines, " ")
    push!(list1,val1)
    push!(list2,val2)
    # increment line_count
    global line_count += 1 
    # print the line
    println(val1)
end
 
# total lines in file
println("line count is $line_count")
 
close(f)