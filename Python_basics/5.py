# loop in python
# (1) for loop
#syntac = for i in range(min_number , max_number+1,step_number):
# Write a program to print 1 to 10
# for i in range(1,10,1):
#     print(i)
# write a program who print from 10 to 1
# for i in range(10,0,-1):
#     print(i)
# # write a program that take starting number and ending number and step number from user
# a = int(input("Enter the starting number: "))
# b = int(input("Enter the ending number: "))
# c = int(input("Enter the step number: "))
# for i in range(a,b,c):
#     print(i)
# for i in range(1,10):
#     # print(i**2)
    
# a = int(input("Enter the number: "))
# b = int(input("Enter the end number: "))
# for i in range(1,b+1,2):
#     print(i**2)  ---> to find out the Square root of the number 
# a = int(input("Enter the number"))
# b = int(input("Enter the end number: "))
# odd = 0
# even = 0
# for i in range(a,b+1,1):
#     if(i%2==0):
#         even = even+i
#         print(i,"Even number")
#     else:
#         odd = odd+i
#         print(i,"Odd number")

#find the factorial of the number
# num = int(input("Enter the number: "))
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print("factorial of the number is: ",fact)


# Reserve a string entered by the user
# string = input("Enter a string")
# reverse = " "
# for i in range(len(string)-1,-1,-1):
#     reverse += string[i]
# print("Reserved string:",reverse)

# text = input("Enter a string ")
# vowels = "aeiou"
# count = 0
# for ch in text:
#     for ch in vowels:
#         count += 1
# print("Number of vowels :",count)


# print("Prime numbers between 1 and 50 are:")

# for num in range(2, 51):   
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:           
#         print(num, end=" ")
        
# print("Reverse the 50 to 1")
# for i in range(50,-1):
#     is_prime = True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime = False
#             break
#         if is_prime:
#             print(num, end=" ")
# for i in range(5):
#     for j in range(4):
#         print(i,j)

# for i in range(1,6):
#     print(i*"*")
# for i in range(5,0,-1):
#     print(i*"*")

# for i in range(1,6):
#     for j in range(i):
#         print("*" ,end = " ") ---> end =" " for space betwen stars
#     print() ---> for next line 

# for i in range(5,0,-1): # ---> i is for rows
#     for j in range(i): #---> j is for column
#         print("*", end = " ")
#     print()

# for i in range(1,6):
#     for j in range(1, i+1): ---> 1 - is the starting , i+1 add value to the i
#         print(j, end = " ") ----> j here is used to print the column output
#     print()

#step-1 (i=5,j=(1,6)) ----> print(1,2,3,4,5)
#step-2 (i=4, j=(1,5)) ----> print(1,2,3,4)
#step-3 (i=3, j=(1,4)) ----> print(1,2,3)
#step-4 (i=2, j=(1,3)) ----> print(1,2)
#step-5 (i=1, j=(1,2)) ----> print(1)

# for i in range(6,0,-1):
#     # for j in range(i,0,-1):
#     for j in range(1,i+1):
#         print(j, end = " ")
#     print()

# WAP to print table from 1 to 10
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,"=",i*j)
#     print()
    
# WAP to print number from 1 to 100
# for i in range(1,101):
    # print(i,end=" ")    
    
# WAP to find vowel and consonent
# text = input("Enter the character: ")

# vowel = "aeiou"
# vowel_count = 0
# consonent_count = 0 

# for char in text:
    # if char.isalpha():
        # if char in vowel:
            # vowel_count+=1
        # else:
            # consonent_count+=1
# print("Vowel count:",vowel_count)
# print("Consonent count:",consonent_count)
            
# for i in range(1, 6):   # rows 1 to 5
#     for j in range(i):  # columns = row number
#         print("*", end=" ")
#     print()

# for i in range(1, 7):
#     for j in range(i):
#       print("*",end=" ")
#     print()


