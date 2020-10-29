# the below code is a good example the if things like Graph and node are orgranized well
# code performance can be improved
# explaination:
#   in dijkstra2.py, in the relax function to relax the neighbours of the greedy node
#     we had to get the neighbours then for each neighbour iterate the queue and reduce its distance
#   but here, we have used a variable called distance from source, which avoids the use of iterating the queue
#   and we get the neighbout and decrease the key directly
#   in previous code , we have to get the neighbour, find the neighbour in array and decrease key
# now we can say that relax is indeed of theta(E log(v))
# where as in the previous code it was theta(E log(v) V) , and extra V for iterating through queue


# instead of using a array lets use a heap to extract min in logV time
class Node:
    def __init__(self, name, neighbours=[], distance_from_source=9999):
        self.name = name
        self.neighbours = neighbours
        self.distance_from_source = distance_from_source

    def add_neighbours(self, arr):
        self.neighbours = arr
            
    def get_neighbours(self):
        return self.neighbours 

    def print_neighbours(self):
        for i in self.neighbours:
            print('node ',i[0].name, 'is at a distance of ',i[1])

a = Node(name='a')
b = Node(name='b')
c = Node(name='c')
d = Node(name='d')
e = Node(name='e')

# construct graph
a.add_neighbours([(b,10), (c,3)])
b.add_neighbours([(d,2), (c,1)])
c.add_neighbours([(b,4), (d,8), (e,2)])
d.add_neighbours([(e,7)])
e.add_neighbours([(d,9)])

# initializing the distance to itself 0 and others to infinity

a.print_neighbours()
c.print_neighbours()

class Graph:
    def __init__(self, source, queue, s = {}):
        self.source = source
        self.queue = queue
        self.s = s
        for i in self.queue:
            if i.name == self.source.name:
                i.distance_from_source = 0

    def print_queue(self):
        for i in self.queue:
            print('node ',i.name, ' distance', i.distance_from_source) 

    def min_heapify(self,i):
        left = 2*i + 1
        right = 2*i + 2
        n = len(self.queue)
        # lets assume that largest the arr[i] is the min heap only
        smallest = i

        if left < n and self.queue[left].distance_from_source < self.queue[smallest].distance_from_source:
            smallest = left
        
        if right < n and self.queue[right].distance_from_source < self.queue[smallest].distance_from_source:
            smallest = right
        
        # if our assumption that i index element is already max heap, swap and recurisvely call it
        if smallest != i:
            self.queue[i], self.queue[smallest] = self.queue[smallest], self.queue[i]
            self.min_heapify(smallest)

    def build_heap(self):
        n = len(self.queue)
        start = n//2 - 1
        for i in range(start, -1, -1):
            self.min_heapify(i)

    def get_min_from_queue(self):
        length = len(self.queue)
        self.queue[0],self.queue[length-1] = self.queue[length-1], self.queue[0]
        smallest = self.queue.pop(length-1)
        self.min_heapify(0)
        return smallest
    
    def dijkstra(self):
        while self.queue:
            greedy_node = self.get_min_from_queue()
            self.s[greedy_node.name] = greedy_node.distance_from_source
            # relax all the neighbours from greedy node
            for neigh in greedy_node.get_neighbours():
                if neigh[0].distance_from_source > greedy_node.distance_from_source + neigh[1]:
                    neigh[0].distance_from_source = greedy_node.distance_from_source + neigh[1]
            # after relaxing heapify it as values are changed
            self.build_heap()

        print('s is ',self.s)

graph =  Graph(source=a, queue=[a,b,c,d,e])
graph.print_queue()
graph.dijkstra()


