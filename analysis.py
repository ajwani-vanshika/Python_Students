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

print("Average Marks for Each Course:")
print(df.groupby("Course")["Marks"].mean())

print("\nStudents Scoring More than 85 Marks:")
print(df[df["Marks"]>85])

highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()
print("\nHighest Marks:",highest_marks)
print("\nLowest Marks", lowest_marks)

print("\nNumber of Students in Each Course:")
print(df["Course"].value_counts())

import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Names vs Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()