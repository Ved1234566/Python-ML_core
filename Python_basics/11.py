# FILE HANDELING
# We use file handeling in programming to store , update , retrieve and maipulate

# Opening file
# conrtiner mein txt , exe file 
# f= open('7,py','+a')
# f.read()
# f.close()

# READING A FILE
# file = open('7.py','r')
# print(file.read())
# file.close()

# WRITTING THE FILE
# file = open('7.py','w')
# file.write('Hello World')
# file.close()

# if any text is already present in the file then how can we add the next line
# for this we can append mode('a')
# file = open('7.py','a')
# file.write("\nThis is the new line! ")
# file.write("\n Here we are ")
# file.close()

# if ant file dosent excist
# file = open('Smaple.py','w')
# file.write("Hello World")
# file.close()

# sentences = ["Ths is the first line from the list, ","This is the second line from the list, ","This is the third line from the list, "]
# file = open('Smaple.txt','w')
# for sentence in sentences:
#     file.write(sentence)
# file.close()

# READ, READLINE,READINES
# file = open('Sample.txt','r')
# READ LINE ONLY ONE
# re = file.readline()
# READ MANY LINES
# li = file.readlines()
# print(type(re))
# print(li)
# file.close()

# file = open('smaple.txt','r')
# text = file.readlines()
# print(text[1])
# file.close

# With is used to close the opened file after I/O operations
# It automatically close the file
# with open('smaple.txt','r') as file:
#     text = file.readlines()
#     print(text[1])
# file.read()

# seek and tell function into the file handeling
# while open('sampl.txt','r') as f:
    # read the file line by line
    # print(f.readline())
    #finding the pointr
    # print(f.tell())
    # seeking the line to 0
    # print(f.seek(0))
    # print(f.readlines())

# Write lines
# Take big files
# big_data = ['hello world' for i in range(20000)]
# with open('new.txt','w') as f:
#     f.writelines(big_data)

# reading big files into small size
# with open('new.txt','r') as f:
#     chunk_size = 100
#     while True:
#         chunk = f.read(chunk_size)
#         if not chunk:
#             break
#         print("chunk ->")
#         print(chunk)

# r+ mode for file handeling
# this is used for reading and writing the file but it works for the exisitng file only
# with open('new_1.txt','r+'):
#     f.write('anythings')
#     f.seek(0)
#     print(f.read())

# w+ mode in the file handeling
# This mode is used for the reading and writing the file and also create the file if it dosent excist
# with open('sample.txt','w+'):
#     f.write('anythings')
#     f.seek(0)
#     print(f.read())

# #copying all the content from one line to another file
# with open('Sample.txt','r') as f:
#     content = f.read()
#     with open('Sample_1.txt','w') as f1:
#         f1.write(content)

# write a program to create a file named hello.txt an write "Hello , python " into it
# with open('hello.txt','w') as f:
    # f.write('Hello , python')
    # f.seek(0)
    # print(f.read())

# write a program to read the content of hello.txt  and print it
# with open('hello.txt','w') as f:
#     print(f.read())

# HOW TO READ CSV FILE
# import csv
# with open('student_marks.csv','r') as f:
#     content = csv.reader(f)
#     for row in content:
#         print(row)

# write a program to append a new line "Welcome to python" to hello.txt
# with open("hello.txt", "a+") as f:
    # f.write("\nWelcome to python")
    # f.seek(0)   # move pointer to beginning of file
    # print(f.read())

# write a program to read the first 10 character of file
# with open('hello.txt','r') as f:
#     print(f.read(10))
#     f.seek(0)
#     print(f.read(10))

# write a program to write a list of number  [1,2,3,4,5] into a file , one number per line
# with open('sample.txt','w') as f:
#     num = [1,2,3,4,5]
#     for i in num:
#         f.write(str(i)+"\n")
#         print(f.write(str(i)+"\n")) 

# WAP a program to read all number from a file and calculate the sum
# with open('sample.txt','r') as f:
#     num = f.readlines()
#     sum = 0
#     for i in num:
#         sum += int(i.strip())
#     print(sum)


    