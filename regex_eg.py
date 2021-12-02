# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re

def find_pat(str):
  pattern = re.compile(r'\d')
  str = pattern.search(str)
  print(str)
  if (str):
    return True 
  else:
    return False

string1 = "ABCDEFabcdef123450"
string2 = "!@#$%^"

print(find_pat(string1))
print(find_pat(string2))

# Write a Python program that matches a string that has an a followed by zero or more b's. 

import re

def text_match(text):
  patterns = re.compile(r"a[b]*")
  if re.search(patterns,  text):
    return 'Found a match!'
  else:
    return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))

# Write a Python program that matches a string that has an a followed by one or more b's. 

def text_match(text):
  patterns = re.compile(r"a[b]+")
  if re.search(patterns,  text):
    return 'Found a match!'
  else:
    return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))

# Write a Python program that matches a string that has an a followed by zero or one 'b'. 

def text_match(text):
  patterns = re.compile(r"a[b]?[^b]")
  if re.search(patterns,  text):
    return 'Found a match!'
  else:
    return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))


# Write a Python program that matches a string that has an a followed by three 'b'. 

import re
def text_match(str):
  pattern = re.compile(r'ab{3}')
  if re.search(pattern, str):
    return "MATCHED!!!"
  else:
    return "Not MAtched :("
  
print(text_match("abbc"))
print(text_match("abbb"))
print(text_match("abbbabb"))


# 6. Write a Python program that matches a string that has an a followed by two to three 'b'. 
import re
def text_match(text):
  pattern = re.compile(r'ab{2,3}')
  if re.search(pattern,text):
    return "MATCHED!!!"
  else:
    return "Not MAtched :("
print(text_match("abc"))
print(text_match("abbb"))

# 7. Write a Python program to find sequences of lowercase letters joined with a underscore. 

import re
def text_match(text):
  pattern = re.compile(r'ab{2,3}')
  if re.search(pattern,text):
    return "MATCHED!!!"
  else:
    return "Not MAtched :("
print(text_match("abc"))
print(text_match("abbb"))

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

import re, collections
def clean_text(sentence):

  op = re.sub('[^a-z|A-Z|\s|\.]+',"", sentence).split()
  print(collections.Counter(op).most_common(3))

print(clean_text(sentence))


