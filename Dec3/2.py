# Objectives
# we should group each 3 lines together and search for a 1 charachter that are in the three lines
# we should found that for all groups.
# Then convert them to a number accourding to the CharToNumber we already have

# Tasks
# make a function that group each three lines together
# make a function that compare letters for these three lines and get the common letter
# convert those letters to numbers
# combine those numbers in totoal

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

    total = 0
    charNumber = ["0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                      "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    charFound = []

    group = []
    groupCount = 0

    # reading the file
    f = open(os.path.join(dirname,"2.txt"), "r")
    lines = f.readlines()

    # looping through all lines
    for line in lines:


        line = line.rstrip()
        lineLength = len(line)
        print(lineLength)
        print(line)

        # group each three lines together in a list then perform some proccess on them
        if(groupCount == 2):
            groupCount += 1
            group.append(line)

            print("")

            # the main process
            temp = checkGroupMatch(group)
            charFound.append(temp)

            print(temp)

            print("")

            groupCount = 0
            group = []
        else:
            groupCount += 1
            group.append(line)

    f.close()


    # looping throw all charachters found and convert them to numbers
    # then combining them in total
    for char in charFound:
        print ("")
        result = charNumber.index(char)
        print(char + " --> " + str(result))
        total += result



    print("")
    print(charFound)
    print("")
    print("Result is: " + str(total))



# checking for a match between 3 sets
def checkGroupMatch(group):
    s = wrap(group[0],1)
    print(s)

    for char in s:

        print(group[1] + " check for " + char)
        print("cehcking")
        check = group[1].find(char)
        if(check > -1):
            print(group[2] + " check for " + char)
            print("cehcking")
            check2 = group[2].find(char)
            if(check2 > -1):
                return char


init()