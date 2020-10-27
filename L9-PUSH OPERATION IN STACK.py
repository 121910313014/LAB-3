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
                raise Exception('element already exists') 
        else:
            raise Exception('Stack over flow')
n=int(input('Enter size : '))
s=Stack(n)
print('enter elements :')
for i in range(n):
    s.push(int(input()))
s.push(4)