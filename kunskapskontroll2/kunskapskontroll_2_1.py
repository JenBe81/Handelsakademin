import numpy as np

def add_mult_matrices(A, B, op):
    if not (isinstance(A, np.ndarray) and isinstance(B, np.ndarray)):
        raise ValueError("Both inputs must be numpy arrays!")
    
    rows_A, cols_A = A.shape
    rows_B, cols_B = B.shape

    if op.lower() == 'add':
        if(A.shape == B.shape):
            return A + B
    elif op.lower() =='multiply':
        if(cols_A == rows_B):
            return A @ B
        else:
            raise ValueError("The number of columns in matrix A must be equal to the number of rows in matrix B for matrix multiplication!")
    else:
        raise ValueError("Invalid operation!, specify either 'add' or 'multiply")

print("Task: print out the dimension (number of exes), shape, size and the datatype of the matrix A")
A = np.arange(1, 16).reshape(3,5)
print(A)
print('Dimension of A:', A.ndim)    # .ndim gives the number of axes of a matrix
print('Shape of A:', A.shape)       # .shape gives the shape of the matrix
print('Size of A:', A.size)         # .size gives the total number of elements of a matrix
print(type(A))

print("\n\nTask: Do the following computations on the matrices B and C:") #
print("- Elementwise subtraction")
print("- Elemntwise multiplication")
print("- Matrix multiplication (by default you should use the @ operator)")
B = np.arange(1, 10).reshape(3, 3)
C = np.ones((3, 3))*2

print("B =", end=' ')
print(B)
print("\nC =", end=' ')
print(C)

D = B - C
print("\nB - C =", end=' ')
print(D)

D = B * C
print("\nB * C=", end=' ')
print(D)

print("\nB @ C=", end=' ')
D = B @ C
print(D)

print("\n\nTask: Do the following calculations on the matrix:")
print("- Exponentiate each number elementwise (use the np.exp function")
print("- Calculate hte minimum value in the whole matrix")
print("- Calculate the minimum value in each row")
print("- Calculate the minimum value in each column")
print("- Find the index value for the minimum value in the whole matrix (hit: use np.argmin)")
print("- Find the index value for the minimum value in each row (hint: use np.argmin)")
print("- Caluclate the sum for all elmeents")
print("- Calculate the mean for each column")
print("- Calculate the medium for each column")
B = np.arange(1, 10).reshape(3, 3)
print("B =", end=' ')
print(B)

B_exp = np.exp(B)
print("B_exp =", end=' ')
print(B_exp)

print("\nminimum value using np.min():", np.min(B))
print("minimum value using .min() method:", B.min())

print("minimum value for each row:", np.min(B, axis=1))
print("minimum value for each column:", np.min(B, axis=0))

print("index for the minimum value of the entire matrix:", np.argmin(B))
print("index for the minimum value of the each row:", np.argmin(B, axis=1))

print("the sum of all elements in the matrix:", np.sum(B))
print("mean for each column:", np.mean(B, axis=0))
print("median for each column:", np.median(B, axis=0))

print("\nTask: What does it mean when you provide fewer indices than exes when slicing?")
print("A[1] will give the second row of the matrix")

print("\nTask How to iterate through the multimdimensial array elemnetwise?")
print("One way to do it would be to use a nested for loop like this:")
for row in A:
    for element in row:
        print(element)
        
print("\nTask: Explain what three axes mean?")
a = np.arange(30)
b = a.reshape((2, 3, -1))
print(a)
print()

print(b)
print("One way to look at it would be that each exis represents a dimension. For one dimesion you can mark a point with an index only. For two dimensional plane you can mark a point by using a two coordinates (x, y) and for a three dimensional space you can mark a coordinate using three coordinates (x, y, z)")

print("\n Exercises in chapter 10.1 in book 'matematik för yrkeshögksolan'")

x = np.array([4, 3])
print("x = ", x)
print("Vektorn har dimension:", x.ndim)
print("5x = ", x*5)
print("3x = ", x*3)
print("5x + 3x = ", (x*5) + (x*3))
print("8x = ", x*8)
print("4x - x = ", (x*4) - x)

x_reshaped = x.reshape(1, -1)
print("x_transposed = ", x_reshaped.T)
print("new dimension = ", x_reshaped.ndim)
print("I am unsure about that dimension because in order to transpose I converted the array (one dimensional) to a 2D matrix. So technically it will have two dimensions, but in reality it is still only one dimension")
print("x + x_transposed is not defined")
print("The norm of vector x, ||x||, is: ", np.linalg.norm(x))

print("\n TAsk: Do all the exercises in chapter 10.2 except 10.2.4. Start with 10.2.1")
A = np.array([[2, 1, -1],
              [1, -1, 1 ]])
A_transposed = A.transpose()
B = np.array([[4, -2, 1],
              [2, -4, -2]])
B_transposed = B.transpose()
C = np.array([[1, 2],
              [2, 1]])
C_transposed = C.transpose()
D = np.array([[3, 4],
              [4, 3]])

D_transposed = D.transpose()
E = np.array([[1], [2]])

I = np.array([[1, 0], [0, 1]])

print("2A = ", 2 * A)
print("B - 2A = ", B - 2 * A)
print("3C - 2E = ", (3 * C) - (2 * E))
print("2D - 3C = ", (2 * D) - (3 * C))
print("D_transposed + 2D = ", D_transposed + (2* D))
print("2C_transposed - 2D_transposed = ", (2 * C_transposed) - (2 * D_transposed))
print("A_transposed - B = Will not work due to incompatible sizes")
print("AC = Will not work due to incompatible sizes")
print("CD = ", C @ D)
print("CB = ", C @ B)
print("CI = ", C @ I)
print("AB_tranposed = ", A @ B_transposed)

print("\nTask: Next is the exercises of 10.2.2:")
A = np.array([[2, 3,4],
              [5, 4, 1]])
A_transposed = A.transpose()

print("AA_transposed = ", A @ A_transposed)

print("\nTask: Next is the exercises of 10.2.3:")
A = np.array([[1, 2],
              [2, 4]])
B = np.array([[2, 1],
              [1, 3]])
C = np.array([[4, 3],
              [0, 2]])

# I accidently entered the wrong nubers in A matrix so had to undertand why I did not get the expected result.
#print("A =", end=' ')
#print(A)
#print("B =", end=' ')
#print(B)
#print("C =", end=' ')
#print(C)
#print("A @ B =", end=' ')
#print(A @ B)
#print("A @ C =", end=' ')
#print(A @ C)

if np.array_equal((A @ B), (A @ C)):
    print("AB = AC")
else:
    print("AB!= AC")

if np.array_equal(B, C):
    print("B = C")
else:
    print("B!= C")
