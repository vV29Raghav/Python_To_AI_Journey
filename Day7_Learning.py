
import numpy as np
import time

#CREATING NUMPY ARRAYS
a = np.array([1.9, 2, 3.1])
print("Array:", a)
print("Data type:", a.dtype)

#Specifying the data type
b = np.array([1.9, 2, 3.1], dtype="i")
print("Integer array:", b)
print("Data type:", b.dtype)

# Mixed data types
c = np.array(["a", 2, "str", 87])
print("Mixed array:", c)
print("Array type:", type(c))


#ARRAY DIMENSIONS AND SHAPE
X = np.array([
    [[1.9, 2, 3.1], [2, 3, 4]],
    [[1, 2, 1], [1, 2, 2]]
])

print("Array:\n", X)
print("Number of dimensions:", X.ndim)
print("Shape:", X.shape)
print("Third dimension size:", X.shape[2])


#CREATING ARRAYS USING arange()
A = np.arange(100)

print("First 10 elements:", A[:10])
print("Element at index 4:", A[4])
print("Element at index -3:", A[-3])


#RESHAPING ARRAYS
arr = np.arange(10)
reshaped = arr.reshape(2, 5)

print("Original array:", arr)
print("Reshaped array:\n", reshaped)


#ARRAY INDEXING AND MODIFYING
A = np.arange(100)

A[4] = -1200
A[92] = -1200

print("Updated values:", A[4], A[92])

# Access multiple elements using fancy indexing
print("Selected elements:", A[[1, 8, 1]])


#BOOLEAN INDEXING AND FILTERING

C = np.argwhere(A == -1200)

print("Positions of -1200:", C)

# Find the first matching position
if len(C) > 0:
    print("First matching position:", C[0][0])

# Boolean condition
B = (A == -1200) * np.arange(A.size)

print("Filtered index values:", B[B != 0])


#MULTIDIMENSIONAL ARRAYS
M = np.random.rand(3, 3)
N = np.random.rand(3, 3)

print("Matrix M:\n", M)
print("Matrix N:\n", N)

J = M + N
print("Addition of matrices:\n", J)

#Random 3D array
random_array = np.random.rand(2, 3, 5)
print("3D array shape:", random_array.shape)


#RANDOM NUMBER GENERATION
print("\n=== 8. RANDOM NUMBERS ===")

random_numbers = np.random.rand(5)
print("Random numbers:", random_numbers)


#NUMPY PERFORMANCE COMPARISON

data = np.random.rand(10000)

# Python built-in sum
start = time.perf_counter()
python_sum = sum(data)
python_time = time.perf_counter() - start

# NumPy sum
start = time.perf_counter()
numpy_sum = np.sum(data)
numpy_time = time.perf_counter() - start

print("Python sum:", python_sum)
print("NumPy sum:", numpy_sum)

print(f"Python sum time: {python_time:.6f} seconds")
print(f"NumPy sum time: {numpy_time:.6f} seconds")


