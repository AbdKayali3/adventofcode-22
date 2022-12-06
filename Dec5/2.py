# Objectives
# We have a bunc of containers in 9 spots.
# we have a list of movment to do.
# after we do all movments get the last container in each spot

# Tasks
# Construct the list of containers as the shape below
# decode the movment to a list
# make a fucntion to perform the movments
# loop throw all containers spots and combine the last itme of them

# containers shape
# [M]                     [N] [Z]    
# [F]             [R] [Z] [C] [C]    
# [C]     [V]     [L] [N] [G] [V]    
# [W]     [L]     [T] [H] [V] [F] [H]
# [T]     [T] [W] [F] [B] [P] [J] [L]
# [D] [L] [H] [J] [C] [G] [S] [R] [M]
# [L] [B] [C] [P] [S] [D] [M] [Q] [P]
# [B] [N] [J] [S] [Z] [W] [F] [W] [R]
#  1   2   3   4   5   6   7   8   9 

# test containers shape
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 



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

    containersHolder = [
        ["",""],
        ["B", "L", "D", "T", "W", "C", "F", "M"],
        ["N", "B", "L"],
        ["J", "C", "H", "T", "L", "V"],
        ["S", "P", "J", "W"],
        ["Z", "S", "C", "F", "T", "L", "R"],
        ["W", "D", "G", "B", "H", "N", "Z"],
        ["F", "M", "S", "P", "V", "G", "C", "N"],
        ["W", "Q", "R", "J", "F", "V", "C", "Z"],
        ["R", "P", "M", "L", "H"],
    ]

    containersHolderTest = [
        ["",""],
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"],
    ]

    # to flip between different container lists without changing anything in the code itself
    currentContainerOnUse = containersHolderTest

    # reading the file
    f = open(os.path.join(dirname,"2_test.txt"), "r")
    lines = f.readlines()


    # looping through all lines
    for line in lines:

        line = line.rstrip()
        print(line)

        # detect the movment
        movment = line.split(" ")
        print(movment)

        print ("")
        print ("perform movment now...")
        print ("")


        # perform the movments
        tempMove = moveContainer(currentContainerOnUse, int(movment[1]), int(movment[3]), int(movment[5]))
        print(tempMove)


        



        


    f.close()


    print("")
    print("")
    print(currentContainerOnUse)


    output = getLastContainerFromEachSpot(currentContainerOnUse)

    print("")
    print ("Calculating output now...")
    print ("")
    print(output)





# perform the movment
def moveContainer(Clist, steps, Cfrom, Cto):
    

    tempHolder = []
    for step in range(steps):

        temp = Clist[Cfrom][len(Clist[Cfrom])-1]
        del Clist[Cfrom][len(Clist[Cfrom])-1]
        tempHolder.append(temp)


    for item in tempHolder:
        Clist[Cto].append(item)

    


    return "moving containers from spot " + str(Cfrom) + " to spot " + str(Cto) + ", " + str(steps) + " time"

# get the last item from each spot and combien then in a string
def getLastContainerFromEachSpot(Clist):
    output = ""

    print(Clist)
    for spot in Clist:
        output += str(spot[len(spot)-1])

    return output



init()