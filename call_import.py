#! /usr/bin/python3

import import_corey as ic
# from import_corey import find_index as fi
# from import_corey import *  # not good approach, not sure what was imported

import sys
print(sys.path)

my_list = ["Math","Eng","Science", "SocialStudies"]
target = ic.find_index(my_list,"Math")
print(target)

print(ic.find_index.__doc__)

print (ic.find_index("Anika","i"))

import random
print(random.choice(my_list))

import math

print (math.sin(math.radians(90)))

import datetime, calendar

today = datetime.date.today()
print("Today is",today)

print(calendar.isleap(2020))

import os # gives access underlying os
print(os.getcwd())

os.chdir('/Users/arathi02/Documents')
print(os.getcwd())
print(os.__file__)  # location of the module on the os

#import antigravity


import requests
import json

r = requests.open("https://xkcd.com/353/")
r.json.loads()




