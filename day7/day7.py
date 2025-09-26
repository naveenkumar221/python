# 1. Right-Angled Triangle (Stars)

for i in range(1, 5):
    print("*" * i)

# 2. Right-Angled Triangle (Numbers)

for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end="")
    print()

# 3. Reverse Right-Angled Triangle

for i in range(5, 0, -1):
    print("*" * i)

# 4. Triangle with Same Number Repeated

for i in range(1, 6):
    print(str(i) * i)

# 5. Number Pyramid

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

