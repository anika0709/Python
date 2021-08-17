# num = [1, 4, 9]

# print(dir(num))

# # iter_val = num.__iter__()   OR use iter() method
# iter_val = iter(num)

# print (iter_val)

# while True:
# 	try:
# #		item = iter_val.__next__() OR use next() method
# 		item = next(iter_val)
# 		print(item)
# 	except StopIteration:
# 		break

########## CREATE ITERATOR TO FIND 

class Even:
	def __init__(self,max):
		self.n = 2
		self.max = max
	def __iter__():
		return (self)
	def __next__():
		if self.n <= self.max:
			result = self.n
			self.n += 2
			return (result)
		else:
			raise StopIteration

