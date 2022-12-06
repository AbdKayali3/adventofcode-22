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
#     [H]         [H]         [V]    
#     [V]         [V] [J]     [F] [F]
#     [S] [L]     [M] [B]     [L] [J]
#     [C] [N] [B] [W] [D]     [D] [M]
# [G] [L] [M] [S] [S] [C]     [T] [V]
# [P] [B] [B] [P] [Q] [S] [L] [H] [B]
# [N] [J] [D] [V] [C] [Q] [Q] [M] [P]
# [R] [T] [T] [R] [G] [W] [F] [W] [L]
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
        ["R", "N", "P", "G"],
        ["T", "J", "B", "L", "C", "S", "V", "H"],
        ["T", "D", "B", "M", "N", "L"],
        ["R", "V", "P", "S", "B"],
        ["G", "C", "Q", "S", "W", "M", "V", "H"],
        ["W", "Q", "S", "C", "D", "B", "J"],
        ["F", "Q", "L"],
        ["W", "M", "H", "T", "D", "L", "F", "V"],
        ["L", "P", "B", "V", "M", "J", "F"],
    ]

    containersHolderTest = [
        ["",""],
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"],
    ]

    # to flip between different container lists without changing anything in the code itself
    currentContainerOnUse = containersHolder

    # reading the file
    f = open(os.path.join(dirname,"1.txt"), "r")
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

    for step in range(steps):
        temp = Clist[Cfrom][len(Clist[Cfrom])-1]
        del Clist[Cfrom][-1]
        Clist[Cto].append(temp)


    return "moving containers from spot " + str(Cfrom) + " to spot" + str(Cto) + ", " + str(steps) + "time"

# get the last item from each spot and combien then in a string
def getLastContainerFromEachSpot(Clist):
    output = ""

    print(Clist)
    for spot in Clist:
        output += str(spot[len(spot)-1])

    return output



init()