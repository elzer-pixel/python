bicycles = ["trek", "cannondale", "redline", "specialized"]
# print(bicycles)

#Accessing Elements in a List (Index positions starts at 0):
print(bicycles[0])

# Using string method on list items.
print(bicycles[0].title())

print(bicycles[1]) # Accessing bycicles at index 1, at position 2 in the list
print(bicycles[2]) # Accessing bycicles at index 3, at position 4 in the list

#Returns 'cannondale' in all caps
print(bicycles[1].upper())

#the negative one (-1) index prints the last element in the list
print(bicycles[-1])

#using individual values from a list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

