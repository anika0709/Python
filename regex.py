import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

patten = re.compile(r'abc')
print(patten)

matches = patten.finditer(text_to_search)
print (matches)

for match in matches:
	print (match)

print(text_to_search[1:4]) 

patten = re.compile(r'\BHa')

matches = patten.finditer(text_to_search)
for match in matches:
	print (match)

patten = re.compile(r'^Start')

# patten = re.compile(r'^a')   // no match

matches = patten.finditer(sentence)
for match in matches:
	print (match)

patten = re.compile(r'end$')

# patten = re.compile(r'a$')   // no match

matches = patten.finditer(sentence)
for match in matches:
	print (match)

# find the phone number

#pattern = re.compile(r'[0-9]{3}[.-][0-9]{3}[.-][0-9]{4}') 
pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}') 
matches = pattern.finditer(text_to_search)
for match in matches:
	print (match)

#pattern = re.compile(r'M[rs]s?[.]?\s\w+') 
pattern = re.compile(r'M(r|s|rs)[.]?\s\w+')
matches = pattern.finditer(text_to_search)
print (matches)

for match in matches:
	print (match)

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
pattern = re.compile(r'[\w.-]+@[\w-]+\.(com|edu|net)')
matches = pattern.finditer(emails)
print (matches)

for match in matches:
	print (match)

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
url_pat = re.compile(r'https?://(www.)?(\w+)(\.\w+)')

match_urls = url_pat.finditer(urls)
# for match in match_urls:
# 	print (match)

# can print out group
# for match in match_urls:
# 	print(match.group(0)) # print whole urls

for match in match_urls:
	print(match.group(2),match.group(3), sep = '')

# sub method to do substitution . Group2(\2) = domain name, Group3(\3) = TLD

subbed_url = url_pat.sub(r'\2\3', urls)
print(subbed_url)

# other methods like finditer (match object with extra functionality), findall just returns the matches

pattern = re.compile(r'M(r|s|rs)[.]?\s\w+')
matches = pattern.findall(text_to_search) # only print out matched groups, if no gruop, all matches
print (matches)

for match in matches:
	print (match)

# match only serach at the beginning of the string, to search entire string use `search` method. PRints first match it finds






