                                                                    #program for finding maximum and minimum keys
#class for creating nodes
class Node:
    #function for initialising nodes
    def __init__(self,data):
        self.prev=None 
        self.data=data 
        self.next=None 
#class for operations on doubly linked list
class DLL:
    #function for initialising doubly liked list
    def __init__(self):
        self.head=None 
        self.tail=None 
    #function for adding nodes 
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
    #function for finding maximum and minimum keys
    def maxmin(self):
        c=self.head 
        ma=self.head.data 
        mi=self.head.data 
        while c:
            if c.data>ma:
                ma=c.data 
            elif c.data<mi:
                mi=c.data 
            c=c.next 
        return [ma,mi]
l=DLL()
n=int(input('Enter number of elements :'))
for i in range(n):
    l.addNode(int(input()))
[maxi,mini]=l.maxmin()
print('maximum value is',maxi,'and minimum value is',mini)
