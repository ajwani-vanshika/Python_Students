import pandas as pd
import matplotlib as plt

df = pd.read_csv("students.csv")

print("First 5 rows of the dataset :  \n")
#print(df.head())

rows, columns = df.shape

print("\nTotal Rows:", rows)
print("\n Total Columns:", columns)

df =  pd.read_csv("students.csv")

print("Column Names:")
print(df.columns)

print("\n Data Types of Each Column:")
print(df.dtypes)

print("\n Missing Values in Each Column: ")
print(df.isnull().sum())

average_marks = df["Marks"].mean()
print("\nAverage Marks:",average_marks)

df["Marks"].fillna(average_marks,inplace=True)

print("\n Missing Values in Marks after replacement:")
print(df["Marks"].isnull().sum())