#Q1. write a program for entering the name of 7 fruits and print them in a list by user input.
# name of fruits apple, banana, orange, mango, grape, pineapple, watermelon, 
# strawberry, kiwi, peach papaya, cherry, blueberry, raspberry, lemon, lime, 
# coconut, avocado, pear, fig
fruits = []
fruits.append(input("Enter the nameof fruit 1:"))
fruits.append(input("Enter the nameof fruit 2:"))
fruits.append(input("Enter the nameof fruit 3:"))
fruits.append(input("Enter the nameof fruit 4:"))
fruits.append(input("Enter the nameof fruit 5:"))
fruits.append(input("Enter the nameof fruit 6:"))
fruits.append(input("Enter the nameof fruit 7:"))
print("the list of fruits is:",fruits)

#Q2. write a program to accept 6 students marks display sort menner.
students = []
students.append(int(input("Enter the marks of student 1:")))
students.append(int(input("Enter the marks of student 2:")))
students.append(int(input("Enter the marks of student 3:")))
students.append(int(input("Enter the marks of student 4:")))
students.append(int(input("Enter the marks of student 5:")))
students.append(int(input("Enter the marks of student 6:")))
students.sort()
print("Students sorted by marks (ascending):", students)

#Q3. check tuple is never changeable in python.
my_tuple = (1, 2, 3, 4, 5)
# Attempting to change the first element of the tuple
my_tuple [0] = 10 # This will raise a TypeError because tuples are immutable

#Q4.write a program to sum the list with 4 numbers.
number = [34, 65, 101, 39]
print("sum of 4 numbers:", sum(number))

#Q5. write a program to count the nubmer of zero in following list.
a = (7, 0, 8, 0, 0, 9)
print("number of zero in list a:",a.count(0))