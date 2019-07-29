SQ = __import__("3stacksandqueues")

class Node:
    name = None
    left = None
    right = None
    
    def __init__(self, val):
        self.name = val
    
    def visit(self):
        print(self.name)
    
class BinarySearchTree:
    root = None
    
    def __init__(self, val):
        self.root = Node(val)
        
    def insert(self, val):
        if self.root is None:
            return
        curr = self.root
        while curr is not None:
            if val <= curr.name :
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    break
            elif val > curr.name:
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    break
    
    #def remove(val):
    
def preOrder(node):
    if node is None:
        return
    node.visit()
    preOrder(node.left)
    preOrder(node.right)
    
def postOrder(node):
    if node is None:
        return
    postOrder(node.left)
    postOrder(node.right)
    node.visit()
    
def inOrder(node):
    if node is None:
        return
    inOrder(node.left)
    node.visit()
    inOrder(node.right)

    
def preOrderStack(node):
    if node is None:
        return
    st = SQ.Stack()
    while node is not None:
        node.visit()
        if node.right is not None: st.push(node.right)
        if node.left is not None: 
            node = node.left
        else:
            node = st.pop() 

                   
def inOrderStack(node):
    if node is None:
        return
    st = SQ.Stack()
    while True:
        if node is not None:
            st.push(node)
            node = node.left
        elif st.empty() == False:
            node = st.pop()
            node.visit()
            node = node.right
        else:
            break 

def postOrderStack(node):
    if node is None:
        return
    st1 = SQ.Stack()
    st2 = SQ.Stack()
    
    while node is not None:
        st2.push(node)
        if node.left is not None: st1.push(node.left)
        if node.right is not None: st1.push(node.right)
        node = st1.pop()
        
    node = st2.pop()
    while node is not None:
        node.visit()
        node = st2.pop()
        
def main():    
    b = BinarySearchTree(8)
    b.insert(6)
    b.insert(5)
    b.insert(2)
    b.insert(7)
    b.insert(10)
    b.insert(9)
    b.insert(20)
    #preOrder(b.root)
    #inOrderStack(b.root)
    postOrderStack(b.root)
    print()
    
main()
    