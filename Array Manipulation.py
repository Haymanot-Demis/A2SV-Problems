
#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    array = [0.0] * n
    for start, end, increment in queries:
        array[start] += increment
        if end + 1 < n:
            array[end + 1] -= increment
    
    for indx in range(1, n):
        array[indx] += array[indx - 1]
    return int(max(array))