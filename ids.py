import problem
def iterativeDeepening(graph , start , goal,length, robot = None ):
    depth = 0
    result = None
    while depth < length:
        stack  = []
        result = depthLimited(graph , start,goal ,depth , stack ,robot = robot)
        if result != None:
            break
        depth +=1
    return result , depth
    
def depthLimited(graph , start , goal, depth, stack ,visited = None , robot = None):
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
            if (not next[0] in visited )and (problem.checkAvailable(graph , next[0], start , robot)):
                if robot != None :
                    direction =  problem.whichDirection(start , next[0])
                    tmp = graph[start][0]
                    graph[start][0] = 'x'
                    checkDeadlock = problem.isDeadlock(start , robot ,"ids",direction , graph)
                    graph[start][0] = tmp
                    if not checkDeadlock:
                        reachGoal =depthLimited(graph , next[0] ,goal, depth-1,stack, visited, robot)
                        if reachGoal:
                             return reachGoal
                else:
                    reachGoal =depthLimited(graph , next[0] ,goal, depth-1,stack, visited , robot)
                    if reachGoal:
                        return reachGoal
                
    depth +=1
    stack.pop()





                

