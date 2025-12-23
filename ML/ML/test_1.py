# import pandas as pd

# df = pd.read_csv('covid_toy.csv')

# pd = df.head(5)
# print(pd) 

# 1. Separate categorical columns and Numerical columns . When you have separate 
# categorical data then you have to replace its sub-categories to numbers i.e. has_covid[yes,no] ---> has_covid[0,1] .
#  df['fever'] = pd.to_numeric(df['fever'], errors='coerce')

# df['fever'].fillna(df['fever'].mean(), inplace=True)


# df.rename(columns = {'age' : 'Age_to', 'gender' : 'Gender_to','has_covid' : 'to_Covid'}, inplace = True)
# df['to_Covid'] = df['to_Covid'].map({'Yes':1, 'No':0})



    # 2. Check if there are missing values are or not ? If there are then handle missing values . 

    # print(df.isnull().sum())
    # df = df.fillna(df.mean(numeric_only=True))

# 3. You have to rename 3 column names of Numerical columns . 
# df.rename(columns = {'age' : 'Age_to', 'gender' : 'Gender_to','has_covid' : 'to_Covid'}, inplace = True)
# print(df)

# 4. You have to filter 15-25 rows with all columns of Categorical  columns . 
# pd = df[df['Age_to'].between(15,25)]
# print(pd)

# 5. You have to check statically view of Nummerical columns . 
# pd = df.describe()
# print(pd)

# 6. You have to export categorical data into csv format and Nummerical data into excel format .

# df['fever'] = pd.to_numeric(df['fever'], errors='coerce')

# df['fever'].fillna(df['fever'].mean(), inplace=True)


# df.rename(columns = {'age' : 'Age_to', 'gender' : 'Gender_to','has_covid' : 'to_Covid'}, inplace = True)
# df['to_Covid'] = df['to_Covid'].map({'Yes':1, 'No':0})


# categorical_cols = ['Gender_to', 'cough', 'city', 'to_Covid']
# numerical_cols = ['Age_to', 'fever']

# categorical_df = df[categorical_cols]
# numerical_df = df[numerical_cols]

# categorical_df.to_csv('categorical_data.csv', index=False)
# numerical_df.to_excel('numerical_data.xlsx', index=False)

# 7. In your Numerical data , you have to arrange data in ascending order using a single column .

# pd = df.sort_values(by = 'Age_to')
# print(pd)
