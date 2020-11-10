def pivot_position(l,first,last):
    pivot=l[first]
    left=first+1
    right=last
    while True:
        while left<=right and l[left]<=pivot:
            left+=1
        while left<=right and l[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            l[left],l[right]=l[right],l[left]
    l[right],l[first]=l[first],l[right]
    return right 
def quick_sort(l,first,last):
    if first<last:
        p=pivot_position(l,first,last)
        quick_sort(l,first,p-1)
        quick_sort(l,p+1,last)
n=int(input('enter length of list : '))
print('Enter elements : ')
l=list()
for i in range(n):
    l.append(int(input()))
quick_sort(l,0,n-1)
print('The second smallest element in the given list is :',l[1])