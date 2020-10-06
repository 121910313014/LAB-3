                                                            #DELETING FIRST NODE
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
    def addElement(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
            return
        c=self.head  
        while c.next:
            c=c.next
        c.next=n
        return 
    #method for deleting nodes
    def delElement(self):
        c=self.head 
        if c is not None:#checking whether the list is empty or not and deleting key  present at the begining 
            self.head=c.next
            return  
    #method for displaying list
    def display(self):
        c=self.head 
        while c:
            print(c.data)
            c=c.next 
n=int(input("Enter length of list:")) #taking length of list from the user
s=LinkedList() #creating instance of class LinkedList
for i in range(n):
    data=int(input("enter element:"))
    s.addElement(data)
print("Initial list:")
s.display() 
s.delElement() #calling method for deleting first key
print("after deleting first key:")
s.display()