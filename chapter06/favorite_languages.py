# DICTIONARY OF SIMILAR OBJECTS

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")


# # Looping through all key-value pairs
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# # LOOPING THROUGH ALL THE KEYS IN A DICTIONARY

# #use the keys() method.
# for name in favorite_languages.keys():
#     print(name.title()) # Printing out the names of everyone who took the poll.

# # Accessing any key inside the loop
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
#     }

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you lave {language}!")


# # You can also use the keys() method to find out if a particular person was polled.
# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# LOOPING THROUGH A DICTIONARY'S KEYS IN A PARTICULAR ORDER
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# LOOPING THROUGH ALL THE VALUES IN A DICTIONARY
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


# TO SEE EACH LANGUAGE CHOSEN WITHOUT REPETITION
# - Use the set()
# - a set is a collection in which each item must be unique
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

