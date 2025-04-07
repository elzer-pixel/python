# Making numerical lists:
for value in range(1, 5):  # Using python's range fucntion
    print(value)

for value in range(1, 6):  # Another example of the off-by-one behavior
    print(value)

for value in range(6):  # Passing one argument, will start at zero to 1 less the value
    print(value)

# Using range to make a list:
numbers = list(range(1, 6))
print(numbers)