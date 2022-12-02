# ruls...
#  There choices: A for Rock, B for Paper, and C for Scissors.
#  Your choices: X for Rock, Y for Paper, and Z for Scissors.

# X = A, B = Y, C = Z
# A > B,C. B > C

# Rock 1
# paper 2
# Scissors 3

import os
import glob

dirname = os.path.dirname(__file__)
print (os.getcwd())
print (dirname)
print (os.path.join(os.getcwd(), 'test'))
print (__file__)


# convert the play type to a number
# A,B,C for first player (type 0)
# X,Y,Z for second player (type 1)
# @type to differ between player 1 and 2
# @choive  is the letter itself
# @retrun the number that is equal to the choice 
def toNumbers(type, choice):
    typeArray = [
        ["A", "B", "C"],
        ["X", "Y", "Z"]
    ]
    if(typeArray[type][0] == choice):
        return 1
    if(typeArray[type][1] == choice):
        return 2
    if(typeArray[type][2] == choice):
        return 3




# calculate if you win or lost or we are havign a draw
# 0 for losing
# 3 for a draw
# 6 for a winning
# @p1 the first player (them)
# @p2 the second player (you)
# @return the result as a number 
def play(p1,p2):
    if (p2 == 3 and p1 == 1):
        print("sepcial lose")
        return 0
    if (p1 < p2):
        return 6
    if (p1 == p2 ):
        return 3
    if (p2 == 1 and p1 == 3):
        print("sepcial win")
        return 6
    return 0


def readFile():

    # to hold the total of the result for each round
    total = 0


    # reading the file
    f = open(os.path.join(dirname,"1.txt"), "r")

    lines = f.readlines()

    # looping through all lines
    for line in lines:
        charachters = line.split(" ")
        # line = line = line.replace(" ", "")
        print(charachters)
        charachters[1] = charachters[1].strip("\n")
        playerOne = toNumbers(0, charachters[0])
        playerTwo = toNumbers(1, charachters[1])

        Result = play(playerOne,playerTwo)

        # for diagnosing purposes
        print("ssssssss")
        print(playerTwo)
        print(str(playerTwo) + str(Result))
        
        total += playerTwo + Result
    f.close()

    print("total is:")
    print(total)



# to init the program
readFile()




# # testing toNumbers() function
# print("A is:" + str(toNumbers(0,"A")))
# print("X is:" + str(toNumbers(1,"X")))
# print("B is:" + str(toNumbers(0,"B")))
# print("Y is:" + str(toNumbers(1,"Y")))
# print("C is:" + str(toNumbers(0,"C")))
# print("Z is:" + str(toNumbers(1,"Z")))


# testing play()
# print("Rock, Paper. win is:" + str(play(1,2)))
# print("Paper, Scissor. win is:" + str(play(2,3)))
# print("Scissor, Rock. win is:" + str(play(3,1)))
#---
# print("Rock, Rock. draw is:" + str(play(1,1)))
# print("Paper, Paper. draw is:" + str(play(2,2)))
# print("Scissor, Scissor. draw is:" + str(play(3,3)))
#---
# print("Paper, Rock. lose is:" + str(play(2,1)))
# print("Scissor, Paper. lose is:" + str(play(3,2)))
# print("Rock, Scissor. lose is:" + str(play(1,3)))