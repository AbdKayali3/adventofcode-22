import os
import glob

dirname = os.path.dirname(__file__)
print (os.getcwd())
print (dirname)
print (os.path.join(os.getcwd(), 'test'))
print (__file__)

f = open(os.path.join(dirname,"1.txt"), "r")

max = 0
temp = 0

# line = ""
lines = f.readlines()
for line in lines:
    if line.strip() == "":
        # empty
        if max < temp:
            max = temp
        temp = 0
    else:
        temp += int(line)
print(max)
f.close()