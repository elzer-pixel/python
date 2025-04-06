# Sorting lists permanently with the sort() method
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

#Sorting a list alphabetically, and then in reverse order.
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

#Sorting a list temporarily with the sorted() function:
cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("\nHere is the sorted list in reverse order:")
print(sorted(cars, reverse=True))

print("\nHere is the original list again, unaffected by the sorted and reverse=True argument:")
print(cars)

#Printing a list in reverse order(Using the reverse method):
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

cars.reverse() #it reverses the order of the list permanently
print(cars)
cars.reverse() #reverts to the original order
print(cars)


#Finding the length of a list
print(len(cars))