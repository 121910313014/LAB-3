class Stack:
    def __init__(self,size):
        self.s=[]
        self.n=size
        self.i=0
    def push(self,data):
        if self.n>0 :
            if data not in self.s:
                self.n-=1
                self.s.append(data)
            else:
                print('element already exists') 
        else:
            print('Stack over flow')
    def isEmpty(self):
        return len(self.s)==0
    def pop(self):
        if self.isEmpty():
            raise Exception('stack under flow')
        return self.s.pop()
    def peek(self):
        return self.s[-1]
    def size(self):
        return len(self.s)
    def specific(self , data):
        if data in self.s:
            self.s.remove(data)
            return 
        else:
            print('element is not present in the stack')
    def printStack(self):
        print(self.s)
n=int(input('Enter size : '))
s=Stack(n)
print('enter elements :')
for i in range(n):
    s.push(int(input()))
p=int(input('enter element you want to pop : '))
print('stack before popping: ')
s.printStack()
s.specific(p)
print('stack after popping: ')
s.printStack()