# lists
#
# identification - []
# mutable datatype - data can be changed or updated during run time
# a container to store different data types
# forward indexing starts from 0 and backward indexing starts from -1
# elements will be seperated by a comma
#
# a = [12, "sam", "raj", 32]
# type(a)
#
# forward indexing
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
#
# reverse indexing
# print(a[-1])
# print(a[-2])
# print(a[-3])
# print(a[-4])
#
# Mutability

# a = [12, "sam", "raj", 32]
# print(a)
# a[1] = "punit"
# print(a)

# loop in list 

# a = [12, "sam", "raj", 32]
# 1) first method
# for i in a:
#   print(i, end = " ")

# 2) second method

# for i in range(len(a)):
#   print(a[i], end = " ")
#
# properties of a list

# 1) concatenation
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)

# 2) replication
# a = [1, 2, 3]
# print(a * 3)
#
# slicing in list

# a = [1, 2, 3, "sam", "raj", 4 [5, "aniket", 6]]

# print(a[1:4])
# print(a[3:])
# print(a[:3])
# print(a[:])
# print(a[1][2])
# print(a[6][1][2:4])
#
# Functions of a list

# 1) len() - returns length of a list
# a = [1, 2, 3, 4]
# print(len(a))

# 2) index() - returns indexing of an element
# a = [1, 2, "sam", "raj", 3]
# print(a.index("raj"))

# 3) count() - returns frequency of an element
# a = [1, 2, 2, 3, 3, 3]
# print(a.count(2))

# 4) append() - adds element at the last indexing of a list
# a = [1, 2, "sam", "raj", 3]
# print(a)
# print(a.append("mohit"))
# print(a)

# 5) insert(index, object) - adds element at a given index
# a = [1, 2, "sam", "raj", 3]
# print(a)
# a.insert(1, "sumit")
# print(a)

# 6) pop() - removes element from last index
# a = [1, 2, "sam", "raj", 3]
# print(a)
# a.pop()
# print(a)

# 7) remove - removes element from a given indexing
# a = [1, 2, "sam", "raj", 3]
# a.remove("sam")
# print(a)
# a.remove(3)
# print(a)

# 8) sort() - arrange elements in ascending order
# a = [1, 3, 2, 4, 5]
# print(a)
# a.sort()
# print(a)

# 9) reverse() - reverse a list
# a = [1, 2, "sam", "raj", 3]
# print(a)
# a.reverse()
# print(a)

# 10) min() - return the lowest number
# a = [1, 2, 3, 4]
# print(min(a))

# 11) max() - return the highest number
# a = [1, 2, 3, 4]
# print(max(a))

# 12) sum() - adds all elements
# a = [1, 2, 3, 4]
# print(sum(a))
#
# Q) create a user defined list
# a = []
# size = int(input("enter count: "))
# for i in range(size):
#   val = input("enter items: ")
#   a.append(val)
# print(a)

# Q-1-WAP t create a user defined list who return total sum of all numbers in a list
# a = []
# size = int(input("Enter a number: "))

# for i in range(size):
#     val = int(input("Enter a number: "))
#     a.append(val)

# print(a)

# sum = 0
# for i in range(len(a)):
#     sum = sum + a[i]

# print("Sum =", sum)

#-Q-2 WAP who print max number in a list
# a = [12,42,51,1]
# max = a[2]
# for i in range (len(a)):
#     if a[i] > max:
#         max = a[i]
#     print(max)

#-Q-3 create a user defined list and count how many even number are in a list withput using count()
# a = []
# user = int(input("Enter a number : "))
# for i in range(user):
    
#     is_even = int(input(" Try to enter a even number "))
#     a.append(is_even)
# print(a)
# for num in a:
#     if(is_even%2==0):
#         print(num,"The number is even ",end =" ")
#     else:
#         print(num,"Its not even ",end =" ")

