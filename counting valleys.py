#!/bin/python3
#time = 7
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    seaLevel = 0
    countValleys = 0
    for i in range(steps):
        if path[i] == 'U':
            seaLevel += 1
        else:
            if seaLevel == 0:
                countValleys += 1
            seaLevel -= 1
    return countValleys

print(countingValleys(len("UDDDUDUUUUDDDDUU"), "UDDDUDUUUUDDDDUU"))
        
