                                                        #attaching an element at the starting of the list
#class for initialising new node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#class for LinkedList and for implementing operations on it
class LinkedList:
    #constructor to initialise tle list 
    def __init__(self):
        self.head=None
    #method for appending elements
    def append(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
            return 
        c=self.head
        while c.next :
          c=c.next
        c.next=n
    #method for attaching an element in the start of a list 
    def prepend(self,data):
        n=Node(data)
        c=self.head
        n.next=c
        self.head=n
    #method for displaying elements
    def display(self):
        c=self.head 
        while c:
            print(c.data)
            c=c.next
l=LinkedList()
n=int(input("enter number of elements :"))
#loop for appending elements
for i in range(n):
    data=int(input("enter element : "))
    l.append(data)
#calling function for prepending elements
data=int(input("enter element to be inserted at the begining : "))
l.prepend(data)
l.display()