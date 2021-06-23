# Artithmetic

x = 19
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)

# Output: x % y = 3
print('x % y =',x%y)

# Comparison
x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)

# Logical
x = True
y = False

#x and y is False
print('x and y is',x and y)

#x or y is True
print('x or y is',x or y)

#not x is False
print('not x is',not x)

# Identity Operator

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False - Interpreter locates them spearately in memory
print(x3 is y3)

y1 = y1 +1

# Output: False
print("x1 is y1:", x1 is y1)

# Membership operator
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print (1 in y)

# Output: False
print ('hello' in y)

# Output: False
print ('a' in y)
