import operator

dict1 = {1: 1, 2: 9}
get_item_with_key_2 = operator.itemgetter(2)

print(get_item_with_key_2(dict1))  # 9



# Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

# #Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic = {}

for d in (dic1,dic2,dic3):
  dic.update(d)

print(dic)

#write a Python script to check whether a given key already exists in a dictionary.

def check_key(dic,k):
  if k in dic:
    print("Exists")
  else:
    print("Not Found")

dict1 = {1: 1, 2: 9}
check_key(dict1,1)

#Write a Python program to iterate over dictionaries using for loops.

d = {'x': 10, 'y': 20, 'z': 30} 
for k, v in d.items():
  print (k, v)


#  Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def gen_dict(n):
  new_dict = {x: x*x for x in range(n+1)} # Dictionary comprehension
  return new_dict


print(gen_dict(4))


# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. Go to the editor
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}




