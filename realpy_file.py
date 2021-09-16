# Reading multiple files
import fileinput
import sys

files = fileinput.input()
for line in files:
    if fileinput.isfirstline():
        print(f'\n--- Reading {fileinput.filename()} ---')
    print(' -> ' + line, end='')
print()
# dir listing

import os

entries = os.scandir(".")
print(entries)

for entry in entries:
	print(entry.name)

#OR
from pathlib import Path

entries = Path(".")
for entry in entries.iterdir():
	print(entry)

#list files and subdir
base_dir = "."
with os.scandir(base_dir) as entries:
	for entry in entries:
		if entry.is_file():
			print(entry.name)
		if entry.is_dir():
			print(entry.name)

# file attributes
with os.scandir(base_dir) as entries:
	for entry in entries:
		info_stat = entry.stat()
		print(info_stat.st_mtime)

# mkdir

#os.mkdir("anika") # only 1 depth
#os.rmdir("anika")
#os.makedirs("anika/rathi") #both anika and rathi created

#Filename Pattern Matching
# endswith() and startswith() string methods
# fnmatch.fnmatch()
# glob.glob()
# pathlib.Path.glob()

import os

# Get .txt files
print(os.getcwd())
os.chdir("/Users/arathi02/Documents")
print(os.getcwd())
for f_name in os.listdir('some_directory'):
	if f_name.endswith('.txt'):
		print(f_name)
		pass
#OR
import glob
os.chdir("/Users/arathi02/Documents/some_directory")
for name in glob.glob('*[0-9]*.txt'):
	print(name)


#Traversing Directories and Processing Files
for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}')
    for file_name in files:
        print(file_name)

# Delete files
data_file = 'home/data.txt'

# Use exception handling
try:
    os.remove(data_file)
except OSError as e:
    print(f'Error: {data_file} : {e.strerror}')

# delete empty dir
trash_dir = 'my_documents/bad_dir'

try:
    os.rmdir(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')

## delete dir tree
import shutil

trash_dir = 'my_documents/bad_dir'

try:
    shutil.rmtree(trash_dir)
except OSError as e:
    print(f'Error: {trash_dir} : {e.strerror}')

shutil.copy2(src, dst) #Using .copy2() preserves details about the file such as last access time, permission bits, last modification time, and flags
shutil.copytree('data_1', 'data1_backup')
shutil.move('dir_1/', 'backup/')
os.rename('first.zip', 'first_01.zip')


#zip file
import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
    zipobj.namelist()