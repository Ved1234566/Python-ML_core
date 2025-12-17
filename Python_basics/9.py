# LOCAL AND GLOBAL VARIABLE
# global variable
# a = 10 

# def hello():
#     #local vriable
#     b = 10 
#     global a
#     print(a)
# print(hello)

#BANK MANAGMENT SYSTEM
# balance = 1000
# # Function with withdrawl amount
# def withdrawl(amount):
#     global balance
#     if amount > 0 and balance >= amount:
#         balance -= amount
#         print(f"You've successfully debited your {amount}")
#         print(f"Your balance is {balance}")
        
# # Function for deposit the balance
# def deposit(amount):
#     global balance
#     if amount > 0:
#         balance += amount
#         print(f"You have successfully deposted the {amount}")
#         print(f"Your balance is {balance}")
        
# return deposit(200)
# return withdrawl(200)

# STUDENT GRADING SYSTEM
# # NESTED FNCTION
# def grade(marks):
#     # nested function to calculate percentage
#     def calculate_percentage(marks):
#         p = marks  # assuming marks are already out of 100
#         return p

#     # nested function to assign grade
#     def nested_grade(percentage):
#         if 90 <= percentage <= 100:
#             return "A"
#         elif 80 <= percentage < 90:
#             return "B"
#         elif 70 <= percentage < 80:
#             return "C"
#         else:
#             return "Fail"

#     percent = calculate_percentage(marks)
#     grad = nested_grade(percent)
#     return grad


# result = grade(50)
# print(result)  # Output: A
 
# # MAP FUNCTION -> build in function used to apply a specific function to each item of an iterable 
# # (like a list) and return a new iterable with the results.
# a = list(map(int,input("Enter a number").split()))
# sum = 0
# for num in a:
#     sum+=num
# print(sum)

# calculate the square of the given number of list [1,2,3,4]
# num = list(map(int,input("Enter a number ").split()))
# for a in num:
#     print(a**2)

# li = [1,2,3,4]
# li = list(map(lambda x:x**2,li))
# print(li)

# BASICALLY U DONT NEED TO USE FOR LOOP
# s = lambda x : x**2
# print(s(4))

# li = [x for x in range(10)]

# s = lambda x:x **2
# list(map(s,li))

# filtered = list(filter(lambda x: x%2==0,li))
# print(filtered)

 
