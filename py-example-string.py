# . Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def count_char(stri):
  freq = {}
  for i in stri:
    if i in freq.keys():
      freq[i] = freq[i] +1
    else:
      freq[i] = 1

  print(freq)

count_char("google.com")

########
# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'

def find_change(str):
  to_find = str[0]
  str = str.replace(to_find, '$')
  str = to_find + str[1:]
  print(str)

find_change("restart")
find_change("perception")


#############
# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

def replace_string(str1, str2):
  ff1 = str1[0:2]
  ff2 = str2[0:2]
  str1 = str1.replace(ff1,ff2)
  str2 = str2.replace(ff2,ff1)
  print (str1, str2)

replace_string('abc', 'xyz')

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))


##########
# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
# Click me to see the sample solution

in_str = 'The lyrics is not that poor!'

def find_some(in_str):
  snot = in_str.find("not")
  print(snot)
  spoor = in_str.find("poor")
  print(spoor)

  if snot > 0 and spoor > 0 and snot < spoor:
    in_str = in_str.replace(in_str[snot:(spoor+4)], 'good')
    return in_str
  else:
    return in_str

print(find_some(in_str))

##########
# Write a Python function that takes a list of words and returns the longest word and the length of the longest one. Go to the editor
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

list_words = ["anika", "mahikka", "kumargaurav"]

def len_word(list):
  for i in range(len(list_words)-1):
    if len(list_words[i]) > len(list_words[i+1]):
      longest = list_words[i]
    else:
      longest = list_words[i+1]

  print ("Longest word: ", longest)
  print ("Length of the longest word: ", len(longest))

len_word(list_words)

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])


#####
# Write a Python program to count the occurrences of each word in a given sentence.

sent = " This is a big sent but not as big a work or a word"

sent = sent.split(" ")
dict = dict()

for i in sent:
  if i not in dict:
    dict[i] = 1
  else:
    dict[i] = dict[i] + 1

print (dict)

######
#  Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 

str = "Python"
count = 0
for i in str[0:4]:
  if i.upper() == i:
    count += 1
if count >= 2:
  print(str.upper())

  #########
  #  Write a Python program to create a Caesar encryption. Go to the editor

# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.
def crypt(step,data_input):
  new_data = []
  uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  for each_l in data_input:
    if each_l in uppercase:
      exist_index = uppercase.index(each_l)
      crypting = (exist_index + step) % 26
      new_l = uppercase[crypting]
      new_data.append(new_l)
    elif each_l in lowercase:
      exist_index = lowercase.index(each_l)
      crypting = (exist_index + step) % 26
      new_l = lowercase[crypting]
      new_data.append(new_l)

  return new_data


print(crypt(3, "ANIKA"))
print(crypt(5, "anika"))
print(crypt(7, "ANIKA"))

#################


#Add a prefix text to all of the lines in a string

import textwrap
sample_text ='''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
text_without_Indentation = textwrap.dedent(sample_text)
wrapped = textwrap.fill(text_without_Indentation, width=50)
#wrapped += '\n\nSecond paragraph after a blank line.'
final_result = textwrap.indent(wrapped, '> ')
print()
print(final_result)
print()
