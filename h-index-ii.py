class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def isFeasible(hindex):
            left_pos = bisect_left(citations, hindex)
            right_pos = bisect_right(citations, hindex)
            length = len(citations)
            while left_pos <= right_pos:
                mid = left_pos + (right_pos - left_pos) // 2
                if length - mid > hindex:
                    left_pos = mid + 1
                elif length - mid < hindex:
                    right_pos = mid - 1
                else:
                    return 0
                    
            if length - right_pos > hindex:
                return 1
            else:
                return -1

        low = 0
        high = min(len(citations), max(citations))
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            res = isFeasible(mid)
            if res == 0:
                ans = mid
                high = mid - 1
            elif res == - 1:
                high = mid - 1
            else:
                low = mid + 1
        return ans