# i = int(input("Enter the number"))
# for i in range(1,11):
#     print("Square of",i, "=",i*i)

# for i in range(1,6):
#     for j in range(i):
#         print("*", end=" ")
#     print()
    
# n = 5
# for i in range(1, n+1):
#     print(" "*(n-i)+"*" * (2*i-1))
    

# for i in range(6,0,-1):
    # num = 1
    # for j in range(i):
        # print(num, end=" ")
        # num += 1   # increase number for each column
    # print()

#Right angel triangle
#step-1 (i=0, sum =1)
#j = 0 ----> print(1), sum = 1+1 =2
#step-2 (i=1, sum=2)
#j = 1 ---> print(1,2) , sum 2+1 =3
#step-3 (i=2 , sum=3)
#j=2 ----> print(1,2,3) , sum 3+1 =4
#step-4 (i=3, sum=4)
#j=3 ----> print(1,2,3,4) , sum 4+1 =5
#step-5 (i=4, sum=5)
#j=4 ----> print(1,2,3,4,5) , sum 5+1 =6

# reversed
# step-1 (i=5, sum=1)
#j = 1 ---> print(2) , Sum = 6-1 = 5
#step-2 (i=4, sum=2)
#j = 2 ---> print(3) , Sum = 5-1 = 4
#step-3 (i=3, sum=3)
#j = 3 ---> print(4) , sum = 4-1 = 3
#step-4 (i=2, sum=4)
#j = 4 ---> print(5) , Sum = 3-1 = 2
#step-5 (i=1, sum=5)
#j = 5 ---> print(6) , sum = 2-1 = 1

# num = 5
# for i in range(1, num+1):
#     print(" "*(num-i), end="")
#     for j in range(1,i+1):
#         print(j, end=" ")
#         # num += 1
#     print()

#pyramid
#step - 1 (i=1, sum=1)
#j = 1 ---> print(1) , sum = 1+1 = 2
#step -2 (i=2, sum=2)
#j = 2 ---> print(2) , sum = 2+1 = 3
#step - 3 (i=3, sum=3)
#j = 3 ---> print(3) , sum = 3+1 = 4
#step - 4 (i=4, sum=4)
#j = 4 ---> print(4) , sum = 4+1 = 5
#step - 5 (i=5, sum=5)
#j = 5 ---> print(5) , sum = 5+1 = 6

# WAP of multiplication of 5 using for loop
# a =5
# for i in range(1,11):
#     print(a*i)
#     i+=1

# WAP to program who count vowels in string
# vowel = input("Enter a vowel ")
# text = "aeiou"

# count = 0
# for ch in vowel:
#     if ch in text:
#         count+=1
# print("The number of vowel in string are" ,count)

# num = 6
# for i in range(1,num+1):
#     print(" "*(num-i), end = " ")
#     for j in range(1,i+1):
#         # num += 1
#         print(j, end=" ")
#     print()

# num  = 6
# for i in range(num,0,-1):
#     print(" " * (num - 1),end = " ")
#     for j in range(1,i + 1):
#         print(j, end=" ")
#         num+=1
#     print()

num = 6
for i in range(num, 0, -1):
    print(" " * (num - i), end=" ")
    for j in range(1, i + 1):        
        print(j, end=" ")
    print()  

#Q -  WAP to reverse a string using a for loop and without build in function

# text = input("Enter a string: ")
# reversed_text = ""
# for char in text:
#     reversed_text = char + reversed_text
# print("Reversed string:", reversed_text)
    
# Start: reversed_text = ""
# Iteration 1: char = "h" → "h" + "" → "h"
# Iteration 2: char = "e" → "e" + "h" → "eh"
# Iteration 3: char = "l" → "l" + "eh" → "leh"
# Iteration 4: char = "l" → "l" + "leh" → "lleh"
# Iteration 5: char = "o" → "o" + "lleh" → "olleh"

