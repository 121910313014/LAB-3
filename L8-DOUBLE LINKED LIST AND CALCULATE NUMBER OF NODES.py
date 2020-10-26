                                                                # Program to count number of nodes in a Doubly Linked List
#class for nodes
class Node:
    #constructor for initialising list
    def __init__(self,data):
        self.prev=None 
        self.data=data 
        self.next=None 
#class for doubly linked list
class DLL:
    #constructor for initialising doubly linked list
    def __init__(self):
        self.head=None 
        self.tail=None 
    #function for appending nodes
    def  addNode(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n 
            self.tail=n 
            return 
        self.tail.next=n 
        n.prev=self.tail 
        self.tail=n 
        return 
    #function for counting nodes
    def countNodes(self):
        co=0
        c=self.head 
        while c:
            co+=1
            c=c.next 
        return co 
l=DLL()
l.addNode(1)
l.addNode(2)
l.addNode(3)
l.addNode(1)
print(l.countNodes())