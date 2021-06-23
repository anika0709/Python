# tuple

tup = (1,2,3,4,5,1,)
print ("First tuple is", tup)

tup2 = (1,2,"3","Anika", 3.5)
print("Sec tuple is", tup2)

tup3=([1,2,3],"A",3.5,(1,2,3,4))
print(tup3[0][1])   #2
print (tup3[3][2])  #3

#A tuple can also be created without using parentheses. This is known as tuple packing.

my_tup= "Anika","Rathi", "Test"
print(type(my_tup))
print(my_tup)

#unpacking tuple
a,b,c = my_tup
print(a)
print(b)

#one element in tuple
one_tup = ("Gaurav")
print(one_tup)
print("Type of 1 element", type(one_tup))

one_tup1 =("Kumar",)
print(one_tup1)
print(type(one_tup1))

#indexing
print(tup[:2])  #(1,2)
print(tup[-3:])  #(3,4,5)

#changing values
print(tup3[0][1])
tup3[0][1] = 4
print(tup3[0])

# concatenation
newTup = tup + tup3
print(newTup)

# repeate
tup_r = ("Hello",)
print(tup_r * 3)   #('Hello', 'Hello', 'Hello')

# del
del tup2
# print (tup2)     #OutPUt: NameError: name 'tup2' is not defined

#tuple methods
print (tup.count(1))

print(2 in tup)
print(3 not in tup)


for i in tup:
	print(i)









