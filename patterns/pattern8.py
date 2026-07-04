# diamond pattern
rows = 5

# Upper Part
for i in range(rows):
    print(" " * (rows - i - 1), end="")
    print("*" * (2 * i + 1))

# Lower Part
for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1), end="")
    print("*" * (2 * i + 1))