# 4-10. Slices
pizza_names =  ["pepperoni", "buffalo chicken", "creamy mushroom", "hawaiian", "Cheese", "Pineapple"]
for pizza in pizza_names:
 #   print(pizza)
    print(f"I like {pizza.title()} pizza.")

print("I really love pizza!")

#-------------------------------------------------------------------------
#Slicing the list
print("\nThe first three items are:")
print(pizza_names[:3])

print("\nThree items from the middle of the list are:")
print(pizza_names[2:5])

print("\nThe last three items in the list are:")
print(pizza_names[-3:])