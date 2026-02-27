# If languages of two friends are same; what will happen to the program in question 6?
d = {}
for i in range(4):
    name = input("enter your name: ")
    language = input("enter your favorite language: ")
    d.update({name: language})
print(d)
# If languages of two friends are same,  no problem
# The dictionary will simply store the same value for different keys (names of friends)