#-Q- WAP to count upper case and lower case character in a string
# text  = "I Love PYThon"

# lower_case  = 0
# upper_case = 0

# for char in text:
#     if char.isupper():
#         upper_case+=1
#     elif char.islower():
#         lower_case+=1
#     else:
#         print("No character in text")
#     # print("Upper and lower case are :",count)
# print("Total upper case are ",upper_case)
# print("Total lower case are ",lower_case)

#-Q- WAP to find the sum of digit of a give number using for loop

# num = 54321
# sum_of_digits = 0


# for digit in str(num):
#     sum_of_digits += int(digit)

# print("Sum of digits:", sum_of_digits)


#-Q- WAP that print only sum of even number in the range of 1 to 11

# num = 11
# sum_of_even = 0
# for i in range(1,num+1):
#     if i%2 == 0:
#         sum_of_even += i
# print("The sum of even number is:",sum_of_even)



# (2) while loop

# Initialization
# Condition 
# Increment / Decrement

# Q.1 Write a program who print number from 1 to 4
# i = 1
# n = 4
# while(i<=n):
#     print(i)
#     i+=1

#STEP - 1 (i=4 , n=4)
# while(i < 4):
#     print(i)
# i = 1+1 = 2
#STEP - 2 (i=2, n=4)
# while(2<=4):
#     print(2)
#     i = 2+1=3
#STEP - 3
# while(3<=4):
#     print(3)
#     i = 3+1=4
#STEP - 4
# while(4<=4):
#     print(4)
#     i = 4+1=5
#STEP - 5
# while(5<=4):
#     print(5)
#     i = 5+1=6

#-Q-2
# WAP to print number from 10 to 1 using while loop

# i = 10
# n = 1
# while i >= n:
#     print(i)
#     i = i - 1

#-Q-3 WAP to who print sum of digit
# i = 1
# n = 4
# sum = 0 
# while(i<+4):
#     sum = sum+i
#     i = i+1
# print(sum)

#Step -1 (i = 1 , n = 4 , sum = 0)
# while(i<=n):
#     sum = 0 + 1 = 1
#     i = 1+1 = 2
#Step - 2 (i = 2, n = 4, sum = 1)
# while(2<=4):
#     sum = 1 + 2 = 3
#     i = 2 + 1 = 3
# Step - 3 (i = 3, n = 4, sum = 3)
# while(3<=4):
#     sum = 3 + 4 = 7
#     i = 3 + 1 = 4
# Step - 4 (i = 4, n = 4, sum = 7)
# while(4<=4):
#     sum = 7 + 4 = 11
#     i = 4 + 1 = 5

# WAP for sum of square in a given range
# range = 1->4
# i  =  1
# n = 4 
# sum = 0
# while i in range(1,n+1):
#     sum += i**3
#     i += 1
# print("The sum of square is:",sum)



# Step 1 (i = 1, sum = 0)
# Condition: 1 ≤ 4 
# sum = 0 + 1 = 1
# square = 1*1 = 1
# i = 2
# Step 2 (i = 2, sum = 1)
# Condition: 2 ≤ 4 
# sum = 1 + 2 = 1 + 4 = 5
# squa1re = 2*2 = 4
# i = 3
# Step 3 (i = 3, sum = 5)
# Condition: 3 ≤ 4 
# sum = 5 + 3 = 5 + 9 = 14
# square = 3*3 = 9
# i = 4
# Step 4 (i = 4, sum = 14)
# Condition: 4 ≤ 4 
# sum = 14 + 4 = 14 + 16 = 30
# square = 4*4 =16
# i = 5 → loop ends
# Answer = 30

# Q-1-WAP to program to print the sum of given number
# i = 1234
# sum  = 0
# while(i>0):
#     d = i%10
#     sum = sum + d
#     i = i//10
# print("Total = ",sum)

