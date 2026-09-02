# Numpy Easy Use in Python

import Numpy as np # Import the numpy to use numpy features

# 1. Array Creation 

arr1 = np.array([1, 2, 3, 4, 5, 6]) # 1D Array

arr2 = np.array([   
  [1, 2, 3],
  [4, 5, 6]
])  # 2D Array 

# ARRAY INFORMATION

print("Array Shape : ", arr.shape)
print("Dimentions : ", arr.ndim)
print("Size : ", arr.size)
print("Data Types : ", arr.dtypes)

# 3. Special Array 

zeros = np.zeros((2, 3))
print(zeros)

ones = np.ones((2, 2))
print(ones)

identity = np.eye(3)
print(identity)

# 4. Arrange & LinSpace

a = np.arrange(1, 11)
print("Arrange : ", a)

b = np.linspace(0, 10, 5)
print("LinSpace : ", b)

# 5. Random Values 

np.random.seed(42)

rand1 = np.random.rand(3, 3)
print(rand1)

rand2 = np.random.randint(1, 100, (3, 3))
print(rand2)

# 6. RESHAPE & FLATTEN

arr = np.arrange(1, 13)

reshaped = np.reshape(3, 4)

print(reshaped)
print(reshaped.flatten())

#7. INDEXING & SLICING

print("First Element :", arr[0])
print("Second Element : ", arr[1])
print("Last Element : ", arr[-1])

print("Slice : ", arr1[1:4]) # Output -> second to the elements 
print("2D Array :", arr2[2, 4]) 

# 8. ARRAY OPERATIONS

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("Addition : ", x + y)
print("Substraction : ", x - y)
print("Multiplication : ", x*y)
print("Division :", x / y)

# 9. BRODCASTING

print( x + 10)

# 10 STASTICAL FUNCTIONS  

print(X.shape)

print("Sum:", np.sum(nums))
print("Mean:", np.mean(nums))
print("Median:", np.median(nums))
print("Max:", np.max(nums))
print("Min:", np.min(nums))
print("Standard Deviation:", np.std(nums))


#. 11 AXIS CONCEPT

print("\n===== AXIS CONCEPT =====")

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nColumn Wise Sum (axis=0):")
print(matrix.sum(axis=0))

print("\nRow Wise Sum (axis=1):")
print(matrix.sum(axis=1))

# 12 . BOOLIEAN MASKING 

print("\n===== BOOLEAN MASKING =====")

arr = np.array([1, 2, 3, 4, 5, 6])

print(arr > 3)

print("Filtered Values:")
print(arr[arr > 3])

# 13. COPY VS VIEW

original = np.array([1, 2, 3])

view_arr = original.view()
view_arr[0] = 100

print("Original after View Change:")
print(original)

original2 = np.array([1, 2, 3])

copy_arr = original2.copy()
copy_arr[0] = 999

print("Original after Copy Change:")
print(original2)

# 14. SORTING & UNIQUE

arr = np.array([5, 2, 8, 1, 2, 5])

print("Sorted Array:")
print(np.sort(arr))

print("Unique Values:")
print(np.unique(arr))

# 15. STACKING & CONCATENATE

a = np.array([1, 2])
b = np.array([3, 4])

print("\nVertical Stack:")
print(np.vstack((a, b)))

print("\nHorizontal Stack:")
print(np.hstack((a, b)))

print("\nConcatenate:")
print(np.concatenate((a, b)))

# 16. MATRIX MULTIPLICATION

m1 = np.array([
    [1, 2],
    [3, 4]
])

m2 = np.array([
    [5, 6],
    [7, 8]
])

print(np.dot(m1, m2))

# 17.  TRANSPOSE

print(m1.T)

# 18. NAN VALUES

arr = np.array([1, 2, np.nan, 4])

print("NaN Check:")
print(np.isnan(arr))

arr[np.isnan(arr)] = 0

# 19 CONDITIONALS OPERATORS 

print("After Replacing NaN:")
print(arr)
numbers = np.array([10, 15, 20, 25, 30])

result = np.where(numbers > 20, "High", "Low")

print(result)

# 20 ITERATING ARRAY

for value in arr1:
    print(value)

# 21 SAVE AND ITERATING ARRAY 

print("\n===== SAVE & LOAD =====")

np.save("my_array.npy", arr1)

loaded = np.load("my_array.npy")

print("Loaded Array:")
print(loaded)

# 22 REAL MACHINE LEARNING STYLE EXAMPLE

data = np.array([
    [22, 50000],
    [25, 60000],
    [30, 80000],
    [35, 90000]
])

print("\nDataset:")
print(data)

