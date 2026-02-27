#Q 2: write a program to input 8 number from user and print unique number(once)
numbers = set()
for i in range(8):
    num= int(input("enter a number: "))
    numbers.add(num)
print("unique numbers are: ", numbers)
