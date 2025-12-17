# OOPS

# object oriented programming - real world entities
# CLASS - blueprint for the object

# class student:
    # # init function automatically called when the object is called
    # def __init__(self,name,rollno):
    #     self.name = name
    #     self.rollno = rollno
        
    #Display all the properites of the student 
    # def display_info(self):
    #     print(f"name: {self.name}")
    #     print(f"rollno:{self.rollno}")
# Here we are creating an object of the class student
# st1 = student("Vedang",101)
# st2 = student("Ankit",102)

# print(st1.display_info())
# print(st1.name)
# print(st1.rollno)
# print(st2.name)
# print(st2.rollno)     

# # Make class if car()                   
# class car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def display_info(self):
#         print(f"make: {self.make}")
#         print(f"model: {self.model}")
#         print(f"year: {self.year}")
# car1 = car("Toyota","Camry",2022)
# car2 = car("NEXA", "Phonnix",2023)

# (car1.display_info())
# (car2.display_info())

# College Managment System
# class student:
#     # Class level attributes
#     college_name = "JK LAKSHMIPAT UNIVERSITY"
#     def __init__(self,name,rollno,college):
#         self.name = name
#         self.rollno = rollno
#         self.college = college
#     def display_info(self):
#         print(f"name: {self.name}")
#         print(f"rollno: {self.rollno}")
#         print(f"college: {self.college}")
# s1 = student("Vedang","2022BCA055",student.college_name)
# s1.display_info()

# class Student:
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno

#     def save_to_file(self, filename):
#         with open('hello.txt', 'a') as f: 
#             f.write(f"{self.name},{self.rollno}\n")
#         print("Student saved successfully!")

# # Take input from user
# name = input("Enter student name: ")
# rollno = input("Enter roll number: ")

# s1 = Student(name, rollno)
# s1.save_to_file("hello.txt")

# MAIN PILLER OF THE OOPS
# 1 - inheritance
# 2 - encapsulation
# 3 - polymorphis
# 4 - abstraction 

# 1) Inheritance
# class student:
#     def __init__(self,name,id,gender,department,):
#         self.name = name
#         self.id = id
#         self.gender = gender
#         self.department = department
# class teacher:
#     def __init__(self,name,id,gender,department,salary):
#         self.name = name
#         self.id = id
#         self.gender = gender
#         self.department = department
#         self.salary = salary

   


# class Person:
#     def __init__(self, name, id, gender):
#         self.name = name
#         self.id = id
#         self.gender = gender

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"ID: {self.id}")
#         print(f"Gender: {self.gender}")


# Inheriting from Person
# class Student(Person):
#     def __init__(self, name, id, gender, marks):
#         super().__init__(name, id, gender) # function is used to call a method from the parent (super) class inside a child class.
#         self.marks = marks

#     def display(self):
#         super().display_info()
#         print(f"Marks: {self.marks}")


# class Teacher(Person):
#     def __init__(self, name, id, gender, salary, department):
#         super().__init__(name, id, gender)
#         self.salary = salary
#         self.department = department

#     def display(self):
#         super().display_info()
#         print(f"Salary: {self.salary}")
#         print(f"Department: {self.department}")


# Creating objects
# student = Student("Rahul", 10, "Male", "BCA")
# teacher = Teacher("Ankit", 11, "Male", 50000, "IT Department")

# # Display info
# student.display()
# print()
# teacher.display()


# 🧩 Q1. Animal Sounds
# Problem: Create a parent class Animal with a method sound(). Then create subclasses
# Dog and Cat that override the sound() method. Print the sound each animal makes.
# Hint: Use the same function name in both child classes.
# Expected Output Example:Dog barks

# class animel:
#     def __init__(self,dog,cat):
#         self.dog = dog
#         self.cat = cat
#     def sound(self):
#         print(f"{self.dog} barks")
#         print(f"{self.cat} meows")
        
# Display the sound
# animel1 = animel("Dog","Cat")
# animel1.sound()

# 🧩 Q2. Vehicle Info
# Problem: Create a class Vehicle with attributes brand and color. Then make a subclass
# Car that adds attributes speed and price. Write a method show_details() that prints
# all details of the car.
# Example:Brand: BMW
# Color: Black
# Speed: 220
# Price: 5000000

# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
# class car(Vehicle):
#     def __init__(self, brand, color, speed, price):
#         super().__init__(brand, color)
#         self.speed = speed
#         self.price = price
#     def display_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Color: {self.color}")
#         print(f"Speed: {self.speed}")
#         print(f"Price: {self.price}")
# c1 = car("BMW","Black",220,5000000)
# c2 = car("NEXA","Phonnix",200,2000000)
# c2.display_info()

# 🧩 Q3. Employee Hierarchy
# Problem: Create a base class Employee with attributes name and id. Create two
# subclasses:
# ● Manager (with attribute department)
# ● Developer (with attribute programming_language)
# Each subclass should have a method to display its full details.

