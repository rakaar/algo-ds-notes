# In A DAG, negative weights exists and shortest path is required
# topo sort 
# relax all the edges from vertices in the top sort

class Node:
    def __init__(self, name, neighbours=[], distance_from_source=9999):
        self.name = name
        self.neighbours = neighbours
        self.distance_from_source = distance_from_source
        self.visited = False

    def add_neighbours(self, arr):
        self.neighbours = arr
            
    def get_neighbours(self):
        return self.neighbours 

    def print_neighbours(self):
        for i in self.neighbours:
            print('node ',i[0].name, 'is at a distance of ',i[1])

r = Node(name='r')
s = Node(name='s')
t = Node(name='t')
x = Node(name='x')
y = Node(name='y')
z = Node(name='z')

# construct graph
r.add_neighbours([(s,5), (t,3)])
s.add_neighbours([(t,2), (x,6)])
t.add_neighbours([(x,7), (y,4), (z,2)])
x.add_neighbours([(y,-1), (z,1)])
y.add_neighbours([(z,-2)])
z.add_neighbours([])

# testing if neighs added properly or not
t.print_neighbours()

class Graph:
    def __init__(self, source, queue=[], s = {}):
        self.source = source
        self.source.distance_from_source = 0
        self.queue = queue
        self.s = s
        
    
    def dfs_visit(self, node):
        node.visited = True
        for neigh in node.get_neighbours():
            if neigh[0].visited == False:
                self.dfs_visit(neigh[0])
        self.queue.append(node)

    def print_top_sort(self):
        self.queue = self.queue[::-1]
        for q in self.queue:
            print(q.name)
    
    def relax(self, node):
        for neigh in node.get_neighbours():
            if neigh[0].distance_from_source > neigh[1] + node.distance_from_source:
                neigh[0].distance_from_source = neigh[1] + node.distance_from_source
    
    def shortest_path(self):
        for q in self.queue:
            self.relax(q)

    def print_shortest_distances(self):
        for q in self.queue:
            print('name',q.name, 'distance',q.distance_from_source)

g = Graph(source = r)
g.dfs_visit(r)
g.print_top_sort()
g.shortest_path()
g.print_shortest_distances()