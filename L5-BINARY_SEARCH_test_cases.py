                                                        #BINARY SEARCH WITH DYNAMIC INPUTS AND USER DEFINED FUNCTIONS
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
#test cases
def tcase(l,a):
    if l!=sorted(l):
        print("the given list is not sorted")
        return
    b=bsearch(l,0,len(l)-1,a)
    if b==-1:
        print('element not present')
        return
    else:   
        print('element is present at',b)
        return 
    
#reading length of the list from the user and calling array() function to read elements 
l=[10,11,20,45,63,74,97,143]
#test case-1
print('test case-1 :')
a=74
tcase(l,a)
#test case-2
print('test case-2 :')
l=[10,11,20,45,63,74,143,97]
a=97
tcase(l,a)
#test case-3
print('test case-3 :')
l=[10,11,20,45,63,74,97,143]
a=94
tcase(l,a)