# Copying a list
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#--------------------------------------------
my_foods.append("cannoli")
friend_foods.append("ice cream")

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#This doesn't work(the new variable references the same place as the old)
#friend_foods = my_foods