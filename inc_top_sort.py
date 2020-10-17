# the below topological sort is incomplete
# reason - it doesn't have its pre requisited - complete DFS
# there is only DFS for the nodes reachable by source, but what about others?
# in other file there is a DFS with recursion - more readable code and complete DFS

# the below code would also be modifed to cover all things but it would defeat the purpose by spoiling it
# main aim of writting DFS like this w/o recrusion is to understand clearly the difference btn DFS and BFS
# by using stack(DFS) instead of queue(BFS)

class Node:
    def __init__(self, item, parent=None, visited=False):
        self.item = item
        self.parent = parent
        self.visited = visited

nodes = {} # each node can be accesed using its number, example node1 can be accessed with dict_of_nodes[1]
for i in range(0,6):
    nodes[i] = Node(item=i)

# directed graph
graph = {
  0: [],
  1:[],
  2: [3],
  3: [1],
  4: [1,0],
  5: [2,0]
} 

# dfs
stack = [5]
reverse_top_sort = []

while stack:
    node_num = stack.pop(-1)
    reverse_top_sort.append(node_num)
    nodes[node_num].visited = True
    for neighbour in graph[node_num]:
        if nodes[neighbour].visited == False:
            nodes[neighbour].visited = True
            nodes[neighbour].parent = nodes[node_num]
            stack.append(neighbour)
        
# 4 is not reachable from 5, we can add it later

print(reverse_top_sort)