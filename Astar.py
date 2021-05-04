import problem



class Node():

    def __init__(self, parent=None, position=None , cost=0 ):
        self.parent = parent
        self.position = position

        self.c = cost
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def a_star(mygraph, start, end , isrobot = False , robotpos = None , butters = [] , current_butter = None):

    sx = int(start[1])
    sy = int(start[0])
    ey = int(end[0])
    ex = int(end[1])

    if sx < 0 or sy < 0 or ex < 0 or ey < 0 :
        return False


    # Create start and end node
    start_node = Node(None, start , mygraph[start][1])
    start_node.g = start_node.h = start_node.f = 0

    end_node = Node(None, end , mygraph[end][1])
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    frontier = []
    explored = []

    current_node = None

    # Add the start node
    frontier.append(start_node)

    # Loop until you find the end
    while len(frontier) > 0:

    

        # Get the current node
        current_node = frontier[0]
        current_index = 0
        for index, item in enumerate(frontier):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            path.reverse()
            cost = 0
            for i in range(len(path)-1):
                cost +=  int(mygraph[path[i+1]][1])

            return (path , cost , len(path) -1 ) # Return reversed path


        if isrobot is True : 
                if current_node.position == current_butter :
                    frontier.pop(current_index)
                    continue 
                    # print("fuck")


        # Pop current off open list, add to closed list
        frontier.pop(current_index)
        explored.append(current_node)

        # Generate children
        children = []
        for new_position in mygraph[current_node.position]: # Adjacent squares

            if type(new_position) != tuple :
                continue

            # Get node position
            node_position = new_position[0]

            # Create new node
            new_node = Node(current_node, node_position , mygraph[node_position][1])

            # Append
            children.append(new_node)


        # Loop through children
        for child in children:
            bummer = False
            
        
            # Create the f, g, and h values
            child.g = current_node.g + child.c
            child.h = abs((int(child.position[0]) - int(end_node.position[0]))) + abs((int(child.position[1]) - int(end_node.position[1])))
            child.f = child.g + child.h

            # Child is on the closed list
            for closed_child in explored:
                if child == closed_child :
                    bummer  = True

            if bummer == True :
                continue
                    
            # Child is already in the open list
            for open_node in frontier:
                if child == open_node and child.g > open_node.g:
                    bummer  = True
            
            if bummer == True :
                continue

            robotp = None
            if current_node.parent is None :
                robotp = robotpos
            else:
                robotp = current_node.parent.position

            if not problem.checktwobefor(mygraph , child.position , butters) :
                bummer  = True
            
            if bummer == True :
                continue
                
            

            # if isrobot is False :
            #     if not problem.deadlock(mygraph , current_node.position , child.position , robotp , "astar") : 
            #         bummer  = True


            if isrobot is False :
                # tmp = mygraph[current_node.position][0]
                # mygraph[current_node.position][0] = 'x'
                direction = problem.whichDirection(current_node.position , child.position  )
                if problem.isDeadlock(current_node.position ,robotp , "astar" , direction , mygraph , butters ) : 
                    bummer  = True
                # mygraph[current_node.position][0] = tmp


            if bummer == True :
                continue

            # Add the child to the open list
            frontier.append(child)
    
    return (None , 0 , 0 )


