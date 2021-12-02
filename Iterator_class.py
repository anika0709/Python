import sys
class Series:
	def __init__(self, low, high):
		self.cur = low
		self.high = high

	def __iter__(self):
		return self


	def __next__(self):
		try:
			if self.cur > self.high:
				raise StopIteration
			else:
				self.cur += 1
				return self.cur - 1
		except StopIteration:
			print("Reached end of the series")
			sys.exit("Bye!")



n_list = Series(1,10)
print(n_list.__next__())
print(n_list.__next__())
print(n_list.__next__())
print(n_list.__next__())
print(list(n_list))