# Challenge: Use super() properly to initialize parent attributes.

# class employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
# class manager(employee):
#     def __init__(self,name,id,department):
#         super().__init__(name,id)
#         self.department = department
# class developer(employee):
#     def __init__(self,name,id,programming_language):
#         super().__init__(name,id)
#         self.programming_language = programming_language
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"ID: {self.id}")
        # print(f"Department: {self.department}")
#         print(f"Programming Language: {self.programming_language}")
        
# cq1 = manager("Ankit",11,"IT Department")
# cq2 = developer("Rahul",10,"Python")
# cq2.display_info()
        
        
# 🧩 Q4. Shape Area Calculation
# Problem: Create a base class Shape with a method area() (that prints "Area not
# defined"). Create subclasses:
# ● Circle (take radius)
# ● Rectangle (take length and width)
# Override the area() method in each subclass to print the correct area.
# Hint:
# ● Formula:
# ○ Circle → πr2
# ○ Rectangle → l × w

# class Shape:
#     def __init__(self):
#         print("Area not defined")

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()  # call parent constructor
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius


# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__()  # call parent constructor
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def display_info(self):
#         print(f"Area of rectangle: {self.area()}")


# # Create objects
# c1 = Rectangle(2, 3)
# cq = Circle(2)

# # Display results
# c1.display_info()
# print(f"Area of circle: {cq.area()}")


# 🧩 Q5. Bank Account System (Mini Project Style)
# Problem: Create a class Account with attributes name, balance, and methods
# deposit() and withdraw(). Create two subclasses:
# ● SavingsAccount (adds interest_rate and method add_interest())
# ● CurrentAccount (adds overdraft_limit)
# Write a main program to:
# 1. Create both types of accounts.
# 2. Perform deposit, withdraw, and add interest operations.
# 3. Display the final balance.

# class Account:
#     def __init__(self, name, balance, method):
#         self.name = name
#         self.balance = balance
#         self.method = method

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount}. New balance: {self.balance}")
#         else:
#             print("Invalid deposit amount")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")
#         else:
#             print("Invalid withdraw amount or insufficient balance")


# class SavingsAccount(Account):
#     def __init__(self, name, balance, method, interest_rate):
#         super().__init__(name, balance, method)
#         self.interest_rate = interest_rate

#     def add_interest(self):
#         interest = self.balance * self.interest_rate / 100
#         self.balance += interest
#         print(f"Interest added: {interest}. New balance: {self.balance}")


# # 🧩 Main program
# s1 = SavingsAccount("Vedang", 5000, "Online", 5)
# s1.deposit(1000)
# s1.add_interest()
# s1.withdraw(2000)
# print("Final Balance:", s1.balance)

# Q - Create a class Book with attributes title, author, and price.
# Create a subclass LibraryBook that adds library_name and copies_available.
# Add a method display_info() to show all details.

# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
# class libraryBook(Book):
#     def __init__(self, title, author, price, library_name, copies_available):
#         super().__init__(title, author, price)
#         self.library_name = library_name
#         self.copies_available = copies_available
    
#     def display_info(self):
#         print(f"Library Book Details:")
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Price: {self.price}")
#         print(f"Library Name: {self.library_name}")
#         print(f"Copies Available: {self.copies_available}")
# c1 = libraryBook("Harry Potter","Jared",2300,"ABC Librarey",True)
# c1.display_info

# Q2. Employee & Manager

# Create a base class Employee with attributes name and salary.
# Create a subclass Manager that adds bonus and a method total_salary()
# that prints the total = salary + bonus.

# # class employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
# class manager(employee):
#     def __init__(self, name, salary, bonus):
#         super().__init__(name, salary)
#         self.bonus = bonus
#     # Something like this IMPORTANT
#     def total_salary(self):
#         return self.salary + self.bonus
#     def display_info(self):
#         print(f"Manager Details:")
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")
#         print(f"Bonus: {self.bonus}")
#         print(f"Total Salary: {self.total_salary()}")
# CQ = manager("Vedang", 5000, 1000)
# CQ.display_info()

# Q5. Student & Marks

# Create a class Student with attributes name and rollno.
# Create a subclass Result that adds marks1, marks2, marks3,
# and a method display_total() that shows total and average marks.

# class student:
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno
# class marks_1(student):
#     def __init__(self, name, rollno,subject_1,subject_2,subject_3):
#         super().__init__(name, rollno)
#         self.subject_1 = subject_1
#         self.subject_2 = subject_2
#         self.subject_3 = subject_3
# class marks_2(marks_1):
#     def __init__(self, name, rollno,subject_1,subject_2,subject_3,subject_4,subject_5):
#         super().__init__(name, rollno,subject_1,subject_2,subject_3)
#         self.subject_4 = subject_4
#         self.subject_5 = subject_5
# class marks_3(marks_2):
#     def __init__(self, name, rollno, subject_1, subject_2, subject_3, subject_4, subject_5,subject_6):
#         super().__init__(name, rollno, subject_1, subject_2, subject_3, subject_4, subject_5)
#         self.subject_6 = subject_6
        
