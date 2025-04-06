#3-8. Seeing the World: five places in the world to visit

places_to_visit = ['ibiza', 'niagara falls', 'bora bora', 'uluru', 'petra']
print("Here is a list of places, unordered, that I would like to visit:")
print(places_to_visit) #Prints the list to the terminal

print("\nHere is a sorted list, using the sorted method:")
print(sorted(places_to_visit))

print("\nHere is the original list:")
print(places_to_visit)

print("\nHere is a sorted list in reverse order:")
print(sorted(places_to_visit, reverse=True))

print("\nHere is the original list again unchanged by the sorted and reverse argument:")
print(places_to_visit)

places_to_visit.reverse()
print("\nHere is the list in reverse order, using the reverse method:")
print(places_to_visit)

places_to_visit.reverse()
print("\nHere is the list back to it's original order, after using the reverse method again:")
print(places_to_visit)

places_to_visit.sort()
print("\nHere the list is sorted alphabetically using the sort method:")
print(places_to_visit)

places_to_visit.sort(reverse=True)
print("\nHere the list is sorted and stored in reverse order:")
print(places_to_visit)
