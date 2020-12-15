# Function to represent the Sparse Matrix
def sparse_matrix(arr):
    sp = []
    r = len(arr) # Number of Rows
    c = len(arr[0]) # Number of columns
    # Finding the non zero elements
    for i in range(r):
        for j in range(c):
            if arr[i][j]!=0:
                sp.append([i,j,arr[i][j]])
    return sp

# Function to multiply two sparse matrices
def mul(arr1,arr2):
    r1 = len(arr1)
    r2 = len(arr2)
    c2 = len(arr2[0])
    res = [[0 for _ in range(c2)] for __ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                res[i][j] += arr1[i][k]*arr2[k][j]
    ans = sparse_matrix(res)
    return ans

# Function to print martix
def print_martix(arr):
    if arr==[]: print('EMPTY MATRIX')
    for i in arr:
        print(*i)

# Function to take array input
def input_matrix(r):
    arr = [] # Declaring the matrix
    i = 0
    while i<r:
        dup = list(map(int,input().split()))
        arr.append(dup)
        i += 1
    return arr


# Inputting arrays
r1 = int(input("Enter the number of rows in first matrix : "))
c1 = int(input("Enter the number of columns in first matrix : "))
r2 = int(input("Enter the number of rows in second matrix : "))
c2 = int(input("Enter the number of columns in second matrix : "))
if c1!=r2:
    print('You cannot multiply these matrices')
    exit()
print("Enter Martix 1")
arr1 = input_matrix(r1)
print("Enter Martix 2")
arr2 = input_matrix(r2)

# Printing Original Matrices
print("The Original Matrices are")
print("Matrix 1")
print_martix(arr1)
print("Matrix 2")
print_martix(arr2)
print()

# Printing Sparse Matrices
print("The Sparse Matrices are")
sp1 = sparse_matrix(arr1)
sp2 = sparse_matrix(arr2)
print("Sparse Matrix 1")
print_martix(sp1)
print("Sparse Matrix 2")
print_martix(sp2)
print()

# Printing the result
print("Multiplication of 2 Sparse Matrices")
result = mul(arr1,arr2)
print_martix(result)