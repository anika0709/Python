# numbers

a = 4
b = 3.4
c = 3.14j

print (a,"is", type(a) )
print (b,"is", type(b) )
print (c,"is", type(c) )

print ("Is c complex?", isinstance(c,complex))

# list -ordered list of items, mutable
any_type = ["Names", 1.0, [1,2,3], {1: "23434", 2: "47"}]

print (any_type)
print("type of", any_type, type(any_type))

print (any_type[2])
print(any_type[0:2])
print (any_type[2:])

any_type[0] = "NoNames"
print(any_type[0:2])


# tuples - immutable
tup = (1,"Anika", [1,2,4])
print (type(tup))
print (tup)
print (tup[0])

#Strings - immutable

state = "This is a single line"
mult_state = ''' this is a 
multi line '''
print (state)
print (mult_state)

print (state[3])
print (state[5:8])


# Unordered set of unique items
set_1 = {1,1,2,2,3,4,4,4,4}
print (set_1)

set_1 = {3234,45,565,767,7}
print (set_1)


# dictionary
d = {1: "first", 2: "second", 3: "third"}
print(d[2])
d[2] = "SECOND"
print(d[2])
