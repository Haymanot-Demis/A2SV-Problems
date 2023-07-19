class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curr = [intervals[0][0], intervals[0][1]]
        delete_count = 0
        for st, end in intervals[1:]:
            if st < curr[1]:
                if end < curr[1]:
                    curr = [st, end]
                delete_count += 1
            else:
                curr = [st, end]
        return delete_count