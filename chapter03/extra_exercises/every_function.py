#3-10. Every Function:


african_cities =["cape town","lagos","nairobi","kampala","cairo","harare","kigali"]
print(african_cities)

#Removing the city of cape town and printing a message about it
print(f"\n{african_cities.pop(0).title()} is a beautiful city to live in.")
print(african_cities)

#Inserting a new city name to be first on the list
african_cities.insert(0, 'tunis')
print(african_cities)

# Removing the city of kampala from the list
del african_cities[3] 
print(african_cities)
print(len(african_cities))

#Accessing a city from the list using an index number:
print(f"\nThe capital city of Egypt is called {african_cities[3].title()}.\n")

#removing a city at the end of the list:
removed_city = african_cities.pop()
print(african_cities)
print(f"{removed_city.title()} is not my favorite city")

#adding a city to the end of the list using the append method:
african_cities.append('johannesburg')
print("\nAdded a new city with the append method:")
print(african_cities)

#sorting the list in alphabetical order:
print("\nSorting the list in alphabetical order using the sorted method:")
print(sorted(african_cities))

#The original list
print("\nThis is the original list again, unaffected by the sorted method:")
print(african_cities)

#Reversing the order of the list
african_cities.reverse()
print("\nReversing the order of the list")
print(african_cities)

# sorting the list in reverse alphabetical order:
african_cities.sort(reverse=True)
print("\nThe list is ordered in the reverse alphabetical order:")
print(african_cities)

# Listing the cities in alphabetical order:
african_cities.sort()
print("\nHere the list is ordered alphabetically:")
print(african_cities)