name = input("Enter your name: ") 
age = int(input("Enter your age: "))
gender = (input("choose your gender. enter M for male and F for female: "))
game = input("Enter your favorite game: ")

print("Your name is:", name)
print("Your age is:", age)
if gender == "M" or gender == "m":
    print("Your gender is male.") 
elif gender == "F" or gender == "f":
    print("Your gender is female.")
else:
    print("Invalid input for gender.")
print("Your favorite game is :", game)

a = input("enter value:")
b = input("enter value:")
sum = int(a) + float(b)
print("The sum of", a, "and", b, "is:", sum) 
