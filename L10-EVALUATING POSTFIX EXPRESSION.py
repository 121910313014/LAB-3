class Stack:
    def __init__(self):
        self.s=[]
    def push(self,data):
        self.s.append(data)
    def pop(self):
        return self.s.pop()
def postfix_eval(q):
    s=Stack()
    for i in q:
        if i in '+-*/':
            a=s.pop()
            b=s.pop()
            if i=='+':
                s.push(a+b)
            elif i=='-':
                s.push(a-b)
            elif i=='*':
                s.push(a*b)
            elif i=='/':
                s.push(a/b)
            elif i=='//':
                s.push(a//b)
        elif i in '0123456789':
            s.push(int(i))
    return s.pop()
q=list(input('Enter postfix expression with space :').split())
r=postfix_eval(q)
print(r)