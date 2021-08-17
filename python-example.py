# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

import datetime

now =datetime.datetime.now()
print(now)
new_now = now.strftime("%Y-%d-%m %H:%M:%S")
print(new_now)

##################

#Write a Python program to get the Python version you are using.

##################

# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
# Click me to see the sample solution

inpu = input("enter input: ")
nlist = inpu.split(",")
print (list(nlist))
print (tuple(nlist))

#######

#Write a Python program to accept a filename from the user and print the extension of that. 
# Sample filename : abc.java
# Output : java


file_name = input("Enter file name")
ext = file_name.split(".")
print (ext[-1])

##############

# Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)
new_exam = str(exam_st_date)
temp_date = new_exam.replace(",", " /")
new_date = temp_date.replace("(", "")
new_date = new_date.replace(")", "")
print(new_date)

#Another_Solution
exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)


####################

# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
# Sample value of n is 5
# Expected Result : 615

n = int(input("Enter number: "))
n1 = int("%s" % n)
n2 = int("%s%s" % (n,n))
n3 = int("%s%s%s" % (n,n,n))
print(n1+n2+n3)


####################

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# Return the absolute value of the argument.

print(abs.__doc__)

#########

#Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar
print(calendar.month(2021,6))


#Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
# Click me to see the sample solution

from datetime import date

f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

#########
# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.


def check_sum(n,m,o):
  sum =  n + m + o
  if n ==m == o:
    print ((sum)*3)
  else:
    print (sum)

check_sum(2,3,4)
check_sum(4,4,4)

#####
# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged. Go to the editor
# Click me to see the sample solution

inp = input("String is: ")

if inp[:2] =="ls":
  print(inp)
else:
  print("ls" + inp)

  #####
  # Write a Python program to get a string which is n (non-negative integer) copies of a given string.

inp = int(input("No of copies: "))
str = "This"
print(str*inp)

##################
#How to check if String is empty in Python
# To check if the string is empty or not, use a not operator.

empty_string = ""

print("Check if the string is empty : ", end="")

if(not empty_string):
    print("The string is empty")
else:
    print("No it is not empty")

 ##############

 #Write a Python program to concatenate all elements in a list into a string and return it. Go to the editor

con = ""
list = ["This", "is", "Anika"]
for item in list:
  con = con + str(item)

print(con)


##############

# Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. Go to the editor
# Sample numbers list :

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

for i in numbers:
  if i == 237:
    break
  elif i % 2 ==0:
    print(i)


########

# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

new_list = color_list_1 - color_list_2
print(new_list)

#######

# Write a Python program to print out a list containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

color_list_1 = ["White", "Black", "Red"]
color_list_2 = ["Red", "Green"]

newlist = []
for list1 in color_list_1:
  found = False
  for list2 in color_list_2:
    #print("Inside for", list2)
    if list1 == list2:
      found = True
     # print(found, list1, list2)
  
  if found == False:
    #print("Appending to", list1)
    newlist.append(list1)

print(newlist)

#######################

#Ask Gaurav
# Write a Python program to compute the greatest common divisor (GCD) of two positive integers

n1 = 336
n2 = 360

for i in range(n2,0, -1):
  if (n2%i == 0) and (n1%i == 0 ):
    print(i)
    break

#####################
# Write a Python program to get the least common multiple (LCM) of two positive integers.

def findLCM(n1, n2):
  if n1 > n2:
    n = n1
  else:
    n = n2
  while True:
    if (n % n1 == 0) and (n %n2  == 0):
      print ("LCM is", n)
      break
    n = n+1

findLCM(4, 6)
findLCM(15, 17)


##############

#Important
# 36. Write a Python program to add two objects if both objects are an integer type.

def add_numbers(a, b):
   if not (isinstance(a, int) and isinstance(b, int)):
       return "Inputs must be integers!"
   return a + b

print(add_numbers(10,20))
print(add_numbers("10",20))

####################
# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). Go to the editor
# Click me to see the sample solution
import math
p1 = [4, 0]
p2 = [6, 6]
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)

# 41. Write a Python program to check whether a file exists. 
import os.path
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))


#Important
# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import platform, struct
print(platform.architecture()[0])
print(struct.calcsize("P") * 8)

#Important
# 43. Write a Python program to get OS name, platform and release information.

import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())

# 44. Write a Python program to locate Python site-packages.

import site; 
print(site.getsitepackages())




