#working with part of list:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # slicing a list (items one to three)
print(players[1:4]) # index 1 and end it at index 4
print(players[:4]) # omitting the first index python starts at zero
print(players[2:]) # starts at item 3, index 2 to the last item
print(players[-3:]) # the last three items 

# Looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())