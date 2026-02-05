# logical operators and, or, not
# and operator 
print("True and False:", True and False) # True and False = False
print("True and True:", True and True) # True and True = True
print("False and False:", False and False) # False and False = False
# or operator
print("True or False:", True or False) # True or False = True
print("True or True:", True or True) # True or True = True
print("False or False:", False or False) # False or False = False
# not operator
print("not (True):", not True) # not True = False
print("not (False):", not False) # not False = True

# example of logical operators in if else
age = 25    # age variable
has_id = True  # has_id variable
if age >= 18 and has_id:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")