# If the names of 2 friends are same; what will happen to the program in question 6?

d = {}
for i in range(4):
    name = input("enter your name: ")
    language = input("enter your favorite language: ")
    d.update({name: language})

print(d)
# If the names of 2 friends are same, then the value of the key will be updated with the new value. The previous value will be overwritten and lost.
