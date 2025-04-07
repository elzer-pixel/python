# A list of the first 10 square numbers:

squares = [] # Creating an empty list
for value in range(1, 11): # A list of numbers from 1 - 10
    square = value ** 2 # values to an exponent of 2
    squares.append(square) # storing the square of each value in the list

print(squares)

# The same results but a more concise code:
squares = []
for value in range(1, 11): 
    squares.append(value ** 2)

print(squares)