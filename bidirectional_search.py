# search where alternatively forward and backward search are done
# terminating condition:- when a node from one of the frontier exists is already extracted from the other frontier

class Node:
    def __init__(self, name, neighbours=[], backward_neighbours=[], distance_from_source=9999, distance_from_target=9999):
        self.name = name
        self.neighbours = neighbours
        self.backward_neighbours = backward_neighbours
        self.distance_from_source = distance_from_source
        self.distance_from_target = distance_from_target

    def add_neighbours(self, arr):
        self.neighbours = arr
    
    def add_backward_neighbours(self, arr):
        self.backward_neighbours = arr
            
    def get_neighbours(self):
        return self.neighbours

    def get_backward_neighbours(self):
        return self.backward_neighbours 

    def print_neighbours(self):
        for i in self.neighbours:
            print('node ',i[0].name, 'is at a distance of ',i[1])

a = Node(name='a')
b = Node(name='b')
c = Node(name='c')
d = Node(name='d')
e = Node(name='e')

# construct graph
a.add_neighbours([(b,3), (d,5)])
b.add_neighbours([(c,3)])
c.add_neighbours([(e,3)])
d.add_neighbours([(e,5)])
e.add_neighbours([])

# construct graph for backwards also
a.add_backward_neighbours([])
b.add_backward_neighbours([(a,3)])
c.add_backward_neighbours([(b,3)])
d.add_backward_neighbours([(a,5)])
e.add_backward_neighbours([(c,3), (d,5)])

class Graph:
    def __init__(self, source, target, queue, backward_queue, s = {}, sb = {}):
        self.source = source
        self.target = target
        self.queue = queue
        self.backward_queue = backward_queue
        self.s = s
        self.sb = sb
        for i in self.queue:
            if i.name == self.source.name:
                i.distance_from_source = 0
        for i in self.backward_queue:
            if i.name == self.target.name:
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
    
    def min_heapify_backward_queue(self,i):
        left = 2*i + 1
        right = 2*i + 2
        n = len(self.backward_queue)
        # lets assume that largest the arr[i] is the min heap only
        smallest = i

        if left < n and self.backward_queue[left].distance_from_source < self.backward_queue[smallest].distance_from_source:
            smallest = left
        
        if right < n and self.backward_queue[right].distance_from_source < self.backward_queue[smallest].distance_from_source:
            smallest = right
        
        # if our assumption that i index element is already max heap, swap and recurisvely call it
        if smallest != i:
            self.backward_queue[i], self.backward_queue[smallest] = self.backward_queue[smallest], self.backward_queue[i]
            self.min_heapify(smallest)

    def build_heap(self):
        n = len(self.queue)
        start = n//2 - 1
        for i in range(start, -1, -1):
            self.min_heapify(i)
    
    def build_heap_backward_queue(self):
        n = len(self.backward_queue)
        start = n//2 - 1
        for i in range(start, -1, -1):
            self.min_heapify(i)

    def get_min_from_queue(self):
        length = len(self.queue)
        self.queue[0],self.queue[length-1] = self.queue[length-1], self.queue[0]
        smallest = self.queue.pop(length-1)
        self.min_heapify(0)
        return smallest
    
    def get_min_from_backward_queue(self):
        length = len(self.backward_queue)
        self.backward_queue[0],self.backward_queue[length-1] = self.backward_queue[length-1], self.backward_queue[0]
        smallest = self.backward_queue.pop(length-1)
        self.min_heapify(0)
        return smallest
    
    def dijkstra(self):
        while self.queue:
            greedy_node = self.get_min_from_queue()
            if greedy_node.name in self.sb:
                pass
                # exit code
            self.s[greedy_node.name] = greedy_node.distance_from_source
            # relax all the neighbours from greedy node
            for neigh in greedy_node.get_neighbours():
                if neigh[0].distance_from_source > greedy_node.distance_from_source + neigh[1]:
                    neigh[0].distance_from_source = greedy_node.distance_from_source + neigh[1]
            # after relaxing heapify it as values are changed
            self.build_heap()

    def backward_dijkstra(self):
        while self.backward_queue:
            greedy_node = self.get_min_from_backward_queue()
            if greedy_node.name in self.s:
                pass
                # exit code
            self.sb[greedy_node.name] = greedy_node.distance_from_source
            # relax all neighbours from greedy node
            for neigh in greedy_node.get_backward_neighbours():
                if neigh[0].distance_from_target > greedy_node.distance_from_target + neigh[1]:
                    neigh[0].distance_from_target = greedy_node.distance_from_target + neigh[1]
            self.build_heap_backward_queue()

graph =  Graph(source=a, target = e, queue=[a,b,c,d,e], backward_queue = [a,b,c,d,e])
graph.print_queue()
graph.dijkstra()