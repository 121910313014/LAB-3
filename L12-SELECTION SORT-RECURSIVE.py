                                        #PROGRAM FOR SELECTION SORT
#method for selection sort
def selection_sort(l,i):
    min_val=min(l[i:])
    index=l.index(min_val,i)
    if l[i]!=min_val:
        l[index],l[i]=l[i],l[index]
    if  i+1<len(l):
        selection_sort(l,i+1)
#input from the user
l=list(map(int,input('enter the elements saperated by spaces : ').split()))
selection_sort(l,0)
print(l)