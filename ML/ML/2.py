# INTRODUCTION TO PANDAS
# pandas is an open source library for the Python programming language, providing data structures and data analysis tools for working with structured data.

# import pandas as pd

# Data Structure of pandas
# (1) Series
# (2) Dataframes

# (1) Series --> It is one dimensional array and it return only values not column name 
# a = pd.Series([1,2,3,4,5,6,7,8,9,10])
# print(a)

# (2) Dataframes --> It is two dimensional array and it return values with column name

# dict = {"Name" : ["Vedant", "Vinit", "Vipul"],
#         "Age" : [21, 22, 23],
#         "City" : ["Mumbai", "Pune", "Nashik"]}

# df = pd.DataFrame(dict)
# print(df)

# HOW CAN WE EXPORT DATAFRAME INTO THE CSV FILE
# df.to_csv("flipkart.csv") 
# df.to_csv("flipkart.csv" , index=False)

# df = pd.read_csv("flipkart.csv")
# print(df)


