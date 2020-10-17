# representing a graph
'''
    a ----- b
    |     / |
    |    /  |
    c ------d
the above undirected graph can be rep as
graph = {
    'a': [b,c],
    'b' : [c,d,a],
    'c': [a,b,d],
    'd': [b,c]
}
'''
class Node:
    def __init__(self, item, level=99999, parent=None, visited=False):
        self.item = item
        self.level = level # here calculated using calculated path, instead of assigning while exploring graph
        self.parent = parent
        self.visited = visited

nodes = {} # each node can be accesed using its number, example node1 can be accessed with dict_of_nodes[1]
for i in range(1,9):
    nodes[i] = Node(item=i)

graph = {
    1: [3,4],
    2: [3],
    3: [1,2],
    4: [1,5,6],
    5: [4,6,8],
    6: [4,5,7,8],
    7: [6,8],
    8: [5,6,7]
}
# bfs
# q is a queue(array) of nodes, whose neighbours are about to explored
q = [1] # add it to the q
while q:
    # the one whose neighbours u are going to explore
    node_num = q.pop(0)
    print('on node ', node_num)
    # mark it true
    nodes[node_num].visited = True
    for neighbour in graph[node_num]:
        if nodes[neighbour].visited == False:
            print('---- visited ',neighbour)
            nodes[neighbour].visited = True # mark them as true as u have explored this
            nodes[neighbour].parent = nodes[node_num] # add their parent
            q.append(neighbour) #add them to the list, as u are gng to xplore their neighbours again

# good for shortest paths, as it looks level by level ahead      
path = []
def calculate_path(node):
    if nodes[node].parent is None:
        path.append(str(node))
        print('->'.join(path[::-1]))
        path.clear() # as its a global variable
        return
    path.append(str(node))
    calculate_path(nodes[node].parent.item)

calculate_path(8)
calculate_path(6) 
calculate_path(5) 
calculate_path(7) 

