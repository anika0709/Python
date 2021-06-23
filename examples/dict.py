#create dictionary


person1 = {"Name": "Ananya", "age": 33, "school": "St Ann's"}
print(person1)

# dict with mixed key
person2 = {1: "Adi", ("age"): 23 }
print (person2)

#person1 = {1: "Adi", ("age"): 23, {3}: "Good"}  #TypeError: unhashable type: 'set'

#Empty dictionary
emp_dic = {}
print(emp_dic)
print("type of empty dictionary", type(emp_dic))

# create dict using dict()
new_dict = dict([(1, "apple"), (2, "orange")])
print(new_dict)
fruits = dict({1: "grapes", 2: "pears"})
print (fruits)


# Accessing dictionary
print(fruits[1])

print(person1.get("Name"))

# Trying to access keys which doesn't exist throws error

print(person1.get('address')) # Output None

# print(person1['address'])   ## KeyError

# changing and adding

person1["Name"] = "Aditi"
print(person1)

person1["address"] = "Noida"
print(person1)


# Removing item
# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

pop_item = squares.pop(2)
print(pop_item)   #4
print(squares)  # {1: 1, 3: 9, 4: 16, 5: 25}

# remove an arbitrary item, return (key,value)
print(squares.popitem())   #(6, 36)


# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
# del squares     # print(squares) # Throws Error


# Dictionary Comprehension

cube = {x: x*x*x for x in range(6)}
print(cube)

sqr = {x: x*x for x in range(10) if x%2 == 1}
print(sqr)


# # Membership Test for Dictionary Keys

print(4 in sqr)  # False
print (5 not in sqr) # False
print (25 in sqr) # False

for k in sqr:
	print ("Key is {} and value is {}". format(k,sqr[k]) )


# length
print("Length is", len(sqr))

squares = {1: 1, 6: 36, 2: 4, 5: 25, 3: 9, 4: 16 }
print ("Sorted dict is", sorted(squares))






