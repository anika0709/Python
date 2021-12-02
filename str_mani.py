#How do you reverse a given string in place?
string="thisistheexample"
print(string[::-1])

#How do you print duplicate characters from a string?
string = "java" 
dict1 = {}
dup_list = []
for i in string:
	if i in dict1:
		dup_list.append(i)
	else :
		dict1[i] = "e"
print(dup_list)

#How do you check if two strings are anagrams of each other
# example: if they contain the same characters but on different order army and mary

str1 = "army"
str2 = "mary"

str1_list = sorted(str1)
print(str1_list)
str2_list = sorted(str2)
print(str2_list)
if str1_list == str2_list:
	print("Yes")
else:
	print("Not an anagram")

# How do you find all the permutations of a string?
from itertools import permutations
for p in permutations("hen"):
	print (''.join(p))

#OR
print ([''.join(p) for p in permutations("bed")]) # create a list

# Python program to print all permutations with
# duplicates allowed

def toString(List):
	return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
	if l == r:
		print toString(a)
	else:
		for i in xrange(l, r + 1):
			a[l], a[i] = a[i], a[l]
			permute(a, l + 1, r)
			a[l], a[i] = a[i], a[l] # backtrack

# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)

# This code is contributed by Bhavya Jain



# How can a given string be reversed using recursion? 
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
s = "Geeksforgeeks"
print(reverse(s))

def rev_rec(s):
	if len(s) == 0:
		return s
	return rev_rec(s[1:]) + s[0]

print(rev_rec(s))

#using stack

def rev_stack(string):
	stack,st = [],[]
	stack = list(string)
	for i in range(len(stack)):
		last_item = stack.pop()
		st.append(last_item)
	print(''.join(st))

rev_stack(s)

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
# Driver code
str1="ABCD"
print(Convert(str1))
print(list(str1))




# How do you check if a string contains only digits?
st1= "abc"
st2 = "123"
print(st1.isdigit())
print(st2.isdigit())
# How do you find duplicate characters in a given string?
# How do you count a number of vowels and consonants in a given string?
from collections import Counter


def get_count(str):
	vow = ['a','e','i','o','u']
	vow_count,const_count = 0,0
	c = Counter(str)
	print(c)
	for k,v in c.items():
		if k in vow:
			vow_count = vow_count + v
		else:
			const_count = const_count + v
	print("Num of vowel are: ", vow_count)
	print("Num of consonants are: ", const_count)

get_count(s)
# How do you count the occurrence of a given character in a string?
def get_char_count(c,st):
	count = Counter(st)
	print(count[c])

get_char_count("e",s)
# How do you print the first non-repeated character from a string?
def get_nonrepeate(str):
	map = {}
	#count = 0
	for i in str:
		if i in map:
			del map[i]
		else:
			map[i] = 1
	if not map:
		print("All Char are repeating")
	else:
		print(next(iter(map)))


get_nonrepeate("aabb")
get_nonrepeate(s)



# How do you convert a given String into int like the atoi()?
# How do you reverse words in a given sentence without using any library method?
sentence = " This is the example"
length = len(sentence)
l = []
for i in range(length-1,0,-1):
	l.append(sentence[i])
print(''.join(l))
	
# How do you check if two strings are a rotation of each other?
if s == reverse(s):
	print("s is a palindrome")
print(s[::-1])
# How do you check if a given string is a palindrome?
# How do you find the length of the longest substring without repeating characters?
# Given string str, How do you find the longest palindromic substring in str?
# How to convert a byte array to String?
# how to remove the duplicate character from String?
# How to find the maximum occurring character in given String?
# How do you remove a given character from String?

