                                                #adding nodes at the end 
#class for nodes
class Node:
    #constructor for initialising list
    def __init__(self,data):
        self.data=data 
        self.prev=None 
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
        if self.head==None:
            self.head=self.tail=n 
            self.head.prev=None 
            self.tail.next=None 
            return 
        self.tail.next=n
        n.prev=self.tail
        self.tail=n
        self.tail.next=None
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
l.display()