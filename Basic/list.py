# Python List Example

numbers = []

# Taking input
n = int(input("How many numbers do you want to enter? "))

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

print("\nOriginal List:", numbers)

# Insert
numbers.insert(1, 100)
print("After insert:", numbers)

# Append
numbers.append(200)
print("After append:", numbers)

# Remove
value = int(input("\nEnter a number to remove: "))

if value in numbers:
    numbers.remove(value)
    print("After remove:", numbers)
else:
    print("Number not found.")

# Pop
numbers.pop()
print("After pop:", numbers)

# Sort
numbers.sort()
print("Sorted List:", numbers)

# Reverse
numbers.reverse()
print("Reversed List:", numbers)

# Length
print("Length of List:", len(numbers))

# Maximum and Minimum
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Sum
print("Sum:", sum(numbers))

# Average
average = sum(numbers) / len(numbers)
print("Average:", average)

# Search
search = int(input("\nEnter number to search: "))

if search in numbers:
    print(search, "is present in the list.")
else:
    print(search, "is not present in the list.")

# Display using loop
print("\nFinal List Elements:")

for item in numbers:
    print(item)
