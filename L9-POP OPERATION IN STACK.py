class Stack:
    def __init__(self,size):
        self.s=[]
        self.n=size
        self.i=0
    def push(self,data):
        if self.i<self.n :
            if data not in self.s:
                self.i+=1
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
n=int(input('Enter size : '))
s=Stack(n)
print('enter elements :')
for i in range(n):
    s.push(int(input()))
p=int(input('enter number of elements you want to pop : '))
for i in range(p):
    print(s.pop())