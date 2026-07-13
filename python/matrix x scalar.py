age = 20
price = 99.99
is_pass = True
name = "Alice"

print(age)
print(price)
print(is_pass)
print(name)

students = [
    [20, 170, 65],
    [21, 168, 60],
    [22, 175, 70]
]

print("Original Matrix:")
for row in students:
    print(row)

print("\nMatrix after multiplying by 2:")

for row in students:
    new_row = []
    for value in row:
        new_row.append(value * 2)
    print(new_row)