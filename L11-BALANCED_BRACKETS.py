s=input('enter the statement to check wheather the brackets are balanced : ')
l='({['
r=')}]'
stack=[]
temp=0
for i in s:
    if i in l:
        stack.append(i)
    elif i in r:
        if stack==[]:
            temp=1
            break
        elif l.index(stack.pop())!=r.index(i):
            temp=1
            break
if stack!=[] or temp==1 :
    print('The brackets are not balanced ')
else:
    print('The brackets are balanced ')