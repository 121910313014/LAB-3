                                                                # Program to delete a node at different postitions of a Doubly Linked List
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
    def addNode(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n 
            self.tail=n 
            return 
        self.tail.next=n 
        n.prev=self.tail 
        self.tail=n 
        return 
    #function for deleting nodes
    def removeNode(self,k):
        if self.head==self.tail:
            self.head=None 
            self.tail=None
            return 
        if self.head.data==k:
            self.head=self.head.next
            self.head.prev=None 
            return 
        if self.tail.data==k:
            self.tail=self.tail.prev 
            self.tail.next=None 
        c=self.head 
        while c:
            if c.data==k:
                p=c.prev 
                nxt=c.next 
                p.next=nxt 
                nxt.prev=p
                c.next=None 
                c.next=None 
                return 
            c=c.next 
    #function for displaying nodes
    def display(self):
        c=self.head 
        while c:
            print(c.data)
            c=c.next
l=DLL()
n=int(input('Enter number of elements :'))
for i in range(n):
    l.addNode(int(input()))
k=int(input('enter the element you want to delete :'))
print('before deletion : ')
l.display()
l.removeNode(k)
print('after deletion : ')
l.display()