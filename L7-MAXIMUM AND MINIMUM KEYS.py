                                                    #PRINTING LARGEST AND SMALLEST
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
    #method for displaying list
    def display(self):
        c=self.head 
        while c:
            print(c.data)
            c=c.next 
    #method for displaying maximum and minimum keys in list
    def maxmin(self):
        c=self.head
        ma=c.data
        mi=c.data 
        while c:
            if ma<c.data:
                ma=c.data 
            if mi>c.data:
                mi=c.data
            c=c.next 
        print('maximum is',ma,'\nminimum is',mi)
n=int(input("Enter length of list:"))#taking length of list from the user
s=LinkedList()#creating instance of class LinkedList
for i in range(n):
    data=int(input("enter element:"))
    s.addElement(data)
print("Initial list:")
s.display()
print('reverse list is:')
s.maxmin()