                                                            #gcd of two numbers
#method for finding gcd
def gcdNumber(a,b):
    if b==0:        
        return a
    else:
        return gcdNumber(b,a%b)
#taking two numbers from the user 
a=int(input('enter 1st number : '))
b=int(input('enter 2nd number : '))
#printing the gcd of the given numbers
print('gcd of given two number is',gcdNumber(a,b))