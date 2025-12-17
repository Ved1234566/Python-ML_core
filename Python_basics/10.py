# from functools import reduce
# li = [1,2,3,4,5,6]
# reduce(lambda x,y :x+y,li)

# Recursion - when thw function call itself then that process of calling that function is know as recurssion
# Fibonachi
# a = 0
# b = 1
# for i in range(1,10):
#     print(a,end=" ")
#     a,b = b,a+b

# it will run unit basi condition matches
# writeing the N th fibonachi

# def fibb(n):
    # if n==1:
        # return 1  #0+1 = 1 , 1+1 = 2 , 2+1=3
    # if n==0:
        # return 0
    # return fibb(n-1) + fibb(n-2)  #same
# for i in range(1,11+1):  # range to run loop till 11 inddex
    # print(fibb(i),end=" ") # print the fibb with space

# print factorial
# n = int(input("Enter a number : "))
# fact = 1
# for i in range(1,n+1):
#    fact*=i
# print(fact)

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# find the largest number from the given list

# li = [1,2,3,4,5,6,7,8,9]

# max = li[0]
# for i in range(len(li)):
#     if li[i] > max:
#         max = li[i]
# print(max)
# find the second largest number from the given list
# li = [2,4,7,1,9,5]
# second_largest = li[1]
# max = li[0]
# for i in range(len(li)):
#     if li[i] <= second_largest:
#     elif second_largest<= max and li[i] != max: 
#          second_largest = li[i]
# print(second_largest)

# li = [2, 4, 7, 1, 9, 5]

# Use different variable names to avoid shadowing built-ins
# li = [12,35,6,1]
# maximum = li[0]
# second_largest = float('-inf')

# for i in range(len(li)):
#     if li[i] > maximum:
#         second_largest = maximum
#         maximum = li[i]
#     elif li[i] > second_largest and li[i] != maximum:
#         second_largest = li[i]

# print("Second largest:", second_largest)

# intersection of the two list [12,13,14,15], [2,3,4,5,6]
# li_1 = [12,13,4,3,15]
# li_2 = [1,2,3,4,5]
# c = []
# for i in li_1:
#     if i in li_2:
#         c.append(i)
# print(c)

# rotate list
# li = [1,2,3,4,5]
# k = 0
# last = li.pop()
# li.insert(k,last)
# print(li)

# li = [1,2,3,4,5]
# reversed = []
# for i in li:
#     reversed = [i] + reversed
# print(reversed)

# li = [1,2,3,4,5]
# left = 0
# right = len(li)-1
# while left<right:
#     li[left],li[right] = li[right],li[left]
#     left+=1
#     right-=1
# print(li)

# li = [1,2,3,4,5]
# def rev(left,right,li):
#     while left<right:
#         li[left],li[right] = li[right],li[left]
#         left+=1
#         right-=1
# key = 2
# reversed = (0,len(li)-1)
# reversed = (0,key-1)
# reversed = (0,len(li)-1)

# li = [1,2,3,3,4,5,1]
# new_li = []
# def remove_duplicate():
#     for item in li:
#         if li not in new_li:
#             new_li.append(item)
#     return new_li
    

    