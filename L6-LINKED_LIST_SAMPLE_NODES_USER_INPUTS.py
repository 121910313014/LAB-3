                        #implementation of linked list by user inputs
#class for initialising nodes
class Node:
    def __init__(self,data):
        self.data=data  
        self.next=None
#class for implementing linked list
class LinkedList:
    #constructor 
    def __init__(self): 
        self.head=None
        self.tail=None
    #method for appending
    def append(self , data):
        n=Node(data)
        if self.head is None:
            self.head=n
            return 
        cur=self.head
        while cur.next:
            cur=cur.next 
        cur.next=n
    #method for displaying
    def display(self):
        cur=self.head 
        while cur:
            print(cur.data)
            cur=cur.next
l=LinkedList()
n=int(input("Enter number of elements :"))
#loop for taking inputs from the user
for i in range(n):
    data=int(input("Enter element : "))
    l.append(data)
l.display()