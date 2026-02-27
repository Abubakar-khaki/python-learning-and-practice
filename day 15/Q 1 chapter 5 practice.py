# Q 1: write a program to create a dictionary of engilsh words with values of urdu meaning. user gives input of word and show meaning of that word in urdu.
urdu_dictionary = {
    "book": "کتاب",
    "pen": "قلم",
    "table": "میز",
    "chair": "کرسی",
    "house": "گھر",
    "water": "پانی",
    "friend": "دوست",
    "happiness": "خوشی",
    "love": "محبت",
    "life": "زندگی",
}
word = input("Enter an english word: ")
if word in urdu_dictionary:
    print(f"{word} meaning is:{urdu_dictionary[word]}")
    # print(word, "meaning is :", urdu_dictionary[word]) same result as above
else:
    print("word not found in dictionary")


