import ids  , Astar 
import Bidirectional_Search


## this function check if next state for butter is deadlock or not 
def isDeadlock(butter,robot, search ,direction , graph  , butters = [] ):
        
        robotsNewPlace = placeRobot(direction , butter)


        if len(robotsNewPlace) >= 3  :
            return True

        xmax = 0
        ymax = 0
        for ii in graph.keys():
            xx = int(ii[1])
            yy = int(ii[0])
            xmax  = max(xmax , xx)
            ymax  = max(ymax , yy)
        ry = int(robotsNewPlace[0])
        rx = int(robotsNewPlace[1])

        if rx > xmax or ry > ymax or rx < 0 or ry < 0 :
            return True
    

        if(checktwobefor(graph ,robotsNewPlace, butters)):

            if(search == "ids"):
                (q, d) =ids.iterativeDeepening(graph,robot , robotsNewPlace, 20)
                if(q):
                    return False
                else:
                    return True

            elif search =="astar" or search == "bidirectional":
                (q  , c , d) = Astar.a_star( graph , robot , robotsNewPlace , True , None , None , butter )
                if(q):
                    return False
                else:
                    return True
                # return False
                
        else:
            return True



    
def deadlockbd(graph , currentpos, nextpos ,parentpos, butters = []  ):


    xmax = 0
    ymax = 0
    for ii in graph.keys():
        xx = int(ii[1])
        yy = int(ii[0])
        xmax  = max(xmax , xx)
        ymax  = max(ymax , yy)


    cy = int(currentpos[0])
    cx = int(currentpos[1])
    ny = int(nextpos[0])
    nx = int(nextpos[1])
    py = int(parentpos[0])
    px = int(parentpos[1])

    
    rx = -1
    ry = -1
    rnx = -1
    rny = -1


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

    if cy == py : 
        rny = cy
        if cx - px > 0 :
            rnx = cx + 1
        else :
            rnx = cx - 1
    elif cx == px : 
        rnx = cx
        if cy - py > 0 :
            rny = cy + 1
        else :
            rny = cy - 1


    if rx > xmax or rnx > xmax or rx < 0 or rnx < 0 :
        return True
    
    if ry > ymax or rny > ymax or ry < 0 or rny < 0 :
        return True


    robotpos = str(ry) + str(rx)
    robotnewpos = str(rny) + str(rnx)

    

    checkresult = checktwobefor(graph , robotpos , butters)
    if checkresult is False :
        return True


    checkresult = checktwobefor(graph , robotnewpos , butters)
    if checkresult is False :
        return True


    
    if(checkfourside(graph ,robotpos , nextpos )):
        return True
    
    (q, c , d) = Astar.a_star(graph , robotpos , robotnewpos  , True ,None , butters , nextpos )
    if(q) :
        return False
    else:
        return True

    

    return False 

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
def checkAvailable(graph , next , butters , robot):
    if next in graph :
        if graph[next][0] == 'x'  or (next in butters) or (next == robot):
            return False
    return True

def checktwobefor(graph , next , butters =None):
    if next in graph :
        if graph[next][0] == 'x'   :
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


def checkfourside(graph , pos , nextpos) :
    
    tmp = graph[nextpos][0]
    graph[nextpos][0] = 'x'

    x = int(pos[1])
    y = int(pos[0])

    xmax = 0
    ymax = 0
    for ii in graph.keys():
        xx = int(ii[1])
        yy = int(ii[0])
        xmax  = max(xmax , xx)
        ymax  = max(ymax , yy) 

    if y != 0 :
        xy1  = str(y-1) + str(x)
        xy1 = graph[xy1][0]
    else :
        xy1 = "x"
    
    if y != ymax :
        xy2  = str(y+1) + str(x)
        xy2 = graph[xy2][0]
    else :
        xy2 = "x"
    
    if x != 0 :
        xy3  = str(y) + str(x-1)
        xy3 = graph[xy3][0]
    else :
        xy3 = "x"
    
    if x != xmax :
        xy4  = str(y) + str(x+1)
        xy4 = graph[xy4][0]
    else :
        xy4 = "x"
    
    graph[nextpos][0] = tmp
    if xy1 != "x" or xy2 != "x" or xy3 != "x" or xy4 != "x"  :
        return False
    
    return True