#     def display_total(self):
#         total = self.subject_1 + self.subject_2 + self.subject_3 + self.subject_4 + self.subject_5 + self.subject_6
#         average = total / 6
#         print(f"Total Marks: {total}")
#         print(f"Average Marks: {average:.2f}")

# cq  = marks_3("Vedang", 123, 80, 90, 75, 88, 92, 85)
# cq.display_total()
        
# 2. Multiple Inheritance
# class grandparent:
#     def message (self):
#         print("Hello from grandparent")
#INHERITING FROM GRANDPARENT
# class father:
#     def message_from_father (self):
#         print("Hello from father")
# INHERITING FROM FATHER
# class child:
#     def message_from_child(self):
#         print("Hello from child")
        
# c = child()
# class teacher:
#     def __init__(self, subject, qualification, experience):
#         self.subject = subject
#         self.qualification = qualification
#         self.experience = experience

#     def teach(self):
#         print(f"Teacher has a good background in {self.subject}")


# class Singer:
#     def __init__(self, songs, genre, album_released):
#         self.songs = songs
#         self.genre = genre
#         self.album_released = album_released

#     def sing(self):
#         print(f"Singer is good in {self.genre} genre")


# # Inheriting from both teacher and Singer
# class person(teacher, Singer):
#     def __init__(self, name, age, subject, qualification, experience, genre, songs, album_released):
#         teacher.__init__(self, subject, qualification, experience)
#         Singer.__init__(self, songs, genre, album_released)
#         self.name = name
#         self.age = age

# p = person("Vedang", 20, "SINPHER", "MSc", 5, "Pop", 10, 2)
# p.teach()
# p.sing()

# POLYMORPHISM  - IT IS A CONCEPT IN WHICH MEAN MANY FORM
# OVERLOADING - 
# OVERRIDING - 


# class A:
#     def show(self):
#         print("Hello from A")
# class B(A):
#     def show(self):
#         print("Hello from B")
# class C(B):
#     def show(self):
#         print("Hello from C")
# class d(c):
#     pass
# obj = D()
# for obj in [A(),B(),C()]:
#     obj.show
    
# MRO (METHOD RESOLUTION ORDER) - 
# It is the order in which the methods are searched for in a class hierarchy.
# It is used to resolve the ambiguity in the case of multiple inheritance.
# The MRO of a class is the list of classes that the class inherits from,
# in the order in which they are searched for methods.
# The MRO of a class can be accessed using the __mro__ attribute.
# The MRO of a class can also be accessed using the mro() method.

# class mother:
#      def skills(self):
#          print("Managing House")
# class father:
#     def skills(self):
#         print("Managing finance")
# class child(mother,father):
#     def skills(self):
#         pass
# obj1 = child()
# obj1.skills()

# Q1. Animal Sound (Basic Polymorphism)
# Problem: Create a parent class Animal with a method sound(). Then create subclasses
# Dog, Cat, and Cow that override the method to print their specific sounds. Finally, loop
# through a list of all animals and call their sound() methods.
        
# class Animal:
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         print("Dog is barking")
# class Cat(Animal):
#     def sound(self):
#         print("Cat is meowing")
# class Cow(Animal):
#     def sound(self):
#         print("Cow is mooing")
# animals = [Dog(), Cat(), Cow()]
# for animal in animals:
#     animal.sound()

# Q2. Employee Hierarchy (Multilevel Inheritance)
# Problem: Create three classes:
# ● Person (name, age)
# ● Employee (inherits from Person, adds employee_id)
# ● Manager (inherits from Employee, adds department)
# Display all details using a display() method in the last class.

# class person:
#     def feature(self,name,age):
#         self.name = name
#         self.age = age
# class employee(person):
#     def feature(self,name,age,employee_id):
#         super().feature(name,age)
#         self.employee_id = employee_id
# class manager(employee):
#     def feature(self, name, age, employee_id, department):
#         super().feature(name, age, employee_id)
#         self.department = department
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Employee ID: {self.employee_id}")
#         print(f"Department: {self.department}")

# m1 = manager()        
# m1.feature("Vedang", 20, 12345, "IT")
# m1.display()
        
# Q3. Vehicle Types (Method Overriding)
# Problem: Make a parent class Vehicle with a method move(). Create subclasses Car
# and Boat that override move() to print "Car drives on road" and "Boat sails on water".
# Demonstrate polymorphism by calling move() for different objects in a loop.  

