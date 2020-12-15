                                                    #finding the power of the given base
#method for finding power
def res(b,p):
    if p==0:
        return 1
    else:
        return b*res(b,p-1)
#taking the inputs of the base and power from the user
b=int(input('enter base : '))
p=int(input('enter power : '))
#printing the resultant
print('the result of',b,'to the power of',p,'is',res(b,p))