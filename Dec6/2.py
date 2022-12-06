# Objectives
# We have a long signal code and we need to detect when a 14 letters are unique.
# example: qwewtytyuio in here there is ewty is unuqiue in each of its charachters

# Tasks
# Seperate the code charachters into a list.
# Make a funtion that will detect the 14 charachters.
# The function should not start detecting until we pass the first 13 charachters from the list.
# The before 13 Charachters shoudl be saved in a list
# If the detection is a fail, the before charachter list shoudl be updated

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

    # number of previews Char to check for unquiness
    howManypreviewsChars = 13

    # list that will save the previews 3 charachters
    previewsChar = []

    # to know how many steps we took to get to the unique char
    countSteps = 0

    # reading the file
    f = open(os.path.join(dirname,"2.txt"), "r")
    lines = f.readlines()

    # looping through all lines
    for line in lines:

        line = line.rstrip()
        # print(line)

        charList = wrap(line,1)
        for char in charList:
            countSteps += 1
            if(len(previewsChar) == howManypreviewsChars):
                print("checking...")
                check = CheckForUniqueCode(previewsChar,char)
                if(check):
                    print("")
                    print("Positive case")
                    print(countSteps)
                    break
                else:
                    print("Negative")
                    previewsChar = previewsChar[1:]
                    previewsChar.append(char) 
            else:
                previewsChar.append(char)
                print("not yet")

    f.close()

    
# checking if all the items in Plist and char are all unique from each other
def CheckForUniqueCode(Plist, char):

    for i in range(len(Plist)):
        for j in range(i):
            if(Plist[i] == Plist[j]):
                return False
        if(Plist[i] == char):
            return False
    
    return True



init()