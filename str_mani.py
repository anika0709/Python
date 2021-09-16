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

# How can a given string be reversed using recursion? 

# How do you check if a string contains only digits?
# How do you find duplicate characters in a given string?
# How do you count a number of vowels and consonants in a given string?
# How do you count the occurrence of a given character in a string?
# How do you print the first non-repeated character from a string?
# How do you convert a given String into int like the atoi()?
# How do you reverse words in a given sentence without using any library method?
# How do you check if two strings are a rotation of each other?
# How do you check if a given string is a palindrome?
# How do you find the length of the longest substring without repeating characters?
# Given string str, How do you find the longest palindromic substring in str?
# How to convert a byte array to String?
# how to remove the duplicate character from String?
# How to find the maximum occurring character in given String?
# How do you remove a given character from String?

