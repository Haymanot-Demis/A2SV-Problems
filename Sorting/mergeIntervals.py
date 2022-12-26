class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda interval : interval[0])
        return self.mergeInterval(intervals, 0)
    
    def mergeInterval(self, intervals, start):
        if start < len(intervals) - 1:
            if intervals[start][1] >= intervals[start + 1][0]:
                intervals[start] = [intervals[start][0], max(intervals[start][1], intervals[start + 1][1])]
                intervals.pop(start + 1)
                return self.mergeInterval(intervals, start)
            else:
                return self.mergeInterval(intervals, start + 1)
        else:
            return intervals            