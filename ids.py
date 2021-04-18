import problem
def iterativeDeepening(graph , start , goal,length,butterCoordinate  = None, robot = None ):
    depth = 0
    result = None
    while depth < length:
        stack  = []
        result = depthLimited(graph , start,goal ,depth , stack,butterCoordinate  ,robot = robot)
        if result != None:
            break
        depth +=1
    return result
    
def depthLimited(graph , start , goal, depth, stack ,butterCoordinate,visited = None , robot = None):
    stack.append(start)

    if start == goal:
        return stack
    elif depth == 0 :
        stack.pop() 
        return None 
    
    if visited is None:
        visited = set()

    visited.add(start)
    for next in graph.get(start):
        if type(next) == tuple: 
            if (not next[0] in visited )and (problem.checkAvailable(graph , next[0], butterCoordinate)):
                if robot != None :
                    direction =  problem.whichDirection(start , next[0])
                    if not problem.isDeadlock(start , robot ,iterativeDeepening,direction , graph,butterCoordinate) :
                        reachGoal =depthLimited(graph , next[0] ,goal, depth-1,stack,butterCoordinate, visited, robot)
                        if reachGoal:
                             return reachGoal
                else:
                    reachGoal =depthLimited(graph , next[0] ,goal, depth-1,stack ,butterCoordinate, visited , robot)
                    if reachGoal:
                        return reachGoal
                
    depth +=1
    stack.pop()





                

