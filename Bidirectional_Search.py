
import collections

# BidirectionalSearch implementation
def BidirectionalSearch(graph , srcm , destm):
	
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

			while len(connected_node) > i:
				
				vertex = connected_node[i][0]

				if not src_visited[vertex]:
					src_queue.append(vertex)
					src_visited[vertex] = True
					src_parent[vertex] = current
					
				i += 1
		else:
			
			current = dest_queue.pop(0)
			connected_node = graph[current]
			i = 2

			while len(connected_node) > i:
				vertex = connected_node[i][0]
				
				if not dest_visited[vertex]:
					dest_queue.append(vertex)
					dest_visited[vertex] = True
					dest_parent[vertex] = current
					
				i += 1
				
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
		
	msgg = bidirectional_search(srcm , destm)
	return msgg
