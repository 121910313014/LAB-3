                                         #NUMBER OF NODES
#class for nodes 
class Node:
    #constructor for creating nodes
    def __init__(self,data):
        self.data=data
        self.next=None 
#class for LinkedList
class LinkedList:
    #constructor for initialising LinkedList
    def __init__(self):
        self.head=None 
    #method for appending nodes  
    def addNode(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
            return 
        c=self.head 
        while c.next:
            c=c.next 
        c.next=n
        return 
    #method for displaying list
    def display(self):
        c=self.head 
        while c:
            print(c.data)
            c=c.next
    #method for finding length of list
    def length(self):
        c=self.head
        k=0 
        while c:
            k+=1
            c=c.next 
        return k 
l=LinkedList()#creating instance of class LinkedList
l.addNode(1)
l.addNode(2)
l.addNode(3)
l.addNode(4)
l.addNode(5)
print('the elements are:')
l.display()
print('length of list is',l.length())#printing length of list