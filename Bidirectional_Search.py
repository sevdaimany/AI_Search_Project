import collections
import problem


# BidirectionalSearch implementation
def BidirectionalSearch(graph , srcm , destm , isrobot = False , robotpos = None , butters = [] , current_butter = None ):
	
	size  = len(graph)

	src_queue = list()
	dest_queue = list()

	src_visited = collections.defaultdict(lambda: False)
	dest_visited = collections.defaultdict(lambda: False)

	src_parent = dict()
	dest_parent = dict()
		

	def bfs(direction = 'forward'):
		
		if direction == 'forward':
			
			# BFS in forward direction
			current = src_queue.pop(0)
			connected_node = graph[current]
			i = 2

			if isrobot is True : 
				if current == current_butter :
					return 
					# print("fuck")

			while len(connected_node) > i:
				
				vertex = connected_node[i][0]
				i += 1

				if not problem.checktwobefor(graph , vertex , butters) :
					continue
				
				parentpos = None
				if current in src_parent.keys():
					parentpos = src_parent[current]
				else:
					parentpos = robotpos

				if 	parentpos == -1 :
					parentpos = robotpos
				
				tmp = graph[current][0]
				graph[current][0] = 'x'
				if isrobot is False :
					direction = problem.whichDirection(current , vertex  )
					if problem.isDeadlock(current , parentpos , "astar" , direction , graph , None ) :
						graph[current][0] = tmp 
						continue
				graph[current][0] = tmp

				if not src_visited[vertex]:
					src_queue.append(vertex)
					src_visited[vertex] = True
					src_parent[vertex] = current
					
				
		else:
			
			# BFS in backward direction
			current = dest_queue.pop(0)
			connected_node = graph[current]
			i = 2

			# if isrobot is True : 
			# 	if current == current_butter :
			# 		return 
			# 		# print("fuck")

			
			while len(connected_node) > i:
				
				vertex = connected_node[i][0]
				i += 1

				if not problem.checktwobefor(graph , vertex , butters) :
					continue

				
				parentpos = None
				if current in dest_parent.keys():
					parentpos = dest_parent[current]

				if 	parentpos == -1 :
					parentpos = None

				tmp = graph[current][0]
				graph[current][0] = 'x'
				if parentpos is not None :
					if problem.deadlockbd(graph , current , vertex, parentpos , butters  ) :
						graph[current][0] = tmp
						continue
				graph[current][0] = tmp

				if not dest_visited[vertex]:
					dest_queue.append(vertex)
					dest_visited[vertex] = True
					dest_parent[vertex] = current
					
				
				
	# Check for intersecting vertex
	def is_intersecting():
		
		# Returns intersecting node
		# if present else -1
		for i in graph.keys():
			if (src_visited[i] and
				dest_visited[i]):
				return i

		return -1

	# Print the path from source to target
	def print_path(intersecting_node,
				src, dest):
						
		# Print final path from
		# source to destination
		path = list()
		path.append(intersecting_node)
		i = intersecting_node
		
		while i != src:
			path.append(src_parent[i])
			i = src_parent[i]
			
		path = path[::-1]
		i = intersecting_node
		
		while i != dest:
			path.append(dest_parent[i])
			i = dest_parent[i]
			
		return path
		
		
	
	# Function for bidirectional searching
	def bidirectional_search( src, dest):
		
		# Add source to queue and mark
		# visited as True and add its
		# parent as -1
		src_queue.append(src)
		src_visited[src] = True
		src_parent[src] = -1
		
		# Add destination to queue and
		# mark visited as True and add
		# its parent as -1
		dest_queue.append(dest)
		dest_visited[dest] = True
		dest_parent[dest] = -1

		path = []
		while src_queue and dest_queue:
			
			
			# BFS in forward direction from
			# Source Vertex
			bfs(direction = 'forward')
			
			# BFS in reverse direction
			# from Destination Vertex
			bfs(direction = 'backward')
			
			# Check for intersecting vertex
			intersecting_node = is_intersecting()
			
			# If intersecting vertex exists
			# then path from source to
			# destination exists
			if intersecting_node != -1:
				
				path = print_path(intersecting_node,src, dest)
				
				return path
				
				
		return path
		
	path = bidirectional_search(srcm , destm)
	if len(path) == 0 :
		return ()
	cost = 0
	for i in range(len(path)-1):
		cost +=  int(graph[path[i+1]][1])
	
	return (path , cost , len(path)-1)