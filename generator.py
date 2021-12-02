def generator_series(low, high):
	while low <= high:
		yield low
		low += 1


n_list = [] #initialize

for i in generator_series(1,10):
	n_list.append(i)

print(n_list)
