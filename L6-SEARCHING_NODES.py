                #Search for a given item in a linked list.
#class for creating a node
class Node:
    #method for adding data into the newly created node
    def __init__(self,data):
        self.data=data 
        self.next=None 
#class for creating a LinkedList and for performing operations
class LinkedList:
    #method for initialising LinkedList
    def __init__(self):
        self.head=None 
    #method for adding elements to the end of list
    def add_end(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n 
            return 
        c=self.head 
        while c.next:
            c=c.next
        c.next=n 
    #method for searching element
    def searching(self,k):
        c=self.head
        t=0 
        while c.next:
            if c.data==k:
                return t
            t+=1
            c=c.next 
        return -1
#loop for taking inputs from the user
l=LinkedList()
n=int(input('enter length of list : '))
for i in range(n):
    data=int(input('enter element: '))
    l.add_end(data)
#taking input from the user to search
k=int(input('enter element to be searched : '))
t=l.searching(k)
#printing the index of the searched element in the list
if t>=0:
    print('element present at :',t)
else:
    print('element not present')
