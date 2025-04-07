#Looping through an entire list:

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

# Doing more work within a for loop:
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wat to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!") #Doing something after a for loop

# # Avoiding indentation Errors : Forgetting to indent:
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
# print(magician) #IndentationError

# # Forgetting to indent additional lines
# magicians = ["alice", "david", "carolina"]
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
# print(f"I can't wat to see your next trick, {magician.title()}.\n") # This is a logical Error

# #Indenting Unnecessarily after a for loop:
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wat to see your next trick, {magician.title()}.\n")

#     print("Thank you, everyone. That was a great magic show!") # This will be part of the for loop(Logical Error)

