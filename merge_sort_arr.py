
# using sort() method
# a= [1,2,3,4]
# b=[3,7,9,12]

# a.extend(b)
# a.sort()
# print(a)

# implementing merge sort without sort()

def merge_sort(a,b):
	if len(a) == 0 and len(b) == 0:
		return a+b
	new_list = []

	i=j=0

	while i<len(a) and j<len(b):
		if a[i] <= b[j]:
			new_list.append(a[i])
			i += 1
		elif b[j] < a[i]:
			new_list.append(b[j])
			j += 1
		print(a[i:])
		print (b[j:])
	return new_list+a[i:]+b[j:]

a=[1,3,4,6,20]
b=[2,3,4,5,6,9,11,76]
x=merge_sort(a,b)
print(x)







