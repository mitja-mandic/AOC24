fileLoc = r'C:/Users/Mitja/Documents/AOC24/AOC24/day 6/input_day6.txt'

floorPlan = []
with open(fileLoc,'r') as f:
    for line in f:
        floorPlan.append(line.strip())

def findStartPosition(plan):
    nrFloors = len(plan)
    for i in range(nrFloors):
        if "^" in plan[i]:
            location = plan[i].index("^")
            return (i,location)
        

def determineNextMove(currentPosition, plan, direction):
    
    if direction=="up":
        nextChar = plan[currentPosition[0]-1][currentPosition[1]]
        if nextChar == "#":
            newLoc = (currentPosition[0],currentPosition[1]+1)
            return "right",newLoc
        else:
            return "up",(currentPosition[0]-1,currentPosition[1])
        
    elif direction == "down":
        nextChar = plan[currentPosition[0]+1][currentPosition[1]]
        if nextChar == "#":
            newLoc = (currentPosition[0],currentPosition[1]-1)
            return "left",newLoc
        else:
            return "down",(currentPosition[0]+1,currentPosition[1])
    
    elif direction == "right":
        nextChar = plan[currentPosition[0]][currentPosition[1]+1]
        if nextChar == "#":
            newLoc = (currentPosition[0]+1,currentPosition[1])
            return "down",newLoc
        else:
            return "right",(currentPosition[0],currentPosition[1]+1)
    elif direction=="left":
        nextChar = plan[currentPosition[0]][currentPosition[1]-1]
        if nextChar == "#":
            newLoc = (currentPosition[0]-1,currentPosition[1])
            return "up",newLoc
        else:
            return "left",(currentPosition[0],currentPosition[1]-1)


def modifyFloorPlan(position, plan, direction):
    pos1 = position[0]
    pos2 = position[1]

    if direction=="up":
        
        plan[pos1-1][pos2] = "#"
        return plan
    elif direction=="down":
        plan[pos1+1][pos2] = "#"
        return plan
    elif direction=="right":
        plan[pos1][pos2+1] = "#"
        return plan
    else:
        plan[pos1][pos2-1] = "#"
        return plan

direction = "up"
visitedLocations = set()
nrFloors = len(floorPlan)
floorSize = len(floorPlan[0])
pos1, pos2 = findStartPosition(floorPlan)[0],findStartPosition(floorPlan)[1]
visitedLocations.add((direction,pos1,pos2))
potentialObstructions = set()
end1 = (pos1==0 and direction == "up")
end2 = (pos1 == nrFloors-1 and direction == "down")
end3 = (pos2 == 0 and direction == "left")
end4 = (pos2 == floorSize-1 and direction == "right")



while not (end1 or end2 or end3 or end4):
    modFloorPlan = modifyFloorPlan((pos1,pos2),floorPlan,direction)
    nextMove = determineNextMove((pos1,pos2),floorPlan, direction)
    nextMoveWithObstruction = determineNextMove((pos1,pos2),modFloorPlan, direction)
    if nextMoveWithObstruction in visitedLocations:
        potentialObstructions.add(nextMoveWithObstruction[1])


    direction = nextMove[0]
    pos1 = nextMove[1][0]
    pos2 = nextMove[1][1]
    
    
    
    visitedLocations.add((direction,pos1,pos2))
    end1 = (pos1==0 and direction == "up")
    end2 = (pos1 == nrFloors-1 and direction == "down")
    end3 = (pos2 == 0 and direction == "left")
    end4 = (pos2 == floorSize-1 and direction == "right")




