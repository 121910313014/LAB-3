                                                        #LINEAR SEARCH WITH DYNAMIC INPUTS AND USER DEFINED FUNCTIONS
#list of elements
l=[1,2,3,4,5,8,0,10,24]
a=int(input("Enter the element to be searched in list:"))       #element to be searched
for i in range(len(l)):             #checking where the element is present
    if l[i]==a:
       print(a,"is present at the index:",i)
       break 
else:
    print(a,"is not present in the given list ")
    