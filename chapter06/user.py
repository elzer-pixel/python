# LOOPING THROUGH ALL KEY-VALUE PAIRS
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
# Creating a for statement to loop through the key-value pairs
# - create names for the two variables
# - The second half is the name of the dictionary, followed by the method item()
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")