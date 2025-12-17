# Q-1 what is the difference between a list and a tuple
# A list is written using square brackets [ ].
# A tuple is written using parentheses ( ).
# A list is mutable, meaning you can change, add, or remove elements after creating it.
# A tuple is immutable, meaning once it is created, you cannot change its elements.
# Lists are slower in performance compared to tuples.
# Tuples are faster because they cannot be changed.
# Use a list when you need data that will change.
# Use a tuple when the data should stay constant.

# Q-2 how do you create a user defined array
# You can create a user-defined array in Python using the numpy library. 

# import numpy as np
# a = np.array([1,2,3,4,5,6,7,8,9,10])
# print(a)

# Q-3 create a random array in range 100-200 and total values will be 64 . And you have to reshape it all possible factor
# import numpy as np
# a = np.arange(100,200)
# b = np.random.randint(100,201,64)
# print(b)

# Q-4 Create an array of (5,5) in with all the values will be 7
# import numpy as np
# a = np.ones((5,5))
# print(a)
# a = a * 7
# print(a)

# Q-5 explain view vs copy with examples
# view --> It is just a reference of original array
# import numpy as np
# a = np.array([1, 2, 3, 4])
# b = a.view()  
# copy --> It is a new array which is independent of original array
# import numpy as np
# a = np.array([1, 2, 3, 4])
# c = a.copy()  

# Q-6 difference between linespace() and unique() with code of example
# linespace -> is used to create equal space between start and end of a list
# import numpy as np
# a = np.linspace(1,2,3)
# print(a)

# Unique -> elemenate dupliacte value and tell only those values which are only one
# import numpy as np
# a = np.array([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10])
# a = np.unique(a)
# print(a)


# Q-7 what is hstack() and vstack()? create 4 array and connect it via hstack and vstack
# hstack() --> It will connect the arrays horizontally
import numpy as np

a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])
d = np.array([7, 8])

h = np.hstack((a, b, c, d))
print("HSTACK Result:", h)

# vstack() --> It will connect the arrays vertically
v = np.vstack((a, b, c, d))
print("VSTACK Result:\n", v)

# Q-8 create an array in range 11-26 now you have to reshape it (4*4) and the you have to calculate total sum , row wise sum and column wise sum
# import numpy as np
# a = np.arange(11,27).reshape(4,4)
# print(a)
# print("Total Sum : ",np.sum(a))
# print("Row Wise Sum : ",np.sum(a,axis=1))
# print("Column Wise Sum : ",np.sum(a,axis=0))
