marks = [75, 94, 75, 80, 85]

def find_avg(marks):
	avg = sum(marks)/len(marks)
	print ("The Average is", avg)
	return avg

avg = find_avg(marks)

def find_grade(avg):
	if avg>=80:
		grade = "A"
	elif avg >=60:
		grade = "B"
	elif avg >=50:
		grade = "C"
	else:
		grade = "D"
	return grade

grade = find_grade(avg)
print("The grade is", grade)

# lambda function

double = lambda x: x*2
print ("The double is", double(4))

xlist = [2,5,7,8,9,3,78,98,67]

even = list(filter(lambda x : (x%2==0), xlist))

print(even)
