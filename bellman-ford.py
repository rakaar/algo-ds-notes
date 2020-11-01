# bellman ford tackles the issue of negative cycles
# dijkstra expects the weights to be postive only
# but for weights with -ve value and non cycle nature
# a topological sort and one pass over the vertices will do it

class Node:
    def __init__(self, name, cost_to_source):
        self.name = name
        self.cost_to_source = cost_to_source

class Edge:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
# example from https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec17.pdf
class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def print_result_of_bellman_ford(self):
        for n in self.nodes:
            print('node ', n.name, 'cost ', n.cost_to_source)

    def bellman_ford(self):
        # the first part of bellman ford algo of relaxing each all edges v - 1 times
        for i in range(len(self.nodes)-1):
            print('---iteration',i+1,'---')
            for e in self.edges:
                if e.to_node.cost_to_source > e.from_node.cost_to_source + e.weight:
                    print('relaxed',e.to_node.name)
                    e.to_node.cost_to_source = e.from_node.cost_to_source + e.weight
        
        self.print_result_of_bellman_ford()
        
        # the second part to detect negative cycles
        # after V -1 passes the shortest paths should have been found out
        # even after V - 1 passes the path can be optimised then a negative cycle exists
        for e in self.edges:
                if e.to_node.cost_to_source > e.from_node.cost_to_source + e.weight:
                    print('Negative cycle detected')
        # foolish point - here only negative cycle is printed once not many times like above case bcoz
        # in the above case after it is found that it can be still relaxed, the value is changed
        # and hence subsequent values also change/relaxed, but here since we don't relax, its printed only once
                    
# source is 'a'
a = Node(name='a', cost_to_source=0)
b = Node(name='b', cost_to_source=9999)
c = Node(name='c', cost_to_source=9999)
d = Node(name='d', cost_to_source=9999)
e = Node(name='e', cost_to_source=9999)

edges = [
    Edge(from_node=a, to_node=b, weight=1),
    Edge(from_node=b, to_node=c, weight=2),
    Edge(from_node=c, to_node=d, weight=-4),
    Edge(from_node=d, to_node=b, weight=1),
    Edge(from_node=c, to_node=e, weight=1)
]

g = Graph(nodes=[a,b,c,d,e], edges=edges)

g.bellman_ford()
