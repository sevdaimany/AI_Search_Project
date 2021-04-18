def isDeadlock(butter,robot, search ,direction , graph):
        
        endX =0;
        endY = 0;
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
         
        if(checkAvailable(graph ,str(endX) + str(endY) )):
            if search(graph,robot , str(endX) + str(endY), 20):
                return False
            else:
                return True
        else:
            return True
            
        
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
    elif yFirst == (ySecond - 1):
        return "l"
   


def checkAvailable(graph , next):
    if next in graph :
        if graph[next][0] == 'x' :
            return False
    return True
