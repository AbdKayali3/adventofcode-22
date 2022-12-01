import os
import glob

dirname = os.path.dirname(__file__)
print (os.getcwd())
print (dirname)
print (os.path.join(os.getcwd(), 'test'))
print (__file__)



# max to hold the max number for all groups
#temp to hold the adition for each group
max = 0
temp = 0

f = open(os.path.join(dirname,"1.txt"), "r")

lines = f.readlines()

# looping through all lines
for line in lines:

    # to detect when we start the data for new group (new line)
    if line.strip() == "":
        # empty line. The end if the group. Change the max if needed
        if max < temp:
            max = temp
        temp = 0
    else:
        # not empty line. keep adding to temp
        temp += int(line)
        
f.close()

print(max)