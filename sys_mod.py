import sys

sys.stderr.write('this is error\n')
sys.stderr.flush()
sys.stdout.write("This is out\n")

print(sys.argv)  # location of the current file, all arguments passed

print(sys.version)
print(sys.copyright)
print(sys.executable)
print(sys.builtin_module_names)   # 
print(sys.modules)  # o/p as dictionary
print('time' in sys.modules)