import pandas as pd

df = pd.read_csv("amazon.csv")
print(df)

# 2. Check if there are missing values are or not ? If there are then handle missing values . 
df.isnull().sum()
df
