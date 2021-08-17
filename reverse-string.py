#/usr/bin/python


string = "Anika"
new_str = ""

length = len(string)

print(length)

for i in range(length-1,-1,-1):
	new_str+= string[i]

print(new_str)

#OR

new_str1 = []

for i in range(length-1,-1,-1):
	new_str1.append(string[i])

	str1 = "".join(new_str1)

print(str1)



