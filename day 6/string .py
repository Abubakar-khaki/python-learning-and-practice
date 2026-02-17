name = "abubakar khaki"
# short name latter 
print("length of name:", len(name))
print("short name is first 3 letter:", name[0:3])
print("first letter of name is:", name[0])
print("first letter of name is:", name[-13])
print("last letter of name is:", name[13])
print("last letter of name is:", name[-1])
print("full letter of name :" , name[:]) 
print("full letter of name :" , name[0:])
print("full letter of name :" , name[:14])

num = "0123456789abcdefghijklmnopqrstuvwxyz"

print(num[0:10:4]) # short name with step 2
print(num[1:14:3]) # short name with step 3

# string functions
print("print length of name:", len(name)) # length of string
print("check name endwith aki:", name.endswith("aki")) # check name end with aki
print("check name startwith abu:", name.startswith("abu")) # check name start with abu
print("name in upper case:", name.upper()) # name in upper case
print("name in lower case:", name.lower()) # name in lower case 
print("replace name khaki with khan:", name.replace("khaki", "khan")) # replace khaki with khan
print("find index of letter k in name:", name.find("k")) # find index of letter k in name
print("count letter a in name:", name.count("a")) # count letter a in name