#-Q-4 Multiply all numbers in the list
# numbs = [12,45,23,98]
# for i in range(len(numbs)):
#     numbs[i] = numbs[i] * 2
# print(numbs)

#-Q-5 remove duplicate from a list without using set()
# a  = [1,2,4,2,4,5,6,5]
# b = []
# for i in a (len(a)):
#     if i not in b:
#         b.append(i)
#     print(b)

#-Q-6 Reverse a list withput using reverse or slicing
# a = [1,2,3,4,5]
# rev = []
# for i in a:
#     rev = [i] + rev
# print(rev)

#-Q-7- Find comman element between two list
# a = [1,2,3,4,5]
# b = [4,5,6,7,8]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

#-Q-8 -> Flattern a nested list
# a = [[1,2],[3,4],[5,6]]
# flat = []  # ----> this is where we store the result from append funcation
# for sub in a:   #----> take each inner list
#     for list in sub:  # ---> take each element from inside
#         flat.append(list)   #----> and append it to flat empty list
# print(flat)

# Q-9->Find the smallest number in a list (like Q2 but for min).
# num = [12,4,89,11,1]
# small = num[0]
# for i in range(len(num)):
#     if num[i] < small:
#         small = num[i]
# print(small)

#-Q-9 Count odd numbers in a list.
# num = [12,11,34,55,63]
# for i in range (len(num)):
#     if num[i]%2!=0:
#         print("The number is odd :",num[i])
#     else:
#         print("The number is even : ",num[i])

#-Q-7->Merge two lists into one (without using +).
# a = [12, 34, 11, "Vedang", "Sharma", "REGEX"]
# b = [34, 23, 55, "Heello", "world"]
# c = []

# for item in a:
#     c.append(item)
# for item in b:
#     c.append(item)

# print(c)

# 8->Square each element in a list.
# text = [14,21,45,77]
# for i in range(len(text)):
#     text[i] = text[i]**2
# print(text)

# List Comprehenchion 
# syntax = [expression i for i in condition]

#-Q-1 Create a list of square of numbers from 1 to 5
# a = [i**2 for i in range(1,6)]
# print(a)

#-Q-2 Create a list of even numbers from 1 to 10
# a = [i for i in range(1,11) if i%2==0]
# print(a)

#-Q-3 create a list of square of odd numbers from 1 to 10
# a = [i**2 for i in range(1,11) if i%2!=0]
# print(a)

#-Q-4 Create a list of first letter of each word in a list
# a = ["apple","Bananan","cherry"]
# b = [i[0] for i in a]
# print(b)

#-Q-5 extract vowel from a given list using list comprehension
# b = "WE learn python"
# a = [i for i in b if i in "aeiosAEIOU"]
# print(a)

#-Q-6 -  WAP to create a lsit of numbers that are multipy of 5 but not 10 (from i to 30)
# a = [i for i in range(1,31) if i%5==0 and i%10!=0]
# print(a)


# Q-7 WAP to create a list of names,
# create a new list containing only names that start and end with the same letter

# name = ["Anna", "Arora", "Sam", "Nitin", "Punit", "Raj", "Naman"]

# a = [n for n in name if n[0].lower() == n[-1].lower()]  
# print(a)

#-Q-8 Extract words longer then 3 letter from a sentence
# a = "AI is the future of technolog"
# chr = (i for i in a.split() if len(i) > 3)
# print(list(chr))

#-Q-9 form the list of names kepp only names that start with a 
# names = ["Amit","Rohit","Anil","Sunil","Ajay","Ravi"]
# start  = (i for i in names if i.startswith("A"))
# print(list(start))

# Tuples in python
# Tuples are used to store multiple items in a single variable.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add, or remove items once the tuple is created.

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))

# Extend -- > extend the exsisting list(a-b)
# li = [1,2,3,4]
# li_2 = [5,6,7]
# # li.extend(li_2)
# # print(li)

# # Sort--> sorts the list in ascending order
# # array = [3,4,5,6]
# # sorted(array)
# # print(sorted)

