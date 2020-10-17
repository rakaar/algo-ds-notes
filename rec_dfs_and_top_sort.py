# for having a top sort, it is necesary to have a DAG, acyclic because u cant have order if there is a cycle
# now the basic idea behind making a topsort is visit the ones that have no dependency
# for example there is a dependency graph of packages or graph of courses and their prerequisistes
# u would like to build dependcies in such a way that u build first the ones that doesn't have a dependnecy and then build others that depend on them
# basicaly u dont want to get to a point in order where ur current package has a dependency that is built in future
# or simpler example, u want to take all the preques of the course u want to take, but those pre reqs also have pre reqs

# how do we achieve this?
# do dfs visit, then reverse the array, that means
# keep doing DFS from the source, and all the vertices once they have vertices to a an array once they nothing left to explore
# 1 -> 2 -> 3 -> 4
# if u do dfs u go from 1 to 2, then to 3, then to 4. u have nothing to visit from 4, add 4
# now u have nothing to visit from 3 add 3
# nothing to visit from  2, add 2
# nothing to visit from 1, add 1
# in practice, this is achieved using recursion

class Node:
    def __init__(self, item, parent=None, visited=False):
        self.item = item
        self.parent = parent
        self.visited = visited

nodes = {} # each node can be accesed using its number, example node1 can be accessed with dict_of_nodes[1]
for i in range(1,8):
    nodes[i] = Node(item=i)

# directed acyclic graph
graph = {
 1: [2,7],
 2: [3],
 3: [4,6],
 4: [5,6],
 5:[],
 6:[],
 7: [3]
} 

# reverse of this wil be top sort
result = []
result1 = []

def dfs_visit(node):
    nodes[node].visited = True
    print('node on', node)
    result1.append(node)
    for neighbour in graph[node]:
        if nodes[neighbour].visited == False:
            dfs_visit(neighbour)
    result.append(node)
    
def dfs(node):
    dfs_visit(node)

dfs(1)
print(result)
print("top_sort", result[::-1])
print(result1)
r'''
Q: Why can't result1 be the top sort?
A: Because if  u print mmediately as u visit, u might miss the the parent of the node, which has not yet been visited
for example  
     1
    / \ 
   /   \ 
  v     v
 2 ----> 3
here if u go on print 1 , print 3, then print 2
1 3 2 is not the top sort bcoz 3 depends on 2 as well, and 2 has to be reached before 3
so how do u tackle it?
we take the help of a tree here
in a tree
if u start from the leaf level, if that leaf is dependent on something then that will be added later to the list
and hence if u reverse the list, u will get the toposort order
for example 
here there are 2 cases of rec tree in the above graph 
 1  3. [3 2 1]
 /
 v
 2  2.[3 2]
 /  
 v
 3  1.[3]
top sort result reverse of [3 2 1]

  1 3.[3 2 1]
/   \
3    2
1.[3] 2. [3 2]
see in the above 3 was dependent on 2, and 2 got added later in the list and u got the right dependency order by reverse the list
because its a acylci graph 
in an edge from u -> v
if u visit u first then v, then no issues
if u vist v first then u, u might be woried that top sort may go wrong
but since there are no cycles, v is not having any back edges(to the ancestors) v wil finish before u
hence v will be added to the list, then u
and ultimately u reverse and get the answer 
aha moment @ https://youtu.be/AfSk24UTFS8?t=2966
'''


r'''
edges are directed from top to bottom
                                            dfs(1)
                                               |
                                               v
                {7. adds 1 to result}        dfs_visit(1)
                                               /         \
                                              /           \
                                             /             \
                    {6. adds 7 to result}   dfs_visit(7)    \    
                                    {5. adds 2 to result}  dfs_visit(2)
                                                          /    
                                                         /     
                                                        /      
                                                       /       
                            {4. adds 3 to result} dfs_visit(3)
                                                       /    \
                                                      /      \
                                                     /        \
                                                    /          \
                    {3. adds 4 to result}    dfs_visit(4) ----> dfs_visit(6)
                                                 /               {2. adds 6 to result}
                                                /
                                            dfs_visit(5)
                                            {1. adds 5 to result}
'''