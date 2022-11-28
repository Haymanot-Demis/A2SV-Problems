import math

# time = 7
#rectangular shape with the size n × m meters
# Each flagstone is of the size a × a.
# return number of flag stones to cover the rectangular theatre
class Solution:
    def numberOfFlagStones(self, m, n, a):
        return math.ceil(m/a) * math.ceil(n/a)

mySolution = Solution()
print(mySolution.numberOfFlagStones(6,10,4))