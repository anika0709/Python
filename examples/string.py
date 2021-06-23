# Python String Operations
str1 = 'Hello '
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)

name = "Mihitta"
for n in name:
	print (n)

# find number of char in a String

count = 0
str = "my heart goes lalalala, lala lala in the morning"
for s in str:
	if (s == "l"):
		count = count + 1

print (count, "l found")


#format()
print ("{} and {} are fun". format("John","Esley"))  # default order

print ("{1} and {0} are fun". format("John","Esley")) #positional

print ("{name} drives {car}". format(name="John",car="Tesla")) #keyword


# raw string
print("This is \x61 \ngood example" )
print(r"This is \x61 \ngood example")


# formatting integers
print("Binary representation of {0} is {0:b}".format(12))

# formatting floats
print ("Exponent representation: {0:e}".format(1566.345))

# string alignment
print ("|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham')) #we can left-justify <, right-justify > or center ^ a string in the given space.


# old style
x = 12.3456789
print('The value of x is %3.2f' %x) #The value of x is 12.35

print('The value of x is %3.4f' %x) #The value of x is 12.3457

# string method
print(len(str))
print(enumerate(str)) #<enumerate object at 0x102ed8e60>
print(list(enumerate(str))) #(0, 'm'), (1, 'y'), (2, ' '), (3, 'h'),....

sample = "ThIs Is mY SAmpLe"
sample2 = "and IT wOrKs"
print("Sample in upper is",sample.upper())
print("Sample in lower is", sample.lower())

list1 = sample2.split()
print("splitting", sample2.split())

print(sample.join(list1)) #andThIs Is mY SAmpLeITThIs Is mY SAmpLewOrKs
print(' '.join(list1))  #and IT wOrKs

print(sample.replace('mY','oUR'))








