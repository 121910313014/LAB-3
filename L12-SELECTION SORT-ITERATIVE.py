                                        #PROGRAM FOR SELECTION SORT
#method for selection sort
def selection_sort(l):
    for i in range(len(l)-1):
        min_val=min(l[i:])
        index=l.index(min_val,i)
        if l[i]!=min_val:
            l[index],l[i]=l[i],l[index]
    return l 
#input from the user
l=list(map(int,input('enter the elements saperated by spaces : ').split()))
l=selection_sort(l)
print(l)