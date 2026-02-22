s = set() # is an empty set
# s = {} # wrong
s = {0, 2, 5, 3, 4, 3, 2, 4, 3, "a"}
s1 = {5, 6, 7, 8}
s.add(1) # add 1 in set
print(s) 
s.remove(0) #remove 0 from  set
print(s)
print(len(s)) # length of set
s.discard(9) # remove if 9 is in set else do nothing
union = s.union(s1) # returns a new set that is the union of s and s1
print("union:", union)
intersection = s.intersection(s1) # returns a new set that is the intersection of s and s1
print("intersection:", intersection)
difference = s.difference(s1) # returns a new set that is the difference of s and s1
print("difference:", difference) # same as s - s1
difference1 = s1.difference(s) # returns a new set that is the difference of s and s1
print("difference1:", difference1)# same as s1 - s
a = {1, 2}
b = {1, 2, 3, 4, 5}
sabset = a.issubset(b) # returns True 
print("a is subset of b:", sabset)
superset = b.issuperset(a) # returns True because b is a superset of a
print("b is superset of a:", superset)
