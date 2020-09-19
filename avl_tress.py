def return_height(node):
    if node == None:
        return -1
    return node.height

class Node:
    def __init__(self, value, parent=None, leftNode=None, rightNode=None, height=0, leftNodeHeight=-1, rightNodeHeight=-1):
        self.value = value
        self.parent = parent
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.height = height
        self.leftNodeHeight = leftNodeHeight
        self.rightNodeHeight = rightNodeHeight

    def balance_check(self):
        height_diff = abs(self.leftNodeHeight - self.rightNodeHeight)
        if height_diff <= 1:
            if self.parent != None:
                return self.parent.balance_check()
            else:
                return
        else:
            self.balancify()   

    def left_rotate(self):
        print('left rotate ', self.value)
        old_parent = self.parent
        old_right = self.rightNode
        old_right_left = self.rightNode.leftNode
        if old_parent != None:
            if old_parent.rightNode == self:
                old_parent.rightNode = old_right
            else:
                old_parent.leftNode = old_right
        
        old_right.parent = old_parent
        old_right.leftNode = self

        self.parent = old_right
        self.rightNode = old_right_left
        if old_right_left != None:
            old_right_left.parent = self
        self.calculate_heights()
        return

    def right_rotate(self):
        print('right rotate ', self.value)
        old_parent = self.parent
        old_left = self.leftNode
        old_left_right = self.leftNode.rightNode
        if old_parent != None:
            if old_parent.rightNode == self:
                old_parent.rightNode = old_left
            else:
                old_parent.leftNode = old_left
        
        old_left.parent = old_parent
        old_left.rightNode = self
        
        self.parent = old_left
        self.leftNode = old_left_right
        if old_left_right != None:
            old_left_right.parent = self
        self.calculate_heights()    
        return
    
    def balancify(self):
        # find the condition and based on condition do left or right rotate
        # case 1
        #   case1.1             case 1.2
        #      6                  5
        #     /                    \
        #   5                       6
        #  /                         \
        # 4                           7  
        #     ^                      ^
        #     |                      |
        # case 2
        #     case 2.1               case 2.2
        #    6                        6 
        #   /                          \
        #  4                            9
        #  \                           /
        #   5                          8
        
        print('unbalanced is',self.value)
        if self.leftNodeHeight == 1 and self.rightNodeHeight == -1:
            if self.leftNode.leftNodeHeight == 0 and self.leftNode.rightNodeHeight == -1: # case 1.1
                self.right_rotate()
            else: # case 2.1
                self.leftNode.left_rotate() # convert to case 1.1 and balancify
                self.balancify()
        elif self.leftNodeHeight == -1 and self.rightNodeHeight == 1:
            if self.rightNode.leftNodeHeight == -1 and self.rightNode.rightNodeHeight == 0: # case 1.2
                self.left_rotate()
            else: # case 2.2
                self.rightNode.right_rotate() # convert to case 1.2 and balancify
                self.balancify()
                

    def calculate_heights(self):
        # this -1 is a good way of making height as a single formula rather than making special cases and assigning height in each conditional case
        leftNodeHeight = return_height(self.leftNode)
        rightNodeHeight = return_height(self.rightNode)
        self.leftNodeHeight = leftNodeHeight
        self.rightNodeHeight = rightNodeHeight
        self.height = max(leftNodeHeight, rightNodeHeight) + 1
        # base condition of recursion, if its a root node(parent is None)
        if self.parent == None:
            return
        self.parent.calculate_heights()
            
            
    def insert(self,value):
        if value < self.value:
            if self.leftNode == None:
                self.leftNode = Node(value=value, parent=self)
                self.leftNode.calculate_heights() # adjust heights
                self.leftNode.balance_check()
            else:
                self.leftNode.insert(value)
        elif value > self.value:
            if self.rightNode == None:
                self.rightNode = Node(value=value, parent=self)
                self.rightNode.calculate_heights() # adjust heights
                self.rightNode.balance_check()
            else:
                self.rightNode.insert(value)
    
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


class AVLT:
    def __init__(self, root=None):
        self.root = root
    
    def find_node(self, value):
        return self.root.find_node(value)
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value=value)
            return
        self.root.insert(value)

tree = AVLT()
tree.insert(41)
tree.insert(20)
tree.insert(65)
tree.insert(50)
tree.insert(11)
tree.insert(29)
tree.insert(26)
# till now the tree is balanced, meaning absolute difference of children's heights is atmost 1
# abs(leftNode.height - rightNode.height) <= 1

# making it unbalanced
tree.insert(23)
tree.insert(55)

print(tree.find_node(55).rightNode.value)




