a = {   "key" : "value",
        "name": "khaki",
        "age": 27, 
        "gender": "male",
        "edu/skill": ["F.A.","python","trading"] 
}

b = {1 : 2, 3:4, 5:6}
print(a.get("name"))# returns the value of the key "name"
print(a["age"])# returns the value of the key "age"
a.update({"name": "khakisage", "hobby": "problem solving"})# updates the value of the key "name" and adds a new key "hobby" 
print(a)
print((a.keys()))# returns a list of all the keys in the dictionary
print(a.values())# returns a list of all the values in the dictionary
print(b.items())# returns a list of all the key-value pairs in the dictionary as tuples
print(b.pop(1))# removes the item with key 1 and returns its value
print("after pop b:", b)
print(b.popitem())# removes the last inserted item and returns it as a tuple
print("after popitem b:", b)
a.clear()
print(a)