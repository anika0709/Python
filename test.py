#Write a Python program to remove newline characters from a file.


#with open("file.txt", 'w') as f:
#	li = f.readlines()
#	print(li)

f = open("file1.txt", 'r')
# while True:
# 	line = f.readlines()
# 	if not line:
# 		break
# 	print(line)
# f.close()

# Read from 1 file and write to another
flist = f.readlines()
print ([ s.rstrip("\n") for s in flist ])

input_file = open("file1.txt","r")
output_fil = open("op.txt", "w")
f1 = input_file.readlines()
for line in f1:
	output_fil.write(line)

#Write a Python program to check that a string contains only a certain set of characters

import re

pattern = re.compile(r"\d")
str = pattern.search("ABCDEFabcdef123450")
print(bool(str))

#split() in string
import sys

str = "100.214.242.245"
no_list = str.split(".")

for no in no_list:
	if int(no) <0 or int(no) > 255 :
		sys.exit(2)
str = ".". join(no_list)
print(type(str))
import sys

print(sys.version)
#####

nums = [2,7,11,15]
tar = 9
for i, n in enumerate(nums):
	hash = {}
	if n in hash:
		return 
	else:
		hash[tar-n] = i





