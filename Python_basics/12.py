
#ZERO DIVISION ERROR
# a = 10
# b = 2

# this 'try' blocks always runs
# try:
#     c = a/b
#     print(c)
    
# this loop block runs when an exception occurs in the program

# except ZeroDivisionError:
#     print("Error: Division by zero")
    
# this else block runs if no exception occurs

# else:
#     print("c")

# Name error

# try:
#     print(z)
    
# Name error

# except NameError:
#     print("Error: Variable 'z' is not defined")
    
# Type error

# try:
#     a = 'str'
#     b = 10
#     c = a+b
# except TypeError:
#     print("Please use the datat type for this operation")
    
# Value error

# try:
#     a = '23fg32'
#     b = int(a)
# except ValueError:
#     print("Please use the integer value in string typecast")
# else:
#     print(b)

# INDEX ERROR
# li = [1,2,3,4,5]
# try:
#     print(li[6])
# except IndexError:
#     print("Error: Index out of range")
    
# KEY ERROR
# di = {
#     "name": "Arun",
#     "Batch": "A-18",
#     "Mobile No": 9876543210
# }

# try:
#     print(di["name"])   # access using key
# except KeyError:
#     print("Error: Key not found")

# FILE NOT FOUND ERROR
# try:
#     with open('sample.txt','r') as f:
#         content = f.read()
        # print(content)
# This block will run when an exception occurs
# except FileNotFoundError:
#     print("Error: File not found")
# this block will run when any exception occurs
# else:
    # print(content)
# this block will always run
# finally:
#     f.close()
#     print("This block will always run")

# 1. Division with Zero Handling
# Problem: Develop a program that prompts the user for two numbers and performs
# division. Implement exception handling to gracefully manage cases where the user
# attempts to divide by zero.

# a = 100
# b = 50 

# try:
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero")

# 2. Integer Input Validation
# Problem: Write a program that requests an integer input from the user. Include exception
# handling to catch and manage situations where the user provides a non-integer value.

# try:
#     a = int(input("Enter a number: "))
#     b = int()
# except ValueError:
#     print("Error: Please enter an integer value")
# else:
#     print(b)

    
# 3. File Not Found Handling
# Problem: Create a program designed to open and read the content of a file named
# data.txt. Implement exception handling to specifically address scenarios where
# data.txt does not exist.

# try:
#     with open('data.txt','r') as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: File not found")

# 4. String to Integer Conversion
# Problem: Develop a program that attempts to convert a given string into an integer.
# Include exception handling to manage cases where the string cannot be successfully
# converted to an integer.

# s = input("Enter a number: ")
# try:
#     a = int(s)
#     print(a)
# except ValueError:
#     print("Error: Please enter an integer value")

# 5. List Index Out of Range
# Problem: Write a program that accepts a list of numbers and asks the user for an index.
# Print the element at the user-provided index. Implement exception handling to prevent
# errors if the user enters an index that is outside the valid range of the list.

# ind = int(input("Enter a index: "))
# li = [1,2,3,4,5]
# try:
#     print(li[ind])
# except IndexError:
#     print("Error: Index out of range")
# except ValueError:
#     print("Error: Please enter an integer value")

# 6. Division with Success Message
# Problem: Create a program that takes two numerical inputs and performs a division
# operation. Utilize try...except...else blocks to ensure a success message is printed
# only when the division is completed without any exceptions.

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# try:
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero")
# else:
#     print("Success: Division completed without errors")

# 7. Custom Negative Number Exception
# Problem: Design a program that prompts the user for a number. If the user enters a
# negative number, raise a custom exception named NegativeNumberError.

# a = int(input("Enter a number: "))
# if a < 0:
#     raise NegativeNumberError
# else:
#     print(a)
# Problem: Write a program that opens a file, reads its content, and guarantees that the file
# is always closed properly, regardless of whether an error occurred during the reading
# process. Use the finally block for this purpose.

