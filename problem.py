import ids  , Astar 
import Bidirectional_Search
from state import State


## this function check if next state for butter is deadlock or not 
def isDeadlock(butter,robot, search ,direction , graph):
        
        endX =0
        endY = 0
       
        robotsNewPlace = placeRobot(direction , butter)

        if(checktwobefor(graph ,robotsNewPlace,State.getButters())):

            if(search == "ids"):
                if(ids.iterativeDeepening(graph,robot , robotsNewPlace, 20)):
                    return False
                else:
                    return True

            elif search == "bidirectional":
                None

            elif search =="astar":
                # if(Astar.a_star( graph , State.getButters() , robotsNewPlace)):
                #     return False
                # else:
                #     return True
                return True
        else:
            return True


def deadlock(graph , currentpos, nextpos , parentpos , search):

    cx = int(currentpos[1])
    cy = int(currentpos[0])
    ny = int(nextpos[0])
    nx = int(nextpos[1])
    rx = -1
    ry = -1

    if cy == ny : 
        ry = cy
        if nx - cx > 0 :
            rx = cx - 1
        else :
            rx = cx + 1
    elif cx == nx : 
        rx = cx
        if ny - cy > 0 :
            ry = cy - 1
        else :
            ry = cy + 1

    robotpos = str(ry) + str(rx)

    checkresult = checktwobefor(graph , robotpos , State.getButters() )

    if parentpos is not None :
        
        if(search == "ids"):
            pass

        elif search == "bidirectional":
            checkpath = Bidirectional_Search.BidirectionalSearch(graph , parentpos , robotpos   , True)

        elif search =="astar":

            checkpath = Astar.a_star(graph , parentpos.position , robotpos   , True)

        
    else :
        checkpath = True
    

    return checkresult and ( checkpath is not False)


    
def deadlockbd(graph , currentpos, nextpos ):

    cx = int(currentpos[1])
    cy = int(currentpos[0])
    ny = int(nextpos[0])
    nx = int(nextpos[1])
    rx = -1
    ry = -1

    if cy == ny : 
        ry = cy
        if nx - cx > 0 :
            rx = nx + 1
        else :
            rx = nx - 1
    elif cx == nx : 
        rx = cx
        if ny - cy > 0 :
            ry = ny + 1
        else :
            ry = ny - 1

    robotpos = str(ry) + str(rx)

    checkresult = checktwobefor(graph , robotpos , State.getButters() )

    return checkresult 

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
def checkAvailable(graph , next , butters ,robot):
    if next in graph :
        if graph[next][0] == 'x'  or (next in butters) or (next == robot):
            return False
    return True

def checktwobefor(graph , next , butters):
    if next in graph :
        if graph[next][0] == 'x'  or (next in butters) :
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