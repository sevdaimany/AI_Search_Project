def iterativeDeepening(graph , startNode,goal):
    depth = 0
    result = None
    while result == None:
        stack  = []
        result = depthLimited(graph , startNode,goal ,depth , stack)
        depth +=1
    return result
    
def depthLimited(graph , start,goal, depth, stack,  visited = None):
    stack.append(start)

    if start == goal:
        print(stack)
        return stack
    elif depth == 0 :
        stack.pop() 
        return None 
    
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph.get(start):
        if type(next) == tuple: 
            if not next[0] in visited:
                reachGoal = depthLimited(graph , next[0] ,goal, depth-1,stack , visited)
                if reachGoal:
                    return reachGoal
    depth +=1
    stack.pop()
                