# try:
#     with open('sample.txt','r') as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("Error: File not found")
# except Exception as e:
#     print(f"Error: {e}")
    
# finally:
#     try:
#         f.close()
#     except NameError:
#         print("Error: File not opened")
        
# 9. Dictionary Key Not Found
# Problem: Develop a program that asks the user to input a key and then attempts to print
# the corresponding value from a predefined dictionary. Implement exception handling to
# manage situations where the entered key does not exist in the dictionary.

# dic = {
#     "Name" : "Vedang",
#     "Course" : "Python",
#     "Location" : "Jaipur"
# }
# try:
#     user = input("Enter a key: ")
#     print(dic[user])
    
#     value = dic[user]
#     print(value)
    
# except KeyError:
#     print("Error: Key not found")

# 10. Nested Exception Handling
# Problem: Create a program that uses nested try...except blocks. The outer block
# should handle ValueError for invalid input (e.g., non-numeric input for division), and the
# inner block should handle ZeroDivisionError when attempting to divide by zero.

# try:
    # Outer try block for invalid input
    
    # num1 = int(input("Enter numerator: "))
    # num2 = int(input("Enter denominator: "))

    # try:
    
        # Inner try block for division
        
#         result = num1 / num2
#         print(f"Result: {result}")

#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero.")

# except ValueError:
#     print("Error: Please enter valid numeric values.")

# CUSTOM EXCEPTION  
# def age_validation(age):
#     if age < 0:
        #  Raise is used to throw the exception
        # Excepton = Its a general purpose class
#         raise Exception("Please provide an age which is valid")
#     else:
#         print("Age is validated")

# try:
#     age_validation(-1)
# except Exception as e:
#     print("You've got the exception:", e)

# BANK MANAGMENT
# balance = 50000

# def bank():
#     global balance
#     withdraw = int(input("Enter the amount to withdraw: "))
#     if withdraw > balance:
#         raise Exception("Insufficient balance")
#     else:
#         balance -= withdraw
#         print("Transaction successful")
#         print("Balance:", balance)
# try:
#   withdraw = int(input("Enter the amount to withdraw: "))
#   bank()
# except Exception as e:
#   print(e)


# 2. Voting Eligibility 
# Scenario: A user is entering their age in a voting application. 
# Question: What exception should be raised if the user enters a negative age or an age greater than 120? 

# def age_validation(age):
#     if age < 0:
#          Raise is used to throw the exception
#         Excepton = Its a general purpose class
#         raise Exception("Please provide an age which is valid")
#     else:
#         print("Age is validated")

# try:
#     age_validation(-1)
# except Exception as e:
#     print("You've got the exception:", e)

# 3. Online Exam Marks 
# Scenario: A teacher is entering marks for students in an online exam system. 
# Question: What exception should be raised if any entered marks are less than 0 or greater than 100? 

# def online_marks(marks):
#     if marks < 0 or marks > 100:
#         raise Exception("Please provide a valid mark")
#     else:
#         print("Marks is validated")
# try:
#     online_marks(101)
# except Exception as e:
#     print("You've got the exception:", e)

# 4. Password Strength 
# Scenario: A website requires users to create a password during registration. 
# Question: What exception should be raised if the user enters a password shorter than 8 characters?

# password = input("Enter your password: ")
# length = len(password)
# def password_strength(password):
#     if length < 8:
#         raise Exception("Password must be at least 8 characters long")
#     else:
#         print("the password is correct -> go AHEAD")
# try:
#     password_strength(password)
# except Exception as e:
#     print("You've got the exception:", e)

# 5. Temperature Conversion 
# Scenario: A weather application is performing temperature conversions. 
# Question: What exception should be raised if the entered temperature in Celsius is less than -273.15 (absolute zero)? 

