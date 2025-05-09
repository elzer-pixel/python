# Checking for Inequality
requested_topping = 'mushrooms'
# if requested topping is not equals to anchovies then don't put them on.
if requested_topping != 'anchovies':
    print("Hold the anchovies")


# Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

#the code would not work properly in an if-elif-else block, because it will stop running after the first passed conditional test:
#The code would look like this:
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.") # Mushrooms would be added, and the other toppings will not
elif 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


#Using if Statements with Lists
#Checking for special items
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")

# If the pizzeria runs out of green peppers. An if statement inside the for loop can handle the situation.
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza")

#Checking that a list is not Empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza.")
else:
    print("Are you sure you want a plain pizza?")

#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")