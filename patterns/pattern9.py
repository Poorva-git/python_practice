# inverted pyramid
rows = 5

for i in range(rows):
    print(" " * i, end="")
    print("*" * (2 * (rows - i) - 1))