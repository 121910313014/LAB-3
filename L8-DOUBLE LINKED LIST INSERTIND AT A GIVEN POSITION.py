                                                #adding nodes after a given node
#class for nodes
class Node:
    #constructor for initialising list
    def __init__(self,data):
        self.prev=None 
        self.data=data
        self.next=None 
#class for doubly linked list
class DoublyLinkedList:
    #constructor for initialising doubly linked list
    def __init__(self):
        self.head=None 
        self.tail=None 
    #function for appending nodes
    def addNode(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n 
            self.tail=n 
            self.head.prev=None 
            self.tail.next=None
            return
        self.tail.next=n 
        n.prev=self.tail 
        self.tail=n 
    #function for adding node after a given node nodes
    def addNodeAfter(self,key,data):
        n=Node(data)
        c=self.head
        while c.next:
            if c.data==key:
                nxt=c.next 
                c.next=n 
                n.prev=c 
                n.next=nxt 
                nxt.prev=n 
                return
            c=c.next 
        if c.data==key:
            l.addNode(data)
            return  
    #function for displaying nodes
    def display(self):
        c=self.head 
        while c:
            print(c.data)
            c=c.next
        return
l=DoublyLinkedList()
l.addNode(1)
l.addNode(2)
l.addNode(3)
l.addNode(4)
l.addNodeAfter(4,10)
l.display()