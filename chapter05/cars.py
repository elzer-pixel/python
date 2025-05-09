# Creating a list with different car models
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    # Conditional if statement
    if car == "bmw":
        print(car.upper()) # The BMW acronym will be printed in uppercase
    else:
        print(car.title()) # Car names a proper names and printed in title case

# An if Conditional Statement Structure
# (1) "if" keyword, 
# (2) expression that can be evaulated(true or false)/conditional test, 
# (3) the code to be executed if conditional test is true

#Checking for Equality (Double equal sign/ equality operator)

car = "audi"
print("\nThe following checks whether car is equal to 'audi'.")
print(car == "audi")

#Ignoring Case When checking for equality
car = "Audi"
#Checking for equality is case sensitive in Python 
print("\ncar is not equal to 'audi'.")
print(car == "audi") # The code evaluates to False

# If case doesn't matter, you can convert the variable's value to lowercase
print(car.lower() == "audi")
#The lower method doesn't change the value that was originally stored
print(car) 