# class vehical:
#     def move(self):
#         pass
# class car(vehical):
#     def move(self):
#         print("Car drives on road")
# class boat(vehical):
#     def move(self):
#         print("Boat sails on water")
# vehical = [car(),boat()]
# for vehicl in vehical:
#     vehicl.move()

# Q4. Device Multiple Inheritance
# Problem: Create two parent classes:
# ● Camera → method capture()
# ● Phone → method call()
# Create a child class Smartphone that inherits from both and has its own method
# browse(). Create an object of Smartphone and call all three methods.

# class problem:
#     def browse(self):
#         pass
# class camera:
#     def capture(self):
#         pass
# class phone:
#     def call(self):
#         pass
# class smartphone(problem,camera,phone):
#     def browse(self):
#         print("Smartphone is browsing")
# smartphone = smartphone()
# smartphone.browse()
# smartphone.capture()
# smartphone.call()
# smartphone.display()

# Q5. Result Calculation (Multilevel + Overriding)
# Problem: Create classes:
# ● Student → attributes: name, roll_no
# ● Marks → inherits from Student, adds marks in 3 subjects
# ● Result → inherits from Marks, calculates total and average

# Override the display() method in Result to show complete details.

# class student:
#     def feature(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no

# class marks(student):
#     def feature(self, name, roll_no, mark_1, mark_2, mark_3):
#         super().feature(name, roll_no)   
#         self.mark_1 = mark_1
#         self.mark_2 = mark_2
#         self.mark_3 = mark_3

# class result(marks):
#     def feature(self, name, roll_no, mark_1, mark_2, mark_3):
#         super().feature(name, roll_no, mark_1, mark_2, mark_3)
#         self.total = mark_1 + mark_2 + mark_3
#         self.average = self.total / 3

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Roll No: {self.roll_no}")
#         print(f"Marks in Subject 1: {self.mark_1}")
#         print(f"Marks in Subject 2: {self.mark_2}")
#         print(f"Marks in Subject 3: {self.mark_3}")
#         print(f"Total Marks: {self.total}")
#         print(f"Average Marks: {self.average:.2f}")

# c1 = result()
# c1.feature("Vedang", 20, 80, 90, 75)
# c1.display()

# Q6. Shape Area (Polymorphism using Overriding)
# Problem: Create a base class Shape with a method area(). Make subclasses Circle,
# Rectangle, and Triangle that each override area() to compute and print their
# respective areas.

# class Shape:
#     def area(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         print(f"Area of rectangle is {self.length * self.breadth}")


# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         print(f"Area of triangle is {0.5 * self.base * self.height}")


# # Create objects with actual values
# shapes = [Rectangle(5, 10), Triangle(6, 8)]

# # Call area() for each shape
# for sh in shapes:
#     sh.area()

# Q7. Bank Account (Multiple Classes + Method Overriding)
# Problem: Create a base class Account with attributes name and balance, and methods
# deposit() and withdraw(). Create two subclasses:
# ● SavingsAccount → adds interest_rate and a method add_interest()
# ● CurrentAccount → adds overdraft_limit
# Override the withdraw() method in both subclasses with different rules.

# class account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#     def withdraw(self, amount):
#         if self.balance < amount:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
# class savingaccount(account):
#     def __init__(self, name, balance, interest_rate):
#         super().__init__(name, balance)
#         self.interest_rate = interest_rate
#     def add_interest(self):
#         self.balance += self.balance * self.interest_rate / 100
# class currentAccount(savingaccount):
#     def __init__(self, name, balance, overdraft_limit):
#         super().__init__(name, balance)
#         self.overdraft_limit = overdraft_limit
#     def withdraw(self, amount):
#         if self.balance - amount < -self.overdraft_limit:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print(f"₹{amount} withdrawn. Remaining balance: ₹{self.balance}")

# savings = SavingsAccount("Vedang", 5000, 0.04)
# savings.deposit(2000)
# savings.add_interest()
# savings.withdraw(8000)
# savings.withdraw(1000)

# print("\n---")

# current = CurrentAccount("Sharma", 3000, 5000)
# current.withdraw(7000)  # within overdraft
# current.withdraw(9000)  # exceeds overdraft

# Q8. Appliance Demo (Multiple Inheritance + Common
# Method Names)
# Problem: Create two classes:
# ● WashingMachine with method start()
# ● Refrigerator with method start()
# Create a child class HomeAppliance that inherits both. Now, create an object of
# HomeAppliance and call start() to see which one executes (MRO concept).


# class WashingMachine:
#     def start(self):
#         print("Washing Machine started washing clothes.")


# class Refrigerator:
#     def start(self):
#         print("Refrigerator started cooling.")


# class HomeAppliance(WashingMachine, Refrigerator):
#     pass  


# home = HomeAppliance()


# home.start()



