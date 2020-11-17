                                                                #PROGRAM FOR INSERTION SORT
#method for insertion sort
def insertion_sort(l,i):
    p=i 
    c=l[i]
    while c<l[p-1] and p>0:
        l[p]=l[p-1]
        p-=1
    l[p]=c
    if i+1<len(l):
        insertion_sort(l,i+1)   
#input from the user
l=list(map(int,input('enter the elements saperated by spaces : ').split()))
insertion_sort(l,0)
print(l)