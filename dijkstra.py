class Node:
    def __init__(self, name, neighbours):
        self.name = name
        self.neighbours = {}

    def add_neighbours(self, arr):
        # arr will be in type (Node(name='b'), 10)
        for i in arr:
            self.neighbours[i[0].name] = i[1]
            
    def get_neighbours(self):
        return self.neighbours 

a = Node(name='a', neighbours={})
b = Node(name='b',neighbours={})
c = Node(name='c', neighbours={})
d = Node(name='d', neighbours={})
e = Node(name='e', neighbours={})

# construct graph
a.add_neighbours([(b,10), (c,3)])
b.add_neighbours([(d,2), (c,1)])
c.add_neighbours([(b,4), (d,8), (e,2)])
d.add_neighbours([(e,7)])
e.add_neighbours([(d,9)])

# initializing the distance to itself 0 and others to infinity


queue = [
    [a,0],
    [b,9999],
    [c,9999],
    [d,9999],
    [e,9999]
]
s = {}
    
def get_minimum_from_queue():
    min_index = 0
    q_length = len(queue)
    for i in range(1,q_length):
        if queue[i][1] < queue[min_index][1]:
            min_index = i
    smallest = queue.pop(min_index)
    return smallest


def relax(node, delta):
    neighs = node.get_neighbours()
    for n,dist in neighs.items():
        for q in queue:
            if q[0].name == n:
                q[1] = delta + dist
                

# start relaxing from source vertex
def dijkstra():
    while queue:
        greedy_node = get_minimum_from_queue()
        s[greedy_node[0].name] = greedy_node[1]
        relax(greedy_node[0], greedy_node[1]) 


dijkstra()
print('shortest distances ',s)

# analysis of the above
# >greedy_node = get_minimum_from_queue() this line takes order(v), it iterates the whole array to get minimum
# it can be made better by using priority queue and it reduces to logv
# currently the above code is order(v) for v vertices so it is v_squared
# it can be reduced to v*logv
# other slow thing is present in relax function
# u iterate thru each neighbour(this is compulsory u cant avoid it), but to find its corresponding place in queue, u iterate the whole queue
# can it be made better?
# no! i think bcoz even if its a heap, u have to search the whole thing