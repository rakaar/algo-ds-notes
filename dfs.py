class Node:
    def __init__(self, item, level=99999, parent=None, visited=False):
        self.item = item
        self.level = level
        self.parent = parent
        self.visited = visited

nodes = {} # each node can be accesed using its number, example node1 can be accessed with dict_of_nodes[1]
for i in range(1,11):
    nodes[i] = Node(item=i)

# directed graph
graph = {
    1 : [9,5,2],
    2: [3],
    3: [4],
    4: [],
    5: [8,6],
    6: [7],
    7: [],
    8: [],
    9: [10],
    10: []
} 

# dfs
stack = [1]
while stack:
    node_num = stack.pop(-1)
    nodes[node_num].visited = True
    print('on ',node_num)
    for neighbour in graph[node_num]:
        if nodes[neighbour].visited == False:
            nodes[neighbour].visited = True
            nodes[neighbour].parent = nodes[node_num]
            stack.append(neighbour)

 
# the above code only explores all the nodes reachable from 1
# if u want to explore the whole graph, u need to do the DFS from other nodes too
# maintain an array of ones who u have explored, and if u know what  nodes are there
# check them if they are in ur visited explored array or not
# if yes, then good. If not! start a DFS from there


# not a good one for finding shortest paths
# as it goes the way it found first