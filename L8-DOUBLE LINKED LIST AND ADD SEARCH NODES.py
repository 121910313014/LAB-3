                                                                # Program to search a node in a Doubly Linked List
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
    #function for searching nodes
    def searchNode(self,k):
        c=self.head
        while c:
            if c.data==k:
                return True 
            c=c.next
        return False
l=DLL()
n=int(input('Enter number of elements :'))
print('enter elements : ')
for i in range(n):
    l.addNode(int(input()))
k=int(input('enter the element you want to search :'))
s=l.searchNode(k)
if s==True:
    print('given value exists in the given linked list')
else:
    print('given value does not exist in the given linked list')