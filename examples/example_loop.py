# loop over sequence

fruits = ["apple", "orange", "banana", "grapes", "berries"]
for fruit in fruits:
	print(fruit)

# Write a Python program to find those numbers which are divisible by 7 
# and multiple of 5, between 1500 and 2700 (both included)

# my_list = []
# for i in range(1500,2701):
#   if (i%5 == 0) and (i%7 ==0):
#     my_list.append(i)
# print (my_list) 

#Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
#[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
 
# choice = (input("Are you typing C or F: "))
# if choice == "F":
#   temp = int(input("Enter the temperature: "))
#   print ("Converting to celsius")

#   #c/5 = f-32/9 
#   new_temp = int((temp-32/9)*5)
#   print (new_temp)
# elif choice == "C":
#   temp = int(input("Enter the temperature: "))
#   print ("Converting to Faranheit")
#   new_temp = int((temp/5)*9 + 32)
#   print (new_temp)
# else:
#   print("You've choose wrong. Use C or F")

###########################

# Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ] 
# Expected Output : 
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius 

input_temp = input("Enter the temperature, eg 64C or 145F: ")

type = input_temp[-1]
temp_temp = int(input_temp[:-1])
print(temp_temp)

if (type == "C"):
  print ("Type is in Centigrade")
  converted_temp = ((temp_temp/5)*9)+32
  print ("{} is {:.2f} in Fahrenheit".format(input_temp, converted_temp))
elif(type == "F"):
  converted_temp = (temp_temp-32/9)* 5
  print ("{} is {:.2f} in Celsius".format(input_temp, converted_temp))
else:
  print ("Type in C or F")

############

# Enter a number, if the number is between 1 to 9, print "Well Guessed" and exit
# else continue

while True:
  enter_num = int(input("Enter"))
  if enter_num in range(10):
    print ("Well Guessed")
    break
  else:
    continue


#########
# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

import random

from random import randint as rt

while True:
  random_num = rt(1,9)
  print (type(random_num), random_num)
  if random_num == int(input("Enter a number between 1 to 9: ")):
    print ("Well Guessed!")
    break
  # else:
  #   continue
    
  
  











