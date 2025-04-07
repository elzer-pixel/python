# 4-11. My Pizzas, Your pizzas

pizza_names =  ["pepperoni", "buffalo chicken", "creamy mushroom", "hawaiian"]
for pizza in pizza_names:
 #   print(pizza)
    print(f"I like {pizza.title()} pizza.")

print("I really love pizza!")


# Copying a list and storing it in the my 'friend_pizzas'
friend_pizzas = pizza_names[:]

#Adding new pizzas to the lists
pizza_names.append('cheese') # Adding a pizza to the original
friend_pizzas.append('Pineapple') #adding a pizza to the new list

print("\nMy favorite pizzas are:")
print(pizza_names)

for pizza in friend_pizzas:
    print(pizza)