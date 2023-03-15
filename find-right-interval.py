class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def binarySearch(array, val, start):
            left = start
            right = len(array) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2
                if array[mid][1][0] >= val:
                    ans = array[mid][0]
                    right = mid - 1
                elif  array[mid][1][0] < val:
                    left = mid  + 1

            return ans
        
        intervals = list(enumerate(intervals))
        intervals.sort(key=lambda x : x[1][0])
        answer = [-1] * len(intervals)
        for i, interval in enumerate(intervals):
            if interval[1][0] != interval[1][1]:
                answer[interval[0]] = binarySearch(intervals, interval[1][1], i + 1)
            else:
                answer[interval[0]] = interval[0]
        return answer