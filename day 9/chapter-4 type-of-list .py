a = (1, 2, 3, 4, 5)
b = {1, 2, 3, 4, 5}
c = [1, 2, 3, 4, 5]
print(type(a)) # a is type tuple
print(type(b)) # b is type set
print(type(c)) # c is type list

list = ["apple", 123, 4.5, None, True, "khaki", {"name": "Alice", "age": 30}, [1, 2, 3], (4, 5, 6), {1, 2, 3}]
#list is a collection of items that can be of different data types. It is ordered, mutable, and allows duplicate elements.
print(list)
l1 = [1, 2, 4, 3, 5,]
print (l1[2]) #in results in 3 - prints the element at index 2
print(l1[1:4]) #results in [2, 3, 4] - prints elements from index 1 to index 3 (4 is not included)
l1.sort()
print("sorting the list:", l1) # in results in [1, 2, 3, 4, 5]

l1.reverse()
print("reversing the list:", l1) # in results in [5, 4, 3, 2, 1]
l1.pop(1)
print("popping item at index 1:", l1) #in results in [5, 3, 2, 1]
l1.append("new item")
print("\"append\" adding new item at the end:", l1) # in results in [5, 3, 2, 1, "new item"]
l1.remove(1)
print("remove '1' from the list:",l1) #in results in [5, 3, 2, "new item"]
l1.insert(6, "inserted item")
print("inserting item at index 6:", l1) #in results in [5, 3, 2, "new item", "inserted item"]
l1[0:3] = [1, 2, 3]
print("replacing first three items with [1, 2, 3]:", l1) #in results in [1, 2, 3, "new item", "inserted item"]
l1.clear()
print("clearing the list:", l1) #in results in []