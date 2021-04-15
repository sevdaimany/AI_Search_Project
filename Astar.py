


class Node():

    def __init__(self, parent=None, position=None , cost=0):
        self.parent = parent
        self.position = position

        self.c = cost
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def a_star(mygraph, start, end):
    
    # Create start and end node
    start_node = Node(None, start , mygraph[start][1])
    start_node.g = start_node.h = start_node.f = 0

    end_node = Node(None, end , mygraph[end][1])
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    frontier = []
    explored = []

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

        # Pop current off open list, add to closed list
        frontier.pop(current_index)
        explored.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

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
            child.h = abs((child.position[0] - end_node.position[0])) + abs((child.position[1] - end_node.position[1]))
            child.f = child.g + child.h

            # Child is on the closed list
            for closed_child in explored:
                if child == closed_child :
                    bummer  = True
                    
            # Child is already in the open list
            for open_node in frontier:
                if child == open_node and child.g > open_node.g:
                    bummer  = True

            if bummer == True :
                continue

            # Add the child to the open list
            frontier.append(child)


