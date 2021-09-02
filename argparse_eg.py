#Program takes 3 inputs, 1st no, 2nd no and Operation and return result

import argparse

'''Program takes 3 inputs, 1st no, 2nd no and Operation and return result'''

#if __name__ == '__main__':
parser = argparse.ArgumentParser(description = "A Calculator")

#Positional Argument
parser.add_argument("number1", help="First No")
parser.add_argument("number2", help="Second No")
parser.add_argument("operation", help="Type of Operation-ADD or +, SUB or -, MULTIPLY, DIVIDE", \
	choices = ["ADD","+","SUB","-","MULTIPLY","*","divide","/"])

#Optional Argument
# parser.add_argument("--number1", help="First No")
# parser.add_argument("--number2", help="Second No")
# parser.add_argument("--operation", help="Type of Operation-ADD or +, SUB or -, MULTIPLY, DIVIDE")
args = parser.parse_args()
print (args.number1)
print(args.number2)
print(args.operation)

n1 =int(args.number1)
n2 = int(args.number2)

if args.operation == "+" or args.operation == "ADD" :
	res = n1 + n2
	print (res)
elif args.operation == "-" or args.operation == "SUB" :
	res = n1 - n2
	print (res)
elif args.operation == "*" or args.operation == "MULTIPLY" :
	res = n1 * n2
	print (res)
elif args.operation == "%" or args.operation == "DIVIDE" :
	res = n1 / n2
	print (res)


