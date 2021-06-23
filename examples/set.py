#set is an unordered collection of items. Every set element is unique (no duplicates) 
# and must be immutable (cannot be changed).

# create set

veg = set()   # empty set
print(type(veg)) #<class 'set'>

veg_try = {}
print (type(veg_try))  #<class 'dict'>

veg = set("potato")
print(veg) #{'a', 'p', 't', 'o'}

veg = set({"potato"})
print(veg)   #{'potato'}

my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set = {1, 2, 3, 4, 3, 2}
print(my_set)


# sets are mutable
#add 1 element
my_set.add(4)
print(my_set)      #{1, 2, 3, 4}

# add multiple elements
my_set.update([5,6,7])   
print (my_set)      #{1, 2, 3, 4, 5, 6, 7}

# add list and set
my_set.update([8,9],{10,11})
print(my_set)             #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}


#discard() function leaves a set unchanged if the element is not present in the set. On the other hand, 
# the remove() function will raise an error in such a condition (if element is not present in the set).

my_set.discard(10)

# pop()
arbitary_item = my_set.pop()
print(arbitary_item, my_set)

#copy()
new_set = my_set.copy()
print("new_set is",new_set)



# clear
my_set.clear()
print(my_set)


# Operation - Union and Intersection

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print ("Union is", A|B)
print("Union is", A.union(B))

print ("Intersection is", A&B )
print("Intersection is", A.intersection(B))

print ("Difference A- B is", A - B )
print("Intersection is", A.difference(B))

print ("Difference B-A is", B - A )
print("Intersection is", B.difference(A))


# in keyword in a set
# initialize my_set
my_set = set("apple")

# check if 'a' is present
# Output: True
print('a' in my_set)

# check if 'p' is present
# Output: False
print('p' not in my_set)

print("Length is", len(new_set))

print("Max is", max(new_set))
print("Min is", min(new_set))







