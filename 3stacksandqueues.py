class Stack:
    _list = None
    _min = None
    def __init__(self, *items):
        self._list = []
        
    def push(self, item):
        self._list.append(item)
        
    def pop(self):
        if len(self._list) == 0:
            return None
        return self._list.pop()
    
    def min(self):
        return self._min

    def empty(self):
        res = True if len(self._list) == 0 else False
        return res

class Queue:
    _list = None
    def __init__(self, *items):
        self._list = []
        
    def add(self, item):
        self._list.append(item)
        
    def remove(self):
        if len(self._list) == 0:
            return None
        item = self._list[0]
        self._list = self._list[1:]
        return item
                

def testStacksQueues():
    s = Stack()
    assert(s.pop() == None)
    s.push(1)
    assert(s.pop() == 1)
    assert(s.pop() == None)
    s.push(2)
    s.push(3)
    assert(s.pop() == 3)
    assert(s.pop() == 2)
    assert(s.pop() == None)
    
    q = Queue()
    assert(q.remove() == None)
    q.add(1)
    assert(q.remove() == 1)
    q.add(2)
    q.add(3)
    assert(q.remove() == 2)
    assert(q.remove() == 3)
    assert(q.remove() == None)
    
    
    
testStacksQueues()