#-Step-1-> (i=1234 , sum = 0)
# while(1234>0):
#     d = 1234%10
#     sum 0+4 =4
#     i = 1234//10 = 123
#-Step-2-> (i=123 , sum 4)
# while(123>0):
#     d = 123%10
#     sum = 4+3 = 7
#     i = 123//1 = 12
#-Step-3-> (i=12 , sum = 4)
# while(12>0):
#     d = 12%10
#     sum = 7 + 1 = 8
#     i = 12 // 10 = 1
# break

# i =1234
# rev=0
# while(i>0):
#     rev = (rev*10) + (i%10)
#     i = i//10
#     print(rev)
    
#-Step-1 (i=123 , rev = 0)
# while(1234>0):
#     rev = (0*10) + (1234%10) = 0+3 = 3
#     i=123//10 = 12
    
#-step-2 (i = 12  , rev = 3)
# while(123>0):
#     rev = (3*10) + (123%10) = 30
#     i=123//10 = 12
#-step-3 (i =12 , rev = 30)
# while(12>0):
#     rev = (12*10) + (12%10)
#     i = 12//10
#-step-4
# while(1>0):
#     rev = (123*10) + (1%10)
#     i= 1//0 = 0
# break

#- WAP to sum of square
# i =123
# sum = 0 
# original = i
# while(i>0):
#     sum = sum + (i%10)**3
#     i = i//10
# print("Total = ",sum)
# if(sum == original):
#     print("Armstrong number")
# else:
# #     print("Not Armstrong number")

# #-Step-1 (i=123 , sum = 0)
# # while(123>0):
#     sum = 0+(123%10)**2 + 0 + (123//10)**2 =9
#     i = 123//10 = 12
#-step-2 (1=12 , sum = 9)
# while(12>0):
#     sum = 9+(12%10)**2 + 12 + (12//10)**2 = 9+4 = 13
#     i = 12//10 = 1
#-step-3 (i=1 , sum = 13)
# while(1>0):
#     sum = 13+(1%10)**2 + 1 + (1//10)**2 = 13+1 = 14
#     i = 1//10 = 0
# #-step-4 (i=0 , sum = 14)
# while(0>0):
#     sum = 14+(0%10)**2 + 0 + (0//10)**2 = 14
#     i = 0//10 = 0
# #-step-5 (i=0 , sum = 14)
# while(0>0):
#     sum = 14+(0%10)**2 + 0 + (0//10)**2 = 14
#     i = 0//10 = 0
#  break

# i = 12345
# count = 0
# while(i>0):
#     count = count + 1
#     i = i//10
# print("Total number of digits = ",count)




# # Membership Operator --->
# # container --> data check
# # in
# # is not

# # identifier operater
# is 
# is not

#-Q-1 WAP to print a prime number and tell if its prime or not

# num = int(input("Enter a number : "))
# if num<=1:
#     print(num,"is not a prime number")
# else:
#     i = 2
#     prime = True
#     while(i<=num):
#         if num%i == 0:
#             prime = False
#             break
#         i = i+1
#     if prime:
#         print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# - Q - WAP print 5 table
# i=1
# while(i<10):
#     print("5 *",i,"=",i*5)
#     i = i+1
# print("Table of 5 is printed",i)

# - Q - WAP to print max number in a string using while loop
# num = [12,43,53,21,98]
# i = 0
# max = num[0]
# if i < len(num):
#     while num[i] < max:
#         max = num[i]
#         i = i+1
# print("The max number is = ",max)

# WAP check the number is even or not 

# i = int(input("Enter a Numbers "))
# its_even = 2
# if i >= its_even:
#     print("The number is even")
# else:
#     print("The number is odd")
#     i = i+1
# print("The even number is = ", i)

# count () ---> it will return frequency of an element
# a = [1,2,3,1,1,1,2]
# a.count(1)

# a = ['Sam','raj',45,78.12]
# print(a)
# a.append('Mohit')
# print(a)