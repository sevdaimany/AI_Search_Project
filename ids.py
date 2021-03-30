graph = {
	1 : [2, 3],
	2 : [4],
	3 : [5, 6],
}

def dls(node , end , depth):
    print(node,depth)

    if depth == 0 and node== end:
        return node
    elif depth > 0:
        for i in graph[node]:
           test = dls(i , end , depth -1)
           if test == end:
                return end