# temperature = int(input("Enter the temperature in Celsius: "))
# def temperature_conversion(temperature):
#     if temperature < -273.15:
#         raise Exception("Temperature cannot be less than -273.15 Celsius")
#     else:
#         print("Temperature is validated")
# try:
#     temperature_conversion(temperature)
# except Exception as e:
#     print("You've got the exception:", e)

# 6. Email Signup 
# Scenario: A user is registering on a website and entering their email address. 
# Question: What exception should be raised if the user's entered email address does not contain an "@" symbol? 

# email = input("Enter your email address: ")
# def email_signup(email):
#     if "@" not in email:
#         raise Exception("Please provide a valid email address")
#     else:
#         print("Email is validated")
# try:
#     email_signup(email)
# except Exception as e:
#     print("You've got the exception:", e)

# 7. Movie Ticket Booking
# Scenario: A user is booking movie tickets through an online system.
# Question: What exception should be raised if the user attempts to book more than 10
# tickets in a single transaction?

# ticket = int(input("Enter the number of tickets: "))
# def online(ticket):
#         if ticket > 10:
#             raise Exception("You can book only 10 tickets at a time")
#         else:
#             print("Ticket is validated")
# try:
#     online(ticket)
# except Exception as e:
#     print("You've got the exception:", e)

# 8. Library System
# Scenario: A user is returning a book in a library system.
# Question: What exception should be raised if the entered number of days (for the return
# period) is negative or exceeds 365?

# user = int(input("Enter the number of days: "))
# def book(user):
#         if(user < 0 or user > 365):
#                 raise Exception("Please provide a valid number of days")
#         else:
#                 print("Book is validated")
# try:
#         book(user)
# except Exception as e:
#         print("You've got the exception:", e)

# 9. School Admission
# Scenario: A student is applying for admission to a school, and their class grade is being
# entered.
# Question: What exception should be raised if a student enters a class grade that is not
# between 1 and 12?

# def check_grade(grade):
#     if grade < 1 or grade > 12:
#         raise ValueError("Grade must be between 1 and 12.")
#     else:
#         print("Grade is valid")


# try:
#     check_grade(15)
# except ValueError as e:
#     print("Error:", e)

# 10. Phone Number Validation
# Scenario: A user is entering their phone number in a registration form.
# Question: What exception should be raised if the user enters a phone number containing
# letters or fewer than 10 digits?

# def phone(number):
#         if number.isdigit() or number.isalpha():
#             raise ValueError("Phone number must contain only digits.")
#         elif len(number) < 10:
#             raise ValueError("Phone number must be at least 10 digits long.")
#         else:
#             print("Phone number is valid.")
# try:
#         phone(number)
# except ValueError as e:
#     print("Error:", e)


# 5. List Index Out of Range
# Problem: Write a program that accepts a list of numbers and asks the user for an index.
# Print the element at the user-provided index. Implement exception handling to prevent
# errors if the user enters an index that is outside the valid range of the list.

# numbers = [23,46,87,82,99,34]
# print("The list of numbers is:",numbers)
# try:
#         index = int(input("Enter a numbers:"))
#         print(numbers[index])
# except ValueError:
#         print("Please enter a valid integer.")
# except IndexError:
#         print("Index out of range. Please enter an index within the valid range.")

# 6. Division with Success Message
# Problem: Create a program that takes two numerical inputs and performs a division
# operation. Utilize try...except...else blocks to ensure a success message is printed
# only when the division is completed without any exceptions.

# a = int(input("Enter a numnber : "))
# b = int(input("Enter b number : "))

# try:
#         result = a/b
# except ZeroDivisionError:
#         print("You can not divide a number by zero")
# else:
#         print("You have zero place here buuddy try again next time ")


# WAP to reverse a string
# li = [1,2,3,4,5]
# for i in range(len(li)):
#         rev = li[::-1]
# print(rev)

# li = [1,2,3,4,5,6]
# reversed = []
# for i in (li):
#         reversed = [i] + reversed
# print(reversed)


