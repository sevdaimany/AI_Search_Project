## this function check if next state for butter is deadlock or not 
def isDeadlock(butter,robot, search ,direction , graph , butterCoordinate):
        
        endX =0;
        endY = 0;
       
        robotsNewPlace = placeRobot(direction , butter)
        
        if(checkAvailable(graph ,robotsNewPlace,butterCoordinate )):
            if search(graph,robot , robotsNewPlace, 20):
                return False
            else:
                return True
        else:
            return True
            

## this function return which direction butter is going to go ('r' , 'l' ,'u', 'd')      
def whichDirection(first , second):
    xFirst = int(first[0:1])
    yFirst = int(first[-1:])
    xSecond = int(second[0:1])
    ySecond = int(second[-1:])

    if xSecond == (xFirst +1):
        return "d"
    elif xSecond == (xFirst -1):
        return "u"
    elif ySecond == (yFirst +1):
        return "r"
    elif ySecond == (yFirst - 1):
        return "l"
   


## this function check if next state is empty or not
def checkAvailable(graph , next , butterCoordinate):
    if next in graph :
        if graph[next][0] == 'x'  or next == butterCoordinate :
            return False
    return True


## this function return a state that robot should go to push butter
def placeRobot(direction , butter):
    rowButter = int(butter[0:1])
    colButter = int(butter[-1:])
    if(direction == "r"):
        endX = rowButter 
        endY = colButter - 1
    if(direction == "l"):
        endX = rowButter 
        endY = colButter + 1 
    if(direction == "u"):
        endX = rowButter +1
        endY = colButter 
    if(direction == "d"):
        endX = rowButter  -1
        endY = colButter

    return str(endX) + str(endY) 