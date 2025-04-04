# Using variables in strings
first_name = "ada"
last_name = "lovelace"

#  f-strings or formatted strings
full_name = f"{first_name} {last_name}" # placing the letter 'f' immediately before the string quotation marks.
print(full_name)

print(f"Hello, {full_name.title()}!") # f-string with a title method on a variable, to display a message.

# Assigning the formatted message to a variable:
message = f"Hello, {full_name.title()}!"
print(message)

# Adding whitespace to strings with Tabs or Newlines
print("Python")
print("\tPython") # adding a tab
print("Languages:\nPython\nC\nJavascript") # adding new lines
print("Languages:\n\tPython\n\tC\n\tJavascript") #adding new lines and tabs


#Stripping whitespace
favorite_language = "Python "
favorite_language.rstrip() #calling the strip method to remove the space on the right.
# Strip Methods [ left space - lstrip(), right space - rstrip(), both sides - strip() ]

# Removing Prefixes
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://')) # the method removes the prefix, but doesn't affect the original variable.
print(nostarch_url)

simple_url = nostarch_url.removeprefix('https://') # storing the return of the method to a new variable
print(simple_url)


