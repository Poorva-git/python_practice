# ============================================
# Dictionary Practice in Python
# ============================================

# 1. Create Dictionary

print("\n========== 1. Create Dictionary ==========")

student = {
    "Name": "Riya",
    "Age": 21,
    "Course": "B.Tech",
    "Marks": 89
}

print(student)

# ============================================
# 2. Access Values
# ============================================

print("\n========== 2. Access Values ==========")

print("Name :", student["Name"])
print("Marks :", student["Marks"])

# ============================================
# 3. Using get()
# ============================================

print("\n========== 3. Using get() ==========")

print(student.get("Course"))
print(student.get("City", "Not Found"))

# ============================================
# 4. Add New Item
# ============================================

print("\n========== 4. Add New Item ==========")

student["City"] = "Delhi"

print(student)

# ============================================
# 5. Update Value
# ============================================

print("\n========== 5. Update Value ==========")

student["Marks"] = 95

print(student)

# ============================================
# 6. Remove Item using pop()
# ============================================

print("\n========== 6. Remove Item ==========")

student.pop("Age")

print(student)

# ============================================
# 7. Remove Last Item
# ============================================

print("\n========== 7. Pop Last Item ==========")

student.popitem()

print(student)

# ============================================
# 8. Keys
# ============================================

print("\n========== 8. Keys ==========")

print(student.keys())

# ============================================
# 9. Values
# ============================================

print("\n========== 9. Values ==========")

print(student.values())

# ============================================
# 10. Items
# ============================================

print("\n========== 10. Items ==========")

print(student.items())

# ============================================
# 11. Loop Through Dictionary
# ============================================

print("\n========== 11. Loop ==========")

for key, value in student.items():
    print(key, ":", value)

# ============================================
# 12. Check Key Exists
# ============================================

print("\n========== 12. Check Key ==========")

if "Marks" in student:
    print("Marks Key Exists")
else:
    print("Marks Key Not Found")

# ============================================
# 13. Dictionary Length
# ============================================

print("\n========== 13. Length ==========")

print(len(student))

# ============================================
# 14. Copy Dictionary
# ============================================

print("\n========== 14. Copy ==========")

student_copy = student.copy()

print(student_copy)

# ============================================
# 15. Nested Dictionary
# ============================================

print("\n========== 15. Nested Dictionary ==========")

students = {
    "Student1": {
        "Name": "Aman",
        "Marks": 90
    },
    "Student2": {
        "Name": "Priya",
        "Marks": 85
    }
}

print(students)

print(students["Student1"]["Name"])

# ============================================
# 16. Dictionary from User Input
# ============================================

print("\n========== 16. User Input ==========")

person = {}

name = input("Enter Name: ")
age = int(input("Enter Age: "))

person["Name"] = name
person["Age"] = age

print(person)

# ============================================
# 17. Character Frequency
# ============================================

print("\n========== 17. Character Frequency ==========")

text = input("Enter a String: ")

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print(frequency)

# ============================================
# 18. Word Frequency
# ============================================

print("\n========== 18. Word Frequency ==========")

sentence = input("Enter a Sentence: ")

words = sentence.lower().split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

# ============================================
# 19. Student Marks Dictionary
# ============================================

print("\n========== 19. Student Marks ==========")

marks = {
    "Math": 90,
    "Python": 95,
    "English": 85
}

total = sum(marks.values())
average = total / len(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)

# ============================================
# 20. Dictionary Comprehension
# ============================================

print("\n========== 20. Dictionary Comprehension ==========")

numbers = {x: x*x for x in range(1, 11)}

print(numbers)

print("\n🎉 Dictionary Practice Completed Successfully!")