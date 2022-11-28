# 40min
import math
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        k_closest = []
        for vector in points:
            if len(k_closest) < k:
                k_closest.append(vector)
            else:
                i = len(k_closest) - 1
                while i >= 0 and self.dis(vector) < self.dis(k_closest[i]):
                    print(self.dis(vector), self.dis(k_closest[i]))
                    i -= 1
                    if i == len(k_closest) - 1:
                        continue
                    else:
                        k_closest[i + 1] = k_closest[i]
                k_closest[i + 1] = vector
        print(k_closest)
        return k_closest

    def dis(self, arr):
        return "{:.2f}".format(math.sqrt(arr[0]*arr[0] + arr[1]*arr[1]))
    

mySolution = Solution()
mySolution.kClosest([[3,3],[5,-1],[-2,4]], 2)
