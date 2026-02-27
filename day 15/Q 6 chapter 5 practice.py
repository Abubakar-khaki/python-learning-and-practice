#Q 6: Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
d = {}
for i in range(4):
    name = input("enter your name: ")
    language = input("enter your favorite language: ")
    d.update({name: language})
print(d)
# name = input("enter your name: ")
# language = input("enter your favorite language: ")
# d[name] = language
#even this will work same as above code