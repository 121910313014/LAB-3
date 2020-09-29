#insertind an element in any desired position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
class LinkedList:
    def __init__(self):
        self.head=None
        self.next=None 
    def append(self,data):
        n=Node(data)
        if self.head is None:
            self.head=n
            return 
        c=self.head 
        while c.next:
            c=c.next 
        c.next=n  
    def insert(self,p,data):
        n=Node(data)
        c=self.head 
        while c:
            if c.data==p:
                n.next=c.next
                c.next=n
                return 
            c=c.next
        print("Do not exist")
    def display(self):
        c=self.head 
        while c:
            print(c.data)
            c=c.next 
l=LinkedList()
n=int(input("Enter number of elements :"))
#loop for taking inputs from the user
for i in range(n):
    data=int(input("Enter element : "))
    l.append(data)
#taking input from the user to insert
data=int(input("Enter element to be inserted : "))
p=int(input("Enter node of the previous position element at which element to be inserted :"))
l.insert(p,data)
l.display()