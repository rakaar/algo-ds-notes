# instead of doing like this 
# it is easier to represnt heap in array format
# reason - at each level it is possible to tell the number of nodes, hence due to that we can 
# hence using each index of array we can tell where it is in the tree and who are its parents and children
# for a heap with root index = 0, 
#   if index of node is i
#       left child is 2*i + 1 (provided this number doesn't exceed len(arr)-1)
#       right child is 2*i + 2 (provided this number doesn't exceed len(arr)-1)
#       parent of the node is (n-1)//2


## why a heap, why not just a sorted list?
# first of all lists are not sorted, while max-heaps and min-heaps are !
# and when u add a new element, u have to sort the list everytime?
# even if u think u can add by binary search, what about the cost of shifting array completely,
# i meant- [1,2,3] if u want to add 0 and make it [0,1,2,3] then u have to move 1,2,3 right ?
# hence we use a heap for that, for a heap, adding a new element wil be order logn (with lesser swaps and less search)!
# bcoz all u do is add a element at the bottom most, and max_heapify its parent
# hence heaps are useful in arrays when in real time events are added and u need to keep them sorted
# the above line nothing but tells about priority queue

class HeapNode:
    def __init__(self, leftNode, rightNode, value,key):
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.value = value
        self.key = key

    def heapify(self):
        # its already heapified if it satisfies the condition
        if self.value >= self.leftNode.value and self.value >= self.rightNode.value:
            return
        
        # if left one or right one is larger
        if self.leftNode.value > self.rightNode.value:
            self.leftNode.value, self.value = self.value, self.leftNode.value  

        elif self.rightNode.value > self.rightNode.value:
            self.rightNode.value, self.value = self.value, self.rightNode.value

    
    
leafNode1 = HeapNode(leftNode=None, rightNode=None, value=4, key=2)
leafNode2 = HeapNode(leftNode=None, rightNode=None, value=1, key=3)

root = HeapNode(leftNode=leafNode1, rightNode=leafNode2, value=2, key=1)

#    2  
#   /\
#  4  1
print('root node value is', root.value)
print('value of left child of root ',root.leftNode.value)
print('value of right child of root ',root.rightNode.value)

root.heapify()

#    4  
#   /\
#  2  1
print('root node value is', root.value)
print('value of left child of root ',root.leftNode.value)
print('value of right child of root ',root.rightNode.value)

