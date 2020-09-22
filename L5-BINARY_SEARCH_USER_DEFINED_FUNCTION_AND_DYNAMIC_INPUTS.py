                                                        #BINARY SEARCH  USER DEFINED FUNCTION AND DYNAMIC INPUTS
#function for reading elements
def array(n):
    l=list()
    print("Enter elements of a sorted list : ")
    for i in range(n):  l.append(int(input()))
    return l
#function for binary search
def bsearch(l,low,high,a):
    if high>=low:
        mid=(high + low)//2
        if l[mid]==a:
            return mid
        elif l[mid]>a:
            return bsearch(l,low,mid-1,a)
        else:
            return bsearch(l,mid+1,high,a)
    else:
        return -1
#reading length of the list from the user and calling array() function to read elements 
n=int(input("Enter length of list : "))
l=array(n)
a=int(input("Enter element to be searched : "))
#calling bsearch function
i=bsearch(l,0,(len(l)-1),a)
if i!=-1:
    print(a,"is present at the index:",i)
else:
    print(a,"is not present in the given list ")