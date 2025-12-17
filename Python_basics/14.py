# INCAPSTIALIZATION
# core oop concept that bundling data and methods that operate on that data into a single unit

# there are three attributes into the Encapsulation
# Access attributes:
#     1. Public attributes
#     2. Private attributes
#     3. Protected attributes

# class student:
#     def __init__(self,name,marks):
#         self.name = name
        # PRIVATE
        # self.__marks = marks
    # GETTER
    # def show(self):
        # HERE WE'RE ACCESSING THE PRIVATE ATTRIBUTE
        # return self.__marks
#     # SETTER
#     def set_marks(self,marks):
#         self.__marks = marks

# s1 = student("Vedant",80)
# print(s1.show())
    
    
# Q1. Basic Encapsulation
# Problem: Create a class Student with private attributes name and marks. Provide
# methods to set and get the values of these attributes. Show how data hiding works by
# trying to access private attributes directly.    

# class student:
#     def __init__(self,name,marks):
#         self.__name = name
#         self.__marks = marks
#     def set_name(self,name):
#         self.__name = name
#     def show(self):
#         return self.__name
    
# s1 = student("Vedant",80)
# print(s1.show())

# Q2. Bank Account
# Problem: Create a class BankAccount with:
# ● Public attribute: account_holder
# ● Private attribute: __balance
# Include methods to deposit and withdraw money safely (no negative deposits or
# overdrafts). Demonstrate data protection by using getter and setter methods for balance.

# class bankaccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder = account_holder
#         self.__balance = balance
    
#     # GETTER
#     def show(self):
#         return self.__balance
    
#     # SETTER
#     def set_balance(self,balance):
#         self.__balance = balance
    
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"You have successfully deposited the {amount}")
#             print(f"Your balance is {self.__balance}")
#         else:
#             print("Invalid amount")
#     def withdraw(self,amount):
#         if amount < self.__balance:
#             self.__balance -= amount
#             print(f"You have successfully withdrawn the {amount}")
#             print(f"Your balance is {self.__balance}")
#         else:
#             print("Invalid amount")
# s1 = bankaccount("Vedant",13000)
# print(s1.show())    

# Q3. Employee Data
# Problem: Create a class Employee with private attributes: __name, __salary. Provide
# methods:
# ● set_salary() → sets salary (salary should be > 0)
# ● get_salary() → returns salary

# class employee:
#     def __init__(self,name,salary):
#         self.__name = name
#         self.__salary = salary
#     def set_salary(self,salary):
#         if salary > 0:
#             self.__salary = salary
#         else:
#             print("Invalid salary")
#     def get_salary(self):
#         return self.__salary
    
# s1 = employee("Vedang",13000)
# print(s1.get_salary())
    
# Q4. Product Inventory
# Problem: Create a class Product with private attributes: __name, __price, and
# __quantity. Add:
# ● Getter and setter methods for all attributes.

# class product:
#     def __init__(self,name,price,quantity):
#         self.__name = name
#         self.__price = price
#         self.__quantity = quantity
    
    # GETTER
    # def get_name(self):
    #     return self.__name
    # def get_price(self):
    #     return self.__price
    # def get_quantity(self):
    #     return self.__quantity
    
#     # SETTER
#     def set_name(self,name):
#         self.__name = name
#     def set_price(self,price):
#         self.__price = price
#     def set_quantity(self,quantity):
#         self.__quantity = quantity
        
# s1 = product("Apple",100,10)
# print(s1.get_name())
# print(s1.get_price())
# print(s1.get_quantity())
    
# Q5. Library Book System
# Problem: Create a class Book with:
# ● Private attributes: __title, __author, __available_copies
# ● Public methods:
# ○ borrow_book() → reduces available copies
# ○ return_book() → increases available copies

# Ensure no one can directly modify the number of copies from outside the class.

# class book:
#     def __init__(self,title,author,available_copies):
#         self.__title = title
#         self.__author = author
#         self.__available_copies = available_copies
    
#     def borrow_book(self):
#         if self.__available_copies > 0:
#             self.__available_copies -= 1
#             print("Book borrowed successfully")
#         else:
#             print("No copies available")
#     def return_book(self):
#         self.__available_copies += 1
#         print("Book returned successfully")
        
#     def display_info (self):
#         print(f"Title: {self.__title}")
#         print(f"Author: {self.__author}")
#         print(f"Available Copies: {self.__available_copies}")

# s1 = book("Python","Guido van Rossum",6)
# s1.display_info()


# Q6. Protected Attribute Use
# Problem: Create a parent class Vehicle with protected attribute _speed. Create a
# subclass Car that can access and modify _speed. Demonstrate how protected members
# are used within subclasses but not meant for direct access outside.

