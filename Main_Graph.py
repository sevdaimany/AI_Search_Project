
import collections
import io ,Bidirectional_Search  , Astar
import eel
import json
import ids
import problem
import copy

eel.init("frontend")
# eel.init("C:\\Users\\rajab\\OneDrive\\Desktop\\Artificial Intelligence\\project\\git\\project1\\AI_Search_Project\\frontend")

mynodes = list()
mygraph = collections.defaultdict(list)
robot =""
goal = []
butters = []
depth = 0
search = "ids"
# search = "astar" or "ids" or "bidirectional"

address = "test3.txt"
with open(address) as reader :
    # print(reader.read())
    myinput = reader.read()
# print(myinput)




# myinput = """5	6
# 1	1	1	1	x	1
# 2	1	1b	1r	1b	2
# 2p	x	1	1	1	2
# 2	1	1	1	1	2
# 1	x	x	x	1	1p"""

# myinput = """5	5
# 1	1	1r	1	x
# 2	1	1b	1	1
# 1	x	x	1	x
# 2	1p	1	1	1
# x	x	1	1	1"""


# myinput = """5	5
# 1	1	1	1	1
# 2	x	1b	1r	1
# 2p	x	1	1	1
# 2	1	2	1	1
# 1	1	1	1	1"""

buf = io.StringIO(myinput)
n , m = map(int ,buf.readlines(1)[0].replace("\t" , " ").replace("\n" , "").split(" "))
for i in range(n):
    buffread = buf.readlines(1)[0].replace("\t" , " ").replace("\n" , "").split(" ")
    mynd = []
    for ii in range(m) : 
        mynd.append(buffread[ii])
    mynodes.append(mynd)



for i in range(n):
    for ii in range(m) :
        pos = str(i) + str(ii)
        # pos = (i , ii)
        kind = 'o'
        if mynodes[i][ii].count('r') > 0 :
            kind = 'r'
            robot = pos
        elif mynodes[i][ii].count('p') > 0 :
            kind = 'p'
            goal.append(pos)
        elif mynodes[i][ii].count('b') > 0 :
            kind = 'b'
            butters.append(pos)
        elif mynodes[i][ii].count('x') > 0 :
            kind = 'x'
        mygraph[pos].append(kind)

        if kind == 'x':
            mygraph[pos].append(-1)
            continue
        elif not mygraph[pos][0] == 'o' :
            mygraph[pos].append(int(mynodes[i][ii][:-1]))
        else :
            mygraph[pos].append(int(mynodes[i][ii]))

        # mygraph[pos].append(-1)

        if i > 0 and not mynodes[i-1][ii] == 'x' :
            cc = mynodes[i-1][ii]
            cc = cc.replace('r',"").replace('b',"").replace('p',"")
            mygraph[pos].append((str(i-1) + str(ii) , cc))
            # mygraph[pos].append(((i-1 , ii) , cc))

        if i < (n-1) and not mynodes[i+1][ii] == 'x' : 
            cc = mynodes[i+1][ii]
            cc = cc.replace("r","").replace("b","").replace("p","")
            mygraph[pos].append((str(i+1) + str(ii) , cc))
            # mygraph[pos].append(((i+1 , ii) , cc))

        if ii > 0 and not mynodes[i][ii-1] == 'x' : 
            cc = mynodes[i][ii-1]
            cc = cc.replace("r","").replace("b","").replace("p","")
            mygraph[pos].append((str(i) + str(ii-1) , cc))
            # mygraph[pos].append(((i , ii-1) , cc))

        if ii < (m-1) and not mynodes[i][ii+1] == 'x' : 
            cc = mynodes[i][ii+1]
            cc = cc.replace("r","").replace("b","").replace("p","")
            mygraph[pos].append((str(i) + str(ii+1) , cc))
            # mygraph[pos].append(((i , ii+1) , cc))



def init():
    for i in range(len(butters)):
        mygraph[butters[i]][0] = 'x'

@eel.expose
def main():
    success = True 
    GRAPH = copy.deepcopy(mygraph)
    init()
    butterPaths =[]
    robotPaths = []
    depth = [0 for i in range(len(butters))]
    costs = [0 for i in range(len(butters))]
    for i in range(len(butters)):
        mygraph[butters[i]][0] = "b"
        if i > 0:
            robotPos = butterPaths[i-1][-2]
        else:
            robotPos = robot
        if search == "ids":
            (q, d) = ids.iterativeDeepening(mygraph , butters[i] , goal[i] ,20,robot=robotPos)
            depth[i] = d
            costs[i] = d
            if q == None :
                success = False
            
            # print(q)
        elif search == "bidirectional":
            
            (q , c , d) = Bidirectional_Search.BidirectionalSearch(mygraph , butters[i] , goal[i]  , False ,  robotPos   , None , None )
            depth[i] = d
            costs[i] = c
            if q == None :
                success = False
            # print("hhh")
            # print(q)

        elif search =="astar":
            
            (q , c , d) = Astar.a_star(mygraph , butters[i]  , goal[i]  , False ,  robotPos   , None ,None )
            depth[i] = d
            costs[i] = c
            if q == None :
                success = False

        butterPaths.append(q)
        if(success):
            robotPaths.append(findRobotPaths(robotPos , q , search , i))
        print(butterPaths)
        print(robotPaths)
    return get_json_result({
        "graph" : GRAPH,
        "pathButters" : butterPaths,
        "pathsRobot" :robotPaths,
        "cost" :costs,
        "depth" : depth,
        "success" : success,
        "width" : m,
        "height" : n,
        },
        )

    
def get_json_result(results):
    return json.dumps(results)


def whereRobotGo(first ,second):
    direction = problem.whichDirection(first,second)
    return problem.placeRobot(direction , first)



def findRobotPaths(firstRobotCoordinate ,pathButter, search, whichButter):
    robotPaths = []
    robotCoordinate  = firstRobotCoordinate
    for i in range(len(pathButter)-1):
        coordinate = whereRobotGo(pathButter[i] , pathButter[i+1])
        tmp = mygraph[pathButter[i]][0]
        mygraph[pathButter[i]][0] = 'x'
        if(search == "ids"):
            (robotPath,e) = ids.iterativeDeepening(mygraph , robotCoordinate , coordinate ,30)

        elif search == "bidirectional":
            (robotPath , c , d) = Astar.a_star(mygraph , robotCoordinate , coordinate  , True ,  None   , None , None )

        elif search == "astar":
            (robotPath , c , d) = Astar.a_star(mygraph , robotCoordinate , coordinate  , True ,  None   , None , None )

        mygraph[pathButter[i]][0] = tmp
        robotCoordinate = pathButter[i]
        robotPaths.append(robotPath)

    tmp = mygraph[pathButter[-1]][0]
    mygraph[pathButter[-1]][0] = 'x'    
    if(search == "ids"):
        # tmp = mygraph[pathButter[-1]][0]
        # mygraph[pathButter[-1]][0] = 'x'
        (robotPath, e) = ids.iterativeDeepening(mygraph , robotCoordinate , pathButter[-2] ,20)
        # mygraph[pathButter[-1]][0] = tmp
    elif search == "bidirectional":
        (robotPath , c , d) = Astar.a_star(mygraph , robotCoordinate , pathButter[-2]  , True ,  None   , None , None )
    elif search == "astar":
        (robotPath , c , d) = Astar.a_star(mygraph , robotCoordinate , pathButter[-2]  , True ,  None   , None , None )

    # mygraph[pathButter[-1]][0] = tmp
    robotPaths.append(robotPath)
    return robotPaths

eel.start('index.html' ,size=(500,500))






