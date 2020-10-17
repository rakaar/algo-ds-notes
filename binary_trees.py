# wrong things done here - not using setter and getter functions and manipulating objects directly 

class Node:
    def __init__(self, value, parent=None, leftNode=None, rightNode=None, n=1):
        self.value = value
        self.parent = parent
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.n = n # number of nodes below the node including itself


    def find_node(self, value):
        # if u find what u were looking for
        if self.value == value:
            return self
        
        # if value is smaller, look at left side of the tree recursively
        if value < self.value:
            if self.leftNode != None:
                return self.leftNode.find_node(value)
            else:
                return None
        # if value is larger, look at right side recursively
        elif value > self.value:
            if self.rightNode != None:
                return self.rightNode.find_node(value)
            else:
                return None

    def find_max_in_sub_tree(self):
        if self.rightNode == None:
            return self
        
        if self.rightNode != None:
            return self.rightNode.find_max_in_sub_tree()

    def find_min_in_sub_tree(self):
        if self.leftNode == None:
            return self
        
        if self.leftNode != None:
            return self.leftNode.find_min_in_sub_tree()
    
    def delete(self):
        # cases where the node is a leaf, just remove it
        if self.leftNode == None and self.rightNode == None:
            if self.parent.value > self.value:
                self.parent.rightNode = None
            else:
                self.parent.leftNode = None
            # remove parent's Link
            self.parent = None
            return

        # cases where children are only in one direction, just change the pointers
        # where children only in left direction
        if self.rightNode == None:
            self.parent.leftNode = self.leftNode
            self.leftNode.parent = self.parent

            self.parent = None
            self.leftNode = None
            return
        # where children only in rightdirection
        elif self.leftNode == None:
            self.parent.rightNode = self.rightNode
            self.rightNode.parent = self.parent

            self.parent = None
            self.leftNode = None
            return

        
        # cases where there are children in both the directions
        # swap values between currentNode and its succesorNode
        # delete the successor_node(which contains the value to be removed from tree), note that the successor_node is a leaf
        successor_node = self.rightNode.find_min_in_sub_tree()
        successor_node.value, self.value = self.value, successor_node.value
        successor_node.delete()
        


class BST:
    def __init__(self, root=None):
        self.root = root

    def increase_parents_n(self, node):
        parent = node.parent
        while parent != None:
            parent.n += 1
            parent = parent.parent
        return    
        
    def insertNode(self, node, value):
        if value < node.value:
            if node.leftNode is None:
                node.n += 1
                node.leftNode = Node(value=value, parent=node)
                # add 1 to parents n value
                self.increase_parents_n(node)
                return True
            else:
                self.insertNode(node.leftNode, value)
        elif value > node.value:
            if node.rightNode is None:
                node.n += 1
                node.rightNode = Node(value=value, parent=node)
                # add 1 to parents n value
                self.increase_parents_n(node)
                return True
            else:
                self.insertNode(node.rightNode, value)
    
    
    # def check_nodes_for_
    def k_min_check(self, value, k):
        current = self.root
        # i want to end when i reach the leaf
        while current != None:
            if abs(current.value - value) > 3:
                if value <= current.value:
                    current = current.leftNode
                elif value > current.value:
                    current = current.rightNode
            else:
                return False
        
        self.insert(value)
        return True
    
    def num_of_nodes_less_than_val(self,val):
        counter = 0
        node = self.root
        # i want to end when i reach the leaf or when i encounter a number bigger than that
        while node != None and node.value <= val:
            # add itself
            counter += 1
            # add the left nodes, if they exist
            if node.leftNode != None:
                counter += node.leftNode.n 
            node = node.rightNode
        return counter

    def find_node(self, value):
        return self.root.find_node(value)    
    
    def next_bigger(self,value):
        node = self.find_node(value)
        # if no such node return None
        if node == None:
            return None
        
        # a general case, where we have a rightNode
        if node.rightNode != None:
            return node.rightNode.find_min_in_sub_tree()
        
        # an odd case where there are no rightNode and it is like an array
        # All parents are smaller than give node
        #     10 
        #    /
        #   9
        #  /
        # (8)
        if node.parent.value > value:
            return node.parent
        
        # An odd case, where all parents are not bigger than given node
        # u see till u divert right side, that is get a bigger number than ur node's value
        #      100
        #      /
        #     99
        #     /
        #   5
        #   \
        #    (6)
        if node.parent.value < value:
            parent = node.parent
            while parent.value < value:
                parent = parent.parent
                if parent == None: # to avoid error of "value of none type at 2 lines above" due to root node
                    break
            return parent
        
    def print_all_in_order(self):
        temp_root = self.root
        while temp_root.leftNode != None:
            temp_root = temp_root.leftNode
        print(temp_root.value)
        # the below code seems to have runtime n*log(n)
        # n -> nodes and each time next successor -> log(n), (reason- worst case is reaching the leaves from node)

        # but on doing amortized ananlysis
        # instead of assuming worst case everytime, which is not practical
        # we can look at the actual process
        # in this case, it happens so that each edge in the tree is traversed twice
        # if there are n nodes, there are n-1 edges
        # 2(n-1) -> O(n) is the run time when analyzed properly
        while temp_root != None and self.next_bigger(temp_root.value) != None:
            print(self.next_bigger(temp_root.value).value)
            if self.next_bigger(temp_root.value)!= None:
                temp_root = self.next_bigger(temp_root.value)
            else:
                break
            
    
    
    def find_max(self):
        return self.root.find_max_in_sub_tree()

    def find_min(self):
        return self.root.find_min_in_sub_tree()
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value=value)
            return
        self.insertNode(self.root, value) 

    def delete(self, value):
        node = self.find_node(value)
        if node == None:
            return None
        return node.delete()                
        
tree = BST()
tree.insert(49)   
tree.insert(46)   
tree.insert(43)   
tree.insert(79)
tree.insert(64)
tree.insert(83)

tree.print_all_in_order()
# tree.delete(79)
# print(tree.find_node(83).leftNode.value) # 64


# print(tree.find_node(604)) # None
# print(tree.find_node(64).value) # 64

# print(tree.find_max().value)
# print(tree.find_min().value)

# tree.insert(10)
# tree.insert(9)
# tree.insert(8)
# print(tree.next_bigger(8).value)

# tree.insert(100)
# tree.insert(99)
# tree.insert(5)
# tree.insert(6)
# print(tree.next_bigger(6).value)


# print(tree.num_of_nodes_less_than_val(79))
# print(tree.num_of_nodes_less_than_val(100))
# print(tree.num_of_nodes_less_than_val(50))


# print(tree.k_min_check(38,3))
# print(tree.k_min_check(42,3)) # |42 - 43| <= 3
# print(tree.k_min_check(80,3)) # |79 - 80| <= 3
# print(tree.k_min_check(90,3))
# print(tree.k_min_check(1,3))