# # TUPLE --> immutable,form of list but is immutable,change once can be changed again
# t = [1,2,3,4,5]
# print(type(t))

# Nested tuple 
# nested_tuple = (1,2,3,4,5[6,6])
# nested_tuple = [3][0]
# print(nested_tuple)

# WAP for the given sum of all the element which are given by the user
# num,age = input("Enter a name and age ").split("") #---> Split can help us to take more than one output,it return the number of substing
# print(num)
# print(type(int(age)))

# WAP to take two number from the user and give sum
# num_1 , num_2 = input("Enter a number a and b ").split()
# a = int(num_1)
# b = int(num_2)
# sum = a+b
# print(sum) 

#Map - give each data their value or their type
# a = list (map(int,input("enter the list of numbers ").split()))
# print(a)
# print(type(a))

# li = [1,2,4,5]
# sum = 0
# max = li[0]
# for i in range(1,len(li)):
    # Here we are comparing the max with the current number
    # if li[i] > max:
        # here we are comparing the second number to max
        # max = li[i]
# print(max)    

# li = [1,2,3,4,5]
# for i in range (len(li)):
#     if(li[i]%2==0):
#         print("These numbers are odd ",i)
#     else:
#         print("This number is even",i)

# li = [1,2,3,4,5]
# squ = []
# for num in range(len(li)):
    # squ = num**2
    # squ.append((num*num))
# print("The Square of the number is ",squ)

#  Wap the second largest number in the list
# print duplicate element from the list
# reversing element from the list

# li = (map(int,input("Enter a number").split()))
# count = []
# for i in range (int(li)):
#     if(li%2==0):
#         print("The number is even")
#     else:
#         print("This number is odd")
#     count+=1

# print duplicate element from the list
# li= [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
# dict = {}
# for num in li:
#     if num in dict:
#         dict[num]+=1
#     else:
#         dict[num] = 1
# print(dict)

# for key,value in dict.items():
#     if value > 1:
#         print(key)

# reversing element from the list
# num = [1,2,3,4,5]
# reverse = num[::-1]
# print(reverse)

# print duplicate element from the list
# num = [21,34,57,38,90]
# num.sort()
# print(num[-2])

# DICTIONARY ---> dictionary is the data type which stores the key and values paires , its is mutable , it is unoredred
# {"Key":"vedang"} --> dict = {}
# di = {"Name":"Vedang","Batch":"A18"} #---> name is key and batch is the value 
# print(di)
# print(di["Name"])
# print(di["Batch"])

#DICT ITEM -> 
# student = {"name": "Deeksha", "age": 20}
# for key, value in student.items():
    # print(key, "->", value)
# for key,value in enumerate(student.items()):
    # print(key,value)

# Create an empty set
# my_set = set()
# print(my_set)       
# print(type(my_set)) 

# Enumerate -->list banana, ek ek cheez ginna aur batana.
# li = [1,2,3,4,5]
# for index,value in enumerate(li):
#     print(index,value)

# fruit = {"Fruit":"Apple","Color":"Red"}
# for key,value in enumerate(fruit.items()):
#     print(key,value)

# WAP to print the student details 
# college = {
#     "Name": ["Vedang_Sharma", "Yash_Pareek"],
#     "Course": ["B.Tech", "BCA"],
#     "Location": ["Jaipur", "Jaipur"]
# }
# for value in enumerate(college.items()):
#     print(value)

#Build in funcation
# Get --> gets the specific value from a dict
# print(college.get("Name"))
# print(college.pop("Name"))

# it removes the key value pair from the dictioary
# print(college.popitem())

#SET Default
# college.setdefault("Study Hours", 0)
# print(college)


# PRINT ALL THE KEY IN A DICTIONARY USING THE LOOP  
# college = {
#     "Name": ["Vedang_Sharma", "Yash_Pareek"],
#     "Course": ["B.Tech", "BCA"],
#     "Location": ["Jaipur", "Jaipur"]
# }
# for key in college.keys():
#     print(key)

