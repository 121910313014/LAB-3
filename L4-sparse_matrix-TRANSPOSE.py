                                          #TRANSPOSE OF SPARSE MATRIX
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
#function for transpose
def transpose(a):
    for i in range(len(a)):
        temp=a[i][0]
        a[i][0]=a[i][1]
        a[i][1]=temp
    a.sort()
    return a
#reading matrix a
print("enter number of rows and columns of a:")
m=int(input())
n=int(input())                                         
a=read(m,n)
#displaying original matrix
print('original matrix a:')
display(a)
s=sparse(a)
#displaying sparse matrix
print('sparse matrix a:')
display(s)
#displaying transpose sparse matrix
print('transpose sparse matrix a:')
display(transpose(s))