# 3-6. More Guests: 

guest_names = ['lucas', 'noma', 'siya']

# Printing a message to each of the people in the list.
print(f"Hello {guest_names[0].title()}, you are invited to dinner at my place tonight.")
print(f"Hello {guest_names[1].title()}, you are invited to dinner at my place tonight.")
print(f"Hello {guest_names[2].title()}, you are invited to dinner at my place tonight.")

print(f"We are saddened that {guest_names[0].title()} will not make to dinner.")

# Replacing the person who won't make it:
guest_names[0] = 'anec'
print(guest_names)

#Printing an invitation message:
print(f"Hello {guest_names[0].title()}, you are invited to dinner at my place tonight.")
print(f"Hello {guest_names[1].title()}, we hope you can still make it to dinner tonight.")
print(f"Hello {guest_names[2].title()}, we hope you can still make it to dinner tonight.")

#Informing people:
print("We are happy to announce we have  bigger table for our dinner")

#Adding new guest to the list using the insert() method
guest_names.insert(0, 'lerato') #Adds guest to the start of the list
print(guest_names)
guest_names.insert(2, 'sfiso') #Adds guest to the middle of the list
print(guest_names)
guest_names.append('lesego') #Adds guest  to the end of the list
print(guest_names) 

#New message to each of the guests
print(f"Good day {guest_names[0].title()}, you are invited to dinner.")
print(f"Good day {guest_names[1].title()}, you are invited to dinner.")
print(f"Good day {guest_names[2].title()}, you are invited to dinner.")
print(f"Good day {guest_names[3].title()}, you are invited to dinner.")
print(f"Good day {guest_names[4].title()}, you are invited to dinner.")
print(f"Good day {guest_names[5].title()}, you are invited to dinner.")

