def gates(s):
    stack=[]
    temp=0
    for i in s:
        if i=='(':
            stack.append('(')
        elif i==')':
            if stack==[] or stack.pop()!='(':
                return -1 
            temp+=1
    if stack!=[] or temp==1:
        return -1
    return temp 
s=input('enter gate notation')
print(gates(s))