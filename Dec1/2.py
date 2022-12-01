import os
import glob

dirname = os.path.dirname(__file__)
print (os.getcwd())
print (dirname)
print (os.path.join(os.getcwd(), 'test'))
print (__file__)



# groupedList to hold in it all groups calories groupe by group
# temp to hold the adition for each group
temp = 0
groupedList = []


f = open(os.path.join(dirname,"2.txt"), "r")

lines = f.readlines()

# looping through all lines
for line in lines:

    # to detect when we start the data for new group (new line)
    if line.strip() == "":
        # empty line. The end if the group. Change the max if needed
        groupedList.append(temp)
        temp = 0
    else:
        # not empty line. keep adding to temp
        temp += int(line)

f.close()


# sorting the list to get the max 3
groupedList.sort()
length = len(groupedList)

print(groupedList[-1] + groupedList[-2] + groupedList[-3])