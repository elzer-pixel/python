# Checking Whether a Value is Not in a List

banned_users = ['andrew', 'carolina', 'david']

user = 'marie' 
# checking if marie is banned/ if she is in the list
if user not in banned_users: 
    print(f"{user.title()}, you can post a response if you wish.")