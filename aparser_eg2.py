# import math


# def volume(radius,height):
# 	vol = (math.pi) * (radius **2 ) * (height)
# 	return vol


# if __name__ == '__main__':
# 	print(volume(2,4))


#Using Argparse

import math
import argparse

parser = argparse.ArgumentParser(description = "Parser for Radius and Height")

# Postional Argument
# parser.add_argument("radius", type=int, help = "Enter Radius")
# parser.add_argument("height", type=int, help = "Enter Height")

# Optional Argument
# parser.add_argument("-r","--radius", type=int, help = "Enter Radius")
# parser.add_argument("-H", "--height", type=int, help = "Enter Height")

# usage: aparser_eg2.py [-h] [-r RADIUS] [-H HEIGHT]

# Parser for Radius and Height

# optional arguments:
#   -h, --help            show this help message and exit
#   -r RADIUS, --radius RADIUS
#                         Enter Radius
#   -H HEIGHT, --height HEIGHT
#                         Enter Height

parser.add_argument("-r","--radius", type=int, metavar="",required=True,help = "Enter Radius")
parser.add_argument("-H", "--height", type=int, metavar="",required=True,help = "Enter Height")

# optional arguments:
#   -h, --help      show this help message and exit
#   -r , --radius   Enter Radius
#   -H , --height   Enter Height

args = parser.parse_args()

print(args.radius)
print(args.height)

radius = int(args.radius)

def volume(radius,height):
	vol = (math.pi) * (radius **2 ) * (height)
	return vol

if __name__ == '__main__':
	print(volume(2,4))


















