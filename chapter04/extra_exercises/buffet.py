#4-13. Buffet: 
# Creating a list of basic foods in a tuple
basic_foods = ("pasta", "rice", "salad", "pap", "uphuthu")

#For loop, to print out the foods in the list:
for food in basic_foods:
    print(food)

# #Trying to modify the tuple:
#basic_foods[0] = "samp" # Python returns a TypeError, does not support item assignment

basic_foods = ("pasta", "samp", "salad", "poikie kos", "uphuthu")
print("\nModified tuple with new menu:")
for food in basic_foods:
    print(food)