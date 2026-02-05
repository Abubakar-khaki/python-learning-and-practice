# type function
# to know the data type of variable we use type() function
a = 10 # integer variable
b = 10.5 # floating point variable 
c = "khaki" # string variable
d = False # boolean variable
e = None # none variable
print ("data type of a:", type(a))
print ("data type of b:", type(b))
print ("data type of c:", type(c))
print ("data type of d:", type(d))
print ("data type of e:", type(e))

#example of type function in if else
value = 123
if type(value) == int:
    print("value is a integer.")
else:
    print("value is not a integer.")

# we canuse type function for change the data type of variable if data type is valid
print(" integer changed to string:", str(a))   
print(" integer changed to float:", float(a))
print(" integer changed to boolean:", bool(a))
print(" integer cann't changed to none:",)

print(" float changed to integer:", int(b))
print(" float changed to string:", str(b))
print(" float changed to boolean:", bool(b))
print(" float cann't changed to none:",)

print(" string cann't changed to integer:",) # if string contain alphabate
print(" string cann't changed to float:",) # if string contain alphabate
print(" string changed to boolean:", bool(c)) # non empty string is true
print(" string cann't changed to none:",)

print(" boolean changed to integer:", int(d)) 
print(" boolean changed to string:", str(d))
print(" boolean changed to float:", float(d))
print(" boolean cann't changed to none:",)

print(" none changed to string:", str(e))
print(" none changed to boolean:", bool(e))