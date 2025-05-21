# USING get() TO ACCESS VALUES

#what happens when you ask for the point value of an alien that doesn’t have a point value
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) 
#This results in a traceback, showing a KeyError

#The get method requires a key as first argument, as second optional argument you can pass the value to be returned.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)