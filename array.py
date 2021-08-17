
string = ['a', 'b', 'c', 'd']

print (string)

print (string.pop(), string) #O(1)

print (string[0])  # O(1)

print(string.append("e"), string)   #O(1)

string.insert(2, 'f')   #O(n)

string.insert(2, 'g')   #O(n)

string.insert(2, 'h') #O(n)
string.insert(2, 'i')  #O(n)

string.remove('a')   #O(n)

print (string)

del string[2:4]    #O(n)

print(string.pop(0))

print (string)

