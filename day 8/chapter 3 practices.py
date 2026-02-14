#Q1. write a python program to display entered user name followed by good afternoon using input 
name =input("Enter your name:")
print(f"good afternoon {name}")

#Q2. write a python program to fill in a letter template give below with name and date
letter1 = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''
print(letter1.replace("<|NAME|>", name).replace("<|DATE|>", "12-12-2025"))

#Q3. write a python program to detect double spaces in a string
str = "khaki is a  sage boy."
if "  " in str:
    print("double space detected.")
else:
    print("no have any double space.")

#Q4. Replacedouble space with single space in given string.
print(str.replace("  ", " "))

#Q5. Write a program to format the following letter using escape sequence characters.
letter = "Dear khaki, this python course is very nice. thanks!"
print("Dear \"khaki\",\nthis python course is very nice. \nthanks!")