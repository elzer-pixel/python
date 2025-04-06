#Modifying elements in a list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

#Adding Elements to a List
motorcycles.append('honda') # adding honda to the end of the list
print(motorcycles)

# Building a list dynamically using the append method
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print("\nList items added dynamically using the append method")
print(motorcycles)

#Inserting Elements into a List
motorcycles.insert(0, 'ducati') #Adds the new element at index 0 in the list
print(motorcycles)

#Removing Elements from a List
del motorcycles[0] # The del statement uses the index number to remove a list item at index 0
print(motorcycles)

del motorcycles[0] # removes item "honda" at index 0
print(motorcycles)

#You can remove an item from any position in a  list usiing the del statement if you know it's index.
motorcycles = ["honda", "yamaha", "suzuki"]
del motorcycles[1] # removes 'yamaha' from the list
print(motorcycles)

#Removing an item using the pop() method
motorcycles = ["honda", "yamaha", "suzuki"]
print(f"\nHere is the complete list:\n{motorcycles}\n")

popped_motorcycle = motorcycles.pop() # removes item from end of list and stores it in a new variable.
print(motorcycles)
print(popped_motorcycle)

# Another example of the application of the pop() method.
motorcycles = ["honda", "yamaha", "suzuki"]

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Removing items from a list using the pop() method and the index number.
motorcycles = ["honda", "yamaha", "suzuki"]

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was {first_owned.title()}.")

# Removing item by value using the remove() method:
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# removing the item and printing a reason for removing it
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


# #This statemet will return an Index error:
# #print(motorcycles[3])

# #This prints out the last item on the list
# print(motorcycles[-1])

# #This returns an Index error, since the list is empty
# motorcycles = []
# #print(motorcycles[-1])