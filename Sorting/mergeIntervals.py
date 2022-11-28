class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        return self.mergeInterval(intervals, 0)
    
    def mergeInterval(self, intervals, start):
        if start < len(intervals) - 1:
            if intervals[start][1] >= intervals[start + 1][0]:
                intervals[start] = [intervals[start][0], intervals[start + 1][1]]
                intervals.pop(start + 1)
                return self.mergeInterval(intervals, start)
            else:
                return self.mergeInterval(intervals, start + 1)
        else:
            return intervals
                  

mySolution = Solution()
merged = mySolution.merge([[0, 2],[1,3],[2,6],[7,8],[8,10],[15,18],[19, 20],[19,22]])
print(merged)