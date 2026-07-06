# ============================================
# Python String Programs
# ============================================

# 1. Reverse String
print("1. Reverse String")
text = input("Enter a string: ")
print("Reversed String:", text[::-1])

print("-" * 40)

# 2. Palindrome Check
print("2. Palindrome Check")
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

print("-" * 40)

# 3. Count Vowels
print("3. Count Vowels")
text = input("Enter a string: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)

print("-" * 40)

# 4. Count Consonants
print("4. Count Consonants")
text = input("Enter a string: ")

count = 0

for ch in text.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1

print("Number of consonants:", count)

print("-" * 40)

# 5. Count Words
print("5. Count Words")
text = input("Enter a sentence: ")

words = text.split()

print("Total Words:", len(words))

print("-" * 40)

# 6. Count Characters
print("6. Count Characters")
text = input("Enter a string: ")

print("Characters:", len(text))

print("-" * 40)

# 7. Remove Spaces
print("7. Remove Spaces")
text = input("Enter a string: ")

print("Without Spaces:", text.replace(" ", ""))

print("-" * 40)

# 8. Character Frequency
print("8. Character Frequency")
text = input("Enter a string: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)

print("-" * 40)

# 9. Remove Duplicate Characters
print("9. Remove Duplicate Characters")
text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result += ch

print("Result:", result)

print("-" * 40)

# 10. Sort Characters Alphabetically
print("10. Sort Characters")
text = input("Enter a string: ")

sorted_text = "".join(sorted(text))

print("Sorted String:", sorted_text)

print("-" * 40)

print("All String Programs Executed Successfully!")