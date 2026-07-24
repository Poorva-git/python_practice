# Tuple Example

fruits = ("Apple", "Banana", "Mango", "Orange", "Banana")

print("Original Tuple:")
print(fruits)

# Accessing elements
print("\nFirst Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Length of tuple
print("\nLength:", len(fruits))

# Count occurrences
print("\nBanana appears", fruits.count("Banana"), "times")

# Find index
print("Index of Mango:", fruits.index("Mango"))

# Loop through tuple
print("\nTuple Elements:")
for item in fruits:
    print(item)

# Membership test
search = input("\nEnter a fruit to search: ")

if search in fruits:
    print(search, "is present in the tuple.")
else:
    print(search, "is not present.")

# Convert tuple to list
fruit_list = list(fruits)
fruit_list.append("Grapes")

print("\nAfter Adding Grapes:")
print(fruit_list)

# Convert list back to tuple
fruits = tuple(fruit_list)

print("\nUpdated Tuple:")
print(fruits)
