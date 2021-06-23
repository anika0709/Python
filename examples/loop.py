text = "Python"
for character in text:
	print (character)

langs = ["English", "Spanish", "Hindi"]
for lang in langs:
	print(lang)

count = 1
while count<=5:
	print("Value of count is",count)
	count = count +1

# OR using for

for c in range(1, 6):
	print("Value of count is",c)

# Range Object
print(range(10))
print (list(range(4)))
print (list(range(2,8)))
print (list(range(1,9,2)))


# Table Generator
num = 6

for n in range(1, 11):
	print("{} * {} = {}".format(num,n,num*n))

# Sum 1 to 100
sum = 0
for number in range (1,101):
	sum = sum + number

print (sum)

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

result = 0
for i in numbers:
	result = result +i

print ("Result is:", result)

# Iterating over range
langs = ["English", "Spanish", "Hindi"]
print (range(len(langs)))

for i in range(len(langs)):
 	print("I can speak", langs[i])
else:
 	print ("No lang left")

# program to display student's marks from record
student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for name in marks:
  if name == student_name:
    print ("Student found")
    print ("MArks of", name, "is", marks[name])
else:
  print ("No Entry")


#num = int(input("Enter a number: "))
num = 6

count = 10
while count > 0:
  res = num * count
  print (num, "X", count, "=", res)
  count = count - 1 

  '''Example to illustrate
the use of else statement
with the while loop'''

counter = 0

while counter < 3:
    print("Inside loop", counter)
    counter = counter + 1
else:
    print("Inside else", count)


