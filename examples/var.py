#vars

a = "Anika"
print(a)

a= "Gaurav"
print(a)

a=2,3,4
print(a)

b,c,d=2,"Anika",1.5
print(b,c,d)


c=d=e="Mahikka"
print (c)
print (d)

# constants
import constant
print(constant.PI)

# Boolean
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

#Special Literal - None

drink ="Available"
food = None
def menu(x):
	if x == "drink":
		print(drink)
	else:
		print(food)
menu("drink")
menu("burger")

#Literal Collections


fruits = ["orange", "apple", "grapes"]  #list 
numbers = (1, 2, 3)   # tuple
alpha = {"a": "Apple", "b": "Ball"}   #dict
vowels = {'a', 'e', 'i', 'o', 'u'}   #set


print(fruits)
print(numbers)
print(alpha)
print(vowels)