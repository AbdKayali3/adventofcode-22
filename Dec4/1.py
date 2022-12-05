# Objectives
# we have a pair of set of numbers and we have to find the fully overlaping between the two sets. 
# THat is when a set will have the wholw otherset inside it 
# Example 12345678 is a set that fully contain 3456 inside it

# Tasks
# Split the line to two strings
# Split each string into a list
# Compare the sets
# Count the positive cases

import os
import glob
from textwrap import wrap
import time

dirname = os.path.dirname(__file__)
print (os.getcwd())
print (dirname)
print (os.path.join(os.getcwd(), 'test'))
print (__file__)

def init():
    print("init")

    # reading the file
    f = open(os.path.join(dirname,"2.txt"), "r")
    lines = f.readlines()

    # looping through all lines
    for line in lines:

        print(line)

    f.close()




init()