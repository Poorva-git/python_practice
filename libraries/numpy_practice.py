# ===========================
# NumPy Basics
# ===========================

import numpy as np


print("=== Creating Arrays ===")
arr = np.array([10,20,30,40,50,60,70])
print(arr)

print("\n=== Indexing & Slicing ===")
print(arr[1])
print(arr[0:4])

print("\n=== Vectorized Operations ===")
print(arr + 10)
print(arr * 2)
print(arr ** 2)

print("\n=== NumPy Functions ===")
print(arr.sum())
print(arr.mean())
print(arr.min(), arr.max())

print("\n=== Data Cleaning Examples ===")
data = np.array([10, -20, 30, -40, 50])
clean = data[data >= 0]
print("Cleaned:", clean)

marks = np.array([80, 90, -1, 75, -1, 60])
marks[marks== -1]=marks[marks!= -1].mean()  #Replacing Average of non negative values
print("Filled Missing:", marks)

cities = np.array([" mumbai ", "PUNE", "Delhi ", " mUmBaI"])
cities = np.char.strip(cities)
cities = np.char.title(cities)
print(cities)

# more of numpy--
print("\n========== 1. Creating Arrays ==========")

arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr2)

# ===========================
# Array Attributes
# ===========================

print("\n========== 2. Array Attributes ==========")

print("Dimensions:", arr2.ndim)
print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data Type:", arr2.dtype)

# ===========================
# Special Arrays
# ===========================

print("\n========== 3. Special Arrays ==========")

print("\nZeros")
print(np.zeros((3,3)))

print("\nOnes")
print(np.ones((2,4)))

print("\nIdentity Matrix")
print(np.eye(4))

print("\nArange")
print(np.arange(1,11))

print("\nLinspace")
print(np.linspace(0,100,5))

# ===========================
# Reshape
# ===========================

print("\n========== 4. Reshape ==========")

arr = np.arange(12)
print(arr)

print("\nReshaped:")
print(arr.reshape(3,4))

# ===========================
# Indexing
# ===========================

print("\n========== 5. Indexing ==========")

arr = np.array([10,20,30,40,50])

print(arr[0])
print(arr[3])

# ===========================
# Slicing
# ===========================

print("\n========== 6. Slicing ==========")

print(arr[1:4])
print(arr[:3])
print(arr[2:])

# ===========================
# Mathematical Operations
# ===========================

print("\n========== 7. Math Operations ==========")

a = np.array([1,2,3,4])

print("Addition:", a+10)
print("Subtraction:", a-2)
print("Multiplication:", a*5)
print("Division:", a/2)

# ===========================
# Statistics
# ===========================

print("\n========== 8. Statistics ==========")

arr = np.array([10,20,30,40,50])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Standard Deviation:", np.std(arr))

# ===========================
# Random Numbers
# ===========================

print("\n========== 9. Random Numbers ==========")

print(np.random.randint(1,100,10))

print(np.random.rand(5))

# ===========================
# Sorting
# ===========================

print("\n========== 10. Sorting ==========")

arr = np.array([8,2,5,1,9,6])

print(np.sort(arr))

# ===========================
# Matrix Operations
# ===========================

print("\n========== 11. Matrix Operations ==========")

a = np.array([[1,2],[3,4]])

b = np.array([[5,6],[7,8]])

print("\nAddition")
print(a+b)

print("\nSubtraction")
print(a-b)

print("\nElement-wise Multiplication")
print(a*b)

# Matrix Multiplication
print("\nMatrix Multiplication")
print(np.dot(a,b))

# ===========================
# Transpose
# ===========================

print("\n========== 12. Transpose ==========")

print(a.T)

# ===========================
# Concatenate
# ===========================

print("\n========== 13. Concatenate ==========")

x = np.array([1,2,3])
y = np.array([4,5,6])

print(np.concatenate((x,y)))

# ===========================
# Flatten
# ===========================

print("\n========== 14. Flatten ==========")

arr = np.array([[1,2],[3,4]])

print(arr.flatten())

# ===========================
# Unique Values
# ===========================

print("\n========== 15. Unique Values ==========")

arr = np.array([1,2,2,3,4,4,5])

print(np.unique(arr))

# ===========================
# Boolean Indexing
# ===========================

print("\n========== 16. Boolean Indexing ==========")

arr = np.array([10,20,30,40,50])

print(arr[arr>25])

# ===========================
# Copy vs View
# ===========================

print("\n========== 17. Copy vs View ==========")

arr = np.array([1,2,3])

copy_arr = arr.copy()
view_arr = arr.view()

arr[0]=100

print("Original:",arr)
print("Copy:",copy_arr)
print("View:",view_arr)

# ===========================
# Stacking
# ===========================

print("\n========== 18. Stacking ==========")

a=np.array([1,2,3])
b=np.array([4,5,6])

print("\nVertical Stack")
print(np.vstack((a,b)))

print("\nHorizontal Stack")
print(np.hstack((a,b)))

# ===========================
# Splitting
# ===========================

print("\n========== 19. Splitting ==========")

arr=np.array([1,2,3,4,5,6])

print(np.array_split(arr,3))

# ===========================
# End
# ===========================

print("\nNumPy Basics Completed Successfully!")