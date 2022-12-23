class Solution(object):
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        sortedPoints = sorted(points, key = lambda vector : vector[0]**2 + vector[1]**2)
        return sortedPoints[:k]
    

mySolution = Solution()
print(mySolution.kClosest([[3,3],[5,-1],[-2,4]], 2))