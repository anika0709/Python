import subprocess

#subprocess.run('ls -a',shell=True) # shell= True can be security hazard
p1 = subprocess.run(['ls','-la'], stdout = subprocess.PIPE, text = True)
print (p1.stdout)
print(p1.args, p1.returncode) #returns 0

# #Print output to a file
# with open('output.txt','w') as f:
# 	p1 = subprocess.run(['ls','-la'], stdout = f, text = True)

p1 = subprocess.run(['ls','ANIKA'], capture_output=True, text = True)  #non-zero return code , no output
print(p1.returncode)  #returns 1
print(p1.stderr)

#p1 = subprocess.run(['ls','ANIKA'], capture_output=True, text = True, check=True)  #output Traceback

p1 = subprocess.run(['ls','ANIKA'], stderr = subprocess.DEVNULL) 

p1 = subprocess.run(['cat','test.txt'], capture_output=True)
print(p1.stdout.decode()) 

p2 = subprocess.run(['grep','-n', 'test'], capture_output=True, text = True, input=p1.stdout.decode())
print(p2.stdout) 




