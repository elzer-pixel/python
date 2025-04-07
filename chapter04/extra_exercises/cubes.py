# 4-8. Cubes
cubes = [] # Creates an empty list

# The for loop generates the values of cubes and adds them to the list
for values in range(1,11):
    value = values ** 3
    cubes.append(value)

print(cubes)

# for loop that prints out the values
for each_cube in cubes:
    print(each_cube)