# class vehicle:
#     def __init__(self,speed):
#         self._speed = speed
# class car(vehicle):
#     def __init__(self,speed):
#         super().__init__(speed)
#     def display_speed(self):
#         print(f"Speed: {self._speed}")
        
#     def show_speed(self):
#         print(f"Speed: {self._speed}")
    
# class member(car):
#     def __init__(self,speed):
#         super().__init__(speed)
#     def display_speed(self):
#         print(f"Speed: {self._speed}")
    
# s1 = member(120)
# s1.show_speed()
        
# Q7. Encapsulation with Validation
# Problem: Create a class UserAccount with private attributes: __username, __password.
# Use setters to validate:
# ● Username must be at least 4 characters.
# ● Password must contain a number and a special character.
# If invalid, display a message "Invalid username or password".        

# class UserAccount:
#     def __init__(self, username, password):
#         self.__username = username
#         self.__password = password

#         if len(self.__username) < 4:
#             print("Invalid username")
#         elif len(self.__password) < 4:
#             print("Invalid password")
#         else:
#             print("Valid username and password")

#     def display_info(self):
#         print("User Account Information:")
#         print(f"Username: {self.__username}")
#         print(f"Password: {self.__password}")

# # Example
# user1 = UserAccount("vedang", "1234")
# user1.display_info()

# Q8. Real-life Example
# Problem: Create a class ATM that has:
# ● Private attributes: __pin, __balance
# ● Methods to:
# ○ check_pin(pin)
# ○ withdraw(amount, pin)
# ○ deposit(amount, pin)

# Ensure all transactions are allowed only after correct PIN verification.        

# class ATM:
#     def __init__(self,pin,balance):
#         self.__pin = pin
#         self.__balance = balance
    
#     def withdraw(self,amount,pin):
#         if pin == self.__pin:
#             if amount <= self.__balance:
#                 self.__balance -= amount
#                 print(f"Withdrawn: {amount}")
#             else:
        #         print("Insufficient balance")
        # else:
#             print("Invalid PIN")
#     def deposit(self,amount,pin):
#         if pin == self.__pin:
#             self.__balance += amount
#             print(f"Deposited: {amount}")
#         else:
#             print("Invalid PIN")
            
#     def display_info(self):
#         print(f"PIN: {self.__pin}")
#         print(f"Balance: {self.__balance}")
        
# atm1 = ATM(pin=1234, balance=10000)
# atm1.withdraw(2000, 1234)
# # deposit(5000,1234)
# atm1.display_info()  

# class vehical:
#     def start(self):
#         print("Vehical started")
#     def stop(self):
#         print("Vehical stopped")
        
# class car(vehical):
#     pass
#     # def start(self):
#     #     print("Car started")
#     # def stop(self):
#     #     print("Car stopped")
# car1 = car()
# car1.start()
# car1.stop() 

# class singer:
#     def __init__(self,num_song,genere,album_experience):
#         self.num_song = num_song
#         self.genere = genere
#         self.album_experience = album_experience    
# class teacher(singer):
#     def __init__(self, num_song, genere, album_experience,yr_exp,qualification):
#         super().__init__(num_song,genere,album_experience)
#         self.yr_exp = yr_exp
#         self.qualification = qualification
# class person(teacher):
#     def __init__(self, num_song, genere, album_experience,yr_exp,qualification,name,age,gender):
#         super().__init__(num_song,genere,album_experience,yr_exp,qualification)
#         self.name = name
#         self.age = age
#         self.gender = gender
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Gender: {self.gender}")
#         print(f"Number of Songs: {self.num_song}")
#         print(f"Genere: {self.genere}")
#         print(f"Album Experience: {self.album_experience}")
#         print(f"Years of Experience: {self.yr_exp}")
#         print(f"Qualification: {self.qualification}")
        
# q1 = person(num_song=100,genere="Pop",album_experience="5 years",
#             yr_exp=10, qualification="M.A in Music",
#             name="Arijit Singh", age=35, gender="Male")

# q1.display_info
# print(q1.name)

# BANK MANAGMENT SYSTEM
# withdraw , balance , deposit  -> private attributes
# getter and setter
    
# class bank:
#     def __init__(self,name,balance):
#         self.name = name
#         self.__balance = balance
#     # GETTER
#     def display_info(self):
#         print(f"The balance is : {self.__balance}")
        
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance += amount
#             print(f"Deposited: {amount}")
#         else:
#             print("Invalid amount")
#             self.__balance += amount
#             self.display_bal()
    # WITHDRAW THE BALANCE
#     def withdraw(self,amount):
#         if amount < self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawn: {amount}")
#         else:
#             print("Insufficient balance")
            
            
# acc1 = bank(name="vedang",balance=10000)
# acc1.display_info()
    
# class vehical -> start , stop -> car,jeep,bike    
   
class vehical:
    def start(self):
        print("Vehical started")
    def stop(self):
        print("Vehical stopped")

    