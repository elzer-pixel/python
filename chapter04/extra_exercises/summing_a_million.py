# 4-5. Summing a Million: 
one_million = list(range(1, 1000001)) # Creating a list from one to one million
print(min(one_million)) # returns the minimum/lowest value in the list
print(max(one_million)) # returns the maximun/ highest value in the list
print(sum(one_million)) # Sums up the values of the list

print(f"\nHere are the first and last items in the list using the index method:")
print(one_million[0])
print(one_million[-1])