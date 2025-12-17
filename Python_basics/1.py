 # INTRODUCTION  to Numpy
 # Numpy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, 
 # along with a large collection of high-level mathematical functions to operate on these arrays
 
 # Difference between Numpy and Lists
 # 1 .  Numpy arrays are more compact than lists, and more memory-efficient than lists
 # 2 Numpy arrays are more fast than lists, and more memory-efficient than lists
 # 3 Numpy arrays are more convenient than lists, and more memory-efficient than lists
 
# import numpy as np
# a = [1,2,3,4,5,6,7,8,9,10]
# print(type(a))

# b= np.array(a)
# print(b)
# print(type(b))

# a = [1,45,32,62]
# print(type(a))

# user Defined Array
# a = []
# size = int(input("Enter the size of the array: "))
# for i in range(size):
#     val = int(input("Enter the value: "))
#     a.append(val)
#     print(a)
#     b = np.array(a)
#     print(b)

# a = [[1,2,3], [4,5,6], [7,8,9]]
# a

# b = np.array(a)
# b

# Matrix --- > rows , columns

# row_1 = [1,2,3]
# row_2 = [4,5,6]
# row_3 = [7,8,9] |

# col_1 = [1,4,7]
# col 2 = [2,5,8]
# col 3 = [3,6,9]

# col_1 = [1,4,7]
# col_2 = [2,5,8]
# col_3 = [3,6,9]

# Total Element  = row * column = 3 * 3 = 9

# print("The Total Number of rows and columns : ",b.shape)
# print("Total Number of Elements in the Matrix : ",b.size)

# to check the dimension check the number of square bracket
# if there is only one square bracket then it is a 1D array
# if there are two square brackets then it is a 2D array
# if there are three square brackets then it is a 3D array
# and so on...  

# How to check the dimension of a matrix
# a = np.array(a)
# print(a)
# print(a.ndim)

# a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# print(a)
# print(a.ndim)

# Images  ---> Pixels(0-225) -->Normaliz(0-1) ---> Matrix ---> Operation
# DL ---> Artificial Neural Network --> weight --> Random creation --> Numpy
# Datasets --> dummy entry --> random modules --> attach pandas

# Pre defined functions in Numpy

#(1) zeroes() = it will create an array in which all the values will be zero in either 1-D or Multi-Dimension

# a = np.zeros((2,3))
# print(a)

# a = np.zeros((2,3))
# print(a)

# (2) Ones() = it will create an array in which all the values will be one in either 1-D or Multi-Dimension
# import numpy as np
# a = np.ones(4)
# print(a)

# a = np.ones((2,5))
# print(a)

# (3) eye() = it will create an identity matrix in which all the values will be one in the diagonal and zero in the rest of the places
# import numpy as np;
# a = np.eye(3)
# print(a)

# b = np.eye(4,2)
# print(b)

# (4) diag() = it will create a diagonal matrix in which all the values will be one in the diagonal and zero in the rest of the places
# import numpy as np;
# a = np.diag([1,2,3])
# print(a)

# #(5) Random Module-- >
# (a) randint(low, high, size)
# it will create a random integer array in the given range
# syntax : np.random.randint(min_range,max_range,total_number)

# a = np.random.randint(1,10,5)
# print(a)

# (b) rand() --> it will generate a random float number between 0 and 1
# Syntax : np.random.rand(total_random_number)

# a = np.random.rand(5)
# print(a)

# (c) seed() --> it will generate a random number but it will always generate the same number
# Syntax : np.random.seed(seed_value)

# np.random.seed(34)
# a  = np.r
# andom.randint(1,10,4)
# print(a)

# view a copy

# a = np.array([1,2,3,4,5,6,7,8,9,10])
# print(a)
 
# b = a[1:4]
# b[:] = 0
# print(b)

# a = np.array([10,20,30,40,50])
# b = a[1:4].copy()
# b[:] = 0
# print(b)

#Reshaping an  array
# total rows * columns = 3 * 4 = 12

# a = np.random.randint(1,10,12)
# print(a)

# y = mx + b
# m = matrix--->  weights
# x = values ---> matrix

# matrix(column) + (row) matix

# a.reshape(-1,4)
# a.reshape(2,-2)

# a = np.arange(1,10)
# print(a*2)

# a = np.arange(1,5).reshape(2,2)
# print(a)

# a.dot(b)

# a>10
# b = a>10
# a[b]

# a = np.arange(1,4)
# print(a**2)

# a = np.arange(1,10).reshape(3,3)
# print(a)

# np.sum(a)
# np.int64(45)

# np.sum(a,axis=1)
# array([6,15,24])

# np.sum(a,axis=0)

# UNIQUE FUNCTION
#it will return 3 arrays
# arr ---> return 3 arrays
# return_index = true --> Indexing of Unique Element
# return count = true --> Frequency of each element

# a = np.array([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10])
# print(a)

# b = np.unique(a,return_index=True,return_counts=True)
# print(b)

# Linespace() ---> it will return an array in which element will be same gap in a given range
# syntax : np.linespace(min_num , max_num  , total_numbers)

# a = np.linspace(1,2,3)
# print(a)

# Horizontal and Vertical Stacking --->
# horizontal stacking ---> It will add 2 or more arrays in horizontally

# a = np.arange(1,5)
# print(a)

# b = np.arange(5,9)
# print(b)

# c = np.arange(a,b)
# print(c)

# np.hstack((a,b,c))

# np.vstack((a,b,c))

# import numpy as np
# a = [1,2,3,4,4,5,6,7,8,9,10]
# np.array(a)
# print(np.zeros((2,3)))
# print(np.ones((2,3)))

# print(np.random.randint(1,10,5))  # 5 random ints 1–9
# print(np.random.rand(4))          # 4 random floats 0–1
# print(np.random.seed(10))         # Fix randomness (repeatable result)

# b = a[1:3]       # view (linked)
# b[:] = a[0:2]  

# x = np.arange(1,13)

# print(a.reshape(3,4))
# print(a.reshape(-1,4))   # Auto calculate rows
    
