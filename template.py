# Objectives
# 

# Tasks
# 

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

        line = line.rstrip()
        print(line)

    f.close()




init()