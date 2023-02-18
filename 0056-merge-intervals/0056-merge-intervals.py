class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        right = 1
        length = len(intervals)
        intervals.sort(key=lambda x : x[0])
        merged_intervals = [intervals[0]]

        while right < length:
            if merged_intervals[-1][1] >= intervals[right][0]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1] ,intervals[right][1])
            else: 
                merged_intervals.append(intervals[right])
            right += 1
        return merged_intervals
                
                  