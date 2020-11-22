"""
Udemy "Interactive Python Dashboards with Plotly and Dash Course
10/25/2020
"""

import numpy as np

# NumPy crash course.


mylist = [1, 2, 3, 4, 5, 6, 7]

print(np.array(mylist))
print(type(mylist))

# makes an array out of a list.
arr = np.array(mylist)
print(arr)
print(type(arr))

a = np.arange(0, 10)
print(a)

# range of numbers with a step of 2.
b = np.arange(0, 20, 2)
print(b)

# matrix or grid array of numbers.
# pass a tuple (5,5).

print(np.zeros((5,5)))

print(np.ones((3,5)))

# produces floating point numbers.
print(type(1.0))
print(type(1.))

# create a random array of integers.
print(np.random.randint(0,100))
# use tuple to make grid (7,7)
print(np.random.randint(0,100,(7,7)))

# array of numbers evenly spaced from 0 to 10, third number is how many spaces.
print(np.linspace(0,10,6))
print(np.linspace(0,10,101))
print(np.linspace(0,10,201))

# set random.seed() to get exact same random numbers each time or as another user.
np.random.seed(101)
print(np.random.randint(0,100,10))

# produce random array of 10 numbers between 0 and 200.
array = np.random.randint(0,200,10)
print(array)
# get data on array.
print(array.max())
print(array.min())
print(array.mean())
# location of max number
print(array.argmax())
print(array.argmin())

# make an array of numbers 0 to 99.
mat = np.arange(0,100)
print(mat)
# reshape into a matrix.
matrix = mat.reshape(10,10)
print(matrix)

# shortcut to above code.
# mat = np.arange(0,100).reshape(10,10)

# get number from matrix. Row then column (zero based index)
print(matrix[5,2])
# get whole column. column 2.
print(matrix[:,2])
# get whole row. row 2.
print(matrix[2,:])

# masking
# boolean values
print(matrix > 50)
# get matrix with only values greater than 50.
print(matrix[matrix>50])


# Pandas Crash Course
import pandas as pd

df = pd.read_csv('salaries.csv')
print(df)

# print just Salary.
print(df['Salary'])

# print two columns using a list. Passing a list into it, hence double brackets.
print(df[['Name','Salary']])

# get data from df. Ex: .min(), .max(), .mean()
print(df['Salary'].mean())

# conditional filtering.
# get boolean values (dtype: bool)
print(df['Age'] > 30)

# using bool to sort out data. Age > 30.
ser_of_bool = df['Age'] > 30
print(df[ser_of_bool])

# above code in one step.
print(df[df['Age'] > 30])

# other methods.
# get unique numbers.
print(df['Age'].unique())
# get number of unique numbers.
print(df['Age'].nunique())
# get columns.
print(df.columns)
# get info about df.
print(df.info())
# get statistical summary.
print(df.describe())
# get index info.
print(df.index)

# Combine numpy and pandas exercise

mat1 = np.arange(0,10).reshape(5,2)
print(mat1)
df1 = pd.DataFrame(data=mat1,columns=['2019','2020'],index=['JAN','FEB','MAR','APR','MAY'])
print(df1)