# CHECK IF NAME-KEY EXCIST IN A DICTIONARY
# if key == "Name":
#     print("Yes")
# elif key == "Course":
#     print("Yes")
# else:
#     print("No")
# COUNT THE FREQUENCY OF LETTER IN A DICTIONARY,SET

# text = "Programming"
# freq = {}

# for char in text:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1

# print(freq)

# text = "Programming"
# unique_letters = set(text)

# for char in unique_letters:
#     print(char, "->", text.count(char))

# num = (map(int,input("Enter a number").split()))
# for chr in num:
#     for count in num:
        
# li = [123,456,789]
# sum = 0
# for num in li:
    # while num>0:
        # digit = num%10
        # sum += digit  #--> in every step sum happens
        # num = num//10 #--> removes one digit from last
# print(sum)

# li = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
# counter = 0
# dup = []
# for num in li:
#     if num in dup:
#         counter +=1
#     else:
#         dup.append(num)
# print(counter)

# WAP to print the unique element in a list
# lis = [1,23,"sam",34,34,12,23,12,]
# uni= []
# for chr in lis:
#     if chr not in uni: 
#         uni.append(chr)
# print(uni)

# WAP where input is [1,2,0,0,4] and the output should be [1,2,4,0,0]
# li = [1,2,0,4,2,0]
# index = 0
# for i in range(len(li)):
    # if li[i] != 0: #--> checking if there is a zero at index [0]
#         li[index] = li[i]
#         index+=1
# while index < len(li):
#     li[index] = 0
#     index+=1
# print(li)

# li = [1,2,3,0,4,0,2]
# zero_count = 0
# for i in range(len(li)):
#     if li[i] == 0:
#         li[zero_count] = li[i]
#         print(f"index -> {zero_count},i -> {i} -> {li}")
#         zero_count += 1
# while zero_count < len(li):
#     li[zero_count] = 0
#     zero_count += 1
# print(li)

# WAP to print all the sublist of the given list
# Input = [1,2,3,4] output: [[1],[1,2],[1,2,3],[2],[2,3],[3]]
 
# li = [1,2,3,4]
# index = []
# # n = 4
# for i in range (len(li)):
#     for j in range(i+1,len(li)+1):
#         index.append(li[i:j])
# print(index)
   

# Hint two loops and slicing 

# ● Explain: From a list, print all elements that are smaller than a given number.
# ● Input: [3, 7, 2, 5, 8], number = 6
# ● Output: [3, 2, 5]
# a = [3,7,2,5,8]
# n = 6
# for i in range(len(a)):
#     if a[i] < n:
#         print(a[i])

# Find the average of the list
# ● Explain: Calculate the average value of all elements in the list.
# ● Input: [4, 5, 6, 7]
# ● Output: 5.5
 
# li = [4,5,6,7]
# sum = 0
# for i in range(len(li)):
#     sum+=li[i]
#     avg = sum/4
# print(avg)

# WAP that Separate even and odd numbers
# ● Explain: Divide the list into two lists—one with even numbers and one with odd
# numbers.
# ● Input: [1, 2, 3, 4, 5]
# ● Output: Even: [2, 4], Odd: [1, 3, 5]

# li = [1,2,3,4,5]
# odd_list = []
# even_list = []
# for i in range(len(li)):
#     if(li[i]%2==0):
#         even_list.append(li[i])
#     elif(li[i]%2!=0):
#         odd_list.append(li[i])
# print(even_list)
# print(odd_list)

# Q4. Find the second largest element
# ● Explain: Find the second largest number in the list.
# ● Input: [10, 20, 5, 15]
# ● Output: 15
    
# li = [-1,-2,-3,-4,0]

# max1 = li[0]          # largest
# max2 = float('-inf')  # second largest (very small initially)

