                                          #ADDITION OF TWO SPARSE MATRICES
#reading elements of matrix from user
def read(m,n):
    a=[]*m
    for ii in range(m):
        t=[]
        for jj in range(n):
            print('enter elements',ii,'row',jj,'column:')
            t.append(int(input()))
        a.append(t)
    return a
#function for displaying matrix
def display(a):
    for r in a:
        for e in r:
            print(e,end=' ')
        print()
#function for creating sparse matrix
def sparse(a):
    s=[]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]!=0:
                t=[]
                t.append(i)
                t.append(j)
                t.append(a[i][j])
                s.append(t)          
    return s
#function for addition
def add(a,b):
    sum=[]
    a1=len(a)
    b1=len(b)
    if a1==0:   sum=b
    if b1==0:   sum=a
    i=0
    j=0
    while a1>0 and b1>0:
        if a[i][0]==b[j][0] and a[i][1]==b[j][1]:
            sum.append([a[i][0],a[i][1],a[i][2]+a[j][2]])
            i+=1
            j+=1
        else:
            sum.append(min(a[i],b[j]))
            if min(a[i],b[j])==a[i]:
                i+=1
            else:
                j+=1
        if i>=a1:
            for k in range(j,b1):
                sum.append([b[k][0],b[k][1],b[k][2]])
            break
        if j>=b1:
            for k in range(i,a1):
                sum.append([a[k][0],a[k][1],a[k][2]])
            break
    return sum 
#reading matrix a
print("enter number of rows and columns of a:")
m=int(input())
n=int(input())                                         
a=read(m,n)
#reading matrix b
print("enter number of rows and columns of b:")
m=int(input())
n=int(input())                                         
b=read(m,n)
#displaying original matrix
print('original matrix a:')
display(a)
s1=sparse(a)
print('original matrix b:')
display(b)
s2=sparse(b)
#displaying sparse matrix
print('sparse matrix a:')
display(s1)
print('sparse matrix b:')
display(s2)
sum=add(s1,s2)
print('sparse matrix of sum :')
display(sum)