# Objectives
# We have a long signal code and we need to detect when a 4 letters are unique.
# example: qwewtytyuio in here there is ewty is unuqiue in each of its charachters

# Tasks
# Seperate the code charachters into a list.
# Make a funtion that will detect the 4 charachters.
# The function should not start detecting until we pass the first 3 charachters from the list.
# The before 3 Charachters shoudl be saved in a list
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

    # list that will save the previews 3 charachters
    previews3Char = []

    # to know how many steps we took to get to the unique char
    countSteps = 0

    # reading the file
    f = open(os.path.join(dirname,"1.txt"), "r")
    lines = f.readlines()

    # looping through all lines
    for line in lines:

        line = line.rstrip()
        # print(line)

        charList = wrap(line,1)
        for char in charList:
            countSteps += 1
            if(len(previews3Char) == 3):
                print("checking...")
                check = CheckForUniqueCode(previews3Char,char)
                if(check):
                    print("")
                    print("Positive case")
                    print(countSteps)
                    break
                else:
                    print("Negative")
                    previews3Char = previews3Char[1:]
                    previews3Char.append(char) 
            else:
                previews3Char.append(char)
                print("not yet")

    f.close()


# IMPORTANT: old and deprecated and for manual testing only
# checking if the 3 cahr in the Plist and the char all are unique from each other
def CheckForUniqueCode_(Plist, char):
    if((Plist[0] != Plist[1]) and (Plist[0] != Plist[2]) and (Plist[1] != Plist[2])):
        if((char != Plist[0]) and (char != Plist[1]) and (char != Plist[2])):
            return True
    
    return False
    
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