# for i in range(len(li)):
#     if li[i] > max1:          # if current is bigger than largest
#         max2 = max1           # old largest becomes second largest
#         max1 = li[i]          # update largest
#     elif li[i] > max2 and li[i] != max1:  
#         max2 = li[i]          # update second largest

# print("Largest:", max1)
# print("Second Largest:", max2)

# Q5. Find the third largest element
# ● Explain: Find the third largest element in the list.

# ● Input: [7, 2, 9, 4, 6]
# ● Output: 6

# li = [10, 20, 5, 15]

# max1 = max2 = max3 = float('-inf')

# for num in li:
    # if num > max1:                 # bigger than largest
        # max3 = max2
        # max2 = max1
        # max1 = num
    # elif num > max2 and num != max1:  # between largest and second
        # max3 = max2
        # max2 = num
    # elif num > max3 and num != max1 and num != max2:  # between second and third
        # max3 = num

# print("Largest:", max1)
# print("Second Largest:", max2)
# print("Third Largest:", max3)

# Q6. Find the three greatest elements (candidates)
# ● Explain: Find the top three largest numbers in the list.
# ● Input: [8, 3, 10, 6, 7]
# ● Output: [10, 8, 7]
# ● Hint: Sort the list or find the largest three using loops.

# li = [8, 3, 10, 6, 7]
# top3 = sorted(li, reverse=True)[:3]
# print("Top 3 elements:", top3)

# ● Explain: For each element in the list, calculate the product of all other elements except
# the current one.
# ● Input: [1, 2, 3, 4]
# ● Output: [24, 12, 8, 6]

# li = [2,5,6,7]
# for i in range(len(li)):
#     product = 1
#     for j in range (len(li)):
#         if i != j:
#             product *= li[j]
#     print("The product is ",product)
    # print("The index is ",i)

# Product a list where each element is the product of all other elements except the current one
# li = [1, 2, 3, 4]
# output = []
# for i in range(len(li)):
#     product = 1
#     for j in range (len(li)):
#         if i != j:
#             product *= li[j]
#     output.append(product)
# print(output)

# IMPORTANT LEET CODE QUESTION
# li = [1,2,3,4]
# sublist  = []
# for i in range(len(li)):
#     for j in range(i+1,len(li)+1):
#         sublist.append(li[i:j])
# print(sublist)

#WAP to reverse a sentence which is in string form
# text = "I am learning python".split
# reverse = ""
# for chr in text:
#     reverse = chr + reverse
# print(reverse)

# WAP that reverse the given string 

# text = "I am learning python".split()
# text.reverse()                         
# reverse = " ".join(text)               
# print(reverse)

# Sum of all elements except the current one
# li = [1,2,3,7]
# sum = 0
# for i in range(len(li)):
#     if sum != li[i]:
#         sum+=li[i]
#     else:
#         sum-=li[i]
# print(sum)
        
# Find the second largest element in a list
# Input: [8, 3, 10, 6, 7]
# Output: 8

# li = [8,3,10,6,7]
# largest =  second_largest = float('-inf')

# for num in li:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num!= largest:
#         second_largest  = num
        
# print(second_largest)

# Print all pairs whose sum is equal to a target
# Input: li = [2, 4, 3, 5, 7], target = 7
# Output: (2, 5), (4, 3)

# li = [2,4,3,5,7]
# target = 7
# # sum = 0
# for i in range(len(li)):
#     for j in range(i+1,len(li)):
#         if li[i] + li[j] == target:
#             print(li[i],li[j])

# ● Explain: Rotate the list to the right by k steps.
# ● Input: [1, 2, 3, 4, 5], k=2
# Output: [4, 5, 1, 2, 3]

# li = [1,2,3,4,5]
# k = 2
# k = k %len(li)

# rotate = li[-k:] + li[:-k]
# print(rotate)    

# Find the longest word in a sentence
# Input: "I am learning Python programming"
# Output: "programming"

# sentence = "I am learning Python programming"

# words = sentence.split()
# longest = ""

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print("Longest word:", longest)




