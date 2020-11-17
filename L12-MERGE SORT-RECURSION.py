                                                                        #PROGRAM FOR MERGE SORT
#method for merge sort
def merge_sort(l):
    if len(l)>1:
        mid=len(l)//2
        llist=l[:mid]
        rlist=l[mid:]
        merge_sort(llist)
        merge_sort(rlist)
        i=0
        j=0
        k=0
        while i<len(llist) and j<len(rlist):
            if llist[i]<rlist[j]:
                l[k]=llist[i]
                i+=1
                k+=1
            else:
                l[k]=rlist[j]
                j+=1
                k+=1
        while i<len(llist):
            l[k]=llist[i]
            i+=1
            k+=1
        while j<len(rlist):
            l[k]=rlist[j]
            j+=1
            k+=1
#input from the user
l=list(map(int,input('enter the elements saperated by spaces : ').split()))
merge_sort(l)
print(l)