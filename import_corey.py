
print("Module imported...")
''' this is intro module to be imported '''

def find_index(list,target):
	'''Find the index in the list'''
	for i,val in enumerate(list):
		if target == val:
			return ("Target is at", i)
	return "Not Found"


#my_list = ["Math","Eng","Science"]
#print(find_index(my_list,"Mth"))