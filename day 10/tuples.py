a = (1, 2, 3, 4, 5, "a", 2, 2, 2.5, None, True)
b = (55,22,33,44,55)
print(type(a)) # a is type of tuple - a collection of items that can be of different
#data types. It is ordered, immutable, and allows duplicate elements.
count = a.count(2)
print(count) # in results in 3 - counts the number of occurrences of '2' in the tuple
index = a.index(2)
print(index) # in results in 1 - returns the index of the first occurrence of '2' in the tuple
cancontenate = a + b
print("concatenating a and b:", cancontenate) # in results in (1, 2, 3, 4, 5, "a", 2, 2.5, None, True, 55, 22, 33, 44, 55) - concatenating two tuples a and b
repeated = a * 2
print(repeated)
len = len(a)
print("length of tuple a:",len)
print("a" in a)# in method use for check avliablity