#Write a Python program to read an entire text file.

in_file = open("read.txt")
print(in_file.read())

#Write a Python program to read first n lines of a file.

def read_nlines(file_name,nlines):
  from itertools import islice 
  with open(file_name) as f:
    for line in islice(f, nlines):
      print(line)

read_nlines("read.txt",4)


#Write a Python program to append text to a file and display the text.

def append_text(f):
  #from itertools import islice
  with open(f, "a+") as fo:
    fo.write("another line\n")
    fo.write("last line\n")
  #txt = open(f)
    print(fo.name,"-",fo.mode) 
    print ("Name of the file: ", fo.name)
    print ("Closed or not : ", fo.closed)
    print ("Opening mode : ", fo.mode)
    #print ("Softspace flag : ", fo.softspace)

    # Check current position
    position = fo.tell()
    print ("Current file position : ", position)

    position = fo.seek(0, 0)
    print(position)
    print(fo.read())


append_text("read.txt") 

#Write a Python program to read last line of a file.

with open('read.txt', 'r') as f:
  last_line = f.readlines()[-1]
  print("".join(last_line))