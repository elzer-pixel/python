#3-5. Changing Guest List: 

guest_names = ['lucas', 'noma', 'siya']

# Printing a message to each of the people in the list.
print(f"Hello {guest_names[0].title()}, you are invited to dinner at my place tonight.")
print(f"Hello {guest_names[1].title()}, you are invited to dinner at my place tonight.")
print(f"Hello {guest_names[2].title()}, you are invited to dinner at my place tonight.")

#------------------------------------------------------------------------------------------
print(f"We are saddened that {guest_names[0].title()} will not make to dinner.")

# Replacing the person who won't make it:
guest_names[0] = 'anec'
print(guest_names)

#Printing an invitation message:
print(f"Hello {guest_names[0].title()}, you are invited to dinner at my place tonight.")
print(f"Hello {guest_names[1].title()}, we hope you can still make it to dinner tonight.")
print(f"Hello {guest_names[2].title()}, we hope you can still make it to dinner tonight.")