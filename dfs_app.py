class Node:
    def __init__(self, item, level=99999, parent=None, visited=False):
        self.item = item
        self.level = level
        self.parent = parent
        self.visited = visited

nodes = {} # each node can be accesed using its number, example node1 can be accessed with dict_of_nodes[1]
for i in range(1,4):
    nodes[i] = Node(item=i)

# directed graph
graph = {
   1: [2],
   2: [3],
   3:[1]
} 

# dfs
stack = [1]
while stack:
    node_num = stack.pop(-1)
    nodes[node_num].visited = True
    for neighbour in graph[node_num]:
        if nodes[neighbour].visited == False:
            nodes[neighbour].visited = True
            nodes[neighbour].parent = nodes[node_num]
            stack.append(neighbour)


#cycle detection
# there is a cycle if there is a backward edge
# a backward edge is an edge which is from a node to its ancestors
all_nodes = [1,2,3] # taking all these nodes that are reachable from 1
for i in all_nodes:
    all_ancestors = []
    current_parent = nodes[i].parent
    # u make a list of all ancestors by taking its parents and parents til u reach the root/source
    while current_parent != None:
        all_ancestors.append(current_parent.item)
        current_parent =  current_parent.parent
    # an array of all reachable nodes
    paths = graph[i]
    # if there is a backward edge, it will have a path to its ancestors
    if len(set(all_ancestors).intersection(set(paths))) != 0:
        print('edge deteched due to back edge frm ',i,'to ',set(all_ancestors).intersection(set(paths)))
        
    
