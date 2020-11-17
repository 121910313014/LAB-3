                                                                #PROGRAM FOR INSERTION SORT
#method for insertion sort
def insertion_sort(l):
    for i in range(1,len(l)):
        p=i 
        c=l[i]
        while c<l[p-1] and p>0:
            l[p]=l[p-1]
            p-=1
        l[p]=c  
    return l 
#input from the user
l=list(map(int,input('enter the elements saperated by spaces : ').split()))
l=insertion_sort(l)
print(l)