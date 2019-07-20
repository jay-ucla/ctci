class LinkedList:
    class Node:
        next = None
        item = None
        def __init__(self, d):
            self.item = d
    
    root = None
            
    def __init__(self, *items):
        self.addAll(*items)
             
    def add(self, item):
        #No elements in LinkedList
        if self.root is None:
            self.root = LinkedList.Node(item)
            return
            
        next = self.root
        while next.next is not None:
            next = next.next
        
        next.next = LinkedList.Node(item)
    
    def addAll(self, *items):
        for i in range(len(items)):
            self.add(items[i])
        
    def remove(self, item):
        curr = self.root
        prev = None
        while curr.item is not item:
            prev = curr
            curr = prev.next
        
        #First node
        if prev is None:
            self.root = self.root.next
        else:    
            prev.next = curr.next
    
    def traverse(self):
        curr = self.root
        traversal = [curr.item]
        while curr.next is not None:
            curr = curr.next
            traversal.append(curr.item)    
            #print(traversal)
        print(traversal)
    
    def reverse(self):
        curr = self.root
        self.root = None
        while curr is not None:
            #Store next node
            temp = curr.next
            #Point current node to previous node (Reverse)
            curr.next = self.root
            #Store curr node as previous node(head of list)
            self.root = curr
            #Go to next node
            curr = temp
                        
def deleteDuplicateSet(ll):
    data_set = {}
    curr = ll.root
    prev = None
    while curr is not None:
        try:
            data_set[curr.item]
            prev.next = curr.next
        except KeyError:
            data_set[curr.item] = ''
            prev = curr
        finally:
            curr = curr.next
            
def checkPalindrome(ll):
    slow = ll.root
    fast = ll.root
    stack = []
    while fast is not None and fast.next is not None:
        stack.append(slow.item)
        fast = fast.next.next
        slow = slow.next
    print(stack)
    
    #odd list
    if fast is not None:
        slow = slow.next
    
    while slow is not None:
        if slow.item == stack.pop():
            slow = slow.next
        else:
            return False
    return True
        
def intersection(ll1, ll2):
    curr1 = ll1.root
    curr2 = ll2.root
    k=0
    while curr1 is not None or curr2 is not None:
        if curr1 is None or curr2 is None:
            k += 1
        


def testLinkedList():
    ll = LinkedList(1)
    ll.traverse()
    ll.remove(1)
    ll.add(2)
    ll.add(3)
    ll.traverse()
    ll.remove(2)
    ll.traverse()
    ll.add(4)
    ll.add(1)
    ll.traverse()
    ll.remove(1)
    ll.remove(4)
    ll.traverse()
    ll.addAll(1,2,3,4,5,6,4,3,2,5,6)
    ll.traverse()
    ll.reverse()
    ll.traverse()
    deleteDuplicateSet(ll)
    ll.traverse()
    ll2 = LinkedList(1)
    ll2.addAll(2,3,2,1)
    print(checkPalindrome(ll2))
    ll2 = LinkedList(1)
    ll2.addAll(2,2,1)
    print(checkPalindrome(ll2))
    ll2 = LinkedList(1)
    ll2.addAll(2,3,3,2,1)
    print(checkPalindrome(ll2))
    ll2 = LinkedList(1)
    ll2.addAll(2,3,3,4,1)
    print(checkPalindrome(ll2))
    ll2 = LinkedList(1)
    ll2.addAll(2,3,2,3)
    print(checkPalindrome(ll2))
    
testLinkedList()