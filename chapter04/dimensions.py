# TUPLES

#defining a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#tuples are immutable, a list with values that cannot be change is a tuple
#dimensions[0] =  250 # This throws an error, tuple object does not support item assignment

#Looping through values of a tuple
for dimension in dimensions:
    print(dimension)

#Writing over a tuple, we redefine the entire tuple:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)