# Program to get letter count in a text file
  
# explit function to return the letter count
def letterFrequency(fileName, letter):
    # open file in read mode
    file = open(fileName, 'r')
  
    # store content of the file in a variable
    text = file.read()
  
    # using count()
    return text.count(letter)
  
  
# call the function and display the letetr count
print(letterFrequency('gfg.txt', 'g'))

#Write a Python program to count the frequency of words in a file.

from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))

# Read last line of the huge file
import os

with open('filename.txt', 'rb') as f:
    f.seek(-2, os.SEEK_END)
    while f.read(1) != b'\n':
        f.seek(-2, os.SEEK_CUR)
    last_line = f.readline().decode()

# read last line of a small file
with open('filename.txt') as f:
    for line in f:
        pass
    last_line = line