# Try adding a tail pointer in addition to the front. You'll need to modify
# the operations which modify the list (insert and pop), when the change happens
# to the last element.
# Note that a tail pointer makes inserting at the end of a list much easier, but
# it doesn't help with removing from the end of a list.

# You can also try to implement any of the other list methods (just do help.lst
# in the shell to see all the existing Python list methods)

class LinkedList(object):
    '''A linked list implementation of a list'''
    
    class Node(object):
        '''A node of a singly linked list.'''
        
        def __init__(self, k):
            '''(Node) -> NoneType
            A new Node with key k and no next.'''
            
            self.key = k
            self.next = None
    
    def __init__(self):
        '''(LinkedList) -> NoneType
        A new empty LinkedList.'''
        
        self.front = None
        self.num_elements = 0
    
    def index(self, o):
        '''(LinkedList, object) -> int
        Return first index of object o. Raise ValueError if the value is not
        present.'''
        
        i = 0
        node = self.front
        while node and node.key != o:
            node = node.next
            i += 1
        if node:
            return i
        else:
            raise ValueError("%s is not in list" % str(o))
        
    def insert(self, i, o):
        '''(LinkedList, int, object) -> NoneType
        Insert object o before index i. Raise IndexError if i is out of 
        range.'''
        
        if i < 0 or i > self.num_elements:
            raise IndexError("insert index out of range")
            # To make this method like the insert method for Python lists, 
            # replace the above line with:
            # i = self.num_elements
        new_node = LinkedList.Node(o)
        if i == 0:
            new_node.next = self.front
            self.front = new_node
        else:
            node = self.front
            for j in range(i - 1):
                node = node.next
            new_node.next = node.next
            node.next = new_node
        self.num_elements += 1
        
    def append(self, o):
        '''(LinkedList, object) -> NoneType
        Append object o to end of list.'''
        
        self.insert(self.num_elements, o)
        
    def pop(self, i):
        '''(LinkedList, int) -> NoneType
        Remove and return item at index. Raise IndexError if list is empty or
        index is out of range.'''
        
        if i < 0 or i >= self.num_elements:
            raise IndexError("pop index out of range")
        if i == 0:
            result = self.front.key
            self.front = self.front.next
        else:
            node = self.front
            for j in range(i - 1):
                node = node.next
            result = node.next.key
            node.next = node.next.next
        self.num_elements -= 1
        return result
    
    def __len__(self):
        '''(LinkedList) -> int
        Return the length of this LinkedList.'''
        
        return self.num_elements
    
    def __str__(self):
        '''(LinkedList) -> str
        Return a string representation of this LinkedList.'''
        
        result = "["
        node = self.front
        if node != None:
            result += str(node.key)
            node = node.next
            for i in range(self.num_elements - 1):
                result += ", " + str(node.key)
                node = node.next
        result += "]"
        return result

if __name__ == "__main__":
    L = LinkedList()
    assert len(L) == 0
    assert str(L) == '[]'
    L.append(10)
    assert len(L) == 1
    assert str(L) == '[10]'
    L.insert(0, 20)
    assert len(L) == 2
    assert str(L) == '[20, 10]'
    assert L.index(10) == 1
    assert L.pop(0) == 20
    assert len(L) == 1
    assert str(L) == '[10]'
    assert L.pop(0) == 10
    assert len(L) == 0
    assert str(L) == '[]'
