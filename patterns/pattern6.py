# butterfly pattern
rows = 5

# Upper Part
for i in range(1, rows + 1):
    print("*" * i, end="")
    print(" " * (2 * (rows - i)), end="")
    print("*" * i)

# Lower Part
for i in range(rows - 1, 0, -1):
    print("*" * i, end="")
    print(" " * (2 * (rows - i)), end="")
    print("*" * i)