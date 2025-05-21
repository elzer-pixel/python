# def greet_user():
#     """Display a simple greeting."""
#     print("Hello")

# greet_user()


#passing information as a parametr
# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")

# greet_user('Jada')



#Using a function with a while loop
#This is an infinite loop!

while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")