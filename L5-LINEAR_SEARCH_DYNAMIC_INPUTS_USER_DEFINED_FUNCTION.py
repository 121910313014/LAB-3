                                                        #LINEAR SEARCH WITH DYNAMIC INPUTS AND USER DEFINED FUNCTIONS
#function for reading elements
def array(n):
    l=list()
    print("Enter elements : ")
    for i in range(n):  l.append(int(input()))
    return l
#function for linear search
def linear(l,a):
    for i in range(len(l)):
        if l[i]==a:
            return i
    return -2
#reading length of the list from the user and calling array() function to read elements 
n=int(input("Enter the length of the list:"))
l=array(n)
a=int(input("Enter the element to be searched in list:"))
#calling linear function
i=linear(l,a)
if i!=-2:
    print(a,"is present at the index:",i)
else:
    print(a,"is not present in the given list ")