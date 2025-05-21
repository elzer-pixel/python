# # CREATING A SIMPLE DICTIONARY:
# # A collection of a key-value pairs
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])

# # WORKING WITH DICTIONARIES:
# # The simplest Dictionary has one key-value pair,
# alien_0 = {"color": "green"}

# # ACCESSING VALUES IN A DICTIONARY:
# print(alien_0['color']) # give name of dictionary, key inside square brackets gives you the value

# # In a game say a player shoots down an alien, you can look up how many points they earn:
# alien_0 = {"color": "green", "points": 5} # Alien with a certain number of points
# new_points = alien_0['points'] # Accessing points and assigned to a variable
# print(f"You just earned {new_points} points!") # printing out the results

# # ADDING NEW KEY-VALUE PAIRS:
# print(alien_0)

# alien_0["x_position"] = 0 #give disctionary name, new key inside square brackets, then add the value using the assignment operator
# alien_0["y_position"] = 25 

# print(alien_0)

# # STARTING WITH AN EMPTY DICTIONARY
# alien_0 = {} # An empty dictionary
# print(alien_0) #Printing the empty Dictionary to see results

# alien_0['color'] = "green" # Adding key-value pair on it's own line
# alien_0['points'] = 5

# print(alien_0) #Printing the dictionary to see the added key-value pairs

# # MODIFYING VALUES IN A DICTIONARY
# alien_0 = {"color": "green"} 
# print(f"The alien is {alien_0['color']}.")
# # To modify: Give the name of the dictionary, with the key in square brackets and then the new value
# alien_0["color"] = "yellow"
# print(f"The alien is now {alien_0['color']}.")

# # A more interesting example: (dictionary with position, speed)
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")

# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alien.
#     x_increment = 3

# # The new posittion is the old position plus the increment.
# alien_0["x_position"] = alien_0["x_position"] + x_increment
# print(f"New position is {alien_0['x_position']}.")

# # REMOVING KEY-VALUE PAIRS
# # Use the del statement
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points'] # del statement, the dictionary name, with the key in square brackets
# print(alien_0) # See the results

# # NESTING
# # Creating a number of dictionaries
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2] #Nesting dictionaries inside a list

# for alien in aliens: # Looping through the list to access the dictionaries
#     print(alien)

# A realistic example:
# # Make an empty list for storing aliens.
# aliens = []

# # Make 30 green aliens.
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# # Show the first 5 aliens.
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# # Show how many aliens have been created.
# print(f"Total number of aliens: {len(aliens)}")

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# first three aliens to yellow, medium-speed aliens worth 10 points each,
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")