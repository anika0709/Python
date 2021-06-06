# convert float to int using int()

fl = 10.356
print (int(fl))

fl2 = 10.7675
print (int(fl2))

fl3 = -10.7675
print (int(fl3))

# convert int to float using float()

int1 = 3
print (float(int1))

# convert to string using str()

int2 = 25
print (str(int2), type(str(int2)))

print (str(43.54), type(str(43.54)))

# convert sequence

list1 = [1,2,3]
print (list1)
new_set = set(list1)
print (new_set)

new_tuple = tuple(list1)
print("tuple is ", new_tuple)

str1 = "hello"
print ( list(str1))

list2 = [[1,0],[2,9],[3,8]]
print (dict(list2))

tup1 = ((1,0),(2,9),(3,8))

print (dict(tup1))