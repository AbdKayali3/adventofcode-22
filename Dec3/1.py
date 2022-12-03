# Objectives
# we have a set of charachters in each line, these charachters are made of 2 subsets combined. 
# Each subset has the same amount of charachters. 
# So if the main set is32 characher, your subsets will be 16 chrachter each.
# You have to combare between the 2 subsets and get the letter that is in both subset (there is only one) (It's Case sensative)
# After finind the charachter, You have to translate that into a number that is givien for each charachter.
# in the end, you combine those numbers to get a final output.

# Tasks
# Make the "convert char to number" list
# Get the sets from seperarte lines
# Devide the set into seperate even subset
# Compare function that loop through the subsets to check and mathc a char
# Convert the char to number
# Combine the output into a total

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

    # reading the file
    f = open(os.path.join(dirname,"1.txt"), "r")
    lines = f.readlines()

    # looping through all lines
    for line in lines:


        line = line.rstrip()
        lineLength = len(line)
        print(lineLength)
        print(line)

        subsets = [line[:int(lineLength/2)], line[int(lineLength/2):]]
        print(subsets)



        print("")

        temp = checkMatch(subsets[0],subsets[1])
        charFound.append(temp)

        print(temp)

        print("")

    f.close()



    for char in charFound:
        print ("")
        result = charNumber.index(char)
        print(char + " --> " + str(result))
        total += result



    print("")
    print(charFound)
    print("")
    print("Result is: " + str(total))





# checking for the match
def checkMatch(subset1,subset2):

    s = wrap(subset1,1)
    print(s)

    for char in s:
        # print(subset2.find(char))
        print(subset2 + " check for " + char)
        print("cehcking")
        check = subset2.find(char)
        if(check > -1):
            return char


init()