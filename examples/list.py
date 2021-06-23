# list - seq data in order

number = [1, 3, 5, 7]

print (len(number))

mixed_list = [1,1, "1.2", 3.2, "Anika", 3.2 ]

list1 = []
print (mixed_list, list1)

print (len(list1))

langs = ["Python", "Java", "Ruby", "Go"]
print (langs)

print(langs[0])

print (langs[0:2])
#print (langs[4])   //IndexError: list index out of range
print (langs[-3:-1])
print (langs[:2])
print (langs[2:])

langs[1] = "JavaScript"
print(langs)

langs[1:3] = ["JavaScript", "Lua"]
print(langs)

# Nested Lists and slicing it
num = [[1,2,3,4], "Hello", [5,6,7]]
print (num)
print (num[1][0])
print (num[0][3])

#num[4] = "New_string" #IndexError: list assignment index out of range

# in keyword - to check if item is in the list

print ("Rust" in langs)   # False

# for loop
for lan in langs:
	print (lan)

# append method - add 1 item
langs.append("Rust")
print(langs)

# extend metho - add multiple items
langs.extend(["Rust", "C"])
print("After using extend", langs)

# insert method - # insert at specific place
langs.insert(1, "Java")
print (langs)

# concatenate
langs = langs + ["C++", "Maven"]
print(langs)

# del method
del langs[4:6]
print ("After deleting", langs)


# remove
langs.remove("Lua")
print(langs)

# copy methos
langs1 = langs.copy()
print (langs1)
print ("Langs=", langs)

#del langs   # delete entire list
# print("Afrer deleting", langs) //NameError: name 'langs' is not defined

##IMP: Comprehensive way to generate list
doub = [x*2 for x in range(1,11)]
print (doub)

pow2 = []
for x in range(1,11):
	pow2.append(2**x)
print(pow2)

pow2.clear()
print(pow2)

# List comprehension
pow2 = [2**x for x in range(1,11)]
print (pow2)

pow2 = [2 ** x for x in range(10) if x > 6 ]
print(pow2)





