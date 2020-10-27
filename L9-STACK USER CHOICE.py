class Stack:
    def __init__(self):
        self.s=[]
    def push(self,data):
        self.s.append(data)
    def pop(self):
        return self.s.pop()
    def printStack(self):
        print(self.s)
s=Stack()
print('Select the operation of your choice:\n1. Push\n2. Pop\n3. Display\n4. Exit')
k=1
while k==1:
    n=int(input('enter your choice : '))
    if n==1:
        data=int(input('enter element you want to push in the stack : '))
        s.push(data)
    elif n==2:
        print('the element which is popped is : ')
        print(s.pop())
    elif n==3:
        print('the elements in the stack are : ')
        s.printStack()
    elif n==4:
        k=0
        print('you cant do anymore operations as you have exitted')
    else:
        print('enter valid choice')