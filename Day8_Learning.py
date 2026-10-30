
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Series
marks = pd.Series(
    [2, 3, 4, 5],
    index=["a", "b", "c", "d"]
)

print(marks)
print("Value at index 'a':", marks["a"])


# 2. DATAFRAME CREATION
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [22, 25, 20, 24, 21],
    "Marks": [85, 72, 91, 65, 88]
}
df = pd.DataFrame(data)
print(df)


# CREATING DATAFRAME FROM SERIES
student_marks = pd.Series({
    "Alice": 4,
    "Bob": 3,
    "Charlie": 5
})
student_grades = pd.Series({
    "Alice": 5.4,
    "Bob": 2.2,
    "Charlie": 4.8
})
D = pd.DataFrame({
    "Marks": student_marks,
    "Grades": student_grades
})
print(D)
print(D.columns)


#FILTERING DATA
high_marks = df[df["Marks"] > 80]

print("Students scoring above 80:")
print(high_marks)


#READING CSV FILES

df.to_csv("students.csv", index=False)

loaded_df = pd.read_csv("students.csv")

print(loaded_df.head(3))
print(loaded_df.info())


# HANDLING MISSING VALUES

# Create a dataset containing missing values
student_data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Marks": [85, np.nan, 91, np.nan],
    "Age": [22, 25, np.nan, 24]
}

missing_df = pd.DataFrame(student_data)

print("Original data:")
print(missing_df)

print("\nMissing values in each column:")
print(missing_df.isna().sum())

# Fill missing numerical values with 0
filled_df = missing_df.fillna(0)

print("\nAfter filling missing values:")
print(filled_df)


#USING SCIKIT-LEARN SIMPLE IMPUTER
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="mean")

imputed_values = imputer.fit_transform(
    missing_df[["Marks", "Age"]]
)

imputed_df = pd.DataFrame(
    imputed_values,
    columns=["Marks", "Age"]
)

print(imputed_df)


#NUMPY AND PANDAS INTEGRATION
arr = np.arange(30).reshape(6, 5)

print("Original array:")
print(arr)

# Select the second column
x = arr[:, 1]

print("\nSecond column:")
print(x)


#FILTERING AND UPDATING ARRAY VALUES

data = np.array([
    [1, 50, 100],
    [2, 90, 200],
    [3, 75, 300],
    [4, 95, 400]
])

# Find rows where second column is greater than 80
selected_rows = data[data[:, 1] > 80]

print("Rows with values above 80:")
print(selected_rows)

# Increase every value in second column by 5
data[:, 1] = data[:, 1] + 5

print("\nUpdated array:")
print(data)


#DATAFRAME OPERATIONS

print("Average marks:", df["Marks"].mean())
print("Maximum marks:", df["Marks"].max())
print("Minimum marks:", df["Marks"].min())

print("\nSorted by marks:")
print(df.sort_values(by="Marks", ascending=False))


#DATA VISUALIZATION

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x)

plt.figure(figsize=(9, 5))

plt.scatter(x, y, label="Sine")
plt.plot(x, z, label="Cosine")

plt.title("Sine and Cosine Functions")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.grid(True)

plt.show()


#STUDENT MARKS VISUALIZATION
plt.figure(figsize=(8, 5))

plt.bar(df["Name"], df["Marks"])

plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

