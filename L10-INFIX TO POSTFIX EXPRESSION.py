class Stack:
    def __init__(self):
        self.s=[]
    def push(self,data):
        self.s.append(data)
    def pop(self):
        return self.s.pop()
    def is_empty(self):
        return self.s==[]
    def peek(self):
        return self.s[-1]
def get_precedence(a):
    r=0
    for i in '+-*/':
        r+=1
        if i==a:
            if i in '-/':
                r-=1
            return r 
def infix_to_postfix(q):
    p=''
    t=Stack()
    for i in q:
        if i not in '+-/*()':
            p+=i
        elif i in '+-*/':
            while True:
                k=t.peek()
                if t.is_empty() or k=='(':
                    t.push(i)
                    break 
                else:
                    a=get_precedence(i)
                    b=get_precedence(k)
                    if a>b:
                        t.push(i)
                        break
                    else:
                        p+=i 
        elif i=='(':
            t.push(i)
        elif i==')':
            c=t.pop()
            while c!='(':
                p+=c 
                c=t.pop()
    return p
q=input('Enter infix expression :')
r=infix_to_postfix(q)
print(r)