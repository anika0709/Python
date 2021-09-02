#Write a Python script to sort (ascending and descending) a dictionary by value.

orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

print(orders.items())

sorted_order = sorted(orders.items())
print(sorted_order) # sorted on the key

sorted_order = sorted(orders.items(),key=lambda x:x[0])
print(sorted_order)  # sorted on the key, output as tuple (key,value)

sorted_order = sorted(orders.items(),key=lambda x:x[1], reverse=True)
print(dict(sorted_order) ) # sorted on the value in descending order, output as dict

# or
sorted_dict = {k: v for k,v in sorted_order } # dictionary comprehension
print(sorted_dict)

# Another solution
import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)


### Another solution
dict1 = {1: 1, 2: 9, 3: 4, 4: 1} # assumption values will be unique
sorted_values = sorted(dict1.values()) # Sort the values
print(sorted_values)
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys(): 
        if dict1[k] == i:
          print(dict1[k])
          sorted_dict[k] = dict1[k]
          break

print(sorted_dict)

####
dict1 = {1: 1, 2: 9, 3: 4, 4: 1} # can handle multiple same values
sorted_keys = sorted(dict1, key=dict1.get) 
print(sorted_keys)
new_dict = {}
for k in sorted_keys:
  print (k)
  new_dict[k] = dict1[k]
print(new_dict)
