class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        curr = [points[0][0], points[0][1]]
        non_overlaps = 1
        for st, end in points[1:]:
            if st <= curr[1]:
                if end < curr[1]:
                    curr = [st, end] 
            else:
                curr = [st, end]
                non_overlaps += 1
        return non_overlaps