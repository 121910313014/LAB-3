#linked list sample nodes as static inputs
#Node class
class Node :
    #Function to initialize the node object
    def __init__(self,data):
        self.data=data #giving a value for the space provided to the value
        self.next=None #initialising the pointer position to None
#class for linked list
class LinkedList:
    #method to initialise the head of linked list
    def __init__(self):
        self.head=None  #initialising to None
    #method for printing list
    def printList(self):
        temp=self.head #initialising temp value as the head position value
        while(temp):
            print(temp.data) #printing temp value
            temp=temp.next #changing temp value to the next value
list1=LinkedList()
list1.head=Node(1)
second=Node(2)
third=Node(3)
list1.head.next=second 
second.next=third
list1.printList() 
