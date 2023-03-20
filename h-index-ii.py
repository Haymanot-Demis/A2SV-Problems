class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def isFeasible(hindex):
            left_pos = bisect_left(citations, hindex)
            if len(citations) - left_pos >= hindex:
                return 1
            else:
                return -1

        low = 0
        high = min(len(citations), max(citations))
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            res = isFeasible(mid)
            if res == 1:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans