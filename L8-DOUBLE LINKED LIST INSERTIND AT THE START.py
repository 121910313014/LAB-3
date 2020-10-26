                                                                    #adding nodes at the start 
#class for creating nodes
class Node:
    #function for initialising nodes
    def __init__(self,data):
        self.prev=None 
        self.data=data
        self.next=None
#class for operations on doubly linked list
class DoublyLinkedList:
    #function for initialising doubly liked list
    def __init__(self):
        self.head=None 
        self.tail=None 
    #function for adding nodes at the start
    def addNode(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
            self.tail=n 
            self.head.prev=None
            self.tail.next=None 
            return
        self.head.prev=n 
        n.next=self.head
        self.head=n
    #function for displaying elements in the list
    def display(self):
        c=self.head 
        while c:
            print(c.data)
            c=c.next
l=DoublyLinkedList()
l.addNode(10)
l.addNode(20)
l.addNode(30)
l.addNode(40)
l.addNode(50)
l.display()