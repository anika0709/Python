import os

os.chdir('/Users/arathi02/Documents/file_dir')
print(os.getcwd())

for f in os.listdir():
	#print(f)
	# split the extension
	f_name, f_ext = os.path.splitext(f) # return tuples
	#print(f_name)
	f_title, f_course, f_num = f_name.split("-")
	f_title = f_title.strip()
	f_course = f_course.strip()
	f_num = f_num.strip()[1:]
	#print('{}-{}-{}{}'.format(f_num,f_title,f_course,f_ext)) OR
	print('{}-{}{}'.format(f_num,f_title,f_ext))